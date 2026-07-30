# Corpus-assembly daily run — 2026-07-30 **(day 29 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-07-30 ~16:10 CEST.
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Mandate for this run, taken from the 07-29 recommendations:** (1) **work the class-3 backlog FIRST** — CNMV direct read and the AFM finfluencer study, both carried unworked for two runs; (2) close or advance **watch (t)**, the class-1 coverage defect.
**Dedup baseline read before writing:** `2026-07-29-corpus-run.md` in full; `findings/longitudinal-2026-06.md` tail; `layoff-tracker/2026-layoff-tracker.csv` (13 rows pre-run); `regulator-filings/` (8 files); `operator-statements/` (3 files); `marketing-campaigns/` (4 files); `job-postings/` listing + `_absence.csv` + `_chrome-queue.csv` + `_absence-cohort-audit.csv`. Repo-wide greps for `luno`, `gnosis`, `uphold`, `hörhager`, `horhager`, `beier`, `lanigan`, `cryptojobslist`, `cnmv`, `miolo`, `finfluencer`, `afm`, `gemini`, `predictions` run before any file was written.

---

## Headline result

**The mandate was to close watch (t). Watch (t) turned out to be wrong — and the true defect underneath it is worse, more specific, and fixable.**

**1. Yesterday's "12 tracked firms are missing from the upstream company list" is FALSIFIED. The real gap is 4.** Direct read of `prospects/scanner/config.json` (147 companies) shows **8 of the 12** firms recorded yesterday as "invisible in both directions" are in the scanner config, with correct ATS types and slugs, scanned daily without error. Including **Ledger**, which yesterday's audit called *"the worst case in this audit… the firm is simply not in the upstream company list."* It is in the list, on the correct Ashby slug.

**2. Gemini falsified it by producing a posting.** A firm recorded yesterday as SILENT returned a **net-new, URL-verified greenhouse posting today**. The feed could see it the whole time. There was nothing to report until there was.

**3. The real defect: class 1 is a FLOW register presented as a STOCK register.** `daily-corpus-sync.py` writes only roles **open at the moment of a run**, and it did not exist until **2026-06-26**. The upstream scanner's own memory (`state/last-scan.json` → `jobs_seen`) holds **5 qualifying marketing roles at 3 tracked firms, all inside the report's rolling 12-month window, none of which are in the corpus** — Trust Wallet (2026-04-29, 2026-06-23), Arbitrum Foundation (2026-05-08), Offchain Labs (2026-05-12, 2026-06-10). They opened and closed before the corpus could see them. **They are recoverable: `jobs_seen` holds the ATS job IDs and first-seen dates.**

**4. A third failure mode nobody had a name for: in the feed, unreachable, and silent about it.** **Sui Foundation**'s Ashby slug in the config is **`sui%20foundation`** — a URL-encoded space. It produces no rows *and no fetch error*. Contrast Chainlink Labs, whose bad Ashby slug 404s loudly. Sui is also the **only OVERLAP row in the entire agency matrix**.

**5. Class 5 broke a standing finding.** Until today the tracker's standing finding read: *"across all 13 rows, not one names marketing as the affected function."* **Gnosis's own X account named marketing** among the functions affected by its July restructuring. Gnosis is **perimeter, not cohort** — so the tracker-scoped finding breaks and the **cohort-scoped one holds**. Phase 2 must say which it means.

**6. The class-3 backlog is cleared. Both carried targets worked, both resolve as nulls with structure.** CNMV direct read **executed**; AFM finfluencer study **closed as out-of-window (2021)**.

**Day-29 named marketing-side enforcement silence HOLDS.**

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 1.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-07-30
source A (jobs)   scan_date: 2026-07-30
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 1  firms: ['Gemini']
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**Feed-health guard: HEALTHY.** `scan_metadata` — `scanned_at_utc 2026-07-29T22:46:21Z`, `scan_date 2026-07-30`, 147 companies scanned (87 API, 60 pending Chrome), **2,102 jobs fetched**, 29 after filter, **`new_count` 1**, **`url_verification_dropped` 0**, `still_open_count` 28. Six fetch-errors, **only Aave tracked** (Lever 404, unchanged for weeks); the other five (Wormhole, Injective, Bitwise, Chainlink Labs, Elliptic) are non-cohort. Drops: 1,593 excluded function · 354 no marketing keyword · 87 no seniority signal · 23 excluded seniority · 12 tracker · 4 excluded location.

#### The net-new posting → `../job-postings/gemini.csv` (NEW FILE)

| field | value |
|---|---|
| firm | **Gemini** (Stratum 1, tracked) |
| title | **Predictions Partnerships Marketing Lead** |
| date_posted | **2026-07-29** |
| jurisdiction | New York, New York |
| seniority | Lead / marketing |
| source_url | `https://boards.greenhouse.io/embed/job_app?for=gemini&token=8091954&gh_jid=8091954` |
| ATS | greenhouse, `url_verified=True` |

**This is the first class-1 capture at Gemini in the corpus's history, and it is cross-class load-bearing.** Gemini **exited the UK, EU and Australia on 2026-02-05** alongside a 25% workforce reduction, redirecting resources to the US business and to **Gemini Predictions** (`layoff-tracker/2026-layoff-tracker.csv`). The first marketing seat this corpus has ever observed at Gemini is a **Predictions** seat, **in New York**. Sequence, not causation — but it is a clean one, and both legs are already in this corpus.

#### **Watch (t) as filed is FALSIFIED. Here is what is actually true.**

Yesterday's audit concluded that 12 of 27 tracked slugs were "invisible in both directions" and diagnosed the cause as *"the firm is simply not in the upstream company list."* **That diagnosis was tested this run against the config itself and does not survive.**

Method: direct read of **`prospects/scanner/config.json`** (the scanner's own `companies` dict, 147 entries), **`prospects/scanner/state/last-scan.json`** (`jobs_seen`, 116 entries / 41 distinct `ats:slug`), and `prospects/prospects-list.txt`.

**8 of the 12 are in the scanner config, correctly configured:**

| firm | ats | slug | in config? |
|---|---|---|---|
| Gemini | greenhouse | `gemini` | **yes** — produced a posting today |
| Ledger | ashby | `ledger` | **yes** — yesterday's "worst case" |
| Aptos Labs | greenhouse | `aptoslabs` | yes |
| Arbitrum Foundation | lever | `arbitrumfoundation` | yes |
| Polygon Labs | ashby | `polygon-labs` | yes |
| Trust Wallet | ashby | `trust-wallet` | yes |
| Tether | recruitee | `tether` | yes |
| Sui Foundation | ashby | `sui%20foundation` | yes, **malformed** |

**Only 4 are genuinely absent from the feed: OKX, Securitize, Rabby, Relai.** That is the real company-list gap, and it is a quarter the size of yesterday's claim. **OKX (Tier-1) and Securitize (Stratum-4, standard greenhouse board already on the prospects list) are one-line fixes.**

**The 12 therefore decompose into four distinct defects, which yesterday's audit collapsed into one:**

| defect | n | firms | what it means |
|---|---|---|---|
| **NOT-IN-FEED** | 4 | okx, securitize, rabby, relai | genuine company-list gap — the only part of watch (t) that survives |
| **FLOW-LOSS** | 2 | arbitrum, trust-wallet | in feed, **produced qualifying roles in window**, corpus never captured them |
| **BROKEN-SLUG** | 1 | sui | in feed, unreachable, **fails silently** |
| **TRUE ABSENCE** | 4 | aptos, ledger, polygon, tether | in feed, scanned clean, **genuinely no qualifying marketing roles** — absence as data in the intended sense |

Written to **`../job-postings/_absence-cohort-audit.csv`**, fully rewritten this run (27 rows, one per tracked slug, now carrying an `upstream_feed_status` column recording what the scanner config actually says).

#### **The flow-vs-stock defect is the one that should worry Phase 2**

`methodology.md` §1 promises a **"rolling 12 months ending August 31, 2026"** capture window for class 1. **The corpus cannot deliver that and has not been delivering it.** `daily-corpus-sync.py` writes a row only when a qualifying role is *open at run time*; it was created **2026-06-26**. Everything that opened and closed before that date — or between two runs since — left no trace.

Demonstrated, not asserted. From `jobs_seen`:

| firm | slug | qualifying roles seen | dates | in corpus? |
|---|---|---|---|---|
| Trust Wallet | `ashby:trust-wallet` | 2 | 2026-04-29, **2026-06-23** | **no** |
| Arbitrum Foundation | `lever:arbitrumfoundation` | 1 | 2026-05-08 | **no** |
| Offchain Labs (→ arbitrum) | `lever:offchainlabs` | 2 | 2026-05-12, **2026-06-10** | **no** |
| Gemini | `greenhouse:gemini` | 1 | 2026-07-30 | **yes, today** |

Both Arbitrum slugs are in the sync script's `TRACKED` alias table (`"arbitrum foundation"`, `"offchain labs"`), so **this is not an alias miss.** The Trust Wallet role dated **2026-06-23** was open **three days before the sync script existed** and still did not survive to the first run.

**Consequence, stated plainly: `corpus/job-postings/` is an inventory of roles that happened to be open on a day the corpus ran, not a 12-month hiring record.** No Theme-1 claim about hiring volume, hiring velocity, or "this firm did not hire" is safe for any period before 2026-06-26. → watch **(t′)**, which replaces (t).

**The fix is cheap and it is a backfill, not an engineering project:** `jobs_seen` retains the ATS job IDs and first-seen dates. A one-off reconciliation pass can recover the pre-epoch roles for every tracked slug.

**Caveat recorded honestly:** `jobs_seen` stores IDs and dates, **not titles or URLs**. It proves a qualifying role existed and when it was first seen; it does not itself supply the schema fields (`title`, `jurisdiction`, `seniority`, `source_url`) the corpus CSVs require. Backfill will need the ATS APIs re-queried per ID, and **closed roles may 404**. Recoverability is therefore **probable, not certain** — `[VERIFY]` on the first attempt before promising the window.

### 2. Agency claims / overlap matrix (deterministic)

**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 45th day unchanged.** Matrix idempotent at 8 tracked firms / 1 OVERLAP. 18 per-agency snapshots rewritten identically. **NOT re-escalated** — stable-by-decision per the 07-10 Path-2 ruling.

**But the matrix's single OVERLAP row took a structural hit this run, from an unexpected direction.** `Sui (coinbound, rzlt)` is the anchor of the report's three-agencies-on-one-firm framing. As of today, Sui is **also** the corpus's only BROKEN-SLUG firm in class 1 — the one tracked firm the job-postings feed is configured to read and silently cannot. So the report's richest agency row sits on a firm whose hiring signal is structurally invisible, **and** (watch q, 07-29) whose actual brand system was built by an agency the panel cannot see. **Three independent instruments, one firm, all three degraded.** Sui should be the first firm Phase 2 audits end-to-end.

### 3. Regulator — **0 net-new. Day-29 silence HOLDS. Backlog CLEARED.**

Both carried targets worked. Both resolve as nulls, and both nulls have structure worth keeping.

#### (a) CNMV direct read — **EXECUTED** (carried three runs) → `../regulator-filings/cnmv-sanctions-register-read-2026-07.md` (NEW FILE)

Fetched and read the **Registro público de sanciones impuestas por la CNMV** landing page. **No in-window Spanish marketing-side enforcement case found.** Two structural facts recorded so no future run re-derives them:

1. **The register is lagging by construction.** It publishes *imposed* sanctions under Art. 334 / 244.1 Ley 6/2023. An *opened* file (`expediente sancionador incoado`) is a separate, earlier event that does not appear until resolved. → **the corpus's silence finding must read "no publicly registered sanction", never "no enforcement activity."**
2. **Anonymisation is permitted** — *"pudiendo, en su caso, mantener el anonimato de la persona sancionada."* So the register cannot support any claim about *which* firms have or have not been sanctioned. Records retained five years.

**Precedent note that sharpens Chapter 1 — and would otherwise have been an error.** Spain opened its **first crypto-advertising sanctioning file on 31 October 2023** (Miolo Desarrollos, two campaigns, "serious" infringements) under **CNMV Circular 1/2022** — a *national* advertising regime, **not MiCA**. **2023 → out of window, NOT entered as a corpus record, recorded as a framing caveat only.** The report's null must therefore be scoped: **zero *MiCA-era* marketing-communications enforcement**, not "zero crypto-advertising enforcement." A Spanish reader would catch the unqualified version.

**New standing target opened:** the CNMV publishes **`Advertencias de entidades no registradas`** separately from the sanctions register — a faster-moving instrument. Given that unauthorised-CASP wind-down carries an explicit duty to *"cease marketing activities and solicitation"*, **NCA warning lists are a plausible place for the first marketing-adjacent public action to surface, and this corpus has never swept them in any jurisdiction.** → watch **(v)**.

#### (b) AFM finfluencer study — **CLOSED, out of window** (carried three runs)

The target existed. It is *"The pitfalls of 'finfluencing' / De valkuilen bij 'finfluencen'"*, **2021** → excluded under the pre-December-2024 rule. **Not entered. Closed, not carried a fourth time.** Recorded in `../regulator-filings/afm-casp-advertising-cost-information-review-2026-04.md`.

**Two notes preserved, because the easy version of this would have been wrong:**

- The AFM's finfluencer work found **investment firms paying finfluencers per acquired customer**, breaching the Dutch commission ban — an **inducement/distribution** finding. BaFin's is a **disclosure** finding. **Two NCAs on the same channel are not making the same argument** and must not be merged.
- The AFM's consumer finfluencer material states **crypto falls largely outside financial supervision** — a *pre-MiCAR perimeter* statement. **Do not cite the 2021 study as evidence of the AFM's post-MiCAR posture.**

**Consequence:** the corpus has **one** NCA (BaFin) on the finfluencer channel in window, not two. **Any Phase-2 sentence implying multi-regulator finfluencer consensus is currently unsupported.**

#### (c) AFM April-2026 review — re-verified, one gap closed

Re-fetched; content identical to the 07-27 capture (33 CASPs examined; 14 with significant advertising shortcomings; 19 with cost-information shortcomings; van Beusekom's *"The period of leniency has ended"*). **Dedup held — not re-entered.** One improvement: today's search surfaced the **Dutch-language original** at a **different path** from the English version already recorded (`verbeterpunten-voor-de-informatieverstrekking-van-casps.pdf` vs `marketing-cost-disclosures-casps.pdf`). Both now recorded, with the NL text flagged as authoritative where they differ. **Neither PDF is extracted yet — still the corpus's largest un-mined class-3 asset.**

#### (d) Swept and nothing net-new

ESMA / BaFin / AMF / CONSOB / AFM / CySEC / FCA / MAS / VARA. No named marketing-side enforcement case surfaced. Everything returned was already held or already excluded (transitional-period and perimeter material).

### 4. Operator statements — **0 net-new. Three candidates examined, all three correctly refused.**

- **Magdalena Hörhager (Bitpanda, VP Growth)** — surfaced again via the Rival "CMO Interviews" page. **Already resolved in this corpus as 2023 → out of window, not entered** (`marketing-campaigns/bitpanda-when-crypto-then-bitpanda-2025-09.md`). Re-fetched anyway; the page still carries **no machine-readable date**. **Dedup worked — a closed loose end was not reopened.**
- **Gillian Lynch (Binance, Head of Europe and the UK)** — in-window interview on MiCA's success criteria (*"measured by how many firms it brings inside the regulated market"*). **Regional general-management role, not a marketing seat → role exclusion**, consistent with Demuth / Armstrong / Gauthier / Ghoos / Liniger / Tenev.
- **Joseph Zammit (CMO/CSO, fintech & crypto; Coinmonks/Medium, June 2026)** — argues MiCA is *"not a compliance story, it is a market-structure story."* Directly on-theme and an eligible title, **but not at a tracked firm** → excluded by cohort. Recorded because it is the kind of item that is tempting precisely because it says what the report wants said.

**Bitpanda now carries zero in-window senior-marketing-operator statements for the fifth consecutive run** — notable for the firm `tracked-firms.md` flags as *"deep MiCA readiness signal expected."* **Dominik Beier (CCO)** remains a live but undated candidate; a CCO who owns brand + performance marketing is a **title-boundary question of the Jordan Francis type** and should get an explicit ruling when a dated primary appears, not a drive-by one.

**Unresolved from 07-29, not worked this run and recorded as such:** Jordan Francis's employer (`[VERIFY]` Sui Foundation) and Sui's own account of the rebrand on `blog.sui.io` / `sui.io/press-center`. **Watch (p) is still not discharged for Sui.**

### 5. Layoff tracker — **3 NET-NEW ROWS (13 → 16). A standing finding BREAKS. Watch (h′) WEAKENS.**

#### (a) **Gnosis — the first row in this tracker that names marketing** → `[PERIMETER — NAMES MARKETING]`, 2026-07-17

Until today: *"across all 13 rows, not one names marketing as the affected function."* On **2026-07-28**, Gnosis's own X account (`@gnosis_`) invited companies hiring across **"engineering, product, design, marketing, developer relations and customer relations"** to contact it for introductions to former employees affected by a recent restructuring. Underlying event: Gnosis stated **2026-07-17**, in its own Q2-2026 quarterly report, that it had reduced headcount following a review of its consumer-facing **Gnosis App**. Headcount and percentage **not disclosed**.

**Three disciplines applied, all of which cut against the exciting reading:**

1. **Scope.** Gnosis is **PERIMETER**, not a Stratum 1–4 tracked firm. The **tracker-scoped** standing finding breaks. The **cohort-scoped** one — *no tracked firm has named marketing* — **still holds.** Phase 2 must state which version it is using; the two are not interchangeable and the difference is the whole finding.
2. **What it does and does not establish.** The post is a **hiring-referral offer listing functions**, not an itemised breakdown of cuts. It establishes that **marketing staff were among those who left**. It does **not** establish how many, what share, or that marketing was disproportionately hit. **Do not print it as a quantified marketing cut.**
3. **Sourcing.** Both primary URLs — the X post (`x.com/gnosis_/status/2082042883939672541`) and the forum report (`forum.gnosis.io/t/gnosis-ltd-quarterly-report-q2-2026/12391`) — were **refused by the fetch tool's provenance rule** and are **not directly captured**. The row rests on **near-primary** reporting (Cointelegraph 2026-07-30, which quotes the function list verbatim and links both primaries) plus independent corroboration (Coingabbar, same list). → **`[VERIFY]` both primaries. This is now the single highest-value verification item in the corpus**, because it is the only evidence anywhere in this tracker that touches the report's central question directly.

**Rationale type: product/consumer-app review — non-AI.** Fourth consecutive non-AI contraction rationale (Polygon 07-16, Exodus 07-17, BitMEX 07-23, Gnosis 07-17).

#### (b) **Luno** — ~20% of global workforce, 2026-07-28

**PERIMETER** (DCG-owned; ~16M users across Africa and APAC; not in the tracked cohort). First reported by **Bloomberg 2026-07-28**. **Rationale is AI/automation-framed and CEO-stated, not anonymous** — CEO **James Lanigan** said the company had invested in **automation and broader operational improvements that changed the resources needed to run the business**, alongside cost trimming and continued investment in compliance, core infrastructure and retail products. Strategic direction: toward institutional clients, financial infrastructure and B2B. Prior round Jan-2023 −35% (~330), out of window, context only. **Bloomberg original paywalled and not directly captured → `[VERIFY]`.**

#### (c) **Uphold** — 85 roles, −17%, 2026-07-27 — **and this one weakens watch (h′)**

**PERIMETER.** 85 roles **including both permanent staff and contractors** (unusual in this tracker; **do not drop the contractor inclusion when quoting the figure**). Rationale is **repositioning, explicitly non-AI**: resources shifting to the enterprise / bank-facing business as retail crypto activity weakens; **no offices closing**; UK, European and enterprise customers served as normal. **Consumer roadmap explicitly unchanged** — US stocks, tokenised securities and **prediction markets** still planned by end-2026. CoinDesk 2026-07-27, corroborated by FinanceFeeds, Crypto Briefing and Finance Magnates at the same figures.

**Watch (h′) — "layoff rationale correlates with firm type" — must be recorded as WEAKENED, not re-fitted.** h′ held that consumer exchanges use AI framing (4/4) and infrastructure/protocol firms do not (2/2). Today: **Luno (consumer) is AI-framed → consistent. Gnosis (infrastructure) is non-AI → consistent. Uphold is consumer-facing and its stated rationale is NOT AI — the first consumer-side non-AI rationale in the tracker.** The clean 4/4 is gone. h′ was already flagged *"not safe to print"* at n=6; it is now n=9 with a counter-example, and **it is further from printable than it was yesterday, not closer.**

#### (d) Aggregate context — recorded **with its caveat attached**

CryptoJobsList: **12 crypto and crypto-adjacent firms** reported cuts in **July 2026**, **894 disclosed jobs**; **7,254 disclosed cuts across 47 companies in 2026**. **The caveat must travel with the number** — Cointelegraph itself states the data *"serves as a broad industry indicator rather than a definitive crypto-only total, as it includes adjacent financial technology companies and is heavily skewed by Block's 4,000-person reduction in February."* **Not entered as a tracker row.** Context only.

#### (e) Carried unchanged

Gemini's ~30% YTD aggregate (only 25% citable); Block's tracker date (row says Q2, Cointelegraph says February); **Coinbase CPO departure still unentered for a sixth consecutive run** (watch j); **Robinhood row still misclassified as "crypto-adjacent perimeter"** despite owning Stratum-1 Bitstamp since June 2025 (watch s) — **not corrected again this run, deliberately**, as there is still no evidence either way that the cuts touched Bitstamp Europe or any marketing function.

### 6. Longitudinal shift for synthesis

Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-30 section):

1. **Watch (t) falsified; the real company-list gap is 4 firms, not 12.** OKX, Securitize, Rabby, Relai.
2. **The true class-1 defect is flow-vs-stock, and it invalidates the promised 12-month window before 2026-06-26.** 5 qualifying roles at 3 tracked firms, in window, missing. → watch **(t′)**.
3. **A third failure mode named: in-feed, unreachable, silent** (Sui, `sui%20foundation`). Failures that 404 are safe; failures that return empty are not.
4. **Gemini enters class 1 for the first time, on a Predictions seat in New York**, five months after exiting the EU to fund exactly that product.
5. **Prediction markets converge across two source classes and three dated artefacts** — Gemini's Feb-2026 redirection, Gemini's 07-29 marketing req, Uphold's retained 07-27 roadmap. First time classes 1 and 5 have pointed at the same product category.
6. **Class 5's standing "nobody names marketing" finding breaks at the perimeter and holds in the cohort** (Gnosis).
7. **Watch (h′) weakens** — first consumer-side non-AI rationale (Uphold). Further from printable, not closer.
8. **Class-3 backlog cleared; both targets resolve as structured nulls**, and the CNMV read produced a scoping caveat that would otherwise have become an error in Chapter 1.

Methodology guards applied and satisfied: **a prior run's own conclusion tested against primary configuration data and withdrawn when it failed** (watch t); **the withdrawal recorded in the audit file itself, not just the run record**; multi-point verification before every class-5 entry; **perimeter-vs-cohort scope enforced on the one finding that most rewarded blurring it** (Gnosis); **a quantified marketing-cut reading explicitly refused** where the source supports only a qualitative one; **an aggregate statistic entered only with its publisher's own skew caveat attached**; **an out-of-window precedent recorded as a framing caveat and explicitly barred from the corpus** (Miolo 2023); **two NCAs on the same channel kept separate** rather than merged into a consensus; **a closed loose end not reopened** (Hörhager); **two role exclusions and one cohort exclusion enforced** (Lynch, Beier deferred, Zammit); **a watch item recorded as weakened rather than quietly re-fitted** (h′); **a backfill recoverability claim downgraded to probable** because `jobs_seen` lacks the schema fields.

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged; still France-reported-only.
- **(b) First named post-deadline NCA marketing-side action** — **day-29 silence HOLDS.** **Backlog CLEARED**: CNMV read executed, AFM finfluencer closed. The null is now better-founded than at any prior point — and, per the CNMV read, must be **scoped to the MiCA-era regime**.
- **(c) Capture panel — 07-31 is TOMORROW and carries three things:** Kraken MiCA-lapse checkpoint, OKX 8% campaign end, Friday nomination check. **Kraken is triple-loaded. OKX is confirmed NOT-IN-FEED, so its checkpoint must be a manual read — there is no automated lane to fall back on.**
- **(d) Agency panel staleness — 45 days.** Stable-by-decision; not re-escalated.
- **(e) Loop cadence** — 07-30 fired normally and on schedule; **third clean single-fire day running.** Tenth consecutive run carrying this; the trend is good. Still needs Jukka's eyes once.
- **(f) Friday nomination cadence** — next check **07-31**. No `inbound-nominations.md` exists.
- **(g) Coinbase brand-rebuild signal** — unchanged at n=1 on postings.
- **(h′) Layoff rationale correlates with firm type** — **WEAKENED.** n=9 with a consumer-side non-AI counter-example (Uphold). **Do not print.**
- **(i) Kraken paid-media build-out** — unchanged; three dated legs, sequence only.
- **(j) Senior-leader exits trailing contractions** — Coinbase CPO still unverified, **sixth run**.
- **(k) Chrome-lane instrumentation gap** — unchanged; the 07-25 Binance Dubai req remains unrecoverable.
- **(l) `methodology.md` §4 inventory too narrow** — unchanged and still costed twice (Bitpanda, Ledger). The §4 rewrite (marketing trade press + regional-language media + firm-owned channels) is not optional for Phase 2.
- **(m) Ad-platform gating** — unchanged (Google France, 2026-07-01).
- **(n) Full-range re-sweep of classes 3 and 5** — classes 3 and 5 re-swept 07-28 and again today. **Classes 1 and 2 historical backfill still not run** — and (t′) now makes it the single highest-value backfill available.
- **(o) Date the document, never an event held about it** — held.
- **(p) Absence claims must be tested against firms' OWN channels** — **not advanced this run** (the class-1 forensics and the class-3 backlog took the budget). Still unswept: Bybit, OKX, Kraken, Coinbase, Crypto.com, Gemini, all of Strata 2 and 4. **Not discharged for Sui.**
- **(q) The agency matrix measures the crypto-native segment, not "agency relationships"** — unchanged, and now compounded: its only OVERLAP row (Sui) is simultaneously the corpus's only BROKEN-SLUG firm in class 1.
- **(r) The absence panel needs a "structural withdrawal" category** — Gemini. **Now more interesting, not less**: the structurally-withdrawn firm is hiring marketing again, in the market it withdrew *to*.
- **(s) The layoff tracker's Robinhood row is misclassified** — unchanged; deliberately not corrected for a second run, for want of evidence either way.
- **(t) ~~12 of 27 tracked firms are missing from the upstream company list~~** — **FALSIFIED AND CLOSED.** 8 of the 12 are in the scanner config, correctly configured. **The surviving gap is 4 firms: OKX, Securitize, Rabby, Relai.** Superseded by (t′).
- **(t′) NEW — class 1 is a FLOW register presented as a STOCK register.** `daily-corpus-sync.py` captures only roles open at run time and began 2026-06-26. `jobs_seen` proves ≥5 qualifying roles at 3 tracked firms were open in window and never reached the corpus. **`methodology.md` §1's "rolling 12 months" promise is currently unmet, and no Theme-1 hiring claim for any period before 2026-06-26 is safe.** Fix is a backfill from `jobs_seen` job IDs; recoverability **probable, not certain** (no titles/URLs stored; closed roles may 404).
- **(u) Brand absorption defeats name-keyed sweeps** — unchanged; the cohort name-alias table is still unbuilt.
- **(v) NEW — NCA *warning lists* have never been swept, in any jurisdiction.** Distinct from sanctions registers and much faster-moving (CNMV `Advertencias de entidades no registradas`, and equivalents at AFM/BaFin/AMF/CONSOB/CySEC). Unauthorised-CASP wind-down carries an explicit duty to *"cease marketing activities and solicitation"* — **if a first marketing-adjacent public action exists anywhere, this is the most likely place it is already sitting.** The day-N silence finding is not fully safe until these are swept once.

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2 deterministic. **1 net-new (Gemini).** Summary captured above.
2. Feed-health guard: direct read of `prospects/open-positions.json` `scan_metadata` / `drops_summary` / `new_since_last_scan` / `fetch_errors`.
3. **Direct read of `prospects/scanner/config.json`** (147-company dict) → **falsified watch (t)**; 8 of 12 "silent" firms present and correctly configured; **only OKX, Securitize, Rabby, Relai genuinely absent**; **Sui slug `sui%20foundation` discovered.**
4. **Direct read of `prospects/scanner/state/last-scan.json` (`jobs_seen`, 116 entries)** → **the flow-vs-stock defect**; 5 qualifying roles at 3 tracked firms, in window, never captured.
5. Direct read of `prospects/prospects-list.txt` → all 12 except Rabby and Relai present with careers URLs, confirming the gap is in the *scanner config*, not the prospect list.
6. Full rewrite of `corpus/job-postings/_absence-cohort-audit.csv` — 27 rows, new `upstream_feed_status` column, four defect classes.
7. `git status` / `git log origin/main..HEAD` → clean tree at 1613f90, already on origin/main.
8. Dedup baseline reads + repo-wide greps (`luno`, `gnosis`, `uphold`, `hörhager`, `beier`, `lanigan`, `cryptojobslist`, `cnmv`, `miolo`, `finfluencer`, `afm`, `gemini`, `predictions`).
9. WebSearch (domain-restricted `afm.nl`) `AFM finfluencer onderzoek crypto marketing report 2026` → **finfluencer study located and dated 2021 → out of window, target CLOSED**; also surfaced the **NL-language** April-2026 report path.
10. `web_fetch` `afm.nl/en/sector/actueel/2026/apr/pb-reclame-informatie-casps` → re-verified; content identical to 07-27 capture. **Dedup held, not re-entered.** NL PDF path added to the existing file.
11. WebSearch `CNMV publicidad criptoactivos MiCA expediente sancionador 2026` → surfaced the sanctions register + the **2023 Miolo Desarrollos** precedent (out of window).
12. WebSearch (domain-restricted `cnmv.es`) `CNMV expediente sancionador publicidad criptoactivos 2026 infracción` → **no 2026 marketing-side enforcement.** Circular-1/2022 and MiCA Q&A material only.
13. `web_fetch` `cnmv.es/portal/Consultas/RegistroSanciones/IniRegSanciones` → **CNMV direct read EXECUTED** (carried three runs). Statutory framing, five-year retention, anonymisation clause, query-interface URL. **→ NEW FILE.**
14. WebSearch `crypto marketing team layoffs July 2026 growth brand restructuring exchange` → **Luno, Uphold, Gnosis + the CryptoJobsList aggregates.**
15. `web_fetch` `cointelegraph.com/news/luno-cuts-staff-crypto-layoffs-july` (published **2026-07-30**) → **Luno −20% + Lanigan verbatim rationale; Gnosis function list including MARKETING; the July/2026 aggregates with the publisher's own skew caveat.** **→ 2 ADDED.**
16. WebSearch `Uphold cuts 17% global headcount enterprise pivot July 2026` → **85 roles / −17%**, non-AI repositioning, retained prediction-markets roadmap; four independent outlets at the same figures. **→ ADDED.**
17. WebSearch `Gnosis quarterly report Q2 2026 restructuring workforce Gnosis App` → **did not surface the forum report**; Ghost/community summaries only.
18. `web_fetch` `forum.gnosis.io/t/gnosis-ltd-quarterly-report-q2-2026/12391` → **REFUSED by the fetch tool's provenance rule. Primary not captured; `[VERIFY]` flagged.**
19. WebSearch `Gnosis restructuring former employees hiring marketing developer relations X post July 2026` → **independent corroboration of the verbatim function list** (Coingabbar), and the 2026-07-17 quarterly-report date.
20. WebSearch `crypto exchange CMO "head of marketing" interview 2026 MiCA marketing compliance brand` → Zammit (**not a tracked firm** → excluded), Gillian Lynch (**role exclusion**).
21. WebSearch `Bitpanda OR Bybit OR "Crypto.com" chief marketing officer 2026 statement brand growth podcast` → Hörhager (**already closed as 2023**), Beier (CCO, undated).
22. `web_fetch` Rival Hörhager content-hub page → **still no machine-readable date. Not entered; closed loose end left closed.**

## Net-new / changed this run

- `corpus/job-postings/gemini.csv` (**NEW FILE — 1 net-new class-1 posting.** Predictions Partnerships Marketing Lead, New York, posted 2026-07-29, greenhouse, URL-verified. First-ever class-1 capture at Gemini)
- `corpus/job-postings/_absence-cohort-audit.csv` (**FULLY REWRITTEN — 27 rows, new `upstream_feed_status` column.** Watch (t) falsified and withdrawn *in the audit file itself*; four defect classes separated: NOT-IN-FEED 4 · FLOW-LOSS 2 · BROKEN-SLUG 1 · TRUE-ABSENCE 4)
- `corpus/layoff-tracker/2026-layoff-tracker.csv` (**13 → 16 rows.** Gnosis [PERIMETER — NAMES MARKETING] 07-17 · Luno [PERIMETER] −20% 07-28 · Uphold [PERIMETER] 85/−17% 07-27. Standing finding broken at the perimeter, held in the cohort; h′ recorded as weakened)
- `corpus/regulator-filings/cnmv-sanctions-register-read-2026-07.md` (**NEW FILE.** CNMV direct read discharged after three carried runs; register is lagging + anonymisable; **Miolo 2023 / Circular 1/2022 precedent recorded as a framing caveat and barred from the corpus**; watch (v) opened)
- `corpus/regulator-filings/afm-casp-advertising-cost-information-review-2026-04.md` (**UPDATED.** NL-language report path added and flagged authoritative; **AFM finfluencer target closed as 2021/out-of-window** with the inducement-vs-disclosure distinction preserved)
- `findings/longitudinal-2026-06.md` (2026-07-30 section)
- `corpus/weekly-runs/2026-07-30-corpus-run.md` (this record)
- **Not changed:** `agency-overlap-matrix.csv` + `agency-claims/*` (idempotent, 45th day); other `job-postings/*.csv` (`_absence.csv` + `_chrome-queue.csv` date re-stamps only); `operator-statements/*` (0 adds — three candidates examined, all refused)

## Recommendation for next run

1. **07-31 is TOMORROW and it is the heaviest date on the calendar:** Kraken MiCA-lapse checkpoint, OKX 8% campaign end, Friday nomination check. **OKX is NOT-IN-FEED — its checkpoint has no automated lane and must be a manual read.** Prepare both captures before the date.
2. **`[VERIFY]` the two Gnosis primaries** — the X post and the forum quarterly report. This is the **highest-value verification item in the corpus**: it is the only evidence in the tracker that names marketing, and it currently rests on near-primary reporting alone.
3. **Run the class-1 backfill from `jobs_seen` (watch t′).** Start with the 5 known-missing roles at Trust Wallet, Arbitrum Foundation and Offchain Labs — re-query the ATS APIs by job ID. **First attempt is a test of recoverability, not a promise**; if closed roles 404, say so and re-scope `methodology.md` §1's 12-month claim accordingly.
4. **Fix the 4 real company-list gaps.** Securitize is the cheapest (standard greenhouse board, already on the prospects list); **OKX is the most valuable** (Tier-1, MiCA-relevant, proprietary ATS → chrome lane). Then resolve careers URLs for Rabby and Relai.
5. **Fix the Sui slug** (`sui%20foundation`) and decide whether Sui goes to the Getro/chrome lane like Solana. **Audit Sui end-to-end while you are there** — it is the only firm currently degraded across three instruments at once.
6. **Sweep NCA warning lists once (watch v).** CNMV `Advertencias`, plus AFM/BaFin/AMF/CONSOB/CySEC equivalents. **The day-N silence finding is not fully safe until this is done once**, and it is the cheapest remaining risk to the report's headline claim.
7. **Extract the AFM report PDFs** (NL preferred). Largest un-mined class-3 asset in the corpus, carried since 07-27.
8. **Continue watch (p)** on the unswept firms, and **discharge it for Sui** (`blog.sui.io`, `sui.io/press-center`) while resolving Jordan Francis's employer.
9. **Escalate to Jukka:** (i) **watch (t′) — the class-1 window promise in `methodology.md` §1 is currently unmet**; this is a methodology-integrity item, not a data-entry one, and it needs a decision: backfill, or re-scope the published claim. (ii) The 4-firm company-list gap (down from the 12 reported yesterday — **yesterday's escalation overstated the problem and this run corrects it**). (iii) The mount's `unlink` block. (iv) Scheduler cadence — three clean days running.
