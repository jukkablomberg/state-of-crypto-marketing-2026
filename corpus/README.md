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
- `weekly-runs/` — dated daily corpus-assembly run records (six-class audit trail + absence-as-data). Latest: `2026-08-25-corpus-run.md`

### 🔴 Class-1 reading rules (added 2026-08-25)

- 🔴 **`_absence.csv` has never contained an absence.** Every row it has ever held carries `reason = api-fetch-error` or `proprietary-ATS/needs-chrome` — a statement about **NorthPoint's ATS reach**, never about the firm's publishing behaviour. Proved on 2026-08-25 when an upstream slug fix moved MetaMask/ConsenSys out of the panel and surfaced a **2026-08-06** Product Marketing Lead posting that had been public for nineteen days. **The report may not print "shows no public marketing-hiring signal" for Aave, Binance, Bybit, HTX or KuCoin.** The supportable sentence is *"not reachable through the ATS APIs this corpus scans."* Record: `job-postings/_coverage-expansion-and-first-absence-panel-exit-2026-08-25.md`.
- ⚠ **The panel is biased by construction.** Four of its five remaining rows are Tier-1 exchanges running proprietary recruiting SPAs — it is a sample of firms that own their hiring stack, not a sample of silence.
- 🔴 **The `total_jobs_fetched` fingerprint series is discontinuous at 2026-08-24 → 2026-08-25** (2,263 → 3,334). The jump is a **coverage expansion** — `companies_via_api` moved 89 → 99 — not market movement. The feed-health guard tests liveness, not comparability. **No longitudinal reading may cross that boundary.**

### Column-integrity notes on `layoff-tracker/2026-layoff-tracker.csv` (updated 2026-08-25)

- The tracker carries **10 fields**. **`headcount_grade`** and **`percentage_grade`** (added 2026-08-25) apply the same five-step ladder as `ai_cover_grade`: **A** firm-stated verbatim in hand · **B** firm-stated relayed · **C** outlet figure, no firm quote · **D** anonymously sourced · **E** inferred/derived · plus `n/a` and `UNCITED`.
- 🔴 **No aggregate headcount sentence may be printed.** Fourteen rows carry a headcount figure and **exactly one is Grade A** (Gnosis — and it is scoped to two teams at a perimeter firm, not company-wide).
- 🟢 **Permitted:** *of the sixteen rows carrying a percentage, four are firm-stated with a verbatim quote — and half of those are SEC filings.*
- 🔴 **The adjudicable denominator is 25, not 26.** Row 6 (MARA) was never labelled `Y` or `N`; the 08-24 audit silently coerced the blank to `N`. Grade-A AI-cover share is **4/25 = 16%**. The row is also uncited and remains flagged to STRIKE at ship.
- 🟢 **The symmetric sweep is done and the `N` side is clean** — 16 of 16 labelled rows correct, each with an explicit non-AI rationale captured from its source. The 35% → 15% collapse of 08-24 stands. ⚠ The `Y`-side token predicate does **not** transfer to the `N` rows (94% false positives — it reads our own adjudication prose, not the source). Record: `layoff-tracker/_symmetric-n-sweep-and-figure-column-grading-2026-08-25.md`.

### Column-integrity notes on `layoff-tracker/2026-layoff-tracker.csv` (added 2026-08-24)

- The tracker carries **8 fields**, including **`ai_cover_grade`** (added 2026-08-24). Every `Y` row in `ai_cover_narrative_y_n` is graded **A** (firm-stated, verbatim captured) · **B** (firm-stated, relayed by an outlet) · **C** (outlet characterisation, no firm quote) · **D** (anonymously sourced) · **E** (inferred — the firm said "automation", not "AI").
- 🔴 **The ungraded AI-cover proportion must not be printed.** 9 of 26 rows are `Y` (35%); only **4 of 26 (15%)** are Grade A. Full audit + the permitted and prohibited sentences: `layoff-tracker/_ai-cover-narrative-grading-audit-2026-08-24.md`.
- 🔴 **Figures in this tracker are not safe until their citation has been opened.** Six rows have been opened across four runs and **all six carried a defect**: Algorand (uncited), Crypto.com (`180` = the outlet's arithmetic), Luno (`−20%` = Bloomberg's, not the firm's), BitGo (unstable aggregator citation supplying a wrong date), **Gemini (`−30% YTD` STRUCK — never firm-stated and irreconcilable with the firm's own SEC-filed base; `200 jobs` refused)**. `headcount_change` and `percentage` still lack a grading ladder.
- 🔴 **`README.md` / `README-for-github.md` advertise three layoff examples — Crypto.com, Gemini, Algorand — and all three have now failed inspection.** Correct before ship.

### Class-3 reading rules (added 2026-08-24)

- 🔴 **Do not read `ae_infrigment` as a statement about a listed entity.** ESMA defines it as *"Case of infringement identified by ESMA in accordance with Article 17 of Regulation (EU) No 1095/2010"* — the breach-of-Union-law procedure **against a national competent authority**. `ae_reason` ("Non compliancy reason", free text) *is* entity-level and is populated for **1 of 167** rows. Record: `regulator-filings/esma-register-field-semantics-ae-infrigment-resolved-2026-08-24.md`.
- ⚠ **`CASPS.csv` truncated on two `web_fetch` attempts** (2026-08-17 and 2026-08-24, both at 82,445 characters, both cut mid-field). **🟢 RESOLVED 2026-08-25 BY CHANGING CHANNEL:** a browser-context `fetch()` returned the complete file — **163,026 chars, 335 rows, all 16 fields, final row terminating.** One URL, two channels, consecutive days: **the cut point is a property of the retrieval channel, confirmed by construction. Structure, not size.** **Do not re-fetch this file via `web_fetch`.**
  - SHA-256 of raw bytes: `196090fa6fa15162fee56084dd0d0e53c158bb7347991538ce683b0b256d6b3e` (163,370 bytes). **No snapshot file exists for 08-25** — base64 transfer was blocked by the channel, and a text transfer was ruled out on evidence (raw 163,370 vs UTF-8 re-encoded 163,367 bytes: the file is not valid UTF-8, so a text round-trip would have produced an artifact three bytes different from the register). **A lossy re-encode is a fabrication too, even automated.** Last stored artifact remains `_esma-casps-snapshot-2026-08-17.csv` (329 rows, md5 `69e7dc…`).
- 🟢 **Class-3 absence claims are PERMITTED from the 08-25 capture.** Of the eleven Tier-1 tracked exchanges, **nine hold an authorised-CASP entry; Binance and HTX hold none** (zero occurrences in any field of any of the 335 rows). Binance's absence has a published explanation (`binance-mica-eu-exit-2026-06.md`); **HTX's has none.**
- 🔴 **An absence from `CASPS.csv` is evidence only for an entity that provides crypto-asset services to EU clients.** Fourteen of the sixteen "absent" tracked firms are a **category error**: L1/L2 foundations are not service providers, non-custodial wallets sit outside the CASP perimeter, and Tether is an issuer governed by MiCA Titles III–IV. **Do not print them as absences.** Record: `regulator-filings/esma-casps-register-complete-capture-alternate-channel-2026-08-25.md`.
- ⚠ **Internal inconsistency to resolve before ship:** `tracked-firms.md` titles Stratum 4 *"CASP-licensed EU firms (non-exchange)"* and lists **Securitize**, which returns zero hits in the register. Relai, in the same stratum, *is* present. **Do not print Stratum 4 as "CASP-licensed" until resolved.**
