# Corpus-assembly daily run — 2026-06-29

**Run type:** Phase-1 daily corpus assembly (automated, daily cadence per 2026-06-26 framework upgrade).
**Methodology:** public-source synthesis only. Every entry anchored to a primary/public source with a URL. No off-the-record, no anonymised, no guessed URLs. Absence of public signal is recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + the 18-agency comparison panel in `../../tracked-firms.md`.
**Dedup baseline read before searching:** prior runs `2026-06-28`, `2026-06-27`, `2026-06-26`, `2026-06-20`; `regulator-filings/` (FCA club-sponsorship; ESMA 23-Jun wind-down; AMF national amplification; Binance MiCA EU-exit); `operator-statements/sport-sponsorship-reset-2026-05.md`; `layoff-tracker/2026-layoff-tracker.csv` (8 rows pre-run); `agency-overlap-matrix.csv` (8 rows, 1 overlap); `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

> **Directory naming:** following the repo's existing `corpus/regulator-filings/` (not `corpus/regulator/` in methodology.md). Consistent with prior runs.

---

## Headline result

**Two days from the 1-July MiCA deadline, the lead Theme-4 case (Binance) tightens on the firm's own words — no new corpus item, an update-in-place.** Net totals: **0 job-posting rows, 0 agency-matrix rows, 0 net-new regulator entries (1 regulator entry updated in place), 0 operator statements, 0 layoffs.** This is an honest "tighten, don't pad" run: the upstream deterministic feeds produced no net-new rows (expected/idempotent), and the only substantive web-search advance is Binance graduating from "withdrew bid" to "firm itself confirming user impact + pre-deadline wind-down steps," plus the migrating EU surface getting quantified.

Substantive advances this run:

1. **Binance confirms the EU wind-down begins, in its own voice (update-in-place).** Binance's own X post (2026-06-24) + corporate blog concede **"some users may be impacted depending on their country and account status"** and that it will "take steps before July 1 to remain compliant." The earlier-flagged "observable onboarding/marketing pull-down" watch item is now on the record from the subject firm, not just third-party reporting.
2. **The competitive-capture read (Theme 3) gets numbers + a fresh licensed entrant.** ~83% of EU-active CASPs remain unauthorised; on euro-denominated spot, **Kraken 43.3% vs Binance 18.5%** (the licensed Tier-1 already out-holds Binance on the surface Binance must vacate); **Ripple received a preliminary MiCA CASP licence from Luxembourg's CSSF covering the full EEA** (logged as Theme-3 context, not a separate class-3 enforcement item).
3. **Scope honesty maintained:** euro pairs are ~1% of Binance's *global* spot volume — the corpus value is the named-public demonstration of the methodology's core read, not financial materiality.

Deterministic feed sync produced its standard classes-1+2 output (no upstream feed change in postings/agency claims → 0 new rows, expected and correct).

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (expected, idempotent).** Source A (`open-positions.json`) **scan_date advanced to 2026-06-29** (was 2026-06-26), but the underlying postings were unchanged by source URL → the dedup-by-URL producer correctly added **0 rows**. Job-postings corpus holds at prior totals (Ava Labs ×2, Optimism ×1 from API; Solana ×3 from Chrome lane). Chrome work-queue (proprietary tracked firms) unchanged: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana(closed). Absence (no API coverage): **Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys** — re-written to `job-postings/_absence.csv` with `as_of=2026-06-29` (idempotent date-stamp refresh only; `_chrome-queue.csv` likewise). **Absence-as-data note (carried):** Binance remains in `_absence.csv` (proprietary ATS, no API coverage) the same week it concedes EU user-impact and a pre-deadline wind-down — the firm under the most acute EU marketing-cessation pressure is still the least publicly legible via standard ATS scanning. The legible Binance signal this week is regulatory/corporate, not hiring.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0 (expected).** Source B (`trend-data.json`) lastUpdated **2026-06-15** — unchanged for a 15th day. Matrix holds at 8 tracked firms, 1 OVERLAP (**Sui — Coinbound + RZLT**). 18 dated per-agency snapshots re-written (idempotent). No new agency claim to seed.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new entries: 0. Updated entries: 1.**

- **UPDATED IN PLACE — Binance MiCA EU exit** → `regulator-filings/binance-mica-eu-exit-2026-06.md` (new dated 2026-06-29 UPDATE block). Binance's own X post (2026-06-24) + blog confirm the Greek withdrawal and concede EU user impact pre-deadline; Gillian Lynch (head of Europe & UK) tells Reuters Binance is "not leaving Europe" (target jurisdiction still undisclosed). Competitive context added: ~83% of EU CASPs unauthorised; Kraken 43.3% vs Binance 18.5% euro-spot share; Ripple's full-EEA CSSF preliminary CASP licence. **Same event-chain — not a second corpus item.**
- **Reviewed, NOT added:** an ESMA-published "list of 35+ non-compliant CASPs" (NCA-flagged, incl. CONSOB) appeared in secondary coverage but was **not** verified against a primary ESMA register at run time → **held for primary-source verification next run** rather than logged on a secondary citation (no guessed URLs). The "1,000 firms / 80%-exit" projections remain industry estimates, not primary firm actions — excluded as before.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new: 0 verifiable.** The interview that surfaced — **OKX Europe chief Erald Ghoos, "80% of crypto exchanges won't survive MiCA" (The Block)** — is a **regional GM/CEO** statement, not a senior *marketing* operator (CMO/VP Marketing/Head of Brand/Growth), so it does **not** qualify under the class-4 definition. Bybit CEO Ben Zhou's MiFID/EMI remarks (CoinDesk, 2026-04-26) are CEO-level and out of fresh window. Gillian Lynch's Binance/Reuters quote is regional-leadership/corporate (logged in the Binance regulator entry). No qualifying named-marketing-operator statement at a tracked firm in-window.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** No new public 2026 marketing-team contraction with stated rationale surfaced in-window. Crypto.com CMO Steven Kalifowitz's exit lands end-June (already captured, May); Binance CMO Rachel Conlan's ~06-15 departure already captured. The perimeter rows (Robinhood, BitGo) added 2026-06-28 stand; no tracked Stratum-1–4 marketing-team cut to add.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-06-29 section). Core advance: the Binance Theme-4 case now rests on the firm's own pre-deadline admission of EU user impact (marketing/onboarding pull-down conceded in Binance's voice), and the competitive Theme-3 read is now **quantified** (Kraken 43.3% > Binance 18.5% euro spot; ~83% CASPs unauthorised; Ripple full-EEA CSSF licence). The three-layer June regulatory picture (placement → entity-permission/solicitation → named-firm exposure) is unchanged in structure; this run deepens the named-firm leg.

---

## Searches run (audit trail)
1. `MiCA transitional period end July 1 2026 crypto exchange cease EU marketing ESMA enforcement` → confirmed ESMA 23-June wind-down rule already captured; reconfirmed "cease marketing activities and solicitation" as first wind-down obligation; "80%/1,000-firms" projections reviewed and excluded (estimates).
2. `Binance MiCA EU license re-apply jurisdiction June 2026 marketing services` → Binance withdrew Greek bid, targets undisclosed EU jurisdiction (reportedly France in some outlets; The Defiant says undisclosed), confirms EU user impact + July-1 service suspension. Update-in-place.
3. `crypto marketing team layoffs June 2026 CMO growth brand cuts exchange` → Kalifowitz (end-June) and Conlan (06-15) already captured; no net-new tracked-firm marketing-team cut.
4. `BaFin CONSOB AFM CySEC crypto unauthorised CASP marketing enforcement statement late June 2026` → AFM enforcement framing + ESMA "35+ non-compliant CASPs" NCA list surfaced in secondary coverage; held for primary verification (not added). NCA coordination messaging consistent with AMF leg already captured.
5. `crypto exchange "head of marketing"/CMO/"head of brand" interview MiCA June 2026 EU marketing strategy` → OKX Europe chief Ghoos (The Block) = regional-GM, not class-4 marketing operator; no qualifying named-marketing-operator statement.
- Fetched + read verbatim: The Defiant Binance-withdrawal article (2026-06-24); crypto.news July-1 lockout explainer (2026-06-27).

## Net-new / changed this run
- `corpus/regulator-filings/binance-mica-eu-exit-2026-06.md` (**updated in place** — 2026-06-29 block: firm-confirmed user impact, quantified competitive surface, Ripple CSSF context, +4 sources)
- `findings/longitudinal-2026-06.md` (2026-06-29 section + last-updated bump)
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` (sync re-write; idempotent `as_of` date-stamp refresh only)
- `corpus/weekly-runs/2026-06-29-corpus-run.md` (this record)

## Recommendation for next run (1 July — the deadline itself)
Re-check for: (a) the actual EU-resident onboarding/marketing pull-down going live on/after 1 July (campaign teardown, sign-up closure, paid-media stop) — the first *completed* observable cessation, not just conceded; (b) which EU jurisdiction Binance names; (c) **primary-source verification of the ESMA "non-compliant CASP" register** (held this run); (d) NCA coordinated action post-deadline (BaFin/CONSOB/AFM/CySEC operationalisation); (e) whether Kraken/Coinbase/Bitvavo/Ripple visibly capture the migrating EU marketing surface; (f) any *other* tracked unauthorised CASP forced to pull EU marketing at the deadline — the cleanest completed named-firm cessation instance the corpus still lacks. Upstream feeds: `open-positions.json` scan_date 2026-06-29 (postings unchanged), `trend-data.json` lastUpdated 2026-06-15 — classes 1+2 will produce rows automatically once the underlying feeds refresh their content.
