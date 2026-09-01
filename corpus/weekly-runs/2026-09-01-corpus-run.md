# Corpus-assembly daily run — 2026-09-01 **(day 62 post-deadline · SHIP DAY · FIRST POST-WINDOW RUN)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-09-01 (**Tuesday — the report ships today**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-31 recommendations:** (1) the pre-ship defect queue is empty — **do not manufacture work to fill it**; (2) row 736 (the published May 13 essay) is Jukka's hand, not this loop's; (3) the two appendix sentences are wanted; (4) the AI-lab observation should reach Theme 2; (5) fingerprint-predicate patch, slug reconciliation and the class-4 `**Published:**` backfill are all explicitly **post-ship, not today**.
**Dedup baseline read before writing:** `2026-08-31-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`; `findings/longitudinal-2026-06.md` tail (three most recent entries); directory indexes for `regulator-filings/` (40), `operator-statements/` (10), `findings/` (5 → 6), `weekly-runs/` (61 → 62); `layoff-tracker/2026-layoff-tracker.csv` all 26 rows; `vara-enforcement-register-at-source-2026-08-14.md` head; upstream `scan_metadata`, `new_since_last_scan`, `still_open_from_prior_scans`, `fetch_errors`, `drops_summary` and `_feed-fingerprint.json` read directly; repo-wide greps for `PIP Labs`, `eToro`, `ESMA supervis`, `single supervisor`, `Austrian`.
**🟢 CADENCE (this loop): HELD. 62 run records for 62 post-deadline days.**
**🟢 CADENCE (the upstream feed): HELD, unassisted, second consecutive day.**

---

## Headline result

**The window closed yesterday, so today the feed's health became a fact about the instrument rather than a fact about the report — and the first thing that changed under the new rule was a date the sync wrote automatically.**

### 1. 🔴⭐ **A HEALTHY FEED PRODUCED AN INADMISSIBLE FILE, AND NOTHING IN THE REPO WOULD HAVE STOPPED IT SHIPPING.**

Class 1's capture window is **"rolling 12 months ending August 31, 2026"** — stated identically in `methodology.md` §1, `README.md` and the public `README-for-github.md`. It closed yesterday, honestly, on a scan that ran.

Today's scan also ran, and passed both predicates:

```
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-31T22:01:36Z, age=14.0h,
  fingerprint total_jobs_fetched=3401, delta=+4 vs 2026-08-31 (3397))
  reason: age 14.0h, fingerprint delta +4
job postings ADDED: 0  firms: []
```

**Both facts are true and they now point in opposite directions.** The feed is live; its output is out of window. `daily-corpus-sync.py` has no concept of the window — it was built to answer *did the scan look?*, and it answers that correctly every day, including days whose answer the report may not use. **A guard that has been right sixty-two times running became, today, the wrong question.**

Zero postings were added, so no out-of-window *posting* entered the corpus. But the sync also writes derived files, and one of them moved:

**`_absence.csv` and `_chrome-queue.csv` rolled their `as_of` from `2026-08-31` to `2026-09-01` — no membership change, no content change, only the date.** The absence panel is a **shipped Theme-1 and Theme-4 exhibit**: it is the artifact that says *Binance, Bybit, HTX, KuCoin and Aave are absent because the scanner could not reach them, not because they were silent.* Shipping it stamped `2026-09-01` would have had the report's own absence exhibit assert an observation date **outside the window all three public documents advertise** — a one-day discrepancy, in the exact register the report criticises in other firms' estates.

🟢 **ACTION TAKEN — both files restored to their 2026-08-31 content, byte-for-byte** (verified: `git status` clean on both; CRLF line endings preserved, which a naive rewrite had silently stripped on the first attempt and `git diff` caught).

🟢 **`_feed-fingerprint.json` KEPT its 2026-09-01 entry.** The distinction is the point: **the fingerprint file is an instrument log and should record that a 09-01 scan ran; the absence panel is a corpus claim and must stay pinned to the window's close.** Watch (ai) — *a derived file can date itself from the run clock* — has been **DORMANT-NOT-FIXED for eleven runs**. Today is the first day the drift was not cosmetic, and it bit on ship day.

### 2. ⚠ **THE POST-WINDOW STATE IS NOT WRITTEN DOWN ANYWHERE, AND THIS LOOP IS STILL SCHEDULED TO RUN TOMORROW.**

There is no instruction in the repo, in `methodology.md`, or in this loop's own prompt covering **what a corpus run does after its capture window closes.** Sixty-one records were written under a rule — *capture, verify, admit* — that expired at midnight. Today's run inferred the rule (`classes 3/4/5 continue; class 1 is frozen at 08-31; derived class-1 files must not re-date`) and applied it, but **inferred it; it is not contracted.** Tomorrow's run will start from the same silence, and the day after that.

**This is a live risk, not a philosophical one:** the sync will roll `as_of` again tomorrow, and the correction made today was made by a run that happened to be reading the window sentence for another reason. **Filed for Jukka as the single post-ship decision** (see below): either the loop is retired at ship, or its prompt gains a post-window clause. Not self-patched — the prompt-patch guard permits self-patching, but a **scope change of this size on ship day, to handle a case that has been correctly handled once, is precisely the trade watch (tt) warns against.** Recorded, not acted on.

### 3. 🟢 **THE THREE SEARCH CLASSES CLOSED THE CYCLE AT ZERO, AND THE NULLS ARE THE FINDINGS.**

- **Watch (b) — the EU-NCA marketing-side enforcement null SHIPS INTACT at day 62.** *No EU national competent authority has published a named marketing-side enforcement action against a CASP since the MiCA transitional deadline.* Searched again today across ESMA/BaFin/AMF/CONSOB/CySEC vocabulary; returned only vendor and law-firm explainers, one supervisory-architecture story, and items the corpus already holds. **This is one of the report's principal findings and it survived every day of the cycle.**
- **FCA v HTX — NULL RE-CONFIRMED ON SHIP DAY.** The High Court stay was listed to expire "late August". Today is 1 September. **No outcome is published**; the most recent primary-adjacent reporting is still the mid-August settlement-talks coverage the corpus holds (`fca-htx-promotions-consent-order-stay-2026-08-28.md`). **The report ships with the stay unresolved, which is the true state of the record.** Nothing inferred from the calendar, on the second consecutive day it would have been easy to.
- **Class 4: 0 net-new, and the refusal set is unchanged.** NorthPoint's own press release refused for the **sixth** consecutive run.
- **Class 5: 0 net-new events.** Tracker holds at **26 rows, 26 citations.** Every firm surfaced today (Coinbase, Kraken, Crypto.com, Gemini, Algorand, OP Labs, Messari, BitGo, Bitwise) is already held.

### 4. ⚠ **THE RETRIEVAL LAYER GARBLED A DATE AGAIN, ON A REGISTER THE CORPUS HOLDS AT SOURCE — WATCH (am), SECOND CONSECUTIVE RUN.**

A class-3 search for VARA marketing enforcement returned a summary stating that the enforcement actions covered *"the past six months, including August 2026"*, that *"the most recent entries date back to August"*, and — in the same paragraph — that *"the formal announcement was made in October 2025."*

**Three mutually inconsistent temporal claims, one of which is the query's own date reflected back.** The corpus holds this register **at source**: `vara-enforcement-register-at-source-2026-08-14.md`, 37 transcribed rows, and the 19-firm action is its **7 October 2025** notice — captured, dated, and unambiguous. Nothing was admitted; nothing needed re-fetching.

⚠ **The instructive part is what would have happened without the at-source capture.** A corpus built on search summaries would have had a plausible route to recording a *2026* VARA marketing action — which, in a report whose headline regulator finding is a **null**, is the single most damaging false positive available. **The 08-14 method change ("change the method, not the vocabulary") paid its final dividend on the last day of the cycle.**

### 5. ⚠ **A SECOND SUMMARY OFFERED A YEARLESS DATE FOR A NON-COHORT FIRM, AND YEARLESS IS THE FAILURE MODE THE DATE GUARD CANNOT SEE.**

The same class-3 pass returned: *"eToro received a MiCA authorisation from BaFin on September 16 after gaining a MiCA licence from CySEC in February."* **No year, on either date.** Refused twice over — eToro is outside the cohort, and an authorisation is not a marketing-side enforcement action — so nothing rested on it. But it is worth recording that `date-provenance-audit.py`'s predicate is *URL-path date vs. recorded date*, and **a bare "September 16" in prose never reaches a URL path.** Same family as watch (am); noted, not made into a new watch on ship day.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`) — **FROZEN AT THE WINDOW CLOSE**

```
date: 2026-09-01   source A (jobs) scan_date: 2026-09-01
FEED HEALTH: HEALTHY (age=14.0h, 3397 → 3401, delta=+4)
job postings ADDED: 0  firms: []   of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance','Bybit','HTX','Kucoin','Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave','Binance','Bybit','HTX','Kucoin']
```

`companies_scanned` **147** · `companies_via_api` **99** · `companies_via_chrome_pending` **48** · `fetch_seconds` **34.8** · `total_jobs_after_filter` **45** · `new_count` **0** · `still_open_count` **42** · `url_verification_dropped` **3**.

Fingerprint series:

```
… 3334 → [no 08-26] → 3356 → 3362 → 3362(frozen) → 3398 → 3397 → 3401
                                                              ↑ 08-31 (window closes)  ↑ TODAY (post-window)
```

⚠ **The +4 is a real delta on a live board and it is the first class-1 movement the report cannot use.** `new_since_last_scan` is **empty** — the four are non-cohort or filtered — so the question never became live. Had one of the four been a tracked-firm marketing role, it would have been **observed, verified, dated, and inadmissible.** Recorded as the concrete shape of headline 1.

`fetch_errors`: the same four stable 404s (Wormhole Foundation, Aave, Bitwise, Chainlink Labs) — **unchanged for the twelfth consecutive run**, which is the evidence they are structural rather than transient. `drops_summary` unchanged in shape (`exclude_function` 2581 · `no_marketing_keyword` 623 · `no_seniority_signal` 105 · `exclude_seniority` 30 · `tracker` 13 · `exclude_location` 4).

**Absence panel: 5 firms, membership unchanged since the cohort expansion.** 🟢 **`as_of` HELD AT 2026-08-31 by hand** — see headline 1. This is the first run in which the panel's date was written by a decision rather than by the clock.

**Watch (ag) — ADVANCED TO n=6, and the series held flat across the window's close.** `still_open_from_prior_scans` holds **OpenAI 12 · Anthropic 8 · Cohere 3 · Perplexity 2 = 25** open AI-lab marketing/comms roles against **Gemini 1 · Phantom 1 = 2** for the entire Stratum 1–4 crypto cohort — **identical to 08-31.** ⚠ **Not a corpus entry**; AI labs are outside the cohort and no claim is derived from them. Handling language for Theme 2 is now written down rather than restated: `findings/appendix-scope-of-the-citation-index.md` §3.

⚠ **Slug-vs-label reconciliation: NOT run, NOT automated — third consecutive run in which it is neither honoured nor dischargeable.** Zero postings added, nothing to reconcile. It is a build item and it is now **published rather than carried**, as §2 of the appendix file. Watch (al) closes as a *disclosure*, not as a fix, and the record says which.

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 78 days stale.** 18 agency-claims files written, **byte-identical for the twenty-first consecutive run.** 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation. Watch (d) stays **CLOSED**: the real last-refresh date is stated in every public document, so the staleness ships published rather than merely known.

### 3. Regulator — **0 NET-NEW.**

| Surfaced | Disposition |
|---|---|
| ESMA statement — unauthorised CASPs to wind down and **cease marketing activities and solicitation** | **ALREADY HELD** at source (`esma-mica-transitional-period-end-2026-06.md`); the AMF mirror adds nothing. Fourth consecutive re-surfacing |
| **VARA — 19 firms fined, penalties $27k–$163k, breaches of the 2024 Marketing Regulations** | **ALREADY HELD AT SOURCE.** `vara-enforcement-register-at-source-2026-08-14.md` transcribes the register (37 rows) and the underlying **7 Oct 2025** notice. ⚠ The summary's dating was internally contradictory — see headline 4. **Primary stands; nothing re-fetched** |
| **AMF + Austrian FMA + CONSOB call for ESMA to supervise crypto firms centrally** | 🔴 **REFUSED ON SCOPE.** Supervisory architecture, not a marketing-side enforcement action. The corpus has touched this thread before (07-04, 08-13) and admits nothing from it. **It does not weaken watch (b); a call for centralised supervision is not a published action** |
| ESMA staff knowledge-and-competence guidelines (apply from 28 July) | 🔴 **REFUSED ON SCOPE**, third consecutive run. Staff competence, not marketing communications |
| **eToro — MiCA authorisation from BaFin, "September 16"; CySEC licence "February"** | 🔴 **REFUSED TWICE OVER.** Non-cohort firm; authorisation is not enforcement. ⚠ **Both dates yearless** — headline 5 |
| **FCA v HTX — stay listed to expire "late August"** | 🔴 **NULL CONFIRMED ON SHIP DAY.** Today is 1 September and **no outcome is published.** Searched specifically; found only the mid-August settlement-talks reporting already held. **Nothing guessed, nothing inferred from the expiry** |
| Vendor / law-firm MiCA explainers (Sedric, Trusty, InnReg, Lexology, Adam Smith, financialregulations.eu, New Balkans, finconduit) | **REFUSED.** Secondary commentary; no regulator speaks in any of them and no tracked-firm operator is quoted |

**Watch (b) — NOT ADVANCED. 🟢 THE NULL SHIPS INTACT AT DAY 62**, in its narrow, defensible form: *no EU national competent authority has published a named marketing-side enforcement action against a CASP since the MiCA transitional deadline.* The FCA/HTX action is UK s.21 FSMA and is excluded by its own record; VARA is Dubai and is held separately at source, where the marketing-side actions are real, named, and **pre-deadline**.

**Not fetched, not guessed:** `CASPS.csv`, `OTHER.csv`, `NCASP.csv`, MAS, the retry queue, the four un-fetched FCA orders, VARA's Shelbit / MEXC / CoinMENA notice bodies, `rulebooks.vara.ae`. **All standing prohibitions honoured.**

### 4. Operator statements — **0 NET-NEW.**

| Surfaced | Disposition |
|---|---|
| **CoinDesk — Binance CMO Rachel Conlan exit / Eowyn Chen interim (2026-05-12)** | **ALREADY HELD.** Captured first-party yesterday (`binance-conlan-cmo-exit-primary-2026-08-31.md`). Re-surfacing is confirmation the capture found the right artifact |
| **Coinbase — Catherine Ferdon appointed CMO (ex-Cash App)** | **ALREADY HELD** (`coinbase-ferdon-marketing-vanguard-2026-04.md`). ⚠ The summary offered it as a possible September-2026 appointment and then corrected itself to September 2025 in the same paragraph — **the corpus's dated capture is what made that self-correction checkable rather than persuasive** |
| Blockchain.com — "Announcing our new VP of Marketing" (Medium, Peter Smith) | 🔴 **REFUSED.** Non-cohort firm, and the item carries **no date at all** in the result. Not fetched; nothing rested on it |
| **NorthPoint's own press release** (natlawreview, 2026-08-14) | 🔴 **REFUSED — sixth consecutive run.** Our own promotional material; the author is not a tracked-firm operator. **The report does not cite its own author's PR** |
| "Top Digital Assets Marketing Leaders in 2026" listicles; job boards (Wellfound, Indeed, cryptocurrencyjobs) | **REFUSED.** Aggregators and directories; no operator speaks |

**Watch (l), 28th costing — WEAK.** Today's refusal set is valid at any §4 width; nothing excluded had Theme bearing. The Ben Zhou marginal case from 08-31 is unchanged and stays recorded rather than re-litigated.

### 5. Layoffs — **0 NET-NEW EVENTS. Tracker holds at 26 rows, 26 citations. Zero edits.**

Search returned the March-2026 cluster and the H1 aggregate reporting: **Gemini, Crypto.com, Algorand, OP Labs, Messari, Coinbase (700), Kraken (150), Crypto.com (180), BitGo, Bitwise** — **all held**, several with the corpus's own adjudications already attached (Crypto.com's ~180 and Gemini's struck 200 are outlet arithmetic; MARA's 40 likewise, repaired 08-30).

- **PIP Labs (Story Protocol) −10%, ~17 March 2026 — STILL DECLINED, and the decline is now final.** Surfaced again inside aggregate reporting. It has never arrived other than as a rendering of a record (watch (mm)); it was declined on 08-21 with its URL captured, and **ship day is not the moment to admit a row on a standard that would not have admitted it on any prior day.** Consistency over completeness.
- Three aggregators (CryptoJobsList, trueup, Medium/Blockchain-Today) not admitted — **consistent with every prior run.**
- ⚠ The "5,000+ / 5,700+ crypto jobs cut in 2026" headline figures were **not** entered. They are aggregator totals over an undefined perimeter; the corpus's own denominator work (`_industry-scale-denominator-2026-08-10.md`) exists precisely because these numbers are not comparable to a 26-row tracker of firm-stated events.

### 6. NorthPoint longitudinal panel

Panel unchanged (78 days stale). **Day-62 entry appended to `findings/longitudinal-2026-06.md` — the ship-day entry, and the last of the assembly cycle.**

---

## Guards run

| Guard | Result |
|---|---|
| `daily-corpus-sync.py` feed-health | 🟢 **HEALTHY**, both predicates pass, unassisted, second consecutive day. ⚠ **And for the first time the verdict is not the question the report is asking** — headline 1. Delta +4, first positive since the negative-delta anomaly; watch (an) untested and unpatched, correctly |
| `verify-capture.py` | **Not run — correctly.** No register CSV was captured this run. Recorded, not silently skipped |
| `date-provenance-audit.py` | 🟢 **exit 0.** `EXEMPT-INSTRUMENT=1 · LAG-EXCEEDED=2 · NO-URL-DATE=14 · SELF-DATED=18 · UNPARSEABLE-DATE=1`. **Zero date inversions, zero citationless rows corpus-wide — held for the third consecutive run, and the corpus ships in that state.** ⚠ `SELF-DATED` moved **17 → 18**: yesterday's Binance capture now carries a URL-path date the predicate can check. **This run first wrote 17 from yesterday's record and the audit corrected it** — a small instance of the rule the whole cycle rests on: *the number comes from running the thing, not from the last run that ran it* |
| **window-vs-`as_of` check (by hand, new)** | 🔴 **1 defect found, 1 fixed.** Two derived CSVs had re-dated themselves past the window close. **This check does not exist as code** and was performed only because the run was re-reading the window sentence for another reason. Its absence is the substance of headline 2 |
| slug-vs-label reconciliation | **Not run — nothing to reconcile** (0 postings added). **Now published as a disclosure** rather than carried as a recommendation |
| first-party citation read | **Not run — nothing new admitted.** The cycle's content-read total stands at **1 of 26 class-5 rows and 1 of 10 class-4 files.** ⚠ **That is the honest number, and the appendix language now states it** |

⚠ **`SELF-DATED` still means the citation and the corpus agree on a date — not that either is right, and not that the source supports the claim.** 17 rows remain unaudited by the date predicate; **all remain unaudited for content.** The report ships with that queue open **and with the queue disclosed**, which is the difference this run was able to make.

---

## Watch items

- **(b) First named post-deadline EU NCA marketing-side action** — 🟢 **NOT ADVANCED. NULL SHIPS INTACT AT DAY 62.** The cycle's principal regulator finding, unbroken on every one of 62 days.
- **(d) Agency panel staleness — 78 days** — 🟢 **CLOSED**, holding. Byte-identical twenty-one runs; published in every public document.
- **(e′) Cadence** — 🟢 **BOTH CLOCKS HELD TO THE LAST DAY.** 62 records / 62 days; the feed ran unassisted on both of the two days it mattered most.
- **(ai) A derived file can date itself from the run clock** — 🔴 **BIT FOR THE FIRST TIME, AND ON SHIP DAY.** Dormant for eleven runs while the drift was cosmetic; the moment the window closed it became a shipped exhibit asserting an out-of-window date. **Corrected by hand.** ⚠ **Still not fixed in code — it will recur tomorrow.**
- **🆕 (ao) 🔴 A GUARD CAN BE RIGHT AND BE THE WRONG QUESTION.** `daily-corpus-sync.py` answers *did the scan look?* — correctly, every day, including days whose answer is inadmissible. **Nothing in the repo knows the capture window has an end.** The feed-health banner will print HEALTHY every day of September and every one of those verdicts is now irrelevant to the report. **A post-window run needs a different guard, or no run at all.**
- **(am) A search-result summary can garble what it summarises** — ⚠ **SECOND CONSECUTIVE RUN.** Yesterday it merged two adjacent sections of one page; today it produced **three mutually inconsistent dates for one VARA action, one of them the query's own date reflected back.** ⚠ **New sub-form: a yearless date in prose is invisible to `date-provenance-audit.py`, whose predicate lives in URL paths** (headline 5). **The at-source capture is what made both harmless.**
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — 🟢 **PAID FORWARD, THIRD CONSECUTIVE RUN.** Nothing today confirmed strongly enough to be dangerous, which is itself the quiet version of the payout.
- **(vv) A number is not safe until someone has read its citation — extended to claims** — 🟢 **DISCHARGED INTO THE REPORT.** No longer only a watch: the appendix language now states what the citation index certifies and what it does not, in publishable form.
- **(al) A URL that resolves is not a company that matches** — 🟢 **CLOSED AS A DISCLOSURE, NOT AS A FIX.** Published in the appendix file with its real 08-30 instance. The reconciliation remains unautomated and the record says so.
- **(ag) Where the marketing hiring actually went** — 🟢 **ADVANCED TO n=6.** 25:2, flat across the window's close. Handling language written for Theme 2.
- **(an) A negative fingerprint delta passes a predicate written for a zero one** — **UNTESTED, UNPATCHED, CORRECTLY.** Today's delta is +4. Post-ship item.
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — 🟢 **HONOURED TWICE.** No fingerprint patch; no self-patch of this loop's prompt for the post-window case, on the day a scope change is least testable.
- **(mm) A rendering of the record is not the record** — 🟢 **HELD TO THE LAST DAY.** PIP Labs declined for the fourth time on the same standard that declined it first.
- **(ad) The absence panel has never contained an absence** — **UNCHANGED.** Permanent in `methodology.md` §1.
- **(ak) A captured primary is a snapshot of an artifact that keeps moving** — **UNCHANGED**, not re-tested; nothing captured today.
- **Unchanged and not re-narrated today:** (a), (c), (e), (f), (g), (h), (h′ — REJECTED), (i), (j), (k), (m), (n), (o), (pp), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (ab — CLOSED), (ac), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (nn), (oo), (qq), (rr), (uu), (ww), (xx — CLOSED), (yy), (zz — CLOSED), (ae — CLOSED), (af — CLOSED), (ah), (aj).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.0h, 3397 → 3401, delta +4.** 0 postings added; 18 agency files; 8 matrix rows; Sui overlap unchanged.
2. Upstream `scan_metadata`, `new_since_last_scan` (**empty**), `still_open_from_prior_scans` (42 rows, counted by company), `fetch_errors`, `drops_summary`, `_feed-fingerprint.json` read directly → post-window state established; watch (ag) recounted at 25:2.
3. `git diff` on the three sync-written files → **`as_of` roll detected**; both CSVs restored to 08-31 content; **CRLF endings verified preserved** after a first restore attempt stripped them (caught by `git diff | cat -A`, not by inspection).
4. WebSearch — ESMA / BaFin / AMF / CONSOB / CySEC crypto marketing enforcement, September 2026 → **0 net-new primary.** One already held, three scope refusals, rest secondary.
5. WebSearch — **FCA / HTX High Court consent-order outcome** → **no outcome published on ship day.** Null recorded; nothing inferred from the stay's expiry.
6. WebSearch — VARA Dubai marketing enforcement, August 2026 → **already held at source**; summary's three-way date contradiction recorded as watch (am).
7. WebSearch — crypto CMO / VP Marketing / MiCA marketing compliance, August 2026 → **0 net-new.** NorthPoint's own PR refused (6th).
8. WebSearch — crypto CMO / VP Marketing appointments, September 2026 → **0 net-new.** Ferdon already held; Blockchain.com item undated and non-cohort.
9. WebSearch — crypto layoffs 2026 naming marketing teams → **0 net-new events.** All firms held; PIP Labs declined 4th; aggregate totals not entered.
10. WebSearch — CASP sanction for misleading marketing communication under MiCA → **0 net-new.** Entirely vendor and law-firm explainers; **no regulator and no named firm.**
11. Repo greps: `PIP Labs`, `eToro`, `ESMA supervis`, `single supervisor`, `Austrian` → prior adjudications located before re-adjudicating any of them.
12. `python3 scripts/date-provenance-audit.py` → **exit 0**, zero citationless rows, zero inversions. `SELF-DATED` **18** (up from 17 — yesterday's Binance capture is now checkable by the predicate); **17 rows remain unaudited by it.**
13. **No URL was fabricated. No figure was entered that its source did not state. No absence claim was made from an unobserved scan. No out-of-window class-1 row was admitted. No register was re-fetched. No paywall was circumvented. No published external content was edited. No guard predicate was changed on ship day.**

---

## Net-new / changed this run

- `findings/appendix-scope-of-the-citation-index.md` — **NEW. The run's finished unit of work.** Ready-to-paste appendix language in three blocks: **what the citation index certifies and what it does not** (discharging watch (vv) into the report); **the two class-1 limits** — slug-derived identity (watch al) and run-clock `as_of` (watch ai) — with their real recorded instances; and **Theme 2's AI-lab observation with its handling rule** (watch ag). Written because a recommendation Jukka has to re-derive into publishable sentences is a format problem, not a supply problem.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — 🟢 **`as_of` HELD AT 2026-08-31 by decision.** Restored byte-for-byte after the sync rolled them past the window close. **The first time these files' dates were written by a ruling rather than a clock.**
- `corpus/job-postings/_feed-fingerprint.json` — sync write, **09-01 entry KEPT** (instrument log, not a corpus claim). 21st run.
- `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — byte-identical, **21st consecutive run.**
- `findings/longitudinal-2026-06.md` — **day-62 ship-day entry appended.** The closing entry of the assembly cycle.
- `corpus/weekly-runs/2026-09-01-corpus-run.md` — this record. **62nd consecutive.**
- **Deliberately NOT written:** any class-1 row from today's post-window scan; any `as_of` past 2026-08-31 on a shipped exhibit; any patch to the fingerprint predicate; any self-patch of this loop's prompt for the post-window case; any admission of the VARA, eToro, Blockchain.com, PIP Labs or aggregate-total items; any FCA/HTX outcome inferred from the stay's expiry; any edit to the published May 13 essay (external, hard-gated, Jukka's hand).

---

## For Jukka — **THE REPORT SHIPS TODAY.**

1. 🟢 **THE CORPUS IS SHIPPABLE AND THE DEFECT QUEUE IS STILL EMPTY.** Sixty-two consecutive daily records. Class-1 capture window closed **2026-08-31 exactly as all three public documents advertise**, on a scan that genuinely ran — **and its exhibits are pinned to that date, checked today.** Corpus-wide citationless rows **zero**, third consecutive run. 26/26 layoff rows cited. **The EU-NCA marketing-enforcement null — the report's principal regulator finding — is intact at day 62.** The FCA/HTX stay is unresolved on the record and the report says so.
2. ⚠ **ONE THING TO PASTE, AND IT IS WRITTEN.** `findings/appendix-scope-of-the-citation-index.md` contains the two appendix blocks you asked for yesterday, final and ready. **The first one matters most:** it tells the reader that the citation index certifies *existence and dating*, not *that a source supports the sentence citing it* — and cites yesterday's Binance incident as the proof. A regulator-readable appendix that overstates its own warrant is the exact defect this report documents in other people's estates. **Block 3 belongs in Theme 2's body, not the appendix.**
3. 🔴 **ONE DECISION, AND IT IS ABOUT TOMORROW, NOT TODAY: THIS LOOP HAS NO POST-WINDOW CONTRACT AND IS STILL SCHEDULED.** The capture window closed yesterday; nothing in the repo or in this loop's prompt says what a corpus run does afterwards. Today's run inferred the rule and caught a real defect doing so — **two derived exhibits had already re-dated themselves past the window close, and would have shipped that way.** The sync will roll them again tomorrow. **Either retire the task at ship, or tell it what a post-window run is for** (my read: classes 3–5 stay valuable as a living register for the *next* cycle; class 1 should be frozen in code, not by hand). Not self-patched — a scope change on ship day is the trade watch (tt) exists to refuse.
4. **Still yours, still outside this repo:** the May 13 essay *"Binance lost its CMO too"* states the reading the corpus struck yesterday. Amend, append a correction, or accept that the report and the essay disagree — **the report being the more defensible of the two.**
5. **Post-ship backlog, unchanged and none of it blocking:** patch the fingerprint predicate for negative deltas (watch an); automate the slug reconciliation or leave it published (watch al, now disclosed); add `**Published:**` to the five class-4 files missing it; and **the one this run adds — teach the sync that its window has an end** (watch ao).

---

## Addendum — commit mechanics, recorded because a claim of cleanliness needs its caveat

**The commit landed by the alternate-index route** (`GIT_INDEX_FILE`), which is the workaround the 08-30 record wrote down for this mount. Parent asserted equal to `refs/heads/main` before the ref was written by hand, per that record's own warning — a concurrent Distribution Engineer commit would otherwise be silently discarded. **`76029dd` is on `main`, one ahead of `origin/main`, working tree clean.** `git push` was **not** attempted (no GitHub auth in autonomous runs); the DE pushes.

⚠ **One residue this run could not remove, stated rather than claimed away: a 0-byte `.git/index.lock`, created at 15:04 by this run's own first (failed) commit attempt.** `rm` and `mv` both return `Operation not permitted` — the standing FUSE limitation, in the same place row 737 hit it on 08-30. **It does not block the push** (push locks refs, not the index) and it did not block this commit, but it **will** block a future `git add` / `git commit` through the normal path until it is removed host-side.

🟢 **The working tree reads clean anyway, and it did not before.** After the alternate-index commit the on-disk `.git/index` was stale, so `git status` reported the two new files as simultaneously deleted and untracked — **a tree that looks dirty is a tree the DE may decline to push.** Rebuilt the index from `HEAD` into a scratch file and **wrote it over `.git/index` in place** (truncate + write needs no unlink — the same manoeuvre as the ref write). `git status` is now empty.

**No new queue row filed for the lock.** The product-builder already has an OPEN 2026-09-01 row covering 108 files of this exact class in `northpoint` and `monitoringroom`; a fourth row for one non-blocking empty file is queue noise, and **the standing rule is that the mount cannot unlink, so the file is reported and never claimed deleted.** If Jukka is running that card's `rm` anyway, this path can ride along:

```
rm "$HOME/Operating System/projects/state-of-crypto-marketing-2026/repo/.git/index.lock"
```
