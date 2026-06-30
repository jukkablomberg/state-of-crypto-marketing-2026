# Corpus-assembly daily run — 2026-06-30

**Run type:** Phase-1 daily corpus assembly (automated, daily cadence per 2026-06-26 framework upgrade).
**Methodology:** public-source synthesis only. Every entry anchored to a primary/public source with a URL. No off-the-record, no anonymised, no guessed URLs. Absence of public signal is recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + the 18-agency comparison panel in `../../tracked-firms.md`.
**Dedup baseline read before searching:** prior runs `2026-06-29`, `2026-06-28`, `2026-06-27`, `2026-06-26`, `2026-06-20`; `regulator-filings/` (FCA club-sponsorship; ESMA 23-Jun wind-down; AMF national amplification; Binance MiCA EU-exit); `operator-statements/sport-sponsorship-reset-2026-05.md`; `layoff-tracker/2026-layoff-tracker.csv` (8 rows pre-run); `agency-overlap-matrix.csv` (8 rows, 1 overlap); `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

> **Directory naming:** following the repo's existing `corpus/regulator-filings/`. New this run: `corpus/marketing-campaigns/` for firm-side marketing-action items that are neither regulator filings nor named-operator statements (rationale in the file header). Autonomous, documented choice.

---

## Headline result

**The deadline-eve run closes the corpus's last open Theme-3 gap: the competitive-capture half is now on the record — named firms, dated windows, quantified offers.** Net totals: **0 job-posting rows, 0 agency-matrix rows, 0 net-new regulator entries (1 cross-ref update), 0 operator statements, 0 layoffs, +1 new marketing-campaigns corpus file.** This is a substantive-growth run (not a tighten): the one piece every June note flagged as missing — *licensed Tier-1s visibly capturing the migrating EU marketing surface* — arrived, verified across two dated sources.

Substantive advance this run:

1. **MiCA competitive-capture campaigns (new corpus item, Theme 3).** Three tracked Stratum-1 firms launched EEA-geofenced acquisition promotions explicitly targeting Binance/Bybit-Global's displaced EU users: **OKX** 8% deposit/transfer bonus (€20k cap, 52 weeks); **Coinbase** 5% transfer bonus before July 13 (named markets DE/FR/IT/BE/PL/SE/UK); **Kraken** €1M prize draw (one entry per euro deposited 22 Jun–31 Jul). The MiCA licence is now a monetised, real-time acquisition weapon — the report's central Theme-3 claim is now a demonstrated *symmetry* (cessation + capture both in the public record), not a directional argument. → `../marketing-campaigns/mica-competitive-capture-2026-06.md`.
2. **Bybit two-state gate-stack case (net-new Theme-1/Theme-4 detail).** Bybit Global progressively limits EEA access from 1 July, while **Bybit EU stays MiCA-authorised via an Austrian licence** — same brand, two regulatory states. ESMA's brand-vs-entity warning makes this a clean "read visibility at the entity level, not the brand level" illustration.
3. **Market-structure quantification.** 244 MiCA CASP licences approved as of 2026-06-29; Germany leads with 57; Greece/Hungary/Poland/Portugal/Romania at zero (Greece = Binance's withdrawn base).

Deterministic feed sync produced its standard classes-1+2 output (no upstream feed change → 0 new rows, expected and correct).

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0 (expected, idempotent).** Source A (`open-positions.json`) **scan_date advanced to 2026-06-30** (was 2026-06-29), underlying postings unchanged by source URL → dedup-by-URL producer added **0 rows**. Job-postings corpus holds at prior totals (Ava Labs ×2, Optimism ×1 from API; Solana ×3 from Chrome lane). Chrome work-queue (proprietary tracked firms) unchanged: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana(closed). Absence (no API coverage): **Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys** — re-written to `job-postings/_absence.csv` with `as_of=2026-06-30` (idempotent date-stamp refresh; `_chrome-queue.csv` likewise). **Absence-as-data note (carried, sharpened):** Binance and Bybit are both in `_absence.csv` (proprietary ATS, no API coverage) the same day they are the *named targets* of rivals' capture campaigns — the two firms under the most acute EU marketing-cessation pressure remain the least publicly legible via standard ATS scanning, while their displacement is fully legible via the rivals' marketing. The legible signal on Binance/Bybit this week is regulatory + competitive, not hiring.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0 (expected).** Source B (`trend-data.json`) lastUpdated **2026-06-15** — unchanged for a 16th day. Matrix holds at 8 tracked firms, 1 OVERLAP (**Sui — Coinbound + RZLT**). 18 dated per-agency snapshots re-written (idempotent). No new agency claim to seed.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new entries: 0. Cross-ref update: 1.** No new named marketing-side enforcement action surfaced in-window. The Binance regulator entry (`regulator-filings/binance-mica-eu-exit-2026-06.md`) received a dated 2026-06-30 cross-reference block pointing to the new capture-campaign file (closing watch item (d) from 06-29). Market-structure context logged in the capture file (244 licences / Germany 57 / five zero-issuers), **sourced to Crypto Briefing's reporting, not yet primary-verified against the ESMA Interim MiCA Register** → held, alongside the still-pending ESMA "non-compliant CASP" register check carried from 06-29. ESMA's brand-vs-entity protection warning (re-stated in coverage) logged as Theme-1/4 context, not as a new enforcement item.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new: 0 verifiable.** The only quoted operator was **OKX Europe GM Erald Ghoos** ("record new customer sign-ups ahead of the MiCA transition deadline") — a regional GM/CEO, **not** a senior *marketing* operator (CMO/VP Marketing/Head of Brand/Growth), so it does not qualify under the class-4 definition. Logged as market-structure colour in the capture file, consistent with the 2026-06-29 ruling on the same speaker. No qualifying named-marketing-operator statement at a tracked firm in-window.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** No new public 2026 marketing-team contraction with stated rationale at a tracked Stratum-1–4 firm. **BitMEX** removed its CEO/CFO/head-of-growth simultaneously (exchange reportedly seeking a buyer) — BitMEX is **not** a tracked firm and this is a C-suite/exec shake-out, not a marketing-team cut → **not added** (consistent with the perimeter-vs-tracked discipline). Crypto.com CMO Kalifowitz's exit lands end-June (already captured, May); Binance CMO Conlan's ~06-15 departure already captured. Tracker holds at 8 rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-06-30 section; last-updated bumped to 2026-06-30). Core advance: the June regulatory/competitive picture is now a **completed symmetric pair** — one regulatory event (1-July transitional-period end) simultaneously (a) darkens the unauthorised incumbents' marketing surface (Binance, Bybit Global) and (b) arms the licensed challengers' acquisition spend (OKX/Coinbase/Kraken), both halves publicly observable and primary-source-anchored. Plus the net-new Bybit two-state (Global vs Austrian-licensed EU) gate-stack detail.

---

## Searches run (audit trail)
1. `ESMA list non-compliant crypto CASP register June 2026 MiCA national competent authorities` → ESMA Interim MiCA Register exists (Arts. 109–110; weekly updates; non-compliant-entities section), but **no primary named list verified at run time** → register check remains held (no secondary-only logging, no guessed URLs).
2. `crypto exchange cease EU marketing June 30 2026 MiCA transitional deadline withdraw onboarding` → reconfirmed wind-down obligations (cease marketing/solicitation, stop onboarding, geo-block); Binance EU-exit already captured; "80%/1,000-firm" exit figures remain industry estimates (excluded).
3. `crypto marketing CMO head of growth layoffs late June 2026 exchange team cuts` → no net-new tracked-firm marketing-team cut; BitMEX exec shake-out reviewed and excluded (non-tracked, not marketing-specific).
4. `Kraken OKX Coinbase Bitvavo capture EU users MiCA July 2026 marketing campaign Binance exit` → **the capture-campaign find.** Verified across two dated primary-ish sources (below).
- Fetched + read verbatim: **Crypto Briefing (2026-06-29)** and **crypto.news (2026-06-28)** — offer mechanics, caps, windows, named markets, Bybit Austrian-entity distinction, 244-licence count all cross-checked between the two.

## Net-new / changed this run
- `corpus/marketing-campaigns/mica-competitive-capture-2026-06.md` (**NEW** — OKX/Coinbase/Kraken capture campaigns; Bybit two-state case; market-structure context; Theme-3 symmetry read)
- `corpus/regulator-filings/binance-mica-eu-exit-2026-06.md` (**updated** — 2026-06-30 cross-ref block closing watch item (d))
- `findings/longitudinal-2026-06.md` (2026-06-30 section + last-updated bump)
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` (sync re-write; idempotent `as_of` date-stamp refresh only)
- `corpus/weekly-runs/2026-06-30-corpus-run.md` (this record)

## Recommendation for next run (1 July — the deadline itself)
Re-check for: (a) the actual EU-resident onboarding/marketing pull-down going **live** on/after 1 July at Binance/Bybit Global (campaign teardown, sign-up closure, paid-media stop) — the first *completed* observable cessation, not just conceded/anticipated; (b) which EU jurisdiction Binance names for re-filing; (c) **primary-source verification of the ESMA non-compliant-CASP register AND the 244-licence / Germany-57 counts** against the ESMA Interim MiCA Register (both held); (d) whether the capture campaigns escalate or new licensed entrants (Bitvavo, Ripple/CSSF) join the EEA bonus war; (e) primary firm-page T&C URLs for the OKX/Coinbase/Kraken promos (EEA-geofenced — Chrome-lane capture) if the report's appendix needs a firm-owned source; (f) any *other* tracked unauthorised CASP forced to pull EU marketing at the deadline. Upstream feeds: `open-positions.json` scan_date 2026-06-30 (postings unchanged), `trend-data.json` lastUpdated 2026-06-15 — classes 1+2 will produce rows automatically once the underlying feeds refresh their content.
