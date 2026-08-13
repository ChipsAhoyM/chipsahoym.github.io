# Minggui Teng's Personal Website

Personal academic website built with Jekyll, based on the [al-folio](https://github.com/alshedivat/al-folio) theme.

**Live site:** [https://tengminggui.cn](https://tengminggui.cn)

## Features

- Publications with BibTeX support (data in `_bibliography/papers.bib`)
- News feed on the homepage (posts in `_news/`)
- Photo gallery with fullscreen viewer
- Dark mode, responsive design
- Third-party CSS/JS/fonts are self-hosted under `assets/vendor/` and `assets/fonts/`
  (no CDN dependencies, works well from mainland China)

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

## Content

- **Publications**: edit `_bibliography/papers.bib`; `selected=true` entries appear on the homepage.
- **News**: add a Markdown file to `_news/` with `date`, `display_date` and `title` front matter.
- **Experiences / Services**: edit `_data/experiences.json` and `_data/services.json`.
- **Gallery**: add the full-size image to `assets/gallery/` and register it in
  `assets/gallery-images.js`. Exif metadata (including GPS) is stripped from the
  published images; keep originals out of this repo.
- **Photos**: for web use, images are kept at ≤2400px longest edge, JPEG quality ~88.

## License

MIT License - Based on [al-folio](https://github.com/alshedivat/al-folio) theme.
