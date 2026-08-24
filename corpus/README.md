# Corpus — State of Crypto Marketing 2026

Public-source corpus organised by source class. Every file in this tree is citation-anchored — each row references a primary source any reader can independently verify.

## Source classes (six)

1. **`job-postings/`** — Senior marketing job postings, by firm, past 12 months. One CSV per firm. Columns: `date_posted, title, jurisdiction, seniority, source_url, captured_date, notes`.
2. **`agency-claims/`** — Agency case studies + press releases naming a firm. Used to build the firm-overlap matrix. One CSV per agency.
3. **`regulator-filings/`** — ESMA, MiCA delegated reg, MAS, VARA, FCA filings + public regulator-action register. Filed as PDFs/HTML extracts with citation index.
4. **`operator-statements/`** — Conference talks, podcast transcripts, public LinkedIn posts where senior operators speak on the record. One Markdown file per firm; each entry timestamped + URL'd.
5. **`layoff-tracker/`** — Public 2026 marketing-team contractions. Single CSV: `firm, date_announced, headcount_change, percentage, source_url, ai_cover_narrative_y_n, notes`.
6. **`agency-overlap-matrix.csv`** — Cross-reference: which firms each agency newly claims; updated weekly Friday cadence.

## Workflow

- Weekly corpus refresh runs Friday. Inbound nominations (per the May 6 cycle-opener essay open call) get evaluated Friday and added if they fit corpus criteria.
- Phase 1 (May–June): build to coverage. Phase 2 (July): synthesise findings. Phase 3 (August–September): ship.
- All entries must be citation-anchored — no claim enters the corpus without a primary-source URL.

## Index of currently active files

- `job-postings/` — per-firm CSVs produced daily by `scripts/daily-corpus-sync.py` from the URL-verified ATS feed (ava-labs, bitpanda, bitstamp, bybit, crypto-com, kucoin, optimism, phantom, solana, **coinbase — added 2026-07-19**). `_absence.csv` carries tracked firms with no API coverage (Aave Lever-404 + 5 proprietary: Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys) — absence is data. `_chrome-queue.csv` tracks the proprietary-ATS backlog.
- `layoff-tracker/2026-layoff-tracker.csv` — seeded with Crypto.com (Mar -12%), Gemini (-30% YTD), Algorand (-25%), Coinbase (May 5 -14%), Block (-4,000), MARA (-40); + Robinhood (Jun 16 -10%), BitGo (Jun 26 -15%), **Polygon Labs (Jul 16, figures undisclosed — added 2026-07-20; in-cohort Stratum 2, first row whose stated rationale is repositioning/M&A rather than AI)**. 9 rows.
- `operator-statements/sport-sponsorship-reset-2026-05.md` — multi-incident sport-sponsorship reset cluster (captured 2026-05-14)
- `regulator-filings/fca-premier-league-sponsorship-warning-2026-06.md` — FCA→football-club crypto-sponsorship warning (2026-06-02/03)
- `regulator-filings/esma-mica-transitional-period-end-2026-06.md` — ESMA Public Statement (23 June 2026, ESMA75-113276571-1710): unauthorised CASPs must "cease marketing activities and solicitation" as the MiCA transitional period ends 1 July 2026
- `weekly-runs/` — dated daily corpus-assembly run records (six-class audit trail + absence-as-data). Latest: `2026-08-24-corpus-run.md`

### Column-integrity notes on `layoff-tracker/2026-layoff-tracker.csv` (added 2026-08-24)

- The tracker carries **8 fields**, including **`ai_cover_grade`** (added 2026-08-24). Every `Y` row in `ai_cover_narrative_y_n` is graded **A** (firm-stated, verbatim captured) · **B** (firm-stated, relayed by an outlet) · **C** (outlet characterisation, no firm quote) · **D** (anonymously sourced) · **E** (inferred — the firm said "automation", not "AI").
- 🔴 **The ungraded AI-cover proportion must not be printed.** 9 of 26 rows are `Y` (35%); only **4 of 26 (15%)** are Grade A. Full audit + the permitted and prohibited sentences: `layoff-tracker/_ai-cover-narrative-grading-audit-2026-08-24.md`.
- 🔴 **Figures in this tracker are not safe until their citation has been opened.** Six rows have been opened across four runs and **all six carried a defect**: Algorand (uncited), Crypto.com (`180` = the outlet's arithmetic), Luno (`−20%` = Bloomberg's, not the firm's), BitGo (unstable aggregator citation supplying a wrong date), **Gemini (`−30% YTD` STRUCK — never firm-stated and irreconcilable with the firm's own SEC-filed base; `200 jobs` refused)**. `headcount_change` and `percentage` still lack a grading ladder.
- 🔴 **`README.md` / `README-for-github.md` advertise three layoff examples — Crypto.com, Gemini, Algorand — and all three have now failed inspection.** Correct before ship.

### Class-3 reading rules (added 2026-08-24)

- 🔴 **Do not read `ae_infrigment` as a statement about a listed entity.** ESMA defines it as *"Case of infringement identified by ESMA in accordance with Article 17 of Regulation (EU) No 1095/2010"* — the breach-of-Union-law procedure **against a national competent authority**. `ae_reason` ("Non compliancy reason", free text) *is* entity-level and is populated for **1 of 167** rows. Record: `regulator-filings/esma-register-field-semantics-ae-infrigment-resolved-2026-08-24.md`.
- ⚠ **`CASPS.csv` has truncated on two separate fetch attempts** (2026-08-17 and 2026-08-24, both at 82,445 characters, both cut mid-field). **No absence claim about a named firm may be made from either.** The last COMPLETE capture is `regulator-filings/_esma-casps-snapshot-2026-08-17.csv` (329 rows, md5 `69e7dc…`).
