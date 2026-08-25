# The symmetric sweep (watch zz) and the figure-column grading ladder (watch ab)

**Date:** 2026-08-25 · **Mandate:** recommendations 1 and 2 of the 2026-08-24 run record.
**Scope:** all 26 rows of `2026-layoff-tracker.csv`. No web fetches; both sweeps run against the corpus's own captured notes.

---

# PART 1 — WATCH (zz): THE SWEEP WHOSE RESULT THE REPORT DID NOT WANT

## Why it was ordered

The 08-24 audit graded the nine `Y` rows — the rows that make the AI-cover share look **high** — and cut the headline from 35% to 15%. Watch (zz) recorded the asymmetry plainly: *"No one has ever audited the seventeen `N` rows for a firm that did invoke AI and was recorded `N`… The sweep that got done is the one whose result the report wanted."*

## 🔴 First result: the predicate that worked on the Y-side does not transfer

The 08-24 audit's method was a token test — *does "AI" appear in the source?* — and eight of nine `Y` rows rested on it. Applied symmetrically to the `N` rows, it **flags 16 of 17.**

All but one are false positives, and the reason is structural: **on the `Y` side the token test reads the source; on the `N` side it reads our own adjudication prose.** The notes say things like *"STATED RATIONALE: macro + crypto downturn. NOT AI"* — the token is present precisely because the question was considered and answered. A test with a 94% false-positive rate is not a test.

**Recorded because it is the same shape as the retired byte-size heuristic: a predicate that looked decisive, transferred cleanly in appearance, and discriminated nothing.** The sweep was completed by reading all seventeen rows.

## The result: the `N` side is clean

Every `N` row carries an explicitly recorded non-AI rationale, captured from its source:

| Row | Firm | Stated rationale as captured | `N` correct? |
|---|---|---|---|
| 3 | Algorand Foundation | *"uncertain global macro environment… broader downturn in crypto markets"* (Foundation's own X post, verbatim) | ✅ |
| 6 | MARA Holdings | — **no citation at all** — | ⚠ see below |
| 7 | Robinhood | *"flatten management layers / accelerate product velocity"* (CEO Tenev) | ✅ **and see §Robinhood** |
| 9 | Polygon Labs (Jul) | repositioning to payments + Coinme integration (CEO Boiron) | ✅ |
| 10 | Exodus Movement | payments pivot; *"expense discipline"* (SEC Ex. 99.1) | ✅ |
| 11 | BitMEX | *"internal strategic assessment… evolving digital asset sector"* | ✅ |
| 12 | OP Labs | *"This is not about finances"*; narrow focus | ✅ |
| 14 | Gnosis | consumer-app review (firm's own quarterly report, first-party) | ✅ |
| 16 | Uphold | shift to enterprise/bank-facing business | ✅ |
| 17 | BitMart | *"operating conditions, market environment, future strategic direction"* (verbatim) | ✅ |
| 18 | FalconX | market slump + derivatives/EU pivot | ✅ |
| 20 | Polygon Labs (Jan) | acquisition-integration headcount balancing (spokesperson, verbatim) | ✅ |
| 21 | Ethereum Foundation | mandate + treasury-policy reorganisation | ✅ |
| 22 | Pump.fun | *"grew too quickly"* (co-founder Tweedale) | ✅ |
| 23 | MVMT Labs | Chapter 11 / token-treasury collapse | ✅ |
| 24 | Bitwise | prolonged digital-asset price decline | ✅ |
| 25 | MANTRA | April-2025 token crash, downturn, competition (CEO Mullin) | ✅ |

**16 of 16 labelled rows are correctly `N`. The labelling is not noisy in both directions.**

## 🟢 THE HEADLINE: THE SYMMETRIC CHECK STRENGTHENS THE 08-24 RESULT RATHER THAN UNDERMINING IT

Watch (zz) asked whether the 35% → 15% collapse was an artifact of auditing only one side. **It was not.** The `N` side holds. The Grade-A AI-cover share stands.

**This is the first time in the series that a sweep run specifically to look for a defect in our own favour came back clean.** Recorded as such, because the corpus's standing record on self-inspection is six-for-six the other way (watch vv).

## 🔴 The one thing it did catch: the denominator is 25, not 26

**Row 6 (MARA Holdings) had an EMPTY `ai_cover_narrative_y_n` cell. Not `N` — blank.** The 08-24 grading audit's arithmetic — *"9 of 26 rows are `Y` (35%); only 4 of 26 (15%) are Grade A"* — **silently coerced that blank to `N`.**

The row is also the corpus's only completely uncited row (flagged 2026-08-21, slated to strike at ship). It has neither a label nor a source.

**Repaired this run.** The cell now reads `(BLANK - NEVER LABELLED)`; its grade reads `n/a - UNGRADEABLE`; the note records the coercion.

| | 08-24 as printed | 08-25 corrected |
|---|---|---|
| Adjudicable rows | 26 | **25** |
| Grade-A AI-cover | 4/26 = **15.4%** | 4/25 = **16.0%** |

**The correction moves the number 0.6 points and does not change the finding.** It is recorded at full length anyway, because *an audit that creates a category and then quietly fills a blank cell with it has manufactured a datapoint* — which is the exact defect this tracker exists to catch, committed by the tracker's own audit.

## ⭐ A distinction the binary column destroys: Robinhood declined the frame

Row 7's own citation is titled *"Robinhood's note on 10% layoffs shows blaming AI isn't cutting it"* and the corpus note records: **"Tenev explicitly declined the AI-blame framing."**

That is not the same fact as *"this firm's rationale happened not to be AI."* It is a firm that was **offered** the AI explanation by the surrounding discourse and **publicly refused it** — a materially stronger Theme-5 datapoint than any other `N` in the tracker, and the `Y/N` column cannot hold it.

**PROPOSED, NOT APPLIED:** split `N` into `N-absent` (rationale simply is not AI — 15 rows) and `N-declined` (firm was offered the frame and rejected it — Robinhood, and no other row on current evidence). **Not applied this run**: it is a schema change seven days from ship, on a column that has now been rewritten twice in two days, and the `N-declined` population is n=1. Flagged for Phase 2.

---

# PART 2 — WATCH (ab): THE GRADING LADDER, EXTENDED TO THE COLUMNS THAT ACTUALLY BREAK

## Why it was ordered

Watch (vv) is **six-for-six**: every figure whose citation has been opened has carried a defect. Those defects were all in `headcount_change` and `percentage` — and after 08-24, the only column with a grading ladder was `ai_cover_narrative`, which has never broken.

## What shipped

Two new columns, **`headcount_grade`** and **`percentage_grade`**, populated for all 26 rows, on the same five-step ladder the AI column uses:

**A** firm-stated, verbatim in hand · **B** firm-stated, relayed, no verbatim in this row · **C** outlet's own figure, no firm quote · **D** anonymously sourced · **E** inferred / derived arithmetic · **n/a** undisclosed or categorical · **UNCITED** figure present, no source at all.

Grades were assigned from provenance language the corpus had already captured in `notes` — not from new fetches, and not from inference about sources not read.

## 🔴 THE RESULT: ONE HEADCOUNT FIGURE IN THE ENTIRE TRACKER IS FIRM-STATED

### `headcount_change`

| Grade | Rows | Which |
|---|---|---|
| **A** | **1** | **14 Gnosis** — *"The App and Circles teams went from 28 to 14"*, first-party |
| B | 0 | — |
| C | 6 | 5 Block · 12 OP Labs · 13 Kraken · 16 Uphold · 20 Polygon (Jan) · 21 Ethereum Foundation |
| D | 1 | 22 Pump.fun (anonymous X account; Sandmark could not confirm) |
| E | 5 | 1 Crypto.com · 4 Coinbase · 7 Robinhood · 18 FalconX · 24 Bitwise |
| UNCITED | 1 | 6 MARA |
| n/a | 12 | undisclosed / categorical |

**Fourteen rows carry a headcount figure. Exactly one is firm-stated with a verbatim quote in hand — and it is scoped to two teams at a perimeter firm, not company-wide.**

> 🔴 **PROHIBITED:** any aggregate headcount sentence across this tracker. *"N thousand crypto jobs cut in 2026"* would be built from **one** firm-stated number and thirteen outlet, derived, anonymous or uncited ones.

### `percentage`

| Grade | Rows | Which |
|---|---|---|
| **A** | **4** | 2 Gemini (SEC 8-K) · 3 Algorand (own X post) · 10 Exodus (SEC Ex. 99.1) · 26 Dune (CEO verbatim) |
| B | 2 | 4 Coinbase (Armstrong memo) · 7 Robinhood (firm's own note) |
| C | 9 | 1 · 5 · 8 · 12 · 13 · 15 · 16 · 21 · 24 |
| D | 1 | 18 FalconX — *"the WEAKEST provenance chain in this tracker"* |
| n/a | 10 | incl. **20 Polygon (Jan) — DISPUTED BY FIRM** |

**Sixteen rows carry a percentage. Four are firm-stated with a verbatim quote. Two of those four are SEC filings.**

> 🟢 **PERMITTED:** *Of the 2026 crypto workforce reductions this corpus records, only four carry a percentage the firm itself stated in a document we hold — and half of those are filings made to a securities regulator, not press statements.*

## Three things the ladder exposed that prose had hidden

1. **`n/a` was doing four different jobs.** *Undisclosed* (Messari — the firm was asked and declined), *refused by us* (BitMart's 550 aggregator figure, deliberately not entered), *categorical* (wind-downs and Chapter 11, where "100%" is a state not a measurement), and **disputed by the firm** (Polygon January, where the firm contests the number). **The A–E ladder has no rung for a contested figure.** Recorded as a sixth category, not forced onto the ladder.
2. **Kraken's anonymity attaches to the framing, not the figures.** Bloomberg's *"person familiar with the matter"* sources the **AI rationale** (Grade D, correctly). The `~150` and `-5%` are Bloomberg's own reporting (Grade C). The row previously read as uniformly anonymous. **It is not, and the distinction is the difference between a usable figure and an unusable one.**
3. **Grade E is a corpus-authored risk, not only an outlet one.** Bitwise's `~25` was computed *by this corpus* from the source's *"approximately 180 → approximately 155"*. Crypto.com's `~180` was computed by the outlet. **Both are derived; only one was ours; neither was labelled until now.**

## Rows still unopened, and what the grades predict

Recommendation 2 also named rows **5 (Block)**, **12 (OP Labs)** and **13 (Kraken)** as the reachable remainder of the citation sweep. **Not opened this run** — the run's fetch budget went to the CASPS register (recommendation 3), which had been refused twice and gates a Theme-4 claim.

All three now sit at **Grade C on both figure columns**, which is the sweep's own prediction of where they will break: an outlet figure with no firm quote is exactly the shape of the six defects already found. Rows **9, 10, 17** remain unreachable.

## Explicit non-claims

1. **No figure was changed, struck or added.** Only grades and one blank-cell repair.
2. **No grade rests on a source read this run.** Every grade derives from provenance language already captured. Where the existing note did not establish firm-statement, the conservative grade was taken and marked `[VERIFY]` — rows 4 and 5 carry that marker.
3. **Grades are claims about provenance, not accuracy.** A Grade-A figure is one the firm stated. It is not thereby true — Gemini's Grade-A `-25%` sits beside a struck `-30%` that propagated for months.
4. **The `N-declined` split was proposed, not applied.**
5. **No claim that the tracker is now sound.** Twelve of 26 rows have never had their citation opened.
