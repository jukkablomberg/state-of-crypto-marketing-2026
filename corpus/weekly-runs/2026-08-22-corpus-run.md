# Corpus-assembly daily run — 2026-08-22 **(day 52 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-22 (**Saturday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-21 recommendations:** (1) **open the ten unread class-5 citations, three per run**, starting with the two `[VERIFY]` rows; (2) keep running watch (oo) — oldest live entries `CASPS.csv` @18/08 and the **ESMA finfluencer-factsheet CANDIDATE**, plus AscendEX and PIP Labs; (3) **add `**Published:**` to the class-4 template and backfill the five files missing it**; (4) do **not** re-fetch `OTHER.csv`, do **not** re-issue the retry queue, do **not** re-open MAS; (5) six escalations to Jukka.
**Dedup baseline read before writing:** `2026-08-21-corpus-run.md` in full; `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; all 25 tracker rows via `csv.DictReader`; `corpus/`, `corpus/regulator-filings/`, `corpus/operator-statements/` and `findings/` indexes; the 08-11 CANDIDATE file in full.
**✅ CADENCE: HELD. 08-21 → 08-22 is a ONE-DAY GAP. Watch (e′) improves to 6 of 10.** Corroborated from inside the data: today's class-1 fingerprint comparison is against **2026-08-21**, yesterday.

---

## Headline result

**The mandate was executed in full, and the item that had been refused nine consecutive times was closed at source. Every one of the three mandated work items paid — and two of them paid by finding a defect in the corpus rather than a fact outside it.**

### 1. ⭐ **THE MOST MARKETING-SPECIFIC REGULATOR INSTRUMENT THIS CORPUS HAS EVER SURFACED IS NOW ADMITTED — AND IT IS ADDRESSED TO PEOPLE WHO HOLD NO LICENCE.**

The **ESMA finfluencer factsheet** — named as a capture queue on 2026-08-11, refused nine times for want of a date — was **captured at source in three first-party fetches** and admitted.

- **ESMA document page** → 200. Lists the EN master + **35 translated versions covering all 27 EU Member States and all three EEA-EFTA states. 36 files. Zero gaps in the EEA.**
- **ESMA EN factsheet PDF** → 200, complete document, quoted verbatim.
- **CONSOB press release PDF** → 200, and **it dates itself in its own text: *"Rome, 12 January 2026."***

**Every prior class-3 admission concerned authorisation status — registers, warning lists, transitional-period statements. Those tell the report who is licensed. This one tells the report what a regulator thinks a promotion may and may not say.** ESMA's own words, naming crypto twice:

> *"Some investments commonly marketed by finfluencers – such as contracts for difference, forex, futures, certain crowdfunding initiatives, or **volatile cryptocurrencies** – can carry very high risk, including the possibility of losing 100 % of the capital you invest."*
> *"Not in tiny text. Not just hashtags. Use words such as **'Ad', 'Paid partnership' or 'Sponsored'**."*
> *"**Disclaimers such as 'This is not investment advice' will not protect you in these cases.**"*

**🔴 And the finding is who it is for.** The factsheet is second-person to finfluencers throughout. **Not one sentence addresses a CASP, an issuer, or any authorised firm**, and it disclaims its own force: *"not intended as legal advice or regulatory interpretation … general guidance only."*

**This anchors in ESMA's own document a read the corpus could previously only infer from a pattern of absences:** the European supervisory response to the crypto marketing surface has taken the form of **guidance addressed to third parties**, not **action against licensees**. It clusters with BaFin *Risks in Focus* (28 Jan 2026): **two European regulator communications naming the promotional channel in the same month, neither aimed at a licensee.**

**It is PRE-DEADLINE and therefore does NOT touch the post-deadline enforcement null.** The conditional branch written on 08-11 resolves exactly as that file predicted. → `../regulator-filings/esma-finfluencers-factsheet-at-source-2026-08-22.md` (**NEW**); the CANDIDATE is marked **PROMOTED / SUPERSEDED** and retained unedited.

### 2. 🔴 **THE CORPUS WAS CARRYING A SECOND NUMBER THE FIRM NEVER SAID. TWO CONSECUTIVE RUNS, TWO OF THE THREE HEADLINE EXAMPLES.**

Row 1, **Crypto.com**, `headcount_change = 180`. The capturing outlet disqualifies it in its own sentence:

> *"The reduction affects roughly 180 employees, **based on the company's previously disclosed headcount of over 1,500**."*

**The firm disclosed a percentage (~12%). The 180 is The Block's arithmetic.** Relabelled **`~180 [DERIVED — NOT FIRM-STATED]`**; the `[VERIFY]` open since 08-11 closes.

**On 08-21 the corpus found it was advertising a percentage it could not source (Algorand). Today it finds it is carrying a headcount the firm never stated (Crypto.com). Two of the three named class-5 examples in `README.md` have now failed inspection in two consecutive runs.** That is no longer a fact about two rows. **It is a fact about how numbers entered this tracker, and it means the remaining seven unread rows should be presumed guilty until fetched.**

### 3. ⭐ **A ROW WAS UNDERSTATING ITSELF, AND THE UPGRADE IS THE STRONGEST FUNCTION-LEVEL SENTENCE IN THE TRACKER.**

Row 25, **MANTRA**, was labelled *"names marketing."* The first-party capture says more than that:

> *"The decision impacts teams across the organization, with functions like **business development, marketing, and HR affected more than others**, according to the post."*

**Not merely named among affected functions — named in the set affected *disproportionately*.** Of 25 rows, 23 name no marketing function at all; Gnosis names marketing inside a six-function placement list; **MANTRA names it inside a three-function set the firm says was hit harder than the rest.** Date confirmed to the day (2026-01-14 08:56 EST). Rationale: April-2025 events, downturn, competition. **AI absent from the capture.** Headcount refused — *"an unspecified number."*

⚠ **The limit is the finding's twin: both rows that name marketing are PERIMETER rows. No tracked-cohort firm has named marketing as an affected function in any of the 25.** That contrast is what ships — not a cohort-wide claim.

### 4. ✅ **RECOMMENDATION 3 EXECUTED — THE CLASS NO GUARD COULD INSPECT IS NOW INSPECTABLE. `NO-PUBDATE-FIELD`: 5 → 0.**

A machine-readable `**Published:**` + `**Published-provenance:**` pair was added to **all eight** class-4 files. `date-provenance-audit.py` class-4 verdicts move from **5 NO-PUBDATE-FIELD / 2 NO-URL / 1 LAG-EXCEEDED** to **4 NO-URL-DATE / 2 NO-URL / 1 LAG-EXCEEDED / 1 SELF-DATED**.

**🔴 State the limit before anyone reads that as progress it is not.** The dates were backfilled from what those files **already asserted**, not from fresh first-party fetches. **The change makes the class auditable. It does not make it verified.** Four of eight are now explicitly "auditable but uncorroborated" — which is a true statement the corpus could not previously make about itself, and a work queue, not a pass.

Two files remain 🔴 `NO-URL` and both were **hand-adjudicated rather than exempted**, per watch (tt): `sport-sponsorship-reset-2026-05.md` genuinely fails the class-4 storage rule and is marked **do-not-cite**; `_stale-article-as-current-signal-instrument-2026-08-20.md` is an instrument note, not an operator statement, and is annotated as exempt-by-kind **without weakening the guard's predicate.**

### 5. 🔴 **RECOMMENDATION 1 WAS BLOCKED BY ESCALATION (i) — THE RUN ROUTED AROUND IT, AND THE ROUTE DOES NOT COVER EVERYTHING.**

`web_fetch` refused the tracker's own committed URLs: *"URL not in provenance set."* **The single work item the last run named highest-yield was unreachable by the run that had committed the URLs.** Workaround: `WebSearch` the article to admit its URL, then fetch. **3 for 3.** But **rows 9 (X post), 10 (SEC EDGAR exhibit) and 17 (firm support-centre article) will not yield to it** — they stay unread through ship unless the prompt-provenance fix lands.

**Class 1: 0 net-new, guard-certified HEALTHY, delta +63. Class 2: byte-identical, 12th run, panel 68 days stale. Class 3: +1 ADMITTED at source, capture queue emptied, 9-run refusal closed. Class 4: 0 net-new, NINTH consecutive recall confirmation; storage defect repaired across all 8 files. Class 5: 0 promotions, tracker holds at 25 — 3 citations opened, 2 rows repaired, 1 row strengthened, 1 `[VERIFY]` closed, 1 `LAG-EXCEEDED` cleared.**

---

## Six-class audit trail

### 0. Retry-queue seed — not re-issued, per mandate item 4

One line, as instructed. Not re-issued. `OTHER.csv` not re-fetched. MAS not re-opened.

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

```
date: 2026-08-22   source A (jobs) scan_date: 2026-08-22
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-21T22:07:16Z, age=14.3h,
  fingerprint total_jobs_fetched=2259, delta=+63 vs 2026-08-21 (2196))
job postings ADDED: 0  firms: []
```

**Both predicates pass. The class-1 absence claim is PERMITTED and is made: the scan ran, it looked at 2,259 postings, and it found no net-new tracked-firm marketing role today.**

**Fingerprint delta +63 — the largest single-day move recorded.** Series now `2151 → 2151 (frozen) → 2186 → 2196 (+10) → 2259 (+63)`. Watch (rr) stays **downgraded**: 63 on a 2,196 base is 2.9%, still inside upstream-scope noise for a scan whose firm list changes. **Operational liveness only. Do not read Theme-5 signal into it.**

**Absence panel unchanged, 6 firms:** Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys. **Chrome work-queue unchanged, 6:** Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana. **Residual gap is bounded and known** (`scripts/README.md`).

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 68 days stale.** 18 agency-claims files written, **byte-identical for the twelfth consecutive run.** 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation.

**Watch (d), 18th run.** `methodology.md` §6 still describes this as a *"daily 18-agency panel."* **It is not daily and has not been for 68 days.** The sentence must be rewritten before ship or the report misdescribes its own instrument.

### 3. Regulator — **+1 ADMITTED AT SOURCE. THE CAPTURE QUEUE IS EMPTY. NINE-RUN REFUSAL CLOSED.**

Three first-party fetches, all HTTP 200, all listed in the audit trail below. Full record in `../regulator-filings/esma-finfluencers-factsheet-at-source-2026-08-22.md`, including six explicit non-claims.

**The date, stated as two quantities because the document asserts two:**

| Evidence | Asserts | Precision | Whose |
|---|---|---|---|
| ESMA path `/2026-01/` on all 36 files | published Jan 2026 | **month** | ESMA's own |
| CONSOB body *"Rome, 12 January 2026"* | CONSOB amplified 12 Jan 2026 | **day** | CONSOB's own |
| Colophon *"© ESMA, **2025**"*, cat. `EK-01-**25**-037-EN-N` | **produced** 2025 | year | ESMA's own |

**Ruling: produced 2025, published January 2026, amplified 12 January 2026.** **Watch (o) in its purest form — the copyright year is a property of the artifact, the path date a property of the publication, the CONSOB date a property of an event held about it.** No day-precision ESMA date is claimed. ⚠ ESMA's landing page carries **no visible publication date at all** — which is why nine runs failed, and is worth one line in the report about a regulator's own publication hygiene.

**NOT re-read today, deliberately: `NCASP.csv`.** The class-3 budget went to closing the queue. **The nineteenth-consecutive-zero stands as of 08-20 and is NOT restated as of today.** Watch (b) does not advance by the calendar.

**Search-only, not admitted:** an aggregator claim that the non-compliant register stands at 167 entries / 165 CONSOB — **the corpus's own 08-16 at-source figures**, returned to it by third parties, alongside a search result that was **northpoint.fi's own page**. **Circular. Not evidence. Not entered.** (Watch (ss): a result that agrees with us is the one to distrust.)

**Not reached, not guessed:** ESMA press release announcing the factsheet (would supply the missing day); the 35 translated PDFs; CONSOB's Italian original; ESMA's 2021 MAR social-media warning (out of window, cited *by* the factsheet).

### 4. Operator statements — **0 NET-NEW ADMITTED. NINTH consecutive recall confirmation. STORAGE DEFECT REPAIRED.**

Search returned only material the corpus already holds — **Crypto.com/Kalifowitz** (`cryptocom-kalifowitz-cmo-exit-primary-2026-08-11.md`) and **Kraken/Gupta** (`kraken-gupta-growth-operating-model-2026-05.md`). **2/2 cohort recall — the search is alive; the null is real, not an artefact of a dead query.**

**One candidate refused on role grounds and recorded so it is not re-discovered:** Crypto.com CEO **Kris Marszalek**'s verbatim enterprise-wide-AI statement. `methodology.md` §4 requires CMO / VP Marketing / Head of Brand / Head of Growth. **CEO ≠ marketing operator. Not admitted.** **Watch (l), 19th costing** — and note what it keeps costing: **the §4 perimeter refuses the most quotable AI-and-headcount material the corpus encounters.**

**Recommendation 3 executed across all 8 files** — see headline 4 for the result and the limit.

### 5. Layoffs — **0 PROMOTIONS. TRACKER HOLDS AT 25. Three citations opened; two rows repaired; one strengthened.**

Full record: `../layoff-tracker/_citation-opening-sweep-2026-08-22.md`.

| Row | Action | Result |
|---|---|---|
| 1 Crypto.com | citation opened | 🔴 **180 relabelled `[DERIVED — NOT FIRM-STATED]`**; `[VERIFY]` closed |
| 23 MVMT Labs | citation upgraded to the event article | `LAG-EXCEEDED` → `SELF-DATED`; **filing DAY still not first-party**, carried `[DATE-VERIFY]` |
| 25 MANTRA | citation opened | ⭐ **"affected more than others"** — strongest function-level sentence in the tracker; date confirmed to the day |

**Class-5 audit deltas: `LAG-EXCEEDED` 2 → 1; `SELF-DATED` 12 → 13; `NO-URL` holds at 1 (MARA, still flagged to strike if unsourced by ship).**

**Cross-verification bonus:** the Crypto.com capture — fetched for an unrelated row — **independently reproduces yesterday's Algorand repair**: same 25%, same verbatim rationale, same firm X post, second outlet. **The 08-21 repair holds under independent corroboration.** It also corroborates rows 2, 5 and 19.

**No net-new layoffs.** Search returned FalconX, Crypto.com, Gemini — all held.

**⭐ Source-quality observation for the methodology appendix:** the CoinDesk MVMT article **lists an AI system as co-author** (`meta-author_2: ai-boost`) and carries an AI disclaimer. **A report about AI's effect on crypto marketing is partly evidenced by articles that are themselves partly AI-generated.** Not a reason to reject it — CoinDesk discloses it, names a human editor, and published a same-day correction, which is more provenance than most citations in this corpus offer. **It is a reason to say so first.** Recommend extending the class-4 `capture_ai_disclosure` field to class 5.

### 6. NorthPoint longitudinal panel

`findings/longitudinal-2026-06.md` — day-52 shift appended. Panel itself unchanged (68 days stale, §2).

---

## Watch items

- **(b) First named post-deadline NCA marketing-side action** — **NOT ADVANCED, DELIBERATELY.** `NCASP.csv` not re-read. **The 08-20 nineteenth-consecutive-zero stands as of 08-20 and is not restated as of today.** The clock does not run on its own. **Today's class-3 admission is pre-deadline and does not touch it** — recorded explicitly so no reader infers otherwise.
- **(d) Agency panel staleness — 68 days**, byte-identical twelve runs running. **18th run.**
- **(e′) Cadence** — **✅ HELD. One-day gap; 6 of 10.**
- **(f) Friday nomination cadence** — **NOT TESTABLE TODAY (Saturday).** The two consecutive Friday failures (08-14, 08-21) stand unrepaired; `inbound-nominations.md` still does not exist; **ten days to ship.** Escalation (ii) carries at full strength.
- **(g) Coinbase n=1** — unchanged, not touched.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED. Still untested.** Today's three rows split 1 AI / 2 non-AI; three rows is not a test. **Do not print.**
- **(j) Senior-leader exits** — **ADVANCED IN CLOCK, ninth consecutive run, and earned:** the search returned two known cohort operators (2/2 recall), so the null is not an artefact of a dead query.
- **(l) §4 too narrow AND provenance-blind** — **🟢 THE PROVENANCE HALF IS CLOSED TODAY.** `**Published:**` now exists on all 8 files; `NO-PUBDATE-FIELD` 5 → 0. **The NARROWNESS half is not closed and cost the run again** — a verbatim, dated, AI-explicit CEO statement refused on role grounds. **19th costing. Stop costing it; decide it.**
- **(n) Full-range re-sweep of classes 3, 4, 5** — **🟢 SEVENTH CONSECUTIVE VINDICATION.** Class 3 produced the admission, class 5 produced two repairs and a strengthened finding, class 4 produced a structural fix. **Three classes, three kinds of return, zero fabrications.**
- **(o) Date the document, never an event held about it** — **🟢 ITS BEST PAYOUT TO DATE.** One document asserted a production year, a publication month and an amplification day, and **all three were recorded as distinct quantities instead of collapsed into one.** The nine-run refusal ended because a regulator's PDF dates itself in its own body text.
- **(oo) The "not fetched, not guessed" list is a work queue** — **🟢 FIFTH CONSECUTIVE PAYOUT, AND IT EMPTIED ITS OWN QUEUE.** Both capture-queue items from 08-11 closed in one run. **New oldest live entries:** `CASPS.csv` @18/08 (not re-read today), the ESMA press release announcing the factsheet (new, not located), **AscendEX** (eighth carry, still blocked by escalation (i)), **PIP Labs** (second carry).
- **(pp) A clean parse is not a complete capture** — not exercised today; no register CSV was captured. `verify-capture.py` not run — **stated rather than silently skipped.**
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — **🟢 PAID.** A search returned the corpus's own 167/165 figures via third parties **and northpoint.fi's own page**. Recognised as circular and refused. **We were nearly cited as a source for ourselves.**
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — **🟢 HONOURED, and it constrained us rather than a source.** Two class-4 files still flag `NO-URL` after today's work. **Both were adjudicated by hand and written down; neither was exempted by editing the predicate.** The tempting move — add an instrument-note exemption to the script — would have been a guard weakened by the person it inconvenienced.
- **🆕 (vv) 🔴 A NUMBER IN THIS TRACKER IS NOT SAFE UNTIL SOMEONE HAS READ ITS CITATION.** Algorand (08-21): advertised a percentage the corpus could not source. Crypto.com (08-22): carried a headcount the firm never stated. **Two of the three named class-5 examples in `README.md`, failed on consecutive runs, both caught only by fetching.** MANTRA moved the other way — the row **understated** what its citation supported. **The rule is not "uncited rows are suspect." It is: an unread citation makes the row wrong in an unknown direction.** Seven rows remain unread. **Presume them wrong until fetched.**
- **🆕 (ww) ⚠ PART OF THIS CORPUS IS EVIDENCED BY PARTLY AI-WRITTEN JOURNALISM.** A CoinDesk article in class 5 carries an AI co-byline and an AI disclaimer. **The report's subject is AI's effect on marketing; its evidence base is not outside that effect.** Disclose it in the methodology appendix and extend `capture_ai_disclosure` to class 5. **Saying it first is the same move as publishing the corpus.**
- **Unchanged and not re-narrated today:** (a), (c), (e), (i), (k), (m), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (bb)/(ff — CLOSED), (cc), (ee — **paid today; the 08-11 near-miss it produced became today's admission**), (gg), (hh), (ii), (jj — **cost the run again; see headline 5**), (ll), (mm), (nn), (qq), (rr — downgraded), (uu — **executing; 3 of 10 done**).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.3h, fingerprint 2196 → 2259, delta +63 vs 2026-08-21.**
2. Repo dedup pass: 08-21 record in full; `methodology.md`, `scripts/README.md`, `tracked-firms.md`; all 25 tracker rows via `csv.DictReader`; four directory indexes; the 08-11 CANDIDATE in full.
3. WebSearch — ESMA/BaFin/AMF/CONSOB/CySEC crypto marketing enforcement Aug 2026 → **no net-new primary**; surfaced the CONSOB finfluencer PR path.
4. WebSearch — ESMA crypto warning list Aug 2026 → **circular** (our own 167/165 figures + northpoint.fi). **Refused.**
5. WebSearch — MANTRA staff cuts Jan 2026 → admitted the article URL to the provenance set.
6. WebSearch — Movement Labs Chapter 11 → admitted the event-article URL.
7. **`web_fetch` The Block MANTRA → 200, full body.** Published 2026-01-14 08:56 EST, updated 09:12 EST. **"affected more than others"** captured verbatim.
8. **`web_fetch` CoinDesk MVMT → 200, full body.** `parsely-pub-date` 2026-07-21T17:54:40.853Z; AI co-byline and disclaimer observed.
9. WebSearch — crypto CMO / head-of-marketing Aug 2026 → **2/2 cohort recall, 0 net-new.**
10. WebSearch — crypto marketing layoffs Aug 2026 → **0 net-new**; admitted The Block Crypto.com URL.
11. **`web_fetch` The Block Crypto.com → 200, full body.** The "based on the company's previously disclosed headcount" sentence captured; Algorand cross-verification obtained as a by-product.
12. WebSearch — ESMA finfluencer factsheet (domain-restricted `esma.europa.eu`) → **ESMA's own document page located.**
13. **`web_fetch` CONSOB `pr_20260112` → 200, `application/pdf`, complete.** *"Rome, 12 January 2026."*
14. **`web_fetch` ESMA document page → 200, full body.** 36 language files enumerated; all paths `/2026-01/`.
15. **`web_fetch` ESMA `Finfluencers_factsheet_EN.pdf` → 200, `application/pdf`, complete document.** Six sections + colophon quoted verbatim.
16. `python3 scripts/date-provenance-audit.py` — run **three times**: baseline, after the class-4 backfill, after the tracker repairs. Deltas recorded in §4 and §5.
17. **`verify-capture.py`: not run — no register CSV was captured today.** Stated, not skipped silently.
18. **`web_fetch` on tracker URLs directly: BLOCKED** — *"URL not in provenance set."* See headline 5.
19. **`OTHER.csv`, MAS, retry queue: deliberately not attempted**, per mandate item 4.
20. **Not reached / not guessed:** see the §3 list. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-finfluencers-factsheet-at-source-2026-08-22.md` — **NEW. The run's shippable finding.** Three first-party captures; the three-way date adjudication; ESMA's verbatim text on paid-partnership labelling, crypto risk and the disclaimer point; the EEA-complete 36-file distribution fact; the addressed-to-non-licensees finding; the January-2026 cluster; **seven explicit non-claims.**
- `corpus/regulator-filings/esma-finfluencer-factsheet-consob-amplification-CANDIDATE-2026-08-11.md` — **UPDATED.** Marked **✅ PROMOTED / SUPERSEDED**, pointer to the successor. **Body retained unedited** as the corpus's cleanest worked example of watch (ee).
- `corpus/layoff-tracker/_citation-opening-sweep-2026-08-22.md` — **NEW.** Three citations opened; the provenance blocker and its workaround; the Crypto.com downgrade; the MVMT upgrade and its residual `[DATE-VERIFY]`; the MANTRA strengthening and its perimeter limit; the AI-co-byline observation; the seven rows still unread and which three cannot be reached.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **UPDATED.** Row 1 relabelled `[DERIVED]` + `[VERIFY]` closed; row 23 citation replaced + `[DATE-VERIFY]`; row 25 strengthened with verbatim. **Still 25 rows; zero promotions.**
- `corpus/operator-statements/*.md` — **ALL 8 UPDATED.** `**Published:**` + `**Published-provenance:**` added. `NO-PUBDATE-FIELD` 5 → 0. Two `NO-URL` files hand-adjudicated in place.
- `findings/longitudinal-2026-06.md` — day-52 shift appended.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json`, `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — date re-stamps / byte-identical rewrites (sync, 12th run).
- **Deliberately NOT written:** any restatement of the watch-(b) null as of today; any claim that today's admission is enforcement; any cohort-wide claim that marketing is disproportionately cut; any day-precision ESMA publication date; the 167/165 aggregator figures.

---

## Recommendation for next run

1. **🔴 KEEP OPENING CITATIONS — WATCH (vv). THREE MORE. Rows 14 (Gnosis), 15 (Luno), 8 (BitGo).** Two runs, two rows found carrying numbers no firm stated, one row found understating its own evidence. **The direction of the error is unpredictable, which is why reading them is not optional.** Use the search-then-fetch workaround; it is 3-for-3. **Rows 9, 10 and 17 are unreachable without the provenance fix — do not waste a run on them.**
2. **🟢 KEEP RUNNING WATCH (oo). Fifth consecutive payout; today it emptied its own queue.** New oldest live entries: `CASPS.csv` @18/08, the ESMA press release announcing the factsheet, **AscendEX** (eighth carry), **PIP Labs** (second carry).
3. **⚠ RE-READ `NCASP.csv` NEXT RUN AND ADVANCE WATCH (b) BY OBSERVATION.** It has not been read since 08-20. **The null is the report's Theme-4 spine and it is currently two days old and ageing by the calendar — the exact defect the 08-20 run closed.** One fetch, one `verify-capture.py` run, and the null is either re-earned or it is not.
4. **Do NOT re-fetch `OTHER.csv`. Do NOT re-issue the retry queue. Do NOT re-open MAS.** Unchanged. One line each.
5. **Escalate to Jukka — six items, in order:**
   - **(i) 🔴 NINE RUNS OLD, AND TODAY IT BLOCKED THE WORK THE LAST RUN CALLED HIGHEST-YIELD.** `web_fetch` refused **this repo's own committed URLs**. A search-then-fetch workaround got 3 of 10 rows open; **rows 9, 10 and 17 cannot be reached that way and will ship unread.** **Fix: paste the tracker's `source_url` values verbatim into the scheduled-task prompt.** One edit. Nine runs unchanged.
   - **(ii) 🔴 THE README'S FRIDAY PROMISE FAILED TWO CONSECUTIVE FRIDAYS AND SHIP IS IN TEN DAYS.** Not testable today (Saturday). No mailbox access; `inbound-nominations.md` does not exist. **Route the mailbox into a readable artifact, or amend the sentence — the second option takes thirty seconds and is honest.**
   - **(iii) 🟢 THEME 4 HAS ITS CLEANEST SENTENCE YET AND IT IS NOW ANCHORED, NOT INFERRED.** *In January 2026 ESMA published a factsheet on responsible financial promotion in 36 language versions covering every EU Member State and every EEA-EFTA state, naming volatile cryptocurrencies twice and telling promoters that "this is not investment advice" will not protect them. It is addressed, in the second person, to influencers. Not one sentence in it addresses a licensed firm.* **Ship it with the pre-deadline date and the "not legal advice" disclaimer attached, in the same paragraph.**
   - **(iv) 🔴 `README.md` HAS NOW HAD TWO OF ITS THREE ADVERTISED LAYOFF EXAMPLES FAIL INSPECTION ON CONSECUTIVE RUNS.** Algorand had no citation (08-21); **Crypto.com's 180 is the outlet's arithmetic, not a company disclosure (08-22).** The same lines are in the public `README-for-github.md`. **Fix both, and consider whether the third — Gemini -30% — should be fetched before ship rather than after someone else does it.**
   - **(v) ⚠ ONE DECISION CLOSES A WATCH THAT HAS COST NINETEEN RUNS.** `methodology.md` §4 admits only CMO / VP Marketing / Head of Brand / Head of Growth. It has now refused, among others, a verbatim dated CEO statement explicitly tying headcount cuts to enterprise-wide AI. **Either widen §4 to admit CEO statements *about the marketing function or about AI-driven headcount* — labelled as such — or stop recording the cost every run.** Both are defensible. **Nineteen runs of neither is not.**
   - **(vi) 🔴 `methodology.md` STILL NEEDS SIX SECTIONS REWRITTEN: §1, §3, §4, §5, §6, §7 — EIGHTEENTH run for §1.** §6's *"daily 18-agency panel"* now describes a file **68 days stale**. **§3 gains a fourth requirement today:** it must name the finfluencer factsheet as a distinct instrument class — regulator guidance to non-licensees — because that distinction is now load-bearing for Theme 4. **§5 must carry the `[DERIVED]` label on Crypto.com's 180 as well as `[PERIMETER]` on Algorand.** **Still the one thing in the repo that could embarrass the report.**
