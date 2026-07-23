# Corpus-assembly daily run — 2026-07-23 (day 22 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). First run since 2026-07-20 — **07-21 and 07-22 did not fire** (loop gap; see watch item (e)). Single fire, morning CEST.
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-20 back to 2026-06-26; `regulator-filings/` (Binance EU-exit event-chain, ESMA/AMF/FCA filings); `marketing-campaigns/mica-competitive-capture-2026-06.md`; `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (9 rows pre-run); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**Day 22 post-deadline. The material result of this run is a genuine net-new class-5 row: Exodus Movement (EXOD) announced an ~25% global workforce reduction on 2026-07-17, primary-sourced to its own SEC Exhibit 99.1 — and its stated rationale is a stablecoin/payments-platform pivot, NOT the AI-efficiency framing.** This is the **second non-AI stated rationale in a week** after Polygon Labs (07-16), and it is a convergent "payments pivot" narrative. Exodus is a **perimeter row** (self-custody wallet firm, NYSE American: EXOD — *not* in the Stratum 1–4 tracked cohort), so it corroborates but does **not** by itself satisfy watch item (h), which requires a second *tracked* firm. Tracker moves **9 → 10**. Class 1 returned/held idempotent against a **current and healthy** feed (`scan_date: 2026-07-23`, 2,235 jobs, `new_count: 0`, `url_verification_dropped: 0`). Class 2 unchanged and **now 38 days stale**. Class 3 net-zero: **day-22 named-enforcement silence holds**. Class 4 net-zero: drought persists.

1. **Class 5 breaks (perimeter) — Exodus, and it repeats Polygon's non-AI pattern (the material result).** Verified against the **primary SEC Exhibit 99.1** (filed 2026-07-17): "*an operating realignment that includes a reduction of approximately 25% of the global workforce … intended to better align its cost structure and organizational priorities with its strategy to build a full-stack card issuance and payments platform … continuing the integration of Monavate and Baanx.*" Pre-tax charges $2.5M–$3.5M (severance/personnel); ~$10M–$13M annualized savings, full benefit 2027. CEO **JP Richardson** quote (not a marketing operator). **No function named — not a marketing-team-specific cut.** **Theme-5 relevance:** every 2026 *tracked-firm* cut prior to Polygon carried an AI-efficiency/AI-infra rationale; Polygon (07-16, in-cohort) and now Exodus (07-17, perimeter) both state **repositioning/payments-pivot** instead. Two non-AI rationales in one week, both framed around a *payments* pivot, is a strengthening of the 07-20 counter-instance read — though the load-bearing "AI framing is a narrative choice" claim still needs a second *tracked* firm, not a perimeter one.
2. **Day-22 named-enforcement silence holds (class 3 absence-as-data).** Twenty-two days past the July-1 transitional-period end, still **no named marketing-side NCA enforcement case** against a tracked-cohort firm. The July sweep surfaced only unauthorised-entity instruments (AMF blacklist — 38 crypto sites YTD) and a non-crypto BaFin securities fine (Brown Capital Management, €187,500, voting-rights/WpHG — not marketing). Register-first, cases-later, now a twenty-two-day pattern.
3. **Figure discipline held.** Exodus headcount recorded as `undisclosed / -25%` — the percentage is firm-stated in the SEC exhibit; an absolute headcount number was not disclosed. The $3.5M figure some secondary write-ups cite is the **top** of the primary $2.5M–$3.5M range; recorded as the range, not the point estimate.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (genuine idempotency).** Printed summary:
```
date: 2026-07-23
source A (jobs)   scan_date: 2026-07-23
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```
**Standing `scan_metadata` cross-check guard applied and satisfied** — the zero is genuine, not an outage: `scanned_at_utc: 2026-07-22T22:45:38Z`, `scan_date: 2026-07-23`, `companies_scanned: 147`, `total_jobs_fetched: 2235`, `total_jobs_after_filter: 26`, `new_count: 0`, `still_open_count: 26`, `url_verification_enabled: true`, `url_verification_dropped: 0`, `fetch_errors: 6` (Wormhole, **Aave**, Injective, Bitwise, Chainlink, Elliptic — of which only **Aave** is tracked, and its error is the long-standing Lever-`aave` HTTP-404, not a new outage). No mass-fetch-error signature. Class 1 **HEALTHY-idempotent**.

`_absence.csv` regenerated honestly to **Aave (Lever-404) + 5 proprietary needs-chrome firms** (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys), `as_of=2026-07-23`. `_chrome-queue.csv` idempotent `as_of=2026-07-23` re-stamp (proprietary list unchanged; Solana ingested). `git diff` after the sync confirmed **only these two `_` files modified — date-only re-stamps** (2026-07-20 → 2026-07-23), content byte-identical otherwise, no data rows changed. Phantom Head of Brand Creative (07-02) and Coinbase Creative Director (07-17, captured 07-19) remain the two latest genuine class-1 rows. Coinbase brand-rebuild watch item (g) stays at **n=1**: no second Tier-1 senior brand/creative requisition this run.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 38th consecutive day unchanged.** Matrix idempotent: 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots written (idempotent). **Escalation to Jukka carried and hardening for a 38th day.** The agency panel is now over five weeks stale and sits squarely inside the Phase-2 synthesis window; a class-2 finding written today would describe mid-June reality. This is upstream of this loop (needs a NorthPoint `trend-data.json` refresh) and remains **the single highest-value unblock available to the report.**

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-22 sweep returned only already-captured or out-of-scope material:
- **BaFin** — a 2026-07-10 administrative fine (€187,500) against **Brown Capital Management LLC** is **securities-law/voting-rights (WpHG)**, not crypto marketing → does not meet the class-3 bar. BaFin's crypto activity remains unauthorised-entity warnings (Verto, DAO1) + finfluencer-supervision posture — not named marketing-side misleading-promotion cases against tracked-cohort CASPs.
- **AMF** — unauthorised-entity blacklist (38 crypto sites added YTD 2026); an unauthorised-entity instrument, not a marketing-side case against a tracked firm.
- **ESMA** — transitional-period-end statement (`ESMA75-113276571-1710`) already captured; policing devolved to 27 NCAs (register-first, cases-later).
- Recurring **FCA→HTX** financial-promotion action = out-of-window UK case, already captured. Platform ad-policy changes (X/Meta/Google) = **platform policy, not regulator enforcement**, below the class-3 bar.

**Absence-as-data: the post-deadline named-enforcement silence is now twenty-two days long.** Register-first, cases-later.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** CMO / Head-of-Brand / Head-of-Growth sweep surfaced only non-qualifying or already-captured material:
- **Kraken CGMO Mayur Gupta** — still profile/role-description only (Crunchbase, Kraken press, LinkedIn), no in-window dated verbatim → fails the quote+URL+date bar. Carried as the highest-probability next qualifying source.
- **Binance CMO Rachel Conlan → Eowyn Chen (interim)** and **Crypto.com CMO Steven Kalifowitz** — already captured; re-surfaced, not net-new.
- **OKX Global CMO Haider Rafique** — The Drum interview (2025-03-11) remains the logged JS-render retry candidate; out-of-window and not retried this run.

The class-4 drought since the May CMO churn persists and remains a Theme-1 datum: the seats at Binance (interim) and Crypto.com (vacated) are precisely the seats that would otherwise be speaking publicly in the post-deadline window, and they are empty.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 1 — tracker moves 9 → 10.** Row written to `corpus/layoff-tracker/2026-layoff-tracker.csv`:

| field | value |
|---|---|
| firm | Exodus Movement (EXOD) **[PERIMETER — non-tracked cohort]** |
| date_announced | 2026-07-17 |
| headcount_change / percentage | **undisclosed / -25%** (percentage firm-stated; absolute headcount not disclosed) |
| source_url | `https://www.sec.gov/Archives/edgar/data/1821534/000119312526308023/d63529dex991.htm` (primary — SEC Exhibit 99.1) |
| ai_cover_narrative | **N** |
| marketing-specific? | **No** — no function named |

Corroborating: Exodus GlobeNewswire PR 2026-07-17; CoinDesk 2026-07-20 (`https://www.coindesk.com/business/2026/07/20/exodus-to-cut-25-of-global-workforce-in-payments-shift`). Verified against primary: ~25% global cut; $2.5M–$3.5M pre-tax charges; ~$10M–$13M annualized savings (full benefit 2027); rationale = full-stack card-issuance/payments-platform pivot + Monavate/Baanx integration; CEO JP Richardson (not a marketing operator).

**Cohort discipline:** Exodus is a self-custody *wallet* firm but is **not** one of the tracked Stratum-3 wallets (MetaMask/ConsenSys, Phantom, Ledger, Trust Wallet, Rabby). Logged as a **perimeter** row (Block/MARA/Robinhood/BitGo precedent), not an in-cohort one. Everything else in the July sweep was already-captured aggregator round-up material (Coinbase −14%, Gemini −30% YTD, Kraken ~30%, Crypto.com −12%, Polygon 07-16). **Still not one row in the 2026 tracker names marketing as the affected function** — that absence continues to hold and is itself the Theme-5 finding.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-23 section). **One shift:** the non-AI-rationale counter-pattern acquires a **second instance in a week** (Exodus, perimeter) alongside Polygon (07-16, in-cohort) — and both frame the cut around a **payments pivot**. The synthesis claim strengthens toward: *"AI framing dominates 2026 stated rationales but is not universal; where a firm has a concrete strategic story — increasingly a payments/stablecoin pivot — it tells that story instead."* Caveat preserved: the defensible "narrative choice" corollary still needs a second **tracked** non-AI instance; Exodus is perimeter corroboration only. Methodology guards restated and satisfied: (i) `scan_metadata` cross-check before treating any job-postings "absence spike" as data; (ii) cross-check aggregator-attached headcount/charge figures against the primary filing (done — recorded the $2.5–3.5M range, not the $3.5M point some write-ups cite).

---

## Watch items
- **(a) Binance re-file jurisdiction** — still France-**reported**-only; firm names no jurisdiction formally. Unchanged.
- **(b) First named post-deadline NCA marketing-side action** — **day-22 silence logged.** Enforcement is NCA-level across 27 member states, not centralised (ESMA statement). Leading indicators remain the ESMA non-compliant register + AMF/BaFin unauthorised-entity instruments.
- **(c) Capture panel** — six firms, no 7th entrant; Ripple still licence-only. **Nearest lifecycle checkpoint: OKX 8% + Kraken lapse 07-31** (8 days out).
- **(d) Agency panel staleness — 38 days** (`trend-data.json` 06-15). Escalation carried and hardening. Highest-value unblock available to the report.
- **(e) Loop cadence** — **07-21 and 07-22 did not fire; 07-23 resumes after a two-day gap.** Pattern remains irregular (07-14/15 no-fire → 07-16 double → 07-17 clean → 07-18 no-fire → 07-19 double → 07-20 clean → 07-21/22 no-fire → 07-23 clean). Corpus fully protected (idempotent sync + corpus-wide dedup on search classes); the **scheduler** still needs a health check. Escalation to Jukka carried.
- **(f) Friday nomination cadence** — today is **Thursday 07-23**; next nomination check **Friday 07-24** (tomorrow). No `inbound-nominations.md` exists yet.
- **(g) Coinbase brand-rebuild signal** — holds at **n=1** (Creative Director, 07-17). No second Tier-1 senior brand/creative requisition today.
- **(h) Layoff-rationale divergence** — **strengthens but not satisfied.** Exodus (07-17, perimeter) is the **second** non-AI, payments-pivot rationale in a week after Polygon (07-16, in-cohort). Two would-satisfy the claim only if the second were a *tracked* firm; Exodus is perimeter. Convergence on a *payments-pivot* framing (not just "non-AI") is the sharper sub-pattern to watch.

## Searches / fetches run (audit trail)
1. `MiCA marketing enforcement action July 2026 BaFin AMF CONSOB CySEC AFM named crypto exchange misleading promotion` → framework/deadline material + NCA supervisory posture; **0 net-new named marketing-side case**.
2. `crypto exchange CMO "head of brand" "head of growth" interview July 2026 Kraken OKX Coinbase Bitpanda marketing MiCA` → captured Conlan→Chen / Kalifowitz / Gupta profile; **0 qualifying class-4 statement**.
3. `crypto marketing team layoffs July 2026 growth brand headcount cut exchange announcement` → surfaced **Exodus (07-17, net-new perimeter)** + captured round-ups.
4. `Exodus Movement layoffs 25% workforce SEC filing July 17 2026 stablecoin payments` → confirmed date/percentage/rationale; primary SEC Exhibit 99.1 + GlobeNewswire located.
5. `BaFin AMF CONSOB CySEC named crypto firm marketing promotion fine warning July 2026 CASP unauthorised solicitation` → BaFin Brown Capital fine (WpHG, non-crypto); AMF blacklist (38 YTD, unauthorised-entity); **0 net-new class-3**.
6. `Kraken Mayur Gupta OR Coinbase OR Bitpanda chief marketing officer statement July 2026` → Gupta profile-only; **0 qualifying class-4**.
7. `web_fetch` SEC Exhibit 99.1 (`.../d63529dex991.htm`) → **primary-source verification** of Exodus figures, date, rationale, CEO quote, charge range.

## Net-new / changed this run
- `corpus/layoff-tracker/2026-layoff-tracker.csv` (**1 net-new class-5 row** — Exodus Movement, 2026-07-17, **perimeter**, primary SEC-sourced, AI-cover=N; tracker 9 → 10 rows)
- `corpus/job-postings/_absence.csv` (honest regeneration, `as_of=2026-07-23` — Aave Lever-404 + 5 proprietary; feed healthy/current)
- `corpus/job-postings/_chrome-queue.csv` (idempotent `as_of=2026-07-23` re-stamp — proprietary firm list unchanged)
- `findings/longitudinal-2026-06.md` (2026-07-23 section: non-AI payments-pivot counter-pattern gets a second, perimeter instance)
- `corpus/weekly-runs/2026-07-23-corpus-run.md` (this record)

## Recommendation for next run
(a) **Watch for a second non-AI rationale at a *tracked* firm** — that, not a perimeter one, converts watch item (h) into a defensible synthesis claim; and watch specifically whether the non-AI rationale keeps converging on a *payments/stablecoin pivot*. (b) **OKX 8% + Kraken lapse 07-31** is the nearest dated checkpoint (8 days) — watch lapse-vs-extend and for a 7th capture-panel entrant. (c) First named post-deadline NCA marketing-side action — day-22 silence; watch NCA sites directly rather than aggregate search. (d) **Agency panel 38 days stale — escalation carried; still the highest-value unblock.** (e) Kraken CGMO Mayur Gupta remains the highest-probability next class-4 source; the OKX/Rafique JS-render retry is available on a spare-budget run. (f) **Friday 07-24 (tomorrow) is the next inbound-nomination check.** (g) Coinbase brand-rebuild signal holds at n=1. (h) Scheduler health check carried — two-day no-fire gap (07-21/22) just occurred.
