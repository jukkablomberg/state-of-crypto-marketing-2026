#!/usr/bin/env python3
"""
date-provenance-audit.py — class-4 / class-5 retrospective date guard.
Added 2026-08-21. Closes recommendation 3 of the 2026-08-20 run record.

WHY THIS EXISTS
---------------
On 2026-08-20 two candidate items were refused because their real publication
dates were 2020 and 2022 while the search result that surfaced them carried no
date at all. Both would have CONFIRMED an open question, which is precisely the
class of item that gets the least scrutiny (watch (ss)).

That check was applied at INTAKE. Nothing had ever audited what was admitted
BEFORE the check existed. This script is that audit.

THE PREDICATE
-------------
Does the row's own `source_url` carry a date inside its path, and is that date
consistent with the date the corpus recorded for the event?

A URL-path date is asserted by the PUBLISHER, is part of the citation the report
already ships, and is checkable without a re-fetch. It is the same mechanism that
resolved the 08-20 Coinbase refusal: the true 2022 date was sitting inside the
capturing sources' own URL paths the whole time.

VERDICTS (per row)
------------------
  SELF-DATED        url-path date is present and consistent with the recorded
                    date (publication same-day or up to LAG_DAYS after the
                    event). The row corroborates itself. No action.
  DATE-INVERSION    url-path date is EARLIER than the recorded event date. The
                    article predates the event it reports. One of the two is
                    wrong. **This is the 08-20 failure mode.** Investigate.
  LAG-EXCEEDED      url-path date is later than the event by more than LAG_DAYS.
                    Legitimate for retrospectives; flag for a human look.
  NO-URL-DATE       url carries no date in its path. The recorded date cannot be
                    corroborated from the citation alone. NOT an error — it is an
                    unaudited row, and that is the point of the sweep.
  NO-URL            row has no source_url at all. Cannot ship as a citation.
  UNPARSEABLE-DATE  recorded date is not a resolvable calendar date.

EXIT CODES
----------
  0  no DATE-INVERSION and no NO-URL rows
  1  at least one DATE-INVERSION or NO-URL row

NOT A COMPLETENESS CLAIM. A SELF-DATED verdict says the citation and the corpus
agree with each other. It does NOT say either is right. Only a first-party fetch
of the artifact can say that. This narrows the queue; it does not empty it.
"""

import argparse
import csv
import datetime
import os
import re
import sys

LAG_DAYS = 7

# Date shapes seen in publisher URL paths across the corpus's existing citations.
URL_DATE_PATTERNS = [
    (re.compile(r"/(\d{4})/(\d{2})/(\d{2})/"), "ymd"),        # coindesk, techcrunch, cryptonomist
    (re.compile(r"/(\d{4})-(\d{2})-(\d{2})-"), "ymd"),        # theblock /news/ecosystems/2026-01-14-...
    (re.compile(r"[/-](\d{4})-(\d{2})-(\d{2})"), "ymd"),      # bloomberg /articles/2026-05-15/
    (re.compile(r"/(\d{4})/(\d{2})/(?!\d{2}/)"), "ym"),       # /2026/03/ with no day
]


def url_date(url):
    """Return (date, precision) read from the URL path, or (None, None)."""
    if not url:
        return None, None
    for pat, kind in URL_DATE_PATTERNS:
        m = pat.search(url)
        if not m:
            continue
        try:
            if kind == "ymd":
                y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
                return datetime.date(y, mo, d), "day"
            y, mo = int(m.group(1)), int(m.group(2))
            return datetime.date(y, mo, 1), "month"
        except ValueError:
            continue
    return None, None


def recorded_date(raw):
    """Parse the corpus's own recorded date. Returns (date, precision) or (None, None)."""
    if not raw:
        return None, None
    s = raw.strip()
    s = re.sub(r"\[VERIFY\]", "", s).strip()
    s = re.sub(r"\(.*?\)", "", s).strip()
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3))), "day"
    m = re.search(r"(\d{4})-(\d{2})\b", s)
    if m:
        return datetime.date(int(m.group(1)), int(m.group(2)), 1), "month"
    m = re.search(r"(\d{4})-Q([1-4])", s)
    if m:
        q = int(m.group(2))
        return datetime.date(int(m.group(1)), (q - 1) * 3 + 1, 1), "quarter"
    return None, None


def adjudicate(rec, rec_prec, u, u_prec):
    """
    PRECISION IS SYMMETRIC. Both sides carry a precision and the ruling is made at
    the COARSER of the two. Ignoring this produced two false DATE-INVERSIONs on the
    2026-08-21 first run: a `/2026/07/` crowdfundinsider path was read as 1 July and
    compared against a 23 July event, and the run nearly recorded a corpus defect
    that was an artefact of the instrument. Same failure shape as the byte-threshold
    rule retired on 08-20: a predicate that looked decisive and was not.
    """
    if rec is None:
        return "UNPARSEABLE-DATE", "recorded date is not a resolvable calendar date"
    if u is None:
        return "NO-URL-DATE", "url path carries no date; recorded date is uncorroborated by the citation"

    span = {"day": 1, "month": 31, "quarter": 92}
    # The comparison window is widened by whichever side is coarser.
    rec_span = span.get(rec_prec, 1)
    u_span = span.get(u_prec, 1)
    coarse = max(rec_span, u_span)
    delta = (u - rec).days

    # url may legitimately sit anywhere inside its own bucket, and the event
    # anywhere inside its own; tolerance is the coarser bucket plus the lag window.
    lower = -(u_span - 1)
    upper = coarse + LAG_DAYS

    if delta < lower:
        return "DATE-INVERSION", (
            f"url date {u} ({u_prec}-precision) PRECEDES recorded event date {rec} "
            f"({rec_prec}-precision) by {-delta}d, beyond the {-lower}d precision tolerance")
    if delta <= upper:
        return "SELF-DATED", f"url {u} ({u_prec}) vs event {rec} ({rec_prec}): delta {delta}d within {upper}d"
    return "LAG-EXCEEDED", f"url date {u} is {delta}d after event date {rec} (> {upper}d)"


def audit_csv(path, id_field, date_field, url_field):
    out = []
    with open(path, encoding="utf-8") as fh:
        for i, row in enumerate(csv.DictReader(fh), 1):
            url = (row.get(url_field) or "").strip()
            raw = (row.get(date_field) or "").strip()
            rec, rec_prec = recorded_date(raw)
            if not url:
                out.append((i, row.get(id_field, "?"), raw, "", "NO-URL", "row has no source_url; cannot ship as a citation"))
                continue
            u, u_prec = url_date(url)
            v, why = adjudicate(rec, rec_prec, u, u_prec)
            out.append((i, row.get(id_field, "?"), raw, str(u) if u else "-", v, why))
    return out


PUBDATE_FIELD = re.compile(
    r"^\s*\*{0,2}(?:Published|Publication date|Date of statement|Statement date)\*{0,2}\s*:?\*{0,2}\s*(.+)$",
    re.IGNORECASE | re.MULTILINE)


def audit_markdown(directory):
    """
    Class-4 files.

    A class-4 file records a STATEMENT, and three different dates live in it: when
    the operator said it, when the outlet published it, and when this corpus
    captured it. Only the first two can corroborate each other; `Captured:` is our
    own clock and proves nothing about the artifact.

    The 2026-08-21 first run compared a `Captured: 2026-08-11` line against a
    CoinDesk `/2026/05/05/` path and reported a DATE-INVERSION. Nothing was wrong
    with the file — it states the article's own date explicitly in prose. The
    instrument was comparing two things that were never the same quantity.

    So this audit does NOT guess. It looks for an explicit publication-date FIELD.
    Where none exists the verdict is NO-PUBDATE-FIELD: not a defect in the finding,
    but a statement that **no automated date guard can ever check this file**, which
    is the actionable half. Fix is a one-line `**Published:**` field in the template.
    """
    out = []
    if not os.path.isdir(directory):
        return out
    for i, name in enumerate(sorted(os.listdir(directory)), 1):
        if not name.endswith(".md"):
            continue
        body = open(os.path.join(directory, name), encoding="utf-8", errors="replace").read()
        urls = re.findall(r"https?://[^\s)\]>\"'`]+", body)
        if not urls:
            out.append((i, name, "", "", "NO-URL",
                        "no URL anywhere in file body — fails the methodology's own class-4 storage rule "
                        "(verbatim quote + URL + speaker + date + role)"))
            continue
        # Prefer a URL that actually carries a date in its path.
        dated = [(x, url_date(x)) for x in urls]
        pick = next(((x, d, p) for x, (d, p) in dated if d), None)
        m = PUBDATE_FIELD.search(body)
        raw = m.group(1).strip() if m else ""
        if not raw:
            note = f"{len(urls)} url(s), {'dated path present' if pick else 'no dated url path'}"
            out.append((i, name, "-", str(pick[1]) if pick else "-", "NO-PUBDATE-FIELD",
                        f"no explicit publication-date field; date is unauditable by any script ({note})"))
            continue
        rec, rec_prec = recorded_date(raw)
        if not pick:
            out.append((i, name, raw, "-", "NO-URL-DATE",
                        "publication-date field present but no url path date to corroborate it"))
            continue
        v, why = adjudicate(rec, rec_prec, pick[1], pick[2])
        out.append((i, name, raw, str(pick[1]), v, why))
    return out


def render(title, rows):
    print(f"\n=== {title} ===")
    if not rows:
        print("  (no rows)")
        return {}
    width = max(len(str(r[1])) for r in rows)
    width = min(width, 58)
    for i, ident, raw, u, v, why in rows:
        mark = "🔴" if v in ("DATE-INVERSION", "NO-URL") else ("⚠ " if v in ("LAG-EXCEEDED", "UNPARSEABLE-DATE", "NO-PUBDATE-FIELD") else "  ")
        print(f"{mark} {i:2} {str(ident)[:width]:<{width}}  rec={raw or '-':<14} url={u:<12} {v}")
        if v != "SELF-DATED":
            print(f"      └ {why}")
    tally = {}
    for r in rows:
        tally[r[4]] = tally.get(r[4], 0) + 1
    print("  " + "  ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    return tally


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    args = ap.parse_args()
    repo = os.path.abspath(args.repo)

    print("=== date-provenance-audit ===")
    print("predicate: does the citation's own URL path corroborate the date the corpus recorded?")
    print(f"lag window: publication up to {LAG_DAYS}d after the event counts as consistent")

    totals = {}

    tracker = os.path.join(repo, "corpus", "layoff-tracker", "2026-layoff-tracker.csv")
    if os.path.exists(tracker):
        t = render("CLASS 5 — layoff tracker", audit_csv(tracker, "firm", "date_announced", "source_url"))
        for k, v in t.items():
            totals[k] = totals.get(k, 0) + v

    ops = os.path.join(repo, "corpus", "operator-statements")
    t = render("CLASS 4 — operator statements", audit_markdown(ops))
    for k, v in t.items():
        totals[k] = totals.get(k, 0) + v

    print("\n=== VERDICT ===")
    print("  " + "  ".join(f"{k}={v}" for k, v in sorted(totals.items())))
    bad = totals.get("DATE-INVERSION", 0) + totals.get("NO-URL", 0)
    unaudited = totals.get("NO-URL-DATE", 0) + totals.get("LAG-EXCEEDED", 0) + totals.get("UNPARSEABLE-DATE", 0) + totals.get("NO-PUBDATE-FIELD", 0)
    if bad:
        print(f"  🔴 {bad} row(s) cannot corroborate their own date from their citation. INVESTIGATE BEFORE SHIP.")
    else:
        print("  ✅ no date inversions and no citationless rows.")
    print(f"  {unaudited} row(s) are UNAUDITED by this predicate — the citation cannot")
    print("  confirm or deny the recorded date. That is a work queue, not a pass.")
    print("\n  LIMIT: a SELF-DATED verdict means the citation and the corpus AGREE.")
    print("  It does not mean either is correct. Only a first-party fetch settles that.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
