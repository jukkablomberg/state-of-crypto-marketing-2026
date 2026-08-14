# Corpus-assembly daily run — 2026-08-14 **(day 44 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-14 (**Friday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, verbatim from the 08-13 recommendations:** (1) open by checking whether the retry-queue URL seed arrived; if not, say so in one line and move on; (2) **patch the feed-health guard — the only item the corpus can fix by itself**; (3) **class 3: change the METHOD, not the vocabulary** — ESMA's pre-deadline index window, **VARA at source**, the MAS register; (4) the Friday nomination-cadence test falls today; (5) escalate seven items.
**Dedup baseline read before writing:** `2026-08-13-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; all 24 tracker rows via `csv.DictReader`; directory indexes for all seven `corpus/` subdirectories; `_aggregator-crossref-2026-08-07.csv` in full; `findings/longitudinal-2026-06.md` head + tail; repo-wide case-insensitive grep on **vara · vesta · "open network" · "ton foundation" · kucoin · mexc · certora · coinmena · shelbit** across `corpus/` and `findings/`.
**🟢 CADENCE: ON TIME. 08-13 → 08-14, consecutive calendar days.** Watch (e′) advances **1 of 4** after the 08-12 portfolio-wide skip reset it to zero.

---

## Headline result

**Twelve consecutive class-3 zeroes were a property of the METHOD, not of the market — and one fetch of a regulator's own register proved it in a single run.**

**1. 🔴🟢 THE CLASS-3 SILENCE WAS SCOPED WRONG, AND THE CORPUS FOUND THAT OUT BY DOING WHAT THE LAST RECORD TOLD IT TO DO.** The 08-13 recommendation was *"change the method, not the vocabulary… the unswept objects are named and stable — ESMA's pre-deadline 2026 index window, VARA at source, the MAS register."* **VARA was swept at source for the first time in the project's history.** `vara.ae/en/enforcement/` returned a **37-row published fines register**; `vara.ae/en/regulations/regulatory-notices/` returned a **30-item notices index**. Both HTTP 200, both full bodies.

**35 of 37 published fine rows carry an advertising/marketing limb. Nine state advertising and marketing as the ONLY reason.** The single **2026-dated** row in the whole table is **Vesta Prime Portal Co. L.L.C., 2026/01/13, reason A and only A: *"Advertising and Marketing virtual asset activities in Dubai."*** Cease-and-desist plus financial penalties.

**Twelve run records described this as "named marketing-side enforcement silence." That phrasing was too broad.** The silence that actually survives contact with the primary record is narrower: **no EU national competent authority has published a named marketing-side enforcement action against a CASP since the MiCA transitional deadline.** Outside the EU it is simply false — VARA has been publishing named, dated, fined marketing-perimeter actions throughout the window. **Watch (b) is unaffected on its own terms** (VARA is not an NCA; the most recent fine row predates the deadline by five and a half months). **What changed is the wording of a claim the report was going to print.** → `../regulator-filings/vara-enforcement-register-at-source-2026-08-14.md` (NEW).

**2. 🟢 THE SINGLE MOST CITABLE CLASS-3 OBJECT THE CORPUS HAS EVER ACQUIRED: A NAMED PROTOCOL FOUNDATION FINED FOR HOW IT MARKETED, AND FOR NOTHING ELSE.** **The Open Network Foundation, 2025/07/24.** Category is **`Regulatory breaches`, not `Unlicensed activities`** — i.e. a licensed-perimeter conduct case. Sole stated reason: **"Breaches of the VARA Marketing Regulations."** Sanctions: cease-and-desist, financial penalties, **and a Public Statement — the only row in the register carrying one.**

Every other marketing-limb row in that register is an unlicensed-operator perimeter case: marketing *without a licence*, which is not the same offence as MiCA Art. 7/66 "fair, clear and not misleading". **TON is the exception, and the exception is exactly what Themes 1 and 4 need: a regulator fining a non-fringe, named entity specifically for the conduct of its marketing.**

**3. 🔴 THE INSTRUMENT CAVEAT IS AS VALUABLE AS THE FINDING — A REGULATOR'S SUMMARY TABLE IS NOT THE REGULATOR'S RECORD.** The fines table's most recent row is **2026/01/13**. The notices index on the same domain carries **four Notices of Fines dated later** — Shelbit **24 Jul 2026**, KuCoin **24 Jun 2026**, MEXC **22 Jun 2026**, CoinMENA **22 Jun 2026** — **none of which appear in the table.** A sweep of `/enforcement/` alone would have concluded VARA issued no fines after January 2026; **the falsifier is one click away on the same host.** Recorded as a standing rule for every future regulator sweep: **read both the register and the notices index, or the count is wrong.**

**4. 🟡 A TRACKED TIER-1 FIRM IS IN THE REGISTER — AND THE HONEST READING IS NARROWER THAN THE HEADLINE WOULD ALLOW.** **KuCoin (Peken Global Limited)**, Stratum 1. **5 Mar 2026 Investor and Marketplace Alert**, titled *"…[commercially **advertising** as "Kucoin"]"*, containing verbatim: *"Any promotion, advertising, or solicitation related to Kucoin has not been approved by VARA, and the company is therefore not allowed to offer, promote, or market any Virtual Asset products or services in Dubai or to its residents."* **24 Jun 2026 Notice of Fines** — but **the fine's stated breach is unlicensed Broker-Dealer/Exchange services, not a marketing breach.** **Marketing is the prohibition limb of the March alert; it is not the charge in the June fine, and the corpus records it that way rather than the way that would read better.** The notice also states the entity *"fully cooperated"*, intends to enter VARA's licensing process, and that liability is confined to Peken Global Limited alone.

**Day-44 EU-NCA named marketing-side enforcement silence HOLDS. Class 3: FIRST NON-ZERO IN THIRTEEN RUNS — 1 net-new capture admitted, non-EU.**

---

## Six-class audit trail

### 0. The retry-queue seed — one line, as instructed

**The seed did not arrive.** The scheduled task prompt for 2026-08-14 contains no URLs. Watch (jj) is unexecutable again; per the 08-13 ruling it is **not re-issued as a run task**. Escalation (i) stands unchanged. Moving on.

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0, AND FOR THE FIRST TIME SINCE THE GUARD WAS BUILT THAT ZERO IS A CLEAN, GUARD-CERTIFIED ABSENCE.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-14
source A (jobs)   scan_date: 2026-08-14
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-13T22:23:52Z, age=13.8h,
             fingerprint total_jobs_fetched=2175, delta=+24 vs 2026-08-13 (2151))
  reason: age 13.8h, fingerprint delta +24
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**🟢 MANDATE ITEM 2 DISCHARGED — WATCHES (bb) AND (ff) ARE CLOSED TOGETHER, IN CODE, IN A SCRIPT THIS REPO OWNS.** The guard now evaluates **two predicates and prints both**:

- **Age** — unchanged, 36h threshold.
- **Fingerprint delta** — `total_jobs_fetched` compared against the last observation **from a prior calendar date**, persisted in `../job-postings/_feed-fingerprint.json`. **A delta of 0 degrades the verdict to STALE regardless of age**, which is what `scripts/README.md` has said in words since 2026-08-06 and never enforced.

**Discrimination was verified both ways before the result was trusted, because a guard that has only ever returned PASS is not a guard:**

| test | input | verdict |
|---|---|---|
| real run | delta `+24` vs 2026-08-13 (2151 → 2175) | **HEALTHY**, absence claim permitted |
| idempotency | same-day re-run | **HEALTHY**, delta still `+24` — the comparison is against a prior *date*, so re-running cannot manufacture a zero |
| discrimination | prior-date fingerprint forced to 2175 | **STALE**, reason printed, **`CLASS-1 ABSENCE CLAIM REFUSED`** emitted |

State was then restored and the real run re-executed. **The 08-13 defect is now impossible to repeat silently: a run in that condition refuses itself.**

⚠ **One honest disclosure about the state file.** The 2026-08-13 entry in `_feed-fingerprint.json` was **backfilled from the verbatim banner quoted in the 08-13 run record**, not re-derived from the upstream feed (which now holds only today's scan). The entry carries a `provenance` field saying exactly that. **Every entry from 2026-08-14 onward is written by the script from the live feed.**

**`fetch_errors`: unchanged.** **OKX (Tier-1), Securitize, Rabby, Relai still absent from the upstream company list — TWELFTH run.** Watch (x) stays REOPENED. **Aave: twelfth consecutive fetch error.**

### 2. Agency claims / overlap matrix (deterministic)

18 files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. `trend-data.json` `lastUpdated` still **2026-06-15**: **60 days stale**. Class-2 output byte-identical for a **sixth** consecutive run. **`methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written — TWELFTH run.** No trend claim made from this panel today.

### 3. Regulator — **1 NET-NEW CAPTURE ADMITTED. The thirteen-run zero ends, and it ends on a method change rather than on a search.**

Full detail: `../regulator-filings/vara-enforcement-register-at-source-2026-08-14.md`.

**What was executed:** the 08-13 recommendation, literally. One WebSearch surfaced VARA's own domain; **four fetches then went to `vara.ae` directly** — the fines register, the notices index, the 7 Oct 2025 notice, and the KuCoin fine + alert pair. **No secondary press, no law firm, no aggregator was admitted.**

**What it produced, in order of value to the report:**

| # | object | why it matters |
|---|---|---|
| 1 | **The Open Network Foundation, 2025/07/24** — `Regulatory breaches`, sole reason *"Breaches of the VARA Marketing Regulations"*, sanctions incl. **Public Statement** | The corpus's first primary-source case of a **named, non-fringe entity fined for marketing conduct rather than for marketing without a licence** |
| 2 | **Vesta Prime Portal Co. L.L.C., 2026/01/13** — sole reason *"Advertising and Marketing virtual asset activities in Dubai"* | The **only 2026-dated row** in the fines table, and it is marketing-only |
| 3 | **The 35/37 and 9/37 tallies** | Quantifies a marketing-enforcement estate the corpus previously had zero primary measurement of |
| 4 | **KuCoin, tracked Stratum 1** — 5 Mar 2026 alert (marketing prohibition) + 24 Jun 2026 fine (**licensing** charge) | Tracked-cohort regulator exposure, recorded with the limbs kept separate |
| 5 | **The two-surface disagreement** | A general sweep rule, worth more than any single row |

**Two refusals logged affirmatively, because the discipline is the product:**
- **The 7 Oct 2025 "19 firms penalised" notice NAMES NO FIRMS.** Fines AED 100,000–600,000, *"Unlicensed activity and unauthorised marketing will not be tolerated."* It is a **numbered but unnamed** action and cannot support any firm-level claim. Its 19 firms are not reconcilable to the table from public information.
- **Fine amounts are not published per row.** The AED range belongs to that one action's 19 firms. **No amount is attached to any named row anywhere in the new file.**

**Also refused: the temptation to call this a break in watch (b).** It is not. VARA is not an EU NCA, MiCA does not apply in Dubai, and the most recent VARA fine row is 2026/01/13 — **five and a half months before the deadline whose aftermath watch (b) measures.** The finding is that the corpus's *description* of the silence was wrong, not that the silence is.

**NOT REACHED, NOT GUESSED:** MEXC / CoinMENA / Shelbit notice bodies · the enforcement PDFs on `media.umbraco.io` · `vara.ae/en/enforcement/unlicensed-vasps/` · `rulebooks.vara.ae` Marketing Regulations 2024 operative text + Schedule 1 fines · VARA's Arabic surfaces · **ESMA's pre-deadline 2026 index window, still never swept (watch (w), now the ONLY unswept object of the three the 08-13 record named)** · MAS PSN08 operative text · the MAS enforcement register · CONSOB July `comunicato` PDFs · the still-undated ESMA finfluencer-factsheet CANDIDATE from 08-11 (**still refused**). `casptracker.eu` remains **named, never used** — fourth consecutive prospective naming under watch (ee). **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW ADMITTED. Held at 6. Third consecutive recall confirmation.**

One search (crypto exchange CMO / head of marketing / 2026, naming Bitpanda, Kraken, Bitstamp, OKX explicitly to break the vocabulary rut). Everything returned is already held or already out of window:

| candidate surfaced | status |
|---|---|
| **Binance — Rachel Conlan departure; Eowyn Chen interim CMO** (CoinDesk 2026-05-12; PaymentExpert 2026-05-13) | **HELD** — `../operator-statements/binance-chen-marketing-not-hype-2026-07.md` |
| **Crypto.com — Steven Kalifowitz departure** (CoinDesk 2026-05-05, + Ministry of Sport, FX News Group, bitcoinke, MEXC relay) | **HELD** — `../operator-statements/cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md` |
| **OKX — Haider Rafique** (surfaced only as prior-employer context for Conlan) | **HELD** — `../operator-statements/okx-rafique-role-reclassification-2026-08-10.md` |
| crypticweb3.com "Top Digital Assets Marketing Leaders in 2026" | **REFUSED — agency listicle, not an operator statement.** Named so it is not re-surfaced as a near-miss |
| cryptocurrencyjobs.co "CMO at EXMO" | **REFUSED — a job advertisement, and EXMO is not in the cohort** |

**No 2026 appointment to any tracked firm's top marketing seat is publicly visible — third consecutive run.** Theme-4 datum with the clock advanced: **nine weeks after Binance's CMO exit and seven weeks after Crypto.com's took effect, neither firm has publicly named a permanent successor, and neither firm's own estate carries a dated record of the change.**

**One scope note.** The VARA capture contains a quotable statement from *"VARA's Regulatory Affairs and Enforcement Division"* — *"Unlicensed activity and unauthorised marketing will not be tolerated."* **Not admitted to class 4: it is unattributed to a natural person and the speaker is a regulator, not a marketing operator at a tracked firm.** It lives in the class-3 file where it belongs.

### 5. Layoffs — **0 NET-NEW ROWS. Tracker holds at 24. But the re-read produced an instrument property the corpus did not have.**

The 08-07 CryptoJobsList crossref was **re-executed seven days later against the same URL**. → `../layoff-tracker/_aggregator-crossref-2026-08-14.csv` (NEW).

**🟢 THE AGGREGATOR PASSES THE ARITHMETIC-INTEGRITY TEST THAT ROOTDATA FAILED ON 08-13.**

| | 2026-08-07 | 2026-08-14 | delta |
|---|---|---|---|
| rows | 54 | 56 | **+2** |
| companies | 50 | 52 | **+2** |
| jobs cut (headline) | 7,294+ | 7,339+ | **+45** |

The two new rows are **Bitwise (−25)** and **Certora (−20)**. **25 + 20 = 45, exactly.** The headline total moved by precisely the sum of the new rows and **no prior row was revised.** That is the direct opposite of RootData, whose count was a *range* that moved *downward* on verification. **Over this 7-day window CryptoJobsList behaves as a monotonic append-only ledger, and Phase 2 may describe it that way with the window stated.** It remains **not a primary source** and **not an industry denominator.**

**Corpus recall against this one public list: 19/54 = 35% (08-07) → 24/56 = 43% (08-14).** Second point on a series that previously had one. Honest reading: **the gap closed from both ends** — the corpus added five rows while the aggregator added two.

**One net-new candidate: Certora** (2026-06-18, −20, −30%, market conditions, single-sourced to thecoinformer.com). **Not entered.** Its date is two months old, which shows the aggregator **backfills**: *new to the list* ≠ *new event*. That is itself a property worth having.

**Three unchanged items that gain weight by being unchanged across two independent reads:** the **FalconX 19-day date conflict** is stable, not drifting (so it is not aggregator noise); the **Coinbase 2026-03-05 −18% row** — still the highest-value unheld row, still unverified; the **Optimism/OP Labs same-date double-listing** has **not** been reconciled in seven days, which is direct evidence for watch (u). And **Bybit's arithmetically impossible row (−15 at −20%) still has an EMPTY source column** — the clearest demonstration that this list does not retire unvetted rows.

**Bitwise gets a third date.** The aggregator dates the event **2026-08-07**, against the corpus row's **2026-08-11 [VERIFY]** (Bloomberg slug) and **2026-08-12** (captured prose "published on Wednesday"). **Three candidates, none asserted, all recorded** — watch (aa) in its cleanest instance; 08-07 is plausibly the announcement and 08-11/08-12 the reporting. **The same read independently corroborates the row's −25 and −14%,** which the corpus had derived arithmetically. Row 24's notes updated; **the row's date field is unchanged.**

**Standing finding UNCHANGED, cohort-scoped: no TRACKED firm's 2026 contraction has named marketing as an affected function.** 24 rows.
**The nine-run non-AI rationale streak is unchanged** — no new contraction arrived to test it.
**Gnosis `[VERIFY]` — NOT CLOSED. 12th run carried.** Blocked by watch (jj), not by effort.

### 6. NorthPoint longitudinal panel

`trend-data.json` **60 days stale**. **No trend claim made.**

---

## What this run did to the mandate

| # | 08-13 recommendation | status |
|---|---|---|
| 1 | Check whether the retry-queue seed arrived; if not, one line and move on | **✅ DONE, AND DELIBERATELY UNDER-REPORTED.** It did not arrive. §0, one line. Not re-issued. |
| 2 | **Patch the feed-health guard — the only item the corpus can fix by itself** | **✅ DONE IN CODE, AND VERIFIED BOTH WAYS.** Second predicate shipped; `_feed-fingerprint.json` added; `scripts/README.md` rewritten to document it; HEALTHY/STALE discrimination demonstrated, idempotency demonstrated. **Watches (bb) + (ff) CLOSED.** |
| 3 | **Class 3: change the METHOD, not the vocabulary — ESMA pre-deadline index, VARA at source, MAS register** | **✅ DONE FOR VARA, AND IT WAS THE RIGHT CALL.** First at-source VARA sweep in the project's history; 13-run class-3 zero ends; a printed claim gets corrected. **ESMA's pre-deadline index window and the MAS register remain unswept — now the only two objects on that list.** |
| 4 | The Friday nomination-cadence test falls today | **🔴 FAILED, AND IT IS THE ONLY ITEM HERE WITH A THIRD PARTY ON THE OTHER SIDE.** See below. |
| 5 | Escalate seven items | **DONE — below, at seven, with two closed, two rewritten, one added.** |

### 🔴 Mandate item 4 — the Friday test, failed honestly

**Today is Friday 2026-08-14, the date the 08-11 record scheduled this test for.** `README.md` tells the public, in the "Open call — nominate a public signal" section: *"Inbound nominations are read every Friday."*

**`inbound-nominations.md` still does not exist.** This run has **no read access to `hello@northpoint.fi`** — the mailbox is not exposed to the corpus repo, no inbox artifact for that address exists in the sales-funnel tree, and none was seeded into the run. **The corpus therefore cannot say whether nominations arrived, and will not say that none did — an unread mailbox is not an empty mailbox.** That is the same distinction as watch (hh), applied to the one surface where a third party is on the other side of it.

**Two clean fixes, both owner actions, both cheap:** either route `hello@northpoint.fi` into an artifact the run can read, or **amend the README sentence to describe what actually happens.** Escalated as item (ii). **This is the only open item in the repo that is a public-facing promise rather than an internal defect, and it has now been carried past its own scheduled test date.**

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-44 silence HOLDS, AND ITS SCOPE IS NOW CORRECTLY STATED FOR THE FIRST TIME.** Thirteenth consecutive EU-NCA zero. **The unqualified phrase "named marketing-side enforcement silence" is retired from this corpus — it was false outside the EU and the VARA register proves it.** Print only: *no EU NCA has published a named marketing-side enforcement action against a CASP since the transitional deadline.* The method caveat in (w) still attaches.
- **(c) Capture panel** — untouched.
- **(d) Agency panel staleness — 60 days**, byte-identical output six runs running. **12th run.**
- **(e′) Cadence** — **🟢 ON TIME. 1 of 4.**
- **(f) Friday nomination cadence** — **🔴 FAILED ON ITS OWN SCHEDULED TEST DATE.** No read access; refusing to claim an absence. Escalation (ii).
- **(g) Coinbase n=1** — unchanged, open.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED. Untested today** (no new contraction). Nine-run non-AI streak intact; temporal hypothesis still unevidenced. **Do not print.**
- **(i) Kraken paid-media build-out** — unchanged.
- **(j) Senior-leader exits** — **ADVANCED IN CLOCK ONLY.** Nine weeks (Binance) / seven weeks (Crypto.com) with no publicly named permanent successor; third consecutive run finding nothing new.
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 too narrow AND provenance-blind** — **13th costing. The definitional half loses ground for a second consecutive run:** the VARA statement was correctly refused (regulator, not operator; no natural person). The provenance half remains live and is subsumed by (jj).
- **(m) Ad-platform gating** — discharged.
- **(n) Full-range re-sweep of classes 3, 4, 5** — **🟢 THE BIGGEST MOVEMENT THIS WATCH HAS EVER SEEN. Class 3 was re-swept by a different METHOD and returned a correction to a printed claim** — the first evidence that class 3's zeroes were measuring the instrument. Class 4: third clean recall check (5/5 held or correctly refused). Class 5: third (all candidates held).
- **(o) Date the document, never an event held about it** — **APPLIED.** Bitwise now carries **three** recorded date candidates, none asserted. VARA rows dated from the register's own date column.
- **(p) Absence claims tested against firms' OWN channels** — **🔴 BLOCKED, 3rd run. Same root cause as (jj).** ⚠ **But today shows the watch generalises beyond firms: the corpus's twelve-run class-3 absence claim was never tested against the REGULATOR's own channel either, and it was wrong when it finally was.** (p) is hereby broadened to cover regulators.
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — unchanged.
- **(s) Robinhood row misclassified** — unchanged, **13th run.**
- **(t′) / (dd) duration claims** — reclassified to Phase 2 on 08-13. **Off the daily agenda. Not carried.**
- **(u) Brand absorption defeats name-keyed sweeps** — **STRENGTHENED TWICE TODAY.** The aggregator still carries Optimism and OP Labs as separate same-date rows after seven days; and VARA files the same firm under **four legal-entity names** while the world knows it as "KuCoin". **An entity-alias table is no longer a nicety — the class-3 register is keyed on legal persons and the cohort is keyed on brands.**
- **(v) NCA sweep** — 6 of 6 over its window; **VARA now added as a swept non-NCA regulator.**
- **(w) Class-3 sweep vocabulary AND method** — **🟢 PARTIALLY DISCHARGED, FOR THE FIRST TIME.** The method half was the right diagnosis and one execution proved it. **ESMA's pre-deadline 2026 index window and the MAS register remain unswept — the list is down from three objects to two.**
- **(x) `fetch_errors`** — unchanged; Aave 12th consecutive; four upstream company-list gaps, **12th run**.
- **(y) Pre-2026 class-1 rows are arithmetic inferences** — unchanged.
- **(z)** — CLOSED 08-11. Do not reopen.
- **(aa) Announcement vs effective dates** — **10th run, and today's Bitwise instance is the cleanest yet: three dates, one event, all recorded, none asserted.**
- **(bb) Class-1 feed-health guard** — **🟢 CLOSED.** Second predicate shipped and verified both ways.
- **(cc) Secondary layer going machine-written** — **not tested today; every class-3 admission came from a regulator's own domain, which is the structural answer to (cc) rather than a measurement of it.**
- **(ee) A source cited once is a source not used as an instrument** — **DISCHARGED SPECTACULARLY ONCE, PROSPECTIVE ONCE.** VARA was named-and-unused in six consecutive records; used today, it produced the run's headline. **This is the strongest possible argument for the watch.** `casptracker.eu` named a fourth time and still unused.
- **(ff) Feed-health guard tests direction, not magnitude** — **🟢 CLOSED with (bb).** Delta is now printed and load-bearing.
- **(gg) six classes in `methodology.md`, seven directories in `corpus/`** — unchanged. Rewrite queue holds at **§1, §4, §5, §6, §7**.
- **(hh) A failed fetch is not a fetched absence** — **STANDS, and today it acquired a sibling: an UNREAD MAILBOX IS NOT AN EMPTY MAILBOX** (the Friday test). Same principle, different surface.
- **(ii) Adjacency inside a corpus file is not attribution** — Phase-2 blocker, blocked by (jj).
- **(jj) The corpus can write a retry queue but cannot read from it** — **UNCHANGED. Seed did not arrive. Not re-issued as a run task.** Escalation (i).
- **🆕 (kk) A REGULATOR'S SUMMARY TABLE IS NOT THE REGULATOR'S RECORD.** VARA's fines table stops at 2026/01/13 while its notices index carries four later Notices of Fines on the same host. **Any future regulator sweep must read both the register and the notices/press index, and any count derived from one surface must name that surface.** The "0 fine rows after 2026-07-01" figure in the new file is explicitly a property of the table, not of VARA.
- **🆕 (ll) THE CORPUS'S ABSENCE CLAIMS HAVE BEEN TESTED AGAINST SECONDARY PRESS AND CALLED SILENCE.** Thirteen class-3 zeroes were produced by searching EU-vocabulary secondary sources; one at-source fetch overturned the claim built on them. **Every standing absence claim in this repo should now be asked one question before Phase 2: was the primary surface ever requested?** For class 3 the answer was no, for twelve runs.

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 13.8h, fingerprint 2151 → 2175, delta +24. Clean absence permitted.**
2. **Guard patch + three-way verification run** (real / idempotency / forced-zero-delta discrimination), state restored, real run re-executed.
3. Repo dedup pass: 08-13 record in full; four root docs in full; `csv.DictReader` over all 24 tracker rows; seven directory indexes; `_aggregator-crossref-2026-08-07.csv` in full; repo-wide grep on nine new-entity keys — **vesta, "open network", "ton foundation", certora, coinmena, shelbit ALL returned ZERO hits: net-new confirmed, not assumed.**
4. WebSearch — MiCA marketing-communications enforcement / CASP / NCA / August 2026 → **the same secondary layer as 08-10/08-11/08-13. 0 admitted. Fourth identical set; the search route is exhausted and is now formally recorded as such under (w).**
5. WebSearch — crypto layoffs August 2026 marketing team cuts → **0 net-new; Bitwise held; surfaced the CryptoJobsList URL into the provenance set.**
6. **`web_fetch cryptojobslist.com/crypto-layoffs` → HTTP 200, full body.** The 7-day longitudinal re-read.
7. **`web_fetch trendingtopics.eu/more-than-7000-jobs-gone-…` → 200 but EMPTY BODY. NOT USABLE.** Recorded as a failed fetch, **not** as a fetched absence (watch (hh)). Added to the retry queue that cannot currently be read — which is the point of escalation (i).
8. WebSearch — VARA Dubai marketing regulations enforcement 2026 → **surfaced `vara.ae` into the provenance set. The method change begins here.**
9. **`web_fetch vara.ae/en/regulations/regulatory-notices/vara-steps-up-enforcement-…` → HTTP 200, full body.** 7 Oct 2025, 19 unnamed firms, AED 100k–600k.
10. **`web_fetch vara.ae/en/enforcement/` → HTTP 200, full body.** **The 37-row fines register. The run's headline.**
11. **`web_fetch vara.ae/en/regulations/regulatory-notices/` → HTTP 200, full body.** The 30-item notices index. **The two-surface disagreement, watch (kk).**
12. **`web_fetch vara.ae/…/vara-notice-of-fines-peken-global-limited-kucoin/` → HTTP 200, full body.** Tracked-firm exposure; charge read as licensing, not marketing.
13. **`web_fetch vara.ae/…/vara-investor-and-marketplace-alert-…-kucoin/` → HTTP 200, full body.** The marketing-prohibition limb.
14. WebSearch — crypto exchange CMO / head of marketing 2026 (Bitpanda, Kraken, Bitstamp, OKX named) → **0 net-new; 3 held, 2 refused with reasons.**
15. **Not reached / not guessed:** MEXC · CoinMENA · Shelbit notice bodies · VARA enforcement PDFs · `vara.ae/en/enforcement/unlicensed-vasps/` · `rulebooks.vara.ae` · ESMA pre-deadline 2026 index window · MAS PSN08 + register · CONSOB July PDFs · the eight retry-queue URLs · the Gnosis `[VERIFY]` URL · the ten Stratum-1 estate URLs · `hello@northpoint.fi`. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/regulator-filings/vara-enforcement-register-at-source-2026-08-14.md` — **NEW. The run's headline.** Full 37-row register transcription with computed tallies (35/37 marketing limb · 9/37 marketing-only · 1 row in 2026 · 0 post-deadline in the table); the TON Foundation marketing-regulations-only case; the Vesta Prime 2026 marketing-only row; KuCoin/MEXC tracked-cohort exposure with the licensing and marketing limbs kept separate; the two-surface disagreement; five explicit scope refusals.
- `corpus/layoff-tracker/_aggregator-crossref-2026-08-14.csv` — **NEW.** 7-day longitudinal re-read: append-only integrity confirmed by exact arithmetic (+2 rows / +2 companies / +45 jobs = 25 + 20); recall 35% → 43%; one new candidate (Certora, not entered); a third Bitwise date; three unchanged conflicts that gain weight from being unchanged.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **row 24 notes extended** with the third date candidate and the independent corroboration of −25 / −14%. **Date field unchanged. Row count unchanged at 24.**
- `scripts/daily-corpus-sync.py` — **feed-health guard second predicate**: fingerprint delta persisted, printed, and enforced; STALE on zero delta regardless of age; same-day idempotency preserved.
- `scripts/README.md` — feed-health section rewritten to document the two-predicate AND, why the second predicate exists, and the both-ways verification.
- `corpus/job-postings/_feed-fingerprint.json` — **NEW.** Guard state, 90-entry rolling history; the single backfilled 08-13 entry carries a `provenance` field.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — date re-stamps / byte-identical rewrites (sync, 6th run).
- `findings/longitudinal-2026-06.md` — day-44 shift appended.
- **Layoff tracker: 24 rows, unchanged. Operator statements: 6, unchanged (5/5 recall). Regulator: +1 capture — FIRST NON-ZERO IN THIRTEEN RUNS. Job postings: 0 net-new, and for the first time a GUARD-CERTIFIED clean absence.**

---

## Recommendation for next run

1. **🟢 FINISH THE JOB THE METHOD CHANGE STARTED — SWEEP THE REMAINING TWO OBJECTS AT SOURCE: ESMA's pre-deadline 2026 index window, and the MAS enforcement register.** Today is the proof of concept: **one at-source fetch corrected a claim thirteen runs of searching had built.** The 08-13 record named three objects; one is done. **This is now the highest-expected-value action available to a daily run, and it needs no owner input** — a search surfaces the domain, then fetch the regulator's own index. **If either returns nothing, that is a MEASURED absence at the primary surface, which is worth more than the twelve unmeasured ones behind it.**
2. **Re-read every standing absence claim in the repo against watch (ll) and mark each one `primary surface requested: yes/no`.** Class 3's twelve zeroes were the biggest one and it is now known to have been `no`. **This is a one-pass audit over the run records and it will tell Phase 2 which of its absences are findings and which are artifacts.** Cheap, and it is the direct generalisation of today's result.
3. **Promote AscendEX from the aggregator queue, or state why not.** It is the only 2026 row in CryptoJobsList whose stated reason is `Regulatory`, it is an exchange shutdown nine days after the MiCA deadline, and it has now sat unverified across two crossreads. **It cross-reads directly against today's class-3 work and against the corpus's "exits, not enforcement" post-deadline narrative.** One fetch of `ascendex.com` first-party settles it.
4. **Do NOT re-issue the retry queue.** Third run on the same constraint; the seed did not arrive. **Check in one line, move on.**
5. **Escalate to Jukka — seven items, in order:**
   - **(i) 🔴 UNCHANGED AND NOW THREE RUNS OLD: ONE TOOLING CONSTRAINT BLOCKS FOUR OF THE CORPUS'S HIGHEST-VALUE OPEN ITEMS.** Watch (jj). Blocked: the (hh) retry queue (now nine entries — trendingtopics.eu joined it today), the (p) estate sweep, the (ii) re-test, the Gnosis `[VERIFY]`. **Fix: paste the queue's URLs verbatim into the scheduled-task prompt so they enter the provenance set.** One edit, four items unblocked. **Today is evidence for the fix, not against it: the ONE thing that worked this run worked because a search put a domain into the provenance set and the run could then fetch it four times.**
   - **(ii) 🔴 THE README MAKES A PUBLIC PROMISE THE RUN CANNOT KEEP, AND TODAY WAS ITS SCHEDULED TEST DATE.** *"Inbound nominations are read every Friday."* The run has no access to `hello@northpoint.fi`; `inbound-nominations.md` does not exist. **The corpus will not claim an empty mailbox it never opened.** Two cheap fixes: route the mailbox into a readable artifact, or amend the sentence. **This is the only open item with a third party on the other side of it, and it is the one most likely to be noticed by a reader on Sep 1.**
   - **(iii) 🟢 A CLAIM THE REPORT WAS GOING TO PRINT HAS BEEN CORRECTED BEFORE IT SHIPPED.** "Named marketing-side enforcement silence" was false outside the EU. **Correct scope: EU NCAs only, post-deadline.** VARA published named, dated, fined marketing-perimeter actions throughout the window and one marketing-**conduct** action against The Open Network Foundation. **This is the most consequential single edit made to the corpus's Theme-4 spine, and it came from executing the previous run's recommendation literally.**
   - **(iv) 🟢 CLASS 3 NOW HAS ITS BEST OBJECT: A NAMED FOUNDATION FINED SOLELY FOR HOW IT MARKETED,** with a Public Statement attached — the only such sanction in VARA's register. **Theme 4 has been short of exactly this, and it is now in the corpus with a primary URL.**
   - **(v) `methodology.md` STILL NEEDS FIVE SECTIONS REWRITTEN: §1, §4, §5, §6, §7 — TWELFTH run for §1**, and §6's *"daily 18-agency panel"* now describes a file 60 days stale. **Still the one thing in the repo that could embarrass the report.** ⚠ **§3 now also needs a sentence**: it names VARA as a source class and the corpus went twelve runs without opening it.
   - **(vi) THE CLASS-5 DENOMINATOR IS STILL NOT COMING, BUT THE INSTRUMENT IS BETTER UNDERSTOOD THAN IT WAS.** CryptoJobsList is append-only and arithmetically self-consistent over a measured 7-day window; RootData is not. **Phase 2 prints primary-verified rows with no industry coverage percentage — and MAY print corpus recall against CryptoJobsList (35% → 43%) named as exactly that, with both dates.**
   - **(vii) AN ENTITY-ALIAS TABLE IS NOW LOAD-BEARING, NOT A NICETY.** VARA files KuCoin under **four legal-entity names**; the aggregator carries Optimism and OP Labs as two rows on one date. **The class-3 register is keyed on legal persons and this cohort is keyed on brands.** Watch (u) has been open since June on a cosmetic argument; today it has a concrete cost — **without the table, a register sweep for "KuCoin" returns nothing.**
