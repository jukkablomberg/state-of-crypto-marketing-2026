# Corpus-assembly daily run — 2026-08-23 **(day 53 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-23 (**Sunday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-22 recommendations:** (1) **open three more class-5 citations — rows 14 (Gnosis), 15 (Luno), 8 (BitGo)**, using the search-then-fetch workaround; do not waste the run on rows 9/10/17; (2) keep running watch (oo) — oldest live entries `CASPS.csv` @18/08, the ESMA press release, AscendEX, PIP Labs; (3) **re-read `NCASP.csv` and advance watch (b) by observation, not by the calendar**; (4) do **not** re-fetch `OTHER.csv`, do **not** re-issue the retry queue, do **not** re-open MAS; (5) six escalations to Jukka.
**Dedup baseline read before writing:** `2026-08-22-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md` in full; all 25 tracker rows via `csv.DictReader`; `corpus/`, `corpus/regulator-filings/`, `corpus/operator-statements/`, `corpus/layoff-tracker/` and `findings/` indexes; the stored `_esma-ncasp-snapshot-2026-08-16.csv` parsed field-by-field.
**✅ CADENCE: HELD. 08-22 → 08-23 is a ONE-DAY GAP. Watch (e′) improves to 7 of 10.** Corroborated from inside the data: today's class-1 fingerprint comparison is against **2026-08-22**, yesterday.

---

## Headline result

**All three mandated work items paid, and the run's two best findings both came out of documents opened for an unrelated reason. The mandate was executed in full; nothing was fabricated; one guard fired, was adjudicated by hand, and was proved right.**

### 1. ⭐ **THE THEME-4 SPINE IS RE-EARNED BY OBSERVATION — AND THE RE-READ PRODUCED A HARDER NUMBER THAN THE NULL.**

`NCASP.csv` re-read at source. ESMA's MiCA page states the interim register was **republished 21 August 2026**. The file is content-identical to the corpus's 08-16 capture on all six discriminators (167 rows, IT 165 / NL 1 / SK 1, same terminal rows, newest decision 22/07/2026, newest update 31/07/2026).

**The stronger null is therefore available and is claimed:** *ESMA republished this register two days ago and it still contains zero entries naming any tracked firm and zero entries alleging a marketing or promotional infringement by anyone.* **Watch (b) advances to a TWENTIETH consecutive zero, by observation.**

**🔴 And filtering it post-deadline gives Theme 4 a number it did not have.** Decisions on or after 1 July 2026: **five rows. All CONSOB. All unbranded promotional-domain clusters. None a licensee. None with a stated reason.**

| 08/07/2026 | Reversal Investment Group · Kortex |
| 22/07/2026 | Cervo Rendisco · Flandenzo · Corona Fondenza |

**Five entries in fifty-three post-deadline days, from one national authority out of thirty.** The register has not moved in thirty-two days despite four weekly republication cycles. **The deadline is not visible in this register.**

**⭐ And the sharpest sentence Theme 4 has produced to date:** `ae_infrigment` is `No` for **all 167 rows without exception**, and `ae_reason` is populated for **exactly one** — the AFM's MEXC entry: *"provides crypto-asset services in the Netherlands without the required MiCAR license… in breach of section 59 MiCAR."* **One hundred and sixty-seven entries; one explains itself; and that one is about an authorisation, not an advertisement.** → `../regulator-filings/esma-ncasp-post-deadline-composition-at-source-2026-08-23.md` (**NEW**).

### 2. ⭐ **A CLASS-5 VERIFICATION TASK PRODUCED THE RUN'S BEST THEME-2 EVIDENCE — AND A SOURCE KIND THE CORPUS DID NOT KNOW IT WANTED.**

Row 14's `[VERIFY]` — *"the single highest-value verification item in the corpus"*, open since 2026-07-30 — was closed by capturing Gnosis Ltd's own Q2-2026 quarterly report. **Inside that document, unrelated to the layoff, is a firm-published Marketing section:**

> *"We embedded AI across the marketing and comms function and saw this impact particularly our short form video (SFV) output and social media content improving our posting cadence while guarding quality."*

> *"In Q3 we will accelerate our progress in SEO / GEO… The focus for this will be Gnosis Pay where high quality content can support the generation of marketing-qualified-leads (MQL)."*

**Theme 2 is framed as claimed adoption vs. JD-confirmed adoption. This is a third side neither of those covers: what a firm writes down about its own marketing function in a routine periodic document, when it is reporting to token holders rather than talking to press or recruiting.** A named function, a named affected output, a named metric direction, and a volunteered quality caveat — more specific than most of what class 4 holds.

**🔴 And it does not fit `methodology.md` §4, which is the point.** §4 admits statements *by a titled operator at a tracked firm*. Gnosis is perimeter and the Marketing section names no one. **§4's perimeter is drawn around individuals, so it cannot see a firm's own published account of its marketing function.** Filed with that failure stated on its face rather than hidden by reclassification. → `../operator-statements/gnosis-q2-2026-quarterly-marketing-section-2026-07-17.md` (**NEW**). **This is watch (l) arriving from a new direction on its twentieth run.**

### 3. 🔴 **A THIRD ROW IN THREE RUNS WAS CARRYING A NUMBER NO FIRM STATED — AND TODAY THE PROPAGATION WAS CAUGHT IN THE ACT.**

Row 15, **Luno**. CoinDesk, verbatim: −20% is *"according to a report by Bloomberg"*, and *"CEO James Lanigan confirmed the cuts to Bloomberg but **declined to disclose the number of employees affected**."* **The firm confirmed the event; the magnitude is the reporter's.** Relabelled `[REPORTED BY BLOOMBERG]`.

Algorand (08-21, no citation) → Crypto.com (08-22, outlet's arithmetic) → **Luno (08-23, reporter's figure)**. And today's class-5 search returned `layoffhedge.com` titled **"Crypto.com Layoffs 2026 — 180 Jobs Cut"** — **the derived figure this corpus downgraded yesterday, already travelling through aggregators as a headline number.** The mechanism is now observed end to end: *a firm confirms an event, a reporter supplies a magnitude, the magnitude travels as though the firm had said it.*

**⚠ And a second label failed on the same row, with wider consequences.** Lanigan's word is **"automation."** Neither he nor CoinDesk says *AI* anywhere. `ai_cover_narrative` relabelled `Y [INFERRED]`. **If "automation" has been silently read as "AI" elsewhere, the AI-cover share — a Theme-5 headline number — is inflated.** Today's four opened rows show three different epistemic grades in one column: BitGo `Y` firm-stated · Dune `Y` firm-stated · Kraken `Y` anonymously sourced · Luno `Y` inferred. **The column needs a grade field or it must stop being counted.**

### 4. ⭐ **A FIGURE THAT HAD BEEN PUBLIC FOR THIRTY-FOUR DAYS WAS ONE SCROLL BELOW A DOCUMENT WE HAD DECIDED WE COULD NOT CAPTURE.**

Row 14's `headcount_change` read `undisclosed`. Kenk (Gnosis Ltd), 20 July 2026 3:37pm, answering a governance question that asked for it directly: ***"The App and Circles teams went from 28 to 14."*** −14 people, −50%, firm-stated, **team-scoped not company-wide.**

**Procedural rule adopted: when the primary is a forum or comment-bearing post, the thread is part of the primary source. Read the replies.**

### 5. 🔴 **THE WEAKEST CITATION IN THE TRACKER IS GONE — AND RETIRING IT CORRECTED A DATE IT HAD SILENTLY SUPPLIED.**

Row 8, **BitGo**, cited `cryptojobslist.com/crypto-layoffs`: a **rolling, undated aggregator page** whose contents change under the citation, and the same source class row 10 documents as unreliable. Replaced with The Block's canonical article; **the primary X post now has a durable URL**, closing a note open since 2026-06-28.

`date-provenance-audit.py` then raised a **DATE-INVERSION** on the row. **The flag was true** — and this is recorded emphatically because the guard's previous two DATE-INVERSIONs were both *script defects*. **It has now been wrong twice and right once, and the only way to know is to look (watch (tt)).** The 1-day gap was a UTC/EDT split, and the `2026-06-26` value had been **inherited from the aggregator**. Corrected to the publisher's date.

**🔴 The temptation refused:** widening the guard's tolerance to ±1 day would have silenced every timezone split. **That is a guard weakened by the person it inconvenienced.** Instead the convention was made explicit — *`date_announced` = the publisher's own stated date, in the publisher's own timezone* — and `DATE-INVERSION` returned to 0 **by fixing the corpus, not the tool.**

**Class 1: 0 net-new, guard-certified HEALTHY, delta +6. Class 2: byte-identical, 13th run, panel 69 days stale. Class 3: +1 ADMITTED at source; watch (b) advances to twenty by observation. Class 4: 0 §4-conforming net-new; TENTH consecutive recall confirmation; +1 new source kind admitted with its perimeter failure stated. Class 5: tracker 25 → 26; 3 citations opened, 1 aggregator citation retired, 1 date corrected, 2 figure labels weakened, 1 headcount recovered.**

---

## Six-class audit trail

### 0. Retry-queue seed — not re-issued, per mandate item 4

One line, as instructed. Not re-issued. `OTHER.csv` not re-fetched. MAS not re-opened.

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

```
date: 2026-08-23   source A (jobs) scan_date: 2026-08-23
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-22T21:52:37Z, age=17.0h,
  fingerprint total_jobs_fetched=2265, delta=+6 vs 2026-08-22 (2259))
job postings ADDED: 0  firms: []
```

**Both predicates pass. The class-1 absence claim is PERMITTED and is made: the scan ran, it looked at 2,265 postings, and it found no net-new tracked-firm marketing role today.**

Fingerprint series `2151 → 2151 (frozen) → 2186 → 2196 → 2259 → 2265 (+6)`. **Watch (rr) stays downgraded** — +6 on a 2,259 base is 0.3%, ordinary upstream noise. **Operational liveness only. Do not read Theme-5 signal into it.** Note for contrast: yesterday's +63 and today's +6 differ by an order of magnitude, which is itself the reason the delta predicate is a liveness test and not a measurement.

**Absence panel unchanged, 6 firms:** Aave, Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys. **Chrome work-queue unchanged, 6:** Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys, Solana. **Residual gap bounded and known** (`scripts/README.md`).

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 69 days stale.** 18 agency-claims files written, **byte-identical for the thirteenth consecutive run.** 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation.

**Watch (d), 19th run.** `methodology.md` §6 still calls this a *"daily 18-agency panel."* **It is not daily and has not been for 69 days. Nine days to ship.** Rewrite the sentence or the report misdescribes its own instrument.

### 3. Regulator — **+1 ADMITTED AT SOURCE. WATCH (b) ADVANCES TO TWENTY BY OBSERVATION.**

Full record with six explicit non-claims: `../regulator-filings/esma-ncasp-post-deadline-composition-at-source-2026-08-23.md`. See headline 1.

**`verify-capture.py` was run** — against the **stored 08-16 snapshot**: `COMPLETE`, exit 0, 167 data rows, 24,614 bytes, md5 `31bffda0e62c3f0f33ea24bcc7aeea4b`, final row 12 of 12 fields. **Watch (pp) exercised, not skipped.**

⚠ **Stated limit, and it is a real weakening.** Today's fetch arrived through a channel returning text, not bytes, so identity with the stored snapshot rests on **six discriminators, not md5**. **A hand-transcribed copy of today's fetch would be a fabricated artifact, not a capture, so none was written.** Discriminator-identity is weaker than byte-identity and is labelled as such in the record.

**Search-only, not admitted — and circular for the second consecutive run:** third-party pages reporting *"167 entries, 165 from Italy, none from BaFin"* (cryptoticker.io, casptracker.eu). **Those are this corpus's own 08-16 at-source figures returned to us.** Refused. **Watch (ss) — a result that agrees with us is the one to distrust.**

**Not fetched, not guessed:** `CASPS.csv` under the 21 August republication (**now the oldest live queue entry, and known-stale against a newer version**); the five post-deadline entities' underlying CONSOB resolutions; ESMA's *Description of the fields* CSV — **which would settle what `ae_infrigment: No` actually means. Until it does, the report must not lean on that column.**

### 4. Operator statements — **0 §4-CONFORMING NET-NEW. TENTH consecutive recall confirmation. +1 NEW SOURCE KIND.**

**🔴 The §4 search returned NorthPoint's own press release** (natlawreview, 2026-08-14, Jukka Blomberg on MiCA and AI-assisted marketing compliance) as its **top result**. **Refused, and recorded so it is not re-discovered.** Jukka is the report's author, not a tracked-firm operator.

**This is watch (ss) in its most uncomfortable form and it needs a line in the methodology appendix: the report's author now ranks in the search surface for the exact query the corpus uses to find operator statements. The instrument can see its own operator.** Every future class-4 search must be read with that in mind.

The remainder of the search returned only material already held. **10/10 cohort recall across the series; the null is real, not an artefact of a dead query.**

**+1 admitted as a new source kind** — the Gnosis quarterly Marketing section, filed with its §4 perimeter failure stated on its face (headline 2). **Watch (l), 20th costing.**

### 5. Layoffs — **TRACKER 25 → 26. Three citations opened; one retired; five changes.**

Full record: `../layoff-tracker/_citation-opening-sweep-2026-08-23.md`.

| Row | Action | Result |
|---|---|---|
| 8 BitGo | aggregator citation **retired** | 🔴 date corrected 06-26 → 06-25; durable primary URL closed; `Y` confirmed **firm-stated**; **~90 headcount REFUSED as arithmetic** |
| 14 Gnosis | `[VERIFY]` **CLOSED at source** | marketing claim **confirmed narrow**; ⭐ headcount recovered (28 → 14, team-scoped); 2nd Q2 restructuring surfaced as a lead |
| 15 Luno | citation opened | 🔴 −20% relabelled `[REPORTED BY BLOOMBERG]`; ⚠ `Y` relabelled `[INFERRED FROM "AUTOMATION"]`; market exit + white-label pivot captured |
| **26 Dune** | **NEW ROW** | ⭐ −25% **firm-stated verbatim by the CEO**; AI rationale **firm-stated** — the clean counter-example, found in the same run as the defects |

**Class-5 audit deltas:** `SELF-DATED` 13 → **15**; `NO-URL-DATE` 10 → **8**; `DATE-INVERSION` 1 → **0** (raised and cleared within the run); `NO-URL` holds at **1** (MARA — **still flagged to strike if unsourced by ship, nine days out**); `LAG-EXCEEDED` holds at **1**.

**No net-new layoffs beyond Dune.** Search returned Bitwise, FalconX, Coinbase, BitGo, Polygon, Luno — all held.

**Lead flagged, not admitted:** Blockworks and DL News both shut down their entire newsrooms in 2026. Crypto-media contraction adjacent to the content surface; **neither firm is in the cohort or the perimeter as defined. Needs a scope decision before admission.**

### 6. NorthPoint longitudinal panel

`findings/longitudinal-2026-06.md` — day-53 shift appended. Panel itself unchanged (69 days stale, §2).

---

## Watch items

- **(b) First named post-deadline NCA marketing-side action** — **🟢 ADVANCED TO TWENTY, BY OBSERVATION, NOT BY THE CALENDAR.** Re-read at source today against a register republished 21 August. **And it is now quantified rather than merely null:** five post-deadline entries, one authority, zero stated reasons, zero licensees. **The 08-22 refusal to restate it by the calendar was correct and is what made today's advance mean something.**
- **(d) Agency panel staleness — 69 days**, byte-identical thirteen runs running. **19th run. Nine days to ship.**
- **(e′) Cadence** — **✅ HELD. One-day gap; 7 of 10.**
- **(f) Friday nomination cadence** — **NOT TESTABLE TODAY (Sunday).** Two consecutive Friday failures (08-14, 08-21) stand unrepaired; `inbound-nominations.md` still does not exist; **nine days to ship.** Escalation (ii) carries at full strength. **Next Friday, 08-28, is the last one before ship.**
- **(g) Coinbase n=1** — unchanged, not touched.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED. Still untested.** Today's rows split 2 AI / 1 non-AI, and one of the AI labels turned out to be inferred. **Three rows is not a test, and today gave a reason to distrust the labels themselves. Do not print.**
- **(j) Senior-leader exits** — **ADVANCED, tenth consecutive run**, recall confirmed.
- **(l) §4 too narrow** — **🔴 20th COSTING, AND FROM A NEW DIRECTION.** Previously §4 refused *titled people at the wrong altitude* (CEOs). Today it could not accommodate **a firm's own published account of its marketing function**, because the perimeter is drawn around individuals. **The narrowness is now demonstrated twice over, two different ways. Escalation (v) should be decided with the Gnosis case in front of it.**
- **(n) Full-range re-sweep of classes 3, 4, 5** — **🟢 EIGHTH CONSECUTIVE VINDICATION, and the strongest yet: the run's best Theme-2 evidence came out of a class-5 verification task, and the run's best Theme-4 number came out of re-reading a file that was expected to have not changed.** Both of today's headline findings were by-products of doing mandated work properly.
- **(o) Date the document, never an event held about it** — **🟢 PAID TWICE.** Gnosis: decision (first week of July) and publication (17 July) recorded as distinct quantities. BitGo: publisher-local date vs UTC conversion adjudicated rather than collapsed, and the convention written down.
- **(oo) The "not fetched, not guessed" list is a work queue** — **🟢 SIXTH CONSECUTIVE PAYOUT.** Row 14's primary — carried as unreachable since 07-30 — was reached today by the search-then-fetch workaround. **New oldest live entry: `CASPS.csv` under the 21/08 republication, now known-stale.** Also live: ESMA's *Description of the fields* CSV (**new, and it gates a column the report might otherwise lean on**), the five CONSOB resolutions, **AscendEX** (ninth carry), **PIP Labs** (third carry).
- **(pp) A clean parse is not a complete capture** — **🟢 EXERCISED.** `verify-capture.py` run on the stored NCASP snapshot: COMPLETE, exit 0. ⚠ **And its limit was hit today:** the guard verifies a stored file; it cannot verify a fetch that never became a file. **Today's identity claim rests on discriminators, not md5, and says so.**
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — **🟢 PAID TWICE, AND THE SECOND ONE IS WORSE THAN THE FIRST.** (a) The 167/165 figures came back through aggregators again — refused. (b) **The class-4 search's top result was NorthPoint's own press release.** The corpus can now see its own author. **Methodology appendix.**
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — **🟢 ITS BEST PAYOUT YET, BECAUSE THIS TIME THE GUARD WAS RIGHT.** `date-provenance-audit.py` was wrong twice on 08-21 and right today. **Adjudicated by hand both times; believed neither time on reputation.** And the fix went into the corpus, not the predicate — **the ±1-day tolerance widening was available, obvious, and refused.**
- **(vv) A number in this tracker is not safe until someone has read its citation** — **🔴 FIVE-FOR-FIVE ACROSS THREE RUNS, AND TODAY IT FOUND A FOURTH DEFECT KIND: an unstable citation.** An aggregator page does not merely fail to support a row — **it silently populates it**, and it populated a wrong date. **Four reachable rows remain unread (2, 5, 12, 13). Row 2 is Gemini −30%: the last of the three README-advertised examples not yet inspected, and the other two both failed.**
- **🆕 (xx) ⚠ THE `ai_cover_narrative` COLUMN MIXES EPISTEMIC GRADES AND CANNOT BE COUNTED AS IT STANDS.** Four rows opened today carry `Y` on three different bases: firm-stated (BitGo, Dune), anonymously sourced (Kraken), inferred from *"automation"* (Luno). **The AI-cover share is a Theme-5 headline number. Add a grade field or stop printing a proportion.** Audit every `Y` row for the automation→AI substitution before Phase 2.
- **🆕 (yy) ⭐ WHEN THE PRIMARY IS A FORUM OR COMMENT-BEARING POST, THE THREAD IS PART OF THE PRIMARY SOURCE.** A firm-stated headcount sat public for thirty-four days, one scroll below a document the corpus had already ruled uncapturable. **Read the replies.** Add to the class-5 capture protocol.
- **Unchanged and not re-narrated today:** (a), (c), (e), (i), (k), (m), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj — **cost the run again on rows 9/10/17**), (ll), (mm), (nn), (qq), (rr — downgraded), (uu — **executing; 6 of 10 done**), (ww).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 17.0h, fingerprint 2259 → 2265, delta +6 vs 2026-08-22.**
2. Repo dedup pass: 08-22 record in full; `README.md`, `methodology.md`, `scripts/README.md`; all 25 tracker rows via `csv.DictReader`; five directory indexes; `_esma-ncasp-snapshot-2026-08-16.csv` parsed field-by-field.
3. WebSearch — Gnosis Ltd Q2 2026 quarterly report → **admitted the forum.gnosis.io URL to the provenance set.**
4. **`web_fetch` forum.gnosis.io Q2-2026 report → 200, full body**, `published_time 2026-07-17T14:32:46+00:00`. Leadership statement, Marketing section, and the 20/07 and 22/07 replies captured verbatim.
5. WebSearch — BitGo layoffs June 2026 → surfaced The Block; **the non-AMP URL was refused by provenance, the AMP URL was admitted.**
6. **`web_fetch` The Block BitGo (AMP → canonical) → 200, full body.** Belshe quote captured; Belshe X-post URL obtained; Q1 financials captured.
7. WebSearch — Luno 20% July 2026 → **admitted the CoinDesk URL.**
8. **`web_fetch` CoinDesk Luno → 200, full body**, `parsely-pub-date 2026-07-30T09:54:18.801Z`. The *"declined to disclose"* sentence and the *"automation"* quote captured; market exit and white-label pivot captured.
9. **`web_fetch` The Block Dune → 200, full body.** Haga quotes captured; row 26 admitted.
10. WebSearch — ESMA NCASP register (domain-restricted `esma.europa.eu`) → **admitted the MiCA page.**
11. **`web_fetch` ESMA MiCA page → 200, full body.** *"Last update: 21 August 2026"* captured at source; all five register file URLs admitted.
12. **`web_fetch` `NCASP.csv` → 200, `text/csv`, complete file.** Header + 167 rows + clean terminal row observed.
13. WebSearch — ESMA/BaFin/AMF/CONSOB/CySEC crypto marketing enforcement Aug 2026 → **no net-new primary; circular aggregator figures refused.**
14. WebSearch — crypto CMO / VP marketing Aug 2026 → 🔴 **top result was NorthPoint's own press release. Refused.**
15. WebSearch — crypto layoffs Aug 2026 marketing → **0 net-new**; caught the Crypto.com `180` propagating via layoffhedge.
16. `python3 scripts/verify-capture.py` on the stored NCASP snapshot → **COMPLETE, exit 0.**
17. `python3 scripts/date-provenance-audit.py` — run **three times**: baseline, after the row edits (**raised DATE-INVERSION on BitGo**), after the hand adjudication (**cleared**).
18. **`web_fetch` on `theblock.co/post/...` and on `NCASP.csv` before step 11: BLOCKED** — *"URL not in provenance set."* Both routed around by search-then-fetch. **Rows 9, 10, 17 cannot be routed around.**
19. **`OTHER.csv`, MAS, retry queue: deliberately not attempted**, per mandate item 4.
20. **Not reached / not guessed:** see the §3 list. **No URL was fabricated. No figure was entered that its source did not state.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-ncasp-post-deadline-composition-at-source-2026-08-23.md` — **NEW. The run's shippable class-3 finding.** The 21/08 republication; six-discriminator identity with the stored capture and its stated limit; the five-entry post-deadline table; the 167-entries-one-reason finding; **six explicit non-claims**; the `ae_infrigment` semantic gap flagged as a gate on the column.
- `corpus/operator-statements/gnosis-q2-2026-quarterly-marketing-section-2026-07-17.md` — **NEW. The run's shippable Theme-2 finding**, and a new source kind. Marketing section verbatim in full; the AI-embedding and SEO/GEO sentences; the B2C→B2B reorientation; **§0 states on its face why the file does not satisfy methodology §4**; five explicit non-claims.
- `corpus/layoff-tracker/_citation-opening-sweep-2026-08-23.md` — **NEW.** Three rows opened, five-defect-kinds table, the BitGo date adjudication in full including the refused tolerance widening, the Gnosis both-directions resolution, the Luno double downgrade, the Dune admission, the unread/unreachable split.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **UPDATED. 25 → 26 rows.** Row 8 citation retired + date corrected + primary URL closed; row 14 `[VERIFY]` closed + headcount populated + source promoted to the firm's own document; row 15 percentage and AI labels both weakened + source promoted; row 26 Dune added.
- `findings/longitudinal-2026-06.md` — day-53 shift appended.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json`, `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — date re-stamps / byte-identical rewrites (sync, 13th run).
- **Deliberately NOT written:** a hand-transcribed `NCASP` snapshot (would be a fabricated artifact, not a capture); the ~90 BitGo headcount; any claim that Gnosis disclosed a marketing cut in its quarterly report; any company-wide reading of the 28 → 14 figure; any causal link between Gnosis's AI adoption and its team reduction; the Blockworks/DL News rows; the 167/165 aggregator figures; any restatement of watch (b) beyond what today's fetch supports.

---

## Recommendation for next run

1. **🔴 FINISH THE CITATION SWEEP — WATCH (vv), FIVE-FOR-FIVE. START WITH ROW 2 (GEMINI −30%).** It is **the last of the three layoff examples advertised in the public `README.md` that has not been inspected, and the other two both failed.** Then rows 5 (Block Inc), 12 (OP Labs), 13 (Kraken). Search-then-fetch is now 6 for 6. **Rows 9, 10 and 17 remain unreachable — do not spend a run on them.**
2. **🔴 AUDIT THE `ai_cover_narrative` COLUMN END TO END — NEW WATCH (xx).** Every `Y` row, checked for the *automation → AI* substitution found on Luno today, and graded firm-stated / reported / inferred. **The AI-cover share is a Theme-5 headline number and it currently cannot be printed honestly.** This is the highest-value single sweep left before ship.
3. **⚠ RE-READ `CASPS.csv` UNDER THE 21 AUGUST REPUBLICATION** — it is now the oldest live queue entry and is **known-stale against a newer published version**, which is worse than merely old. One fetch, one `verify-capture.py` run. **And fetch ESMA's *Description of the fields* CSV in the same pass** — it gates what `ae_infrigment: No` may be claimed to mean.
4. **Do NOT re-fetch `OTHER.csv`. Do NOT re-issue the retry queue. Do NOT re-open MAS.** Unchanged. One line each.
5. **Escalate to Jukka — six items, in order:**
   - **(i) 🔴 TENTH RUN. IT BLOCKED THE WORK AGAIN, AND THE WORKAROUND HAS A HARD CEILING.** `web_fetch` refused this repo's own committed URLs again today; search-then-fetch got 3 more rows open (6 for 6), **but rows 9 (X post), 10 (SEC EDGAR exhibit) and 17 (firm support-centre article) cannot be reached that way and will ship unread.** **Fix: paste the tracker's `source_url` values verbatim into the scheduled-task prompt.** One edit. Ten runs unchanged. **Nine days left.**
   - **(ii) 🔴 THE README'S FRIDAY PROMISE — 08-28 IS THE LAST FRIDAY BEFORE SHIP.** Two consecutive Friday failures stand; no mailbox access; `inbound-nominations.md` does not exist. **Either route the mailbox into a readable artifact this week, or amend the sentence. The second takes thirty seconds and is honest.** After 08-28 the choice is made by default.
   - **(iii) 🟢 THEME 4 HAS A HARD NUMBER NOW, NOT A NULL.** *In the fifty-three days after MiCA's transitional period closed, the EU's register of non-compliant crypto-asset service providers gained five entries. All five came from one national authority out of thirty. None is a licensed firm. None states a reason. Of the register's 167 entries in total, exactly one explains itself — and it is about an authorisation, not an advertisement.* **Ship that paragraph with the 21 August republication date attached, because the date is what makes it a finding rather than a gap.**
   - **(iv) 🔴 `README.md` — THE THIRD ADVERTISED LAYOFF EXAMPLE IS THE ONLY ONE LEFT UNCHECKED, AND THE FIRST TWO BOTH FAILED.** Algorand had no citation (08-21); Crypto.com's 180 is the outlet's arithmetic (08-22). **Gemini −30% is next and should be fetched before ship rather than after a reader does it.** Both READMEs still carry all three lines uncorrected. **This is the one thing in the repo most likely to be checked by a hostile reader, because we published the corpus.**
   - **(v) ⚠ ONE DECISION, TWENTY RUNS, AND TODAY IT FAILED IN A SECOND WAY.** `methodology.md` §4 admits only CMO / VP Marketing / Head of Brand / Head of Growth **at a tracked firm**. It has refused a dated verbatim CEO statement on AI and headcount, and today it could not accommodate **a firm's own published quarterly account of its marketing function** — because the perimeter is drawn around job titles, not around statements about the function. **Either widen §4 to admit firm-published statements about the marketing function, labelled as such, or stop recording the cost every run.** Both defensible. **Twenty runs of neither is not.**
   - **(vi) 🔴 `methodology.md` STILL NEEDS SIX SECTIONS REWRITTEN: §1, §3, §4, §5, §6, §7 — NINETEENTH run for §1. NINE DAYS.** §6's *"daily 18-agency panel"* describes a file **69 days stale**. §3 must name the register's one-stated-reason structure. §4 must resolve escalation (v) and must carry the **author-in-the-search-surface** disclosure. §5 must carry `[DERIVED]` on Crypto.com, `[REPORTED]` on Luno, `[PERIMETER]` on Algorand, **and the `ai_cover_narrative` grading from recommendation 2.** **Still the one thing in the repo that could embarrass the report.**
