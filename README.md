# twincan.com

The website for **Twincan** — a voice-note app for exactly two people.

You string a can to one person: a partner, a parent, your best friend. From then
on every note you record lands on their platter, and theirs on yours. No feeds,
no followers, no group chats. One person, both directions.

Twincan is an iOS app. It has no accounts and no servers of its own — notes move
between the two phones through your own iCloud. It is currently in a small beta.

- **Site:** [twincan.com](https://twincan.com)
- **Privacy policy:** [twincan.com/privacy.html](https://twincan.com/privacy.html)
- **Terms of use:** [twincan.com/terms.html](https://twincan.com/terms.html)

## About this repository

This repo holds **only the public marketing site** — three static pages, no
tracking, no framework. The iOS app is closed source and lives elsewhere; nothing
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
| Privacy policy | `privacy.md` |
| Terms of use | `terms.md` |

`index.html`, `privacy.html` and `terms.html` are **generated** — edit the sources
above and re-run the build, or your changes will be overwritten. The generated
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

## Licence

Site content and copy © Chris Messina. `build.py` is MIT.
