# Contributing to neo-consulting

Thanks for your interest in contributing. This is a small static project, so the
process is intentionally lightweight.

## How to contribute

1. Fork the repository and create a branch from `main`:
   `git checkout -b feat/your-change`
2. Make your changes.
3. Run the quality gates before opening a pull request:
   - meta audit: `python3 scripts/meta_audit.py --html index.html --css css/tokens.css css/main.css`
   - Lighthouse (local server + `audit.js`) targets: mobile ≥ 90, desktop ≥ 90
   - ensure zero new raw hex colors outside `css/tokens.css`
4. Commit with Conventional Commits (e.g. `feat:`, `fix:`, `docs:`).
5. Open a pull request against `main` and describe what and why you changed.

## What to avoid

- External runtime dependencies (fonts, CDN, analytics) — the page must work offline.
- Breaking the single `<h1>` rule or the WCAG heading hierarchy.
- Changing copy in `index.html` without syncing `docs/content.md`.

## Getting help

Open a [discussion](https://github.com/bestdeejay-design/neo-consulting/discussions)
or an [issue](https://github.com/bestdeejay-design/neo-consulting/issues) if you
need support.