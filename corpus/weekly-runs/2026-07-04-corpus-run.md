# Corpus-assembly daily run — 2026-07-04 (day 3 post-deadline)

**Run type:** Phase-1 daily corpus assembly (automated).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Dedup baseline read before searching:** prior runs 2026-07-03 back to 2026-06-20; `regulator-filings/` (all 4 files, incl. the full Binance event-chain file); `marketing-campaigns/mica-competitive-capture-2026-06.md`; `operator-statements/`; `layoff-tracker/2026-layoff-tracker.csv` (8 rows); `agency-overlap-matrix.csv`; `job-postings/*.csv`; `findings/longitudinal-2026-06.md`.

---

## Headline result

**Net totals: 0 job-posting rows, 0 agency-matrix rows, 0 net-new class-3 enforcement entries, 0 qualifying operator statements, 0 layoffs. A genuinely quiet day — and on day 3 post-deadline, the quiet is the finding:**

1. **Day-3 regulator silence holds (class 3 absence-as-data).** Three full days after the MiCA transitional period ended, still **no named marketing-side NCA enforcement case** (BaFin/AMF/CONSOB/AFM/CySEC/ESMA) has surfaced in public search. The one public enforcement instrument in motion remains the ESMA interim-register non-compliant list (157 NCA-flagged entities, logged 07-03). The ESMA "orderly wind-down" statement and AMF hard-cutoff reminder that today's searches re-surfaced are the already-captured pre-deadline documents — nothing new is on the record.
2. **Binance watch item (a) — named re-file jurisdiction — stays open, unchanged.** Today's sweep re-surfaced only the already-logged material: France as *reported* target (FT-sourced press; Binance's own statement — "confident we will secure a MiCA licence in the coming months" — still names no jurisdiction). The crypto.news explainer that today's search surfaced is dated **2026-06-27** (pre-deadline, in-corpus event chain) — not net-new. No over-claim; France remains reported-only.
3. **Capture-panel status quo; the Bitpanda expiry check comes due tomorrow.** No sixth capture entrant and no extension/performance signal surfaced today. Bitpanda's €25+3% offer is capped at **2026-07-05 / first 500 users** — whether it extends (campaign-performance signal, watch item e) is checkable from tomorrow's run.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)
**Net-new: 0.** Source A scan_date **2026-07-03** (feed not yet re-stamped for 07-04 at run time; sync is idempotent either way); no new URL-verified rows — Phantom Head of Brand Creative (07-02) stands as the latest. Chrome work-queue unchanged (Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana). Absence re-stamped `as_of=2026-07-04`: Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys — absence-as-data note stands.

### 2. Agency claims / overlap matrix (deterministic)
**Net-new: 0.** Source B `trend-data.json` lastUpdated **2026-06-15** — **20th day unchanged.** The 07-03 escalation to Jukka stands (upstream NorthPoint feed needs a refresh before July synthesis; not fixable from this loop). Matrix holds 8 tracked firms / 1 OVERLAP (Sui — Coinbound + RZLT). 18 per-agency snapshots idempotent.

### 3. Regulator (ESMA/BaFin/AMF/CONSOB/AFM/CySEC/FCA/MAS/VARA)
**Net-new named enforcement entries: 0.** Day-3 post-deadline: coordinated-action, blacklist, and NCA-warning searches returned only pre-deadline captured documents (ESMA 23-Jun wind-down statement, AMF 1-Jul reminder, April ESMA supervisory statement) and secondary guides/CASP-list trackers. **Absence-as-data: the post-deadline enforcement silence is now three days long** — a datapoint for Theme 4's enforcement-timing read (register-listing-as-sanction is running ahead of named actions).

### 4. Operator statements (senior marketing operators at tracked firms)
**Net-new qualifying: 0.** Targeted sweeps (exchange CMO/Head-of-Marketing statements; Bitpanda/Kraken/Bitvavo marketing-exec quotes on the capture campaigns; Eowyn Chen interim-CMO activity) surfaced only already-captured material: Conlan departure (05-12), Kalifowitz departure (05-05), Chen interim appointment (05-12). No verbatim in-window statement by a qualifying marketing operator at a tracked firm.

### 5. Layoff tracker (2026 marketing-team contractions)
**Net-new rows: 0.** July-window searches re-surfaced only captured items (Crypto.com −12% citing AI, Coinbase −700 incl. marketing, Gemini, Algorand). Tracker holds at 8 rows.

### 6. Longitudinal shift for synthesis
Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-04 section; last-updated bumped): day-3 enforcement silence as the leading Theme-4 timing datum; agency panel 20 days stale; watch items carried without change — the first fully-zero net-new day since the deadline, itself a marker that the deadline-week news pulse has passed and the corpus's next accretion likely comes from (i) the first named NCA action, (ii) the Bitpanda extension check, or (iii) post-deadline conference/podcast content landing.

---

## Searches/fetches run (audit trail)
1. `MiCA enforcement action crypto marketing July 2026 BaFin AMF CONSOB CySEC warning unauthorised CASP` → pre-deadline material + secondary guides only; no named post-deadline case.
2. `crypto exchange CMO "chief marketing officer" OR "head of marketing" interview statement July 2026` → Conlan/Kalifowitz/Chen items, all previously captured; 0 net-new qualifying.
3. `crypto company marketing team layoffs July 2026` → all previously captured (March-cycle items); 0 net-new.
4. `"July 2026" MiCA first enforcement blacklist unauthorised crypto exchange national regulator named` → no named case; absence logged.
5. `Binance EU return re-apply license France Ireland July 2026 statement` → France still reported-only; firm statement names no jurisdiction; watch item (a) unchanged.
6. `Bitpanda Bitvavo Kraken welcome bonus campaign Binance users July 2026 extended` → all five capture campaigns previously captured; no extension signal yet (Bitpanda cap 07-05 — check tomorrow).
7. `Bitpanda OR Kraken OR Bitvavo "chief marketing" OR CMO … quote statement MiCA … campaign` → no attributed marketing-exec quote; 0 qualifying.
8. `ESMA OR AMF OR BaFin OR AFM OR CONSOB statement press release July 2/3 2026 … non-compliant warning list` → only captured pre-deadline documents.
9. Fetch (full): crypto.news Binance-lockout explainer → **published 2026-06-27**, pre-deadline; confirms nothing net-new on re-file jurisdiction; not added.

## Net-new / changed this run
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` (idempotent `as_of=2026-07-04` re-stamp — the only file deltas today)
- `findings/longitudinal-2026-06.md` (2026-07-04 section + last-updated bump)
- `corpus/weekly-runs/2026-07-04-corpus-run.md` (this record)

## Recommendation for next run
(a) Binance named re-file jurisdiction (open; France reported-only); (b) **first named post-deadline NCA action** — day-3 silence logged; the 157-entity non-compliant register remains the leading indicator; (c) direct **ESMA CSV pull** at synthesis time to double-anchor 243/157 (mirror caveat carried); (d) OKX + Coinbase primary firm-page/T&C capture (geofenced — Chrome lane); (e) **Bitpanda extension check comes due 07-05** (cap expiry) + any sixth capture entrant; (f) agency panel **20 days stale — escalation to Jukka carried** (upstream `trend-data.json` refresh needed before July synthesis); (g) qualifying class-4 statements as post-deadline conference/podcast content lands (Chen interim-CMO surface worth re-checking weekly).
