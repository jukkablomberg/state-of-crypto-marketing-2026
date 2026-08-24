# Corpus-assembly daily run — 2026-08-24 **(day 54 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-24 (**Monday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-23 recommendations:** (1) **finish the citation sweep — start with row 2, Gemini −30%**, the last of the three README-advertised layoff examples not yet inspected; (2) **audit `ai_cover_narrative` end to end** and grade every `Y` row — the highest-value single sweep left before ship; (3) **re-read `CASPS.csv` under the 21 August republication, and fetch ESMA's *Description of the fields* CSV in the same pass** — it gates a column the report might otherwise lean on; (4) do **not** re-fetch `OTHER.csv`, do **not** re-issue the retry queue, do **not** re-open MAS; (5) six escalations to Jukka.
**Dedup baseline read before writing:** `2026-08-23-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md`, `corpus/README.md` in full; all 26 tracker rows via `csv.DictReader`, with the nine `Y` rows' full notes read individually; `corpus/operator-statements/`, `corpus/regulator-filings/`, `corpus/layoff-tracker/`, `corpus/job-postings/` and `findings/` indexes; grep sweep for `conlan|kalifowitz` across `corpus/` and `findings/`.
**✅ CADENCE: HELD. 08-23 → 08-24 is a ONE-DAY GAP. Watch (e′) improves to 8 of 10.** Corroborated from inside the data: today's class-1 fingerprint comparison is against **2026-08-23**, yesterday.

---

## Headline result

**All four mandated work items were executed. Three of them changed what the report may print, and one of them retracted a sentence the corpus drafted yesterday. Nothing was fabricated. Two guards were applied; one of them could not be run and said so.**

### 1. 🔴 **THE COLUMN THE 08-23 RUN GATED WAS GATED CORRECTLY — AND THE GATE WAS RIGHT TO EXIST, BECAUSE THE COLUMN MEANS SOMETHING ELSE ENTIRELY.**

ESMA's *Description of the fields in the interim MiCA register* was fetched at source. `ae_infrigment` is defined, verbatim, as *"Case of infringement identified by **ESMA in accordance with Article 17 of Regulation (EU) No 1095/2010**."*

**Article 17 is the ESMA Regulation's breach-of-Union-law procedure — ESMA against a NATIONAL COMPETENT AUTHORITY. It is not a field about the listed entity at all.**

So yesterday's true observation — *`ae_infrigment` is `No` for all 167 rows* — is **interpretively empty**, and the candidate sentence built on it is **withdrawn before it ever shipped.** The 08-23 record refused to lean on the column and put it on the work queue instead. **That refusal is the reason this is a correction and not an erratum.**

**🟢 And the load-bearing half survives intact, because it never rested on that column.** `ae_reason` is confirmed by ESMA's own description as an entity-level free-text *"Non compliancy reason"* field. It is populated for **one row in 167**. The shippable sentence stands, now field-semantics-verified:

> *Of the 167 entities on the EU's register of non-compliant crypto-asset service providers, ESMA provides a free-text "non-compliancy reason" field. Exactly one entry uses it — and that one is about an authorisation, not an advertisement.*

→ `../regulator-filings/esma-register-field-semantics-ae-infrigment-resolved-2026-08-24.md` (**NEW**)

### 2. ⭐ **THE THIRD README-ADVERTISED LAYOFF EXAMPLE FAILED TOO — AND THE SAME FETCH PRODUCED THE BEST-SOURCED ROW IN THE TRACKER.**

Row 2's citation was opened. The primary turned out to be **a Form 8-K, Exhibit 99.1, filed with the SEC on 2026-02-05** — the firm's announcement is a *filed regulatory document*, which makes this row's primary stronger than any other in the corpus.

**🔴 The number broke, as the other two did.** The firm states: *"In 2022, our workforce peaked around approximately 1,100. Heading into the end of 2025, we were about 50% of that size. Today, we are reducing our size again by roughly 25%."* The 25% and 50% are **cumulative-since-2022**, not YTD. **There is no firm-stated −30% YTD anywhere. STRUCK.** The widely-reported **"200 jobs" is not firm-stated either** — and is the first propagated figure the corpus has found that does not reconcile against the firm's own published base (25% of ~550 ≈ 137).

**Three for three. Every layoff example this report advertises publicly has been found defective on inspection** — Algorand uncited (08-21), Crypto.com derived (08-22), Gemini unsourced-and-unreconcilable (08-24).

**⭐⭐ And the capture's best sentence is about non-engineering work.** Verbatim, in the filed exhibit, in the same paragraph as the 25% reduction:

> *"Critically, we are seeing that this step change holds true for every engineer who adopts AI into their workflows. **And it also holds true for non-engineering work.**"*

**A Tier-1 tracked exchange telling a securities regulator that its 100x AI productivity claim extends past engineering, while cutting a quarter of its staff. Marketing is non-engineering work. THE FIRM DOES NOT NAME MARKETING and no marketing claim is attributed to it** — but nothing else in the corpus places the function this close to the substitution frame in a *filed* document. **Watch (l), from a third direction and on the strongest artifact yet.**

→ `../layoff-tracker/_gemini-row2-citation-opened-at-primary-2026-08-24.md` (**NEW**)

### 3. 🔴 **THE MANDATED COLUMN AUDIT FOUND THE OPPOSITE DEFECT TO THE ONE IT WENT LOOKING FOR — AND IT IS WORSE.**

The audit was ordered because Luno's *automation → AI* substitution might be systemic. **It is not: eight of nine `Y` rows rest on the token "AI" appearing in the source; Luno is the only inference. The defect is confined to its own row.**

**But grading the column end to end collapses the headline number.** A new `ai_cover_grade` field now carries a five-step ladder (A firm-stated-verbatim · B relayed · C outlet characterisation · D anonymous · E inferred). The result:

**A naive AI-cover share of 9/26 = 35% becomes 4/26 = 15% on Grade-A evidence alone. A twenty-point gap, on a Theme-5 headline number.**

**MAY NOT BE PRINTED:** ~~"35% of 2026 crypto layoffs cite AI."~~ Ungraded, it treats an SEC filing and an unnamed source as the same evidence.

→ `../layoff-tracker/_ai-cover-narrative-grading-audit-2026-08-24.md` (**NEW**)

### 4. 🔴 **`CASPS.csv` TRUNCATED AGAIN — CAUGHT ON STRUCTURE, AT A CUT POINT IDENTICAL TO 08-17.**

82,445 characters, 205 lines, final line severed **mid-field inside an unterminated quoted address** (`"27-31 avenue du Général Leclerc - 94`). Against the **329 rows verified COMPLETE on 08-17**, a ~38% deficit. **CLASS-3 ABSENCE CLAIM REFUSED.**

**⚠ And `verify-capture.py` could not be run on it** — the fetch never became a file the guard could open, so its primary predicate was applied **by hand** and the weakening is labelled. **No snapshot was written: hand-transcribing 82,445 characters would produce a fabricated artifact, not a capture** (08-23 precedent, applied again).

**⚠ The retired size heuristic got a tempting data point and stays retired.** Today's cut is byte-identical to 08-17's on the same file — the channel budget is evidently stable per-channel. **08-20 already proved a different cut point exists. A reproducible number is not a diagnostic one. Structure decided, as it did on 08-17 and 08-20.**

**Class 1: 0 net-new, guard-certified HEALTHY, delta −2. Class 2: byte-identical, 14th run, panel 70 days stale. Class 3: +1 NEW — a field-semantics resolution that RETRACTS a drafted claim and confirms the surviving one; CASPS re-read attempted and refused. Class 4: 0 net-new, ELEVENTH consecutive recall confirmation; the author's own press release ranked top again, on two domains. Class 5: 0 net-new layoffs; row 2 opened at an SEC filing, 2 figures struck, 1 [VERIFY] closed by striking, 1 [VERIFY] closed by capture; the whole `ai_cover_narrative` column graded and a new field added.**

---

## Six-class audit trail

### 0. Retry-queue seed — not re-issued, per mandate item 4

One line, as instructed. Not re-issued. `OTHER.csv` not re-fetched. MAS not re-opened.

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

```
date: 2026-08-24   source A (jobs) scan_date: 2026-08-24
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-23T21:51:02Z, age=14.3h,
  fingerprint total_jobs_fetched=2263, delta=-2 vs 2026-08-23 (2265))
  reason: age 14.3h, fingerprint delta -2
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
```

**Both predicates pass. The class-1 absence claim is PERMITTED and is made: the scan ran, it looked at 2,263 postings, and it found no net-new tracked-firm marketing role today.**

⚠ **A first for the fingerprint predicate: today's delta is NEGATIVE (−2).** The guard's rule is *"a delta of 0 degrades the verdict to STALE"* — it tests **movement**, not direction, so −2 passes correctly. Recorded because it is worth being explicit that a shrinking board is liveness evidence exactly as a growing one is: postings expire, and an expiring posting proves the scan re-read the source. **No Theme-5 signal is read into it. Watch (rr) stays downgraded.**

Fingerprint series `2151 → 2151 (frozen) → 2186 → 2196 → 2259 → 2265 (+6) → 2263 (−2)`.

**Absence panel unchanged, 6 firms:** Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys. **Chrome work-queue unchanged, 6:** Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana. **Residual gap bounded and known** (`scripts/README.md`).

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 70 days stale.** 18 agency-claims files written, **byte-identical for the fourteenth consecutive run.** 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation.

**Watch (d), 20th run.** `methodology.md` §6 still calls this a *"daily 18-agency panel."* **It is not daily and has not been for 70 days. Eight days to ship.** Rewrite the sentence or the report misdescribes its own instrument.

### 3. Regulator — **+1 NEW. A DRAFTED CLAIM RETRACTED; THE SURVIVING ONE VERIFIED; CASPS REFUSED.**

Full record with six explicit non-claims: `../regulator-filings/esma-register-field-semantics-ae-infrigment-resolved-2026-08-24.md`. See headlines 1 and 4.

**Watch (b) — NOT restated today.** `NCASP.csv` was read at source on 08-23 against a register republished 21 August. **It is not re-read by the calendar and the twenty-consecutive-zero count is not advanced by a run that did not look.** (The 08-22 precedent, applied.)

**Search, no net-new primary:** ESMA/BaFin/AMF/CONSOB/AFM/CySEC marketing-side actions — nothing in-window that the corpus does not hold.

**Not fetched, not guessed:** `CASPS.csv` under the 21/08 republication (**attempted today, truncated, still the oldest live queue entry — and now known-truncated on two separate attempts**); the five post-deadline CONSOB resolutions; `OTHER.csv` (standing instruction).

### 4. Operator statements — **0 NET-NEW. ELEVENTH consecutive recall confirmation.**

**🔴 The §4 search returned NorthPoint's own press release as its top result again — and this time on TWO domains** (natlawreview and einnews, both 2026-08-14, Jukka Blomberg). **Refused, and recorded so it is not re-discovered a third time. The syndication is spreading, which means this will keep happening and will keep ranking higher.** Watch (ss); it needs the methodology-appendix disclosure that escalation (v) has been carrying.

Two candidate leads surfaced and **both were already held** — checked by grep, not by memory:

| Lead | Status |
|---|---|
| Crypto.com CMO Steven Kalifowitz departs (2026-05-05) | **HELD** — `operator-statements/cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md` |
| Binance CMO Rachel Conlan departs (2026-05-12) | **HELD** — `operator-statements/binance-chen-marketing-not-hype-2026-07.md` et al. |

**11/11 cohort recall across the series. The null is real, not an artefact of a dead query** — the query surfaced two genuine senior-marketing exits at tracked firms and the corpus already had both.

**+0 admitted.** The Gemini "non-engineering work" sentence (headline 2) is a class-4-shaped finding that **§4 cannot admit**, and it is filed under class 5 with that failure stated on its face rather than reclassified to fit. **Watch (l), 21st costing, third distinct failure mode.**

### 5. Layoffs — **0 NET-NEW. Row 2 opened at an SEC filing; the whole `ai_cover` column graded.**

Full records: `../layoff-tracker/_gemini-row2-citation-opened-at-primary-2026-08-24.md` and `../layoff-tracker/_ai-cover-narrative-grading-audit-2026-08-24.md`.

| Row | Action | Result |
|---|---|---|
| 2 Gemini | citation opened **at an SEC-filed 8-K EX-99.1** | 🔴 `−30% YTD` **STRUCK** (never firm-stated, does not reconcile); 🔴 `200 jobs` **REFUSED**; ⭐ `Y` confirmed **Grade A, strongest in the tracker**; ⭐ the *"non-engineering work"* sentence; Theme-4 EU-exit anchor **upgraded to a filed document**; two 07-28 `[VERIFY]`s closed |
| all 26 | **new `ai_cover_grade` column** | 9 `Y` rows graded A–E; **35% → 15% on Grade-A evidence** |

**Search returned:** CryptoJobsList, FalconX, Crypto.com, Algorand, Gemini, MANTRA, trendingtopics aggregate — **all held. 0 net-new layoffs.** The aggregator line *"Gemini… roughly 30%… headcount to around 445"* is the lineage of the figure struck today; **refused, and its refusal is now sourced.**

**Class-5 audit deltas** (`date-provenance-audit.py`, run post-edit): `DATE-INVERSION` holds at **0** · `NO-URL` holds at **1** (MARA — **still flagged to strike if unsourced by ship, eight days out**) · `LAG-EXCEEDED` holds at **1**. **No regression from the row-2 source swap.**

### 6. NorthPoint longitudinal panel

`findings/longitudinal-2026-06.md` — day-54 shift appended. Panel itself unchanged (70 days stale, §2).

---

## Watch items

- **(b) First named post-deadline NCA marketing-side action** — **NOT RESTATED. The register was not re-read today.** The count stands at twenty by observation as of 08-23. **A run that did not look does not advance it.**
- **(d) Agency panel staleness — 70 days**, byte-identical fourteen runs running. **20th run. Eight days to ship.**
- **(e′) Cadence** — **✅ HELD. One-day gap; 8 of 10.**
- **(f) Friday nomination cadence** — **NOT TESTABLE TODAY (Monday).** Two consecutive Friday failures (08-14, 08-21) stand unrepaired; `inbound-nominations.md` still does not exist. **08-28 is the last Friday before ship — four days away.** Escalation (ii) carries at full strength.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED, and today gives a new reason to distrust the test itself:** the grading audit shows the `Y` labels carry five different evidentiary weights. **A hypothesis tested on an ungraded column was never a test. Do not print.**
- **(j) Senior-leader exits** — **ADVANCED, eleventh consecutive run**, recall confirmed against two genuine leads.
- **(l) §4 too narrow** — **🔴 21st COSTING, THIRD DISTINCT FAILURE MODE.** §4 has now refused: a titled person at the wrong altitude (CEOs); a firm's own published account of its marketing function (Gnosis, 08-23); and today, **a firm's statement about non-engineering work in an SEC-filed exhibit.** Each refusal was on a stronger document than the last. **Escalation (v) should be decided with all three in front of it.**
- **(n) Full-range re-sweep of classes 3, 4, 5** — **🟢 NINTH CONSECUTIVE VINDICATION.** The run's best Theme-2/Theme-5 sentence came out of a class-5 *citation-repair* task, and the run's most consequential class-3 result came from fetching a **field-description file** — the least interesting-looking item on the queue.
- **(o) Date the document, never an event held about it** — **🟢 PAID.** Gemini's 8-K carries `Period: 2026-02-05 | Filed: 2026-02-05`; both recorded, and the row's date confirmed against the filing rather than against the reporting.
- **(oo) The "not fetched, not guessed" list is a work queue** — **🟢 SEVENTH CONSECUTIVE PAYOUT, and the payout was the boring entry.** The *Description of the fields* CSV — added to the queue only yesterday, and the least glamorous thing on it — **retracted a claim.** ⚠ **New oldest live entry unchanged: `CASPS.csv`, now known-truncated on two attempts.** Also live: the five CONSOB resolutions, **AscendEX** (tenth carry), **PIP Labs** (fourth carry), and **two class-5 primaries that would upgrade grades C→A and B→A** (`theblock.co/post/391520`, Block/Dorsey; `x.com/diran_li/...`, Messari/Li) — both open since 08-06.
- **(pp) A clean parse is not a complete capture** — **🟢 FIRED, AND ITS LIMIT WAS HIT FROM THE OTHER SIDE.** On 08-23 the guard could verify a stored file but not a fetch that never became one. **Today the fetch again never became a file, so the guard could not run at all** and its primary predicate was applied by hand. **Two consecutive runs blocked by the same plumbing gap on the highest-stakes class.**
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — **🔴 PAID TWICE, AND THE SECOND ONE IS THE MOST DANGEROUS INSTANCE YET.** (a) The author's press release ranked top again, now syndicated to two domains. (b) **A search summary supplied three specific, checkable, named C-suite departures (CFO/CLO/COO) that do not appear anywhere in the SEC-filed primary.** Had they been admitted, they would have been **three fabricated class-4 datapoints about a tracked firm** — and they would have read as perfectly plausible.
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — **NOT EXERCISED TODAY.** `date-provenance-audit.py` ran clean post-edit; no flags raised, none adjudicated.
- **(vv) A number in this tracker is not safe until someone has read its citation** — **🔴 SIX-FOR-SIX ACROSS FOUR RUNS. Not one number has survived having its citation opened.** Today added a fifth defect kind: **a figure that is both unsourced AND arithmetically irreconcilable with the firm's own published base.** Reachable rows still unread: **5 (Block Inc), 12 (OP Labs), 13 (Kraken)**. Rows 9, 10, 17 remain unreachable.
- **🆕 (xx) — 🟢 CLOSED AS MANDATED, AND IT INVERTED.** The substitution defect does **not** propagate (8 of 9 `Y` rows say "AI"; only Luno infers). **But grading the column cut the headline share from 35% to 15%.** The mandate found a smaller problem than feared and a larger one than expected. **New field `ai_cover_grade` shipped; the ungraded share is now prohibited.**
- **🆕 (zz) ⚠ THE SYMMETRIC AUDIT HAS NEVER BEEN RUN — AND ITS ABSENCE HAS A DIRECTION.** Today audited every `Y` row: the rows that make the AI-cover share *look high*. **No one has ever audited the seventeen `N` rows for a firm that did invoke AI and was recorded `N`** — the rows that would make it look higher still, or reveal the labelling is noisy in both directions. **The sweep that got done is the one whose result the report wanted. Run the `N` sweep before Phase 2.**
- **🆕 (ab) ⚠ THE FIGURE COLUMNS NEED THE GRADING LADDER TOO.** `ai_cover_narrative` now has one. `headcount_change` and `percentage` — the columns watch (vv) has broken six times — still do not. **Same treatment, same five grades, before Phase 2.**
- **Unchanged and not re-narrated today:** (a), (c), (e), (g), (i), (k), (m), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (mm), (nn), (qq), (rr — downgraded), (uu), (ww), (yy).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.3h, fingerprint 2265 → 2263, delta −2 vs 2026-08-23.**
2. Repo dedup pass: 08-23 record in full; `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md`, `corpus/README.md`; all 26 tracker rows via `csv.DictReader`, nine `Y` notes read individually; five directory indexes; grep `conlan|kalifowitz` across `corpus/` + `findings/`.
3. WebSearch — Gemini Feb-2026 exit/25%/AI → **admitted the CoinDesk URL.**
4. **`web_fetch` CoinDesk Gemini → 200, full body**, `parsely-pub-date 2026-02-05T17:11:13.436Z`. **⚠ Contains NO AI framing whatsoever** — which is what made the firm's own document necessary rather than optional.
5. WebSearch — ESMA MiCA register / 21 August → **admitted the *Description of the fields* CSV and `CASPS.csv`.**
6. **`web_fetch` ESMA *Description of the fields* CSV → 200, `text/csv`, complete file.** All five templates' field definitions captured; `ae_infrigment` and `ae_reason` resolved verbatim.
7. **`web_fetch` `CASPS.csv` → 200, `text/csv`, 82,445 chars / 205 lines — 🔴 TRUNCATED mid-field.** Terminal row observed by hand; absence claim refused.
8. **`web_fetch` `gemini.com/en-GB/blog/...`: BLOCKED** — *"URL not in provenance set"* — despite being a hyperlink inside the page fetched at step 4. Routed around by search-then-fetch. **Watch (i), eleventh run.**
9. WebSearch — Gemini 2.0 blog → **admitted the SEC EDGAR exhibit URL.**
10. **`web_fetch` SEC EDGAR `a8kblogpostfeb52026.htm` → 200, full body.** Gemini Space Station, Inc. 8-K EX-99.1, Period 2026-02-05, Filed 2026-02-05. Full text captured verbatim.
11. WebSearch — crypto CMO / VP marketing Aug 2026 → 🔴 **top result was the author's own press release, on two domains. Refused.** Surfaced the Crypto.com CMO lead.
12. WebSearch — Crypto.com CMO departure → **Kalifowitz confirmed HELD; Binance/Conlan confirmed HELD.** 0 net-new.
13. WebSearch — crypto layoffs Aug 2026 marketing → **0 net-new**; located the aggregator lineage of the struck Gemini −30%.
14. `python3 scripts/date-provenance-audit.py` — run post-edit. **DATE-INVERSION 0, NO-URL 1 (MARA), LAG-EXCEEDED 1. No regression.**
15. **`verify-capture.py`: NOT RUN — could not be.** Today's `CASPS.csv` fetch never became a file on a reachable filesystem. Predicate applied by hand; weakening stated.
16. **`OTHER.csv`, MAS, retry queue: deliberately not attempted**, per mandate item 4. **`NCASP.csv` deliberately not re-read** — it was read at source yesterday and is not restated by the calendar.
17. **Not reached / not guessed:** see §3. **No URL was fabricated. No figure was entered that its source did not state. No snapshot was hand-transcribed.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-register-field-semantics-ae-infrigment-resolved-2026-08-24.md` — **NEW.** ESMA's own field definitions at source; the Article 17 resolution; the retraction of the drafted `ae_infrigment` claim; the surviving `ae_reason` sentence verified; the CASPS truncation adjudication in full including the refused revival of the size heuristic; six explicit non-claims.
- `corpus/layoff-tracker/_gemini-row2-citation-opened-at-primary-2026-08-24.md` — **NEW. The run's shippable class-5 finding.** The SEC-exhibit promotion; the −30% strike with the firm's own arithmetic; the 200-jobs refusal; the *"non-engineering work"* sentence with its attribution limits stated three separate ways; the Theme-4 upgrade; six explicit non-claims **including the three fabricated C-suite names the search summary offered.**
- `corpus/layoff-tracker/_ai-cover-narrative-grading-audit-2026-08-24.md` — **NEW.** All nine `Y` rows graded A–E with basis; the 35% → 15% collapse; the printable sentence and the prohibited one; the tracked-firm n=4 split; four explicit statements of what the audit did **not** do.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **UPDATED. 26 rows, now 8 fields.** New `ai_cover_grade` column populated for all 26. Row 2 `source_url` promoted to the SEC exhibit; `percentage` and `headcount_change` both rewritten with strikes; note extended with the six-part capture record.
- `findings/longitudinal-2026-06.md` — day-54 shift appended.
- `corpus/README.md` — index updated.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json`, `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — date re-stamps / byte-identical rewrites (sync, 14th run).
- **Deliberately NOT written:** a hand-transcribed `CASPS` snapshot; any absence claim about a named firm in the CASPS register; any `verify-capture.py` exit code for today; any restatement of watch (b); the −30%, 200 and 445 Gemini figures; the three C-suite names absent from the filed exhibit; any claim that Gemini cut marketing; any attribution of Gemini's EU exit to MiCA; any ungraded AI-cover proportion.

---

## Recommendation for next run

1. **🔴 RUN THE SYMMETRIC SWEEP — NEW WATCH (zz). AUDIT THE SEVENTEEN `N` ROWS.** Today graded every row that makes the AI-cover share look high. **Nobody has ever checked the rows that would move it the other way, or reveal the labelling is noisy in both directions.** The sweep that got done is the one whose result the report wanted; that is precisely watch (ss)'s shape, and it is now inside our own method. **Highest-value sweep left.**
2. **🔴 EXTEND THE GRADING LADDER TO `headcount_change` AND `percentage` — NEW WATCH (ab).** Watch (vv) is **six-for-six**: not one figure has survived its citation being opened. The AI column now has grades; **the columns that have actually broken six times do not.** Same five grades. Then finish the reachable citation sweep: **rows 5 (Block Inc), 12 (OP Labs), 13 (Kraken)** — and note rows 5 and 13 are exactly the two whose grades would upgrade.
3. **⚠ `CASPS.csv` — TRUNCATED ON TWO ATTEMPTS. STOP RE-FETCHING IT THE SAME WAY.** Two runs have now spent a fetch on it and been refused. **It needs a channel that persists bytes to disk, or it ships unread and the register question about named tracked firms ships open.** Decide which — do not spend a third fetch on the same failing route.
4. **Do NOT re-fetch `OTHER.csv`. Do NOT re-issue the retry queue. Do NOT re-open MAS. Do NOT re-read `NCASP.csv` by the calendar.** One line each.
5. **Escalate to Jukka — six items, in order:**
   - **(i) 🔴 ELEVENTH RUN. IT BLOCKED THE WORK AGAIN — AND TODAY IT BLOCKED A LINK INSIDE A PAGE WE HAD JUST FETCHED.** `web_fetch` refused `gemini.com/blog/...` while that exact URL sat as a hyperlink in the CoinDesk body captured seconds earlier. **The run recovered only because the SEC happened to hold a second copy.** Rows 9, 10 and 17 have no second copy and will ship unread. **Fix: paste the tracker's `source_url` values verbatim into the scheduled-task prompt.** One edit. Eleven runs unchanged. **Eight days left.**
   - **(ii) 🔴 THE README'S FRIDAY PROMISE — 08-28 IS THE LAST FRIDAY BEFORE SHIP, FOUR DAYS AWAY.** Two consecutive Friday failures stand; no mailbox access; `inbound-nominations.md` does not exist. **Either route the mailbox into a readable artifact this week, or amend the sentence. The second takes thirty seconds and is honest.** After 08-28 the choice is made by default.
   - **(iii) 🔴 `README.md` — ALL THREE ADVERTISED LAYOFF EXAMPLES HAVE NOW FAILED INSPECTION. THE SWEEP IS COMPLETE AND THE SCORE IS 0 FOR 3.** Algorand: no citation (08-21). Crypto.com: the outlet's arithmetic (08-22). **Gemini: −30% never firm-stated and irreconcilable with the firm's own SEC-filed base (08-24).** **Both READMEs still carry all three lines uncorrected, and we published the corpus, so a hostile reader can run this exact check.** This is now the single most likely source of public embarrassment in the repo. **Correct the three lines before ship.**
   - **(iv) ⭐ THEME 5 HAS AN HONEST NUMBER NOW, AND IT IS HALF THE OBVIOUS ONE.** *Of 26 public crypto workforce reductions recorded in 2026, nine are framed around AI — but only four carry a verbatim statement from the firm itself. Two reach us relayed through a reporter, one is a reporter's characterisation with no company quote, one rests on an anonymous source the company has never confirmed, and one is an inference from the word "automation."* **35% → 15%. Ship the graded version; the ungraded one is now prohibited in the tracker's own documentation.**
   - **(v) ⚠ ONE DECISION, TWENTY-ONE RUNS, AND IT HAS NOW FAILED IN A THIRD WAY ON THE STRONGEST DOCUMENT YET.** `methodology.md` §4 admits only CMO / VP Marketing / Head of Brand / Head of Growth at a tracked firm. It has refused a CEO's dated statement on AI and headcount; a firm's own published account of its marketing function; and now **a Tier-1 tracked exchange telling a securities regulator that its 100x AI claim "also holds true for non-engineering work," in the same paragraph as a 25% cut.** **Either widen §4 to admit firm-published statements about the function, labelled as such, or stop recording the cost every run.** Both defensible. **Twenty-one runs of neither is not.** §4 must also carry the **author-in-the-search-surface** disclosure — the press release now ranks top on two syndicated domains.
   - **(vi) 🔴 `methodology.md` STILL NEEDS SIX SECTIONS REWRITTEN: §1, §3, §4, §5, §6, §7 — TWENTIETH run for §1. EIGHT DAYS.** §6's *"daily 18-agency panel"* describes a file **70 days stale**. §3 must state the register's one-stated-reason structure **and must not lean on `ae_infrigment`**. §4 must resolve escalation (v) and carry the author disclosure. §5 must carry `[DERIVED]` on Crypto.com, `[REPORTED]` on Luno, `[PERIMETER]` on Algorand, **`[STRUCK]` on Gemini −30%, and the `ai_cover_grade` ladder.** **Still the one thing in the repo that could embarrass the report.**
