# Contributing

`README.md` is the public face of the OutOf0 organization — GitHub renders it on
[github.com/outof0](https://github.com/outof0). Treat it as a product page, not as developer
documentation. Repo setup, local development, and deployment belong here.

## What lives where

| Path | Purpose |
| --- | --- |
| `README.md` | Organization profile page. Audience: visitors. |
| `src/pages/index.astro` | The landing page, including its inline styles. |
| `brand/` | Brand source of truth — tokens, messaging, logo sources, page guide. |
| `public/` | Runtime assets the site actually serves. Mirrors the needed parts of `brand/`. |
| `docs/github-org-profile.md` | Settings that can only be changed in the GitHub UI (bio, repo descriptions, topics). |
| `.github/workflows/ci.yml` | Type check, build, and Cloudflare Pages deploy. |

## Local development

```bash
pnpm install
pnpm dev
```

## CI/CD

GitHub Actions runs type checks and a production build on every pull request. A push to
`main` deploys the generated `dist/` directory to Cloudflare Pages.

Configure these in the GitHub **production environment** before the first merge to `main`:

- `CLOUDFLARE_API_TOKEN` — repository secret with Cloudflare Pages edit permission.
- `CLOUDFLARE_ACCOUNT_ID` — repository secret for the target Cloudflare account.
- `CLOUDFLARE_PAGES_PROJECT` — optional repository variable. Defaults to `outof0`.

The deploy job creates the Cloudflare Pages project automatically on its first run, then
publishes `dist/` on every later push to `main`. Do not run a manual
`wrangler pages deploy` locally.

The site serves from `https://outof0.com`, attached to the Cloudflare Pages project as a
custom domain. `www.outof0.com` has no DNS record — add one plus a redirect rule if that
matters to you.

`site` in `astro.config.mjs` is the single source of the canonical origin. The page head
derives its `canonical`, `og:url`, and `og:image` URLs from it, so change the domain there
and nowhere else. See
[`docs/github-org-profile.md`](./docs/github-org-profile.md#1-domains).

## Brand assets

Production-ready copies of assets used by Astro live in `public/`. Do not change the logo
assets in `public/` without mirroring the relevant source asset in `brand/`.
