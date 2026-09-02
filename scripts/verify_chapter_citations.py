#!/usr/bin/env python3
"""
verify_chapter_citations.py — the anti-fabrication gate for report chapters.

WHY THIS EXISTS
---------------
The report's credibility rests on one promise: every URL printed in it was read
from a primary source and recorded in the corpus, not recalled or constructed.
A model drafting a chapter can produce a URL that looks perfectly plausible and
does not exist. That failure is invisible to a human reader and fatal to the
report.

This script makes the promise machine-checkable. For every URL printed in a
chapter it asks one question: does this exact string appear somewhere in the
corpus, or in a corpus-derived findings note, that was written before the
chapter? A URL that appears nowhere else was invented by the drafter and is
refused.

WHAT IT DOES NOT DO
-------------------
It does not check that the URL resolves (that is a network job, and the
capture records already carry HTTP status). It does not check that the source
supports the sentence citing it — the appendix says plainly that this is a
reading, done by hand, and that the index does not certify it. This script
certifies provenance within the corpus and nothing more.

Exit 0 = every URL traced. Exit 1 = at least one untraced URL. Chapters must
not be committed at exit 1 without an explicit, recorded decision.

Usage:  python3 scripts/verify_chapter_citations.py [--chapter FILE]
"""
import os, re, sys, argparse

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FINDINGS = os.path.join(REPO, "findings")

# The chapters this gate governs (report body). Working notes are corpus, not chapters.
CHAPTERS = [
    "00-opening-register-first-cases-later.md",
    "01-shape-of-the-function.md",
    "02-ai-in-the-stack.md",
    "03-agency-stack.md",
    "04-mica-readiness.md",
    "05-next-twelve-months.md",
    "06-closing-implications.md",
]

# Two citation shapes appear in this report, and the gate must see both:
#   1. a full URL with a scheme            https://www.afm.nl/en/...
#   2. the house style of Chapter 1: a bare domain and path, no scheme
#          afm.nl/en/sector/actueel/2025/jan/sb-crypto-reclame
# Missing shape 2 was a silent false PASS — three chapters reported zero URLs
# while citing dozens. The lookbehind stops "Crypto.com" yielding "rypto.com".
SCHEME_RE = re.compile(r'https?://[^\s\)\]\>\'"`,;|]+')
BARE_RE = re.compile(
    r'(?<![A-Za-z0-9@.-])'
    r'((?:[a-z0-9][a-z0-9-]*\.)+'
    r'(?:com|org|io|net|co|uk|gov|eu|de|fr|it|es|nl|ch|fm|news|info|xyz|ai|dev|app|finance)'
    r'/[^\s\)\]\>\'"`,;|]*)'
)
VERIFY_RE = re.compile(r'\[(?:DATE-)?VERIFY[:\]]')


def normalise(u: str) -> str:
    """Trim trailing punctuation that markdown prose glues onto a URL."""
    return u.rstrip('.,;:!?*_)]}>"\'')


def corpus_haystack(exclude_path):
    """Every byte of the repo except the chapter under test and this script."""
    parts = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__', '_to_delete')]
        for fn in files:
            p = os.path.join(root, fn)
            if p == exclude_path or fn == os.path.basename(__file__):
                continue
            if not fn.endswith(('.md', '.csv', '.json', '.py', '.txt')):
                continue
            try:
                with open(p, encoding='utf-8', errors='ignore') as f:
                    parts.append(f.read())
            except OSError:
                pass
    return "\n".join(parts)


def key_all(hay):
    """Scheme- and www-stripped haystack, so citation shape never masks a match."""
    hay = re.sub(r'https?://', '', hay)
    return re.sub(r'(?<![A-Za-z0-9])www\.', '', hay)


def check(chapter_file):
    path = os.path.join(FINDINGS, chapter_file)
    if not os.path.exists(path):
        return None
    with open(path, encoding='utf-8') as f:
        text = f.read()

    found = set(SCHEME_RE.findall(text)) | set(BARE_RE.findall(text))
    urls = sorted({normalise(u) for u in found if normalise(u)})
    hay = corpus_haystack(path)

    # A bare-domain citation matches a corpus record that stored the full URL,
    # and vice versa: compare on the scheme-stripped, www-stripped form.
    def key(u):
        u = re.sub(r'^https?://', '', u)
        return re.sub(r'^www\.', '', u)
    hay_k = key_all(hay)
    untraced = [u for u in urls if key(u) not in hay_k]
    return {
        "file": chapter_file,
        "urls": len(urls),
        "untraced": untraced,
        "verify_tags": len(VERIFY_RE.findall(text)),
        "words": len(text.split()),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", help="check a single chapter filename")
    args = ap.parse_args()

    targets = [args.chapter] if args.chapter else CHAPTERS
    failed = False
    total_urls = total_untraced = 0

    print("CHAPTER CITATION PROVENANCE GATE")
    print("=" * 72)
    for ch in targets:
        r = check(ch)
        if r is None:
            print(f"  --  {ch:<46} NOT WRITTEN YET")
            continue
        total_urls += r["urls"]
        total_untraced += len(r["untraced"])
        status = "PASS" if not r["untraced"] else "FAIL"
        if r["untraced"]:
            failed = True
        print(f"  {status}  {ch:<46} {r['urls']:>3} URLs · "
              f"{r['verify_tags']:>2} VERIFY tags · {r['words']:>5} words")
        for u in r["untraced"]:
            print(f"        !! UNTRACED — appears in no other repo file: {u}")

    print("=" * 72)
    print(f"  {total_urls} URLs checked · {total_untraced} untraced")
    if failed:
        print("  RESULT: FAIL — an untraced URL is an invented citation until proven otherwise.")
        print("  Fix by (a) citing the corpus record that holds the real URL, or")
        print("         (b) cutting the claim, or (c) replacing it with a [VERIFY: ...] tag.")
        print("  A cut claim beats a fake anchor.")
        return 1
    print("  RESULT: PASS — every printed URL traces to a corpus record.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
