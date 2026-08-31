# Corpus-assembly daily run — 2026-08-31 **(day 61 post-deadline · T-1 TO SHIP · LAST DAY OF THE CLASS-1 CAPTURE WINDOW)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-31 (**Monday — ships tomorrow, 2026-09-01**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-30 recommendations:** (1) 🔴 decide the Binance §5 claim — the only load-bearing defect left; (2) ⚠ re-run the sync and confirm the feed is still live on the window's final day; (3) ⚠ automate or retire the slug reconciliation; (4) 🔴 read the git-lock workaround before committing; (5) do **not** re-fetch `CASPS.csv` / `OTHER.csv` / `NCASP.csv`, re-open MAS, re-issue the retry queue, attempt row 13's Bloomberg paywall, or fetch the four un-fetched FCA orders / VARA's Shelbit, MEXC, CoinMENA notice bodies.
**Dedup baseline read before writing:** `2026-08-30-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`; `sport-sponsorship-reset-2026-05.md` in full; directory indexes for `regulator-filings/` (41), `operator-statements/` (9 → 10), `findings/` (5), `weekly-runs/` (60 → 61); upstream `scan_metadata`, `new_since_last_scan`, `still_open_from_prior_scans`, `drops_summary`, `fetch_errors` and `_feed-fingerprint.json` read directly; `queues/needs-jukka.md` row 735 read before acting on it.
**🟢 CADENCE (this loop): HELD.** 08-30 → 08-31 is a one-day step; **61 run records for 61 post-deadline days.**
**🟢 CADENCE (the upstream feed): HELD, unassisted.** See §1 — and this matters more today than on any other day of the cycle.

---

## Headline result

**The report's last uncited claim turned out to have a citation. Reading it destroyed the claim. That is the finding — not the anchor.**

### 1. 🔴⭐ **THE MISSING SOURCE EXISTED, AND IT REFUTES THE CLAIM IT WAS SUPPOSED TO SUPPORT.**

Row 735 of `needs-jukka.md` gave two options by today: **send the CoinDesk URL**, or reply **"cut it."** No reply arrived. The pre-declared default was *cut*. Before cutting, the loop did the cheap thing nobody had done in 110 days: **it looked for the article.**

It exists, it is exactly the scoop the file described, and it was fetched first-party:

> **https://www.coindesk.com/business/2026/05/12/binance-s-chief-marketing-officer-rachel-conlan-is-leaving-the-exchange**
> Ian Allison · edited by Sheldon Reback · CoinDesk · tagged `exclusive` · **published 2026-05-12 11:25 ET · publisher-modified 2026-05-19 10:18 ET**

**The claim under adjudication was:**

> *"First Tier-1 to put a non-marketing operator (wallet product CEO) into the interim CMO seat **without running a search**. The brief is being re-cut into a product-and-distribution job sitting where the marketing org used to sit."*

**What the article actually contains:**

| Limb | Verdict |
|---|---|
| Conlan exits; **last day 15 June 2026**; took the post **September 2023** | 🟢 **STATED** (the September 2023 date links to Binance's own leadership blog) |
| **Eowyn Chen, former CEO of Trust Wallet, is interim CMO** | 🟢 **STATED**, attributed to a Binance spokesperson by email |
| Conlan **stays on as an adviser** | 🟢 **STATED** |
| **"…without running a search"** | 🔴 **ABSENT.** The article says nothing about a search — not that one ran, not that one was skipped. No source in this corpus does |
| **"First Tier-1 to…"** | 🔴 **UNSUPPORTED.** No comparative claim anywhere. A "first" is an absence claim about every *other* Tier-1 firm and needs class-3/4 evidence for each |
| **"The brief is being re-cut into a product-and-distribution job"** | 🔴 **INFERENCE.** Nothing in the primary describes the interim brief at all |

**Action taken — the incident is anchored and three limbs are struck.**

- 🟢 **New class-4 capture:** `corpus/operator-statements/binance-conlan-cmo-exit-primary-2026-08-31.md` — verbatim quotes from Conlan *and* the Binance spokesperson, speaker, role-at-time, publication date, modification date. **It carries an explicit `**Published:**` field** — closing, on one file, the class-4 template gap `scripts/README.md` has flagged since 08-21 (five of eight class-4 files remain unauditable by any script).
- 🔴 **`sport-sponsorship-reset-2026-05.md` §5 rewritten.** The struck reading is left visible under strikethrough with the reason, so no future run restores it from the essay.
- 🟢 **Admissible replacement:** *Binance's CMO seat turned over in May–June 2026; the publicly named interim occupant's stated prior role is chief executive of a wallet business rather than a marketing seat; the departing CMO stayed on as an adviser; the firm's public framing of the exit is personal ("to focus on personal priorities"), not structural.* **Narrower, true, and cited.**

⚠ **The May 13 NorthPoint essay "Binance lost its CMO too" was built on the struck reading.** It is **published external content and is not editable from this corpus** — hard gate. Escalated to Jukka today as the only open item.

### 2. 🔴 **THE STRUCTURAL LESSON, AND IT OUTLIVES THIS REPORT: EVERY GUARD HERE CHECKS THAT A CITATION *EXISTS*. NONE CHECKS THAT IT *SAYS WHAT THE ROW CLAIMS*.**

`date-provenance-audit.py` now reports §5 as **`SELF-DATED`** — its cleanest verdict — and **that verdict would have been byte-identical had the article asserted the opposite of the claim.** The audit compares the URL's *path date* to the corpus's *recorded date*. It has no view of the article's *content*, and never did.

Every prior headline catch was a **presence** defect: MARA uncited (08-21); a file certifying its own compliance while citing seven outlets by name and none by URL (08-30). **This is the first *content* defect the cycle has produced, and it is the one the instrument suite is structurally blind to.**

> **Watch (vv) — *a number is not safe until someone has read its citation* — extends from numbers to CLAIMS.** The citation index the report ships certifies that a source exists and is correctly dated. **It does not certify that the source supports the sentence pointing at it.** The appendix should say so plainly; a reader who trusts the index deserves to know its scope.

### 3. 🔴 **A SEARCH-RESULT SUMMARY MANUFACTURED A FINDING THAT WOULD HAVE FLIPPED A RECORDED CORPUS RULING — VIA ADJACENCY, ONE STEP UPSTREAM OF ANY GUARD.**

The class-5 search returned, presented as a statement about **Coinbase**:

> *"…layoffs affecting roles within engineering, product and **marketing** teams."*

The corpus has recorded since 08-29 that **no source names marketing as an affected function at Coinbase** — a load-bearing absence in Theme 1 and in `theme-1-marketing-function-attrition-coinbase-openai.md`. Admitting this would have flipped it.

**Fetched the underlying page and read the lines around it.** The sentence is at **line 443** and belongs to **LinkedIn, quoting CEO Daniel Shapero**, sourced to Bloomberg. The **Coinbase section begins at line 445**. The summariser merged two adjacent sections of a chronological layoff-tracker page.

🟢 **THE 08-29 RULING STANDS, re-verified at source.** The Coinbase page states the 700-employee figure and Armstrong's "AI-Native pods" quote; **it names no marketing function.**

⚠ **This is the Kalifowitz error mechanism precisely** — framing migrating one section down a page and acquiring a source it never had — **except it occurred in the retrieval layer**, before anything in this repo can audit it. `verify-capture.py` watches register CSVs; `date-provenance-audit.py` watches admitted rows. **Nothing watches the summary that proposes a row.** New watch (am).

**Watch (ss) paid for itself for the second run running:** the item *confirmed* a plausible expectation (a 14% cut hitting marketing), which is exactly the class that gets the least scrutiny, and it was false.

### 4. 🟢 **THE CAPTURE WINDOW CLOSED HONEST ON ITS FINAL DAY — AND THIS TIME THE FEED RAN WITHOUT A HUMAN.**

```
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-30T21:45:51Z, age=14.3h,
  fingerprint total_jobs_fetched=3397, delta=-1 vs 2026-08-30 (3398))
  reason: age 14.3h, fingerprint delta -1
job postings ADDED: 0  firms: []
```

`scan_date` **2026-08-31**. `companies_scanned` **147** · `companies_via_api` **99** · `fetch_seconds` 12.6 — today's numbers, not a re-read. **Both predicates pass.**

🟢 **This was the open risk carried from 08-29 and re-flagged on 08-30**, where the recovery was a product-builder one-shot rather than a restored cadence. It did not need one today. `methodology.md` and both READMEs advertise a class-1 window of *"rolling 12 months ending August 31, 2026"* — **the window closes as advertised, on a scan that ran. No scope sentence is needed, and there was no day left to recover if it had been.**

> 🟢 **PERMITTED, and stated:** *no firm in the Stratum 1–4 cohort had a net-new marketing or growth posting observable through the ATS API scan of 2026-08-31.*
> 🔴 **STILL PROHIBITED:** any statement extending that to Binance, Bybit, HTX, KuCoin or Aave, which are not API-reachable and sit in `_absence.csv` for that reason.

### 5. ⚠ **A NEGATIVE FINGERPRINT DELTA IS NEW, AND THE GUARD HAS NEVER BEEN TESTED AGAINST ONE.**

`total_jobs_fetched` moved **3398 → 3397: delta −1.** Every prior delta in the series has been ≥ 0.

Predicate 2 refuses a delta of **exactly 0**. −1 is non-zero and passes — **right in intent**: postings close, attrition is genuine scan movement, and a shrinking total is evidence the scanner read a live board. But **"non-zero" and "the scan looked" are not the same predicate**, and −1 is one row away from a value a stale file could produce by losing a line. Age (14.3h) carries today's verdict independently, so **nothing in this run rests on it.**

**Not patched.** Changing a guard's predicate at T-1, on the last day of the capture window, to handle a case that did not bite, is the trade the 08-21 rule warns about. Recorded as **watch (an)** for whoever picks the instrument up after ship.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

```
date: 2026-08-31   source A (jobs) scan_date: 2026-08-31
FEED HEALTH: HEALTHY (age=14.3h, 3398 → 3397, delta=-1)
job postings ADDED: 0  firms: []   of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance','Bybit','HTX','Kucoin','Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave','Binance','Bybit','HTX','Kucoin']
```

Fingerprint series:

```
2151 → 2151(frozen) → 2186 → 2196 → 2259 → 2265 → 2263 ‖ 3334 → [no 08-26] → 3356 → 3362 → 3362(frozen) → 3398 → 3397
                                                          ↑ break                                                  ↑ TODAY (first NEGATIVE delta)
```

Upstream **`new_count` 0** — the scan ran and found nothing new anywhere, not merely nothing in the cohort. `total_jobs_after_filter` **45**, `still_open_count` **42**. `fetch_errors`: the same four stable 404s (Wormhole Foundation, Aave, Bitwise, Chainlink Labs) — unchanged for the eleventh run, which is itself the evidence they are structural and not transient.

**Watch (ag) — ADVANCED TO n=5, and it is the cycle's closing number.** `still_open_from_prior_scans` holds **OpenAI 12 · Anthropic 8 · Cohere 3 · Perplexity 2 = 25 open AI-lab marketing/comms roles** against **Gemini 1 · Phantom 1 = 2** for the entire Stratum 1–4 crypto cohort. ⚠ **Not a corpus entry** — AI labs are outside the cohort and no claim is made from them — but **25:2 on the final day of a twelve-month capture window is the sharpest form this observation has ever taken**, and Theme 2's read of *where marketing hiring actually went in 2026* is incomplete without it.

**Absence panel: 5 firms, membership unchanged since the cohort expansion.** `as_of` rolled to 2026-08-31 and **today it is earned** — a 2026-08-31 scan produced it. Watch (ai) remains dormant-not-fixed.

⚠ **Slug-vs-label reconciliation (recommendation 3 of 08-30): NOT automated, and NOT re-run.** Zero postings were added today, so there was nothing new to reconcile and re-running it would have re-verified the same 17 rows it cleared yesterday. **The recommendation is therefore neither honoured nor dischargeable by this run** — it is a build item, and it is carried to Jukka as an appendix-disclosure item instead (see below). Stated rather than quietly dropped.

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 77 days stale.** 18 agency-claims files written, **byte-identical for the twentieth consecutive run.** 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation. Watch (d) stays **CLOSED**: every public document now states the real last-refresh date, so the staleness is published rather than merely known.

### 3. Regulator — **0 NET-NEW.**

| Surfaced | Disposition |
|---|---|
| ESMA statement — unauthorised CASPs to wind down and **cease marketing activities and solicitation** | **ALREADY HELD** — captured at source (`esma-mica-transitional-period-end-2026-06.md`); the AMF mirror adds nothing |
| CONSOB → ESMA non-compliant register additions (Reversal Investment Group, Kortex) | **ALREADY HELD** — `esma-ncasp-post-deadline-composition-at-source-2026-08-23.md` + `_esma-ncasp-snapshot-2026-08-16.csv`, read at source. ⚠ Secondary coverage quotes **164** entries against our at-source **167**; **our register capture is the primary and stands.** Not adjudicated further — no claim depends on the delta |
| ESMA staff knowledge-and-competence guidelines (apply from 28 July) | 🔴 **REFUSED ON SCOPE**, second consecutive run. Staff competence, not marketing communications |
| **FCA v HTX — High Court stay listed to expire "late August"** | 🔴 **NULL CONFIRMED. Today is 31 August and no outcome is published.** Searched specifically for it; found only the same mid-August settlement-talks reporting the corpus already holds (`fca-htx-promotions-consent-order-stay-2026-08-28.md`). **Nothing guessed, nothing inferred from the calendar.** The report ships with the stay unresolved, which is the true state of the record |

**Watch (b) — NOT ADVANCED. The EU-NCA marketing-side enforcement null stands at day 61 — the last day of the corpus** — in its narrow form: *no EU national competent authority has published a named marketing-side enforcement action against a CASP since the MiCA transitional deadline.* The FCA/HTX action is UK s.21 FSMA and is excluded by its own record. **This null is one of the report's principal findings and it survived to ship intact.**

**Not fetched, not guessed:** `CASPS.csv`, `OTHER.csv`, `NCASP.csv`, MAS, the retry queue, the four un-fetched FCA orders, VARA's Shelbit / MEXC / CoinMENA notice bodies, `rulebooks.vara.ae`. **All 08-30 prohibitions honoured.**

### 4. Operator statements — 🟢 **+1 ADMITTED. First class-4 admission in seventeen runs.**

| Surfaced | Disposition |
|---|---|
| **CoinDesk — Binance CMO Rachel Conlan exit / Eowyn Chen interim (2026-05-12)** | 🟢 **ADMITTED.** Fetched first-party. Verbatim quotes from Conlan (CMO, tracked Tier-1 firm) and a Binance spokesperson. → `binance-conlan-cmo-exit-primary-2026-08-31.md` |
| **Ben Zhou (CEO, Bybit) — will not renew the F1 sponsorship, seeking "better commercial value"**, in the same article | 🔴 **REFUSED ON THE CLASS-4 ROLE GATE.** CEO, not CMO / VP Marketing / Head of Brand / Head of Growth. Same gate that excluded Travis McGhee. **Recorded inside the capture file** so a later run does not re-discover it and read the refusal as an oversight. It does **not** source §1 of the sport file, which stays `UNSOURCED — DO NOT CITE` |
| **NorthPoint's own press release** (natlawreview, 2026-08-14) | 🔴 **REFUSED — fifth consecutive run.** Our own promotional material; the author is not a tracked-firm operator |
| Vendor/consultancy MiCA explainers (Unit21, InnReg, Narvi, Coinmonks, Adam Smith, Surgence) | **REFUSED.** Secondary commentary; no tracked-firm operator speaks in any of them |

⭐ **The admission did not come from a new search.** It came from opening a citation the corpus had been describing for three months without reading. **The cheapest source of net-new class-4 material this cycle produced was the corpus's own footnotes.**

⚠ **Watch (l), 27th costing — WEAK, but weaker than usual in an instructive way.** Today's refusal set is valid at any §4 width **except** the Ben Zhou line, which a role gate one notch wider (CEO speaking *about marketing spend*) would have admitted. That is the first time in 27 costings the gate has excluded something with a direct Theme-2 bearing. **Escalation (v) is marginally strengthened** — noted, not acted on at T-1.

### 5. Layoffs — **0 NET-NEW EVENTS. Tracker holds at 26 rows, 26 citations.**

Search returned Crypto.com (row 1), Coinbase (row 4), FalconX (row 18) and the March-2026 cluster — **all held.** Three aggregators (CryptoJobsList, trueup, milkroad) not admitted, consistent with standing practice.

🔴 **One candidate refused after a source read — see headline 3.** The "Coinbase cut marketing" line belongs to LinkedIn. **Zero rows added; one recorded finding defended.**

### 6. NorthPoint longitudinal panel

Panel unchanged (77 days stale). **Day-61 shift appended to `findings/longitudinal-2026-06.md` — the final entry of the assembly cycle**, carrying items 1–3 above plus the closing window and cohort numbers.

---

## Guards run

| Guard | Result |
|---|---|
| `daily-corpus-sync.py` feed-health | 🟢 **HEALTHY**, both predicates pass, **unassisted**. Capture window closes as advertised. ⚠ First **negative** delta in the series — watch (an) |
| `verify-capture.py` | **Not run — correctly.** No register CSV was captured this run. Recorded, not silently skipped |
| `date-provenance-audit.py` | 🟢 **exit 0.** `EXEMPT-INSTRUMENT=1 · LAG-EXCEEDED=2 · NO-URL-DATE=14 · SELF-DATED=17 · UNPARSEABLE-DATE=1`. **Zero date inversions, zero citationless rows corpus-wide** — held for the second consecutive run |
| slug-vs-label reconciliation | **Not run — nothing to reconcile** (0 postings added). Not automated; carried as an appendix-disclosure item, not silently dropped |
| **first-party citation read (by hand, new)** | 🔴 **1 of 1 checked, 1 defect found.** The only citation opened for content this cycle contradicted three limbs of the claim citing it. **n=1 — this is a rate of nothing.** It is, however, the strongest argument the cycle has produced for the appendix stating what the citation index certifies |

⚠ **`SELF-DATED` still means the citation and the corpus agree on a date, not that either is right, and — as headline 2 establishes — not that the citation supports the claim.** 17 rows remain unaudited by the date predicate; **all 26 remain unaudited for content.** That is the work queue the report ships with, and the appendix should name it.

---

## Watch items

- **(b) First named post-deadline EU NCA marketing-side action** — **NOT ADVANCED. Null holds at day 61 and ships intact.**
- **(d) Agency panel staleness — 77 days** — 🟢 **CLOSED**, holding. Byte-identical twenty runs; published in every public document.
- **(e′) Cadence** — 🟢 **BOTH CLOCKS HELD, and the feed needed no help.** 61 records / 61 days.
- **(j) Senior-leader exits** — 🟢 **ADVANCED.** The Conlan→Chen transition is now a first-party capture rather than a described one. Seventeen runs of recall broken by reading, not searching.
- **(l) §4 too narrow** — **27th costing. WEAK, but the Ben Zhou refusal is the first with direct Theme-2 bearing.**
- **(n) Full-range re-sweep** — 🟢 **FIFTEENTH VINDICATION.** A claim survived 110 days because the file describing its source was read many times and **the source itself never once.**
- **(pp) A clean parse is not a complete capture** — 🟢 **HONOURED.** No absence claim from an unverified capture; none attempted.
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — 🟢 **PAID FORWARD, SECOND CONSECUTIVE RUN.** The "Coinbase cut marketing" line confirmed a plausible expectation and belonged to LinkedIn.
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — 🟢 **HONOURED BY INACTION.** The negative-delta case was recorded rather than patched at T-1.
- **(vv) A number is not safe until someone has read its citation** — 🔴 **EXTENDED TO CLAIMS, and it is the run's headline.** Eleven-for-eleven.
- **(ac) The fingerprint series is not one series** — 🟢 **EXERCISED.** Today's −1 is a genuine one-day step (08-30 → 08-31) and is recorded as such.
- **(ad) The absence panel has never contained an absence** — **UNCHANGED.** Permanent in `methodology.md` §1.
- **(ai) A derived file can date itself from the run clock** — **DORMANT, NOT FIXED.** Today's `as_of` is earned.
- **(ak) A captured primary is a snapshot of an artifact that keeps moving** — 🟢 **APPLIED DIRECTLY.** The CoinDesk article was **publisher-modified on 2026-05-19, seven days after publication, with no changelog.** The May 13 essay relied on a version nobody in this corpus ever captured. The capture file states this rather than presenting today's fetch as the May 12 text.
- **(al) A URL that resolves is not a company that matches** — **UNCHANGED, not re-tested** (0 postings added). Carried to the appendix.
- **🆕 (am) 🔴 A SEARCH-RESULT SUMMARY CAN MERGE TWO ADJACENT SECTIONS OF ONE PAGE AND ATTRIBUTE THE WRONG COMPANY.** The "Coinbase cut marketing" sentence was LinkedIn's, two lines up. **This is the Kalifowitz adjacency error occurring in the retrieval layer, upstream of every guard the repo owns.** `verify-capture.py` watches captures and `date-provenance-audit.py` watches admitted rows; **nothing watches the summary that proposes a row.** The only defence is fetching the page and reading the lines around the sentence — which is what happened, and it is not automatable at present.
- **🆕 (an) ⚠ A NEGATIVE FINGERPRINT DELTA PASSES A PREDICATE WRITTEN FOR A ZERO ONE.** −1 is genuine attrition and the verdict is right today, carried independently by the age predicate. But *non-zero* is not *the scan looked*. Untested territory; recorded for post-ship.
- **Unchanged and not re-narrated today:** (a), (c), (e), (f), (g), (h), (h′ — REJECTED), (i), (k), (m), (o), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (ab — CLOSED), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (mm), (nn), (oo), (qq), (rr), (uu), (ww), (xx — CLOSED), (yy), (zz — CLOSED), (ae — CLOSED), (af — CLOSED), (ag — ADVANCED to n=5), (ah), (aj).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.3h, 3398 → 3397, delta −1.** 0 postings added; absence panel 5; `as_of` earned.
2. Upstream `scan_metadata`, `new_since_last_scan` (**empty**), `still_open_from_prior_scans`, `drops_summary`, `fetch_errors`, `_feed-fingerprint.json` read directly → window-close confirmed on a live scan.
3. `queues/needs-jukka.md` row 735 read in full before acting on it — **no reply present; the pre-declared default applied.**
4. WebSearch — ESMA / BaFin / AMF / CONSOB crypto marketing enforcement Aug 2026 → **0 net-new primary.** Three already held, one scope refusal.
5. WebSearch — **CoinDesk Binance Conlan / Eowyn Chen May 2026** → located the scoop the corpus had described since May.
6. `web_fetch` **coindesk.com/business/2026/05/12/binance-s-chief-marketing-officer-rachel-conlan-is-leaving-the-exchange** → 🟢 **first-party capture.** Verbatim quotes, September-2023 start, 15-June exit, adviser transition, publisher-modified 2026-05-19 — **and no mention of a search, no comparative claim, no description of the brief.**
7. WebSearch — crypto CMO / head of marketing / MiCA Aug 2026 → **0 net-new.** NorthPoint's own PR refused (5th).
8. WebSearch — crypto layoffs marketing Aug 2026 → **0 net-new events**; surfaced the false Coinbase-marketing line.
9. `web_fetch` **informationweek.com/it-staffing-careers/2026-tech-company-layoffs** → read the lines around the sentence: **line 443 is LinkedIn / Daniel Shapero; the Coinbase section starts at line 445.** Candidate refused; the 08-29 ruling re-verified.
10. WebSearch — **FCA / HTX High Court stay outcome, late August 2026** → **no outcome published.** Null recorded, nothing inferred from the calendar.
11. `python3 scripts/date-provenance-audit.py` → **exit 0**, zero citationless rows, zero inversions.
12. **No URL was fabricated. No figure was entered that its source did not state. No absence claim was made from an unobserved scan. No register was re-fetched. No paywall was circumvented. No published external content was edited. No claim was left standing that its own citation contradicts.**

---

## Net-new / changed this run

- `corpus/operator-statements/binance-conlan-cmo-exit-primary-2026-08-31.md` — **NEW. +1 class-4.** Full primary capture with verbatim quotes, speaker, role-at-time, publication **and** modification dates, an explicit "what the primary does NOT state" table, and the Ben Zhou role-gate refusal recorded in place.
- `corpus/operator-statements/sport-sponsorship-reset-2026-05.md` — **§5 SOURCED AND SPLIT.** Incident anchored; three Theme-1 limbs struck under strikethrough with reasons; disposition block and header provenance updated from "three of seven anchored" to **four of seven**.
- `findings/longitudinal-2026-06.md` — the in-window Conlan/Chen confirmation line re-anchored and its old reading marked cut; **day-61 entry appended** (7 items — the closing entry of the assembly cycle).
- `corpus/weekly-runs/2026-08-31-corpus-run.md` — this record. **61st consecutive.**
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json` — sync writes (20th run).
- `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — byte-identical, 20th consecutive run.
- **Deliberately NOT written:** any edit to the published May 13 essay (external, hard-gated); any patch to the fingerprint predicate at T-1; any admission of the LinkedIn-sourced Coinbase line; any FCA/HTX outcome inferred from the stay's expiry; any re-run of the slug reconciliation against zero new rows; any register re-fetch.

---

## For Jukka — **SHIP IS TOMORROW, 2026-09-01.**

1. 🟢 **THE PRE-SHIP DEFECT QUEUE IS EMPTY. THE CORPUS IS SHIPPABLE.** Sixty-one consecutive daily records; the class-1 capture window closed **on 2026-08-31 exactly as all three public documents advertise, on a scan that genuinely ran**; corpus-wide citationless rows **zero**; 26/26 layoff rows cited; the EU-NCA marketing-enforcement null — a principal finding — **intact at day 61**.
2. 🔴 **ONE ITEM NEEDS YOUR HAND, AND IT IS OUTSIDE THIS REPO.** Row 735 is **resolved in the corpus**: the CoinDesk URL was found, fetched, and it **does not support** *"without running a search"*, *"first Tier-1"*, or the re-cut-brief reading. All three are cut; the incident is anchored. **But the May 13 essay "Binance lost its CMO too" is published on northpoint.fi and states the struck reading about a named person at a named firm.** Agents do not edit published content. **Your options are to amend the essay, append a correction note, or leave it and accept that the report and the essay now disagree** — the report being the more defensible of the two. Filed as a `needs-jukka` row today.
3. ⚠ **TWO SENTENCES THE APPENDIX SHOULD CARRY, both honest and both cheap.** (a) **What the citation index certifies:** that a source exists and its date is consistent — **not that it supports the sentence citing it.** Today is the proof, and a regulator-readable appendix that overstates its own warrant is the exact defect this report documents in other people's estates. (b) **Class-1 company identity is slug-derived and reconciled by nothing** (watch al), and **`_absence.csv` dates itself from the run clock** (watch ai). Neither is a blocker; both are better published than re-discovered.
4. ⚠ **ONE OBSERVATION THEME 2 SHOULD NOT SHIP WITHOUT.** On the final day of a twelve-month capture window, the feed holds **25 open marketing/comms roles at four AI labs against 2 across the entire 27-firm crypto cohort.** The labs are outside the cohort and **no claim is made from them** — but a report about where the crypto marketing function went in 2026 that omits where the hiring went is answering half its own question.
5. **Post-ship, not now:** patch the fingerprint predicate for negative deltas (watch an); automate the slug reconciliation or publish its absence (watch al); add a machine-readable `**Published:**` field to the remaining five class-4 files (today's new capture has one). **None of these blocks tomorrow.**
