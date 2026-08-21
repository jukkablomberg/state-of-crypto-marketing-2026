# Retrospective date-provenance sweep — every class-4 and class-5 row admitted before the date check existed

**Instrument:** `scripts/date-provenance-audit.py` (**NEW this run**).
**Mandate:** recommendation 3 of `../weekly-runs/2026-08-20-corpus-run.md` — *"Run the new date check on the corpus's existing rows, not just on new ones. Nothing has audited what was admitted before the check existed. This is the cheapest remaining integrity win before Sep 1."*
**Scope:** all 25 rows of `2026-layoff-tracker.csv` + all 8 files in `../operator-statements/`.
**Date:** 2026-08-21. **Eleven days to ship.**

---

## Why this sweep exists

On 2026-08-20 two candidate items were refused at intake because their true publication dates were **2020** and **2022**, while the search results that surfaced them carried no date at all. Both would have *confirmed* an open question — one closing a seven-run null, one supplying a bigger version of an existing finding. Watch (ss) was adopted from it: **the corpus has good defences against implausible claims and none against welcome ones.**

That check ran at the door. **Nothing had ever checked what was already inside.**

## The predicate

**Does the row's own `source_url` carry a date in its path, and is that date consistent with the date the corpus recorded?**

A URL-path date is asserted by the publisher, ships inside the citation the report already carries, and is checkable without a re-fetch. It is the exact mechanism that resolved the 08-20 Coinbase refusal — the true 2022 date was sitting in the capturing sources' own URL paths the whole time.

---

## 🔴 The instrument's first run was wrong twice, and that is recorded before its results

The first execution reported **two DATE-INVERSIONs**. Both were adjudicated by hand before anything was written to the corpus. **Both were bugs in the instrument, not defects in the corpus.**

| Reported | Reality |
|---|---|
| Row 11 BitMEX — *"url date 2026-07-01 PRECEDES event 2026-07-23 by 22d"* | The URL is `crowdfundinsider.com/**2026/07**/293286-…` — **month precision**, read as 1 July and compared against a day-precision event. 23 July is inside July. **Consistent.** |
| Class 4 `cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md` — *"url date 2026-05-05 PRECEDES 2026-08-11 by 98d"* | `2026-08-11` is the file's **`Captured:`** line — our own clock. `2026-05-05` is CoinDesk's publication date. **Two different quantities. The comparison was meaningless.** The file itself states the article's date correctly in prose. |

**Both fixed.** Precision is now symmetric — the ruling is made at the coarser of the two sides. The class-4 audit no longer guesses a date from prose; it looks for an explicit publication-date field and reports `NO-PUBDATE-FIELD` where there is none.

**This is the same failure shape as the byte-threshold rule retired on 08-20: a predicate that looked decisive and was not.** Two instruments built two days apart, each of which had a wrong rule caught on first contact with real data. **The pattern is now worth naming: a new guard's first run is a test of the guard, not of the corpus, and its output must be adjudicated by hand before any of it is believed.**

---

## Results after the fix

### Class 5 — layoff tracker, 25 rows

| Verdict | n | Meaning |
|---|---|---|
| **SELF-DATED** | 12 | citation's URL path corroborates the recorded date |
| **NO-URL-DATE** | 10 | citation carries no path date; recorded date uncorroborated **but not contradicted** |
| **LAG-EXCEEDED** | 2 | Pump.fun (122d), MVMT Labs (25d) — both known retrospectives, both already annotated |
| **NO-URL** | 1 | **MARA Holdings — no citation at all** |

### Class 4 — operator statements, 8 files

| Verdict | n |
|---|---|
| **NO-PUBDATE-FIELD** | 5 |
| **NO-URL** | 2 |
| **LAG-EXCEEDED** | 1 |

---

## 🔴 Finding 1 — the report advertised a figure its own corpus could not support

**`Algorand -25%` is printed as one of exactly three named class-5 examples in three root documents:** `README.md` L66, `methodology.md` L32, and **`README-for-github.md` L81 — the public-facing one.**

The other two examples (Crypto.com −12%, Gemini −30%) had citations. **Algorand's tracker row had `source_url` empty, `headcount_change` empty, `notes` empty. The row was firm name, `2026-Q1`, and a percentage.**

**✅ REPAIRED THIS RUN, at source.** First-party fetch of the capturing outlet:

- **Date `2026-03-18`**, read from the article's own `published_time` meta (`2026-03-18T21:00:02`) and byline — **not inherited from the search result that surfaced it.** Was `2026-Q1`; now precise to the day.
- **Firm primary quoted verbatim**, Algorand Foundation's own X post (`x.com/AlgoFoundation/status/2034298850878652616`): *"Today, the Algorand Foundation made the difficult decision to reduce our workforce by 25%. This decision was not taken lightly and is in response to the uncertain global macro environment as well as the broader downturn in crypto markets."*
- **Rationale: macro + market downturn. NOT AI.** `ai_cover_narrative_y_n = N` confirmed correct.
- **Headcount REFUSED.** The outlet states plainly that *"Details about how many individuals were affected were not shared."* Secondary estimates of 40–50 positions circulate; **not entered.** Row now reads `undisclosed (firm did not state; DO NOT PRINT A FIGURE)`.
- **Relabelled `[PERIMETER]`** — Algorand is not in the Stratum 1–4 cohort, which the three root docs do not say when they cite it.
- **No function named**, so no marketing-specific impact is established and the cohort-scoped standing finding is untouched.

### ⭐ And the repair produced a Theme-1 signal the uncited row never carried

The same capture records that **after cutting 25% of staff, the Algorand Foundation's careers page still carried two open requisitions — community management and business development.**

**Community management is a marketing function.** A firm reducing headcount by a quarter while keeping a community seat open is direct evidence about *which* marketing sub-functions survive a contraction — the question Theme 5 exists to answer. **This ships.**

**The general lesson is worth more than the row: the uncited row was not merely unsupported, it was under-read. Sourcing it produced a finding. There are nine more rows in this tracker whose citations have never been opened.**

## 🔴 Finding 2 — MARA Holdings, uncited, and deliberately left that way

Row 6: `40` headcount, `2026-Q2`, **no source, no percentage.** No citation was sought and none was invented. Row annotated `[UNCITED - 2026-08-21] … DO NOT PRINT until sourced. If unsourced by ship, STRIKE THE ROW.`

## 🔴 Finding 3 — two class-4 files contain no URL anywhere

`../operator-statements/sport-sponsorship-reset-2026-05.md` and `_stale-article-as-current-signal-instrument-2026-08-20.md` return **zero matches for `http`** in their entire bodies.

The instrument file is a methods note and its lack of links is defensible — though **a note whose whole subject is two mis-dated articles ought to carry those two articles' URLs**, and it does not.

`sport-sponsorship-reset-2026-05.md` is the real problem. It is a substantive four-incident cluster feeding Themes 1, 2 and 5, its sources are named only in prose (*"Bybit corporate communications + Sportcal coverage Q4 2024"*), and **methodology §4 requires class-4 storage to be "verbatim relevant quote + URL + speaker + date + role."** It fails its own storage rule. **Flagged for sourcing or striking before ship.**

## ⚠ Finding 4 — no class-4 file can be date-audited by any script

**Five of eight operator-statement files carry no explicit publication-date field.** They carry `Captured:` — our clock, which proves nothing about the artifact. The two that *are* checkable are checkable only because someone typed the publication date into prose by hand.

**Fix, one line:** add a `**Published:**` field to the class-4 file template. Until then the class most exposed to the 08-20 failure mode — operator statements surfaced by undated search results — is the class no automated guard can inspect.

**One incidental validation:** the sweep independently flagged `okx-rafique-role-reclassification-2026-08-10.md` for a 1,337-day gap between its stated `2022-12-06` document date and its `2026-08-04` URL path. **The file had already caught this by hand and says so** — *"page states Updated on Apr 25, 2024."* The instrument rediscovered a real defect the corpus had already handled correctly. **That is the best available evidence the predicate detects the thing it claims to detect.**

---

## Candidate NOT promoted

**PIP Labs (Story Protocol) −10%**, ~17 March 2026, surfaced *inside* the Algorand capture with a URL (`decrypt.co/361027/pip-labs-sheds-staff-story-protocol-ai`). **Not entered.** Watch (mm) — a rendering of the record is not the record — and the corpus does not promote a layoff from a mention inside another article. **Carried to the next run's work queue with its URL captured, which is more than most candidates arrive with.**

## The honest limit

**A `SELF-DATED` verdict means the citation and the corpus agree with each other. It does not mean either is correct.** Only a first-party fetch settles that. Twelve of 25 class-5 rows now corroborate themselves; **ten cannot be checked by this predicate at all.** This sweep narrowed the queue. It did not empty it, and it must not be reported as a clean bill.

**Tracker still holds at 25 rows. Zero promotions. One row repaired, one row condemned, one candidate declined.**
