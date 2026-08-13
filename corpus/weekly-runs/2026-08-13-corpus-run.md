# Corpus-assembly daily run — 2026-08-13 **(day 43 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-13 (**Thursday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, verbatim from the 08-11 recommendations:** (1) **execute watch (hh) first — re-fetch every failed-fetch URL**; (2) seed the (p) sweep's firm URLs, then run it; (3) fetch the RootData dead-projects list (2nd carry); (4) do the (dd)+(t′) sweep or kill it (5th carry); (5) re-test the remaining six sections of `sport-sponsorship-reset-2026-05.md` under watch (ii); (6) escalate eight items.
**Dedup baseline read before writing:** `2026-08-11-corpus-run.md` in full; all 23 tracker rows via `csv.DictReader`; directory indexes for `operator-statements/`, `regulator-filings/`, `layoff-tracker/`, `job-postings/`, `marketing-campaigns/`, `ad-platform-gates/`, `agency-claims/`; `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; `findings/longitudinal-2026-06.md` tail; `_industry-scale-denominator-2026-08-10.md`; repo-wide grep on "empty body / not usable / not reachable" to rebuild the retry queue; targeted grep on Bitwise across `corpus/` and `findings/`.
**🔴 CADENCE: BROKEN AGAIN. 08-11 → 08-13. NO RUN ON 08-12.** Watch (e′) needed four consecutive on-time runs after the last break; it got **one**. **Reset to 0 of 4.** The same 08-12 gap is recorded independently in `situation.md` for the convertor and the product-builder loops — **this was a portfolio-wide skip, not a corpus-specific one**, which is a materially different diagnosis and is escalated as such.

---

## Headline result

**Three things, and the first one says the top-priority recommendation of the last run cannot be executed by this run at all.**

**1. 🔴 WATCH (hh) — THE RETRY QUEUE — IS BLOCKED BY THE SAME TOOLING RULE THAT BLOCKED WATCH (p), AND THAT IS NOW A PATTERN, NOT AN INCIDENT.** The 08-11 record's recommendation #1 was *"re-fetch every 'empty body / not usable / not reachable' URL in the run records… the cheapest recall improvement in the repo."* The queue was rebuilt this run — **eight entries across seven run records** — and the first attempt, `bitstamp.net/bitstamp-way`, **was refused: `URL not in provenance set`.** A URL recorded in this repo's own audit trail is **not** a provenanced URL: the fetch tool accepts only URLs that appeared in a user message, a prior fetch result, or a search result **in the current run**. **The corpus can write a retry queue but cannot read from it.** A search-first workaround was tested on the same URL and **failed to surface it** — so the queue is not merely gated on search, it is gated on search *succeeding*. **The 08-11 Kalifowitz recovery, which produced that run's headline, worked only because a WebSearch happened to re-surface the URL. It was luck, and it has now been shown to be luck.** New watch **(jj)**. Escalated as item (i) — **this is the second top-priority recommendation in three runs to die on the identical constraint.**

**2. 🟢 CLASS 5 GAINS A ROW — THE FIRST NET-NEW CONTRACTION IN TEN DAYS — AND IT ARRIVES WITH BETTER PROVENANCE THAN THE ROW ABOVE IT.** **Bitwise Asset Management, ~14%, approximately 180 → approximately 155 employees**, CEO **Hunter Horsley** named. The captured source states *"The Bitwise team independently confirmed the layoffs to The Crypto Times when asked to verify the accuracy of the report"* — **a firm confirmation to a named outlet**, which the FalconX row (08-03, Bloomberg-relayed) does not have. **No marketing function is named** — the cohort-scoped standing finding survives its 24th row. **Rationale is price decline, not AI: the ninth consecutive non-AI 2026 contraction rationale. Watch (h′) stays rejected.** Date entered `2026-08-11 [VERIFY]` because the Bloomberg slug says 08-11 and the captured prose says "published on Wednesday" (= 08-12) — **a one-day slug-vs-prose disagreement, recorded rather than resolved.** → `../layoff-tracker/2026-layoff-tracker.csv` (row 24).

**And the row carries the tracker's first cross-class pairing.** **Bitwise is one of the six persistent class-1 `fetch_errors`** (`api.lever.co/v0/postings/bitwiseinvestments` → HTTP 404, unchanged since at least 2026-07-09). **The corpus cannot see this firm's hiring at all, and can see its contraction.** No "hiring held up while headcount fell" inference is available here in either direction — logged as a pairing, asserting nothing.

**3. 🟡 THE ROOTDATA LIST WAS FINALLY CAPTURED, AND ON CAPTURE IT IS NOT THE INSTRUMENT TWO RUN RECORDS SAID IT WAS.** Named 08-10, carried 08-11, **fetched today, HTTP 200, clean four-field date integrity.** It was described in both records as *"the only object that sizes the universe class 5 samples."* **It does not.** The captured source gives a **range, not a count** — ~70 (end of June), 99–101 (early-August verified), ~110 (late-July) — **a late-July snapshot larger than an early-August one, i.e. the list is revised downward on verification** — and states in its own text that it *"treats a bankruptcy filing and a community-voted shutdown as equivalent data points."* **It is a project-mortality census, not a workforce-contraction universe. The class-5 denominator remains unmeasured, and the corpus should stop expecting this instrument to supply it.** → `../layoff-tracker/_rootdata-dead-projects-instrument-2026-08-13.md` (NEW).

**Day-43 named marketing-side enforcement silence HOLDS. Class 3: twelfth consecutive zero.**

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0. 🔴 AND THIS ZERO MAY NOT BE WRITTEN AS A CLEAN ABSENCE — THE GUARD'S TWO HALVES DISAGREE FOR THE FIRST TIME.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-13
source A (jobs)   scan_date: 2026-08-13
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-12T22:10:37Z, age=14.0h,
             fingerprint total_jobs_fetched=2151)
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**Age 14.0h → HEALTHY. Fingerprint 2,151 → 2,151 → +0, ACROSS A TWO-CALENDAR-DAY GAP.**

`scripts/README.md` states the fingerprint rule in its own words: *"if it moves while `new_count` stays 0, the scan genuinely looked. If it is byte-identical to the prior run, the scan did not."* **By the guard's own written rule, today's fingerprint says the scan did not look.** By the guard's age test, it says the scan is the second-freshest ever recorded. **The two halves of the guard return opposite verdicts and the printed banner reports only the half that passes.**

Direct read of `scan_metadata` gives the tie-breaking detail, and it does not resolve cleanly either way: `fetch_seconds: 10.5`, `companies_scanned: 147` (89 via API, 58 chrome-pending), `total_jobs_after_filter: 25`, `new_count: 0`, `still_open_count: 25`, `url_verification_dropped: 0`, and a populated `drops_summary` (1,660 excluded function · 360 no marketing keyword · 68 no seniority signal · 24 excluded seniority · 12 tracker · 2 excluded location). **`companies_via_api` moved 87 → 89 since 07-28 and the drops distribution has shifted, both of which are consistent with a live scan.** An exactly-repeated total across two days is possible; the observed daily deltas have been **+49 / +1 / +4 / +7**, and **never 0**.

**RULING, and it is the conservative one:** the corpus cannot distinguish *"the scan ran and the market produced an identical total"* from *"the scan replayed."* **Class 1 for 2026-08-13 is recorded as UNRESOLVED — neither a genuine absence nor an unobserved window.** No class-1 absence claim is made for today. **This is exactly the ambiguity the 08-06 guard was built to kill, and it has reappeared through a hole the guard's age test cannot see.** Watch **(ff)** — magnitude, not direction — is upgraded from *unaddressed* to **🔴 COSTING**, and watch **(bb)** now needs a second predicate: **the banner must print the fingerprint DELTA, not the fingerprint, and must degrade to STALE on a zero delta regardless of age.** That is a one-line change to a script this repo owns.

**`fetch_errors`: 6, unchanged** — Wormhole Foundation, **Aave (tracked, 11th consecutive run)**, Injective Labs, **Bitwise**, Chainlink Labs, Elliptic. **Bitwise's entry stops being background today** — see headline 2. **OKX (Tier-1), Securitize, Rabby, Relai still absent from the upstream company list — ELEVENTH run.** Watch (x) stays REOPENED.

**(dd)+(t′) retroactive sweep — 5th carry. 🔴 NOT DONE, AND PER THE 08-11 RECORD'S OWN INSTRUCTION THAT MEANS IT MUST NOW BE KILLED OR OWNED.** The 08-11 record wrote: *"If the next run does not do it, kill it the way (z) was killed today and state that the corpus accepts one-sided duration claims."* **This run did not do it.** It is **not** killed here, and the reason is stated rather than buried: **(z) was a discretionary exercise whose substance was already evidenced elsewhere; (dd)+(t′) is a correctness defect in claims the report will print.** Killing it would not retire the work, it would only stop recording that the work is owed. **It is therefore RECLASSIFIED, not carried: removed from the daily-run agenda (where five runs have proven it does not fit) and escalated to Jukka as a one-session Phase-2 blocker.** See escalation (iii). **This is a decision, not a sixth carry.**

### 2. Agency claims / overlap matrix (deterministic)

18 files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. `trend-data.json` `lastUpdated` still **2026-06-15**: **59 days stale**; underlying file mtime **2026-07-10**, i.e. the file has not been rewritten in 34 days either. Class-2 output byte-identical for a **fifth** consecutive run. **`methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written — ELEVENTH run.** No trend claim made from this panel today or on any recent day.

### 3. Regulator — **0 NET-NEW ADMITTED. Day-43 silence holds. Twelfth consecutive zero.**

One search run (MiCA marketing-communications enforcement / CASP / August 2026). It returned **the same secondary layer as 08-10 and 08-11** — Lexology, Trusty, Regulation Tomorrow, Global Law Experts, Trapets, plus the AMF's republication of the ESMA public statement. **Nothing admitted. The set has now been byte-comparable across three runs spanning five days**, which the corpus records for what it is: **consistent with there being nothing to move about, and consistent with the search vocabulary being exhausted. It does not discriminate between those.**

**Two items surfaced and neither is a marketing-side enforcement action:**
- **ESMA supervisory guidelines to prevent market abuse under MiCA** — *market abuse*, not promotional conduct. Out of scope for the class-3 register as defined.
- **ESMA Common Supervisory Action launched early July 2026 on digital operational resilience** — **not marketing.** Recorded here so a future run does not surface it a fourth time and mistake it for a near-miss.

The **finfluencer-factsheet CANDIDATE** from 08-11 remains **undated and therefore still refused**; no new dating evidence was sought this run, and none arrived. `casptracker.eu` remains **named, never used** — third consecutive prospective naming under watch (ee).

**NOT REACHED, NOT GUESSED:** ESMA's finfluencer factsheet · CONSOB's amplifying communication · ESMA `?sort_by=chronological` · **the ESMA index's pre-deadline 2026 window, still never swept (watch (w))** · MAS PSN08 operative text · MAS enforcement register · **VARA, still never swept at source** · CONSOB July `comunicato` PDFs. **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW ADMITTED. Held at 6. And the zero is a RECALL CONFIRMATION plus one scope refusal.**

The class-4 search (crypto exchange CMO / head of marketing, August 2026) returned **nothing the corpus does not already hold**:

| candidate surfaced | status |
|---|---|
| **Binance — Eowyn Chen, Interim CMO**, *"Crypto Marketing's Next Job Isn't Hype"* (Coingape) | **HELD** — `../operator-statements/binance-chen-marketing-not-hype-2026-07.md`, with the 08-02 sourcing caveat about the outlet's paid-placement surface still attached |
| **Kraken — Mayur Gupta appointed CMO** (BusinessWire) | **HELD, and OUT OF WINDOW** — April 2022 |
| **Kraken — Evan Kohn, Global Head of Marketing & Growth, Kraken Pro** | **OUT OF WINDOW** — September 2025 appointment, and a **sub-brand** seat, not the firm's top marketing seat. Not admitted. Named here so it is not re-surfaced as net-new |
| The Block "key hires, moves and exits" monthlies | **ALL 2025 or 2022.** Out of window |

**No August-2026 appointment to any tracked firm's top marketing seat is publicly visible — for the second consecutive run.** Restating the Theme-4 datum with its clock advanced: **eight weeks after Binance's CMO exit and six weeks after Crypto.com's took effect, neither firm has publicly named a permanent successor, and neither firm's own estate carries a dated record of the change.**

**One scope refusal logged affirmatively.** The Bitwise capture carries a quotable line from **Ryan Rasmussen, Head of Research** — *"There are bull markets everywhere for those with the eyes to see."* **Refused: Head of Research is not a marketing seat under `methodology.md` §4's role gate.** Recorded because watch (l) has argued for eleven runs that §4 is too narrow — **this is a case where the gate is doing exactly what it should, and the negative case belongs in the record alongside the complaints.**

### 5. Layoffs — **1 NET-NEW ROW. Tracker 23 → 24.**

**Bitwise Asset Management `[PERIMETER]`** — full detail in headline 2 and in the row's own notes. Search returned four other candidates, **all already held**: Gemini (−30%), Coinbase (−14%), BitGo (−15%), Polygon Labs, Luno (−20%). **Second consecutive run in which every non-new candidate was already in the tracker** — recall evidence, **not** a completeness claim.

**The nine-run non-AI streak is now the tracker's most robust pattern and should be stated plainly for Phase 2:** Ethereum Foundation 06-23 · Polygon 07-16 · Exodus 07-17 · Gnosis 07-17 · BitMEX 07-23 · BitMart 07-26 · FalconX 08-03 · Pump.fun 08-10 · **Bitwise 08-11**. **Nine consecutive 2026 contractions with a non-AI stated rationale.** The AI-cover narrative in this corpus is carried by **Coinbase, Crypto.com, BitGo and Luno** — four firms, all of them earlier in the year. **Watch (h′) stays rejected as a firm-type correlation; the time-ordering is the live hypothesis and it is not yet evidenced.**

**Standing finding UNCHANGED, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** 24 rows.

**Gnosis `[VERIFY]` — the firm-to-source-URL mismatch — NOT CLOSED. 11th run carried.** It needs one fetch of a URL that is **in the tracker but not in this run's provenance set** — **the same watch-(jj) constraint as the retry queue.** The corpus's highest-value open verification is blocked by a tooling rule, not by effort. Escalated.

### 6. NorthPoint longitudinal panel

`trend-data.json` **59 days stale**, file untouched 34 days. **No trend claim made.**

---

## What this run did to the mandate

| # | 08-11 recommendation | status |
|---|---|---|
| 1 | **🔴 EXECUTE WATCH (hh) FIRST — re-fetch the failed-fetch queue** | **🔴 BLOCKED BY TOOLING, PROVEN NOT ASSUMED.** Queue rebuilt (8 entries / 7 run records); first attempt refused `URL not in provenance set`; search-first workaround attempted on the same URL and **failed to surface it**. **New watch (jj). Escalated as item (i).** |
| 2 | Seed the (p) sweep's firm URLs, then run it | **NOT POSSIBLE — the seeding is an owner action, not a run action.** The scheduled task did not supply the ten Stratum-1 estate URLs, so (p) is unexecutable for the second consecutive run. **Now provably the same root cause as item 1.** |
| 3 | **Fetch the RootData dead-projects list (2nd carry)** | **✅ DONE — and it reduced the corpus's confidence rather than raising it.** Headline 3; new file. **Carry closed.** |
| 4 | (dd)+(t′) sweep, or kill it | **🔵 RECLASSIFIED, NOT CARRIED AND NOT KILLED.** Removed from the daily agenda; escalated as a Phase-2 blocker. Reasoning stated in §1 rather than buried. |
| 5 | Re-test the other six sections of `sport-sponsorship-reset-2026-05.md` (watch (ii)) | **🔴 NOT DONE — 1st carry.** It requires re-fetching each section's own source; **those URLs are in the file, not in the provenance set — item 1 again.** The re-test is therefore **not** a cheap in-run exercise, contrary to how 08-11 scoped it. **Rescoped, and named in escalation (i).** |
| 6 | Escalate eight items | **DONE — below, at seven, with two closed and one added.** |

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-43 silence HOLDS.** Twelfth consecutive class-3 zero. Never print "silence" as a finding without the method caveat in (w).
- **(c) Capture panel** — untouched.
- **(d) Agency panel staleness — 59 days**, byte-identical output five runs running, file untouched 34 days. `methodology.md` §6 wording must change. **11th run.**
- **(e′) Cadence** — **🔴 BROKEN. Reset to 0 of 4.** No 08-12 run. **Portfolio-wide skip, not corpus-specific** — see escalation (ii).
- **(f) Friday nomination cadence** — **unkept, and the test the 08-11 record scheduled for 2026-08-14 falls TOMORROW.** `inbound-nominations.md` still does not exist; `README.md` still tells the public nominations are read every Friday. **This is the only watch item that is a public-facing promise rather than an internal defect.**
- **(g) Coinbase n=1** — unchanged, open.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED, and today STRENGTHENS the rejection while naming a better hypothesis.** Nine consecutive non-AI rationales; the four AI-cover rows are all earlier in 2026. **Time-ordering, not firm type. Not yet evidenced — do not print.**
- **(i) Kraken paid-media build-out** — unchanged.
- **(j) Senior-leader exits** — **UNCHANGED IN SUBSTANCE, ADVANCED IN CLOCK.** Three of ten Stratum-1 top marketing seats vacant/interim/unestablishable; **no successor named at Binance (8 weeks) or Crypto.com (6 weeks)**; the one-reporter concentration caveat stands.
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 too narrow AND provenance-blind** — **12th costing, and today the definitional half LOSES further ground.** The Rasmussen refusal shows the role gate working correctly. The provenance half of (l) is now subsumed by **(jj)** and is the live complaint.
- **(m) Ad-platform gating** — discharged.
- **(n) Full-range re-sweep of classes 3, 4, 5** — **class 4 got a clean recall check today (4/4 held); class 5 got its second (5/5). Class 3 remains unmeasured.**
- **(o) Date the document, never an event held about it** — **APPLIED TWICE.** Bitwise: slug 08-11 vs prose "Wednesday" 08-12 → **[VERIFY], both candidates recorded, neither asserted.** RootData feature: four-field agreement → **logged affirmatively.**
- **(p) Absence claims tested against firms' OWN channels** — **🔴 BLOCKED, 2nd run. Same root cause as (jj).**
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — **STRENGTHENED by the RootData census**: ten centralized exchanges are named as dead in 2026, of which the corpus holds three. The category is no longer hypothetical.
- **(s) Robinhood row misclassified** — unchanged, **12th run.**
- **(t′) Class 1 is a FLOW register presented as a STOCK register** — **RECLASSIFIED with (dd); escalated, off the daily agenda.**
- **(u) Brand absorption defeats name-keyed sweeps** — unchanged; alias table still unbuilt. **Live cost today: the `bitstamp-way` retry could not be reached by search under either its URL or its brand name.**
- **(v) NCA sweep** — 6 of 6 over its window; see (w).
- **(w) Class-3 sweep vocabulary AND method** — **unchanged and unaddressed. ESMA's index has never been swept for the pre-deadline 2026 window.**
- **(x) `fetch_errors`** — 6 entries; **Aave tracked, 11th run**; **Bitwise promoted from background to load-bearing** (see headline 2). Four upstream company-list gaps, **11th run**.
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z)** — CLOSED 08-11. Do not reopen.
- **(aa) Announcement vs effective dates** — **live instance today** in the Bitwise slug-vs-prose gap. **9th run.**
- **(bb) Class-1 feed-health guard** — **🔴 FAILED SILENTLY FOR THE FIRST TIME.** Age says HEALTHY, fingerprint says the scan did not look, **and the banner prints only the first.** Needs a second predicate: **print the DELTA and degrade to STALE on a zero delta regardless of age.** One-line change to a script this repo owns.
- **(cc) Secondary layer going machine-written** — **second affirmative reading, and a new sub-case:** the RootData capture carries an **"AI Summary" widget on the page but outside the cited body**, under a human byline and human editor, on an outlet with a standing AI Policy. **"AI on the page" and "AI in the text" are different facts and the field must record which.**
- **(dd) Class 1 cannot measure time-to-fill** — **RECLASSIFIED with (t′).**
- **(ee) A source cited once is a source not used as an instrument** — **DISCHARGED ONCE, PROSPECTIVE ONCE.** RootData was named on 08-10 and 08-11 and **used today** — the watch working end-to-end for the first time. `casptracker.eu` named a third time and still unused.
- **(ff) Feed-health guard tests direction, not magnitude** — **🔴 UPGRADED FROM UNADDRESSED TO COSTING.** Distribution now **+49 / +1 / +4 / +7 / +0**, and the first zero arrived on a two-day gap where it is least interpretable.
- **(gg) six classes in `methodology.md`, seven directories in `corpus/`** — unchanged, unwritten. Rewrite queue holds at **§1, §4, §5, §6, §7**.
- **(hh) A failed fetch is not a fetched absence** — **STANDS AS A PRINCIPLE, PROVEN UNEXECUTABLE AS A PROCEDURE.** Superseded operationally by (jj).
- **(ii) Adjacency inside a corpus file is not attribution** — **1st carry, and RESCOPED**: it needs source re-fetches that (jj) blocks. It is a Phase-2 blocker, not a daily-run task.
- **🆕 (jj) THE CORPUS CAN WRITE A RETRY QUEUE BUT CANNOT READ FROM IT.** A URL recorded in this repo's own audit trail is not in the fetch tool's provenance set; only URLs surfaced **within the current run** are fetchable. **This single constraint now blocks: watch (hh)'s retry queue, watch (p)'s estate sweep, watch (ii)'s re-test, and the Gnosis `[VERIFY]` — i.e. four of the corpus's highest-value open items, including the top recommendation of each of the last two runs.** The 08-11 recovery that broke a 15-day class-4 drought worked **because a search happened to re-surface the URL**. **The corpus's error-correction capability is currently a function of search luck.** Fixable by the owner in one action: **seed the queue's URLs into the scheduled task's prompt so they enter the provenance set.** Escalated as item (i).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **Age HEALTHY 14.0h; fingerprint 2,151 → 2,151, delta 0. Guard halves disagree; class 1 recorded UNRESOLVED.**
2. Direct read of `prospects/open-positions.json` `scan_metadata`, `fetch_errors`, `drops_summary` — the tie-break attempt described in §1.
3. Repo dedup pass: `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; 08-11 run record in full; seven directory indexes; `csv.DictReader` over all 23 tracker rows; `_industry-scale-denominator-2026-08-10.md`; findings tail; **repo-wide grep rebuilding the failed-fetch retry queue (8 entries / 7 run records)**; Bitwise grep across `corpus/` + `findings/`.
4. WebSearch — ESMA / MiCA marketing-communications enforcement / CASP / August 2026 → **same secondary layer as 08-10 and 08-11. 0 admitted.**
5. WebSearch — crypto layoffs August 2026 marketing team cuts → **1 net-new (Bitwise); 5 candidates already held.**
6. **`web_fetch` cryptotimes.io `/2026/08/12/bitwise-cuts-14-of-staff-…`** → **HTTP 200, full body.** The class-5 row.
7. **`web_fetch` cryptotimes.io `/2026/08/04/from-bitmex-to-leap-wallet-100-crypto-projects-…`** → **HTTP 200, full body.** The RootData instrument; **mandate item 3 discharged.**
8. WebSearch — crypto exchange CMO / head of marketing / August 2026 → **0 net-new; 4 candidates held or out of window.**
9. **`web_fetch bitstamp.net/bitstamp-way` → 🔴 REFUSED: `URL not in provenance set`.** The retry-queue test. **Not retried, not guessed.**
10. WebSearch — `"bitstamp.net/bitstamp-way"` / "The Bitstamp Way" → **URL not surfaced; search-first workaround FAILED.** Watch (jj) confirmed by two independent routes.
11. **Not reached / not guessed:** RootData's own list URL (recorded for a future provenance set) · Bloomberg Bitwise article (paywall) · Bitwise's own estate · Galaxy Research · TRM Labs · ESMA finfluencer factsheet · CONSOB communication · ESMA pre-deadline index window · MAS PSN08 + register · VARA · the seven remaining retry-queue URLs · the Gnosis `[VERIFY]` URL · the ten Stratum-1 estate URLs. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **row 24: Bitwise Asset Management `[PERIMETER]`**, −14%, ~180 → ~155, Hunter Horsley named, firm-confirmed-to-outlet, non-AI rationale, `[VERIFY]` on the date with both candidates recorded, and the class-1/class-5 cross-pairing.
- `corpus/layoff-tracker/_rootdata-dead-projects-instrument-2026-08-13.md` — **NEW.** The carried instrument, captured and **downgraded**: a range not a count, heterogeneous units, project mortality not workforce contraction. Full sector census reproduced; Polygon zkEVM and DL News flagged; `capture_ai_disclosure` records the page-vs-text AI distinction.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — date re-stamps (sync).
- `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — rewritten, byte-identical content (**5th run**).
- `findings/longitudinal-2026-06.md` — day-43 shift appended.
- **Layoff tracker: 23 → 24 rows. Operator statements: 6, unchanged (4/4 recall). Regulator: 0 admitted, 12th zero, 1 candidate still refused. Job postings: 0 net-new, CLASS 1 UNRESOLVED — no absence claim made.**

---

## Recommendation for next run

1. **🔴 DO NOT RE-ISSUE THE RETRY QUEUE AS A RUN TASK. It has now failed twice on the same constraint and re-issuing it a third time would be the sixth-carry pattern this corpus already decided is indefensible.** Either the owner seeds the URLs (escalation (i)) or the queue is reassigned to a manual pass. **The next run should open by checking whether the seed arrived, and if it did not, say so in one line and move on.**
2. **Patch the feed-health guard — it is the only item on this list the corpus can fix by itself.** Print `fingerprint_delta`, degrade to **STALE on delta 0 regardless of age**, and re-run. **One line, in a script this repo owns, closing watches (bb) and (ff) together.** It should be the first thing the next run does, and unlike the retry queue there is no external dependency that can block it.
3. **Class 3: change the method, not the vocabulary.** Three runs of an identical secondary set is evidence the search route is exhausted. **The unswept objects are named and stable — ESMA's pre-deadline 2026 index window, VARA at source, the MAS register.** If they remain unreachable, that is a *method* limitation Phase 2 must print, not a *market* silence.
4. **Tomorrow is Friday 2026-08-14 — the nomination-cadence test the 08-11 record scheduled.** `README.md` publicly promises inbound nominations are read every Friday. **Either the mailbox is read or the README is amended.** It is the only open item with a third party on the other side of it.
5. **Escalate to Jukka — seven items, in order:**
   - **(i) 🔴 ONE TOOLING CONSTRAINT NOW BLOCKS FOUR OF THE CORPUS'S HIGHEST-VALUE OPEN ITEMS, INCLUDING THE TOP RECOMMENDATION OF EACH OF THE LAST TWO RUNS.** Watch (jj): a URL in this repo's own audit trail is not fetchable; only URLs surfaced within the current run are. Blocked: the (hh) retry queue, the (p) estate sweep, the (ii) re-test, the Gnosis `[VERIFY]`. **The 08-11 correction that broke a 15-day drought and killed a 98-day false characterisation worked only because a search happened to re-surface the URL — the corpus's error correction is currently running on luck. Fix: paste the queue's URLs verbatim into the scheduled-task prompt so they enter the provenance set.** One edit, four items unblocked.
   - **(ii) 🔴 2026-08-12 WAS A PORTFOLIO-WIDE SKIP, NOT A CORPUS ONE.** No corpus run; `situation.md` independently records the convertor and product-builder loops missing the same day. **Cadence watch (e′) resets to 0 of 4 — but the diagnosis is scheduler-level and belongs above this project.** The corpus's cost was two days of latency on a class-5 row.
   - **(iii) THE (dd)+(t′) DURATION-CLAIM SWEEP IS A PHASE-2 BLOCKER, NOT A DAILY TASK — and it is being reclassified rather than carried a sixth time.** Every duration statement in the repo needs `captured_date`-flooring **and** a "not since re-verified" qualifier. Five daily runs have proven it does not fit in one. **One focused session, before drafting.**
   - **(iv) `methodology.md` STILL NEEDS FIVE SECTIONS REWRITTEN: §1, §4, §5, §6, §7 — ELEVENTH run for §1**, and §6's *"daily 18-agency panel"* is now describing a file untouched for 34 days. **This remains the one thing in the repo that could embarrass the report.**
   - **(v) THE CLASS-5 DENOMINATOR IS NOT COMING.** The RootData list was the named candidate for three runs; on capture it measures project mortality, not workforce contraction, and reports a *range* that moves down on verification. **Phase 2 must print 24 primary-verified rows with no coverage percentage attached, and say why.**
   - **(vi) NINE CONSECUTIVE NON-AI LAYOFF RATIONALES, WITH ALL FOUR AI-COVER ROWS EARLIER IN THE YEAR.** If Theme 5 is going to say anything about the AI narrative, **the shape is temporal, not structural — and it is not yet evidenced well enough to print.** Flagged now so drafting does not reach for the easier claim.
   - **(vii) FOUR UPSTREAM COMPANY-LIST GAPS — OKX (Tier-1), Securitize, Rabby, Relai — ELEVENTH run**, plus Aave's eleventh consecutive fetch error. **New today: Bitwise's fetch error is no longer cosmetic** — the corpus captured that firm's contraction while structurally blind to its hiring.
