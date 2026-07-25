# Corpus-assembly daily run — 2026-07-24 (day 23 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Runs the morning after 2026-07-23; loop fired on cadence. Single fire, morning CEST.
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-23 back to 2026-06-26; `regulator-filings/` (Binance EU-exit chain, ESMA/AMF/FCA filings); `operator-statements/` (sport-sponsorship-reset cluster); `layoff-tracker/2026-layoff-tracker.csv` (10 rows pre-run); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.
**Operating-context note:** the 07-23 CoS session opened Phase-2 synthesis and STAGED a replacement task prompt (`../../../STAGED-corpus-task-prompt.md`) that would flip this loop to synthesis-first. That prompt is **pending Jukka's approval and has NOT been applied**, so this run correctly executes as full six-class corpus assembly. Recorded so the transition is visible in the run history.

---

## Headline result

**Day 23 post-deadline. The material result of this run is a genuine net-new class-1 event: Kraken posted TWO "Director, Paid Marketing" requisitions (United States + United Kingdom) on 2026-07-23, both URL-verified via Ashby — the FIRST Kraken rows to enter the job-postings corpus.** A dual-jurisdiction Director-of-Paid-Marketing hire is a paid-media build-out signal at a Tier-1 firm whose CGMO (Mayur Gupta) is the standing highest-probability class-4 source, and it lands eight days before Kraken's 07-31 MiCA-lapse checkpoint. Class 5 also moved: **BitMEX announced a full exchange wind-down on 2026-07-23** (effective 2026-09-23), a perimeter contraction row whose marketing-adjacent angle is a late-June Head-of-Growth/CGO departure; tracker **10 → 11**. Class 2 unchanged (`trend-data.json` still 06-15 — 39th day; **held stable by the 07-10 Path-2 snapshot decision, NOT re-escalated**). Class 3 net-zero: **day-23 named-enforcement silence holds**. Class 4 net-zero: drought persists (the surfaced Gupta interview is Apr-2025, out of window). Friday 07-24 nomination check: no `inbound-nominations.md` exists yet — nothing to intake.

1. **Class 1 breaks with a genuine net-new tracked-firm signal — Kraken paid-media build-out (the material result).** `daily-corpus-sync.py` added **2 rows** against a healthy, current feed (`scan_date: 2026-07-24`, `new_count: 2`): **Kraken "Director, Paid Marketing" — United States** (`https://jobs.ashbyhq.com/kraken.com/5e07a439-ae65-4f08-bb5e-edff883d12bb`) and **United Kingdom** (`https://jobs.ashbyhq.com/kraken.com/f0b3a00e-57a5-47eb-9d4c-9b2c1a3d9345`), both `date_posted 2026-07-23`, seniority Director / marketing, ATS=ashby, `url_verified=True`. This creates **`corpus/job-postings/kraken.csv`** (first Kraken file in the corpus). Two Director-level paid-media reqs opened simultaneously in the two largest English-language jurisdictions is a **performance-marketing scale-up** signal — notable because Kraken's public marketing identity (via CGMO Mayur Gupta) is built on the "80% of growth is still organic" thesis; a paid-Director double-hire is a visible tilt toward the paid side of that stack. Theme-1 (shape of the function) + Theme-2 (AI-in-stack, pending JD read) relevance.
2. **Class 5 moves (perimeter) — BitMEX full wind-down, and a Head-of-Growth exit precedes it.** Verified against Crowdfund Insider (2026-07-23, direct-to-users comms; `published_time 2026-07-23T08:16:32-04:00`): **HDR Global Trading Limited** will sunset the BitMEX exchange effective **2026-09-23 04:00 UTC**; new registrations halted immediately; risk-reducing-only orders from 08-26. Stated rationale: *"internal strategic assessment of the company's position and the evolving digital asset sector"* amid intensifying competition and regulatory pressure — **not** an AI-efficiency framing. **Marketing-adjacent (Theme-1/5):** in **late June 2026** BitMEX lost its CEO (Stephan Lutz), CFO, and **Head of Growth / Chief Growth Officer (Raphael Polansky)**, backfilled by internal promotions amid reported sale-exploration; the full closure indicates those efforts did not yield a continuation strategy. Logged as a **perimeter** row (BitMEX is a crypto-derivatives exchange, **not** in the Stratum 1–4 tracked cohort). Tracker **10 → 11**.
3. **Day-23 named-enforcement silence holds (class 3 absence-as-data).** Twenty-three days past the July-1 transitional-period end, still **no named marketing-side NCA enforcement case** against a tracked-cohort firm. The July sweep surfaced only framework/aggregate material (a cumulative "€540M+ in MiCA fines since enforcement began" figure that is neither named nor marketing-specific) and out-of-window items (CySEC €2.3M Jan-2026 AML/sanctions fines). Register-first, cases-later, now a twenty-three-day pattern.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 2 (genuine — feed is current and non-idempotent today).** Printed summary:
```
date: 2026-07-24
source A (jobs)   scan_date: 2026-07-24
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 2  firms: ['Kraken']
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```
**Standing `scan_metadata` cross-check guard applied and satisfied** — the two adds are genuine net-new, and the feed is healthy: `scanned_at_utc: 2026-07-23T22:45:55Z`, `scan_date: 2026-07-24`, `companies_scanned: 147` (87 API / 60 chrome-pending), `total_jobs_fetched: 2230`, `total_jobs_after_filter: 28`, `new_count: 2`, `still_open_count: 26`, `url_verification_enabled: true`, `url_verification_dropped: 0`, `fetch_errors: 6` (Wormhole, **Aave**, Injective, Bitwise, Chainlink, Elliptic — of which only **Aave** is tracked, and its error is the long-standing Lever-`aave` HTTP-404, not a new outage). No mass-fetch-error signature. Class 1 **HEALTHY, non-idempotent** — two genuine tracked-firm marketing rows added.

New file **`corpus/job-postings/kraken.csv`** written (2 rows, both `captured_date 2026-07-24`, both `url_verified=True`, `src=open-positions.json 2026-07-24`). `_absence.csv` and `_chrome-queue.csv` are **date-only re-stamps** (2026-07-23 → 2026-07-24); `git diff` confirms content byte-identical otherwise, no data rows changed — Aave (Lever-404) + 5 proprietary needs-chrome firms (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys) unchanged. Phantom Head of Brand Creative (07-02) and Coinbase Creative Director (07-17) remain the prior latest genuine class-1 rows; today's Kraken pair is the newest. Coinbase brand-rebuild watch item (g) stays at **n=1** (no second Tier-1 senior brand/creative requisition this run — the Kraken reqs are paid-performance, not brand/creative).

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 39th consecutive day unchanged.** Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots written (idempotent). **NOT re-escalated:** per the 07-23 CoS reconciliation, agency-panel staleness is a **deliberate Path-2 snapshot decision (Jukka, 07-10)** — Theme 3 cites the panel as-of 2026-06-15 by design, and the prior loop's daily re-escalations of this as "highest-value unblock" were stale. Recorded here as a stable, known state, not an open blocker.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-23 sweep returned only already-captured or out-of-scope material:
- **Aggregate/framework** — a widely-cited "€540M+ in MiCA fines since enforcement began" figure is a cumulative sector total, **neither named to a tracked firm nor marketing-side-specific** → below the class-3 bar.
- **CySEC** — €2.3M in fines (Jan-2026) is **AML/sanctions-scope**, out-of-window, and not a marketing-side case; recurring CySEC enforcement (TradeEU/Titan Edge operator) is non-crypto-marketing.
- **BaFin / AMF** — no net-new named marketing-side action surfaced; BaFin's crypto posture remains unauthorised-entity warnings + finfluencer supervision; AMF's remains the unauthorised-entity blacklist (unauthorised-entity instruments, not marketing-side cases against tracked CASPs).
- Recurring **FCA→HTX** financial-promotion action = out-of-window UK case, already captured.

**Absence-as-data: the post-deadline named-enforcement silence is now twenty-three days long.** Register-first, cases-later. Policing is devolved to 27 NCAs (per the already-captured ESMA statement `ESMA75-113276571-1710`); a centralised marketing-enforcement action was never the mechanism — cases, when they come, arrive from NCAs one at a time.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** CMO / Head-of-Brand / Head-of-Growth sweep surfaced only non-qualifying or out-of-window material:
- **Kraken CGMO Mayur Gupta** — the strongest candidate given today's Kraken class-1 signal, but the surfaced flagship interview (20VC / "Inside Kraken's $1.5BN Growth Playbook") is dated **Apr 25, 2025** (`https://www.thetwentyminutevc.com/mayur-gupta`) — **out of the 2026 post-deadline window** and pre-existing, not net-new. The recurring quotes ("long-term sustainable growth can no longer happen in any silo", "an engine of ands and not an engine of ors", "80% of Kraken's growth is still organic") lack a clean dated **in-window** primary → fail the quote+URL+date bar. Carried as the highest-probability next qualifying source; the Kraken paid-Director double-hire makes an in-window Gupta statement the single most valuable class-4 capture to watch for.
- **Coinbase CMO** (variously reported as Cat Ferdon / long-term-strategy framing), **Binance Conlan→Chen (interim)**, **Crypto.com Kalifowitz (departed)**, **OKX CMO Haider Rafique** — all already captured or profile-only; OKX/Rafique The Drum (2025-03-11) remains the logged JS-render retry candidate, out-of-window, not retried this run.

The class-4 drought since the May CMO churn persists and remains a Theme-1 datum: the Binance (interim) and Crypto.com (vacated) seats that would otherwise be speaking in the post-deadline window are empty.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 1 — tracker moves 10 → 11.** Row written to `corpus/layoff-tracker/2026-layoff-tracker.csv`:

| field | value |
|---|---|
| firm | BitMEX (HDR Global Trading) **[PERIMETER — WIND-DOWN, non-tracked cohort]** |
| date_announced | 2026-07-23 |
| headcount_change / percentage | **undisclosed / wind-down (100%)** |
| source_url | `https://www.crowdfundinsider.com/2026/07/293286-crypto-derivatives-exchange-bitmex-to-wind-down-operations/` (near-primary — direct-to-users comms, published 2026-07-23) |
| ai_cover_narrative | **N** |
| marketing-specific? | **No** — full exchange wind-down; no function named. Marketing-adjacent: late-June CGO/Head-of-Growth departure precedes it. |

Verified: exchange activities cease **2026-09-23 04:00 UTC**; new registrations halted immediately; risk-reducing-only orders from 2026-08-26; unsettled positions auto-liquidated at close. Stated rationale = internal strategic assessment + evolving sector/competition/regulation (**not** AI-efficiency). Late-June 2026 departures: CEO Stephan Lutz, CFO, **Head of Growth / CGO Raphael Polansky** (internal backfills; reported sale-exploration that did not yield a continuation strategy). Corroborating exec-departure context: CoinDesk 2026-06-29.

**Cohort discipline:** BitMEX is a crypto-derivatives exchange, **not** in the tracked Stratum 1–4 cohort. Logged as a **perimeter** row (Block/MARA/Robinhood/BitGo/Exodus precedent). A full wind-down is a **distinct category** from a layoff round, flagged as such in the row notes. **Still not one row in the 2026 tracker names marketing as the affected function** — that absence continues to hold and is itself the Theme-5 finding. Note: BitMEX is the **third consecutive non-AI-framed 2026 contraction** (Polygon 07-16, Exodus 07-17, BitMEX 07-23), though a wind-down is not directly comparable to the Polygon/Exodus layoff-round rationale.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-24 section). **Two shifts:** (i) **first Kraken class-1 rows** — a dual-jurisdiction Director-of-Paid-Marketing hire is a visible tilt toward the paid side of a stack publicly narrated as ~80% organic; sharpens the Theme-1 "shape of the function" read at a Tier-1 firm and sets up a high-value class-4 pairing if Gupta speaks to it in-window. (ii) **BitMEX wind-down + preceding Head-of-Growth exit** — the non-AI-rationale cluster extends to a third July instance, and the growth-leadership-exit-before-contraction sequence is a Theme-5 pattern worth watching (echoes the "interim/empty senior marketing seat precedes the visible cut" read). Methodology guards restated and satisfied: (i) `scan_metadata` cross-check before treating job-postings counts as signal (done — the +2 is genuine, feed current); (ii) primary-source verification of the BitMEX date/rationale before entry (done — Crowdfund Insider direct-to-users comms, published 2026-07-23).

---

## Watch items
- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-23 silence logged.** Enforcement is NCA-level across 27 member states, not centralised. Leading indicators remain the ESMA non-compliant register + AMF/BaFin unauthorised-entity instruments. Watch NCA sites directly rather than aggregate search.
- **(c) Capture panel** — six firms, no 7th entrant; Ripple still licence-only. **Nearest lifecycle checkpoint: OKX 8% + Kraken lapse 07-31** (7 days out).
- **(d) Agency panel staleness — 39 days** (`trend-data.json` 06-15). **Reclassified: stable-by-decision, not a blocker** (07-10 Path-2 snapshot; Theme 3 cites as-of 06-15). No longer re-escalated daily.
- **(e) Loop cadence** — 07-24 fired on cadence after a clean 07-23 (which itself followed a 07-21/07-22 no-fire gap). A **duplicate task-trigger fired mid-run today**; handled by continuing the single execution (deterministic sync idempotent + corpus-wide dedup protect against double-writes). Scheduler health check carried.
- **(f) Friday nomination cadence** — today **is** Friday 07-24; checked — **no `inbound-nominations.md` exists**, nothing to intake. Next check Friday 07-31.
- **(g) Coinbase brand-rebuild signal** — holds at **n=1** (Creative Director, 07-17). Today's Kraken reqs are paid-performance, not brand/creative — do not advance (g).
- **(h) Layoff-rationale divergence** — BitMEX is the **third** non-AI 2026 contraction rationale (after Polygon 07-16 in-cohort, Exodus 07-17 perimeter), but a **wind-down is a distinct category** and BitMEX is perimeter — so (h) is **not** advanced toward its trigger (a second *tracked* firm with a non-AI **layoff** rationale). Watch still stands.
- **(i) NEW — Kraken paid-media build-out** — two Director-of-Paid-Marketing reqs (US + UK, 07-23). Watch for (1) a matching in-window Gupta statement on the paid/organic balance (highest-value class-4 pairing), (2) whether other Tier-1 firms open Director-of-Paid reqs (a category-level shift), and (3) the JD's AI-tooling requirements for Theme-2 once the posting body is read.

## Searches / fetches run (audit trail)
1. `python3 scripts/daily-corpus-sync.py --sales ../../northpoint/sales-funnel` → classes 1+2 deterministic; **+2 class-1 (Kraken), 0 class-2**; printed summary captured above.
2. WebSearch `MiCA crypto marketing enforcement action July 2026 BaFin AMF CONSOB CySEC AFM named exchange misleading promotion` → framework/aggregate material only; **0 net-new named marketing-side case**.
3. WebSearch `crypto exchange layoffs marketing growth team July 2026 headcount cut announcement` → surfaced **BitMEX wind-down (07-23, net-new perimeter)** + captured round-ups (Crypto.com growth/CRM, Exodus).
4. WebSearch `Kraken CMO Mayur Gupta marketing interview July 2026 brand growth statement` → Gupta interviews all May-2026 or earlier; **0 qualifying in-window class-4**.
5. WebSearch `crypto CMO "head of brand" "head of growth" interview July 2026 Coinbase Bitpanda OKX Kraken MiCA marketing` → captured profiles / MiCA-competition campaign framing; **0 qualifying class-4**.
6. `web_fetch` Crowdfund Insider BitMEX article → **primary/near-primary verification** of the wind-down date (2026-09-23), 2026-07-23 announcement, rationale, and late-June CEO/CFO/Head-of-Growth departures.
7. `web_fetch` 20VC Mayur Gupta page → confirmed the flagship Gupta interview is dated **Apr 25, 2025** (out of window) → **not added**.

## Net-new / changed this run
- `corpus/job-postings/kraken.csv` (**NEW FILE — 2 net-new class-1 rows**: Kraken "Director, Paid Marketing" US + UK, posted 2026-07-23, Ashby, URL-verified; feed `scan_date 2026-07-24`, `new_count 2`)
- `corpus/layoff-tracker/2026-layoff-tracker.csv` (**1 net-new class-5 row** — BitMEX full wind-down, 2026-07-23, **perimeter**, non-AI rationale, CGO-exit-precedes; tracker 10 → 11)
- `corpus/job-postings/_absence.csv` (date-only re-stamp `as_of=2026-07-24` — Aave Lever-404 + 5 proprietary; feed healthy/current)
- `corpus/job-postings/_chrome-queue.csv` (date-only re-stamp `as_of=2026-07-24` — proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-24 section: first Kraken paid-media rows + BitMEX wind-down/CGO-exit)
- `corpus/weekly-runs/2026-07-24-corpus-run.md` (this record)

## Recommendation for next run
(a) **Kraken is the firm to watch** — the paid-Director double-hire (watch item (i)) plus the 07-31 MiCA-lapse checkpoint plus Gupta being the standing class-4 candidate make it a triple-loaded target; specifically watch for an in-window Gupta statement on paid-vs-organic. (b) **OKX 8% + Kraken lapse 07-31** is the nearest dated checkpoint (7 days) — watch lapse-vs-extend and for a 7th capture-panel entrant. (c) First named post-deadline NCA marketing-side action — day-23 silence; watch NCA sites directly. (d) Agency panel stable-by-decision (06-15 snapshot) — do NOT re-escalate. (e) Duplicate-trigger + prior no-fire gaps → scheduler health check carried. (f) Next nomination check Friday 07-31. (g) Coinbase brand-rebuild holds at n=1. (h) Layoff-rationale divergence still needs a second *tracked* firm with a non-AI **layoff** (not wind-down) rationale. **Operating-context flag for Jukka:** the staged synthesis-first prompt is still unapplied — until it is, this loop keeps collecting rather than drafting; today's Kraken + BitMEX signals are exactly the kind of net-new the collection lane is meant to catch, which argues the collection lane still has value even as synthesis opens.
