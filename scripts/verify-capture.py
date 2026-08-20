#!/usr/bin/env python3
"""verify-capture.py — class-3 capture guard.

Class 1 has a two-predicate feed-health guard that prints a verdict every run.
Class 3 — the regulator registers — is now load-bearing for Theme 4 and had no
guard at all. On 2026-08-17 a `web_fetch` of ESMA's CASPS.csv returned HTTP 200
and 49% of the file, cut mid-field, and reported success; a truncated CSV parses
cleanly, so every derived statistic would have been internally consistent and
wrong. On 2026-08-20 the same thing happened to OTHER.csv — and it was caught by
hand again.

This script implements the checks written down on 08-17 as watch (pp), plus the
correction 08-20 forced on them.

    python3 scripts/verify-capture.py <file> [--expect-rows N] [--json]

Verdict is COMPLETE / TRUNCATED / SUSPECT / UNKNOWN. Only COMPLETE permits an
absence claim about a named entity (methodology rule: "never derive an absence
claim about a named entity from a single unverified large capture").

CHECKS
  1. Final-row termination. Does the last data row have the same field count as
     the header, and does the file end with a newline or a complete field? This
     is the check that has caught BOTH real truncations. It is the primary
     predicate.
  2. Field-count consistency. Rows whose field count differs from the header's
     are reported. (ESMA registers contain legitimately quoted multi-line
     fields, so this is reported, not fatal, when the parser is csv-aware.)
  3. Byte count + md5, recorded for the run record so the capture is auditable
     and a later re-fetch can be compared byte-for-byte.
  4. Size heuristic — REPORTED ONLY, NOT A PREDICATE. See below.

WHY CHECK 4 IS NOT A PREDICATE (correction adopted 2026-08-20)
  The 08-17 rule said: "any web_fetch result near ~82,000 characters is presumed
  truncated." On 08-20 OTHER.csv was truncated at 64,556 characters — well below
  that line — while a NCASP.csv capture of 24,614 characters was complete. The
  cut point is a property of the retrieval channel's token budget on the day, not
  a fixed byte count, so a byte threshold cannot discriminate. The rule is
  RETIRED as a predicate and kept as a printed note only.
  The structural check (1) caught both. Structure, not size.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import sys

# Retained only as a printed note. NOT a verdict predicate — see module docstring.
HISTORICAL_CUT_POINTS = (64_556, 82_445)


def analyse(path: str, expect_rows: int | None = None) -> dict:
    with open(path, "rb") as fh:
        raw = fh.read()

    result: dict = {
        "path": path,
        "bytes": len(raw),
        "md5": hashlib.md5(raw).hexdigest(),
        "verdict": "UNKNOWN",
        "reasons": [],
        "notes": [],
    }

    if not raw:
        result["verdict"] = "TRUNCATED"
        result["reasons"].append("empty body (0 bytes)")
        return result

    text = raw.decode("utf-8-sig", errors="replace")
    result["chars"] = len(text)
    result["ends_with_newline"] = text.endswith(("\n", "\r\n", "\r"))

    # --- csv-aware parse -------------------------------------------------
    try:
        rows = list(csv.reader(io.StringIO(text)))
    except csv.Error as exc:
        result["verdict"] = "TRUNCATED"
        result["reasons"].append(f"csv parse error: {exc}")
        return result

    if not rows:
        result["verdict"] = "TRUNCATED"
        result["reasons"].append("no rows parsed")
        return result

    header = rows[0]
    data = [r for r in rows[1:] if r]
    result["header_fields"] = len(header)
    result["data_rows"] = len(data)

    # --- CHECK 1 (primary): final-row termination ------------------------
    if not data:
        result["verdict"] = "TRUNCATED"
        result["reasons"].append("header present but zero data rows")
        return result

    last = data[-1]
    result["last_row_fields"] = len(last)
    short_last = len(last) < len(header)
    if short_last:
        result["reasons"].append(
            f"FINAL ROW INCOMPLETE: {len(last)} of {len(header)} fields "
            f"(cut mid-record) — this is the check that caught the 08-17 CASPS "
            f"and 08-20 OTHER truncations"
        )
    if not result["ends_with_newline"] and not short_last:
        result["notes"].append(
            "file does not end with a newline, but the final row has a full "
            "field count — treated as complete-but-unterminated, not truncated"
        )

    # --- CHECK 2: field-count consistency --------------------------------
    ragged = [i + 2 for i, r in enumerate(data) if len(r) != len(header)]
    result["ragged_row_count"] = len(ragged)
    result["ragged_rows_sample"] = ragged[:10]

    # --- CHECK 4: size note (NOT a predicate) ----------------------------
    for cut in HISTORICAL_CUT_POINTS:
        if abs(result["chars"] - cut) <= 200:
            result["notes"].append(
                f"char count {result['chars']} sits within 200 of a historical "
                f"truncation cut point ({cut}) — note only, not a verdict input"
            )

    # --- expected-row cross-check ----------------------------------------
    if expect_rows is not None:
        result["expect_rows"] = expect_rows
        if len(data) < expect_rows:
            result["reasons"].append(
                f"row count {len(data)} is below the expected {expect_rows}"
            )
        elif len(data) > expect_rows:
            result["notes"].append(
                f"row count {len(data)} exceeds the expected {expect_rows} — "
                f"the source may have gained rows; re-baseline before claiming a delta"
            )

    # --- verdict ---------------------------------------------------------
    if result["reasons"]:
        result["verdict"] = "TRUNCATED"
    elif ragged:
        result["verdict"] = "SUSPECT"
        result["reasons"].append(
            f"{len(ragged)} row(s) disagree with the header field count "
            f"(quoted multi-line fields can do this legitimately — adjudicate by hand)"
        )
    else:
        result["verdict"] = "COMPLETE"
        result["reasons"].append(
            f"final row has all {len(header)} fields; {len(data)} data rows parsed; "
            f"no ragged rows"
        )

    return result


def main() -> int:
    ap = argparse.ArgumentParser(description="Class-3 capture completeness guard.")
    ap.add_argument("path", help="captured CSV file to verify")
    ap.add_argument("--expect-rows", type=int, default=None,
                    help="row count from a prior verified capture, for a delta cross-check")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of the banner")
    args = ap.parse_args()

    if not os.path.exists(args.path):
        print(f"CAPTURE HEALTH: UNKNOWN — file not found: {args.path}", file=sys.stderr)
        return 2

    r = analyse(args.path, args.expect_rows)

    if args.json:
        print(json.dumps(r, indent=2))
    else:
        print("=== verify-capture ===")
        print(f"file:    {r['path']}")
        print(f"bytes:   {r['bytes']}   chars: {r.get('chars', 'n/a')}   md5: {r['md5']}")
        print(f"rows:    header {r.get('header_fields', 'n/a')} fields / "
              f"{r.get('data_rows', 'n/a')} data rows "
              f"(last row {r.get('last_row_fields', 'n/a')} fields)")
        print(f"CAPTURE HEALTH: {r['verdict']}")
        for reason in r["reasons"]:
            print(f"  reason: {reason}")
        for note in r["notes"]:
            print(f"  note:   {note}")
        if r["verdict"] != "COMPLETE":
            print("  ⚠ CLASS-3 ABSENCE CLAIM REFUSED — a claim that a named entity is")
            print("    absent from this register may NOT be derived from this capture.")
            print("    Positive hits inside the captured portion remain usable.")

    return 0 if r["verdict"] == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
