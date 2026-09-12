# GitHub organization profile setup

Everything on this page is set in the GitHub UI (or the API) — it cannot be committed. Run
through it once, and re-check it whenever the product line changes.

The goal: someone who lands on [github.com/outof0](https://github.com/outof0) should
understand what OutOf0 builds, and reach a product, in under ten seconds.

## 1. Domains

`outof0.com` is the organization domain. It resolves through Cloudflare and serves the
landing page — `https://outof0.com` returns `200`. Use it in the profile.

| Domain | State |
| --- | --- |
| `outof0.com` | **Live.** The org domain. |
| `www.outof0.com` | **No DNS record.** Add a `CNAME` to the Pages project plus a redirect rule if people are likely to type it. |
| `outof0.dev` | Does not resolve. It was declared in `astro.config.mjs` until 2026-09-12; it was never the real domain. |
| `kitland.dev`, `gitview.dev`, `anypick.dev` | Live, `200`. |

`site` in `astro.config.mjs` is the single source of the canonical origin. The page head
derives `canonical`, `og:url`, and `og:image` from it, so the domain is declared in exactly
one place.

## 2. Organization profile

**Settings → Profile** (or `PATCH /orgs/outof0`).

| Field | Value |
| --- | --- |
| Display name | `OutOf0` |
| Bio | `Independent studio building local-first developer tools. Kitland · AnyPick · GitView. All MIT.` |
| URL | `https://outof0.com` |
| Email | `hello.outof0@gmail.com` |
| Location | *(leave empty rather than inventing one)* |

The bio is the single highest-value field here — it renders next to the org name in search
results, on every repo page, and in link previews. Right now it is empty, so GitHub falls
back to `outof0 has 5 repositories available. Follow their code on GitHub.`

## 3. Repository descriptions and topics

Every repo currently shows the GitHub default — *"Contribute to outof0/X development by
creating an account on GitHub."* — and no repo has topics. Both are set per repo, under the
**About** panel (gear icon) on the repo page, or via `gh repo edit`.

| Repo | Description | Topics |
| --- | --- | --- |
| `outof0/kitland` | `64 local-first developer tools for formatting, encoding, generating, and inspecting data. Web, browser extension, VS Code, and MCP. No account, no upload.` | `developer-tools`, `local-first`, `privacy`, `browser-extension`, `vscode-extension`, `mcp`, `typescript` |
| `outof0/anypick` | `Point any AI coding CLI at any account you already own. Claude Code on your Grok account, Codex on your Gemini login. Local proxies, no shared credentials.` | `ai-coding`, `cli`, `claude-code`, `codex`, `openrouter`, `local-first`, `typescript` |
| `outof0/gitview` | `A Git workspace for VS Code — true three-way merge from real Git index stages, plus history, blame, compare, and hosted review.` | `git`, `merge-conflict`, `three-way-merge`, `vscode-extension`, `developer-tools`, `typescript` |
| `outof0/gitview-landing` | `Static marketing site for GitView, published at gitview.dev.` | `astro`, `landing-page`, `tailwindcss` |
| `outof0/outof0` | `Organization profile and landing page source for OutOf0 — local-first developer tools.` | `developer-tools`, `local-first`, `astro` |

Also set **Website** on each product repo to its own domain (`kitland.dev`, `anypick.dev`,
`gitview.dev`).

## 4. Pinned repositories

Use **Customize your pins** on the org profile page. Pin, in this order:

1. `kitland`
2. `anypick`
3. `gitview`
4. `gitview-landing`

Pinning is what turns the profile from a file list into a product list.

## 5. Doing it from the command line

Install the GitHub CLI, authenticate, then run this from the repo root. The org update needs
the `admin:org` scope.

```bash
gh auth login
gh auth refresh -s admin:org

gh api -X PATCH /orgs/outof0 \
  -f name="OutOf0" \
  -f description="Independent studio building local-first developer tools. Kitland · AnyPick · GitView. All MIT." \
  -f blog="https://outof0.com" \
  -f email="hello.outof0@gmail.com"

gh repo edit outof0/kitland \
  --description "64 local-first developer tools for formatting, encoding, generating, and inspecting data. Web, browser extension, VS Code, and MCP. No account, no upload." \
  --homepage "https://kitland.dev" \
  --add-topic developer-tools --add-topic local-first --add-topic privacy \
  --add-topic browser-extension --add-topic vscode-extension --add-topic mcp --add-topic typescript

gh repo edit outof0/anypick \
  --description "Point any AI coding CLI at any account you already own. Claude Code on your Grok account, Codex on your Gemini login. Local proxies, no shared credentials." \
  --homepage "https://anypick.dev" \
  --add-topic ai-coding --add-topic cli --add-topic claude-code --add-topic codex \
  --add-topic openrouter --add-topic local-first --add-topic typescript

gh repo edit outof0/gitview \
  --description "A Git workspace for VS Code — true three-way merge from real Git index stages, plus history, blame, compare, and hosted review." \
  --homepage "https://gitview.dev" \
  --add-topic git --add-topic merge-conflict --add-topic three-way-merge \
  --add-topic vscode-extension --add-topic developer-tools --add-topic typescript

gh repo edit outof0/gitview-landing \
  --description "Static marketing site for GitView, published at gitview.dev." \
  --homepage "https://gitview.dev" \
  --add-topic astro --add-topic landing-page --add-topic tailwindcss

gh repo edit outof0/outof0 \
  --description "Organization profile and landing page source for OutOf0 — local-first developer tools." \
  --add-topic developer-tools --add-topic local-first --add-topic astro
```

## 6. What renders where

| Surface | Source | Notes |
| --- | --- | --- |
| Org profile README | `outof0/outof0/README.md` | This repo. GitHub renders it on the profile page. |
| Org bio | GitHub UI only | Section 2. |
| Repo list descriptions | GitHub UI only | Section 3. |
| Repo sidebar | `README.md` of each repo | Already written. |
