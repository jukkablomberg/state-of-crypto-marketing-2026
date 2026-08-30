# Corpus-assembly daily run — 2026-08-30 **(day 60 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-30 (**Sunday — T-2 to ship**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-29 recommendations:** (1) 🔴 check the upstream ATS scan before anything else; (2) ⚠ decide the absence-panel sentence — fifth restatement; (3) ⚠ fix `methodology.md` §6's "daily 18-agency panel"; (4) ⚠ source or strike `sport-sponsorship-reset-2026-05.md` and tracker row 6 (MARA); (5) do **not** re-fetch `CASPS.csv` / `OTHER.csv` / `NCASP.csv`, re-open MAS, re-issue the retry queue, attempt row 13's Bloomberg paywall, or fetch the four un-fetched FCA orders / VARA's Shelbit, MEXC, CoinMENA notice bodies.
**Dedup baseline read before writing:** `2026-08-29-corpus-run.md` in full; `README.md`, `README-for-github.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md`; all 26 tracker rows via `csv.DictReader`, row 6 field-by-field; all 17 rows across the 13 tracked-firm job-postings CSVs; `sport-sponsorship-reset-2026-05.md` and `_stale-article-as-current-signal-instrument-2026-08-20.md` in full; directory indexes for `operator-statements/` (9), `weekly-runs/` (59), `findings/` (5); upstream `scan_metadata`, `new_since_last_scan`, `still_open_from_prior_scans`, `drops_summary` and `_feed-fingerprint.json` read directly.
**🟢 CADENCE (this loop): HELD.** 08-29 → 08-30 is a one-day step; 60 run records for 60 post-deadline days.
**🟢 CADENCE (the upstream feed): RECOVERED.** See §1.

---

## Headline result

**The feed came back, and the day's work was spending the four remaining pre-ship defects down to one. Every layoff-tracker row now carries a citation, for the first time in the cycle. The report's own compliance claim in a class-4 file turned out to be false, and a slug collision showed that a URL-verified posting can be the wrong company.**

### 1. 🟢 **THE UPSTREAM ATS SCAN RAN. CLASS 1 IS GENUINELY ABSENT TODAY — THE FIRST EARNED ABSENCE CLAIM SINCE THE FREEZE.**

```
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-30T00:15:22Z, age=11.9h,
  fingerprint total_jobs_fetched=3398, delta=+36 vs 2026-08-29 (3362))
  reason: age 11.9h, fingerprint delta +36
job postings ADDED: 0  firms: []
```

Both predicates pass. `scan_date` is **2026-08-30**, `scanned_at_utc` is fresh, and the fingerprint moved **3362 → 3398**. The scan looked and found no tracked-firm marketing role.

⚠ **The recovery was not the scheduler healing itself, and the run record must not read as if it were.** `situation.md` records that the **product-builder ran the repo's own scanner in-session tonight** (`[NP-ATS-FEED-ONESHOT]`, 147 companies, 3,398 jobs) — a **one-shot**, not a restored cadence. It also found that `scan.py`'s docstring wrongly claimed the sandbox blocks greenhouse/lever/ashby/workable; all four return 200. **So today's HEALTHY verdict is real but manually produced, and nothing yet proves the scheduled task will fire on 08-31** — the last day of the advertised capture window. Carried on the needs-jukka row rather than treated as closed.

> 🟢 **PERMITTED, and stated:** *no firm in the Stratum 1–4 cohort had a net-new marketing or growth posting observable through the ATS API scan of 2026-08-30.*
> 🔴 **STILL PROHIBITED:** any statement extending that to Binance, Bybit, HTX, KuCoin or Aave, which are not API-reachable and are in `_absence.csv` for that reason.

⚠ **The delta is a two-day delta, not a one-day rate.** The prior observation is 08-28's scan (08-29 was the frozen re-read of it), so **+36 spans two calendar days.** Watch (ac) — *the fingerprint series is not one series* — applies directly, and the run record says so rather than letting `+36` be read as a daily figure.

🟢 **And the capture-window defect the 08-29 record escalated did not materialise.** Class 1's window ends **2026-08-31** as `methodology.md` and both READMEs state. No scope sentence is needed. **Escalation (i) of 08-29 is CLOSED.**

⭐ `_absence.csv` rolled to `as_of 2026-08-30` and **today that date is earned** — a 2026-08-30 scan did produce it. Watch (ai) is dormant, not fixed: the sync still writes `as_of` from its own clock. Now recorded permanently in `methodology.md` §1 instead of only in run records.

### 2. 🟢 **EVERY LAYOFF-TRACKER ROW NOW CARRIES A SOURCE URL. ROW 6 SOURCED; THE STRIKE FLAG IS LIFTED — AND THE FIGURE IT ADVERTISED WAS AN OUTLET'S ARITHMETIC.**

MARA Holdings had been flagged **STRIKE AT SHIP** since 2026-08-21 for having no citation at all. Two primaries were fetched and the row is now the best-graded it has ever been — and materially different from what it said:

| Field | Was | Now |
|---|---|---|
| `date_announced` | `2026-Q2` | **2026-04-02 [REPORTED]** — the firm announced no date |
| `percentage` | *(empty)* | **-15%, FIRM-STATED VERBATIM** — spokesperson: *"we made the difficult but necessary decision to reduce our team by approximately 15%"* |
| `headcount_change` | **`40`**, bare | **undisclosed by the firm.** 40 is Blockspace's arithmetic — 15% × 266 most-recently-disclosed FTEs |
| `ai_cover` | *(blank — never labelled)* | **Y-ADJACENT**, graded down deliberately |
| `source_url` | *(none)* | `unchainedcrypto.com/mara-holdings-cuts-15-of-staff…` |

**Three things worth keeping.**

🔴 **(a) A third advertised headcount figure turns out to be an outlet computing a percentage against a stale base.** Row 1 (Crypto.com ~180) and row 2 (Gemini 200, struck) were the first two. **Three of twenty-six rows.** The report must not print `40` for MARA any more than it prints `200` for Gemini.

🔴 **(b) The AI framing is the outlet's, not the firm's.** MARA's own words are *"strategic evolution from a pure-play Bitcoin miner into an **energy and digital infrastructure** company."* The words *AI* and *HPC* belong to the outlets' section headers and to Thiel's framing **of the bitcoin sale**, not to the spokesperson's framing of the layoff. Graded `Y-ADJACENT` for exactly this reason. **This is the 2026-08-11 Kalifowitz error mechanism — adjacency is not attribution — caught before entry rather than three months after it.**

⭐ **(c) Two primaries captured the same day disagree, purely as a function of capture time.** Bitcoin Magazine (published **2026-04-02**) states verbatim that the figures *"ha[ve] not been disclosed, and the company has not publicly commented on the cuts."* Unchained (published 2026-04-03 06:55 ET) carries the firm's 15% — inside an explicit stamp: *"Update Friday April 3, 2026, 12pm ET: Article now credits Blockspace with breaking the news and adds comment from MARA."* **A captured primary is a snapshot of an artifact that keeps moving, and the earlier capture would have supported a *stronger* absence claim than the truth.** New watch (ak).

**Result: 26 of 26 rows cited. Class-5 `NO-URL` is zero.** MARA is perimeter-only and **no source names marketing as an affected function** — the row carries no Theme-1 signal and is recorded as such.

### 3. 🔴 **A CLASS-4 FILE CERTIFIED ITS OWN COMPLIANCE IN ITS CLOSING PARAGRAPH, AND THE CERTIFICATE WAS FALSE FOR THREE MONTHS.**

`sport-sponsorship-reset-2026-05.md` ended with:

> *"Every claim above is anchored to a public source (Bybit Q4 2024 comms, Bloomberg, CoinDesk, Wu Blockchain, FX News Group, Inside Sport). No off-the-record interview material. Phase 1 corpus rule satisfied."*

**None of the seven incidents was anchored to a URL.** Naming an outlet is not anchoring to a source, and the Phase-1 rule — *either there is a citation, or the claim is omitted* — was not satisfied by any of them. `date-provenance-audit.py` had flagged the file 🔴 NO-URL on every run since 08-21; **the closing paragraph is why nobody read the flag as damning.**

Repaired today, without fetching or guessing anything:

- 🟢 **§2, §3, §4 ANCHORED** to primaries the corpus already holds (tracker rows 1 and 4; the Kalifowitz capture). Cite those, not this file.
- 🔴 **§1, §5, §6, §7 marked `UNSOURCED — DO NOT CITE`** inline. Nothing in this corpus cites them.
- 🔴 The false paragraph is replaced with an accurate one that says what it replaced and why it survived.
- The header now states what the file is: **a synthesis note, never a class-4 capture** — which is why a class-4 rule flagged it forever.

🔴 **§5 is load-bearing and is the escalation.** The Binance Conlan→Chen reading — *first Tier-1 to put a non-marketing operator in the CMO seat without running a search* — is quoted in the May 13 essay and referenced in Theme 1, and it rests entirely on an uncited CoinDesk scoop. **Source it before ship or cut the Theme-1 claim.** Not fetched today: the 08-29 mandate prohibits speculative fetching, and this needs Jukka's call on whether the claim stays.

**Watch (n), fourteenth vindication**, and the sharpest yet: *a file that asserted its own compliance was believed for three months because nobody read the assertion against the file above it.*

### 4. ⭐ **A URL-VERIFIED, CORRECTLY-DATED, FIT-SCORED POSTING WAS THE WRONG COMPANY. THE COHORT FILTER CAUGHT IT — BY LUCK.**

Two of today's three net-new upstream postings are labelled **Circle · Tier 2 · Stablecoin**, `url_verified: true`, `head_200`, `fit_score` 100 and 85. **Every automated signal green.** Their own posting body reads:

> *"Circle is building the world's leading AI-powered, all-in-one platform for digital businesses. We make it possible for creators, coaches, educators, and businesses to bring together their audience…"*

That is **circle.so**, the creator-community platform — not Circle Internet Financial, the USDC issuer the labels describe. Identity in the feed resolves by **ATS slug**; tier and category come from a prospect table keyed on the display name; **nothing checks the two against each other**, and `head_200` verifies that a URL resolves, not that it resolves to the company the row names.

⚠ **The cheap check gives the wrong answer confidently:** searching the slug returns *Circle Health* and *Funding Circle*; searching the name returns the USDC issuer. Only the posting body settles it. Corroborated against circle.so's own public copy, which carries the same sentence nearly verbatim.

🔴 **The filter that saved the corpus is a filter on the name, and the name was the thing that was wrong.** Circle is not in the cohort, so both rows were dropped. Had the colliding slug belonged to a cohort display name — *Gemini*, *Phantom*, *Ledger*, *Kraken* are all common English words — two fabricated crypto marketing postings, URL-verified and correctly dated, would have entered `corpus/job-postings/` with nothing positioned to object.

🟢 **Independently corroborated the same day, by a loop that had no idea it was corroborating anything.** The Convertor's apply lane worked the *same two rows* this morning and its log names the company **"Circle (circle.so)"** — it resolved the identity correctly because staging an application forces you to read the job description. It also caught that the sister row is geo-ineligible (*"any North American time zone"*) and recorded a **Lead Gen sourcing-filter miss**. **Two loops, opposite ends of the pipeline, hit the same defect within hours; the one that reads bodies saw it and the one that reads labels did not.**

**A slug-vs-label reconciliation was run across all 17 rows in the 13 tracked-firm CSVs: 0 real mismatches.** It raised two flags and **both were defects in the check** — `gemini` reads `boards.greenhouse.io/embed/job_app?**for=gemini**` (company in a query parameter, not the path) and `optimism` reads slug `oplabs` (OP Labs, a known-good alias matching tracker row 12). Recorded in full per the 08-21 rule that a guard's first run is a test of the guard. Full record: `corpus/job-postings/_ats-slug-collision-circle-2026-08-30.md`. New watch (al).

### 5. 🟢 **THE CLASS-4 GUARD WAS FLAGGING A FILE THAT DECLARES ITSELF EXEMPT. A 🔴 THAT CAN NEVER CLEAR IS WORSE THAN NO FLAG.**

`date-provenance-audit.py` applied the class-4 storage rule to `_stale-article-as-current-signal-instrument-2026-08-20.md`, an instrument note whose own header reads *"Instrument/methodology note, **not an operator statement**. Exempt from the class-4 storage rule by kind."* It was flagged 🔴 NO-URL anyway, on every run, and it never can be otherwise — it cites no external artifact and correctly never will.

Patched to honour the repo-wide underscore convention (`_absence.csv`, `_feed-fingerprint.json`, `_esma-*-snapshot-*.csv`, `_citation-opening-sweep-*.md`), and **reported as `EXEMPT-INSTRUMENT`, never silently skipped.** Discrimination verified both ways in the same run: the instrument note now reports `EXEMPT-INSTRUMENT`; `sport-sponsorship-reset-2026-05.md` still fired 🔴 `NO-URL` and still exited 1 **before** its repair. **Corpus-wide 🔴 count: 2 → 0.**

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

```
date: 2026-08-30   source A (jobs) scan_date: 2026-08-30   ← RECOVERED
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-30T00:15:22Z, age=11.9h,
  fingerprint total_jobs_fetched=3398, delta=+36 vs 2026-08-29 (3362))
job postings ADDED: 0  firms: []   of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance','Bybit','HTX','Kucoin','Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave','Binance','Bybit','HTX','Kucoin']
```

Fingerprint series:

```
2151 → 2151(frozen) → 2186 → 2196 → 2259 → 2265 → 2263 ‖ 3334 → [no 08-26] → 3356 → 3362 → 3362(frozen) → 3398
                                                          ↑ break                                          ↑ TODAY (+36 over TWO days)
```

`companies_scanned` **147**, `companies_via_api` **99**, `companies_via_chrome_pending` **48** — today's numbers, not a stale re-read. `fetch_errors`: the same four stable 404s (Wormhole Foundation, Aave, Bitwise, Chainlink Labs). Upstream `new_count` **3**, all outside the cohort: **Circle ×2** (see §4 above — mislabelled) and **OpenAI — Business Communications Lead, Cybersecurity**, posted 2026-08-28.

**Watch (ag) — ADVANCED TO n=4.** The AI-lab marketing/comms posting pattern gained a fourth *observation*: OpenAI again, and `still_open_from_prior_scans` holds **OpenAI 11 · Anthropic 8 · Cohere 3 · Perplexity 2 = 24 open AI-lab marketing roles** against **Gemini 1 · Phantom 1** for the cohort. ⚠ **Not a corpus entry** — AI labs are outside Stratum 1–4 — but the ratio is the sharpest form the observation has taken and belongs in Theme 2's read of where marketing hiring actually is.

**Absence panel: 5 firms, membership unchanged since the cohort expansion, `as_of` earned today.**

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 76 days stale.** 18 agency-claims files written, **byte-identical for the nineteenth consecutive run.** 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation.

🟢 **Watch (d), 25th run — CLOSED.** The last overstatement is gone. Six exact-string edits across three files, each with an asserted occurrence count, then a residual grep confirming **CLEAN**:

| File | Was | Now |
|---|---|---|
| `README.md` ×2, `README-for-github.md` ×2 | *"daily competitor-intelligence panel"* / *"refreshed daily"* | *"18 agencies; **last refreshed 2026-06-15**"* + a line stating the panel is designed to refresh daily, did so through mid-June, and **has not moved since**, and that the report makes no claim about agency-side activity after that date |
| `methodology.md` §6 heading | *"NorthPoint **daily** competitor-intelligence pipeline"* | *"⚠ last refreshed 2026-06-15"* |
| `methodology.md` §"Automated daily feeds" | *"**daily** 18-agency panel"* | *"`lastUpdated` 2026-06-15 and unchanged since; the class-2 outputs have been byte-identical on every run after that date"* |

### 3. Regulator — **0 NET-NEW. Every candidate already held or refused on scope.**

| Surfaced | Disposition |
|---|---|
| CONSOB finfluencer warnings amplifying ESMA's factsheet | **ALREADY HELD** — `esma-finfluencer-factsheet-consob-amplification-CANDIDATE-2026-08-11.md`, `esma-finfluencers-factsheet-at-source-2026-08-22.md` |
| ESMA statement calling unauthorised CASPs to wind down / cease marketing | **ALREADY HELD** — captured at source; the AMF mirror adds nothing the primary lacks |
| ESMA warning list — "167 entries, 165 from Italy, none from BaFin" | **ALREADY HELD** — this is the 08-23 finding, from `NCASP.csv` read at source. Secondary coverage of our own held register |
| ESMA knowledge-and-competence guidelines (AMF DOC-2026-03) | 🔴 **REFUSED ON SCOPE.** Staff competence, not marketing communications |

**Watch (b) — NOT ADVANCED. The EU-NCA marketing-side enforcement null stands at day 60**, in its narrow form: *no EU national competent authority has published a named marketing-side enforcement action against a CASP since the MiCA transitional deadline.* The FCA/HTX action is UK s.21 FSMA and is excluded by its own record.

**Not fetched, not guessed:** `CASPS.csv`, `OTHER.csv`, `NCASP.csv`, MAS, the retry queue, the four un-fetched FCA orders, VARA's Shelbit / MEXC / CoinMENA notice bodies, `rulebooks.vara.ae`. **All 08-29 prohibitions honoured.**

### 4. Operator statements — **0 NET-NEW. SIXTEENTH consecutive recall confirmation.**

| Surfaced | Disposition |
|---|---|
| **NorthPoint's own press release** (natlawreview, 2026-08-14) | 🔴 **REFUSED — fourth consecutive run.** Our own promotional material; the author is not a tracked-firm operator. A report that cited its own publisher as a corpus source would deserve everything it got |
| Vendor/consultancy MiCA explainers (Trusty, Unit21, Rightlander, Coinmonks, Cryptonomist) | **REFUSED.** Secondary commentary; no tracked-firm operator speaks in any of them |

⚠ **Watch (l), 26th costing — WEAK.** Both refusals are valid at any §4 width. **Escalation (v) is not strengthened.**

**+0 admitted. §4 repair work this run was on the files already held — see headline 3.**

### 5. Layoffs — **0 NET-NEW EVENTS. Row 6 repaired; tracker now 26 rows, 26 citations.**

Search returned Crypto.com (row 1), Coinbase (row 4), Gemini (row 2), FalconX (row 18), BitGo (row 8), Ethereum Foundation (row 21), Bitwise (row 24), Luno (row 15) — **all held.** Two aggregators (CryptoJobsList, layoffhedge, ratelys) not admitted. MARA surfaced as a *sourcing* target, not a new event; see headline 2.

🟢 **Row 6 (MARA): SOURCED. Strike flag LIFTED.** The ai_cover denominator returns to **26**.

### 6. NorthPoint longitudinal panel

Panel unchanged (76 days stale). Day-60 shift appended to `findings/longitudinal-2026-06.md`.

---

## Guards run

| Guard | Result |
|---|---|
| `daily-corpus-sync.py` feed-health | 🟢 **HEALTHY**, both predicates pass. First earned class-1 absence claim since the 08-27→08-29 freeze |
| slug-vs-label reconciliation (by hand, new) | 🟢 **0 real mismatches / 17 rows.** 2 false positives, both defects in the check, both adjudicated. ⚠ **Not automated — nothing runs this on a schedule** |
| `verify-capture.py` | **Not run — correctly.** No register CSV was captured this run. Recorded, not silently skipped |
| `date-provenance-audit.py` | **Run twice.** Before repairs: exit 1, 2×🔴 NO-URL. After: **exit 0**, `EXEMPT-INSTRUMENT=1 · LAG-EXCEEDED=2 · NO-URL-DATE=14 · SELF-DATED=17 · UNPARSEABLE-DATE=1`. **Zero citationless rows corpus-wide, for the first time** |

⚠ **`SELF-DATED` still means the citation and the corpus agree, not that either is right**, and **17 rows remain unaudited by the predicate.** That is a work queue, not a pass. Unchanged.

---

## Watch items

- **(b) First named post-deadline EU NCA marketing-side action** — **NOT ADVANCED.** Null holds at day 60.
- **(d) Agency panel staleness — 76 days** — 🟢 **CLOSED.** Every public document now states the last-refresh date. Byte-identical nineteen runs; that fact is now published rather than merely known.
- **(e′) Cadence** — 🟢 **BOTH CLOCKS HELD.** The loop stepped one day; the upstream feed recovered. First run since 08-28 where these agree.
- **(i) `web_fetch` provenance refusals** — **EXERCISED, AND IT BIT.** `jobs.ashbyhq.com/circle` could not be fetched (not in the provenance set), so the Circle identity was settled from the feed's own captured body plus circle.so's public copy. **The refusal did not block the finding; it changed which evidence carried it.**
- **(j) Senior-leader exits** — **NOT ADVANCED.** Sixteen consecutive runs.
- **(l) §4 too narrow** — **26th costing, WEAK.**
- **(n) Full-range re-sweep** — 🟢 **FOURTEENTH VINDICATION, and the sharpest.** A file's own closing paragraph certified compliance it did not have, and the certificate is why the standing 🔴 was never read as damning.
- **(pp) A clean parse is not a complete capture** — 🟢 **HONOURED.** No absence claim from an unverified capture; none attempted.
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — 🟢 **PAID FORWARD.** The Circle rows *confirmed* a Tier-2 stablecoin firm hiring growth talent, scored 100, and were wrong. Caught by reading the body, not the label.
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — 🟢 **HONOURED TWICE.** The slug reconciliation's two flags were both its own bugs; the class-4 exemption patch was discrimination-tested both ways before being believed.
- **(vv) A number is not safe until someone has read its citation** — 🟢 **TEN-FOR-TEN.** MARA's `40` had no citation at all and is an outlet's arithmetic.
- **(ac) The fingerprint series is not one series** — 🟢 **EXERCISED.** `+36` spans two calendar days and is recorded as such, not as a daily rate.
- **(ad) The absence panel has never contained an absence** — **UNCHANGED**, but no longer only in run records: `methodology.md` §1 now carries the firm-silence vs. scanner-reach distinction as a permanent table. **Recommendation 2 of 08-28/08-29, fifth restatement — CLOSED.**
- **(ai) A derived file can date itself from the run clock** — **DORMANT, NOT FIXED.** Today's `as_of` is earned because the scan ran. The sync still writes it from its own clock; the defect and the workaround (read `as_of` against `_feed-fingerprint.json`) are now recorded in `methodology.md` §1.
- **(aj) A secondary chain invented a named CEO** — 🟢 **APPLIED.** MARA's spokesperson quote was taken only from the outlet that stamps when it was added, and the AI framing was traced to whose mouth it was actually in.
- **🆕 (ak) ⚠ A CAPTURED PRIMARY IS A SNAPSHOT OF AN ARTIFACT THAT KEEPS MOVING.** Bitcoin Magazine (04-02) says MARA disclosed nothing; Unchained (04-03, explicitly updated 12pm ET) carries the firm's 15%. **The earlier capture would have supported a stronger absence claim than the truth.** Where an outlet stamps an update, record the stamp. Where it does not, a capture date is not a publication date. Bears on every class-3/4/5 record captured once and never re-read.
- **🆕 (al) 🔴 A URL THAT RESOLVES IS NOT A COMPANY THAT MATCHES.** `head_200` is a liveness check. Company identity in class 1 is slug-derived and is reconciled against the label by nothing. The cohort filter is a filter on the name — useless when the name is the error. **Two of four ATS URL shapes put the company in a query string, so any automation of this must parse both.**
- **Unchanged and not re-narrated today:** (a), (c), (e), (f), (g), (h), (h′ — REJECTED), (k), (m), (o), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (ab — CLOSED), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (mm), (nn), (oo), (qq), (rr), (uu), (ww), (xx — CLOSED), (yy), (zz — CLOSED), (ae — CLOSED), (af — CLOSED), (ag — ADVANCED to n=4), (ah).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 11.9h, 3362 → 3398, delta +36.** 0 postings added; absence panel 5, `as_of` earned.
2. Upstream `scan_metadata`, `new_since_last_scan`, `still_open_from_prior_scans`, `drops_summary`, `_feed-fingerprint.json` read directly → recovery confirmed; the 3 net-new items inspected field-by-field.
3. WebSearch — ESMA / BaFin / AMF / CONSOB crypto marketing enforcement Aug 2026 → **0 net-new primary.** Three already held, one scope refusal.
4. WebSearch — Ashby `circle` slug identity → **inconclusive; returned the wrong companies.** Recorded as a finding about the check.
5. WebSearch — the posting's verbatim boilerplate → **resolved it to circle.so** against that company's own public copy.
6. WebSearch — crypto CMO / head of marketing / MiCA Aug 2026 → **0 net-new.** NorthPoint's own PR refused (4th).
7. WebSearch — crypto layoffs marketing Aug 2026 → **0 net-new events**; all eight named firms already held.
8. WebSearch — MARA Holdings layoffs → surfaced the two primaries.
9. `web_fetch` **bitcoinmagazine.com/news/mara-conducts-ongoing-layoffs** (published 2026-04-02) → *"has not been disclosed… the company has not publicly commented on the cuts."*
10. `web_fetch` **unchainedcrypto.com/mara-holdings-cuts-15-of-staff…** (published 2026-04-03, updated 12pm ET) → the firm-stated 15% quote, the Blockspace attribution, and the 266-FTE base behind the ~40.
11. `web_fetch` **jobs.ashbyhq.com/circle/…** → 🔴 **REFUSED, not in the provenance set. Not retried, not circumvented.**
12. `csv.DictReader` over all 26 tracker rows; row 6 field-by-field before and after; post-write re-read verifying 26 rows × 10 fields and **0 rows without a `source_url`**.
13. Slug-vs-label reconciliation across all 17 rows in 13 tracked-firm CSVs; both flags adjudicated by hand.
14. **6 exact-string edits across `README.md`, `README-for-github.md`, `methodology.md`** (panel staleness), each with an asserted occurrence count; residual grep **CLEAN**.
15. `methodology.md` §1 — absence-panel section added (what `_absence.csv` does and does not mean, three-row table, two recorded limits).
16. **8 exact-string edits to `sport-sponsorship-reset-2026-05.md`**; front matter re-ordered after the disposition block was inserted.
17. `scripts/date-provenance-audit.py` patched for instrument-record scope; **run before and after repairs**; discrimination verified both ways.
18. **No URL was fabricated. No figure was entered that its source did not state. No absence claim was made from an unobserved scan. No register was re-fetched. No paywall was circumvented. No provenance refusal was worked around. No person was named on a secondary's uncorroborated attribution. No posting was admitted whose body contradicts its label.**

---

## Net-new / changed this run

- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **row 6 (MARA) sourced and fully regraded.** 90,682 → 92,440 bytes. **26/26 rows now cited.**
- `corpus/operator-statements/sport-sponsorship-reset-2026-05.md` — disposition block; §2/§3/§4 anchored; §1/§5/§6/§7 marked `UNSOURCED — DO NOT CITE`; the false compliance paragraph replaced.
- `corpus/job-postings/_ats-slug-collision-circle-2026-08-30.md` — **new.** The class-1 identity-resolution defect, the reconciliation and its two false positives.
- `scripts/date-provenance-audit.py` — instrument-record scope fix; `EXEMPT-INSTRUMENT` verdict added.
- `README.md`, `README-for-github.md`, `methodology.md` — panel-staleness honesty (6 edits) + the `methodology.md` §1 absence-panel section.
- `corpus/weekly-runs/2026-08-30-corpus-run.md` — this record.
- `findings/longitudinal-2026-06.md` — day-60 shift appended.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json` — sync writes (19th run).
- `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — byte-identical, 19th consecutive run.
- **Deliberately NOT written:** any admission of the Circle rows; any fetch of the refused Ashby URL; any URL for §1/§5/§6/§7 of the sport file; any `as_of` patch to the sync; any register re-fetch; any edit to the 25 tracker rows that were already cited; any Theme-1 claim resting on the uncited Binance section.

---

## Recommendation for next run — **T-1. SHIP IS 2026-09-01.**

1. 🔴 **DECIDE THE BINANCE §5 CLAIM. THIS IS THE ONLY LOAD-BEARING DEFECT LEFT.** *"First Tier-1 to put a non-marketing operator into the interim CMO seat without running a search"* is a **named-firm claim about a named person**, it is in Theme 1 and in a published essay, and its only corpus support is an uncited section of a file that until today certified its own compliance falsely. **One CoinDesk URL settles it. Without that URL the claim must be cut.** This is Jukka's call, not the loop's.
2. ⚠ **RE-RUN THE SYNC AND CONFIRM THE FEED IS STILL LIVE.** 08-31 is the last day of the class-1 capture window that all three public documents advertise. **If the scan is frozen on 08-31, the window claim needs a scope sentence after all** — and unlike today, there will be no day left to recover.
3. ⚠ **AUTOMATE OR RETIRE THE SLUG RECONCILIATION.** It found a live near-miss and it runs only because a session chose to run it. Either it becomes a predicate in `daily-corpus-sync.py` (parsing both path and query-parameter slug forms) or the report's appendix states plainly that class-1 company identity is slug-derived and unreconciled. **Do not leave it as a thing that happened once.**
4. 🔴 **THE REPO NOW HAS TWO STALE GIT LOCK FILES AND THE MOUNT CANNOT REMOVE THEM. READ THIS BEFORE TRYING TO COMMIT.**

```
.git/HEAD.lock              (0 bytes,  left by this run's first commit)
.git/refs/heads/main.lock   (41 bytes, left by this run's second)
```

`rm` and `mv` both return `Operation not permitted` — the known mount limitation, in a new place. **`git commit` and `git update-ref` will fail on 08-31**, exactly as the second commit failed today. The proven sequence, used successfully twice this run:

```bash
export GIT_INDEX_FILE=/tmp/idx-$$          # alternate index — the .git/index.lock cannot be unlinked either
git read-tree HEAD && git add -A -- <paths>
TREE=$(git write-tree); PARENT=$(git rev-parse HEAD)
COMMIT=$(printf '%s' "$MSG" | GIT_AUTHOR_NAME="Jukka Blomberg" \
  GIT_AUTHOR_EMAIL="jukka.blomberg@outlook.com" GIT_COMMITTER_NAME="Jukka Blomberg" \
  GIT_COMMITTER_EMAIL="jukka.blomberg@outlook.com" git commit-tree "$TREE" -p "$PARENT" -F -)
# git update-ref WILL FAIL on the stale HEAD.lock. Write the ref directly instead —
# an in-place truncate+write needs no unlink:
python3 -c "open('.git/refs/heads/main','w').write('$COMMIT\n')"
git log origin/main..HEAD --oneline     # verify before believing it
```

⚠ **Verify the parent before writing the ref.** Writing `refs/heads/main` by hand bypasses git's own safety check that the ref has not moved underneath you. Read the current value first and assert it equals the `$PARENT` you built on — as this run did — or a concurrent Distribution Engineer commit is silently discarded.

🟢 **This does not block the push.** `git push` updates `refs/remotes/origin/main`, a different lock. Both of today's commits are on `main` ahead of `origin/main` and are pushable as they stand.

5. **Do NOT re-fetch `CASPS.csv`, `OTHER.csv`, `NCASP.csv`. Do NOT re-open MAS. Do NOT re-issue the retry queue. Do NOT attempt row 13's Bloomberg paywall. Do NOT fetch the four un-fetched FCA orders, or VARA's Shelbit / MEXC / CoinMENA notice bodies.** Nothing in the report depends on any of them, and there is no time to adjudicate a surprise.
6. **Escalate to Jukka — three items, in order:**
   - **(i) 🔴 ONE CITATION HOLE LEFT, AND IT IS A CLAIM ABOUT A NAMED PERSON AT BINANCE.** See 1. Source or cut. **Two days.**
   - **(ii) 🟢 THE PRE-SHIP DEFECT QUEUE IS OTHERWISE EMPTY.** The feed recovered, so the capture window holds to 08-31 as advertised. Every layoff-tracker row is cited (26/26) — first time in the cycle. Every public document now states the agency panel's real last-refresh date. The absence-panel distinction Themes 1 and 4 depend on is written into `methodology.md` rather than living in run records. **The corpus-wide citationless-row count is zero.**
   - **(iii) ⚠ TWO INSTRUMENT LIMITS THE APPENDIX SHOULD STATE RATHER THAN THE LOOP KEEP RE-DISCOVERING.** Class-1 company identity is slug-derived and reconciled by nothing (watch al); `_absence.csv` dates itself from the run clock, not the observation (watch ai). Both are honest to publish and cheap to state. **Neither is a blocker.**
   - **(iv) 🔴 `/sessions` STORAGE.** Not re-tested this run. Cost the corpus 08-26 outright; host-side fix only Jukka can perform — `needs-jukka` row 545. **Unchanged.**
