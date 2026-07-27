# Corpus-assembly daily run — 2026-07-27 (day 26 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-07-27 ~10:15 CEST.
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** run records 2026-07-25 back to 2026-06-30; `operator-statements/` (Gupta, sport-sponsorship-reset); `marketing-campaigns/` (both files); `regulator-filings/` (ESMA/AMF/FCA/Binance-EU-exit chain); `layoff-tracker/2026-layoff-tracker.csv` (11 rows pre-run); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`. Repo-wide greps run for `ferdon`, `marketing vanguard`, `podscan`, `rooney`, `beige`, `relai`, `babics`, `hoerhager`, `rafique`, `ethena`, `common supervisory`, `operational resilience`, `swissborg`, `cryptonow` to confirm net-newness before writing.

---

## 0. Cadence anomaly — the 2026-07-26 run has no run record (operational, recorded so the gap is visible)

The deterministic sync **did** execute on 2026-07-26: `_absence.csv` and `_chrome-queue.csv` carry `as_of=2026-07-26`, and the Distribution Engineer committed them (`9ddc668`, *"distribution-engineer: sync 2 change(s) [2026-07-26 15:09]"*, 14 insertions / 14 deletions, date-only re-stamps). **But no `corpus/weekly-runs/2026-07-26-corpus-run.md` exists** — the 07-26 run produced its class-1/2 output and did not complete Step 3 (web-search classes, run record, findings update).

**Assessment:** class-1/2 coverage for 07-26 is intact and idempotent, so no deterministic data was lost. What was lost is one day of classes 3/4/5 sweeping and the audit trail for it. Today's sweeps are scoped to the **full in-window range** (per the 07-25 standing guard), so the 07-26 web-search gap is covered by construction rather than by a catch-up pass.

**Watch item (e) hardens again.** Recent cadence: 07-21/07-22 no-fire · 07-24 duplicate trigger · 07-25 clean · **07-26 partial (sync-only, no record)** · 07-27 clean. Five irregular days in seven. Scheduler health check escalated to Jukka — this is now the sixth consecutive run to carry it.

---

## Headline result

**Day 26 post-deadline. The corrected class-4 query shape produces a second high-value capture in three days — and this one lands inside the report's most heavily loaded firm.** A **2026-04-09** episode of **Adweek's *Marketing Vanguard*** supplies dated, verbatim statements from **Catherine Ferdon, Coinbase's CMO**, including a boundary-drawing position on AI in the marketing stack — *"AI can be a really powerful tool to get us to creative outcomes faster, but **AI is not creative**… you need really solid people wielding that tool"* — and the cleanest CMO-seat statement of the gate-stack's creative cost the corpus has: *"there's really strong **gravitational pull towards being beige** where I'm sitting."* Two consequences. **(1) Theme 2 gains a dated three-point sequence** — Ferdon's human-centred AI framing (04-09) sits **26 days before** Armstrong's AI-native-pods memo and 14% cut at the same firm (05-05), and 40 days before Gupta's "natively AI growth engine" at Kraken (05-19). **(2) Theme 4 gets its causal mechanism named from inside the function** rather than inferred from artefacts. This also **closes the carried Ferdon item** that runs 07-24 and 07-25 logged as "aggregator write-up only, no dated primary located." Classes 1 and 2 idempotent against a healthy, current feed. Class 3: **day-26 named marketing-side enforcement silence holds** — and a sharper piece of scope evidence arrived (ESMA's first post-deadline coordinated supervisory action, 2026-07-08, targets **custody/operational resilience, not marketing**). Class 5: net-zero, tracker holds at 11.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — genuine idempotency against a healthy, current feed.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-07-27
source A (jobs)   scan_date: 2026-07-27
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**Standing `scan_metadata` cross-check guard applied and satisfied:** `scanned_at_utc 2026-07-26T22:44:49Z`, `scan_date 2026-07-27`, `companies_scanned 147` (87 API / 60 chrome-pending), `total_jobs_fetched 2112`, `total_jobs_after_filter 29`, **`new_count 0`**, `still_open_count 29`, `url_verification_enabled true`, **`url_verification_dropped 0`**, `fetch_errors 6` (Wormhole Foundation, **Aave**, Injective Labs, Bitwise, Chainlink Labs, Elliptic — **identical set to 07-23/07-24/07-25**; only Aave is tracked, and its error remains the long-standing Lever-`aave` HTTP-404, not a new outage). No mass-fetch-error signature. `drops_summary` consistent with prior runs (1,603 excluded by function; 353 no marketing keyword; 88 no seniority signal).

**`new_since_last_scan` is empty (0 items) and there is no `chrome_supplementary` block this scan.** Consequence for finding (k): the Binance "Global Product Marketing Lead" (Dubai) item seen on 07-25 has **rotated out of the new-items window without ever becoming corpus-grade** — it never acquired a posting date or a per-posting permalink. **Binance therefore remains in `_absence.csv` as an instrumentation absence, and the Chrome-lane gap is now demonstrably lossy, not merely incomplete: a real marketing requisition at a tracked Tier-1 was observed and is now unrecoverable from the feed.** That strengthens the case for the upstream fix (Chrome lane emitting permalink + date rows into `_chrome-inbox.json`) and it is the sharpest version of finding (k) to date.

**Kraken's two 07-23 Director-Paid-Marketing rows remain in `still_open_from_prior_scans`** — fourth consecutive confirmation that the 07-24 capture is complete.

`_absence.csv` and `_chrome-queue.csv` are **date-only re-stamps** (`2026-07-26 → 2026-07-27`): 14 insertions / 14 deletions, byte-identical otherwise. No data rows changed.

### 2. Agency claims / overlap matrix (deterministic)

**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 42nd consecutive day unchanged.** Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots written (idempotent). **NOT re-escalated** — per the 07-10 Path-2 decision (Jukka) this is a deliberate snapshot; Theme 3 cites the panel as-of 2026-06-15 by design. Recorded as a stable known state.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)

**Net-new named marketing-side enforcement entries: 0. Day-26 silence holds.** Three sweeps run. What surfaced:

- **Framework/guide material only** — MiCA Art. 7/9/66 marketing-communication obligations, the up-to-12.5%-of-global-turnover penalty ceiling, ESMA's April-2026 uniform-standards statement, AMF's transitional-period reminders and its application of ESMA staff knowledge-and-competence guidelines. All already captured or below the class-3 bar (no named firm, no marketing-side case).
- **Already-captured / out-of-scope recurrences:** the FCA→HTX High Court action (Feb 2026, out-of-window UK); BaFin's **Ethena GmbH** wind-down (already logged 2026-07-17 — a token/licensing action, not marketing-side); AMF unauthorised-entity blacklist entries (instrument, not marketing enforcement).
- **Not regulator enforcement but adjacent, and worth one line:** Google's advertising policy for France changed **2026-07-01** — AMF DASP registration is no longer accepted for crypto exchange/wallet ads; advertisers must hold MiCA CASP authorisation (`https://support.google.com/adspolicy/answer/17218519?hl=en`). This is a **platform** gate, not an NCA action, so it does not enter class 3. It is however a Theme-4 datum: the licence is becoming a precondition for *paid distribution*, enforced by ad platforms ahead of, and independently of, any regulator case. Flagged for Phase-2; not written as a corpus row this run.

**Net-new class-3 scope evidence (recorded here, deliberately NOT as an enforcement row):** **ESMA launched its first post-deadline Common Supervisory Action on 2026-07-08**, and its subject is **CASPs' digital operational resilience, with emphasis on custody** — to be run by NCAs on a risk-based sample, second half 2026 through first half 2027 (`https://www.esma.europa.eu/press-news/esma-news/esma-launches-common-supervisory-action-casps-digital-operational-resilience`).

**Why this matters to the absence finding.** Twenty-six days of named-enforcement silence could be read two ways: regulators are slow, or regulators are busy elsewhere. This is the first hard evidence for the second reading. **The first coordinated, EU-wide supervisory exercise after the transitional period ended is about custody and operational resilience — not marketing communications.** The report's "register first, cases later" thesis can now be stated more precisely: *not only have no named marketing-side cases appeared, the first coordinated supervisory priority ESMA announced post-deadline points somewhere else entirely.* That is a stronger, more falsifiable claim than silence alone, and it is anchored to ESMA's own press release.

**Standing methodological caution restated:** aggregate search remains a poor instrument for this class; NCA sites should be read directly (watch item (b), still open).

### 4. Operator statements (senior marketing operators at tracked firms)

**Net-new qualifying: 1.** Written to `corpus/operator-statements/coinbase-ferdon-marketing-vanguard-2026-04.md`.

| field | value |
|---|---|
| speaker / role | **Catherine ("Cat") Ferdon — Chief Marketing Officer, Coinbase** (role at time of statement; joined Sept 2025) |
| firm / stratum | Coinbase — **Stratum 1** (Tier-1, EU-passported) |
| date published | **2026-04-09** (in-window; **pre-deadline** — flagged explicitly) |
| format | Podcast interview — *Marketing Vanguard* (Adweek), host Jenny Rooney, 32 min |
| URL | `https://podscan.fm/podcasts/marketing-vanguard/episodes/the-art-of-making-fintech-cool-with-catherine-ferdon-of-coinbase` (publisher surface: `https://shows.acast.com/cmo-moves/episodes/the-art-of-making-fintech-cool-catherine-ferdon-coinbase`) |
| date verification | four points — `article:published_time` metadata, description string, on-page published field, and the speaker's own "about six months ago" against a documented Sept-2025 start |
| themes | 2 (AI in stack) · 1 (function shape) · 4 (regulatory posture) · 5 (by sequence) |

**Load-bearing captures:** (i) *"AI can be a really powerful tool to get us to creative outcomes faster, but AI is not creative, right? So you need really solid people wielding that tool to achieve the best results."* (ii) *"there's like a lot of things that we've passed on because they're just, frankly, they're too beige… there's really strong gravitational pull towards being beige where I'm sitting."* (iii) *"there's constant regulatory scrutiny… evolving in different ways across hundreds of geographies. And so when you have that situation on the field, the first instinct is really to generate like a very sterile brand."* (iv) *"We built the tech for a decade. And my mandate is really to market for that next decade of adoption."*

**Provenance caveats recorded in the file, not suppressed:** the verbatim is from **Podscan's public partial transcript** (machine-generated, first ~20 lines only; remainder paywalled), not an Adweek-published transcript; visible ASR artefacts ("Kat", "the company store") are preserved uncorrected and flagged for audio check before publication; the Acast publisher page could not be independently fetched this run (fetch-tool provenance restriction) and is recorded for verification before the report ships.

**Method consequence — the §4 source inventory is understating the class-4 surface.** This capture came from the **marketing trade press** (Adweek), not from any of the eight crypto podcasts listed in `methodology.md` §4, and it is dated **April**. Two runs, two captures, both from outside the documented inventory (regional written crypto media on 07-25; marketing trade press today). **Recommendation: widen §4's inventory to name the marketing trade press explicitly (Adweek/Marketing Vanguard, Marketing Brew, Campaign, The Drum) — crypto CMOs speak *as CMOs* there, while crypto media interviews them as executives.**

**Also checked and NOT added this run (each verified, each excluded for a stated reason):**
- **Haider Rafique (OKX CMO)** — Blockworks "generational brand" interview **verified 2023-10-23 → out of window.** Not added. Partially resolves the long-carried JS-render retry item: that particular piece is datable and out of window regardless of render. MarketingReport.one interview **returned an empty body** on fetch — date unverified, not added, carried.
- **Magdalena Hörhager (Bitpanda VP Growth)** — *Scratch: CMO Interviews* (Rival). **No machine-readable date on the page**; secondary indications point to 2023 → treated as out of window. Not added. Bitpanda still has **no in-window senior-marketing-operator statement** in the corpus — notable for a firm the tracked-firms file flags as "deep MiCA readiness signal expected."
- **Imo Bábics (Relai CGO/CMO)** — MoneyToday profile with direct quote **verified 2021-08-20 → out of window.** Not added. The 07-25 recommendation specifically flagged Relai's DACH/IT posting velocity as a likely regional-media source; it was searched and produced nothing in-window.
- **Julian Liniger (Relai co-founder/CEO)** — MiCA-licence quote, MoneyToday **2025-10-24**, in-window. **Excluded from class 4:** CEO, not a senior *marketing* operator — consistent with the standing Erald Ghoos ruling (06-29, 06-30, 07-25). Logged as a Stratum-4 lead: the same article records Relai planning *"Marketingkampagnen und Events für 2026"* off the back of the licence, which would be a MiCA-capture-panel artefact if a dated campaign surfaces.

### 5. Layoff tracker (2026 marketing-team contractions)

**Net-new rows: 0. Tracker holds at 11.** Sweeps for 07-25 → 07-27 announcements surfaced only already-captured or non-cohort items: Exodus (07-17), Polygon Labs (07-16), BitMEX (07-23), Crypto.com (March), Gemini, Algorand, Coinbase (05-05), Messari. TechCrunch's running AI-attributed-layoffs list (updated 2026-07-25) added **Monday.com** — non-crypto, non-cohort, excluded.

**Coinbase CPO departure — still not entered.** The 07-25 run flagged Lawrence Brock's reported resignation with **conflicting dates** (2026-07-24 vs an August-17 step-down) and correctly declined to enter it. **No primary source (Coinbase filing or own-channel statement) was located this run either.** It stays out of the corpus. Watch item (j) remains at three unverified instances.

**Standing Theme-5 finding unchanged:** across all **11** tracker rows, **not one names marketing as the affected function.** Every marketing-specific read is an inference from a subsequent exit or from press attribution. That absence is the finding.

### 6. Longitudinal shift for synthesis

Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-27 section). **Three shifts:** (i) **Theme 2 gains a dated three-point AI sequence with an intra-firm 26-day gap** (Ferdon 04-09 → Armstrong 05-05 → Gupta 05-19). (ii) **Theme 4's causal mechanism is named from the CMO seat** — regulatory scrutiny as the gravitational pull toward beige — and it sits opposite Kraken Institutional's compliance-as-product-claim posture, giving Theme 4 a real axis rather than a single direction. (iii) **Class 3's absence claim is upgraded from silence to redirected priority** by ESMA's 07-08 CSA on custody/operational resilience. Methodology guards applied and satisfied this run: `scan_metadata` cross-check before treating class-1 counts as signal (done); multi-point primary-source date verification before entry (done, four points on the Ferdon page); verbatim reproduction without silent correction (done, ASR artefacts preserved and flagged); refusal to enter a conflicting-date item (done, Coinbase CPO, second consecutive run).

---

## Watch items

- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-26 silence logged, and now with scope evidence** (ESMA's first CSA targets custody, not marketing). Read NCA sites directly; aggregate search remains the wrong instrument.
- **(c) Capture panel** — six firms, no 7th entrant. **Kraken MiCA-lapse checkpoint 07-31 is 4 days out** (with OKX 8% campaign end). New Stratum-4 lead: Relai stated marketing campaigns + events planned for 2026 off its Oct-2025 French MiCA licence — watch for a dated artefact.
- **(d) Agency panel staleness — 42 days** (`trend-data.json` 06-15). Stable-by-decision, **not** re-escalated.
- **(e) Loop cadence — HARDENS.** 07-26 fired partially (sync committed, no run record, classes 3/4/5 not swept). Five irregular days in seven. **Sixth consecutive run carrying this; recommend Jukka check the scheduler.**
- **(f) Friday nomination cadence** — next check Friday **07-31**. No `inbound-nominations.md` exists.
- **(g) Coinbase brand-rebuild signal** — holds at **n=1** (Creative Director, 07-17) on the class-1 side. **But note the pairing now available:** a CMO who says the brand's problem is beige-ness (04-09) and a Creative Director requisition (07-17) are the same story told in two source classes. Not yet n=2 on postings; the qualitative half is now anchored.
- **(h) Layoff-rationale divergence** — unchanged; still needs a second **tracked** firm with a non-AI **layoff** rationale.
- **(i) Kraken paid-media build-out** — unchanged and still open. Gupta has not publicly addressed the paid build-out; that reconciliation remains the highest-value outstanding class-4 capture.
- **(j) Senior-leader exits trailing the contraction they executed** — unchanged at three unverified instances; Coinbase CPO date still unverified, still not in corpus. Needs a primary source and a fourth instance.
- **(k) Chrome-lane instrumentation gap — SHARPENS to demonstrably lossy.** The Binance Dubai marketing role seen on 07-25 has rotated out of `new_since_last_scan` without ever becoming corpus-grade, and is now unrecoverable from the feed. Binance's absence-panel entry is an **instrumentation** absence; the report must not conflate it with firm silence. Fix is upstream (permalink + date into `_chrome-inbox.json`).
- **(l) NEW — `methodology.md` §4 source inventory is too narrow.** Two of the corpus's best class-4 captures (Gupta 07-25, Ferdon 07-27) came from surfaces the inventory does not name: regional written crypto media, and the marketing trade press. Recommend a documented widening before Phase-2 writes anything about operator silence.
- **(m) NEW — ad-platform gating as a parallel enforcement surface.** Google's France policy (effective 2026-07-01) requires MiCA CASP authorisation for crypto exchange/wallet ads, replacing AMF DASP registration. Not a regulator action, so not class 3 — but if other platforms or jurisdictions follow, "who can buy distribution" becomes a Theme-4 mechanism operating faster than NCA enforcement. Watch for equivalents at Meta/X/TikTok or in other member states.

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2 deterministic; **0 net-new both**; printed summary captured above.
2. Direct read of `prospects/open-positions.json` (`scan_metadata`, `fetch_errors`, `drops_summary`, `new_since_last_scan`, `tracker_status`) → feed-health guard satisfied; established that `new_since_last_scan` is empty and no `chrome_supplementary` block exists → sharpened finding (k).
3. `git log`/`git show 9ddc668` + `weekly-runs/` listing → established the **07-26 missing-run-record anomaly** (§0).
4. WebSearch `Bitpanda CMO OR "head of marketing" interview 2026 MiCA marketing strategy` → surfaced Hörhager (Rival) + Beier (CCO); no dated in-window primary.
5. WebSearch `Magdalena Hörhager Bitpanda CMO interview Rival marketing` → Scratch/Rival episode; **undated page**.
6. `web_fetch` Rival content-hub page → no machine-readable date recoverable; **not added**.
7. WebSearch `Haider Rafique OKX chief marketing officer 2026 interview brand strategy` → Blockworks, MarketingReport, Campaign ME, Consensus-2026 speaker page.
8. `web_fetch` Blockworks OKX/Rafique interview → **date verified 2023-10-23, out of window; not added.**
9. `web_fetch` MarketingReport.one Rafique interview → **empty body**; not added, carried.
10. WebSearch `crypto exchange marketing enforcement MiCA national competent authority named action July 2026` → framework material only; **0 net-new class-3**.
11. WebSearch `BaFin OR AMF OR CONSOB OR CySEC crypto advertising misleading promotion sanction decision July 2026` → no named marketing-side case; surfaced the **Google France ad-policy change** (logged as watch (m), not class 3).
12. WebSearch `Imo Bábics Relai CMO interview marketing Bitcoin 2026` → German/Swiss regional media hits.
13. `web_fetch` MoneyToday Bábics profile → **date verified 2021-08-20, out of window; not added.**
14. `web_fetch` MoneyToday Relai MiCA-licence article → **date verified 2025-10-24**; CEO quote, **excluded from class 4** by role; logged as Stratum-4 capture-panel lead.
15. WebSearch `Relai MiCA licence France AMF announcement 2026 European expansion Bitcoin app` → corroborated the Oct-2025 licence date; no in-window marketing-operator statement.
16. WebSearch `crypto company layoffs July 2026 marketing team growth restructuring announcement` → all already captured; **0 net-new class-5**.
17. WebSearch `Coinbase Cat Ferdon CMO 2026 marketing brand interview` → **surfaced the Marketing Vanguard episode (the material find)** + CoinDesk Gen C episode.
18. `web_fetch` CoinDesk Gen C Ferdon episode page → **empty body**; not used.
19. `web_fetch` Podscan Marketing Vanguard / Ferdon episode → **primary verification**: four-point date confirmation, role, verbatim quotes, transcript-provenance caveats. **→ ADDED as class 4.**
20. WebSearch `ESMA AMF BaFin crypto marketing communication enforcement CASP first case since 1 July 2026 deadline` → **0 net-new enforcement**; surfaced **ESMA's 2026-07-08 CSA on digital operational resilience/custody** → recorded as class-3 scope evidence.
21. Repo-wide dedup greps (`ferdon`, `marketing vanguard`, `podscan`, `rooney`, `beige`, `relai`, `babics`, `hoerhager`, `rafique`, `ethena`, `common supervisory`, `operational resilience`) → the Ferdon capture confirmed net-new before writing.

## Net-new / changed this run

- `corpus/operator-statements/coinbase-ferdon-marketing-vanguard-2026-04.md` (**NEW FILE — the material result; 1 net-new class-4 capture**, Coinbase CMO Catherine Ferdon, 2026-04-09, verbatim + URLs + speaker + role + four-point date verification, window and transcript-provenance caveats recorded)
- `corpus/job-postings/_absence.csv` (date-only re-stamp `as_of=2026-07-27`; content otherwise byte-identical — Aave Lever-404 + 5 proprietary needs-chrome firms unchanged)
- `corpus/job-postings/_chrome-queue.csv` (date-only re-stamp `as_of=2026-07-27`; proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-27 section)
- `corpus/weekly-runs/2026-07-27-corpus-run.md` (this record)
- **Not changed:** `layoff-tracker/2026-layoff-tracker.csv` (holds at 11); `agency-overlap-matrix.csv` + `agency-claims/*` (idempotent); `job-postings/*.csv` data rows (0 adds); `regulator-filings/*` (0 adds — day-26 silence)

## Recommendation for next run

(a) **Keep running the corrected class-4 sweep — it is producing at a rate of roughly one high-value capture per run.** Two for two. Next priority targets, now re-ranked by the trade-press insight: **Bitpanda** (no in-window operator statement at all, and the tracked-firms file expects deep MiCA signal), **Bitstamp**, **Sui Foundation**, **Ledger**, **Phantom**. Query the marketing trade press (Adweek, Marketing Brew, Campaign, The Drum) *and* regional-language crypto media, across the full Dec-2024→ range.
(b) **Watch item (i) still the single highest-value target** — an in-window Gupta statement reconciling the Kraken paid-Director double-hire with the dated organic thesis.
(c) **07-31 is the nearest dated checkpoint (4 days)** — Kraken MiCA lapse + OKX 8% campaign end + Friday nomination check, all on the same day.
(d) **Class 3: read NCA sites directly.** Aggregate search has now returned framework-only material for 26 consecutive days. The ESMA CSA finding suggests the productive question is not "has a marketing case appeared" but "what are NCAs actually prioritising" — which is answerable from NCA supervisory work-programme pages.
(e) **Verify the Acast publisher page and the Ferdon audio** before any quote from today's capture goes into the report (transcript is machine-generated).
(f) **Escalate the scheduler cadence to Jukka** (watch (e)) and the Chrome-lane permalink fix (watch (k)) — both are outside this loop and both now have concrete evidence of cost: one lost run record, one unrecoverable Binance requisition.
(g) Agency panel stable-by-decision (06-15) — do **not** re-escalate.
