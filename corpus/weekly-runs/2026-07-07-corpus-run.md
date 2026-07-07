# Corpus-assembly daily run — 2026-07-07 (day 6 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-05 back to 2026-06-20; `regulator-filings/` (all 4 files, incl. the full Binance EU-exit event-chain file); `marketing-campaigns/mica-competitive-capture-2026-06.md` (through the 07-03 five-firm panel); `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**Net totals: 0 job-posting rows, 0 agency-matrix rows, 0 net-new class-3 enforcement entries, 0 qualifying operator statements, 0 layoffs — but ONE net-new class-3/Theme-3 marketing-campaign item: a sixth capture entrant (Gate Europe).** After two consecutive fully-zero days (07-04, 07-05), the accretion vector rotated exactly where the 07-04 note predicted it would — the capture panel, not the enforcement register.

1. **NET-NEW: Gate Europe joins the MiCA-deadline capture panel as the sixth firm (Theme 3).** Gate (Gate.io / Gate.com brand; Gate Europe = Gate Technology Ltd) is running **up to 10% deposit rewards for new EU users**, explicitly aimed at Binance's displaced France/Italy/Spain/Poland pool (Crypto Briefing, 2026-06-29, in-window). **Classification-critical verification done before adding:** Gate Europe holds a **MiCA CASP licence from MFSA Malta (granted 2025-09-29, in the ESMA register)** — so this is a *clean licensed-capture entrant*, not an unlicensed-post-deadline-solicitation case. Logged as **capture-context (non-tracked cohort)**, consistent with the Bitvavo precedent. Panel is now **six firms** (OKX 8% / Coinbase 5% / Kraken €1M / Bitpanda €25+3% / Bitvavo up-to-10%-APY / Gate up-to-10%-deposit). Added to `marketing-campaigns/mica-competitive-capture-2026-06.md` (07-07 block).
2. **Day-6 named-enforcement silence holds (class 3 absence-as-data).** Six days past the transitional-period end, still **no named marketing-side NCA enforcement case** (BaFin/AMF/CONSOB/AFM/CySEC/ESMA) on the public record. Today's sweep re-surfaced only pre-deadline instruments (AMF 1-Jul reminder, ESMA wind-down statement) plus secondary CASP-list trackers. The register-first, cases-later read (157 NCA-flagged non-compliant entities as the only public instrument in motion) extends to a six-day pattern.
3. **Bitpanda 07-05 cap outcome — RESOLVED as lapse (watch item c closed).** Two days past the stated "first 500 users / until July 5, 2026" cap, today's sweep surfaced **no primary extension signal** and no re-up; press still describes the offer with the original 07-05 window. Read: the offer closed on schedule as a bounded promotion — the first completed campaign-lifecycle datapoint the capture panel has yielded. The 500-vs-"first 1,000" secondary-cap discrepancy remains a secondary-source ambiguity (never promoted to a finding); no primary T&C page captured to arbitrate it, and the offer is now closed regardless.
4. **Binance re-file jurisdiction (watch item a) — unchanged.** Sweep re-confirmed only the already-logged posture (Teng: "dedicated to securing our MiCA license," expects one "in the coming months"; France reported as likely next jurisdiction; firm names no jurisdiction formally). A 07-06 cryptotimes "withdrawal chaos" story is the **same event-chain user-impact follow-on**, already captured in `regulator-filings/binance-mica-eu-exit-2026-06.md` — not a net-new class-3 item.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0.** Source A scan_date **2026-07-07** (feed re-stamped fresh today). No new URL-verified rows — Phantom Head of Brand Creative (07-02) stands as the latest class-1 row. Chrome work-queue unchanged (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana). Absence re-stamped `as_of=2026-07-07`: Aave (Lever API 404), Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys — absence-as-data note stands. Deterministic file deltas: `_absence.csv`, `_chrome-queue.csv` (idempotent re-stamp only).

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` lastUpdated **2026-06-15** — **22nd day unchanged.** The escalation to Jukka stands (upstream NorthPoint `trend-data.json` needs a refresh before July synthesis; not fixable from this loop; now certain to overlap the synthesis start). Matrix holds 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots idempotent.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-6 post-deadline: coordinated-action, blacklist, and NCA-warning searches returned only pre-deadline captured documents (AMF 1-Jul reminder, ESMA wind-down statement) and secondary CASP-list/guide trackers. **Absence-as-data: the post-deadline named-enforcement silence is now six days long** — register-listing running ahead of named marketing-side actions. *(The one net-new item this run is a firm-side capture campaign, logged under `marketing-campaigns/`, not a regulator action — see Headline #1.)*

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** Targeted CMO / Head-of-Marketing sweep (Coinbase/Kraken/OKX/Bitpanda) surfaced only previously-captured or non-qualifying material: the May CMO-churn items (Conlan/Binance ~06-15, Kalifowitz/Crypto.com end-June, Chen interim) are all already in `operator-statements/sport-sponsorship-reset-2026-05.md` and `regulator-filings/binance-mica-eu-exit-2026-06.md`; Mayur Gupta (Kraken CGO/CMO) surfaced as a profile, no in-window verbatim statement. No new verbatim quote by a qualifying marketing operator at a tracked firm. The class-4 drought since May remains itself a Theme-1 datum (the seats that would give post-MiCA statements sit interim/empty at Binance and Crypto.com).

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced captured items (Crypto.com −12% AI-cover, Coinbase −700, Gemini −30%, BitGo −15%, Robinhood −10%). **Yield Guild Games** surfaced as a candidate (2026-07-07 cryptonomist: "marketing support for third-party games will end entirely") but **verified OUT: non-tracked firm (crypto-gaming guild, not in Stratum 1–4), and the item is a partner-marketing wind-down, not a marketing-team headcount cut at a tracked exchange/foundation/wallet** — excluded per cohort + definition. Tracker holds at 8 rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-07 section; last-updated bumped): the capture panel reaching six firms across four NCAs (CBI/AFM/MFSA/FMA) is the run's synthesis-grade shift — the "licence-as-acquisition-weapon" dynamic is **jurisdiction-diverse**, and Gate's headline-first/sparse-disclosure style contrasts with Kraken's and Bitvavo's elaborate equal-prominence dressing, giving the report a spread of compliance-dressing sophistication within one campaign cluster.

---

## Searches/fetches run (audit trail)
1. `MiCA marketing enforcement action crypto July 2026 BaFin AMF CONSOB CySEC AFM unauthorised CASP named warning` → pre-deadline instruments + secondary guides only; no named post-deadline marketing-side case (day-6 silence).
2. `Bitpanda €25 BTC welcome offer extended July 2026 capture campaign` → offer still described with 07-05 window; no extension; watch item (c) resolved as lapse.
3. `Binance MiCA licence France reapply CASP jurisdiction July 2026` → France reported-only; firm names no jurisdiction; 07-06 "withdrawal chaos" = same event-chain follow-on (already captured); watch item (a) unchanged.
4. `crypto exchange CMO "head of marketing" interview conference July 2026 Coinbase Kraken OKX Bitpanda` → only previously-captured CMO-churn + non-verbatim profiles; 0 qualifying class-4.
5. `crypto company marketing team layoffs July 2026 exchange restructuring cuts` → captured items + YGG candidate (verified out: non-tracked, partner-marketing wind-down).
6. `crypto exchange EU capture campaign July 2026 Binance users bonus OKX Coinbase Kraken migrate` → surfaced Gate (net-new entrant) + re-confirmed OKX/Coinbase/Kraken/Gate.io panel + Coinbase July-13 deadline (already captured).
7. `"July 2026" crypto marketing promotion enforcement warning ESMA MiCA financial promotion misleading` → ESMA wind-down statement + secondary trackers only; no named enforcement case.
8. `Gate.io Gate Europe MiCA CASP licence authorised EU 2026 registered` → **verified Gate Technology Ltd MFSA MiCA CASP licence (2025-09-29, ESMA register)** — confirms Gate is a licensed-capture entrant before adding.
9. Fetch: cryptobriefing.com Gate deposit-rewards article (primary press source; published 2026-06-29, mechanics sparse).

## Net-new / changed this run
- `corpus/marketing-campaigns/mica-competitive-capture-2026-06.md` (**net-new 07-07 block: Gate Europe sixth capture entrant, MFSA-licence-verified, non-tracked capture-context**)
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` (idempotent `as_of=2026-07-07` re-stamp — the only deterministic file deltas today)
- `findings/longitudinal-2026-06.md` (2026-07-07 section + last-updated bump)
- `corpus/weekly-runs/2026-07-07-corpus-run.md` (this record)

## Recommendation for next run
(a) Binance named re-file jurisdiction (open; France reported-only); (b) **first named post-deadline NCA marketing-side action** — day-6 silence logged; ESMA non-compliant register remains the leading indicator; (c) **Gate/OKX/Coinbase primary firm-page T&C capture** — Gate especially, to confirm whether its headline-first/sparse-disclosure style holds on the primary page (Art. 7 exposure read); Chrome-lane, geofenced; (d) any seventh capture entrant (Ripple/CSSF still licence-only, no consumer campaign observed); (e) qualifying class-4 statements as post-deadline conference/podcast content lands (Chen interim-CMO surface worth re-checking weekly); (f) agency panel **22 days stale — escalation to Jukka carried** (upstream `trend-data.json` refresh needed before July synthesis).
