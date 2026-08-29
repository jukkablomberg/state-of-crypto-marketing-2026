# Corpus-assembly daily run — 2026-08-29 **(day 59 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-29 (**Saturday — T-3 to ship**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-28 recommendations:** (1) 🔴 fix the README's Friday promise; (2) 🔴 fix the two countable README defects; (3) ⚠ decide the absence-panel sentence; (4) do **not** re-fetch `CASPS.csv` / `OTHER.csv` / `NCASP.csv`, re-open MAS, re-issue the retry queue, attempt row 13's Bloomberg paywall, or fetch the four un-fetched FCA orders; (5) four escalations to Jukka.
**Dedup baseline read before writing:** `2026-08-28-corpus-run.md` in full; `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; both READMEs at every line touched; all 26 tracker rows via `csv.DictReader`; directory indexes for `regulator-filings/` (41), `operator-statements/` (9), `layoff-tracker/` (14), `findings/` (5), `weekly-runs/` (58); `vara-enforcement-register-at-source-2026-08-14.md` in full; grep sweeps for `peken`, `mexc`, `MX Global`, `thirty firms`, `every Friday`, `Gemini -30%`, `corpus/regulator/`, `30 tracked firms`.
**🟢 CADENCE (this loop): HELD.** 08-28 → 08-29 is a one-day step; 59 run records for 59 post-deadline days.
**🔴 CADENCE (the upstream feed): BROKEN.** See §1.

---

## Headline result

**The deterministic half of the corpus went blind overnight, and the run's honest output is a refusal plus the repair the last three run records asked for and did not get.**

### 1. 🔴 **THE UPSTREAM ATS SCAN DID NOT RUN. CLASS 1 IS UNOBSERVED, NOT ABSENT — AND BOTH GUARD PREDICATES FAILED TOGETHER FOR THE FIRST TIME.**

```
FEED HEALTH: STALE (scanned_at_utc=2026-08-27T21:49:06Z, age=38.3h,
  fingerprint total_jobs_fetched=3362, delta=+0 vs 2026-08-28 (3362))
  reason: scan age 38.3h exceeds 36h
  !! CLASS-1 ABSENCE CLAIM REFUSED
```

`open-positions.json` still carries **`scan_date: 2026-08-28`** and the identical `scanned_at_utc`. The file the sync read today **is byte-for-byte the file it read yesterday.** Age 38.3h fails predicate 1; delta +0 across a calendar-date boundary fails predicate 2.

**This is the guard's third real catch and its first double failure.** On 2026-08-05 only the age predicate existed and a ~66h freeze nearly published an unearned absence. On 2026-08-13 the two halves *disagreed* (age HEALTHY, fingerprint frozen) and the run had to be adjudicated by hand. **Today they agree, and the guard made the ruling itself with no human adjudication.** The 08-14 enforcement change is what turns today from an incident into a routine refusal.

> 🔴 **PROHIBITED, in these exact words:** *"the cohort posted no marketing roles on 2026-08-29"*, *"class 1 produced nothing"*, and any count of tracked firms absent from the scan today.
> 🟢 **PERMITTED:** *the corpus loop ran; its upstream job-postings feed did not; class 1 is **unobserved** for 2026-08-29.*

**⭐ And the absence panel inherits the defect.** `_absence.csv` diffs on **`as_of` only** — Aave, Binance ×2, Bybit, HTX, KuCoin, identical rows, date rolled 08-28 → 08-29. **The file now asserts a 2026-08-29 observation that no 2026-08-29 scan produced.** This is watch (ad) in a sharper form than Arbitrum's two-day entry/exit: yesterday the panel was unstable, today it is *dated to a day it did not observe*. The sync writes `as_of` from the run clock, not from `scan_date`. **Recorded as a defect; deliberately not patched three days from ship (watch tt).**

### 2. 🟢 **THE README DEFECTS ARE FIXED. TWENTY-ONE EXACT-STRING EDITS ACROSS THREE FILES — THE LAST CHEAP WIN, TAKEN.**

Recommendations 1 and 2 of the 08-28 record had been restated for three consecutive runs on a **public** repo. Every one is now closed, by targeted replacement with an asserted occurrence count per edit (no wholesale rewrite, no splice):

| Defect | Was | Now |
|---|---|---|
| 🔴 **Cohort count** | *"across thirty firms"*; *"cohort (~30)"*; *"across 30 tracked firms"* | **27 named** — verified by counting `tracked-firms.md`: 11 + 8 + 5 + 3 = 27 |
| 🔴 **Gemini figure** | *"Gemini -30%"* in **both READMEs and `methodology.md`** | **-25% firm-stated/SEC-filed** — tracker row 2 says verbatim *"THE '-30% YTD' IS STRUCK… DO NOT PRINT -30%"* |
| 🔴 **Class-5 framing** | *"every public 2026 **marketing-team** contraction"* | *"workforce contraction… marketing-specific impact **where the firm or press states it**"* + an explicit note that most 2026 crypto cuts are company-wide |
| 🔴 **Friday promise** | *"nominations are read every Friday"*; *"the corpus updates here every Friday"* | *"read on the next daily corpus run"*; *"updates here **daily** — see `corpus/weekly-runs/`"* |
| ⚠ **Nomination reality** | silent | `methodology.md` now records the limit: **the loop has no mailbox access and no nomination has ever been read by it** |
| ⚠ **Wrong paths** | `corpus/regulator/`, `corpus/layoff-tracker.csv` | `corpus/regulator-filings/`, `corpus/layoff-tracker/2026-layoff-tracker.csv` |

**The Gemini one is the material fix.** The public README printed a figure the corpus had explicitly struck as unprintable — a hostile reader could have set the README against the tracker in ninety seconds and found NorthPoint contradicting its own evidence on a named firm's SEC filing. **Three days before ship.**

⚠ **Not touched, deliberately:** Block, Inc. is still advertised nowhere despite being the tracker's best-graded AI-cover row. Adding it is an editorial choice, not a defect repair, and it is not this loop's call three days out.

### 3. 🔴 **A FALSE ITEM THAT CONFIRMED THE THESIS, CAUGHT — WATCH (ss), AGAIN, ON CLASS 5.**

A class-5 search returned, as current, that *"Coinbase plans on reducing its headcount by 700 employees, with CEO **Daniel Shapero** saying the layoffs will affect roles within engineering, product and **marketing** teams."*

Three defects, all disqualifying:

1. **Not net-new.** It is tracker **row 4** — Coinbase, **2026-05-05**, `~700`, `-14%`. A 116-day-old event re-presented as August news.
2. **The name is wrong.** Coinbase's CEO is **Brian Armstrong**. Daniel Shapero is LinkedIn's COO. The attribution is fabricated somewhere in the secondary chain.
3. **"Marketing teams" is unsupported.** Row 4's own notes, drawn from the Armstrong memo, name *pure managers*, *AI-native pods* and a 5-layer cap. A follow-up search confirmed the affected functions as *"engineers, designers, and product managers"*. **No primary names marketing as an affected function at Coinbase.**

**This is the exact shape watch (ss) predicts: an item that confirms what Theme 1 wants to be true gets less scrutiny than a surprising one.** A marketing-named Tier-1 cut is the single most citable class-5 object the report could acquire, which is precisely why it was checked hardest. **Refused. Tracker untouched.**

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

```
date: 2026-08-29   source A (jobs) scan_date: 2026-08-28   ← FROZEN
FEED HEALTH: STALE (scanned_at_utc=2026-08-27T21:49:06Z, age=38.3h,
  fingerprint total_jobs_fetched=3362, delta=+0 vs 2026-08-28 (3362))
  reason: scan age 38.3h exceeds 36h
  !! CLASS-1 ABSENCE CLAIM REFUSED
job postings ADDED: 0  firms: []
chrome work-queue (proprietary tracked firms): ['Binance','Bybit','HTX','Kucoin','Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave','Binance','Bybit','HTX','Kucoin']
```

Fingerprint series:

```
2151 → 2151(frozen) → 2186 → 2196 → 2259 → 2265 → 2263 ‖ 3334 → [no 08-26] → 3356 → 3362 → 3362(frozen)
                                                          ↑ break                          ↑ TODAY
```

`companies_scanned` **147**, `companies_via_api` **99**, `companies_via_chrome_pending` **48** — unchanged, but **these are 08-28's numbers, not today's**, and are recorded as such. `fetch_errors` are the same four stable 404s (Wormhole, Aave, Bitwise, Chainlink Labs); `new_count: 2` is 08-28's Anthropic + OpenAI pair, **already counted yesterday and not re-counted today.**

**Watch (ag) — CANNOT BE ADVANCED.** The AI-lab posting pattern needs a third *observation*, and today produced none. n stays 3.

**Absence panel: 5 firms, membership unchanged, `as_of` rolled without an observation.** See headline 1.

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 75 days stale.** 18 agency-claims files written, **byte-identical for the eighteenth consecutive run.** 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation.

🟢 **Watch (d), 24th run — PARTIALLY RESOLVED TODAY.** `methodology.md` §6 still calls this a *"daily 18-agency panel"*, but the READMEs' *"refreshed daily"* line is now the only remaining overstatement, and the far more visible Friday/count/Gemini claims are fixed. ⚠ The §6 wording was **left alone deliberately**: it is a description of the intended feed, and rewriting the source-class definition three days from ship is a larger edit than a defect repair. **Escalated, not executed.**

### 3. Regulator — **0 NET-NEW. All candidates held or refused on scope.**

| Surfaced | Disposition |
|---|---|
| **CONSOB warnings on crypto finfluencers, amplifying ESMA's factsheet** | **ALREADY HELD** — `esma-finfluencer-factsheet-consob-amplification-CANDIDATE-2026-08-11.md` and `esma-finfluencers-factsheet-at-source-2026-08-22.md` |
| **Joint AMF / FMA / CONSOB call for a stronger European framework** | 🔴 **REFUSED ON SCOPE — third time.** Supervisory architecture, not a marketing-side enforcement action |
| **VARA Notices of Fines — Peken Global (KuCoin), MX Global (MEXC)** | **ALREADY HELD** — `vara-enforcement-register-at-source-2026-08-14.md` §3, where the KuCoin fine is read honestly as a **licensing** charge, not a marketing charge |
| **CySEC on-site audit / enforcement initiative, 2H2026–1H2027** | **REFUSED ON SCOPE.** A supervisory programme, forward-dated, naming no firm and no promotion |
| **Latham & Watkins commentary on the FCA's first crypto-marketing enforcement action** | **SECONDARY ON A HELD PRIMARY.** The FCA/HTX matter was captured at source on 08-28 from `fca.org.uk` including the sealed consent order. Law-firm commentary adds nothing the primary does not carry, and `methodology.md` prefers the primary |

**Watch (b) — NOT ADVANCED. The day-59 EU-NCA marketing-side enforcement null stands**, in its correctly narrowed form: *no EU national competent authority has published a named marketing-side enforcement action against a CASP since the MiCA transitional deadline.* The FCA/HTX action is UK s.21 FSMA and is excluded by its own record.

**Not fetched, not guessed:** `CASPS.csv`, `OTHER.csv`, `NCASP.csv`, MAS, the retry queue, the four un-fetched FCA orders, the MEXC/CoinMENA/Shelbit notice bodies, `rulebooks.vara.ae`. **All five 08-28 prohibitions honoured.**

⚠ **Named next objects, still un-fetched and recorded so they are not re-discovered:** VARA's **Shelbit General Trading Notice of Fines, 24 Jul 2026** — the register's only post-MiCA-deadline-dated VARA notice of any kind — and the **MEXC Notice of Fines, 22 Jun 2026**. Neither firm is in the cohort; neither is worth a fetch three days out.

### 4. Operator statements — **0 NET-NEW. FIFTEENTH consecutive recall confirmation.**

| Surfaced | Disposition |
|---|---|
| **NorthPoint's own press release** (natlawreview) | 🔴 **REFUSED — third consecutive run.** Our own promotional material; the author is not a tracked-firm operator. A report that cited its own publisher as a corpus source would deserve everything it got |
| **Marie Tatibouet, CMO, Gate.io** (Coinbound podcast) | **REFUSED — non-cohort.** Gate.io is not in Stratum 1–4 |
| **Brett Li, VP Marketing, Flipside** (2026-03-11) | **REFUSED — non-cohort**, and the episode predates the capture focus |

⚠ **Watch (l), 25th costing — WEAK.** All three refusals are cohort or self-citation refusals valid at any §4 width. **Escalation (v) is not strengthened.**

**+0 admitted.**

### 5. Layoffs — **0 NET-NEW EVENTS. TRACKER UNTOUCHED — 26 rows, 10 fields, byte-identical.**

Search returned Crypto.com (row 1), Gemini (row 2), Coinbase (row 4), FalconX (row 18), CryptoJobsList, layoffhedge, trueup, InformationWeek — **all held or aggregators.** The one apparently-new item was the Coinbase/"marketing teams" claim of headline 3: **refused on three independent grounds.**

🔴 **Row 6 (MARA) remains unlabelled, uncited, and flagged to STRIKE at ship.** Adjudicable denominator **25**.

### 6. NorthPoint longitudinal panel

Panel unchanged (75 days stale). Day-59 shift appended to `findings/longitudinal-2026-06.md`.

---

## Guards run

| Guard | Result |
|---|---|
| `daily-corpus-sync.py` feed-health | 🔴 **STALE, both predicates failed. Class-1 absence claim refused.** First double failure; first fully automatic adjudication |
| `verify-capture.py` | **Not run — correctly.** No register CSV was captured this run. Running it over unchanged stored snapshots to reprint an unchanged verdict is the "builders not scanners" failure |
| `date-provenance-audit.py` | **Run. Exit 1.** Class 5: `SELF-DATED` 17 · `NO-URL-DATE` 13 · `NO-URL` 3 · `LAG-EXCEEDED` 2. Class 4: `NO-PUBDATE-FIELD`/`NO-URL-DATE` 5 · `NO-URL` 2 · `LAG-EXCEEDED` 1 · `SELF-DATED` 1. **Unchanged from 08-27** — both files are untouched, and the verdict is recorded as a re-confirmation, not a new finding |

🔴 **Three rows still cannot corroborate their own date from their citation, and `sport-sponsorship-reset-2026-05.md` still carries no URL at all** — a class-4 file violating `methodology.md`'s own class-4 storage rule, three days from ship.

---

## Watch items

- **(b) First named post-deadline EU NCA marketing-side action** — **NOT ADVANCED.** Null holds at day 59.
- **(d) Agency panel staleness — 75 days**, byte-identical eighteen runs. 🟢 **Partially resolved:** the public-facing overstatements are fixed; `methodology.md` §6 is not. Escalated.
- **(e′) Cadence** — 🟢 **This loop held (one-day step).** 🔴 **The upstream feed did not.** These are different clocks and today separated them.
- **(i) `web_fetch` provenance refusals** — **NOT EXERCISED.** No fetch was required; every class-3 candidate was already held or refused on scope.
- **(j) Senior-leader exits** — **NOT ADVANCED.** Fifteen consecutive runs.
- **(l) §4 too narrow** — **25th costing, WEAK.** All refusals valid at any width.
- **(n) Full-range re-sweep** — 🟢 **THIRTEENTH VINDICATION.** The Gemini -30% defect was found by re-reading a file the repo has held since June against a tracker row written in February.
- **(pp) A clean parse is not a complete capture** — 🟢 **HONOURED.** No absence claim from an unverified capture; none attempted.
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — 🔴 **PAID, AND EXPENSIVELY.** See headline 3. A wrong CEO name and an unsupported "marketing teams" attribution on the report's most citable possible class-5 object.
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — 🟢 **HONOURED.** The `as_of`-without-observation defect in `_absence.csv` was diagnosed and **deliberately not patched** three days from ship.
- **(vv) A number is not safe until someone has read its citation** — 🟢 **NINE-FOR-NINE.** The public README's `-30%` was unsafe for months precisely because nobody had read it against row 2.
- **(ac) The fingerprint series is not one series** — **NOT EXERCISED.** No new observation to compare.
- **(ad) The absence panel has never contained an absence** — 🔴 **WORSENED.** It now carries a date it did not observe. Prohibitions unchanged and already at full width.
- **(ae) The cohort is 27 named firms; both READMEs say thirty** — 🟢 **CLOSED.** Both READMEs and `methodology.md` now say 27.
- **(ah) A regulator's own change log omitted a change** — **NOT EXERCISED.** No regulator page dated this run.
- **🆕 (ai) 🔴 A DERIVED FILE CAN DATE ITSELF FROM THE RUN CLOCK RATHER THAN THE OBSERVATION.** `_absence.csv`'s `as_of` comes from the sync's clock, not `scan_date`. When the feed freezes, the file silently asserts an observation that did not happen. **Generalise before ship: any corpus file carrying a date must date itself from the artifact, not from the run.** Same family as the 08-21 `Captured:`-line bug in `date-provenance-audit.py`.
- **🆕 (aj) ⚠ A SECONDARY CHAIN INVENTED A NAMED CEO.** The Coinbase item attributed a quote to a person who does not hold the role. **Any operator attribution surfaced by search, not by a first-party fetch, must have its speaker's role verified independently before admission** — this is `§4`'s role gate applied to class 5.
- **Unchanged and not re-narrated today:** (a), (c), (e), (f), (g), (h), (h′ — REJECTED), (k), (m), (o), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (ab — CLOSED), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (mm), (nn), (oo), (qq), (rr), (uu), (ww), (xx — CLOSED), (yy), (zz — CLOSED), (af — CLOSED), (ag — frozen).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **STALE, age 38.3h, 3362 → 3362, delta +0. CLASS-1 ABSENCE CLAIM REFUSED.** 0 postings added; absence panel 5, `as_of` rolled without an observation.
2. Upstream `scan_metadata` / `fetch_errors` / `_feed-fingerprint.json` read directly → confirmed `scan_date` **2026-08-28** and an identical `scanned_at_utc`. The freeze is upstream, not in the sync.
3. WebSearch — ESMA / BaFin / AMF / CONSOB crypto marketing enforcement Aug 2026 → **0 net-new primary.** Two scope refusals, one repeat.
4. WebSearch — CySEC / AFM / VARA / MAS crypto advertising enforcement late Aug 2026 → **0 net-new.** VARA KuCoin/MEXC items verified as already held by reading the 08-14 record in full.
5. WebSearch — crypto CMO / head of marketing / MiCA Aug 2026 → **0 net-new.** NorthPoint's own PR refused (3rd), Gate.io and Flipside refused on cohort.
6. WebSearch — crypto layoffs marketing Aug 2026 → surfaced the Coinbase/"marketing teams" item.
7. WebSearch — Coinbase 700 layoffs, functions affected → **disproved it.** Same 2026-05-05 event as row 4; affected functions are engineering, design, product; the CEO name in the first summary is wrong.
8. `csv.DictReader` over all 26 tracker rows; row 4 read field-by-field.
9. `grep -ril` sweeps for `peken`/`mexc`/`MX Global` across `corpus/` and `findings/` → 21 files, all pre-existing.
10. **21 exact-string edits across `README.md`, `README-for-github.md`, `methodology.md`**, each with an asserted occurrence count, then a residual-defect grep confirming **CLEAN**.
11. `python3 scripts/date-provenance-audit.py` → **exit 1**, verdict unchanged from 08-27.
12. `python3 scripts/verify-capture.py` **deliberately not run** — no capture this run. Recorded, not silently skipped.
13. **No URL was fabricated. No figure was entered that its source did not state. No absence claim was made from an unobserved scan. No register was re-fetched. No paywall was circumvented. No tracker row was edited. No person was named on a secondary's uncorroborated attribution.**

---

## Net-new / changed this run

- `README.md`, `README-for-github.md`, `methodology.md` — **the defect repair.** Cohort count 30 → **27 named**; `Gemini -30%` → **-25% firm-stated/SEC-filed**; class-5 framing corrected from *"marketing-team contraction"* to *"workforce contraction… marketing-specific impact where stated"*; the Friday promise replaced with the daily reality plus the recorded mailbox limit; two wrong storage paths fixed. **Closes watch (ae) and recommendations 1 and 2 of 08-28.**
- `corpus/weekly-runs/2026-08-29-corpus-run.md` — this record.
- `findings/longitudinal-2026-06.md` — day-59 shift appended.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json` — sync writes (18th run). **The `_absence.csv` diff is `as_of` only and is a recorded defect, not an observation.**
- `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — byte-identical, 18th consecutive run.
- **Deliberately NOT written:** any class-1 absence claim; any edit to the layoff tracker; any admission of the Coinbase "marketing teams" item; any `as_of` patch to the sync; any rewrite of `methodology.md` §6's "daily panel" description; any addition of Block, Inc. to the READMEs' advertised examples; any register re-fetch; any new guard.

---

## Recommendation for next run

1. **🔴 CHECK THE UPSTREAM ATS SCAN BEFORE ANYTHING ELSE.** If `scan_date` is still `2026-08-28` on 08-30, class 1 will have been unobserved for **two of the last three days before ship**, and the report's class-1 coverage claim needs a scope sentence: *"job-postings coverage runs to 2026-08-27."* **The sync cannot fix this; the feed has to run.**
2. **⚠ DECIDE THE ABSENCE-PANEL SENTENCE — FIFTH RESTATEMENT, AND TODAY MADE IT WORSE.** The panel is now demonstrably capable of asserting a date it did not observe. `methodology.md` §1 needs one paragraph distinguishing *firm silence* from *scanner reach on the day of the scan*, or Themes 1 and 4 inherit a claim the corpus cannot support. **Theme 4's findings file was deliberately written not to depend on it — so this is a methodology defect, not a blocker.**
3. **⚠ `methodology.md` §6 STILL SAYS "DAILY 18-AGENCY PANEL". IT IS 75 DAYS STALE.** The public READMEs are fixed; this one is not. It is one sentence — *"an 18-agency panel, last refreshed 2026-06-15"* — and it is the last uncorrected overstatement in a public document.
4. **⚠ `sport-sponsorship-reset-2026-05.md` HAS NO URL.** A class-4 file that violates the class-4 storage rule, in a report whose entire argument is *"either there is a citation, or the claim is omitted."* **Either source it or strike it before ship.** Same for tracker row 6 (MARA).
5. **Do NOT re-fetch `CASPS.csv`, `OTHER.csv`, `NCASP.csv`. Do NOT re-open MAS. Do NOT re-issue the retry queue. Do NOT attempt row 13's Bloomberg paywall. Do NOT fetch the four un-fetched FCA orders, or VARA's Shelbit/MEXC/CoinMENA notice bodies.** Nothing in the report depends on any of them.
6. **Escalate to Jukka — four items, in order:**
   - **(i) 🔴 THE JOB-POSTINGS FEED IS DOWN, THREE DAYS FROM SHIP.** The scan has not run since 2026-08-27 21:49 UTC. The guard caught it and refused the absence claim — that part worked. **But if it stays down, class 1's capture window ends 08-27, not 08-31 as both READMEs and `methodology.md` state.** That is a fourth countable defect in a public document, and unlike today's three it cannot be fixed by editing text.
   - **(ii) 🟢 THE README DEFECTS ARE CLOSED.** Cohort count, the struck Gemini figure, the class-5 framing, the Friday promise, two wrong paths — **21 edits, all committed, all verifiable by grep.** The public repo no longer contradicts its own corpus on a named firm's SEC-filed figure.
   - **(iii) ⚠ TWO CITATION HOLES REMAIN AND BOTH ARE THE REPORT'S OWN STATED RULE.** `sport-sponsorship-reset-2026-05.md` (no URL) and tracker row 6 / MARA (no URL). **Strike or source. Three days.**
   - **(iv) 🔴 `/sessions` STORAGE.** Not re-tested this run. It cost the corpus 08-26 outright and remains a host-side fix only Jukka can perform — `needs-jukka` row 545.
