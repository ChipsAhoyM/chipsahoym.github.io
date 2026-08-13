# Minggui Teng's Personal Website

Personal academic website built with Jekyll, based on the [al-folio](https://github.com/alshedivat/al-folio) theme.

**Live site:** [https://tengminggui.cn](https://tengminggui.cn)

## Features

- Publications with BibTeX support (data in `_bibliography/papers.bib`)
  and DOI links
- News feed on the homepage (posts in `_news/`)
- Print-friendly CV page at `/cv/` (generated from `_data/education.json`,
  `_data/experiences.json`, `_bibliography/papers.bib` and `_data/services.json`)
- Photo gallery with fullscreen viewer
- Dark mode, responsive design
- Open Graph / Twitter cards + JSON-LD Person structured data (Google Scholar,
  ORCID, Semantic Scholar, GitHub)
- Bootstrap 5 only (no MDB, no jQuery); all CSS/JS/fonts are self-hosted under
  `assets/vendor/` and `assets/fonts/` — no CDN dependencies, works well from
  mainland China. MathJax loads only on pages with `math: true` front matter.

## Local Development

Jekyll 4.4+ requires **Ruby 3.1 or newer** (macOS system Ruby 2.6 is too old).
Install a recent Ruby first, e.g.:

```bash
brew install ruby@3.2
export PATH="/opt/homebrew/opt/ruby@3.2/bin:$PATH"
```

Then:

```bash
bundle install
bundle exec jekyll serve
```

The site deploys automatically to GitHub Pages (custom domain `tengminggui.cn`)
via `.github/workflows/pages.yml` on every push to `main`.

## Automation

- `.github/workflows/sync-bibliography.yml` (monthly) fills missing
  volume/number/pages/publisher/doi in `papers.bib` from DBLP and opens a PR.
  Run it locally with `python3 .github/scripts/sync_bib.py --apply`
  (add `--source crossref` when dblp.org is unreachable).
- `.github/workflows/link-check.yml` (monthly) checks all links on the site and
  in the bibliography with [lychee](https://lychee.cli.rs/) (config in `lychee.toml`).
- `.github/dependabot.yml` keeps GitHub Actions and Ruby gems up to date.

## Content

- **Publications**: edit `_bibliography/papers.bib`; `selected=true` entries appear on the homepage.
  Add a `doi` field to get a "doi" link on the paper card.
- **News**: add a Markdown file to `_news/` with `date`, `display_date` and `title` front matter.
- **Experiences / Services**: edit `_data/experiences.json` and `_data/services.json`.
- **CV**: edit `_data/education.json`; the rest of the CV is generated automatically.
- **Gallery**: add the full-size image to `assets/gallery/` and register it in
  `assets/gallery-images.js`. Exif metadata (including GPS) is stripped from the
  published images; keep originals out of this repo.
- **Photos**: for web use, images are kept at ≤2400px longest edge, JPEG quality ~88.

## License

MIT License - Based on [al-folio](https://github.com/alshedivat/al-folio) theme.
