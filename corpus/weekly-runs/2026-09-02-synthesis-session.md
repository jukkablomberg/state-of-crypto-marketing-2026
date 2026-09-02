# 2026-09-02 — SYNTHESIS SESSION (CoS, out-of-band; not a 15:07 loop run)

**KPI — units done of 11: 8.** Units 1–8 complete. Remaining: 9–10 (citation audit), 11 (bundle + proof). **Publish 2026-09-15, unchanged.**

> This is not a scheduled-loop run record. It is written to the same file convention so the loop
> reads it as one, because the loop's next run must know these units are done or it will redraft
> Chapter 6 tomorrow at 15:07.

## What was done

| unit | output | words | URLs traced |
|---|---|---|---|
| 1 | `findings/05-next-twelve-months.md` — Theme 5, layoffs / next twelve months | 4,946 | 45 / 45 |
| 2 | `findings/01-shape-of-the-function.md` — Theme 1 | 4,462 | 59 / 59 |
| 3 | `findings/02-ai-in-the-stack.md` — Theme 2 | 3,684 | 29 / 29 |
| 4–5 | `findings/04-mica-readiness.md` — Theme 4, scorecard + narrative | 5,272 | 66 / 66 |
| 6 | `findings/03-agency-stack.md` — Theme 3 | 3,224 | 32 / 32 |
| 7 | `findings/06-closing-implications.md` — closing | 2,193 | derivative |
| 8 | Ch.1 correction + `report/state-of-crypto-marketing-2026.md` assembled | 21,740 total ≈ **19.8pp / 25pp** | — |

Two instruments were built rather than the work being done by hand, because both get re-run:

- **`scripts/verify_chapter_citations.py`** — the anti-fabrication gate. Every URL printed in a chapter
  must appear verbatim in a corpus record; a URL that appears nowhere else was invented and the gate
  refuses it. Handles both citation shapes in this report (full URL, and Chapter 1's bare-domain house
  style) — missing the second shape produced a silent false PASS on three chapters on the first run, and
  that is recorded here because it is exactly the failure class this cycle's post-mortem is about: **a
  check that cannot fail is not a check.** Negative-tested with two invented URLs before being trusted.
  Current state: **240 URLs across 7 chapters, 0 untraced, exit 0.**
- **`scripts/assemble_report.py`** — the report is assembled from the chapter files, never hand-written,
  so a chapter corrected in the citation audit reaches the report by re-running the script rather than by
  someone remembering. It prints every line of drafting apparatus it drops; an assembler that removes
  content silently is the same failure class as a report that re-dates itself silently.

## One correction to a chapter that already existed

**Chapter 1's "quiet copy" paragraph promised something this corpus does not contain.** It described an
audit sweep finding "live, quotable instances across dozens of firms" — *"unqualified 'maximum safety'
heroes, three-digit APY promotions with no on-page risk language, disclaimers that literally fail to
render"* — and forward-referenced a Chapter 5 per-firm scorecard in which "every entry was live-verified."

Repo-wide greps: **"maximum safety" appears only in that sentence. The highest APY figure anywhere in the
corpus is 10%. There is no record of a non-rendering disclaimer.** Public-copy observations exist for three
tracked firms (Kraken, OKX, Bitpanda), from the 08-01/02/03/05 promotional-teardown checkpoints.

The paragraph is rewritten to the record that exists — which is narrower and, on its own terms, sharper:
deadline-keyed campaign surfaces still live in the present tense with working CTAs two days after their
stated close, each read verbatim from a page fetched that day, each carrying the non-EEA-fetch qualifier.
The chapter carries a v0.4 changelog saying what was cut and why. **Nothing was cut for being inconvenient;
it was cut for being unevidenced.** Found by the Theme-4 drafting pass, not by any standing check.

## Corrections the chapters made to their own briefs (each narrows a claim)

1. **The layoff null is false as Chapter 1 stated it.** Two of 26 rows name marketing — Gnosis (07-17) and
   MANTRA (01-14), **both perimeter, zero tracked**. The cohort-scoped claim holds; the tracker-scoped one
   is retired.
2. **The AI-rationale share is 5 of 26 firm-verbatim (19%), not the naive 9 of 26 (35%).** One row is
   anonymously sourced, one is this corpus's own inference from "automation", one is `Y-ADJACENT` and
   barred. ⚠ `_ai-cover-narrative-grading-audit-2026-08-24.md` publishes **4/26** and grades Block as C;
   the CSV upgraded Block C→A on 08-27. **That audit file's share figure is stale and must be corrected
   before it is quoted.**
3. **The consumer-exchange / infrastructure split fails when tested**, and fails asymmetrically — it holds
   inside the seven tracked rows (4 vs 3) and breaks across the full record on Grade-A evidence. Reported
   as a failed test, not smoothed.
4. **Four agencies claim tracked firms, not five** — so **14 of 18** panel agencies claim no cohort firm,
   not 13. Seven name no client at all.
5. **Three `tracked-firms.md` annotations are unsupported by the 2026-06-15 panel** (KuCoin "three-agency
   overlap"; HTX "NinjaPromo relationship"; and `sport-sponsorship-reset-2026-05.md`'s "MarketAcross holds
   PR retainers at Binance and Crypto.com"). None printed; all flagged.
6. **The struck "Binance did not run a CMO search" limb is still live in two corpus files** —
   `cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md` and `longitudinal-2026-06.md` line ~1010. Not
   reproduced in any chapter. **Repair before the audit, or it returns.**
7. **Theme 4's scorecard cannot fill four columns** and says so on the page: KOL/influencer disclosure
   (zero creator posts examined for any tracked firm), regulatory-comms hire status, cost-disclosure
   prominence against the AFM's one-click/two-click standard, and risk-language outside the campaign panel.

## Post-window corpus check

None run this session — this was a synthesis session, not a loop run. The class-1 window stays frozen at
**2026-08-31** in `scripts/daily-corpus-sync.py`; nothing in this session touched it. The 09-03 15:07 run
does STEP 0 as normal and then takes **unit 9**, not unit 1.

## Open for the citation audit (units 9–10)

**47 `[VERIFY]` tags across seven chapters — that is the worklist.** The heaviest: Ferdon's quotes against
episode audio (machine transcript, ASR artefacts in the same text); the Bybit/Helen Liu datum, which is
uncited anywhere in the repo and is currently not citable; the six unread ESMA rows from the 08-25 capture;
the AMF forbearance quote (near-primary via The Block); the EEA-egress re-read of the lapsed campaign
surfaces; Bitwise's date (three candidates); and the recruitee adapter behind Tether's absence claim.

**And the standing distinction the audit exists to close:** the provenance gate certifies that a source
exists and is correctly dated. It does not certify that a source supports the sentence citing it. That
check has been run on **1 of 26** layoff rows. Units 9–10 are where that number moves.
