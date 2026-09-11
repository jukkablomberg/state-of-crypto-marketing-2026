# State of Crypto Marketing 2026 — Cycle State

> **Active research cycle for SKILL v3 Cat F.** Public-source synthesis (NOT interview-based — pivoted May 4, 2026 per Jukka's instruction). This file is the source of truth for the daily branding task. Read first when generating any Cat F action.

**Started:** 2026-05-03
**Pivoted to public-source synthesis:** 2026-05-04
**Target ship date:** September 1, 2026 (Q3)
**Phase line amended 2026-09-11, later — PRODUCTION PASS.** Second external review scored the rebuilt object 7.4/10 ("execution, not concept": footer occlusion, Type 3 fonts, machine pagination, walls of copy, browser-printout references). Root cause of the first two was Chromium embedding variable fonts as Type 3 — replaced with static TrueType instances; `pdffonts` clean; footer presence rasterised and checked every build. Pagination done by hand; prose modulated into panels, cards, tables and a method grid; references un-underlined and balanced. `../publish-bundle-v4/` now 25 pp. Internal QA 8.4/10 on the reviewer's own sub-scores. Detail: `../HANDOFF-2026-09-10.md` top block.

**Phase line amended 2026-09-11 — EDITORIAL-DESIGN REBUILD.** External design review scored the 09-10 object 5.5/10 ("institutional minimalism without institutional authority"). Rebuilt the design layer, prose frozen: `../publish-bundle-v4/` now 24 pp — dark cover with the register motif (324 entities, computed at build), summary spread, fresh-page chapter openers, authored exhibits with "What to notice", titled sources, colophon, tagged PDF + bookmarks + metadata. Build is `build/render5.py`. One figure corrected at source (register: 124 / 38.3% / 68, canonical typed 123 / 38.0% / 69 — fix owed). Detail: `../HANDOFF-2026-09-10.md` top block; runbook `../publish-bundle-v4/PUBLISH.md`.

**Current phase (updated 2026-09-10, afternoon — V4 DRAFT BUILT):** 🔴 **Phase 4 — the growth-led v4 report EXISTS: `../publish-bundle-v4/` (report.pdf 16 pp, report.html, summary.pdf 2 pp, PUBLISH.md, build/).** Built from `corpus/_canonical/` only — `build/canon.py` asserts 26/25/23/25 and 9/5/1/1 against the tracker CSV at build time. Summary + 4 chapters (pp.3–10) + appendix (pp.11–16), six charts, seven pull-quotes, 41 numbered citations, NorthPoint light tokens. Two hostile audit rounds run; blocking findings closed. Open: Jukka's read; DE pushes `_canonical/` + cited corpus files to the public repo (Appendix F links 404 until then); 09-23 FCA v HTX one-sentence check; tagged PDF (ledger row 22) OPEN; Huobi/HTX merge (row 28) OPEN. Decisions taken in the build and the two `_canonical/` corrections owed are in `../HANDOFF-2026-09-10.md` (top block). **`publish-bundle/` is superseded.** Runs until 09-23 owe STEP 0 + one run-record line; **no loop edits the v4 bundle.**

**Superseded phase line (2026-09-09, late evening — JUKKA'S STANDING DIRECTIVE):** 🔴 **Phase 4 — GROWTH-LED REBUILD. Publishes 2026-09-24, morning, FIXED.** Jukka, once, in session: *"It will be the best report ever made about the subject… Compliance is shit. It should play a sideshow and growth, the companies and agencies the main role."* **Canonical contract: `../REPORT-DIRECTIVE-2026-09-09.md`, which outranks `synthesis-plan.md` (now history, its 11-unit ladder spent) and `../CORRECTION-LEDGER-2026-09-09.md` (the 25 verified corrections + Tier 0 + the dated schedule).** Structure v3: seven chapters, growth in 1–5, **compliance demoted to one descriptive chapter at 6 — no scoring, no article-by-article judgement, no enforcement null as a thesis** — 20–24pp. Draft outline for Jukka: `../DRAFT-OUTLINE-v3-2026-09-09.md`. **The date does not move again: work that cannot reach the bar is CUT, not slipped.** 🔴 **`publish-bundle/` is UNFROZEN and STALE — nothing publishes from it.** Tier 0 runs 09-10 before any prose: freeze one canonical dataset, re-extract the agency panel in full (**18 agencies · 162 dated entries · 88 distinct claimed clients, of which only 25 ever reached the corpus**), and **recompute the overlap matrix before any chapter states how many firms run multiple agencies** — the "exactly one overlap (Sui)" finding is probably an artefact of the same extraction filter. From then on every figure is derived, none typed.

**Superseded phase line (2026-09-09, evening):** 🔴 **Phase 3b — BUNDLE UNFROZEN, CORRECTION ROUND. Publish moves 15 September → 2026-09-24.** An external reviewer read the 44-page reader edition end to end and returned a structural critique; CoS verified the falsifiable allegations against the artefacts rather than accepting them, and **confirmed eleven of thirteen**. The publication-blocking ones: **MiCA Art. 68 is *Governance arrangements*, characterised four times as carrying marketing-communications obligations, while Arts. 7, 29 and 53 — the actual marketing-communications articles — appear ZERO times**; the "not approved by any competent authority" statement is scored "absent" against CASP surfaces though it is an offeror/issuer duty; Ch.1's enforcement null claims 27 member states swept daily where Ch.5 says six NCA indexes; 26 tracker rows are printed as "twenty-six firms" when they are 25 organisations including 3 closures; Ch.3 and Ch.6 print mutually exclusive readings of Robinhood and Uphold. **And the FCA stay did NOT lapse on 09-08 — Consent Order of Chief Master Shuman, 7 September, extends it to 22 September; it was published 94 minutes after the 09-08 run read the page and concluded the opposite. That correction is applied (`04` L85, `06` L29/L71, citation anchors).** Jukka's three calls: narrow the null now and sweep the remaining NCAs only if time allows; narrow until no legal claim is made and commission review for a v2; keep the title and fix the subtitle. **Contract for the round: `../CORRECTION-LEDGER-2026-09-09.md`** — 22 rows, dated schedule, 1 closed. **One gain from the new date: the FCA stay expires 22 September, so the outcome is knowable two days before publication rather than being an open `[VERIFY]` on publication morning.**

**Phase line amended 2026-09-10 (Jukka's read of the old report.pdf) — SPEC v4, and the report shrinks by ~70%.** Target cut from 20–24pp to **5–7pp + appendix**. The report now **opens with a Summary, not Chapter 1** ("if chapter 1 was supposed to get the reader excited, it failed miserably"). New shape: **Summary · 1 Regulation rewrote crypto marketing · 2 AI and the marketing function · 3 The agency stack · 4 Nobody will say who runs marketing · Appendix** — each with a one-sentence purpose, which is the fix for "we need to understand what this chapter is about". Old Ch.2 is **90% cut**; old Ch.5 **dissolves** (FCA v Huobi and "compliance as the offer" move into Ch.1; the register analysis moves to the appendix); the regulatory material in the agency chapter is cut entirely as "adding no value". Added: **NorthPoint branding + Built by JukkaBlomberg.com**, **six charts**, **press-scale pull-quotes**, and a **separate 2-page `summary.pdf`** — the thing that actually gets forwarded. Ch.1 leads with events and adds regulation as support, never the reverse: Gemini's 5 Feb exit from UK/EU/Australia, Binance's June EEA marketing wind-down, then the capture campaigns. Full spec: `../REPORT-SPEC-v4-2026-09-10.md`. **Two answers recorded there: (a) we are NOT sure Rafique's CMO role ended — OKX's own CMO page is 28 months stale and no dated transition document exists, which makes it the emblem of the disclosure void rather than a departure story; (b) "AI-efficiency is the dominant story of the year" keeps its four named firms and loses three words — "most frequent framing in this record" is true, "dominant story of the year" is not.**

**Phase line amended 2026-09-09, later the same evening — SECOND REVIEW ROUND, and CoS was the one who got something wrong.** The reviewer retracted three items (the Ch.6 attribution, the NUL claim, the narrow 35% allegation) and sharpened one into a finding CoS had missed. **Both new claims were verified at source and both hold.** (1) 🔴 **CoS overclaimed in saying the AI critique "does not survive contact with the document."** True of the narrow allegation; **false of the report's conclusions, which assert dominance three times without the taxonomy to support it** — L80, L316 and L649 (a section heading). Rigorous row-level grading and an unearned chapter-level conclusion sit in the same document; CoS defended the first and thereby excused the second. Repair keeps the novel finding — *AI was the most frequent frame in this documented event set, and a measurable part of it is not the firms' story* — and drops "dominant". (2) **The adjudicable denominator is 25, not 26**: `ai_cover_narrative_y_n` holds 16 `N`, 9 `Y`-variants and one `Y-ADJACENT` (MARA) that is neither — so **four defensible denominators now exist (26 rows · 25 adjudicable · 25 organisations · 23 layoff rounds) and the report uses one number for all four.** (3) **CoS adopted the reviewer's structural argument:** the ledger's first 22 rows fix instances, not the class; **Tier 0 is now to freeze a canonical dataset and derive every figure mechanically before any prose is touched.** **Jukka's decisions 4 and 5: narrow the report and keep 09-24; compress old Chapters 2–4 into ONE limits chapter** — *what the public record could not establish about marketing organisation, AI adoption and agency relationships* — which is the reviewer's own concession that this is a legitimate methodology finding, just not a state-of-market read. **New shape: 5 chapters, ≈15–18 pages.** The remaining-NCA sweep is **dropped** (the narrowing makes it unnecessary). Kill condition recorded: if Tier 0 on 09-10 shows the dataset conflicts need sources re-opened, the date moves and BTCHEL gets a private draft, not a publication.

**Superseded phase line (2026-09-09, midday):** **Phase 3 — FROZEN BUNDLE, awaiting publication (T-6). No scheduled exception remains.** The 09-09 run owed no unit and took none: STEP 0 plus one run-record line, exactly as the REMAINING RUNS row binds. **No chapter, report or bundle artefact was touched, and both bundle SHA-256 values were RECOMPUTED and match the frozen tripwire values in `PUBLISH.md`** — the freeze is verified this run, not assumed. Verifier exit 0, clean; its counts rose (15→16 active loops, 34→35 edges, 39→45 prompt checks) because the **Art Director** went live 06:44Z with E37, which also puts a second loop in the 15:07 slot until this one retires — per SYSTEM-MAP § 1 the two do not collide, and this run wrote nothing outside the project folder. Post-window check: six classes at zero, three drop-everything zeroes, feed HEALTHY for a third day (15.2 h, delta −1). Every layoff candidate the sweep surfaced (Luno, BitMEX/HDR, Crypto.com, Gemini) was **already a tracker row, checked by grep, not by memory**; the Bitget CMO interview was rejected on cohort grounds a second time. **BitMEX's cessation takes effect 2026-09-23, eight days after publication — a perimeter wind-down already on the record, not a report change.** Runs 09-10 → 09-14 are STEP 0 plus one line; Jukka publishes 09-15.

**Phase line as set 2026-09-08:** **Phase 3 — FROZEN BUNDLE, awaiting publication. The last scheduled change has come and gone without changing anything.** The 09-08 run took bounded exception (b), the **FCA v Huobi stay-expiry check**, and adjudicated it **NO CHANGE**: the FCA's own proceedings page reads `Last updated 26/08/2026`, its Key documents list still ends at the Order of Master Marsh dated 24 August 2026, and **no settlement, discontinuance, judgment or further extension is published**. The stay lapsed today without a published outcome — the state Chapters 5 and 7 already describe in the past tense. No chapter, report or bundle artefact was edited; both bundle SHA-256 values stand. **The Chapter 7 `[VERIFY]` tag is deliberately NOT cleared** — it promises a check on the *morning of publication*, and a reading seven days early cannot discharge it; `PUBLISH.md` check 1 carries the duty to Jukka. Verifier exit 0, no findings. Post-window check: six classes at zero, three drop-everything zeroes, feed HEALTHY (14.4 h, delta −35 — postings closing faster than opening, not a scanner fault). **No scheduled exception remains. Runs 09-09 → 09-14 are STEP 0 plus one run-record line; Jukka publishes 09-15.**

**Phase line as set 2026-09-07:** **Phase 3 — FROZEN BUNDLE, awaiting publication.** The 09-07 loop run made no change to any chapter, the report or the bundle. System-map verifier **exit 0 with no findings at all** (yesterday's `[DEPLOY] _meta ahead=5` line, another loop's, is gone). Post-window check: six classes at zero and three drop-everything zeroes — the one class-4 candidate (Bitget's CMO, crypto.news) was **rejected on cohort grounds**: Bitget is perimeter, not tracked, so it is non-admissible regardless of date. **The jobs feed RECOVERED after two stale days — 14.4 h, delta +6, the first non-zero delta in four days** — so the `scan_metadata` guard would now pass; no back-fill was made and none is owed, the class-1 exhibit stays frozen at 08-31. **Next scheduled change is the 09-08 FCA v Huobi check — tomorrow, and the last one before publication.**

**Phase line as set 2026-09-06:** **Phase 3 — FROZEN BUNDLE, awaiting publication.** The 09-06 loop run made no change to any chapter, the report or the bundle. Verifier exit 0 with one finding that belongs to another loop (`_meta` DEPLOY-STRANDED, already filed by the product-builder as `[NP-DEPLOY-BLOCK-VISIBLE]`). Post-window check: six classes at zero and three drop-everything zeroes — one class-4 candidate (Binance interim CMO Eowyn Chen, CoinGape, 18 Jul 2026) was fetched in full and found **already in the corpus and cited in Chapters 2 and 3**, so nothing was added; the fetch incidentally re-confirmed Chapter 5's "zero mentions of MiCA / EU / regulation" claim about that interview. **The jobs feed is STALE for a second day and worsening (62.3 h, delta +0, three days frozen), so the `scan_metadata` guard again refused the class-1 absence claim** — no report consequence, the exhibit is frozen at 08-31. Next scheduled change is the **09-08 FCA v Huobi check**.

**Phase line as set 2026-09-05:** **Phase 3 — FROZEN BUNDLE, awaiting publication.** The 09-05 loop run made no change to any chapter, the report or the bundle. System-map verifier exit 0 clean. Post-window check: six classes at zero, three drop-everything zeroes — and the **jobs feed went STALE (38.3 h, delta +0), so the `scan_metadata` cross-check guard refused the class-1 absence claim and none was written.** No report consequence: the class-1 window closed 2026-08-31 and the absence exhibit is frozen at that date. Next scheduled change is the **09-08 FCA v Huobi check**.

**Phase line as set 2026-09-04:** **Phase 3 — FROZEN BUNDLE, awaiting publication.** The 09-04 loop run made no change to any chapter, the report or the bundle: post-window check clean (six classes at zero, feed HEALTHY, three drop-everything zeroes), the re-date side duty confirmed already applied and closed, next scheduled change the **09-08 FCA v Huobi check**. The line below stands unedited.

**Phase line as set 2026-09-03:** **Phase 3 — FROZEN BUNDLE, awaiting publication.** All 11 of 11 units are done. The 2026-09-03 loop run took the cadence's bounded second-pass audit: the 30 PARTIAL and 9 NOT-OPENED adjudications from the 09-02 content audit were re-opened and closed, ten narrowings applied, and both bundle artefacts rebuilt (`report.html` 176 live links; `report.pdf` 44pp). The provenance gate stands at 250 URLs / 0 untraced and the report at 23,070 words ≈ 21.0pp of a 25pp budget. **No further edits to chapters, report or bundle except the 09-08 FCA v Huobi check. Publishes 15 September 2026 — Jukka's act.**

**Superseded phase line (2026-09-02):** **Phase 3 — citation audit, bundle, publish.** All seven chapters are drafted and the report is assembled at `report/state-of-crypto-marketing-2026.md` (21,740 words ≈ 19.8pp against a 25pp budget). Units 8 of 11 done; units 9–11 are the citation audit and the publish bundle. **Publishes 15 September 2026.**

**Phase history, stated honestly rather than tidied.** Phase 1 (corpus assembly) ran 2026-05-05 → 2026-08-31 and produced the corpus this report is built from. **Phase 2 (synthesis) did not run at all between 23 July and 1 September**: the synthesis prompt approved on 07-29 never reached the scheduled task, so 34 further daily runs collected corpus while chapters 2–7 went unwritten, and the advertised 1 September date passed with one chapter in existence. The full account is `../POST-MORTEM-2026-09-02.md`; the public re-date is `../PUBLIC-REDATE-2026-09-02.md`. Chapters 2–7 were drafted on 2026-09-02. This line stayed wrong for eight weeks and is part of why nobody noticed — a phase field that nothing updates is not a status, it is decoration.

---

## Cycle goal

Ship a 40-page operator-grade report — *State of Crypto Marketing 2026. Built from the public record.* — synthesised entirely from public sources across 30+ crypto marketing organisations. Every claim citation-anchored. The visibility filter is itself the analysis.

## Brand-build mechanism

1. The report is a permanent owned asset that compounds as it is cited — citation-anchored claims are easier for analysts and journalists to quote than anonymised interview reads.
2. Drip-released findings fuel Cat B essays for 12+ weeks at zero additional research cost.
3. Press push at ship time = 6-8 weeks of inbound trail.
4. The corpus itself becomes a public asset (likely shipped as a companion GitHub repo, satisfying Cat E for a future week).
5. The "regulator's reading" framing differentiates from every other industry report in the category.

---

## This week's drip target

**Week of May 3-9, 2026:** ✅ DRAFTED + STAGED + REWRITTEN — *State of Crypto Marketing 2026. Built from the public record.* Ship target: **Wed May 6** (next B-slot per v3 daily allocation). Files staged in `site/`; cross-post to Dev.to + Substack + Medium-via-import on ship day.

- Markdown: `./competitor-intelligence/content-drafts/2026-05-06-state-of-crypto-marketing-2026.md`
- Site HTML: `./branding/northpoint-renewal-2026/site/resources/writing/state-of-crypto-marketing-2026.html`
- Live URL (post-push): https://northpoint.fi/resources/writing/state-of-crypto-marketing-2026

**Article version history:**
- v1 (May 4 morning) — interview-based framing ("twenty-five interviews, anonymised by default"). Pulled before push.
- v2 (May 4 afternoon, current) — public-source synthesis framing ("built from the public record, citation by citation"). Currently staged.

**Last drip published:** ✅ 2026-05-06 — cycle-opener live across all 4 surfaces (northpoint.fi · Dev.to · Substack · Medium).

**2026-05-07 micro-drip (corpus infrastructure):** ✅ Pre-staged. (a) `./corpus/` tree created with job-postings/ (5 firm CSVs: Bybit, KuCoin, Crypto.com, Bitpanda, Bitstamp), agency-claims/, regulator-filings/, operator-statements/, layoff-tracker/. (b) `./corpus/layoff-tracker/2026-layoff-tracker.csv` seeded with 6 entries — Crypto.com, Gemini, Algorand, **Coinbase (May 5 -14% with Armstrong AI-native pod memo)**, Block, MARA. (c) Coinbase row in `tracked-firms.md` annotated with the May 5 signal — first Tier-1 to publicly name the operating model; spine of Theme 1 + Theme 5. Phase 1 corpus assembly is now click-and-paste from public sources.

---

## Corpus build status

| Source class | Status | Notes |
|---|---|---|
| Job postings (12 months × 30 firms) | 🟡 Scaffold ready (May 7) — 5 priority firms scaffolded | Bybit, KuCoin, Crypto.com, Bitpanda, Bitstamp CSVs created. Phase 1 fill starts week of May 11 (or pulled forward Sat May 9 if window opens). |
| Agency case studies (18 agencies) | 🟡 Partial — competitor-intelligence pipeline already captures this | Cross-reference matrix to be built in May |
| Regulator filings | 🟡 Partial — ESMA April 17, MiCA, MiCA delegated reg already in hand | Add MAS, VARA, FCA, public regulator-action register |
| Operator public statements (podcasts, conferences, LinkedIn) | 🟡 In progress — 2 entries (Conlan/Eowyn Binance signals May 13 + sport-sponsorship reset multi-incident cluster May 14) | 20+ podcast inventory still to transcribe-extract; cluster-style captures preferred for Theme 1 first read |
| Layoff tracker | 🟢 In progress — Crypto.com -12% / Gemini -30% / Algorand -25% / **Coinbase -14% (May 5 + AI-native pod memo)** / Block -4,000 / MARA -40 documented in `corpus/layoff-tracker/2026-layoff-tracker.csv` | Coinbase entry is the highest-signal 2026 datapoint for Theme 1 (function shape) and Theme 5 (next twelve months) |
| NorthPoint competitor-intelligence pipeline | 🟢 Continuous — 18-month panel already runs daily | Just continue |

---

## Tracked firms (substantive synthesis cohort)

See `./tracked-firms.md` — currently ~28 firms across exchanges, L1/L2 foundations, wallets, CASP-licensed firms; ~30 by end of May after gap-resolution.

---

## Companion GitHub repo

✅ **LIVE as of 2026-05-05:** https://github.com/jukkablomberg/state-of-crypto-marketing-2026 (MIT). README mirrors `methodology.md` + `tracked-firms.md` excerpts + open-call for nominations. Link added to the staged May 6 essay HTML and the markdown source — both surfaces will carry it on ship day.

## Current blockers

- None. Corpus build can start week of May 11 once May 6 essay ships.

---

## Drip log (rolling, weekly)

| Week | Drip published | Type | URL | Notes |
|---|---|---|---|---|
| May 3-9 | ✅ 2026-05-06 — State of Crypto Marketing 2026. Built from the public record. | announcement + methodology + open call for nominations | northpoint.fi · [Dev.to](https://dev.to/jukkablomberg/state-of-crypto-marketing-2026-built-from-the-public-record-1nmi) · [Substack](https://open.substack.com/pub/jukkablomberg/p/state-of-crypto-marketing-2026-built) · [Medium](https://medium.com/@jukkablomberg/state-of-crypto-marketing-2026-built-from-the-public-record-b4d67112c39e) | First drip — opens the cycle publicly. v2 (public-source synthesis framing). All 4 surfaces verified live May 6. |
| May 3-9 | ✅ 2026-05-07 — Coinbase named the model: AI-native pods are the new marketing org. | market-trigger essay (Coinbase 14% layoff + Armstrong AI-native-pod memo, May 5) | [northpoint.fi](https://northpoint.fi/resources/writing/coinbase-named-the-model) · [Dev.to](https://dev.to/jukkablomberg/coinbase-named-the-model-ai-native-pods-are-the-new-marketing-org-3ad1) · [Medium](https://medium.com/@jukkablomberg/coinbase-named-the-model-ai-native-pods-are-the-new-marketing-org-9802cd250e21) · [Substack](https://jukkablomberg.substack.com/p/coinbase-named-the-model-ai-native) | Second drip in 48h — market-trigger override of the Thu E/F default. Anatomy-of-the-pod cover image. Coinbase row in tracked-firms.md and layoff-tracker corpus carry the same May 5 signal. Two-essay cadence ✅ for Week 5. |
| May 11-17 | ⬜ 2026-05-14 — The sport-celeb era is over. What replaces it for crypto marketing. | market-trigger essay (Tour de Suisse cancels Zondacrypto + Crypto.com Travis McGhee exit on top of the post-Conlan / Kalifowitz / Coinbase wave) | northpoint.fi staged for push · Dev.to + Substack + Medium-import pending today | Pairs with the Cat F operator-statements capture (`./corpus/operator-statements/sport-sponsorship-reset-2026-05.md`) — the essay is the public version of the same Theme 1 first read. Five essays in seven days; sixth market-trigger override in 11 days. B drops back to 1/wk after Sun May 17. |

## Drip backlog (planned, weeks ahead)

- **Week of May 13:** First substantive finding — *Which Tier-1 exchanges have a publicly visible MiCA-marketing-comms seat?* (Theme 4 micro-essay; 800 words; cite each firm's public posting status)
- **Week of May 20:** *The agency-overlap matrix — what three agencies on one firm tells you about the gate-stack vacancy* (Theme 3 micro-essay; cite Bybit + KuCoin + Sui examples)
- **Week of May 27:** *AI in the stack — claimed adoption vs. JD-confirmed adoption across thirty firms* (Theme 2 micro-essay; cite specific JDs)
- **Week of June 3:** *Where the 2026 layoff cycle hit marketing first — and where it didn't* (Theme 5 micro-essay; cite Crypto.com / Gemini / Algorand earnings disclosures)
- **Week of June 10:** *The shape of the marketing function — split-IC pattern across thirty firms* (Theme 1 micro-essay; cite Bybit + Crypto.com + Gemini reorganisations)

Each drip is also a Cat B essay-grade ship (counts toward the 2/week B-cap when essay-quality, not just a research note).

---

## Phase 3 ship checklist (do not edit until Aug 15)

- [ ] All five theme syntheses drafted (Aug 1)
- [ ] Opening framing chapter + closing implications chapter drafted (Aug 8)
- [ ] Citation audit — every claim verified against primary source (Aug 15)
- [ ] Design pass + interactive HTML version (Aug 22)
- [ ] Regulator-readability review (Aug 25)
- [ ] Press kit drafted (CoinDesk, The Block, Decrypt, DL News, CryptoSlate) (Aug 27)
- [ ] Substack launch edition (Aug 29)
- [ ] Dev.to + Medium executive summaries (Aug 29)
- [ ] LinkedIn outreach to nominated-source contributors on ship day (Sep 1)
- [ ] PDF + interactive HTML version on northpoint.fi (Sep 1)
- [ ] Companion GitHub repo with corpus index (Sep 1) — Cat E credit for that week
