# Corpus-assembly daily run — 2026-06-28

**Run type:** Phase-1 daily corpus assembly (automated, daily cadence per 2026-06-26 framework upgrade).
**Methodology:** public-source synthesis only. Every entry anchored to a primary/public source with a URL. No off-the-record, no anonymised, no guessed URLs. Absence of public signal is recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + the 18-agency comparison panel in `../../tracked-firms.md`.
**Dedup baseline read before searching:** prior runs `2026-06-27`, `2026-06-26`, `2026-06-20`; `regulator-filings/` (FCA club-sponsorship; ESMA 23-Jun wind-down; Binance MiCA EU-exit); `operator-statements/sport-sponsorship-reset-2026-05.md`; `layoff-tracker/2026-layoff-tracker.csv` (6 rows pre-run); `agency-overlap-matrix.csv` (8 rows, 1 overlap); `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

> **Directory naming:** following the repo's existing `corpus/regulator-filings/` (not `corpus/regulator/` in methodology.md). Consistent with prior runs.

---

## Headline result

**The 1-July watch item resolved early, in the anticipated direction — and a second regulatory + a Theme-1 thread firmed up.** Three substantive advances this run, all tightening reads already on the record (net total: 1 regulator entry net-new, 1 regulator entry updated-in-place, 2 layoff perimeter rows, 0 job-posting rows, 0 agency rows, 0 operator statements):

1. **Binance confirmed-withdrew its Greek MiCA bid (~2026-06-25).** Yesterday's lead Theme-4 case was logged as *reported* (Reuters, denied by Binance). It is now **firm-confirmed by Binance's own withdrawal** — Binance enters 1 July with no EU passport, as an unauthorised CASP for EU-resident services. Updated **in place** in the existing Binance regulator entry (same event-chain; **not** double-counted as a new item).
2. **AMF (France) national amplification of ESMA's wind-down — net-new regulator entry.** The "coordinated NCA action" watch item is now on the record, with a France-specific 30-March-2026 wind-down clock that pre-dates the EU deadline.
3. **Two perimeter layoffs (Robinhood, BitGo) repeat the Coinbase management-layer-flattening framing** — logged honestly as perimeter (non-tracked, non-marketing-specific), but the narrative convergence is a Theme-1 datapoint.

Deterministic feed sync produced its standard classes-1+2 output (no upstream feed change → 0 new rows, expected and correct).

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (expected, idempotent).** Source A (`open-positions.json`) scan_date **2026-06-26** — unchanged since the 06-27 run, so the dedup-by-URL producer correctly added 0 rows. Job-postings corpus holds at prior totals (Ava Labs ×2, Optimism ×1 from API; Solana ×3 from Chrome lane). Chrome work-queue (proprietary tracked firms) unchanged: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana(closed). Absence (no API coverage): **Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys** — re-written to `job-postings/_absence.csv` with `as_of=2026-06-28` (idempotent date-stamp refresh only). **Absence-as-data note (carried, sharpened):** Binance is in `_absence.csv` (proprietary ATS, no API coverage) the same week it confirms-withdraws its EU licence bid — the firm under the most acute EU marketing-cessation pressure remains the least publicly legible via standard ATS scanning. The legible signal on Binance this week is regulatory, not hiring.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0 (expected).** Source B (`trend-data.json`) lastUpdated **2026-06-15** — unchanged. Matrix holds at 8 tracked firms, 1 OVERLAP (**Sui — Coinbound + RZLT**). 18 dated per-agency snapshots re-written (idempotent). No new agency claim to seed.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new entries: 1. Updated entries: 1.**

- **NET-NEW — AMF (France), 23 June 2026** → `regulator-filings/amf-mica-transitional-period-end-2026-06.md`. National-NCA amplification of the ESMA 23-June wind-down, from the bloc's strictest MiCA interpreter. Adds the France-specific clock: per AMF's 5-Feb-2026 statement, unauthorised DASPs without a pending CASP application should have had a wind-down plan in place **as of 30 March 2026** — a quarter before the EU deadline. This is the "coordinated NCA action" leg the longitudinal note flagged to watch. Primary AMF page fetched + read verbatim. **Dedup discipline:** ESMA's EU-level statement is already in corpus (`esma-...`), which lists AMF as same-day corroboration; this file is logged as the distinct *NCA-operationalisation* data point, explicitly flagged so synthesis counts the rule once.
- **UPDATED IN PLACE — Binance MiCA EU exit** → `regulator-filings/binance-mica-eu-exit-2026-06.md` (new dated UPDATE block). Binance **withdrew its Greek MiCA application ~2026-06-25** (CoinDesk 2026-06-24 + Cointribune/DailyCoin corroboration), ahead of the deadline, and will seek another EU base. Graduates the case from *reported rejection (denied)* to *firm-confirmed withdrawal*; Binance enters 1 July with no EU passport. **Not** a second corpus item — same event-chain, updated.
- Reviewed, not added: the "80%-of-exchanges-exit" / "1,000 firms" projections (industry estimates from KuCoin blog, FinTelegram — not primary-source firm actions); BaFin "Risks in Focus" finfluencer framing (already in the Theme-4 backlog; 2026-01 out of fresh window). MFSA/other NCA same-day statements noted as corroboration under the ESMA entry, not separately filed.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new: 0 verifiable.** No new verbatim public statement by a named senior **marketing** operator (CMO/VP/Head-of-Brand/Growth) at a tracked firm surfaced in-window. The new statements this week are *corporate/CEO* — Tenev (Robinhood) and Belshe (BitGo) on layoffs — which do not qualify under the class-4 definition and are logged in the layoff tracker instead. Kalifowitz (Crypto.com, exit end-June) and the Conlan→Chen Binance CMO transition remain prior-captured longitudinal ticks, not net-new.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 2 (both perimeter, both flagged non-marketing-specific).**
- **Robinhood — -10% (~290 roles), 2026-06-16.** SEC-filing-backed; ~$28M restructuring charge. Stated rationale: *"flatten management layers, accelerate product velocity, remain lean and disciplined"* (CEO Tenev), who **explicitly declined the AI-blame framing**. Crypto-adjacent broker → perimeter (per Block/MARA precedent), NOT a marketing-team cut. Logged for its Theme-1 value: direct echo of Coinbase's mgmt-layer-flattening / IC-leader read. Source: TechCrunch 2026-06-16.
- **BitGo — -15%, 2026-06-26.** CEO Mike Belshe announced via X; narrows focus to five core areas (security, trading, stablecoins, settlement, AI-powered infrastructure). Custody/infra → perimeter, NOT a marketing-team cut. AI-infra repositioning narrative (ai_cover Y). Source: CryptoJobsList layoffs tracker (durable primary X URL pending).
- **Discipline note:** neither is a tracked Stratum-1–4 firm and neither is a *marketing-team-specific* contraction, so both are perimeter rows, not core class-5 evidence. They are in the corpus for the **narrative-convergence** datapoint (management-layer flattening as the stated 2026 rationale across Coinbase/Robinhood/BitGo), not as marketing-headcount evidence. No tracked-firm marketing-team cut surfaced in-window.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-06-28 section). Three advances: (a) Binance Theme-4 case firm-confirmed; (b) the regulatory picture now reads **three layers, two timestamped** — placement (FCA→clubs), entity-permission/solicitation (ESMA 23-June + AMF national amplification with 30-March French clock), named-firm exposure (Binance); (c) a cross-firm Theme-1 pattern — management-layer flattening as the *stated* 2026 layoff rationale (Coinbase/Robinhood/BitGo), with the AI-cover narrative now being publicly *resisted* (Tenev), not just asserted.

---

## Searches run (audit trail)
1. `MiCA transitional period end July 1 2026 crypto exchange cease marketing EU enforcement ESMA` → surfaced AMF national statement (net-new regulator); confirmed ESMA rule already captured; KuCoin/FinTelegram projections reviewed and excluded (estimates, not firm actions).
2. `crypto marketing layoffs June 2026 exchange brand growth team cuts` → BitGo -15% (06-26) and Robinhood -10% (mid-June) surfaced as perimeter; no tracked-firm marketing-team cut.
3. `crypto CMO "head of growth" interview podcast June 2026 MiCA marketing strategy` → no qualifying net-new named senior-marketing-operator statement at a tracked firm (class 4 = 0).
4. `BaFin AMF CONSOB CySEC crypto marketing financial promotion enforcement June 2026` → AMF/CONSOB/FMA "jurisdiction-shopping" coordination + BaFin finfluencer framing; no net-new primary firm-side enforcement action beyond items captured/backlogged.
5. `Robinhood layoffs June 2026 management layers reduction` → confirmed -10%/~290/$28M, Tenev mgmt-layer-flattening rationale, AI-blame declined.
6. `Binance Greece HCMC MiCA licence decision June 2026 EU services` → **confirmed Binance withdrew Greek bid ~2026-06-25** (CoinDesk 2026-06-24 + corroboration) — the watch-item resolution.
- Fetched + read verbatim: AMF primary page (2026-06-28).

## Net-new / changed this run
- `corpus/regulator-filings/amf-mica-transitional-period-end-2026-06.md` (**+1 regulator entry**, NCA-amplification leg)
- `corpus/regulator-filings/binance-mica-eu-exit-2026-06.md` (**updated in place** — 06-25 confirmed withdrawal block + 3 sources)
- `corpus/layoff-tracker/2026-layoff-tracker.csv` (**+2 perimeter rows** — Robinhood, BitGo)
- `findings/longitudinal-2026-06.md` (2026-06-28 section: confirmed Binance, NCA-amplification leg, mgmt-layer-flattening pattern)
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` (sync re-write; idempotent `as_of` date-stamp refresh only)

## Recommendation for next run (week of 1 July — peak window)
Re-check for: (a) which alternative EU jurisdiction Binance re-files in, and any visible interim EU-marketing restriction or campaign/onboarding pull-down; (b) any *other* tracked unauthorised CASP forced to pull EU marketing at the deadline (the cleanest completed named-firm cessation instance the corpus still lacks); (c) NCA coordinated action post-1-July (BaFin/CONSOB/AFM/CySEC equivalents of the AMF statement); (d) whether MiCA-licensed rivals (Coinbase, Kraken) publicly capture the migrating-user marketing surface. Upstream feeds (`open-positions.json` scan_date 2026-06-26; `trend-data.json` lastUpdated 2026-06-15) had not refreshed at run time — classes 1+2 will produce rows automatically once they do.
