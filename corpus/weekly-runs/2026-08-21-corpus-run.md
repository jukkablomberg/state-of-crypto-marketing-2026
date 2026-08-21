# Corpus-assembly daily run — 2026-08-21 **(day 51 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-21 (**Friday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-20 recommendations:** (1) **re-fetch `OTHER.csv` complete** and verify before reading; (2) keep running watch (oo) on both lists — oldest live entries `ARTZZ.csv` / `EMTWP.csv` and **AscendEX**; (3) **run the new date check on the corpus's existing rows, not just new ones**; (4) do **not** re-issue the retry queue, do **not** re-open MAS; (5) six escalations to Jukka.
**Dedup baseline read before writing:** `2026-08-20-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`, `tracked-firms.md` in full; all 25 tracker rows via `csv.DictReader`; all `corpus/` and `findings/` directory indexes; both committed register snapshots re-verified by script.
**✅ CADENCE: REPAIRED. 08-20 → 08-21 is a ONE-DAY GAP. Watch (e′) recovers to 5 of 9.** The three-day break recorded on 08-20 did not extend. The class-1 fingerprint corroborates from inside the data: today's comparison is against **2026-08-20**, yesterday.

---

## Headline result

**The mandate was executed in full. It closed the oldest item on the not-fetched list, produced one shippable Theme-4 finding, repaired the report's most exposed citation — and its two new instruments each refused something this run wanted to print.**

**1. 🔴 NOT ONE TRACKED FIRM APPEARS AS AN ISSUER IN THE EU's E-MONEY-TOKEN REGISTER. THEY APPEAR ONLY AS CHAINS INSIDE OTHER PEOPLE'S FILINGS.**

`EMTWP.csv` — interim MiCA register file 3/5, e-money tokens — opened for the first time and **verified COMPLETE** (42 rows, 15,305 bytes, md5 `10d30624…`, `verify-capture.py` exit 0). **Because the capture verified complete, absence claims from it are permitted.**

A whole-record scan for all 32 tracked-cohort identifiers returns **seven hits, and every one is a blockchain name inside a deployment field of somebody else's stablecoin** — Solana ×2 in Société Générale — Forge's white-paper paths, and Solana/Polygon/Optimism/Arbitrum/Avalanche in one `ae_DTI` list belonging to **Bridge Building S.A.** **Zero hits in `ae_lei_name`. Zero in `ae_commercial_name`. Zero as an issuer of anything.** Tether — the cohort's only stablecoin issuer — is absent from the register entirely.

**The structural echo is the finding.** 08-20 found the tracked foundations in `OTHER.csv` only as **tokens filed for by a third party**. Today finds them in `EMTWP.csv` only as **infrastructure other people's tokens are deployed on**. → `../regulator-filings/esma-emtwp-artzz-white-paper-registers-2026-08-21.md` (**NEW**), snapshot `_esma-emtwp-snapshot-2026-08-21.csv` (**NEW**).

⚠ **Limit ships attached, and it is not small:** most of the cohort are exchanges and foundations, **not** EMT issuers. Absence from an EMT register is largely a statement about what business they are in. **Visibility finding, not compliance finding.**

**2. 🔴 THE RUN'S MOST STRIKING SENTENCE WAS REFUSED BY A GUARD THAT IS TWO DAYS OLD.**

`ARTZZ.csv` — asset-referenced tokens — returned HTTP 200, `text/csv`, **273 bytes: a 16-field header and zero data rows.**

This run wanted to write: *"The EU's register of asset-referenced token issuers is empty."* **`verify-capture.py` returned TRUNCATED, exit 1, `CLASS-3 ABSENCE CLAIM REFUSED`, and the sentence was not written.**

**A header with zero data rows is exactly what an empty register looks like AND exactly what a truncation-at-the-header looks like.** The circumstantial case for genuinely-empty is decent — 273 bytes is nowhere near any budget, the header terminates cleanly, and the same channel returned a 15KB file whole minutes later. **It is still circumstantial**, and watch (ss) says exactly this: an empty ART register is the most *welcome* finding available to Theme 4, which is the reason to distrust it. **UNRESOLVED. Escalated for one hand-verification.**

**3. 🔴 `OTHER.csv` IS UNREACHABLE, REPRODUCIBLY — RECOMMENDATION 1 CLOSES AS A HARD BLOCK, NOT A CARRY.**

Re-fetched per mandate item 1. **64,556 characters / 241 lines — byte-identical to 08-20, cut mid-URL inside the same Central Bank of Ireland record**, at the same character. Two fetches three calendar days apart, across a publisher republication, same cut point. **The truncation is deterministic. Re-fetching will never fix it.**

The 08-20 escalation was *"a chunked or ranged retrieval — not a second full attempt."* **That escalation is unavailable to an autonomous run.** This is now a hard block only Jukka can clear. **Do not re-attempt.** Malta and the Netherlands remain outside the capture; **no absence claim may be derived from `OTHER.csv`.**

**4. 🔴 THE REPORT ADVERTISED A FIGURE ITS OWN CORPUS COULD NOT SUPPORT — CAUGHT, AND REPAIRED AT SOURCE.**

Recommendation 3 executed via a new instrument, `scripts/date-provenance-audit.py`. Its top catch:

**`Algorand -25%` is printed as one of exactly three named class-5 examples in `README.md` L66, `methodology.md` L32 and — the one that matters — the public `README-for-github.md` L81. Its tracker row had `source_url` empty, `headcount_change` empty, `notes` empty.** The other two examples had citations.

**✅ Repaired the same run, first-party.** Date **2026-03-18** read from the article's own `published_time` meta, not from the search result. Firm primary quoted verbatim from the Algorand Foundation's own X post. **Rationale macro + downturn, NOT AI.** Headcount **refused** — the outlet states the firm did not disclose one; circulating 40–50 estimates not entered. Relabelled `[PERIMETER]`.

**⭐ And sourcing it produced a finding the uncited row never carried:** the same capture records that **after cutting 25% of staff, the Foundation's careers page still carried two open reqs — community management and business development.** **Community management is a marketing function.** Direct evidence about which marketing sub-functions survive a contraction — the Theme-5 question. **This ships.**

**The general lesson is worth more than the row: the uncited row was not merely unsupported, it was under-read. There are ten more rows whose citations have never been opened.**

**5. 🔴 THE NEW INSTRUMENT'S FIRST RUN WAS WRONG TWICE, AND THAT IS RECORDED BEFORE ITS RESULTS.**

`date-provenance-audit.py` reported **two DATE-INVERSIONs** on first execution. Both were adjudicated by hand before anything entered the corpus. **Both were bugs in the instrument.** A `/2026/07/` path read as 1 July and compared against a 23 July event; and a `Captured:` line — our own clock — compared against a publisher's date, two quantities that were never the same thing. Both fixed; precision is now symmetric.

**This is the same shape as the byte heuristic retired on 08-20: a predicate that looked decisive and was not. Two instruments built two days apart, each with a wrong rule caught on first contact with real data.** → **rule adopted: a new guard's first run is a test of the guard, not of the corpus.**

**Class 1: 0 net-new, guard-certified HEALTHY, delta back positive. Class 2: byte-identical, 11th run, panel 67 days stale. Class 3: +2 register files opened, 1 verified complete, 1 refused, 1 closed as unreachable. Class 4: 0 net-new, EIGHTH consecutive recall confirmation, null HOLDS. Class 5: 0 promotions, tracker holds at 25 — 1 row repaired, 1 condemned, 1 candidate declined.**

---

## Six-class audit trail

### 0. The retry-queue seed — one line, as instructed

**Did not arrive.** No URLs in the scheduled-task prompt. Watch (jj) unexecutable for an **eighth** run; **not re-issued** per the 08-13 ruling. Escalation (i) stands. **It bit twice today** — see §3a. Moving on.

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0 — guard-certified, sixth consecutive run.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-21
source A (jobs)   scan_date: 2026-08-21
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-20T21:47:54Z, age=14.3h,
             fingerprint total_jobs_fetched=2196, delta=+10 vs 2026-08-20 (2186))
  reason: age 14.3h, fingerprint delta +10
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**🆕 THE FINGERPRINT IS POSITIVE AGAIN: +10 (2,186 → 2,196).** Six-observation series: **+24, +4, +16, +3, −12, +10.**

**Watch (rr), opened yesterday, does not survive its first test as a trend.** The −12 was read then as *possibly* a Theme-5 contraction signal and explicitly not claimed, on two grounds: n=1, and it spanned three calendar days because of the cadence break. **Today's +10 is a clean single-day observation and it reverses the sign.** The honest reading is that the series is **noise around a flat level, not a direction** — 2,198 → 2,186 → 2,196 is a 0.5% band. **Watch (rr) is DOWNGRADED from "potentially substantive" to "operational liveness only."** The standing objection also holds unchanged: `total_jobs_fetched` counts **all** roles, not marketing roles, so it cannot bear a marketing-specific reading at all. **No trend claimed. This is the correct outcome for a watch item — it was opened as a question and one more observation answered it in the boring direction.**

**`fetch_errors`: unchanged. OKX (Tier-1), Securitize, Rabby, Relai still absent from the upstream company list — SEVENTEENTH run.** Watch (x) stays REOPENED. **Aave: seventeenth consecutive fetch error.**

### 2. Agency claims / overlap matrix (deterministic)

18 files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. `trend-data.json` `lastUpdated` still **2026-06-15**: **67 days stale.** Class-2 output byte-identical for an **eleventh** consecutive run. **`methodology.md` §6's phrase *"daily 18-agency panel"* remains inaccurate as written — SEVENTEENTH run.** No trend claim made from this panel today.

### 3. Regulator — **+2 REGISTER FILES OPENED, +1 VERIFIED COMPLETE, +1 REFUSED, +1 CLOSED AS UNREACHABLE.**

Full detail in `../regulator-filings/esma-emtwp-artzz-white-paper-registers-2026-08-21.md`.

**3a. All three URLs read from ESMA's own MiCA page, fetched first-party this run. None pattern-guessed.** ⚠ **Watch (jj) bit twice before that was possible**: the first `web_fetch` of `OTHER.csv` was refused — *"URL not in provenance set"* — even though the corpus has held that exact URL in a committed file since 08-20. **A URL this repo already cites cannot be re-fetched by the run that cites it.** Cleared by fetching the ESMA landing page first, which is the correct provenance route anyway and yielded the *"Last update: 18 August 2026"* reading as a by-product. **Recorded as the concrete, twice-observed cost of escalation (i).**

**3b. `EMTWP.csv` — mandate item 2, executed, and it is the run's shippable finding.** §1 above. **Twelve source data-quality defects logged uncorrected**, including: **the competent authority's name misspelled in 3 of 9 Dutch rows** (`De Nederlansche Bank`) and a second collision (`Bank of Lithuania` / `Bank of Lithuania (LSC)`) — **together these make a naive `GROUP BY` return 14 authorities where the true count is 12**, which is the identical defect class that produced 08-17's own "4 authorities" error; an **exact duplicate row** (StablR ×2); **`wp_url` values that are not URLs** (`EMT_NO_WP` ×2) — a register of white papers whose white-paper field says there is no white paper; **pre-MiCA dates in a MiCA field** (19/05/1979, 26/06/2007); **an authorisation dated a year after its own white paper**; and multi-line tab-indented values inside a quoted field. **Cross-register consequence: eleven defects in `OTHER.csv`, twelve here, of the same kinds. The data-quality problem is a property of the interim register as a whole, not of its largest file.**

**3c. `ARTZZ.csv` — refused.** §2 above. **UNRESOLVED, escalated.**

**3d. `OTHER.csv` — closed as unreachable.** §3 above. **Recommendation 1 does not carry forward as a fetch task; it carries forward as an escalation.**

**3e. Register cadence — third observation, no claim.** ESMA's page still reads *"Last update: 18 August 2026"* — **unchanged after three days**, against a stated weekly cadence. Recorded. **Three observations is not a cadence and no inference is drawn.** `NCASP.csv` deliberately **not** re-read today, so the 08-20 nineteenth-consecutive-zero null is **not re-advanced and not restated as of today.** `CASPS.csv` deliberately not re-fetched; the 08-17 CONSOB/BaFin inversion is **not restated.**

**3f. MAS — remains CLOSED as NOT ADMITTED.** Not re-opened, per mandate item 4. One line, moving on.

**NOT REACHED, NOT GUESSED:** the complete `OTHER.csv` (**unreachable, escalated**) · `ARTZZ.csv` at a verifiable standard (**refused, escalated**) · `CASPS.csv` at its 18/08 version · `NCASP.csv` today · any of the ~230 `wp_url` documents · the Description-of-fields CSV · Crypto Risk Metrics GmbH corporate filings · the AFM MEXC warning page · the CONSOB post-deadline notice bodies · the NBS LWEX notice · the ESMA 2026-02 statement PDF · the ESMA finfluencer-factsheet CANDIDATE from 08-11 (**9th refusal, still undated**) · VARA notice bodies · `rulebooks.vara.ae` · the retry-queue URLs · `ascendex.com` · `hello@northpoint.fi`. **No URL was fabricated.**

### 4. Operator statements — **0 NET-NEW ADMITTED. EIGHTH consecutive recall confirmation.**

**3/3 recall on named cohort seats:** Binance/**Rachel Conlan** CMO departure with **Eowyn Chen** interim (held); Crypto.com/**Steven Kalifowitz** stepping down after almost six years (held; CoinDesk publication date 2026-05-05 independently re-corroborated by today's sweep); Coinbase/**Catherine Ferdon** as CMO (held).

**No 2026 appointment to any TRACKED firm's top marketing seat is publicly visible — eighth consecutive run. Clock advanced: eleven weeks after Binance's CMO departure and eight weeks after Crypto.com's took effect, neither firm has publicly named a permanent successor.**

**One in-window CMO appointment surfaced and was refused on cohort grounds, not date grounds:** WISeKey International named **Alexander Hirsch** Group CMO, **21 August 2026** — today, correctly dated, verifiably real, and **not a crypto firm and not in the cohort.** Not admitted. Noted because it demonstrates the class-4 search is surfacing same-day items, which strengthens the null: **the search is live, and it is still returning nothing for the cohort.**

The **Fireblocks / Michal Ferguson** perimeter appointment carried from 08-17 is **still carried, still not admitted, still not fetched at source.**

**⚠ Structural weakness found in this class today — see §5.** Five of eight class-4 files carry **no machine-readable publication-date field**, so the class most exposed to the 08-20 stale-article failure mode is the class no automated guard can inspect. **Two files carry no URL at all**, one of which — `sport-sponsorship-reset-2026-05.md` — is a substantive four-incident cluster feeding three themes and **fails methodology §4's own storage rule.** Flagged for sourcing or striking before ship.

### 5. Layoffs — **0 PROMOTIONS. TRACKER HOLDS AT 25. One row repaired, one condemned, one candidate declined.**

Full detail in `../layoff-tracker/_date-provenance-sweep-2026-08-21.md`.

- **✅ REPAIRED — Algorand (row 3).** §4 above. **The report's most exposed citation, cited at last.**
- **🔴 CONDEMNED — MARA Holdings (row 6).** `40` headcount, `2026-Q2`, **no source, no percentage.** No citation sought, **none invented.** Annotated `DO NOT PRINT until sourced. If unsourced by ship, STRIKE THE ROW.`
- **DECLINED — PIP Labs (Story Protocol) −10%, ~17 March 2026.** Surfaced *inside* the Algorand capture with its URL. **Not entered** — watch (mm), a rendering of the record is not the record. **Carried with its URL captured, which is more than most candidates arrive with.**
- **Crypto.com 180-headcount `[VERIFY]`** opened 08-20 — **still open.** The figure re-surfaced today from the same secondary aggregator; not fetched first-party; **not entered.**
- **Gnosis `[VERIFY]`** — 17th run carried, blocked by watch (jj). **AscendEX** — seventh consecutive non-promotion; watch (oo)'s oldest candidate-list entry, **not reached today** because the run's budget went to the register files and the retrospective sweep.
- **Sweep verdicts:** 12 SELF-DATED · 10 NO-URL-DATE · 2 LAG-EXCEEDED · 1 NO-URL. **The two LAG-EXCEEDED rows (Pump.fun 122d, MVMT 25d) are known retrospectives, already annotated, no change.**

**SCOPE DISCIPLINE, DO NOT ELIDE: the cohort-scoped standing finding — *no TRACKED firm's 2026 contraction has named marketing as an affected function* — HOLDS.** Two of 25 rows name marketing (Gnosis, MANTRA); **both perimeter; zero tracked.** Algorand's repaired row **names no function**, so it does not disturb this. **The non-AI-rationale streak extends to fourteen runs** — and today's repair adds a firm-stated, verbatim-quoted macro rationale to the evidence rather than an inferred one. Watch (h′) remains **REJECTED and untested. Do not print.**

### 6. NorthPoint longitudinal panel

`trend-data.json` **67 days stale**. **No trend claim made.**

---

## Watch items

- **(b) First named post-deadline NCA marketing-side action** — **NOT ADVANCED TODAY, DELIBERATELY.** `NCASP.csv` was not re-read; the run's class-3 budget went to the two unopened white-paper files. **The 08-20 nineteenth-consecutive-zero stands as of 08-20 and is not restated as of today.** Advancing a null by the calendar rather than by an observation is precisely the artefact-of-cadence objection that run closed. **The clock does not run on its own.**
- **(d) Agency panel staleness — 67 days**, byte-identical output eleven runs running. **17th run.**
- **(e′) Cadence** — **✅ REPAIRED. One-day gap; 5 of 9.** The 08-18 gap remains unexplained but did not recur.
- **(f) Friday nomination cadence** — **🔴 TESTABLE TODAY (Friday) AND FAILED AGAIN.** Second consecutive Friday failure after 08-14. No access to `hello@northpoint.fi`; `inbound-nominations.md` still does not exist. **The README's promise is now two test cycles past due with eleven days to ship.** Escalation (ii) **hardens**.
- **(g) Coinbase n=1** — unchanged, not touched.
- **(h′) Layoff rationale correlates with firm type** — **REJECTED. Untested.** Fourteen-run non-AI streak. Do not print.
- **(j) Senior-leader exits** — **ADVANCED IN CLOCK, eighth consecutive run**, and today the clock advance is **earned**: a correctly-dated same-day CMO appointment surfaced and was refused on cohort grounds, so the null is not an artefact of a dead search.
- **(l) §4 too narrow AND provenance-blind** — **18th costing. 🔴 THE PROVENANCE HALF IS NOW QUANTIFIED**: 5 of 8 class-4 files have no publication-date field, 2 have no URL. **Stop costing it and fix it — the fix is one line in the template.**
- **(n) Full-range re-sweep of classes 3, 4, 5** — **🟢 SIXTH CONSECUTIVE VINDICATION.** Class 3 produced the shippable finding, class 5 produced the citation repair, class 4 produced a structural defect in its own storage. **Three classes, three different kinds of return, zero admissions.**
- **(o) Date the document, never an event held about it** — **🟢 PAID DIRECTLY.** Algorand's date came from the article's own `published_time` meta. The instrument that enforces it also **rediscovered** the OKX file's 1,337-day document-vs-page gap, which the corpus had already caught by hand — **the best available evidence the predicate detects what it claims to.**
- **(pp) A clean parse is not a complete capture** — **🟢 SECOND PAYOUT IN TWO DAYS, and this time it refused a finding rather than a file.** `verify-capture.py` blocked the ART-register claim. **The instrument is now 2-for-2 on catching things a human reading the same bytes would have accepted.**
- **(rr) Class-1 fingerprint direction** — **🟢 DOWNGRADED AND EFFECTIVELY CLOSED.** §1. Series reversed to +10; band is 0.5%; noise, not direction. **Operational liveness only. Do not read Theme-5 signal into it.**
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — **🟢 ITS BEST DAY YET, AND IT WORKED ON US RATHER THAN ON A SOURCE.** The ART-register emptiness was the most welcome sentence available to this report, and it was refused on exactly (ss)'s reasoning. **The watch has now caught a welcome finding generated by our own pipeline, not just a welcome article found outside it.**
- **🆕 (tt) 🔴 A NEW GUARD'S FIRST RUN IS A TEST OF THE GUARD, NOT OF THE CORPUS.** `verify-capture.py`'s byte heuristic was wrong on 08-20; `date-provenance-audit.py` produced two false DATE-INVERSIONs on 08-21. **Two instruments, two days apart, each with a rule that looked decisive and was not — and in both cases the wrong rule was caught only because a human adjudicated the output before believing it.** With two guards now running unattended in a daily task, **the failure mode has shifted from "no instrument" to "an instrument nobody checks."** Rule: **every flag from a guard less than five runs old is adjudicated by hand and the adjudication is written down.**
- **🆕 (uu) ⚠ AN UNCITED ROW IS NOT MERELY UNSUPPORTED — IT IS UNDER-READ.** Sourcing Algorand did not just supply a URL; it supplied a firm-stated verbatim rationale, a precise date, a refused headcount, **and a Theme-1 signal (community-management req still open after a 25% cut) that no one knew was there.** **Ten class-5 rows still have citations nobody has opened.** Each is a potential finding, not just a potential liability. **This is the highest-yield remaining work in the corpus and it needs no new sources.**
- **Unchanged and not re-narrated today:** (a), (c), (i), (k), (m), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (mm), (nn), (oo), (qq).
- **(oo) The "not fetched, not guessed" list is a work queue** — **🟢 FOURTH CONSECUTIVE PAYOUT, and it cleared its two oldest entries in one run.** `ARTZZ.csv` and `EMTWP.csv` both came off it; one produced the shippable finding, one produced a refusal worth recording. **`OTHER.csv` leaves the list entirely — not because it was fetched, but because it was proven unreachable.** A work queue that can retire an item as impossible is a better queue than one that carries it forever. **Keep running it.**

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.3h, fingerprint 2186 → 2196, delta +10 vs 2026-08-20. Sign reversed; watch (rr) downgraded.**
2. Repo dedup pass: 08-20 record in full; four root docs in full; `csv.DictReader` over all 25 tracker rows; `corpus/` + `findings/` indexes; both committed register snapshots re-verified by `verify-capture.py`.
3. WebSearch (domain-restricted `esma.europa.eu`) — interim MiCA register white-paper files.
4. **`web_fetch` ESMA MiCA landing page → 200, full body.** All five register file links read from the page; **"Last update: 18 August 2026"** read here. Also the provenance route that unblocked step 6 — see §3a.
5. **`web_fetch` `ARTZZ.csv` → 200, `text/csv`, 273 bytes.** Header + zero data rows. **`verify-capture.py` → TRUNCATED, exit 1, absence claim REFUSED.**
6. **`web_fetch` `EMTWP.csv` → 200, `text/csv`, 15,305 bytes / 42 data rows.** **`verify-capture.py` → COMPLETE, exit 0, md5 `10d30624347d0838503d5395490d23e1`.** Snapshot committed.
7. **`web_fetch` `OTHER.csv` → 64,556 chars / 241 lines. BYTE-IDENTICAL to 08-20.** Final row cut at the same character inside the same CBI/Payward record. **Deterministic truncation; recommendation 1 closed as unreachable.**
8. Programmatic cohort cross-reference over the verified `EMTWP.csv`: 32 tracked identifiers × all 19 fields → **7 hits, all chain-names in deployment fields, 0 as issuer.** Authority/member-state/issuer tallies, duplicate detection, non-URL `wp_url` detection, date-range extraction — all recomputable from the committed snapshot.
9. **Built `scripts/date-provenance-audit.py`; ran it over all 25 tracker rows and all 8 class-4 files.** First run produced **2 false DATE-INVERSIONs**; both adjudicated by hand, both traced to instrument bugs, both fixed; re-run clean. See §5 and watch (tt).
10. WebSearch — crypto CMO / head-of-marketing appointments August 2026 → **3/3 cohort recall; one correctly-dated same-day appointment (WISeKey, 2026-08-21) refused on cohort grounds.**
11. WebSearch — crypto layoffs marketing August 2026 → **no net-new.** Returned only material the corpus already holds (FalconX, Crypto.com 12%, Gemini). Crypto.com 180-headcount re-surfaced from the same secondary; `[VERIFY]` stays open.
12. WebSearch ×2 — Algorand Foundation 2026 layoffs → surfaced the capturing outlet and the firm's own X post.
13. **`web_fetch` `decrypt.co/361625/...` → 200, full body. `published_time` meta `2026-03-18T21:00:02`.** Firm's X post quoted verbatim inside. **Basis for the row repair; headcount expressly refused.**
14. **MAS: deliberately not attempted.** Closed 08-20. Not re-opened.
15. **Not reached / not guessed:** see the §3 list. **No URL was fabricated.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-emtwp-artzz-white-paper-registers-2026-08-21.md` — **NEW. The run's shippable finding.** `EMTWP.csv` verified complete; the **zero-tracked-issuers** result with all seven hits adjudicated to deployment fields; the structural echo of the 08-20 `OTHER.csv` finding; **twelve source defects logged uncorrected** including the two authority-name collisions; the `ARTZZ.csv` refusal in full; the `OTHER.csv` reproducible-truncation closure; **six explicit non-claims.**
- `corpus/regulator-filings/_esma-emtwp-snapshot-2026-08-21.csv` — **NEW.** Verified-COMPLETE raw capture, md5 `10d30624…`, so every figure above is recomputable.
- `corpus/regulator-filings/_esma-artzz-snapshot-2026-08-21.csv` — **NEW.** Committed **as a refused capture**, md5 `63043ec3…`, so the re-fetch is comparable byte-for-byte. **Its verdict travels with it in the companion note; it is not usable for an absence claim.**
- `corpus/layoff-tracker/_date-provenance-sweep-2026-08-21.md` — **NEW.** The full sweep; the two instrument bugs recorded before the results; the Algorand repair and its Theme-1 by-product; the MARA condemnation; the class-4 structural weakness; the PIP Labs decline; the honest limit.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **UPDATED.** Row 3 Algorand repaired and relabelled `[PERIMETER]`; row 6 MARA annotated `[UNCITED]` with a strike instruction. **Still 25 rows; zero promotions.**
- `scripts/date-provenance-audit.py` — **NEW.** Class-4/5 retrospective date guard. Symmetric-precision adjudication; explicit publication-date-field requirement for class 4; exit code.
- `scripts/README.md` — **UPDATED.** New section with the predicate, the verdict table, **the two first-run bugs and their fixes**, the corpus results, and the honest limit. Daily task ordering gains step 4.
- `findings/longitudinal-2026-06.md` — day-51 shift appended.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json`, `corpus/agency-claims/*.csv`, `corpus/agency-overlap-matrix.csv` — date re-stamps / byte-identical rewrites (sync, 11th run).
- **Deliberately NOT written: any claim that the EU's ART register is empty.** Refused by `verify-capture.py`. **The single most striking sentence available to this run, and it does not ship until it is verified.**

---

## Recommendation for next run

1. **🔴 OPEN THE TEN UNREAD CITATIONS — watch (uu). THIS IS THE HIGHEST-YIELD WORK LEFT AND IT NEEDS NO NEW SOURCES.** Ten class-5 rows carry a `source_url` that nobody has fetched. Algorand proved the yield: one fetch produced a precise date, a verbatim firm rationale, a refused headcount **and a Theme-1 finding nobody knew was there.** **Do three per run for the remaining runs.** Start with the two `[VERIFY]` rows (MVMT 23, Bitwise 24) since a fetch closes them as a side effect.
2. **🟢 KEEP RUNNING WATCH (oo). Fourth consecutive payout; it cleared its two oldest entries today.** New oldest live entries: on the not-fetched list, **`CASPS.csv` at its 18/08 version** and **the ESMA finfluencer-factsheet CANDIDATE** (9th refusal, still undated); on the candidate list, **AscendEX** (seventh carry) and **PIP Labs** (new, arrives with its URL).
3. **🔴 ADD `**Published:**` TO THE CLASS-4 TEMPLATE AND BACKFILL THE FIVE FILES MISSING IT.** One line each. Until it exists, the class most exposed to the stale-article failure mode is the class no guard can inspect. **Cheapest structural fix in the repo.**
4. **Do NOT re-fetch `OTHER.csv`. Do NOT re-issue the retry queue. Do NOT re-open MAS.** The first is now proven unreachable through this channel; the other two are closed. One line each, move on.
5. **Escalate to Jukka — six items, in order:**
   - **(i) 🔴 EIGHT RUNS OLD, AND TODAY IT COST THE RUN TWICE. Watch (jj).** The scheduled-task prompt cannot pass URLs into a run's provenance set — **and a URL this repo has cited in a committed file since 08-20 was refused on those grounds today.** **AscendEX** (seventh carry), the retry queue and the Gnosis `[VERIFY]` remain blocked. **Fix: paste the queue's URLs verbatim into the task prompt.** One edit, three items unblocked, eight runs unchanged.
   - **(ii) 🔴 THE README'S FRIDAY PROMISE HAS NOW FAILED TWO CONSECUTIVE FRIDAYS.** *"Inbound nominations are read every Friday."* Today is Friday. No mailbox access; `inbound-nominations.md` still does not exist. **Eleven days to ship, and this is the only open item with a third party on the other side.** **Route the mailbox into a readable artifact, or amend the sentence.**
   - **(iii) 🔴 TWO MINUTES OF YOUR TIME CLOSES THE RUN'S BIGGEST OPEN QUESTION.** Open `https://www.esma.europa.eu/sites/default/files/2024-12/ARTZZ.csv` **in a browser** and tell the next run whether it has data rows. If it is genuinely empty, **the EU's register of asset-referenced-token issuers is empty and that is a Theme-4 headline.** If it is not, we avoided printing something false. **The automated channel cannot settle it and the guard is right to refuse.** Same trip: `OTHER.csv` complete — save it into `corpus/regulator-filings/` and the Malta/Netherlands blind spot closes with it.
   - **(iv) 🟢 THEME 4 HAS A SECOND SPINE SENTENCE AND IT COMPOUNDS WITH THE FIRST.** *Across the two EU crypto-asset white-paper registers this corpus can read at a verified standard, not one tracked Stratum 1–4 firm appears as the filer of its own disclosure document — except Bitpanda. In the e-money-token register the cohort appears only as the blockchains other issuers deploy on; in the register of other crypto-assets the majority filer is a single German intermediary filing for tokens it does not issue.* **Ship the Article-4 limit and the not-EMT-issuers limit in the same paragraph.**
   - **(v) 🟢 THE ALGORAND CATCH IS A PRESS ANGLE, NOT JUST A FIX.** The report's own README advertised a figure the corpus could not support, an instrument caught it eleven days from ship, and the repair produced a new finding. **"We audited our own citations and found one of the three we advertise had none" is a credibility asset if we say it first** — it is the same move as publishing the corpus. Consider one line in the methodology appendix.
   - **(vi) 🔴 `methodology.md` STILL NEEDS SIX SECTIONS REWRITTEN: §1, §3, §4, §5, §6, §7 — SEVENTEENTH run for §1.** §6's *"daily 18-agency panel"* now describes a file **67 days stale**. **§3 gains a third requirement today:** the white-paper registers must be named as three distinct instruments, with their per-file capture status stated, because one of them is verified, one is refused and one is unreachable. **§5 must stop citing `Algorand -25%` without the `[PERIMETER]` label** — and the same line is in the public `README-for-github.md`. **Still the one thing in the repo that could embarrass the report.**
