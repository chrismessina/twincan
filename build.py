#!/usr/bin/env python3
"""Build the static twincan.com site.

index.src.html is a FRAGMENT (no doctype/head/body) because it was originally
written to be sliced apart and injected into Ghost. This wraps it into a real
document and adds the meta tags a standalone site needs.

privacy.md / terms.md are converted with a compact shell that reuses the
cover's own :root custom properties, so the legal pages read as the same
product without duplicating 90 lines of cover CSS.

Run: python3 build.py
"""
import html as _html
import pathlib
import re

HERE = pathlib.Path(__file__).parent
SRC = (HERE / "index.src.html").read_text()

DESCRIPTION = ("An answering machine for two! String the can to one person and every note "
               "you record lands on their platter, and theirs on yours.")
SITE = "https://twincan.com"


def inline(s: str) -> str:
    s = _html.escape(s, quote=False)
    # The URL lands inside a quoted attribute, so it needs attribute escaping —
    # html.escape(quote=False) above only covers text context.
    s = re.sub(r"\[(.+?)\]\((.+?)\)",
               lambda m: f'<a href="{_html.escape(m.group(2), quote=True)}">{m.group(1)}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def md_to_html(md: str) -> tuple[str, str]:
    """Return (page_title, body_html). Unlike the Ghost publisher, the <h1> is
    kept — here there is no CMS to render the title separately."""
    title, out, in_list = "", [], False
    for line in md.splitlines():
        if line.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line[2:])}</li>")
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        if line.startswith("### "):
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            title = line[2:].strip()
            out.append(f"<h1>{inline(line[2:])}</h1>")
        elif line.strip():
            out.append(f"<p>{inline(line)}</p>")
    if in_list:
        out.append("</ul>")
    return title, "\n".join(out)


def meta(title: str, path: str) -> str:
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{_html.escape(DESCRIPTION, quote=True)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Twincan">
<meta property="og:title" content="{_html.escape(title, quote=True)}">
<meta property="og:description" content="{_html.escape(DESCRIPTION, quote=True)}">
<meta property="og:url" content="{SITE}{path}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{SITE}{path}">"""


# ---- index.html: wrap the fragment into a document --------------------------
# These extractors assume a narrow shape for index.src.html. They are asserted
# rather than trusted: a silently mis-built page is far worse than a failed
# build, and this file gets hand-edited.
assert SRC.count("</style>") == 1, (
    "index.src.html must contain exactly one <style> block — the split below "
    "would put later CSS into <body>.")
assert SRC.count(":root{") == 1, (
    "index.src.html must contain exactly one ':root{' rule (and spelled without "
    "a space) — the legal pages copy the palette from it.")
assert SRC.split("<title>", 1)[0].strip() == "", (
    "index.src.html must start with <title> — anything before it is dropped.")

head_frag, body_frag = SRC.split("</style>", 1)
head_frag += "</style>"
title = re.search(r"<title>(.*?)</title>", head_frag).group(1)
head_frag = head_frag.split("</title>", 1)[1]       # re-emitted below in order

(HERE / "index.html").write_text(f"""<!DOCTYPE html>
<html lang="en">
<head>
<title>{title}</title>
{meta(title, "/")}
{head_frag.strip()}
</head>
<body>
{body_frag.strip()}
</body>
</html>
""")

# ---- legal pages ------------------------------------------------------------
tokens = re.search(r":root\{(.*?)\}", SRC, re.S).group(0)   # reuse the cover's palette

LEGAL_CSS = tokens + """
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--night);color:var(--paper);font-family:var(--serif);
  line-height:1.65;font-size:17px}
.wrap{max-width:680px;margin:0 auto;padding:56px 22px 80px}
h1{font-family:var(--slab);text-transform:uppercase;letter-spacing:2px;
  font-size:1.6rem;margin:0 0 6px}
h2{font-family:var(--slab);text-transform:uppercase;letter-spacing:2px;
  font-size:1rem;margin:36px 0 10px;color:var(--paper-dim)}
h3{font-family:var(--slab);font-size:.95rem;margin:24px 0 8px}
p,li{max-width:62ch}
a{color:var(--paper);text-underline-offset:3px}
a:hover{color:var(--tp-red)}
nav.back{font-family:var(--type);font-size:.8rem;letter-spacing:.06em;
  text-transform:uppercase;margin-bottom:34px;display:block}
nav.back a{text-decoration:none;color:var(--paper-dim)}
nav.back a:hover{color:var(--tp-red)}
footer{margin-top:52px;font-family:var(--type);font-size:.75rem;
  letter-spacing:.06em;color:var(--paper-dim)}
footer a{color:var(--paper-dim)}
"""

FONTS = re.search(r'<link rel="preconnect".*?rel="stylesheet">', SRC, re.S).group(0)

# Clean URLs: GitHub Pages has no rewrite rules, but it serves index.html from a
# directory, so privacy/index.html is reachable as /privacy/ (Pages 301s /privacy
# to the trailing-slash form). Keep every internal link pointing at /privacy/.
for slug, path in (("privacy", "/privacy/"), ("terms", "/terms/")):
    t, body = md_to_html((HERE / f"{slug}.md").read_text())
    (HERE / slug).mkdir(exist_ok=True)
    (HERE / slug / "index.html").write_text(f"""<!DOCTYPE html>
<html lang="en">
<head>
<title>{t}</title>
{meta(t, path)}
{FONTS}
<style>{LEGAL_CSS}</style>
</head>
<body>
<div class="wrap">
<nav class="back"><a href="/">&larr; Twincan</a></nav>
{body}
<footer><a href="/">Twincan</a> &middot; <a href="/privacy/">Privacy</a> &middot; <a href="/terms/">Terms</a></footer>
</div>
</body>
</html>
""")

print("built: index.html, privacy/index.html, terms/index.html")
