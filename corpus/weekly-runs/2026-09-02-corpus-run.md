# Corpus-assembly daily run — 2026-09-02 **(day 63 · FIRST FULL POST-WINDOW DAY · day 1 post-ship)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-09-02 (Wednesday). The report shipped yesterday; the class-1 capture window closed 2026-08-31.
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 09-01 record:** (1) the post-window rule was *inferred, not contracted* — today either contracts it or repeats the inference; (2) the sync **will roll `as_of` again today**, stated in advance as a live risk; (3) row 756 (retire the loop, or say what a post-window run is for) is **Jukka's letter and is still OPEN** — not re-asked here; (4) post-ship backlog: fingerprint negative-delta predicate (an), slug reconciliation (al, disclosed), class-4 `**Published:**` backfill, and *teach the sync that its window has an end* (ao).
**Dedup baseline read before writing:** `2026-09-01-corpus-run.md` in full; `methodology.md`, `scripts/README.md`, `tracked-firms.md`; `findings/longitudinal-2026-06.md` tail; `layoff-tracker/2026-layoff-tracker.csv` all 26 rows; `operator-statements/` index (10); upstream `scan_metadata`, `new_since_last_scan`, `still_open_from_prior_scans`, `fetch_errors`, `drops_summary`, `_feed-fingerprint.json` read directly; `queues/needs-jukka.md` searched for an answered row before raising anything; repo greps for `Pagliari`, `Luno`, `VP of Growth`, `Growth and Media`.
**🟢 CADENCE (this loop): HELD. 63 run records for 63 post-deadline days.**
**🟢 CADENCE (the upstream feed): HELD, unassisted, third consecutive day.**

---

## Headline result

**Yesterday's record predicted this run would roll two shipped exhibits' dates. It did — and it did something worse than the prediction, which is why the rule is now in code rather than in a paragraph.**

### 1. 🔴⭐ **THE POST-WINDOW DEFECT RECURRED IN 24 HOURS AND ESCALATED: IT NO LONGER ONLY RE-DATES THE ABSENCE PANEL, IT ADDS A MEMBER TO IT.**

Run unpatched first, deliberately, to observe the real behaviour rather than assume yesterday's:

```
FEED HEALTH: HEALTHY (scanned_at_utc=2026-09-01T22:17:46Z, age=13.9h,
  fingerprint total_jobs_fetched=3355, delta=-46 vs 2026-09-01 (3401))
job postings ADDED: 0  firms: []
tracked firms STILL w/o coverage: ['Aave','Binance','Bybit','Gemini','HTX','Kucoin']
```

`git diff` on the two shipped exhibits:

- **`_chrome-queue.csv`** — `as_of` `2026-08-31` → `2026-09-02`, content otherwise identical. **Exactly yesterday's defect, repeated.**
- **`_absence.csv`** — `as_of` rolled **and a seventh row appeared**: `Gemini,api-fetch-error,…boards-api.greenhouse.io/v1/boards/gemini/jobs?content=true: The read operation timed out,2026-09-02`.

⚠ **That second half is the escalation.** Yesterday the roll was a date on unchanged content — bad, but cosmetic in substance. Today the sync was **one write from putting a post-window class-1 observation into a shipped Theme-1/Theme-4 exhibit**, changing what the exhibit *says*, not just when it says it was true. **Both files restored byte-for-byte** (md5 verified against `HEAD`; the mount refuses `unlink`, so `git checkout` fails and the restore was done by truncate-and-write-in-place, which also preserves the CRLF endings a naive rewrite stripped on 09-01).

### 2. 🟢⭐ **WATCH (ao) CLOSED IN CODE. THE SYNC NOW KNOWS ITS WINDOW HAS AN END — AND THE GUARD IS RED-PROOFED BOTH WAYS.**

**Two hand corrections on consecutive days is the signal to stop hand-correcting.** `scripts/daily-corpus-sync.py` gains:

```python
CAPTURE_WINDOW_END = "2026-08-31"      # or --window-end YYYY-MM-DD | none
```

| Artifact | Post-window | Why |
|---|---|---|
| `job-postings/<firm>.csv` | **not written**; offered rows counted + printed | corpus claim |
| `_absence.csv` | **not written**, even when content is unchanged | corpus claim; the `as_of` column alone re-dates it |
| `_chrome-queue.csv` | **not written** | same |
| `_feed-fingerprint.json` | **still written every run** | **instrument log.** "A 09-02 scan ran" is a true fact about the instrument |
| class 2 (`agency-*`) | untouched | its `as_of` comes from the feed's `lastUpdated`, not the run clock |

The distinction between the third row and the fourth **is the whole patch**; it is the ruling made by hand on 09-01, now executable.

🟢 **Red-proofed (lessons L16 — a check that cannot fail is not a check):**

| Invocation | Verdict |
|---|---|
| default (`--window-end 2026-08-31`) | **FROZEN** — both exhibits byte-identical to `HEAD` by md5, 0 rows admitted, Gemini drift flagged not written |
| `--window-end none` | **WRITES** — reproduces the exact defect in a scratch copy: `as_of` → `2026-09-02` on both files **plus the new Gemini row** |
| `--window-end 2026-12-31` | **WRITES** — window open, normal behaviour intact |

`--window-end` exists *so that* the guard can be made to return the other verdict. Idempotence re-verified: one `2026-09-02` fingerprint entry after three runs.

⚠ **Why this was in scope while row 756 stays Jukka's.** Row 756 asks him to retire the task or contract it. **A change to a script this loop owns is safe under all three branches of that letter** — if he retires the loop the patch is inert, if he keeps it the patch is precisely what (b) proposed, if he pauses it nothing fires. What was **not** touched: the loop's own prompt, the scheduler, and the decision itself. The patch narrows row 756 from *"keep it and hand-correct an exhibit every day"* to a clean **keep-or-retire**.

### 3. 🔴⭐ **THE ABSENCE PANEL GAINED A MEMBER FOR THE FIRST TIME EVER — AND IT IS A FACT ABOUT THE SCANNER, NOT ABOUT GEMINI.**

`methodology.md` §1 has stated since 08-30 that the panel's *"membership has been the same five firms (Aave, Binance ×2, Bybit, HTX, KuCoin) on every run since the cohort expansion."* Today the **live** read is six. The cause is in the feed verbatim: a greenhouse **`read operation timed out`** on `boards-api.greenhouse.io/v1/boards/gemini/jobs` — **not a proprietary ATS, not a 404, a transient timeout.**

`fetch_errors` is consequently **5, not the four stable 404s** that had been unchanged for twelve consecutive runs (Wormhole Foundation, Aave, Bitwise, Chainlink Labs — all still 404). Gemini is the first *timeout*-class member the panel has ever had.

🟢 **Not admitted. Recorded in `methodology.md` §1 as post-window drift**, with the point stated in the section's own vocabulary: **the panel's membership is a fact about the scanner, and today it moved while nothing about any firm moved.** Anyone re-running the sync sees six in the banner and five in the file; that gap is the freeze working.

### 4. ⚠⭐ **AND IT TOOK HALF THE CRYPTO COHORT'S MARKETING-HIRING COUNT WITH IT. WATCH (ag) MOVED 25:2 → 24:1 ON ZERO FIRM BEHAVIOUR.**

`still_open_from_prior_scans`, counted by company:

| | 09-01 | 09-02 |
|---|---|---|
| AI labs (OpenAI · Anthropic · Cohere · Perplexity) | 12 · 8 · 3 · 2 = **25** | 11 · 8 · 3 · 2 = **24** |
| Stratum 1–4 crypto cohort | Gemini 1 · Phantom 1 = **2** | Phantom 1 = **1** |

**The crypto side halved because a job board timed out.** Gemini's single open marketing role did not close; it became unobservable. n=7 in the series, and the most instructive observation in it: **a ratio Theme 2 was going to quote moved 50% on the denominator side for a reason that has nothing to do with any firm's marketing function.** This is exactly why watch (ag) was never allowed to become a corpus claim, and the appendix language written on 09-01 (`findings/appendix-scope-of-the-citation-index.md` §3) already carries the handling rule. ⚠ **Still not a corpus entry**; AI labs are outside the cohort and no claim is derived from them.

### 5. ⚠ **THE NEGATIVE-DELTA HOLE GOT ITS LARGEST INSTANCE — AND TODAY IT SHARES A CAUSE WITH HEADLINE 3, WHICH SHARPENS WATCH (an) RATHER THAN JUST ADVANCING IT.**

`total_jobs_fetched` **3401 → 3355, delta −46** — the largest negative in the series (prior: −12, −2, −1). The second predicate refuses a delta of **0**; −46 is non-zero and passes. Age (13.9h) carries the verdict independently, so nothing rests on it.

⚠ **What is new is the mechanism.** Gemini's board timed out, so its jobs left `total_jobs_fetched`. **The fingerprint moved because the instrument lost reach — not because the market moved.** The predicate's premise is *"if the fingerprint moves, the scan genuinely looked"*; today it moved by −46 **while the scan looked at one fewer company than yesterday.** Non-zero and *the scan looked at the same estate* are not the same claim, and the gap between them is now measured rather than hypothesised. **Not patched today** — one predicate change per run, red-proofed, and this one needs a companies-scanned-normalised comparison that is a design question, not a line edit. Recorded for the post-ship backlog with its first real instance.

### 6. ⚠ **WATCH (am), THIRD CONSECUTIVE RUN — AND THE RETRIEVAL LAYER MADE THE SAME WRONG ATTRIBUTION IT MADE ON 08-31, ESCALATED.**

Today's class-5 summary states that the Coinbase cuts came *"with CEO Daniel Shapero noting the layoffs will affect roles within engineering, product and marketing teams."*

**This is the 08-31 incident, one step worse.** On 08-31 the summariser merged two adjacent sections of one page — the sentence sits at line 443 and belongs to **LinkedIn**, whose section ends before Coinbase's begins at line 445. Today it has stopped merging and started **asserting**: it names Shapero as *Coinbase's* CEO. The corpus's own held row cites the **Armstrong memo** (Fortune, 2026-05-05) and names no other executive.

🟢 **The 08-29 ruling STANDS, re-verified for the third time: no source names marketing as an affected function at Coinbase.** It is a load-bearing absence in Theme 1, it has now survived three retrieval-layer attempts to overturn it, and **each time the thing that caught it was a held, cited row — not the search.**

### 7. ⚠ **A STALE ITEM ARRIVED UNDATED, AND IT WOULD HAVE CONFIRMED. WATCH (ss), FOURTH CONSECUTIVE PAYOUT.**

The class-4 search returned, inside a 2026 framing and with **no date**: *"Crypto.com has hired Nicolò Pagliari as Global VP of Growth and Media, marking another high-profile departure from the traditional CFD brokerage sector."*

It is close to ideal bait: **a tracked Stratum-1 firm, a senior marketing seat, and a CFD→crypto talent-flow story that sits comfortably inside Theme 1.** A second, targeted search resolved it to **July 2025** — eleven months before the event it was sitting next to.

🔴 **REFUSED, twice over.** (a) Stale-as-current — the `_stale-article-as-current-signal-instrument-2026-08-20.md` pattern, arriving in the retrieval layer where no corpus guard reaches. (b) Class 4 wants a *statement by* a senior operator with Theme bearing; the only quote available is Pagliari's LinkedIn post about **leaving Saxo Bank**, which says nothing about crypto marketing.

⚠ **One trap recorded so a later run does not fall into it: this is NOT the Kalifowitz succession.** Steven Kalifowitz's CMO exit is effective 2026-06-30 (`cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md`); Pagliari's VP hire predates it by eleven months. A reader meeting the two items adjacently — which is exactly how the retrieval layer presented them — would naturally read the second as filling the first. **It does not, and nothing in the corpus says it does.**

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`) — **FROZEN IN CODE, first run under the new guard**

```
date: 2026-09-02
CLASS-1 CAPTURE WINDOW CLOSED (2026-08-31) — class-1 corpus files FROZEN.
FEED HEALTH: HEALTHY (age=13.9h, 3401 → 3355, delta=-46)
job postings ADDED: 0   post-window rows OFFERED but NOT admitted: 0  firms: []
chrome work-queue: ['Binance','Bybit','HTX','Kucoin','Solana']
tracked firms STILL w/o coverage: ['Aave','Binance','Bybit','Gemini','HTX','Kucoin']  [LIVE READ]
  !! POST-WINDOW ABSENCE-PANEL DRIFT: ['Gemini'] — instrument reach, not evidence about the firm. Not written.
```

`companies_scanned` **147** · `companies_via_api` **99** · `companies_via_chrome_pending` **48** · `fetch_seconds` **17.4** · `total_jobs_after_filter` **45** · `new_count` **2** · `still_open_count` **40** · `url_verification_dropped` **3**.

⚠ **`new_count` is 2 and both are out of cohort** — Anthropic *Communications Lead, DACH* (Munich, posted 2026-09-01) and OpenAI *Integrated Marketing Lead, Brand & Policy* (SF, posted 2026-08-31). AI labs; filtered; **0 rows offered to the freeze.** Recorded because the question *"what happens when a tracked firm posts a marketing role after the window closes?"* is now answered in code rather than by whichever run notices — **it would be counted, printed, and refused.**

Fingerprint series: `… 3362 → 3398 → 3397 → 3401 → 3355` ← today, delta **−46**, largest negative on record (headline 5).

`fetch_errors`: **5, up from four.** The four stable 404s (Wormhole Foundation, Aave, Bitwise, Chainlink Labs) — **thirteenth consecutive run**, the evidence they are structural — plus **Gemini, greenhouse read timeout**, new and transient-class. `drops_summary` unchanged in shape (`exclude_function` 2543 · `no_marketing_keyword` 619 · `no_seniority_signal` 102 · `exclude_seniority` 30 · `tracker` 12 · `exclude_location` 4).

**Absence panel: shipped at 5 firms, `as_of` 2026-08-31, now held by code rather than by hand.** Live read 6 — headline 3.

**Slug-vs-label reconciliation: not run, nothing to reconcile** (0 rows admitted; post-window it can never again have anything to reconcile). Watch (al) remains **closed as a disclosure**, published in `findings/appendix-scope-of-the-citation-index.md` §2.

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 79 days stale.** 18 agency-claims files written, **byte-identical for the twenty-second consecutive run** (no `git diff` at all). 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation. Watch (d) stays **CLOSED**: the real last-refresh date is stated in every public document. Class 2 is deliberately **outside** the window freeze — its `as_of` derives from the feed's `lastUpdated`, not the run clock, which is why it has never drifted.

### 3. Regulator — **0 NET-NEW.**

| Surfaced | Disposition |
|---|---|
| ESMA statement — unauthorised CASPs to wind down and **cease marketing activities and solicitation** (+ AMF mirror, + the ESMA PDF itself) | **ALREADY HELD** at source (`esma-mica-transitional-period-end-2026-06.md`). Fifth consecutive re-surfacing |
| **VARA — 19 firms sanctioned, AED 100k–600k ($27k–$163k), breaches of the 2024 Marketing Regulations** | **ALREADY HELD AT SOURCE** (`vara-enforcement-register-at-source-2026-08-14.md`, 37 rows, underlying **7 Oct 2025** notice). Fifth consecutive re-surfacing. **Nothing re-fetched** |
| **"Fines since MiCA enforcement began have exceeded €540 million"** (cryptonomist, secondary) | 🔴 **REFUSED — and recorded explicitly because it LOOKS like it breaks watch (b) and does not.** No named firm, no named NCA, no marketing nexus, no primary. An aggregate of *all* MiCA-perimeter penalties is not a marketing-side action against a CASP. Same family as the "5,000+ crypto jobs cut" totals class 5 refuses |
| MiCA Art. 111 penalty ceilings (€5m / 12.5% of turnover; €30k–€15m / 15% for market abuse) | **REFUSED — statute, not an action.** Held already via the Regulation itself |
| MAS — "may revoke licences, require market exit, issue public warnings, disqualify individuals for misleading promotions" | 🔴 **REFUSED.** Supervisory *powers* described by a vendor page; **no MAS instrument, no named firm, no date.** Not fetched |
| Vendor / law-firm explainers (Sedric ×2, Hacken, InnReg, Unit21, bleap, Zitadelle, coinlaw, Coinzilla, eakdigital, neoslegal, cryptoverselawyers, aosphere, financialregulations.eu, casptracker, Global Law Experts) | **REFUSED.** Secondary commentary; no regulator speaks in any of them and no tracked-firm operator is quoted |
| **FCA v HTX** — proceedings still paused under the 25 June orders; settlement talks continued "through late August" | 🔴 **NULL RE-CONFIRMED, day 2 post-window.** **No consent order and no outcome is published.** Only the mid-August settlement-talks reporting the corpus already holds (`fca-htx-promotions-consent-order-stay-2026-08-28.md`). **Nothing inferred from the stay's expiry, on the third consecutive day it would have been easy to** |

**Watch (b) — NOT ADVANCED. 🟢 THE NULL HOLDS AT DAY 63**, in its narrow form: *no EU national competent authority has published a named marketing-side enforcement action against a CASP since the MiCA transitional deadline.* Post-ship it is no longer a finding under test — it is **a shipped finding under maintenance**, and today is the first day it was checked as such.

**Not fetched, not guessed:** `CASPS.csv`, `OTHER.csv`, `NCASP.csv`, MAS instruments, the retry queue, the four un-fetched FCA orders, VARA's Shelbit / MEXC / CoinMENA notice bodies, `rulebooks.vara.ae`. **All standing prohibitions honoured.**

### 4. Operator statements — **0 NET-NEW.** Held at 10 files.

| Surfaced | Disposition |
|---|---|
| **Binance — Conlan exit / Eowyn Chen interim (2026-05-12)** | **ALREADY HELD** (`binance-conlan-cmo-exit-primary-2026-08-31.md`, first-party) |
| **Crypto.com — Kalifowitz CMO exit eff. 2026-06-30** | **ALREADY HELD** (`cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md`) |
| **Crypto.com — Nicolò Pagliari, Global VP Growth & Media (ex-Saxo)** | 🔴 **REFUSED TWICE OVER — headline 7.** Undated in the summary; resolves to **July 2025**. And an appointment is not a statement: the only quote concerns leaving Saxo. ⚠ **Explicitly not the Kalifowitz succession** |
| Coinbase — Ferdon CMO | **ALREADY HELD** (`coinbase-ferdon-marketing-vanguard-2026-04.md`) |
| Trade-press aggregations of the above (paymentexpert, yellow.com, MEXC News, bitcoinke, FX News Group, fxdailyreport, ministryofsport, coinspectator, advfn, tradeinformer, Gate Wiki) | **REFUSED.** Renderings of records the corpus holds at primary — watch (mm) |

**Watch (l), 29th costing — WEAK.** Today's refusal set is valid at any §4 width. The one item with genuine Theme bearing (Pagliari) fails on date and on class, not on width.

### 5. Layoffs — **0 NET-NEW EVENTS. Tracker holds at 26 rows, 26 citations. Zero edits.**

Every firm surfaced is already held: **Coinbase (−14%, 700) · Luno (−20%, PERIMETER) · Crypto.com (−12%, ~180) · Gemini (−25% firm-stated; the "−30% YTD" is struck and must not be printed) · BitMEX (wind-down, 23 Sep 2026)**.

- ⚠ **The Coinbase item arrived misattributed for the third time — headline 6.** Corpus row stands on the Armstrong memo; the "marketing teams" clause still belongs to a different company's section of the same page.
- ⚠ **The Luno rationale was re-offered with the CEO named as James Lanigan** — which **matches the corpus's own row verbatim** (CoinDesk, 2026-07-30; `ai_cover` graded `Y [INFERRED FROM "AUTOMATION" — FIRM DID NOT SAY "AI"]`). Recorded because on a day when the same summary got Coinbase's attribution wrong, the one it got right is worth naming: **the corpus checked both against held rows and only one failed.**
- "More than 7,000 jobs gone" / aggregate 2026 totals (trendingtopics, CryptoJobsList, layoffhedge, Ratelys, informationweek, CCN, Yahoo) — **not entered**, consistent with every prior run. Aggregator totals over an undefined perimeter; `_industry-scale-denominator-2026-08-10.md` exists because these are not comparable to a 26-row tracker of firm-stated events.
- **PIP Labs (Story Protocol) −10% — not re-surfaced today; the 09-01 final decline stands.**

### 6. NorthPoint longitudinal panel

Panel unchanged (79 days stale). **Day-63 entry appended to `findings/longitudinal-2026-06.md` — the first post-ship entry.**

---

## Guards run

| Guard | Result |
|---|---|
| `daily-corpus-sync.py` feed-health | 🟢 **HEALTHY**, both predicates pass, unassisted, third consecutive day. ⚠ Delta **−46**, largest negative on record, and today it is **traceable to lost instrument reach rather than market movement** — watch (an) advanced with its first mechanism, not just its first size |
| **`daily-corpus-sync.py` window freeze (NEW)** | 🟢 **FIRST RUN, and its first run is a test of the guard, not of the corpus** (watch tt). Discrimination verified three ways: default FREEZES (exhibits md5-identical to `HEAD`), `--window-end none` and `--window-end 2026-12-31` both WRITE and reproduce the exact 09-01/09-02 defect in a scratch copy. Idempotent across three runs |
| `verify-capture.py` | **Not run — correctly.** No register CSV was captured. Recorded, not silently skipped |
| `date-provenance-audit.py` | 🟢 **exit 0.** `EXEMPT-INSTRUMENT=1 · LAG-EXCEEDED=2 · NO-URL-DATE=14 · SELF-DATED=18 · UNPARSEABLE-DATE=1` — **identical to 09-01. Zero date inversions, zero citationless rows corpus-wide, fourth consecutive run.** 17 rows remain unaudited by the predicate |
| window-vs-`as_of` check | 🟢 **NO LONGER BY HAND.** Yesterday this check existed only because a run happened to re-read the window sentence. Today it is code, and it caught both the roll and the new Gemini row without being asked |
| slug-vs-label reconciliation | **Not run — nothing to reconcile, permanently.** Published as a disclosure |
| first-party citation read | **Not run — nothing new admitted.** Content-read total stands at **1 of 26 class-5 rows and 1 of 10 class-4 files.** The honest number, unchanged, and the appendix states it |

⚠ **`SELF-DATED` still means the citation and the corpus agree on a date — not that either is right, and not that the source supports the claim.**

---

## Watch items

- **(b) First named post-deadline EU NCA marketing-side action** — 🟢 **NOT ADVANCED. NULL HOLDS AT DAY 63**, now under maintenance rather than under test. A €540m aggregate was refused today precisely because it resembles a break and is not one.
- **🆕 (ao) A guard can be right and be the wrong question** — 🟢 **CLOSED IN CODE, 24 hours after it was opened.** `CAPTURE_WINDOW_END`, red-proofed three ways. **The fastest close in the cycle, because the defect recurred the next morning exactly as predicted.**
- **(ai) A derived file can date itself from the run clock** — 🟢 **CLOSED FOR THE POST-WINDOW CASE.** ⚠ **The in-window form is UNFIXED and stays open**: while a window is open, `as_of` still comes from the run clock rather than the artifact (the original 08-29 instance). `methodology.md` §1 now says which half is fixed.
- **🆕 (ap) 🔴 THE ABSENCE PANEL'S MEMBERSHIP CAN MOVE ON INSTRUMENT NOISE ALONE.** Gemini entered on a *timeout*, not a 404 or a proprietary ATS — a class the panel had never contained. Five firms had been stable across every in-window run; one transient network failure changed that, **and simultaneously halved the crypto cohort's open-marketing-role count (watch ag, 2 → 1).** Absence-as-data survives only while absence is *durable*; a timeout is not.
- **(an) A negative fingerprint delta passes a predicate written for a zero one** — ⚠ **ADVANCED, first mechanism.** −46, and it moved because the scanner lost a company, not because the market moved. **Not patched** — one predicate per run, and the fix needs normalising against `companies_via_api`, which is design, not a line edit.
- **(am) A search-result summary can garble what it summarises** — ⚠ **THIRD CONSECUTIVE RUN, and escalating in kind:** 08-31 merged adjacent sections; 09-01 produced three mutually inconsistent dates; **today it asserted a wrong CEO for a tracked firm — the same person as the 08-31 merge, now promoted from a neighbouring section into Coinbase's chair.** The corpus's held row is what caught it, all three times.
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — 🟢 **PAID OUT, FOURTH CONSECUTIVE RUN, and today with a real specimen:** an undated July-2025 appointment at a tracked Stratum-1 firm, presented inside a 2026 frame, fitting Theme 1 comfortably. Refused on date and on class.
- **(ag) Where the marketing hiring actually went** — ⚠ **ADVANCED TO n=7 AND THE SERIES BROKE FOR AN INSTRUMENT REASON.** 25:2 → **24:1**. Still not a corpus entry; the handling rule is published.
- **(mm) A rendering of the record is not the record** — 🟢 **HELD.** Eleven trade-press renderings of held primaries refused.
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — 🟢 **HONOURED.** The window freeze was red-proofed before being believed, and the negative-delta predicate was **not** patched in the same run.
- **(d) Agency panel staleness — 79 days** — 🟢 **CLOSED**, holding. Byte-identical twenty-two runs.
- **(e′) Cadence** — 🟢 **BOTH CLOCKS HELD.** 63 records / 63 days; feed unassisted three consecutive days.
- **(al) A URL that resolves is not a company that matches** — 🟢 **CLOSED AS A DISCLOSURE.** Post-window it can never recur.
- **(ad) The absence panel has never contained an absence** — **UNCHANGED** in the sense that matters (no firm is in it for being silent), but see 🆕 (ap): its membership is now demonstrably noise-sensitive.
- **(ak) A captured primary is a snapshot of an artifact that keeps moving** — **UNCHANGED**, not re-tested; nothing captured today.
- **(vv) A number is not safe until someone has read its citation** — 🟢 **DISCHARGED INTO THE REPORT**, unchanged.
- **Unchanged and not re-narrated today:** (a), (c), (e), (f), (g), (h), (h′ — REJECTED), (i), (j), (k), (l), (m), (n), (o), (pp), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (ab — CLOSED), (ac), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (nn), (oo), (qq), (rr), (uu), (ww), (xx — CLOSED), (yy), (zz — CLOSED), (ae — CLOSED), (af — CLOSED), (ah), (aj).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` **unpatched**, deliberately, to observe rather than assume → HEALTHY, 3401 → 3355, delta **−46**; 0 postings; **`as_of` rolled on both exhibits AND a Gemini row added.**
2. `git diff` on the three sync-written files → defect confirmed and characterised; both exhibits **restored byte-for-byte by truncate-and-write-in-place** (the mount refuses `unlink`, so `git checkout --` fails with `Operation not permitted`); md5 verified against `HEAD`.
3. Upstream `scan_metadata`, `new_since_last_scan` (**2 rows, both AI labs**), `still_open_from_prior_scans` (40 rows, counted by company), `fetch_errors` (**5**), `drops_summary`, `_feed-fingerprint.json` read directly → watch (ag) recounted at **24:1**.
4. **Patched `scripts/daily-corpus-sync.py`** — `CAPTURE_WINDOW_END`, `--window-end`, `count_new_rows()` dry run, freeze banner, absence-drift banner. **Red-proofed three ways in a scratch copy at `/tmp`, since removed.** `scripts/README.md` and `methodology.md` §1 updated to match.
5. WebSearch — ESMA / BaFin / AMF / CONSOB / CySEC crypto marketing enforcement, September 2026 → **0 net-new primary.** One already held; the rest vendor explainers.
6. WebSearch — **FCA / HTX High Court consent-order outcome** → **no outcome published.** Null recorded; nothing inferred from the stay.
7. WebSearch — crypto CMO / VP Marketing / Head of Growth moves, September 2026 → **0 net-new.** Pagliari surfaced undated.
8. WebSearch — **Pagliari targeted, to date the item before adjudicating it** → resolves to **July 2025**. Refused. **This search existed only because the first summary carried no date** — the discipline that turned a plausible admission into a recorded refusal.
9. WebSearch — crypto layoffs naming marketing teams, Aug/Sep 2026 → **0 net-new events.** Coinbase misattribution caught against the held row.
10. WebSearch — MiCA marketing-communications breach, named CASP, NCA fine → **0 net-new.** €540m aggregate refused; Art. 111 ceilings refused as statute.
11. WebSearch — MAS / VARA marketing enforcement 2026 → **0 net-new.** VARA held at source, fifth re-surfacing; MAS item is vendor-described powers, no instrument.
12. Repo greps: `Pagliari` (none), `Luno`, `VP of Growth`, `Growth and Media` → prior adjudications located before adjudicating anything.
13. `queues/needs-jukka.md` searched for an answered row before raising anything → **row 756 is OPEN; not re-asked, not duplicated.**
14. `python3 scripts/date-provenance-audit.py` → **exit 0**, zero inversions, zero citationless rows, distribution identical to 09-01.
15. **No URL was fabricated. No figure was entered that its source did not state. No absence claim was made from an unobserved scan. No post-window class-1 row was admitted. No register was re-fetched. No paywall was circumvented. No published external content was edited. No scheduled task was created, disabled or rescheduled. This loop's own prompt was not patched.**

---

## Net-new / changed this run

- `scripts/daily-corpus-sync.py` — **the run's finished unit of work.** `CAPTURE_WINDOW_END = "2026-08-31"` + `--window-end` + `count_new_rows()` + two banners. Closes watch (ao); closes watch (ai) for the post-window case. **Red-proofed three ways.**
- `scripts/README.md` — new § *Class-1 capture-window freeze*, with the artifact table, the two dated incidents that caused it, and the discrimination table.
- `methodology.md` §1 — two additions: the **post-window absence-panel drift** (Gemini, timeout, five-vs-six) and the 🟢 **patched** half of the run-clock `as_of` limit, with the unfixed in-window half stated as still open.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — 🟢 **`as_of` HELD AT 2026-08-31, now by code.** Restored byte-for-byte after the unpatched run rolled them.
- `corpus/job-postings/_feed-fingerprint.json` — sync write, **09-02 entry kept** (instrument log). 22nd run.
- `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — byte-identical, **22nd consecutive run.**
- `findings/longitudinal-2026-06.md` — **day-63 entry appended.** First post-ship entry.
- `corpus/weekly-runs/2026-09-02-corpus-run.md` — this record. **63rd consecutive.**
- **Deliberately NOT written:** any post-window class-1 row; any `as_of` past 2026-08-31 on a shipped exhibit; the Gemini absence row; any patch to the fingerprint predicate; any self-patch of this loop's prompt; any change to the scheduler; any admission of the Pagliari, €540m, MAS-powers, VARA or aggregate-layoff-total items; any FCA/HTX outcome inferred from the stay; any edit to the published May 13 essay (external, hard-gated, Jukka's hand).

---

## For Jukka

1. 🟢 **THE DAILY HAND-CORRECTION IS GONE.** Yesterday's record said the sync would roll two shipped exhibits' dates again today. It did — **and also tried to add Gemini to the absence panel**, which would have changed what a shipped exhibit *says*, not just its date. Both restored; **the rule is now in code and red-proofed both ways**, so this cannot recur whoever runs it.
2. 🔴 **ROW 756 IS STILL YOURS AND I AM NOT RE-ASKING IT — but it is now a cleaner decision than it was yesterday.** It read *retire the loop, or tell it what a post-window run is for.* The patch removes the "hand-correct an exhibit every morning" cost from the keep branch, so the choice is simply **keep or retire**. My read is unchanged: classes 3–5 are worth keeping as a living register for the next cycle; class 1 is now frozen in code rather than by hand. **Scheduler is your click either way.**
3. ⚠ **THE MOST INTERESTING THING TODAY IS A NUMBER THAT MOVED FOR NO REASON.** Gemini's job board timed out, and with it the crypto cohort's open-marketing-role count went **2 → 1** while the AI-lab count went 25 → 24. **Half the crypto side of a ratio Theme 2 was going to quote vanished on a network error.** It is not in the corpus and never was — but if that number ever reaches the report, it needs the denominator sentence from `findings/appendix-scope-of-the-citation-index.md` §3 next to it, not on its own.
4. **Still yours, still outside this repo:** the May 13 essay *"Binance lost its CMO too"* states the reading the corpus struck on 08-31 (row 751). Amend, append a correction, or accept the disagreement.
5. **Post-ship backlog, unchanged and none of it blocking:** the fingerprint negative-delta predicate (watch an — **now with a real mechanism**, normalise against `companies_via_api`); `**Published:**` on the five class-4 files missing it; the in-window half of the run-clock `as_of` (watch ai). **Nothing here needs a decision today.**
