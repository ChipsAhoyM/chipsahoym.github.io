#!/usr/bin/env python3
"""Sync missing bibliographic metadata into _bibliography/papers.bib.

Supports two sources:

  --source dblp      (default, works on GitHub Actions): resolve the DBLP author
                     profile by name + publication overlap, then merge missing
                     fields (volume / number / pages / publisher / doi) into the
                     entries of papers.bib. Never overwrites existing values and
                     never touches custom fields (pdf, code, thumbnail, ...).

  --source crossref  (fallback for offline use): query the Crossref REST API per
                     entry by title, merge missing volume/issue/pages/publisher/doi.

Usage:
  python3 .github/scripts/sync_bib.py                 # dblp, dry-run
  python3 .github/scripts/sync_bib.py --apply         # dblp, write changes
  python3 .github/scripts/sync_bib.py --source crossref --apply

Exit code 0 when nothing changed, 1 when papers.bib was updated (or an error).
"""

import argparse
import difflib
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BIB = REPO / "_bibliography" / "papers.bib"
CONFIG = REPO / "_config.yml"

UA = {"User-Agent": "website-bib-sync/1.0 (mailto:minggui_teng@pku.edu.cn)"}

ENTRY_RE = re.compile(r"@(?P<type>\w+)\s*\{\s*(?P<key>[^,\s]+)\s*,")


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def fetch_json(url):
    return json.loads(fetch(url))


def norm_title(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def parse_bib():
    """Return list of (entry_text, fields_dict, key) for each entry in order."""
    text = BIB.read_text(encoding="utf-8")
    entries = []
    # split into entries by lines that start with @ (skip @STRING)
    parts = re.split(r"(?m)^(@)", text)
    current = ""
    for i, p in enumerate(parts):
        if p == "@" and i + 1 < len(parts):
            if current.strip() and not current.lstrip().startswith("@STRING"):
                entries.append(current)
            current = "@" + parts[i + 1]
        elif p == "@":
            continue
    # simpler robust approach: split on newline-@
    entries = []
    strings = []  # @STRING macro definitions must be preserved verbatim
    for chunk in re.split(r"\n(?=@)", text):
        chunk = chunk.strip()
        if not chunk:
            continue
        if chunk.startswith("@STRING"):
            strings.append(chunk)
            continue
        entries.append(chunk)
    parsed = []
    for chunk in entries:
        m = ENTRY_RE.search(chunk)
        key = m.group("key") if m else "?"
        fields = {}
        for fm in re.finditer(r"^\s*([A-Za-z0-9_]+)\s*=\s*\{([^{}]*)\}\s*,?\s*$", chunk, re.M):
            fields[fm.group(1).lower()] = fm.group(2).strip()
        for fm in re.finditer(r"^\s*([A-Za-z0-9_]+)\s*=\s*([A-Za-z0-9_]+)\s*,?\s*$", chunk, re.M):
            if fm.group(1).lower() not in fields:
                fields[fm.group(1).lower()] = fm.group(2).strip()
        parsed.append({"chunk": chunk, "fields": fields, "key": key})
    return parsed, strings


def dblp_author_candidates():
    url = ("https://dblp.org/search/author/api?q="
           + urllib.parse.quote("Minggui Teng") + "&format=json")
    data = fetch_json(url)
    hits = data.get("result", {}).get("hits", {}).get("hit", [])
    out = []
    for h in hits:
        info = h.get("info", {})
        name = info.get("author", "")
        if "Teng" not in name and "Minggui" not in name:
            continue
        out.append({
            "name": name,
            "url": info.get("url", ""),
            "notes": info.get("notes", ""),
        })
    return out


def dblp_pid_from_url(url):
    m = re.search(r"/pid/[^/]+/[^/]+", url)
    return m.group(0) if m else None


def dblp_publications(pid):
    xml_text = fetch(f"https://dblp.org{pid}.xml", timeout=60)
    root = ET.fromstring(xml_text)
    pubs = []
    for child in root:
        tag = child.tag
        if tag in ("article", "inproceedings", "proceedings", "incollection"):
            title = child.findtext("title", default="")
            def sub(tag_, k):
                e = child.find(f"{tag_}/{k}")
                return e.text.strip() if e is not None and e.text else None
            pubs.append({
                "title": title,
                "year": child.findtext("year", default=None),
                "venue": child.findtext("booktitle") or child.findtext("journal"),
                "volume": child.findtext("volume"),
                "number": child.findtext("number"),
                "pages": child.findtext("pages"),
                "publisher": child.findtext("publisher"),
                "doi": child.findtext("ee"),
            })
    return pubs


def crossref_lookup(title):
    q = urllib.parse.quote(title)
    url = (f"https://api.crossref.org/works?rows=3"
           f"&query.bibliographic={q}&query.author=Teng+Minggui"
           f"&select=DOI,title,volume,issue,page,publisher")
    data = fetch_json(url)
    items = data.get("message", {}).get("items", [])
    best, best_score = None, 0.0
    want = norm_title(title)
    for it in items:
        titles = it.get("title") or [""]
        score = max(difflib.SequenceMatcher(None, want, norm_title(t)).ratio()
                    for t in titles)
        if score > best_score:
            best, best_score = it, score
    if best is None or best_score < 0.8:
        return None
    pages = best.get("page")
    if pages is None:
        art = best.get("article-number")
        pages = art if art else None
    doi = best.get("DOI")
    if doi:
        doi = doi.upper()  # DOIs are case-insensitive; canonical bib form is uppercase
    publisher = best.get("publisher") or ""
    pl = publisher.lower()
    if "springer" in pl:
        publisher = "Springer"
    elif "ieee" in pl:
        publisher = "IEEE"
    elif "neurips" in pl or "neural information" in pl:
        publisher = "NeurIPS"
    elif "artificial intelligence" in pl:
        publisher = "AAAI Press"
    return {
        "doi": doi,
        "volume": best.get("volume"),
        "number": best.get("issue"),
        "pages": pages,
        "publisher": publisher,
    }


def set_field(chunk, key, value, dry_run, changes):
    """Add or update a field in the entry text if missing/different."""
    pattern = re.compile(rf"^(\s*{key}\s*=\s*\{{)[^{{}}]*(\}}\s*,?\s*)$", re.M)
    m = pattern.search(chunk)
    if m:
        old = re.sub(r"[\s,{}]+", "", m.group(0).split("=", 1)[1])
        if old.strip() == value.strip():
            return chunk
        if not dry_run:
            changes.append((key, value))
        return chunk
    # field absent: insert after the key line (first line of entry)
    lines = chunk.splitlines()
    insert_at = 1
    indent = "  "
    lines.insert(insert_at, f"{indent}{key}={{{value}}},")
    if not dry_run:
        changes.append((key, value))
    return "\n".join(lines)


def run(source, dry_run, update_config):
    entries, strings = parse_bib()
    if not entries:
        print("No entries parsed from papers.bib")
        return 1

    sources = []
    if source in ("dblp", "auto"):
        try:
            cands = dblp_author_candidates()
        except Exception as e:
            print(f"DBLP author search failed: {e}")
            cands = []
        # pick the candidate whose publication titles overlap best with our bib
        our_titles = [norm_title(e["fields"].get("title", "")) for e in entries]
        best_pid, best_score = None, 0.0
        for cand in cands:
            pid = dblp_pid_from_url(cand["url"])
            if not pid:
                continue
            try:
                pubs = dblp_publications(pid)
            except Exception as e:
                print(f"DBLP pid {pid} fetch failed: {e}")
                continue
            overlap = sum(
                1 for p in pubs
                if any(difflib.SequenceMatcher(None, norm_title(p["title"]), t).ratio() >= 0.9
                       for t in our_titles))
            if overlap > best_score:
                best_score, best_pid = overlap, pid
        if best_pid:
            pubs = dblp_publications(best_pid)
            print(f"Resolved DBLP profile: https://dblp.org{best_pid} "
                  f"(overlap {best_score}/{len(entries)})")
            sources.append(("dblp", pubs))
            if update_config:
                _update_dblp_url(f"https://dblp.org{best_pid}")
        else:
            print("No matching DBLP profile found; skipping dblp source")

    if source in ("crossref", "auto") and not sources:
        sources.append(("crossref", None))

    if not sources:
        print("No usable source")
        return 1

    changed = []
    new_text_entries = []
    for entry in entries:
        chunk = entry["chunk"]
        f = entry["fields"]
        title = f.get("title", "")
        if not title:
            new_text_entries.append(chunk)
            continue
        want = norm_title(title)
        meta = None
        for kind, pubs in sources:
            if kind == "dblp":
                best = None
                for p in pubs:
                    score = difflib.SequenceMatcher(
                        None, norm_title(p["title"]), want).ratio()
                    if best is None or score > best[0]:
                        best = (score, p)
                if best and best[0] >= 0.9:
                    p = best[1]
                    doi = p.get("doi") or ""
                    m2 = re.search(r"10\.\d{4,9}/[^\s\"']+", doi)
                    doi = m2.group(0) if m2 else None
                    meta = {
                        "doi": doi,
                        "volume": p.get("volume"),
                        "number": p.get("number"),
                        "pages": p.get("pages"),
                        "publisher": p.get("publisher"),
                    }
                    break
            else:
                try:
                    meta = crossref_lookup(title)
                except Exception as e:
                    print(f"Crossref lookup failed for {title[:50]}: {e}")
                    meta = None
        if not meta:
            new_text_entries.append(chunk)
            continue
        for key, value in meta.items():
            if not value:
                continue
            if key in f and f[key]:
                continue  # never overwrite
            new = set_field(chunk, key, str(value), dry_run, changed)
            if new != chunk:
                print(f"  + {key} = {value}  <- {entry['key']}")
            chunk = new
        new_text_entries.append(chunk)

    if not dry_run and changed:
        output = "\n\n".join(strings + new_text_entries) + "\n"
        BIB.write_text(output, encoding="utf-8")
        print(f"papers.bib updated ({len(changed)} fields)")
    elif dry_run and changed:
        print(f"dry-run: {len(changed)} fields would be added")
    else:
        print("papers.bib is up to date")
    return 0


def _update_dblp_url(url):
    text = CONFIG.read_text(encoding="utf-8")
    if "dblp_url: " in text and "dblp.org" not in text.split("dblp_url:", 1)[1][:60]:
        new = re.sub(r"(dblp_url:\s*).*", rf"\1{url}  # your DBLP profile url", text)
        CONFIG.write_text(new, encoding="utf-8")
        print(f"Updated {CONFIG.name}: dblp_url = {url}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["dblp", "crossref", "auto"], default="auto")
    ap.add_argument("--apply", action="store_true", help="write changes (default is dry-run)")
    ap.add_argument("--update-config", action="store_true")
    args = ap.parse_args()
    rc = run(args.source, dry_run=not args.apply, update_config=args.update_config)
    sys.exit(rc)


if __name__ == "__main__":
    main()
