# Minggui Teng's Personal Website

Personal academic website built with Jekyll, based on the [al-folio](https://github.com/alshedivat/al-folio) theme.

**Live site:** [https://chipsahoym.github.io](https://chipsahoym.github.io)

## Features

- Publications with BibTeX support
- Photo gallery with fullscreen viewer
- Responsive design

## Local Development

```bash
bundle install
bundle exec jekyll serve
```

## Gallery

Add images to `assets/gallery/` and run:

```bash
python3 generate_thumbnails.py
```

Then update `assets/gallery-images.js` with image metadata.

## License

MIT License - Based on [al-folio](https://github.com/alshedivat/al-folio) theme.
