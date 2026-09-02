#!/usr/bin/env python3
"""
build_publish_bundle.py — build the reader-facing deliverables from the assembled report.

Outputs into ../publish-bundle/ at PROJECT level, deliberately outside the public
repo: the bundle stays private until Jukka publishes.

  report.html   self-contained (no external CSS, JS, fonts or images), print-styled,
                every citation a live link
  report.pdf    built separately by a headless browser; this script emits the HTML
                and prints the exact command

WHY THE LINKIFY STEP IS CAREFUL
-------------------------------
The report cites in two shapes: full URLs, and Chapter 1's house style of a bare
domain and path with no scheme. A reader of the PDF cannot click a bare domain, and
the report's whole promise is that a disagreeing reader can open every source. So
bare-domain citations are turned into real links — but only outside code spans,
outside existing links, and only where the string is shaped like a citation. A
linkifier that rewrites text inside a corpus file path would corrupt the record it
is supposed to make checkable.

Usage:  python3 scripts/build_publish_bundle.py
"""
import os, re, sys, html, subprocess, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "report", "state-of-crypto-marketing-2026.md")
BUNDLE = os.path.abspath(os.path.join(REPO, "..", "publish-bundle"))
OUT_HTML = os.path.join(BUNDLE, "report.html")

TLDS = ("com|org|io|net|co|uk|gov|eu|de|fr|it|es|nl|ch|fm|news|info|xyz|ai|dev|app|finance")
BARE = re.compile(r'(?<![A-Za-z0-9@./-])((?:[a-z0-9][a-z0-9-]*\.)+(?:' + TLDS + r')/[^\s\)\]\>"`,;|]*)')
FULL = re.compile(r'(?<!\()(?<!\[)(https?://[^\s\)\]\>"`,;|]+)')
FULL_ONLY = r'https?://\S+'
BARE_ONLY = r'(?:[a-z0-9][a-z0-9-]*\.)+(?:' + TLDS + r')(?:/\S*)?'


def protect_and_linkify(md: str) -> str:
    """Turn citation strings into markdown links, never touching non-citation code spans.

    The report cites in three shapes and all three must end up clickable:
      1. a full URL in prose
      2. Chapter 1's bare domain + path, no scheme
      3. a URL inside a code span — which the 2026-09-02 citation audit made the
         commonest shape by upgrading bare citations to explicit full URLs

    Shape 3 is why this function cannot simply shelf every code span: doing that
    left 2 links in a report carrying 250 citations. A code span whose ENTIRE
    content is a citation becomes a link that keeps its monospace styling; every
    other code span - corpus file paths, register field names - is left alone,
    because rewriting inside those would corrupt the record this report exists to
    make checkable.
    """
    shelf = []

    def stash(text):
        shelf.append(text)
        return "\x00%d\x00" % (len(shelf) - 1)

    def is_citation(t):
        return bool(re.fullmatch(FULL_ONLY, t) or re.fullmatch(BARE_ONLY, t))

    # 1. Code spans: link the ones that are wholly a citation, shelf the rest verbatim.
    def code_span(m):
        inner = m.group(1).strip().rstrip("*_")
        if is_citation(inner):
            href = inner if inner.startswith("http") else "https://" + inner
            return stash("[`%s`](%s)" % (inner, href))
        return stash(m.group(0))

    md = re.sub(r'`([^`\n]*)`', code_span, md)

    # 2. Existing markdown links stay as they are.
    md = re.sub(r'\[[^\]\n]*\]\([^)\n]*\)', lambda m: stash(m.group(0)), md)

    # 3. Bare citations left in prose.
    def link(m, scheme=""):
        u, trail = m.group(1), ""
        # A citation abutting markdown emphasis ("…-2026**") must not carry the
        # markers into the href, or they print literally in the rendered page.
        while u and u[-1] in ".,;:*_":
            trail, u = u[-1] + trail, u[:-1]
        if not u:
            return m.group(0)
        return "[%s](%s%s)%s" % (u, scheme, u, trail)

    md = FULL.sub(lambda m: link(m), md)
    md = BARE.sub(lambda m: link(m, "https://"), md)

    for i, original in enumerate(shelf):
        md = md.replace("\x00%d\x00" % i, original)
    return md


CSS = """
@page { size: A4; margin: 20mm 18mm 22mm 18mm; }
:root{ --ink:#16181d; --muted:#5b6270; --rule:#d8dce4; --accent:#1c4f8b; --bg:#fff; --panel:#f6f7f9; }
*{ box-sizing:border-box; }
html{ -webkit-text-size-adjust:100%; }
body{ margin:0; background:var(--bg); color:var(--ink);
  font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
  font-size:11.2pt; line-height:1.58; }
.wrap{ max-width:46em; margin:0 auto; padding:3.5em 1.5em 6em; }
h1,h2,h3{ font-family:"Helvetica Neue",Helvetica,Arial,sans-serif; line-height:1.25; letter-spacing:-.011em; }
h1{ font-size:1.85em; margin:0 0 .7em; padding-top:.2em; }
h2{ font-size:1.18em; margin:2.4em 0 .7em; color:var(--ink); }
h3{ font-size:1.0em; margin:1.9em 0 .5em; color:var(--muted); text-transform:uppercase; letter-spacing:.06em; }
p{ margin:0 0 1.05em; }
a{ color:var(--accent); text-decoration:underline; text-underline-offset:2px;
   text-decoration-thickness:.5px; word-break:break-word; }
strong{ font-weight:600; }
hr{ border:0; border-top:1px solid var(--rule); margin:2.6em 0; }
blockquote{ margin:1.4em 0; padding:.85em 1.15em; background:var(--panel);
  border-left:3px solid var(--rule); font-size:.94em; }
blockquote p:last-child{ margin-bottom:0; }
ul,ol{ margin:0 0 1.05em; padding-left:1.35em; }
li{ margin:.3em 0; }
code{ font-family:"SF Mono",Menlo,Consolas,monospace; font-size:.86em;
  background:var(--panel); padding:.08em .32em; border-radius:3px; word-break:break-word; }
.tablewrap{ overflow-x:auto; margin:1.5em 0; }
table{ border-collapse:collapse; width:100%; font-size:8.6pt; line-height:1.4;
  font-family:"Helvetica Neue",Helvetica,Arial,sans-serif; }
th,td{ border:1px solid var(--rule); padding:.42em .5em; text-align:left; vertical-align:top; }
th{ background:var(--panel); font-weight:600; }
em{ font-style:italic; }
/* The cover */
.cover{ border-bottom:2px solid var(--ink); padding-bottom:2em; margin-bottom:2.5em; }
.cover h1{ font-size:2.5em; margin-bottom:.15em; }
.cover .sub{ font-size:1.12em; color:var(--muted); margin:0 0 1.4em; font-style:italic; }

/* Back matter: the seven per-chapter citation blocks. Reference apparatus, not
   reading matter - set smaller and in two columns so it behaves like endnotes
   instead of doubling the document. */
.endmatter{ font-size:.86em; overflow-wrap:anywhere; }
.endmatter h1{ font-size:1.4em; }

@media print{
  @page{ margin:16mm 15mm 18mm 15mm; }
  body{ font-size:9pt; line-height:1.45; }
  .wrap{ max-width:none; padding:0; }
  a{ color:#000; text-decoration:underline; }
  h1{ page-break-before:always; page-break-after:avoid; font-size:1.6em; margin-bottom:.55em; }
  .cover h1, h1:first-of-type{ page-break-before:avoid; }
  h2{ font-size:1.1em; margin:1.7em 0 .5em; }
  h2,h3{ page-break-after:avoid; }
  p{ margin-bottom:.8em; orphans:3; widows:3; }
  blockquote{ margin:1em 0; padding:.6em .9em; font-size:.92em; }
  table{ font-size:7.4pt; }
  th,td{ padding:.3em .38em; }
  blockquote,tr{ page-break-inside:avoid; }
  thead{ display:table-header-group; }  /* repeat the header on every page */
  tfoot{ display:table-row-group; }
  .tablewrap{ overflow:visible; margin:1.1em 0; }
  .endmatter{ font-size:7.6pt; line-height:1.4; column-count:2; column-gap:7mm;
    overflow-wrap:anywhere; word-break:break-word; hyphens:auto; }
  .endmatter h1{ column-span:all; }
  .endmatter h3{ font-size:.95em; margin:1.1em 0 .35em; break-after:avoid; }
}
"""


def main():
    if not os.path.exists(SRC):
        print("FAIL: %s missing — run scripts/assemble_report.py first." % SRC)
        return 1
    os.makedirs(BUNDLE, exist_ok=True)

    md = open(SRC, encoding="utf-8").read()
    # Strip the YAML front matter; the cover is rendered from the body's own heading.
    md = re.sub(r'\A---\n.*?\n---\n', '', md, flags=re.S)
    linked = protect_and_linkify(md)

    body = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"],
        input=linked, capture_output=True, text=True, check=True).stdout

    # Tables get a scroll container so a wide exhibit never forces the page sideways.
    body = re.sub(r'<table>', '<div class="tablewrap"><table>', body)
    body = re.sub(r'</table>', '</table></div>', body)

    # Wrap the per-chapter citation blocks as back matter so the print rules reach them.
    m = re.search(r'<h1[^>]*>Citation anchors, by chapter</h1>', body)
    if m:
        body = body[:m.start()] + '<section class="endmatter">' + body[m.start():] + '</section>'
    else:
        print("  NOTE: citation back-matter heading not found — not wrapped.")

    today = datetime.date.today().isoformat()
    doc = ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">\n"
           "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
           "<title>State of Crypto Marketing 2026 — NorthPoint</title>\n"
           "<meta name=\"description\" content=\"What the public record shows about crypto's "
           "marketing function in its first regulated year. NorthPoint, September 2026.\">\n"
           "<style>%s</style></head>\n<body><div class=\"wrap\">\n%s\n</div></body></html>\n"
           % (CSS, body))

    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(doc)

    links = doc.count('<a href=')
    print("Wrote %s" % OUT_HTML)
    print("  %s bytes · %d live citation links · %d tables"
          % (format(os.path.getsize(OUT_HTML), ','), links, doc.count('<table>')))
    print("  self-contained: %s" % ("YES" if not re.search(
        r'<(script|link)\b|src=|@import', doc) else "NO — external resource found"))
    print("\nPDF: run a headless browser against the HTML, e.g.")
    print("  chrome --headless --disable-gpu --no-pdf-header-footer \\")
    print("    --print-to-pdf=%s/report.pdf %s" % (BUNDLE, OUT_HTML))
    return 0


if __name__ == "__main__":
    sys.exit(main())
