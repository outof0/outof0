# OutOf0 brand source

The files in this directory are the only retained brand source for the landing page.

- `tokens.css` and `tokens.json` — color, type, radius, and spacing tokens.
- `messaging.md` — approved organization copy.
- `landing-guide.md` — page structure and content direction.
- `logos/` — primary/reverse lockups, symbols, and wordmarks.
- `logos/readme-banner-light.svg` and `logos/readme-banner-dark.svg` — tight-cropped lockups
  for the GitHub organization profile README. Same artwork as the lockups, trimmed viewBox so
  the logo fills the width instead of sitting in the left half of an 860×180 canvas. Not used
  by the site, so they are not mirrored into `public/`.
- `favicon.svg` — favicon source.

Production-ready copies of assets used by Astro live in `public/`. Do not change the logo assets in `public/` without mirroring the relevant source asset here.
