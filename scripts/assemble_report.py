#!/usr/bin/env python3
"""
assemble_report.py — build the report body from the chapter files.

The report is assembled, never hand-written, so that a chapter corrected during
the citation audit reaches the report by re-running this script rather than by
someone remembering to copy the change across. Hand-assembly is how a corrected
chapter and an uncorrected report end up disagreeing in public.

WHAT IT DROPS, AND WHY IT SAYS SO
---------------------------------
Chapter files carry drafting apparatus the report body should not: a DRAFT
version line, and changelog blockquotes recording how a chapter changed between
revisions. Those are process records and they stay in findings/ where the run
records can point at them. Everything else is carried verbatim.

The script PRINTS every line it drops. An assembler that silently removes
content is the same failure class as a report that silently re-dates itself.

The per-chapter "Citation anchors used" blocks are moved, not cut: they are
collected into a single endmatter section so the reader meets the argument
first and the apparatus second, exactly as they would in a printed report.

Usage:  python3 scripts/assemble_report.py [--check]
        --check  report page budget and exit non-zero if over, write nothing
"""
import os, re, sys, argparse, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FINDINGS = os.path.join(REPO, "findings")
OUT_DIR = os.path.join(REPO, "report")
OUT = os.path.join(OUT_DIR, "state-of-crypto-marketing-2026.md")

# Words per printed page at this report's density, measured on Chapter 1.
WORDS_PER_PAGE = 1100
PAGE_BUDGET = 25

CHAPTERS = [
    ("00-opening-register-first-cases-later.md", "Chapter 1 — Register first, cases later"),
    ("01-shape-of-the-function.md",              "Chapter 2 — The shape of the marketing function"),
    ("02-ai-in-the-stack.md",                    "Chapter 3 — AI in the stack: claimed versus confirmed"),
    ("03-agency-stack.md",                       "Chapter 4 — The agency stack"),
    ("04-mica-readiness.md",                     "Chapter 5 — MiCA and regulated-marketing readiness"),
    ("05-next-twelve-months.md",                 "Chapter 6 — Layoffs and the next twelve months"),
    ("06-closing-implications.md",               "Chapter 7 — What the visible record says about the invisible"),
]

DRAFT_LINE = re.compile(r'^\*\*DRAFT v[\d.]+.*$', re.M)
CHANGELOG_BQ = re.compile(r'^> \*\*v[\d.]+ changelog.*?(?=\n(?!>)|\Z)', re.M | re.S)
# Split on a LOOKAHEAD so the marker and everything after it survives. The earlier
# pattern consumed the marker line greedily to its last `**`, which on a one-line
# anchor block silently deleted most of the chapter's citations from the report.
# Assembly must never remove a citation; the guard below now proves it doesn't.
ANCHORS_SPLIT = re.compile(r'\n(?=\*\*Citation anchors used)', re.M)


def strip_apparatus(text, chapter, dropped):
    for m in DRAFT_LINE.finditer(text):
        dropped.append((chapter, "DRAFT line", m.group(0)[:100]))
    text = DRAFT_LINE.sub('', text)
    for m in CHANGELOG_BQ.finditer(text):
        first = m.group(0).split('\n')[0]
        dropped.append((chapter, "changelog blockquote",
                        first[:100] + f"  [{len(m.group(0).split())} words]"))
    text = CHANGELOG_BQ.sub('', text)
    return re.sub(r'\n{4,}', '\n\n\n', text).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    today = datetime.date.today().isoformat()
    body, endmatter, dropped, missing = [], [], [], []
    total_words = 0

    for fn, title in CHAPTERS:
        path = os.path.join(FINDINGS, fn)
        if not os.path.exists(path):
            missing.append(fn)
            continue
        raw = open(path, encoding='utf-8').read()
        raw = strip_apparatus(raw, fn, dropped)

        parts = ANCHORS_SPLIT.split(raw, maxsplit=1)
        chapter_body = parts[0].rstrip()
        anchors = parts[1].strip() if len(parts) > 1 else ""

        # Normalise the chapter's own H1 to the report's chapter title.
        chapter_body = re.sub(r'\A#\s+[^\n]*', f'# {title}', chapter_body)

        total_words += len(chapter_body.split())
        body.append(chapter_body)
        if anchors:
            endmatter.append(f"### {title}\n\n{anchors}")

    # GUARD: assembly may drop drafting apparatus. It may never drop a citation.
    src_urls, out_urls = 0, 0
    URL = re.compile(r'https?://|(?<![A-Za-z0-9@.-])(?:[a-z0-9][a-z0-9-]*\.)+'
                     r'(?:com|org|io|net|co|uk|gov|eu|de|fr|it|es|nl|ch|fm|news|info)/')
    for fn, _ in CHAPTERS:
        fp = os.path.join(FINDINGS, fn)
        if os.path.exists(fp):
            src_urls += len(URL.findall(open(fp, encoding='utf-8').read()))
    assembled_text = "\n".join(body) + "\n".join(endmatter)
    out_urls = len(URL.findall(assembled_text))
    if out_urls < src_urls:
        print("FAIL: assembly DROPPED citations — %d in chapters, %d in the report."
              % (src_urls, out_urls))
        print("      A report that cites less than its chapters is not the same document.")
        return 1
    print("Citation guard: %d citation strings in chapters, %d carried through." % (src_urls, out_urls))

    if missing:
        print("MISSING CHAPTERS — report is incomplete:")
        for m in missing:
            print("   !!", m)

    pages = total_words / WORDS_PER_PAGE
    print(f"Report body: {total_words:,} words ≈ {pages:.1f} pages "
          f"(budget {PAGE_BUDGET}) at {WORDS_PER_PAGE} words/page")

    if dropped:
        print(f"\nDropped drafting apparatus ({len(dropped)} items) — listed, never silent:")
        for ch, kind, snippet in dropped:
            print(f"   - {ch}: {kind} :: {snippet}")

    if args.check:
        if missing:
            return 1
        print("\n--check: no file written.")
        return 0 if pages <= PAGE_BUDGET else 1

    cover = f"""---
title: "State of Crypto Marketing 2026"
subtitle: "What the public record shows about crypto's marketing function in its first regulated year"
publisher: "NorthPoint"
assembled: "{today}"
---

# State of Crypto Marketing 2026

### What the public record shows about crypto's marketing function in its first regulated year

**NorthPoint.** Capture window closed **31 August 2026**. Assembled {today}.

This report is a public-source synthesis. There are no interviews, no anonymised
quotes and no private knowledge anywhere in it. Every claim is anchored to a primary
source a disagreeing reader can open, or carries an explicit `[VERIFY]` tag marking a
check the authors have not completed. Where a figure's primary source states a range,
the range is reported rather than the convenient endpoint. Where the record is silent,
the silence is recorded as data — and, wherever the silence might instead be an artefact
of our own instruments, it is labelled as that instead.

The corpus, the methodology and the dated run records that produced this report are
public at **github.com/jukkablomberg/state-of-crypto-marketing-2026**, MIT licensed.

---

## Contents

""" + "\n".join(f"{i}. {t}" for i, (_, t) in enumerate(CHAPTERS, 1)) + """
8. Methodology
9. Citation anchors, by chapter

---

"""

    method = open(os.path.join(REPO, "methodology.md"), encoding='utf-8').read()
    tail = ("\n\n---\n\n# Methodology\n\n" + method.split('\n', 1)[1].strip()
            + "\n\n---\n\n# Citation anchors, by chapter\n\n"
            + "\n\n---\n\n".join(endmatter) + "\n")

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(cover + "\n\n---\n\n".join(body) + tail)

    print(f"\nWrote {OUT}")
    print(f"  {os.path.getsize(OUT):,} bytes · {len(CHAPTERS) - len(missing)}/{len(CHAPTERS)} chapters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
