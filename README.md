# OutOf0 landing

Astro landing page for OutOf0, deployed automatically to Cloudflare Pages.

Brand sources are consolidated in [`brand/`](./brand/); the website only serves the required runtime assets in `public/`.

## Local development

```bash
pnpm install
pnpm dev
```

## CI/CD

GitHub Actions runs type checks and a production build on every pull request. A push to `main` deploys the generated `dist/` directory to Cloudflare Pages.

Configure these in the GitHub **production environment** before the first merge to `main`:

- `CLOUDFLARE_API_TOKEN` — repository secret with Cloudflare Pages edit permission.
- `CLOUDFLARE_ACCOUNT_ID` — repository secret for the target Cloudflare account.
- `CLOUDFLARE_PAGES_PROJECT` — optional repository variable. Defaults to `outof0`.

The deploy job creates the Cloudflare Pages project automatically on its first run, then publishes `dist/` on every later push to `main`. Do not run a manual `wrangler pages deploy` locally.
