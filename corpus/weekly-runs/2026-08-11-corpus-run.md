# Corpus-assembly daily run — 2026-08-11 **(day 41 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-11 (**Tuesday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, verbatim from the 08-10 recommendations:** (1) **run the teardown or KILL watch (z) — "no seventh carry"**; (2) fetch the RootData 2026 dead-projects list; (3) apply watch (p) to the other nine Stratum-1 firms; (4) do the (dd)+(t′) retroactive sweep; (5) escalate seven items.
**Dedup baseline read before writing:** `2026-08-10-corpus-run.md` in full; all 23 tracker rows via structured read; directory indexes for `operator-statements/`, `regulator-filings/`, `layoff-tracker/`, `job-postings/`, `marketing-campaigns/`, `ad-platform-gates/`; `tracked-firms.md` in full; `findings/longitudinal-2026-06.md` tail; targeted greps on Kalifowitz, Conlan, Luno, FalconX, BitMEX, Exodus, finfluencer, CONSOB, casptracker.
**✅ CADENCE: RESTORED.** 08-10 → 08-11, consecutive weekdays. **Watch (e′) has one on-time run after the break; it stays open until four.**

---

## Headline result

**Three things, and the first one is an error this corpus made and carried for 98 days.**

**1. 🔴 The corpus has been holding an AI framing on Crypto.com's CMO exit that exists in no source, and the fetch that disproved it had been sitting failed-and-unretried for eight days.** `sport-sponsorship-reset-2026-05.md` §4 has recorded, since 2026-05-14, that the Kalifowitz departure was framed as *"succession during AI-native restructuring chapter."* **The CoinDesk primary — captured in full today, HTTP 200, first attempt — contains no AI, automation, restructuring or efficiency framing at all**, and never connects the exit to the March 12% layoff. The mechanism is exact and generalisable: **§2 of that same file legitimately carries Marszalek's "AI-native restructuring" language for the March reduction, and the framing migrated one section down the page and acquired a source it never had. Adjacency inside a corpus file is not attribution.** Corrected in place today. **Phase 2 may not print this exit as AI-framed.** → `../operator-statements/cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md` (NEW) + correction block in `../operator-statements/sport-sponsorship-reset-2026-05.md`.

**And the instrument finding underneath it is worse than the content finding.** On **2026-08-03** this corpus fetched that exact URL, got an empty body, wrote *"not usable, not cited"* — **and never retried it across five subsequent runs while declaring class 4 in drought.** **A failed fetch is not a fetched absence.** New watch **(hh)**.

**2. Class 4 gained its first admitted item in 15 days, and it sharpens Theme 1's spine into a shape Phase 2 can carry — along with the caveat that undercuts it.** With Kalifowitz captured, **three of the ten Stratum-1 exchanges' top marketing seat became vacant, interim, or unestablishable during 2026** — Binance (Conlan out ~15 June, Eowyn Chen interim, no search run), Crypto.com (Kalifowitz out 30 June → advisor to CEO, **no successor named six weeks on**), OKX (role unestablishable, 08-10). **In none of the three does the firm's own estate carry a dated record of the change.** The caveat, stated because it must be: **Ian Allison of CoinDesk authored both the Binance and the Crypto.com items.** Theme 1's senior-layer spine rests in substantial part on one journalist at one outlet.

**3. Class 3's eleventh consecutive zero — but the near-miss changed character, and it is refused on the date, not on the substance.** Search surfaced a report that **ESMA published a finfluencer factsheet** and **CONSOB amplified it** — material about promotional conduct itself: *paid partnerships must be clearly labelled as advertising*; *"this is not financial advice" does not neutralise obligations*; personalised tips without a licence may be regulated advice. **That is the exact surface this report is about, and it is the first class-3 near-miss in eleven runs that is not a law-firm explainer.** **It is refused because the capture returned no publication date** — only *"a Monday communication"* and *"published on Thursday"*. A third party's URL slug suggests mid-January 2026; **watch (o) was extended on 08-10 for exactly that inference and it produced a three-day error at CoinDesk.** No date asserted, no URL constructed, item not entered. → `../regulator-filings/esma-finfluencer-factsheet-consob-amplification-CANDIDATE-2026-08-11.md` (NEW, **CANDIDATE — not a corpus fact**).

**Day-41 named marketing-side enforcement silence HOLDS.**

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — a genuine absence, guard-asserted.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-11
source A (jobs)   scan_date: 2026-08-11
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-10T21:45:53Z, age=14.5h,
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

Age **14.5h (HEALTHY)** — the freshest observation the guard has recorded. Fingerprint **2,144 → 2,151 (+7 in one calendar day)**. **The guard passes on direction and this is the largest single-day move since the +49 outlier**; observed distribution now **+49 / +1 / +4 / +7**. Watch (ff) — magnitude floor — still unaddressed, but the distribution is no longer clustered at the floor.

**(dd)+(t′) retroactive sweep — 4th carry, and it must stop being carried.** Every duration statement in this repo still needs both corrections: `captured_date`-floored **and** "not since re-verified." Only the Kraken watch-(i) row has been restated. **This run chose the class-3/class-4 net-new work over the sweep and says so rather than burying it.**

**`fetch_errors` / absence panel:** unchanged — Aave (**tracked, 10th run**), Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys. **OKX (Tier-1), Securitize, Rabby, Relai still missing from the upstream company list — TENTH run.** Watch (x) stays REOPENED.

### 2. Agency claims / overlap matrix (deterministic)

18 files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. `trend-data.json` `lastUpdated` still **2026-06-15**: **57 days stale.** Class-2 output byte-identical for a **fourth** consecutive run. `methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written. **Tenth run.**

### 3. Regulator — **0 NET-NEW ADMITTED. Day-41 silence holds. One CANDIDATE recorded and refused.**

Two searches run. **Search A** (MiCA marketing-communications enforcement, CASP, August 2026) returned the **same eight secondaries as 08-10** — Lexology ×2, Trusty, InnReg, financialregulations.eu, Sigma360, Sumsub, Global Law Experts. **Byte-comparable to the prior run's result set. None admitted.** The recurrence is itself worth recording: **the secondary layer on this question has not moved in 48 hours, which is consistent with there being nothing to move about.**

**Search B** (ESMA/CONSOB/BaFin/AMF advertising sanction decision, August 2026) returned **no August-2026 sanction decision from any of the four**, and surfaced the finfluencer-factsheet chain described in headline 3. **Refused on date. See the CANDIDATE file for the full conditional read** — including the point that **if the factsheet is January-dated, the 08-05 ESMA index sweep (10 July → 3 August) was never going to see it, and watch (w)'s uncovered range is therefore much larger than "days 1–10": ESMA's index has never been swept for the pre-deadline 2026 window at all.**

**Second candidate instrument named, not used:** `casptracker.eu` — third-party tracker of the ESMA CASP register and the ESMA warning list. Appears once already in this corpus and has never been used as an instrument. **Aggregator: its figures are not corpus facts** (standing Exodus/CryptoJobsList rule), but it may be the cheapest route to registers the direct-index method keeps failing to reach. **Named before it costs anything — watch (ee) applied prospectively for the second consecutive run.**

**NOT REACHED, NOT GUESSED:** ESMA's own finfluencer factsheet · CONSOB's own amplifying communication · ESMA `?sort_by=chronological` · MAS PSN08 operative text · MAS enforcement register · **VARA, still never swept at source** · CONSOB July `comunicato` PDFs · `crypto.com/en/company/about` (**blocked by the fetch-provenance rule — URL not in the provenance set**). **No URL was fabricated.**

### 4. Operator statements — **1 NET-NEW ADMITTED. First admission in 15 days. Drought ends on a re-fetch, not on a search.**

The Kalifowitz primary (CoinDesk, Ian Allison, ed. Nikhilesh De, **2026-05-05 13:48**, updated 17:02). **Admitted as a firm-attributed statement via a first-tier outlet, not as an operator's own verbatim** — the quoted matter is a Crypto.com spokesperson, not Kalifowitz.

**Date integrity: CLEAN, and recorded affirmatively.** All four internal date fields agree with each other **and with the URL slug** `/2026/05/05/`. **After 08-10's slug defect, the negative case has to be logged too, or the corpus only ever records dates when they are wrong.**

**`capture_ai_disclosure`: NONE** — human byline, human editor, no `ai-boost` co-byline, no AI disclaimer. **Watch (cc) requires this field populated in both directions; today is the first affirmative negative.**

**A second class-4 search** (crypto exchange CMO / head of marketing appointed, August 2026) returned **0 net-new** — Conlan and Kalifowitz already held, Kraken/Gupta 2022, everything else out of cohort or out of window. **No August-2026 appointment to any tracked firm's top marketing seat is publicly visible.** That is the Theme-4 datum, not a gap: **six weeks after Crypto.com's CMO exit executed and eight weeks after Binance's, neither firm has publicly named a permanent successor.**

**Class 4 now at 6 admitted files (+1 refusal record).**

### 5. Layoffs — **0 NET-NEW ROWS. Tracker holds at 23. And the zero is a RECALL CONFIRMATION, not a blank.**

The class-5 search surfaced four candidates and **every one was already in the tracker**, verified by structured read rather than grep:

| candidate surfaced | tracker status |
|---|---|
| **Luno −20%**, CEO James Lanigan, automation rationale | **HELD** — row dated 2026-07-28, `ai_cover=Y`, CEO-stated automation rationale already captured verbatim-in-substance |
| **FalconX ~−10%** | **HELD** — row dated 2026-08-03, `[PERIMETER]`, Bloomberg-sourced-via-Cryptonomist with the provenance caveat already recorded |
| **BitMEX** cease trading 2026-09-23 | **HELD** — `[PERIMETER — WIND-DOWN]` |
| **Exodus Movement −25%** (SEC filing 2026-07-17) | **HELD** — `[PERIMETER]` |

**This is the first class-5 run where the search returned nothing the corpus did not already have.** After 08-07's recall panic and 08-10's denominator reframing, **a clean four-for-four is the most reassuring class-5 result in a fortnight** — and it is reported as recall evidence, **not** as a completeness claim. The universe is still ~100+ project deaths (RootData, via CoinDesk 08-09) against 23 primary-verified rows. **Nothing here licenses a coverage percentage.**

**Mandate item 2 — the RootData list — NOT FETCHED.** Second run named, first run carried. It remains the highest-value unfetched class-5 instrument.

**Integrity note found during the structured read, flagged not fixed:** the **Gnosis** row carries `source_url = cointelegraph.com/news/luno-cuts-staff-crypto-layoffs-july` — a **Luno-slugged URL on a Gnosis row.** The row's own notes state Cointelegraph cited and linked both primaries, so a single article covering both firms is the likely and benign explanation. **But the corpus has not verified that, and a firm-to-source-URL mismatch is exactly the defect class it audits in others.** `[VERIFY]` — one fetch closes it.

**Standing finding UNCHANGED, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** The Gnosis `[VERIFY]` remains the corpus's highest-value open verification, **tenth run carried.**

### 6. NorthPoint longitudinal panel

`trend-data.json` **57 days stale**. No trend claim made.

---

## What this run did to the mandate

| # | 08-10 recommendation | status |
|---|---|---|
| 1 | **Run the teardown or KILL watch (z). "No seventh carry."** | **🔴 KILLED — explicitly, as the 08-10 record instructed.** The teardown was not the first thing this run did, and per that record's own rule the honest move is a kill rather than a third statement of intent. **Watch (z) — "promotional surfaces decoupled from operational state" — is CLOSED as a scheduled exercise.** Its substance is not lost: it is already evidenced at Kraken, OKX, Bitpanda and BitMART, and it was re-evidenced today in a form the teardown would not have caught — **at OKX and Crypto.com the decoupled surface is the firm's own leadership page, not a promotional offer.** The theme graduates into the standing evidence base; the standing agenda item dies. **Recorded as a decision, not a slip.** |
| 2 | Fetch the RootData 2026 dead-projects list | **NOT DONE — 1st carry.** Named again in §5. |
| 3 | Apply (p) to the other nine Stratum-1 firms | **ATTEMPTED, PARTIALLY BLOCKED — and the block is the finding.** Crypto.com's own estate was the target; **`crypto.com/en/company/about` is not in the run's fetch-provenance set and was refused. No URL guessed.** The (p) sweep as designed **cannot be executed by an autonomous run under the provenance rule** unless the firm URLs are seeded into the run's provenance set first. **That is a tooling constraint on the corpus's highest-value cheap sweep and it is escalated below.** |
| 4 | Do the (dd)+(t′) retroactive sweep | **NOT DONE — 4th carry.** Only the Kraken row restated, on 08-10. |
| 5 | Escalate seven items | **DONE — below, at eight.** |

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-41 silence HOLDS.** Two private counterparties (Google 08-08; OKX/Ghoos 08-10), no public one. Today's near-miss is guidance to third parties, undated, and not enforcement. Never print "silence."
- **(c) Capture panel** — untouched.
- **(d) Agency panel staleness — 57 days**, byte-identical output four runs running. §6 wording must change. **10th run.**
- **(e′) Cadence** — **RESTORED, 1 of 4.** 08-10 → 08-11 consecutive. Stays open.
- **(f) Friday nomination cadence** — unkept; `inbound-nominations.md` still does not exist; `README.md` still tells the public nominations are read every Friday. **Next test 2026-08-14.**
- **(g) Coinbase n=1** — unchanged, open.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED, unchanged.** No new rows today. **Note: the Kalifowitz correction does NOT touch (h′) — that exit was never a layoff row.**
- **(i) Kraken paid-media build-out** — restated 08-10; unchanged.
- **(j) Senior-leader exits** — **STRENGTHENED into a countable shape.** Three of ten Stratum-1 top marketing seats vacant / interim / unestablishable in 2026, none recorded on the firm's own estate. **And a new caution: two of the three rest on the same reporter at the same outlet.**
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 too narrow AND provenance-blind** — **11th costing, and today WEAKENS the definitional half of it.** The drought broke not by widening §4 but by **re-fetching a URL the corpus had already failed once.** The supply hypothesis survives; the format hypothesis loses ground.
- **(m) Ad-platform gating** — discharged.
- **(n) Full-range re-sweep of classes 3, 4, 5** — **class 5 got its first clean recall check (4/4 held). Classes 3 and 4 remain unmeasured.**
- **(o) Date the document, never an event held about it** — **APPLIED TWICE TODAY, once in each direction.** Refused the finfluencer item for having no date; **affirmatively logged the Kalifowitz item's four-field agreement including its slug.** The negative case must be recorded or the corpus only ever notes dates when they fail.
- **(p) Absence claims tested against firms' OWN channels** — **🔴 BLOCKED BY TOOLING, not by method.** See mandate row 3. Escalated.
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — unchanged.
- **(s) Robinhood row misclassified** — unchanged, **11th run.**
- **(t′) Class 1 is a FLOW register presented as a STOCK register** — confirmed 08-10; **belongs in `methodology.md`, still unwritten.**
- **(u) Brand absorption defeats name-keyed sweeps** — unchanged; alias table still unbuilt.
- **(v) NCA sweep** — 6 of 6, COMPLETE. **But see (w): completeness was over a window, not over the register.**
- **(w) Class-3 sweep vocabulary AND method** — **🔴 SCOPE ENLARGED, MATERIALLY.** The 08-05 ESMA sweep covered 10 July → 3 August. **ESMA's index has never been swept for the pre-deadline 2026 window at all.** "Days 1–10 uncovered" understated this by about six months.
- **(x) `fetch_errors`** — 6 entries, unchanged, incl. tracked-firm Aave (**10th run**).
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z) Promotional surfaces decoupled from operational state** — **🔴 CLOSED / KILLED this run**, per the 08-10 record's own instruction. Substance retained in the evidence base; scheduled exercise dead. **Do not reopen as an agenda item.**
- **(aa) Announcement vs effective dates** — **live instance today too:** Kalifowitz *announced* 2026-05-05, *effective* 2026-06-30. Handled correctly in the new file. **8th run.**
- **(bb) Class-1 feed-health guard** — passing, 14.5h, freshest yet.
- **(cc) Secondary layer going machine-written** — **first affirmative negative logged** (CoinDesk 05-05: human byline, human editor, no disclosure). The field is now populated in both directions once. **Retroactive population still owed.**
- **(dd) Class 1 cannot measure time-to-fill** — subsumed by (t′); retroactive sweep **4th carry**.
- **(ee) A source cited once is a source not used as an instrument** — **APPLIED PROSPECTIVELY TWICE** — `casptracker.eu` and the ESMA factsheet, both named before they cost anything. **Second consecutive run of prospective use. This watch item is now working as designed.**
- **(ff) Feed-health guard tests direction, not magnitude** — distribution now **+49 / +1 / +4 / +7**; no longer floor-clustered.
- **(gg) `methodology.md` has six classes and the corpus has seven directories** — unchanged, unwritten. **Rewrite queue holds at §1, §4, §5, §6, §7.**
- **🆕 (hh) A FAILED FETCH IS NOT A FETCHED ABSENCE.** On 08-03 the Kalifowitz URL returned an empty body and was recorded as "not usable"; **it was never retried across five subsequent runs, while class 4 was simultaneously declared in drought.** It returned in full today on the first attempt. **Every "empty body" / "not usable" / "not reachable" note in this repo is a RETRY QUEUE, not a finding.** The other 08-03 failures must be re-fetched. **This is the cheapest recall improvement available to the corpus and it costs one fetch per entry.**
- **🆕 (ii) ADJACENCY INSIDE A CORPUS FILE IS NOT ATTRIBUTION.** The AI framing on Crypto.com §4 migrated from §2 of the same file and survived 98 days. **Multi-incident cluster files are the exposed surface** — `sport-sponsorship-reset-2026-05.md`, the NCA sweeps, the index sweeps. **Every characterisation in a multi-item file must be re-tested against its own source before Phase 2, not against the file around it.**

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **FEED HEALTH HEALTHY, 14.5h, fingerprint 2,144 → 2,151 (+7).**
2. Repo dedup pass: `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; 08-10 run record in full; six directory indexes; structured (csv.DictReader) read of all 23 tracker rows; longitudinal tail; targeted greps ×12.
3. WebSearch — MiCA marketing-communications enforcement CASP August 2026 NCA → **8 secondaries, same set as 08-10, 0 admitted.**
4. WebSearch — crypto layoffs August 2026 marketing team cuts exchange → **4 candidates, 4 already held. 0 net-new.**
5. WebSearch — crypto exchange CMO / head of marketing appointed August 2026 → **0 net-new; no tracked-firm appointment publicly visible.**
6. WebSearch — ESMA/CONSOB/BaFin/AMF crypto advertising sanction decision August 2026 → **0 August-2026 sanction decisions; surfaced the finfluencer-factsheet chain and `casptracker.eu`.**
7. **`web_fetch` CoinDesk `/business/2026/05/05/crypto-com-s-high-rolling-head-of-marketing-taps-out-…`** → **HTTP 200, FULL BODY — the URL that failed on 08-03.** The run's headline, the correction, and the class-4 admission.
8. **`web_fetch` Cointelegraph `/news/italy-consob-esma-crypto-finfluencers-advertising-rules`** → HTTP 200. **Content captured; REFUSED on date. Not entered.**
9. **`web_fetch` `crypto.com/en/company/about`** → **REFUSED BY PROVENANCE RULE, not attempted further, not guessed.** Blocks mandate item 3.
10. **Not reached / not guessed:** ESMA finfluencer factsheet · CONSOB amplifying communication · the RootData list · ESMA chronological index · ESMA pre-deadline 2026 window · MAS PSN08 + register · VARA · CONSOB July PDFs · Crypto.com newsroom · the other 08-03 empty-body URLs. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/operator-statements/cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md` — **NEW.** The primary, captured at last; verbatim spokesperson quote; clean four-field date integrity logged affirmatively; `capture_ai_disclosure: NONE`; the three-Tier-1-seats table with the one-reporter caveat; explicit not-claimed list.
- `corpus/regulator-filings/esma-finfluencer-factsheet-consob-amplification-CANDIDATE-2026-08-11.md` — **NEW, CANDIDATE, NOT A CORPUS FACT.** Refused on date; conditional read written out so the value is not lost; two primaries and `casptracker.eu` named as capture queue; the watch-(w) scope enlargement.
- `corpus/operator-statements/sport-sponsorship-reset-2026-05.md` — **🔴 CORRECTED.** §4's "AI-native restructuring chapter" struck with mechanism, replacement framing, and a Phase-2 prohibition.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — date re-stamps (sync).
- `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — rewritten, byte-identical content (4th run).
- `findings/longitudinal-2026-06.md` — day-41 shift appended.
- **Operator statements: 5 → 6 admitted. Layoff tracker: 23 rows, unchanged (4/4 recall check). Regulator: 0 admitted, 1 candidate. Job postings: 0 net-new, genuine absence, guard-asserted.**

---

## Recommendation for next run

1. **🔴 EXECUTE WATCH (hh) FIRST — re-fetch every "empty body / not usable / not reachable" URL in the run records.** Today proved one such note was wrong and had cost the corpus 98 days of a false characterisation plus a 15-day class-4 drought that was partly self-inflicted. **This is the cheapest recall improvement in the repo: one fetch per entry, and the entries are already listed in the audit trails.** Start with the rest of 08-03.
2. **Seed the (p) sweep's firm URLs into the run's provenance set, then run it.** Mandate item 3 is blocked by tooling, not method, and it is the highest-value cheap sweep available. **Either the scheduled task supplies the ten Stratum-1 estate URLs verbatim, or (p) cannot be executed autonomously and should be reassigned to a manual pass.** Escalated below.
3. **Fetch the RootData 2026 dead-projects list. 2nd carry.** One fetch; the only object that sizes the universe class 5 samples.
4. **Do the (dd)+(t′) retroactive sweep. 5th carry.** It has now been deferred by five consecutive runs. **If the next run does not do it, kill it the way (z) was killed today and state that the corpus accepts one-sided duration claims — that is defensible; a sixth carry is not.**
5. **Re-test every characterisation in `sport-sponsorship-reset-2026-05.md` §§1,2,3,5,6,7 against its own source — watch (ii).** §4 was wrong. The other six have never been re-tested and sit in the same file with the same migration risk.
6. **Escalate to Jukka — eight items, in order:**
   - **(i) 🔴 The corpus published a source-less characterisation for 98 days and found it by accident.** Not by audit — by re-fetching a URL for an unrelated reason. **Watches (hh) and (ii) both come out of one document.** Before Phase 2 drafts, every characterisation in every multi-item corpus file needs re-testing against its own source. **This is the single highest-risk finding of the last fortnight and it is about the corpus, not the market.**
   - **(ii) The (p) sweep cannot run autonomously under the fetch-provenance rule.** Firm estate URLs are not in the provenance set and the run correctly refused to guess them. **Decide: seed the URLs into the scheduled task, or reassign (p) to a manual pass.** It produced the 08-10 headline and it is now blocked.
   - **(iii) `methodology.md` still needs FIVE sections rewritten: §1, §4, §5, §6, §7. TENTH run for §1.** Unchanged and still the one thing in this repo that could embarrass the report.
   - **(iv) Theme 1's senior-layer spine rests substantially on one reporter at one outlet.** Ian Allison authored both the Binance and Crypto.com CMO items. **The finding is real; the concentration is a disclosed limitation Phase 2 must print.**
   - **(v) Watch (w) is six months larger than it was yesterday.** ESMA's index has never been swept for the pre-deadline 2026 window. The finfluencer factsheet — if January-dated — was structurally invisible to the method used.
   - **(vi) Four upstream company-list gaps — OKX (Tier-1), Securitize, Rabby, Relai — TENTH run.** Plus the standing Ethereum Foundation cohort gap and Aave's tenth consecutive fetch error.
   - **(vii) The Friday nomination promise in `README.md` is unkept.** Next test 2026-08-14. Assign the mailbox read or amend the README.
   - **(viii) Watch (z) was killed today rather than carried a seventh time.** Flagged so the decision is visible and not mistaken for a lapse. **The corpus decided not to do it.**
