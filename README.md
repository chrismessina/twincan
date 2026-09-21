# twincan.com

Static marketing site for **Twincan**, a voice-note app for exactly two people.

Three pages, no server, no build dependencies beyond Python 3.

## Deploying

GitHub Pages serves this repo's `main` branch from the root. Push and it's live.
`CNAME` pins the custom domain to `twincan.com`.

The app itself lives in a separate private repo — nothing here is part of the iOS
source.

## Editing

| To change | Edit | Then |
|---|---|---|
| The landing page | `index.src.html` | `python3 build.py` |
| Privacy policy | `privacy.md` | `python3 build.py` |
| Terms of use | `terms.md` | `python3 build.py` |

**Do not edit `index.html`, `privacy.html` or `terms.html` directly — they are
generated and will be overwritten.** Commit both the sources and the built HTML;
Pages serves the built files and there is no CI build step.

### Why `index.src.html` exists

It is a *fragment* — no `<!DOCTYPE>`, no `<head>`, no `<body>`. It was originally
written to be split at `</style>` and injected into Ghost as an HTML card, which
is why it has that shape. `build.py` wraps it into a real document and adds the
meta, Open Graph and canonical tags a standalone site needs.

The legal pages reuse the cover's own `:root` palette, read out of
`index.src.html` at build time, so the colours can't drift.

## Still on Ghost

`chrismessina.me/tincan/`, `/tincan-privacy/` and `/tincan-terms/` still serve the
same content, published by `publish-ghost.py` in the app repo. Once this site is
live those should 301 here, via a `redirects.json` upload in
Ghost Admin → Settings → Labs. Until then the content is duplicated in two places.
