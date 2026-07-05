# Corpus-assembly daily run — 2026-07-05 (day 4 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-04 back to 2026-06-20; `regulator-filings/` (all 4 files, incl. the full Binance EU-exit event-chain file); `marketing-campaigns/mica-competitive-capture-2026-06.md`; `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**Net totals: 0 job-posting rows, 0 agency-matrix rows, 0 net-new class-3 enforcement entries, 0 qualifying operator statements, 0 layoffs. Second consecutive fully-zero net-new day — day 4 post-deadline, the silence is the finding:**

1. **Day-4 regulator silence holds (class 3 absence-as-data).** Four days after the MiCA transitional period ended, still **no named marketing-side NCA enforcement case** (BaFin/AMF/CONSOB/AFM/CySEC/ESMA) on the public record. Today's sweep re-surfaced only the already-captured pre-deadline instruments (AMF 1-Jul transitional-end reminder, ESMA wind-down statement) plus secondary CASP-list trackers. The enforcement mechanism in motion remains **register-listing (the ESMA non-compliant list), not named actions** — the register-first, cases-later read continues to strengthen for Theme 4's enforcement-timing section.
2. **Bitpanda €25-BTC welcome offer cap comes due TODAY (07-05) — no extension signal, and a cap discrepancy surfaced (watch item e, partially resolved-as-absence).** The tracked €25-BTC + 3%-cashback capture offer was capped at "first 500 users / 07-05." Today's sweep surfaced **no primary confirmation of an extension**; secondary coverage now cites **conflicting caps (500 vs "first 1,000")**, so the exact cap is a secondary-source ambiguity, not a primary fact — logged as such, not added as a finding. The honest read: the offer's stated window closes today with no public extension; whether Bitpanda re-ups is checkable from tomorrow's run (campaign-performance signal). No over-claim.
3. **Non-capture Bitpanda campaign reviewed and EXCLUDED (dedup/scope discipline).** Search surfaced a Bitpanda **savings-plan raffle** (€100/mo to 3 winners for automating stock/ETF/ETC savings plans, min €25). Primary window **2026-05-27 → 2026-06-08** — out of the current capture window, ended, and **not a MiCA-capture / crypto-acquisition campaign** (equities/ETF DCA raffle). Not added to `marketing-campaigns/`; noted here as reviewed-and-excluded so a future run doesn't re-surface it as net-new.
4. **Binance re-file jurisdiction (watch item a) — unchanged.** Today's sweep re-confirmed only the already-logged posture: Binance "remains committed to Europe" and plans to reapply "in the coming months," with **France reported as the likely next jurisdiction** (press-sourced); Binance's own statement still **names no jurisdiction formally**. No net-new; France stays reported-only.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0.** Source A scan_date **2026-07-03** (feed not re-stamped for 07-05 at run time; sync is idempotent either way); no new URL-verified rows — Phantom Head of Brand Creative (07-02) stands as the latest class-1 row. Chrome work-queue unchanged (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana). Absence re-stamped `as_of=2026-07-05`: Aave (Lever API 404), Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys — absence-as-data note stands.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` lastUpdated **2026-06-15** — **21st day unchanged.** The 07-03 escalation to Jukka stands (upstream NorthPoint `trend-data.json` needs a refresh before July synthesis; not fixable from this loop). Matrix holds 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots idempotent.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-4 post-deadline: coordinated-action, blacklist, and NCA-warning searches returned only pre-deadline captured documents (AMF 1-Jul reminder, ESMA wind-down statement, April supervisory statement) and secondary CASP-list/guide trackers. **Absence-as-data: the post-deadline named-enforcement silence is now four days long** — register-listing running ahead of named marketing-side actions.

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** Targeted sweeps (exchange CMO / Head-of-Marketing statements at Coinbase/Kraken/Bitpanda; post-deadline conference/podcast content) surfaced only non-qualifying material: conference appearances by non-marketing executives (Coinbase Chief Policy Officer, Kraken CEO, Bitpanda CEO at Paris Blockchain Week Apr 15–16) and the already-noted OpenAI-poaches-Coinbase-marketing-team thread (04-23, previously in view). No verbatim in-window statement by a qualifying marketing operator (CMO/VP Marketing/Head of Brand/Growth) at a tracked firm.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced captured items (Crypto.com −12% AI-cover, Coinbase −700, Gemini, Algorand, Robinhood/BitGo perimeter). **MANTRA Chain** surfaced as a candidate ("marketing among largest-reduced functions") but **verified OUT: announced 2026-01-14 (6 months stale, out of window), non-tracked firm, OM-collapse-driven** — excluded per window + cohort rules. Tracker holds at 8 rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-05 section; last-updated bumped): the second consecutive fully-zero net-new day confirms the deadline-week news pulse has fully passed; the corpus's next accretion most likely comes from (i) the first named NCA marketing-side action, (ii) the Bitpanda 07-05 cap outcome (extend vs close), or (iii) post-deadline conference/podcast content landing a qualifying class-4 quote.

---

## Searches/fetches run (audit trail)
1. `MiCA enforcement action crypto marketing July 2026 BaFin AMF CONSOB CySEC AFM unauthorised CASP named warning` → pre-deadline instruments + secondary guides only; no named post-deadline case.
2. `Bitpanda welcome bonus €25 campaign extended July 2026 Binance users` → offer window 07-05 confirmed; no extension; secondary cap discrepancy (500 vs 1,000) noted, not primary.
3. `Bitpanda savings plan promotion monthly cash prizes 2026` → equities/ETF DCA raffle, window 05-27→06-08, out-of-scope; excluded.
4. `Binance MiCA licence France re-apply jurisdiction July 2026 statement` → France reported-only; firm names no jurisdiction; watch item (a) unchanged.
5. `crypto exchange CMO "head of marketing" interview conference July 2026 Coinbase Kraken Bitpanda` → non-marketing-exec conference appearances only; 0 qualifying class-4.
6. `crypto company marketing team layoffs July 2026 exchange restructuring` → captured items + MANTRA candidate (verified out-of-window).
7. `MANTRA Chain layoffs 2026 marketing restructuring date announcement` → confirmed 2026-01-14 announcement; excluded (window + non-tracked cohort).

## Net-new / changed this run
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` (idempotent `as_of=2026-07-05` re-stamp — the only deterministic file deltas today)
- `findings/longitudinal-2026-06.md` (2026-07-05 section + last-updated bump)
- `corpus/weekly-runs/2026-07-05-corpus-run.md` (this record)

## Recommendation for next run
(a) Binance named re-file jurisdiction (open; France reported-only); (b) **first named post-deadline NCA action** — day-4 silence logged; the ESMA non-compliant register remains the leading indicator; (c) **Bitpanda 07-05 cap outcome** — check whether the €25-BTC offer extended (campaign-performance signal) or closed; resolve the 500-vs-1,000 cap against the primary T&C page; (d) OKX + Coinbase primary firm-page/T&C capture (geofenced — Chrome lane); (e) any sixth capture entrant; (f) agency panel **21 days stale — escalation to Jukka carried** (upstream `trend-data.json` refresh needed before July synthesis); (g) qualifying class-4 statements as post-deadline conference/podcast content lands (Chen interim-CMO surface worth re-checking weekly).
