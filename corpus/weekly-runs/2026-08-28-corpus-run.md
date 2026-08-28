# Corpus-assembly daily run — 2026-08-28 **(day 58 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-28 (**Friday — the last Friday before ship**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-27 recommendations:** (1) 🔴 **inventory every stored register snapshot by FIELD, not by file** — new watch (af); (2) 🔴 **write the Theme-4 paragraph**; (3) ⚠ decide the absence-panel sentence; (4) do **not** re-fetch `CASPS.csv`, `OTHER.csv`, `NCASP.csv`, re-open MAS, re-issue the retry queue, or attempt row 13's Bloomberg paywall; (5) five escalations to Jukka.
**Dedup baseline read before writing:** `2026-08-27-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`, `corpus/README.md` in full; all 26 tracker rows via `csv.DictReader`; `situation.md` head + RECENT DECISIONS; directory indexes for `regulator-filings/`, `operator-statements/`, `job-postings/`, `layoff-tracker/`, `findings/`; grep sweeps for `ae_website_platform`, `serviceCode_cou`, `passport`, `ae_reason`, `MEXC`, `artzz`, `ae_infrigment`, `bitget`, `falconx`, `htx`.
**🟢 CADENCE: RESTORED.** 08-27 → 08-28 is a **one-day** step. The fingerprint comparison is against 2026-08-27 and `_feed-fingerprint.json` carries an 08-28 entry. **Watch (e′) recovers to 10 of 12.** ⚠ `/sessions` still reports **100% used, 0 bytes free** in this run's sandbox — the condition that ate 08-26 is unfixed; today survived it.

---

## Headline result

**Both blocking mandates executed, and for the second consecutive day the run's biggest finding came from reading a file the repo already held. But the day's sharpest artifact came from the web after all — a sealed High Court consent order, published by the FCA two days ago, in which the marketing function is a named defendant class.**

### 1. ⭐⭐ 🔴 **A REGULATOR IS SUING THE MARKETING FUNCTION AS AN UNIDENTIFIED LEGAL PERSON — AND THE STAY EXPIRES SEVEN DAYS AFTER SHIP.**

**FCA v Huobi Global S.A. & Others**, Chancery Division, claim issued **21 October 2025**. **HTX is a Stratum-1 tracked firm** and the one the 08-17 register record called *"the sharpest open question in the cohort."*

**The fourth defendant is a marketing function**, verbatim from the sealed order:

> *"(4) PERSONS UNKNOWN (who are the persons currently in control of promotions on behalf of the HTX Exchange on any of the following social media platforms and/or messenger services: X, Facebook, Instagram, Telegram, TikTok, YouTube, Discord, Medium and/or LinkedIn)"*

— and the fifth binds whoever holds those accounts **on or before 31 October 2028**.

**⭐ The Consent Order of Master Marsh dated 24 August 2026 stays the proceedings "as between the Claimant and the First Defendant" from that date until 8 September 2026** for settlement by ADR, **"no order as to costs."** The report ships **1 September**. The stay expires **8 September** — a dated forward marker any reader can check.

🔴 **And reading the primary corrected the secondary.** The trade coverage that surfaced this said the court had paused the case *"until late August."* That described the **superseded** 25 June order. A report citing it would have shipped on 1 September asserting the expiry of a stay that had eleven days left. **Watch (vv), eighth vindication, first on a class-3 item.**

⚠ **The stay binds two parties of five.** Defendants 2–5, including the promotions class, are not party to it.
🔴 **No causal link asserted between the UK proceedings and HTX's absence from ESMA's registers.** Two public facts, juxtaposed. **This is the FCA under s.21 FSMA, not an EU NCA under MiCA — watch (b) is untouched and the day-46 EU enforcement null stands.**

→ `../regulator-filings/fca-htx-promotions-consent-order-stay-2026-08-28.md` (**NEW**)

### 2. ⭐⭐ 🟢 **WATCH (af) CLOSED IN ONE PASS, NO NETWORK — AND THE UNREAD COLUMN MEASURES THE PROMOTIONAL SURFACE.**

All four stored ESMA snapshots profiled **column by column**: population rate, distinct values, modal values, md5. **CASPS reproduces its 08-17 md5 and row count exactly** — a third independent re-verification as a side effect.

**`ac_serviceCode_cou` — the passporting column, populated 324/329, read once before today for "3 blanks" — is a regulator-published measurement of every firm's lawful promotional reach, and it is sharply bimodal:**

| States | Rows | Share |
|---|---:|---:|
| **1** | **124** | **38.3%** |
| 2–28 | 68 | 21.0% |
| **29–30** | **132** | **40.7%** |

**Median 10, mean 15.0 — and the mean falls in the distribution's empty middle.** 🔴 The mean may not be printed as typical.

**⭐ Eleven of the thirteen tracked-firm entities sit at 26–30.** Two exceptions, both second entities of firms already at 30: **Payward Global Solutions** (Kraken) at **CY|IE only**, and **BP23 CA Limited** (Bitpanda) **blank** — one of five blanks in 329 rows. 🔴 Entity-level, never aggregated to firm level.

**⭐⭐ And it completes yesterday's Volksbank finding.** Post-deadline entrants are **65.7% single-market** against **34.1%** pre-deadline — and **all 14 German post-deadline entrants took a domestic-only authorisation.**

**🔴 A defect in ESMA's own register, found in passing:** Greece is coded as **both `EL` and `GR`**; 71 rows carry `EL`, 94 carry `GR`, **9 carry both** — and those 9 are the file's only "31-state" rows. **Max real breadth is 30.** Every figure above is computed on the normalised set.

**🔴 The register has a field for the promotional estate and it is empty.** `ae_website_platform`: 47 populated → less 4 `n/a` and 3 documented column-bleed rows → **40 real → 2 that differ from the corporate URL.** *The register MiCA's marketing-communications obligations attach to cannot, from its own fields, see where those communications are published.*

**🔴 Same column name, different variable across registers.** `ac_authorisationNotificationDate` in **EMTWP** modes on **23/11/2022** and **26/04/2017** — it dates the underlying e-money licence, corroborated by `ae_authorisation_other_emt` reading "Electronic money institution" in 29 of 42 rows. **A pooled MiCA-authorisation time series across registers would place MiCA authorisations in 2017.** The 08-27 rate is safe only because it was computed on CASPS alone.

→ `../regulator-filings/esma-register-field-inventory-and-passporting-breadth-2026-08-28.md` (**NEW**)

### 3. ⭐ 🟢 **THEME 4 IS WRITTEN. THE FINDINGS FILE EXISTS.**

Four days from ship, `findings/` held no Theme-4 file. It now holds the passage, adjudicated, with every figure traced to a named corpus record and every inherited prohibition attached — including the two the passage most invites (absence-as-non-compliance; the FCA/ESMA causal link).

→ `../../findings/theme-4-mica-exposure-surface.md` (**NEW**)

### 4. 🔴 **ARBITRUM LEFT THE ABSENCE PANEL. YESTERDAY'S PREDICTION WAS TESTED IN ONE DAY AND CONFIRMED.**

`_absence.csv` **6 → 5**. Arbitrum is gone; the Lever read timeout did not recur. Yesterday's record predicted exactly this, in these words:

> *"A firm can enter the panel and leave it on consecutive days with no event at either end — which means an absence claim drawn from this file is not merely biased, it is non-reproducible."*

**Twenty-four hours later, that is now an observation rather than an inference.** Arbitrum entered on 08-27 and left on 08-28; **the firm did nothing on either day.**

🔴 **Watch (ad) is no longer a warning, it is a measured property.** The 08-25/08-27 prohibitions stand and need no strengthening — they were already written at full width. **What changed is their status: the corpus no longer needs to argue the panel is unstable.**

⚠ Today's four `fetch_errors` are all **stable HTTP 404s** (Wormhole, Aave, Bitwise, Chainlink Labs) — a different error class from yesterday's transient Lever timeouts, and consistent with the panel returning to its stable membership of five.

**Class 1: 0 net-new to the cohort (both of the feed's net-new roles are AI labs — non-cohort); guard HEALTHY and comparable; absence panel 6 → 5. Class 2: byte-identical, 17th run, panel 74 days stale. Class 3: +2 NEW — the FCA/HTX consent order and the four-register field inventory. Class 4: 0 net-new, FOURTEENTH consecutive recall confirmation. Class 5: 0 net-new events; tracker untouched. Plus the Theme-4 findings file.**

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

```
date: 2026-08-28   source A (jobs) scan_date: 2026-08-28
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-27T21:49:06Z, age=14.3h,
  fingerprint total_jobs_fetched=3362, delta=+6 vs 2026-08-27 (3356))
  reason: age 14.3h, fingerprint delta +6
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance','Bybit','HTX','Kucoin','Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave','Binance','Bybit','HTX','Kucoin']
```

Fingerprint series, with the 08-24 denominator break and the 08-26 gap marked:

```
2151 → 2151(frozen) → 2186 → 2196 → 2259 → 2265 → 2263 ‖ 3334 → [no 08-26] → 3356 → 3362
                                                          ↑ break                    ↑ +6, ONE day
```

**🟢 Today's +6 is the first single-calendar-day delta since the denominator break.** `companies_scanned` **147**, `companies_via_api` **99**, `companies_via_chrome_pending` **48** — all identical to 08-25 and 08-27. Comparability hand-verified again; the **(ac) guard remains deliberately unshipped** — watch (tt), third consecutive run declining to ship a new guard four days from ship.

**`ADDED: 0` is not silence.** The feed reports `new_count: 2`, both **posted 2026-08-27**, both **Tier 3 / category AI, outside the cohort**:

| Company | Role | ATS | URL-verified |
|---|---|---|---|
| **Anthropic** | Field Marketing Lead, Public Sector | greenhouse | `head_200` |
| **OpenAI** | Product Marketing Lead, Executive Engagement | ashby | yes |

The sync correctly admitted neither.

> 🟢 **PERMITTED:** *the scan ran, found two net-new senior marketing roles across 147 companies, and neither was at a cohort firm.*
> ⚠ **NOTED, NOT CLAIMED — and it is the second consecutive day of it.** On 08-27 the single net-new senior marketing role in the whole scan was at Anthropic; today both are at Anthropic and OpenAI. **This rhymes with `findings/theme-1-marketing-function-attrition-coinbase-openai.md`** — the senior layer leaving crypto marketing for AI labs. 🔴 **It is not evidence for that finding and must not be cited as such.** n=3 postings over two days, from a scan that reaches 99 of 147 companies and excludes five tracked firms by construction. **Recorded as a pattern to test properly after ship, not as a datum.**
> 🔴 **PROHIBITED:** *"the cohort posted no marketing roles today."*

**Absence panel 6 → 5** (see headline 4). Chrome work-queue **5, unchanged**.

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 74 days stale.** 18 agency-claims files written, **byte-identical for the seventeenth consecutive run.** 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation.

🔴 **Watch (d), 23rd run.** `methodology.md` §6 still calls this a *"daily 18-agency panel."* **It is not daily and has not been for 74 days. Four days to ship.**

### 3. Regulator — **+2 NEW. One from the web, one from the repo.**

Full records: `../regulator-filings/fca-htx-promotions-consent-order-stay-2026-08-28.md` and `../regulator-filings/esma-register-field-inventory-and-passporting-breadth-2026-08-28.md`. Headlines 1 and 2.

**🟢 Provenance was clean today — watch (i) DID NOT PAY.** Both FCA fetches returned **200 on the first attempt**, including a PDF. **Fifteen runs of provenance refusals, and the first clean class-3 fetch pair in three runs.** ⚠ Not evidence the underlying problem is fixed — both URLs came from search results in the same session, which is the sanctioned path. The escalation stands.

**⚠ A provenance defect at the FCA's end, recorded:** the statement page's own "Page updates" log stops at **29/06/2026** and does not record the 24 August order that the page itself lists. Only `article:modified_time: 2026-08-26T10:34:02+01:00` evidences the edit. **Rule adopted: take FCA statement-page dates from `article:modified_time`, not from the on-page log.**

**Search, no further net-new primary:** ESMA/BaFin/AMF/CONSOB/AFM/CySEC marketing-side actions — nothing in-window the corpus does not hold. The **joint AMF/FMA/CONSOB call for a stronger European framework** and the **ESMA peer review of CySEC's cross-border supervision** surfaced again and were **refused again on scope** (supervisory architecture, not marketing-side enforcement) — recorded so they are not re-discovered a third time as near-misses.

**Not fetched, not guessed:** `CASPS.csv`, `OTHER.csv`, `NCASP.csv`, MAS, the retry queue, the five post-deadline CONSOB resolutions, the +6 rows of 08-25 (**still unread; every figure this run scoped to 08-17 and says so**). The four FCA orders other than 24 August were **listed, not fetched**, and nothing is claimed about their contents.

**Watch (b) — NOT RESTATED and NOT ADVANCED.** No EU NCA marketing-side action. The FCA item is explicitly excluded from watch (b) in its own record.

### 4. Operator statements — **0 NET-NEW. FOURTEENTH consecutive recall confirmation.**

| Surfaced | Disposition |
|---|---|
| **Steve Smart, joint executive director of enforcement and market oversight, FCA** — *"This is the first time we've taken enforcement action against a crypto firm illegally marketing their products to UK consumers."* | **NOT CLASS 4 — filed under class 3.** §4 requires a **marketing operator at a tracked firm**. A regulator is not one. **Recorded because the quote is the best verbatim the run captured and the temptation to file it here was real.** |
| **NorthPoint's own press release** (natlawreview / einnews) | 🔴 **REFUSED AGAIN — second consecutive run.** Our own promotional material; the author is not a tracked-firm operator. |
| **Bitget CMO** — *"crypto exchanges must evolve beyond trading"* (crypto.news) | **REFUSED — non-cohort.** Already refused on 07-19 on the same ground. Third appearance. |
| **Bybit CEO Ben Zhou** on MiCA + MiFID/EMI licensing (CoinDesk, 2026-04-26) | **ALREADY HELD / REFUSED** — CEO, not a marketing title; out of the §4 role gate. Refused 07-19 on the same ground. |
| **OKX Europe chief**, theblock.co/post/405777 | **ALREADY HELD** — 06-29, 07-13, 07-16, 07-17 run records; also fails the role gate. |

⚠ **Watch (l), 24th costing — WEAK again, and it is not inflated.** Today's refusals are all **scope or role** refusals the report would make at any width. **Escalation (v) is NOT strengthened.** It still rests on the three strong refusals of 08-23/08-24.

**+0 admitted.**

### 5. Layoffs — **0 NET-NEW EVENTS. TRACKER UNTOUCHED — 26 rows, 10 fields, byte-identical.**

Search returned FalconX (**already row 18**, 2026-08-03, −10%), Crypto.com, Gemini, Coinbase, CryptoJobsList, layoffhedge, ratelys, trueup — **all held.**

**No row was edited, no grade moved, no figure entered.** `date-provenance-audit.py` **not re-run** — the file is unchanged since the 08-27 post-edit run whose verdict (exit 1; `DATE-INVERSION` 0 · `NO-URL` 3 · `LAG-EXCEEDED` 2 · `SELF-DATED` 17 · `NO-URL-DATE` 13) therefore still describes it. 🟢 **Recorded rather than re-run: re-running an audit over an unchanged file to print an unchanged verdict is the "builders not scanners" failure in miniature.**

🔴 **Row 6 (MARA) remains unlabelled, uncited, and flagged to STRIKE at ship.** The adjudicable denominator remains **25**.

### 6. NorthPoint longitudinal panel

`findings/longitudinal-2026-06.md` — day-58 shift appended. Panel itself unchanged (74 days stale, §2).

---

## Watch items

- **(b) First named post-deadline EU NCA marketing-side action** — **NOT ADVANCED.** The FCA/HTX item is explicitly out of scope for this watch and says so in its own record. Null holds at day 58.
- **(d) Agency panel staleness — 74 days**, byte-identical seventeen runs. **23rd run. Four days to ship.**
- **(e′) Cadence** — 🟢 **RESTORED. One-day step; recovers to 10 of 12.** ⚠ The cause of the 08-26 loss is unfixed: `/sessions` still 100%, 0 bytes free.
- **(i) `web_fetch` provenance refusals** — 🟢 **DID NOT PAY.** Two class-3 fetches, both 200 first attempt, one of them a PDF. First clean pair in three runs. **The escalation stands** — one clean run is not a fix, and the one-line remedy is still unapplied with four days left.
- **(j) Senior-leader exits** — **NOT ADVANCED.** No new departure surfaced. Fourteen consecutive runs.
- **(l) §4 too narrow** — **24th costing, WEAK.** All four refusals were scope/role refusals valid at any width.
- **(n) Full-range re-sweep of classes 3, 4, 5** — 🟢 **TWELFTH CONSECUTIVE VINDICATION.** Half of today's class-3 output came from parsing files already on disk; the other half came from a case the corpus had surfaced **on 07-19 and never written down.** Both halves are re-sweep findings.
- **(o) Slug-date inference** — **NOT EXERCISED.** Both FCA URLs are slug-dated by the regulator itself and the dates were taken from metadata, not slugs.
- **(pp) A clean parse is not a complete capture** — 🟢 **HONOURED.** No absence claim was made from an unverified capture. `verify-capture.py` not re-run: today's CASPS read reproduced the stored md5 exactly, which is the same assurance by a shorter path, and is recorded as such.
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — 🟢 **PAID, USEFULLY.** The trade press's "paused until late August" **confirmed** the corpus's prior of a stalled case and was wrong; the primary said 8 September. **A confirming secondary got read anyway, and that is the only reason the error was caught.**
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — 🟢 **HONOURED, third consecutive run.** The (ac) comparability predicate verified by hand, deliberately unshipped.
- **(vv) A number is not safe until someone has read its citation** — 🟢 **EIGHT-FOR-EIGHT, and the first on a class-3 date.** See headline 1.
- **(ac) The fingerprint series is not one series** — 🟢 **VERIFIED COMPARABLE**, by hand, `companies_via_api` 99 = 99 = 99 across 08-25 / 08-27 / 08-28. **Today's +6 is the first true single-day delta since the break.**
- **(ad) The absence panel has never contained an absence** — 🔴 **CONFIRMED BY OBSERVATION, NOT INFERENCE.** Arbitrum entered 08-27 and left 08-28 with no event at either end. **Prohibitions unchanged — they were already written at full width.**
- **(ae) The cohort is 27 named firms; both READMEs say thirty** — **UNCHANGED, uncorrected. Four days.**
- **(af) A verified capture is not a read** — 🟢 **CLOSED.** All four stored ESMA snapshots inventoried by field in one pass, no network. **It paid on the first attempt**: the passporting distribution, the Greece double-coding defect, the empty platform-estate field, and the cross-register semantic collision all came out of it.
- **🆕 (ag) ⚠ THE FEED'S NET-NEW SENIOR MARKETING ROLES ARE AT AI LABS TWO DAYS RUNNING.** Anthropic 08-27; Anthropic + OpenAI 08-28. **Not a datum — n=3, biased instrument, explicitly not cited to Theme 1/2.** Opened so that if it continues it is already being counted, and so that nobody later mistakes it for evidence gathered on purpose.
- **🆕 (ah) 🔴 A REGULATOR'S OWN CHANGE LOG OMITTED A CHANGE.** The FCA statement page lists the 24 August order but its update log stops at 29 June. **Take dates from `article:modified_time`.** Generalise before ship: any regulator page used as a dated primary should be dated from metadata, not from its visible history.
- **Unchanged and not re-narrated today:** (a), (c), (e), (f), (g), (h), (h′ — REJECTED), (k), (m), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (ab — CLOSED), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (mm), (nn), (oo), (qq), (rr), (uu), (ww), (xx — CLOSED), (yy), (zz — CLOSED).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.3h, 3356 → 3362, delta +6. 0 postings added; absence panel 6 → 5.**
2. Upstream `scan_metadata` read: 147 / **99** / 48 — unchanged vs 08-25 and 08-27. Comparability hand-verified (watch ac).
3. Upstream `new_since_last_scan` (2), `fetch_errors` (4), `needs_chrome_fallback` read → both net-new roles are AI labs; all four errors are **stable 404s**, none a timeout.
4. **Field-by-field inventory of all four stored ESMA snapshots** — population rate, distinct count, modal values, byte count and md5 per file. **CASPS md5 `69e7dc926b…` and 329 rows reproduce the 08-17 and 08-27 records exactly.**
5. **Programmatic passporting analysis** — raw and EL/GR-normalised breadth distributions; median/mean; single-state and ≥29 shares; the 13 tracked entities; the 5 blank rows; pre- vs post-deadline cross-tab; German post-deadline subset.
6. **`ae_website_platform` analysis** — populated / `n/a` / column-bleed / net real / differs-from-corporate, with the two differing rows named.
7. WebSearch — ESMA/BaFin/AMF/CONSOB/AFM/CySEC marketing enforcement Aug 2026 → **0 net-new primary.** Two supervisory-architecture items refused on scope, second time.
8. WebSearch — crypto CMO / head of marketing / MiCA Aug 2026 → **0 net-new.** NorthPoint's own PR (refused), Bitget CMO (non-cohort), Bybit CEO (role gate), OKX Europe chief (held).
9. WebSearch — crypto layoffs marketing Aug 2026 → **all held.** FalconX is row 18.
10. WebSearch — FCA/MAS/VARA crypto promotion enforcement Aug 2026 → surfaced the FCA/HTX matter with an **fca.org.uk primary** in the result set.
11. WebSearch — FCA HTX settlement → confirmed the FCA statement-page URL and surfaced the trade-press "late August" characterisation **that the primary then disproved.**
12. `web_fetch` `fca.org.uk/news/press-releases/fca-action-against-htx-illegal-financial-promotions` → **200**, full body, metadata dates captured.
13. `web_fetch` `fca.org.uk/news/statements/htx-huobi-legal-proceedings` → **200**, key-documents list + `article:modified_time` 2026-08-26 + the omitted-change-log defect.
14. `web_fetch` `fca.org.uk/publication/documents/order-master-marsh-24-august-2026.pdf` → **200, sealed consent order read in full.** The stay dates, the scope of the stay, the costs order and the five defendant definitions are quoted from this document, not from any outlet.
15. Repo dedup pass: 08-27 record in full; four repo docs in full; all 26 tracker rows; five directory indexes; nine grep sweeps.
16. `date-provenance-audit.py` **deliberately not re-run** — tracker unchanged; prior verdict still describes the file. Recorded, not silently skipped.
17. **No URL was fabricated. No figure was entered that its source did not state. No absence claim was made from an unverified capture. No paywall was circumvented. No register was re-fetched. No allegation was asserted as fact. No person was named against the PERSONS UNKNOWN defendant classes.**

---

## Net-new / changed this run

- `corpus/regulator-filings/fca-htx-promotions-consent-order-stay-2026-08-28.md` — **NEW. The run's sharpest artifact.** The promotions-controllers defendant class verbatim; the 24 August consent order and its 8 September expiry; the stay's two-party scope; the FCA's pleaded allegations attributed as allegations; the Steve Smart quote filed under class 3 with the reason; the regulator's own omitted change log; a full primary-sourced chronology; eight explicit non-claims including the two traps (naming a person; linking to HTX's ESMA absence).
- `corpus/regulator-filings/esma-register-field-inventory-and-passporting-breadth-2026-08-28.md` — **NEW. Closes watch (af).** Four registers profiled by field with md5s; the bimodal passporting distribution and why the mean is prohibited; the thirteen tracked entities and the two instructive exceptions; the post-deadline single-market cross-tab; the EL/GR double-coding defect; the empty platform-estate field; the cross-register semantic collision on `ac_authorisationNotificationDate`; eight explicit non-claims.
- `findings/theme-4-mica-exposure-surface.md` — **NEW. The theme's first findings file, four days from ship.** Thesis paragraph; four load-bearing facts each traced to a record; the enforcement half with its notification-asymmetry limit; the FCA case as the one live marketing-side action and why it does not close watch (b); a set candidate passage; four open items.
- `findings/longitudinal-2026-06.md` — day-58 shift appended.
- `corpus/README.md` — index + reading rules updated.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json` — sync writes (17th run).
- `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — byte-identical, 17th consecutive run.
- **Deliberately NOT written:** any edit to the layoff tracker; any figure covering the +6 CASPS rows of 08-25; any absence claim about Aave, Arbitrum, Binance, Bybit, HTX or KuCoin, or any count of absent firms; any Theme-1/2 citation of the AI-lab posting pattern; the (ac) comparability guard; any schema change; any edit to `tracked-firms.md`, `README.md`, `README-for-github.md` or `methodology.md`; any characterisation of the four FCA orders that were not fetched; any prediction about the FCA/HTX settlement.

---

## Recommendation for next run

1. **🔴 THE README'S FRIDAY PROMISE — TODAY WAS THE LAST FRIDAY BEFORE SHIP, AND IT PASSED UNRESOLVED.** `README.md` says inbound nominations *"are read every Friday"* and that *"the corpus updates here every Friday."* There is no mailbox access from this loop and `inbound-nominations.md` has never existed. **Three consecutive Friday failures now stand, and there is no fourth Friday.** The honest fix is one sentence: say the corpus updates **daily** (it does — 57 run records prove it) and drop or qualify the nominations cadence. **Thirty seconds. It is the last chance.**
2. **🔴 THE TWO COUNTABLE README DEFECTS — FOUR DAYS, FOUR LINES.** (a) Both READMEs say **thirty** tracked firms; `tracked-firms.md` names **27**. (b) The three advertised layoff examples — Algorand, Crypto.com, Gemini — are **0-for-3 on inspection**, while **Block, Inc.**, the tracker's best-graded AI-cover row, is advertised nowhere. **The corpus is public and both are countable in ninety seconds by a hostile reader.**
3. **⚠ DECIDE THE ABSENCE-PANEL SENTENCE — FOURTH CONSECUTIVE RESTATEMENT, AND THE ARGUMENT IS NOW OVER.** The panel's instability is no longer inferred; Arbitrum entered and left on consecutive days with no event. Either `methodology.md` §1 gains a paragraph distinguishing *firm silence* from *scanner reach on the day of the scan*, or Themes 1 and 4 inherit a claim the corpus cannot support. **The Theme-4 findings file was written to depend on it nowhere — deliberately — so this is now a methodology defect rather than a blocker.**
4. **⭐ READ THE +6 CASPS ROWS, OR KEEP THE SCOPE SENTENCE EVERYWHERE.** Every Theme-4 figure is scoped "as at 2026-08-17". **Keeping the scope sentence is safe and free; a re-fetch four days from ship is neither.** Recommendation: **keep the scope sentence and do not re-fetch.**
5. **Do NOT re-fetch `CASPS.csv`, `OTHER.csv`, `NCASP.csv`. Do NOT re-open MAS. Do NOT re-issue the retry queue. Do NOT attempt row 13's Bloomberg paywall. Do NOT fetch the four un-fetched FCA orders** — nothing in the report depends on them.
6. **Escalate to Jukka — four items, in order:**
   - **(i) ⭐⭐ THEME 4 HAS BOTH HALVES OF ITS STORY AND A LIVE COURT CASE THAT RESOLVES SEVEN DAYS AFTER SHIP.** *Thirty-five firms entered ESMA's authorised-CASP register in the fifty-eight days after MiCA's transitional period ended. Twelve were German cooperative banks, all fourteen German entrants took domestic-only authorisations, and none was a crypto-native firm this report tracks. Meanwhile, in the UK's first crypto-marketing enforcement action, the fourth defendant is "the persons currently in control of promotions" on nine named platforms — and the case is stayed for settlement until 8 September, one week after we ship.* **The draft passage is in `findings/theme-4-mica-exposure-surface.md` and is safe to set.**
   - **(ii) 🔴 THE README DEFECTS ARE THE LAST CHEAP WIN AND THE FRIDAY WINDOW IS NOW CLOSED.** Items 1 and 2 above: five lines of editing, on a public repo, four days out.
   - **(iii) 🔴 `/sessions` IS STILL AT 100% WITH 0 BYTES FREE.** It cost the corpus 08-26 outright. Today's run survived it. **Host-side fix only Jukka can perform — `needs-jukka` row 545.**
   - **(iv) ⚠ WATCH (i) DID NOT PAY TODAY — the first clean class-3 fetch pair in three runs — but the one-line fix is still unapplied.** Pasting the tracker's `source_url` values verbatim into the scheduled-task prompt has been the remedy for fifteen runs. **Four days. After ship it stops mattering.**
