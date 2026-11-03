# twincan.com

The website for **Twincan** — an answering machine for two!

You string a can to one person: a partner, a parent, your best friend. From then
on every note you record lands on their platter, and theirs on yours. No feeds,
no followers, no group chats. One person, both directions.

Twincan is an iOS app. It has no accounts and no servers of its own — notes move
between the two phones through your own iCloud. It is currently in a small beta.

- **Site:** [twincan.com](https://twincan.com)
- **Privacy policy:** [twincan.com/privacy/](https://twincan.com/privacy/)
- **Terms of use:** [twincan.com/terms/](https://twincan.com/terms/)

## About this repository

This repo holds **only the public marketing site** — a few static pages, no
tracking, no framework — and the small Worker behind its beta signup form. The iOS app is closed source and lives elsewhere; nothing
here is part of it.

It is public because a marketing site has nothing to hide, and because a privacy
policy and terms of use ought to be as inspectable as any other published
document.

## Building

Python 3, no dependencies.

```bash
python3 build.py
```

| To change | Edit |
|---|---|
| Landing page | `index.src.html` |
| AI and note tools page (`/ai/`) | `ai.md` |
| Privacy policy | `privacy.md` |
| Terms of use | `terms.md` |
| Beta signup service | `worker/` (see below) |
| OpenRouter sign-in callback (`/auth/openrouter/`) | the block at the end of `build.py` |

`index.html`, `privacy/index.html`, `terms/index.html`, `ai/index.html` and `auth/openrouter/index.html` are **generated** — edit
the sources above and re-run the build, or your changes will be overwritten. The generated
files are committed because GitHub Pages serves them directly; there is no CI
build step.

`build.py` wraps `index.src.html` into a complete document and adds the meta,
Open Graph and canonical tags. The legal pages are rendered with a compact shell
that reads its palette out of `index.src.html`, so the colours cannot drift apart.

The build asserts the shape of its inputs and fails loudly rather than quietly
emitting a wrong page. If it stops with an `AssertionError`, the message names
the assumption the edit broke.

## Deploying

GitHub Pages serves `main` from the repository root, so pushing is deploying.
`CNAME` pins the custom domain.

URLs are extensionless (`/privacy/`, not `/privacy.html`) because the legal pages
build into their own directories as `index.html`. Pages has no rewrite rules, so
this is the only way to get clean URLs from it — keep internal links pointing at
the trailing-slash form.

## Beta signups

The landing page's form posts to `https://api.twincan.com/beta`, a Cloudflare
Worker in `worker/` that stores an email, an optional name and a timestamp in
the D1 database `twincan-beta`. Cloudflare Turnstile and a hidden honeypot
field keep bots out. The form only appears on twincan.com and localhost.

```bash
cd worker
wrangler d1 migrations apply twincan-beta --remote   # schema; rerun after adding a migration
wrangler secret put TURNSTILE_SECRET     # once; the widget's secret key
wrangler deploy                          # ship the Worker
./export.sh > testers.csv                # every signup, as TestFlight CSV
./export.sh 2026-11-10 > new.csv         # signups since a date (UTC)
```

Import the CSV in App Store Connect: TestFlight → the external group →
Testers → + → Import from CSV.

Local preview: `python3 -m http.server 8000` in the repo root and
`wrangler dev --port 8787` in `worker/` (first run:
`wrangler d1 migrations apply twincan-beta --local`). `worker/.dev.vars`
(gitignored) points the Worker at localhost and Turnstile's always-pass test
secret:

```
ALLOWED_ORIGINS="http://localhost:8000"
TURNSTILE_SECRET="1x0000000000000000000000000000000AA"
```

## Licence

Site content and copy © Chris Messina. `build.py` is MIT.
