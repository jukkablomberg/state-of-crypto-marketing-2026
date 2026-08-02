# Corpus-assembly daily run — 2026-08-02 **(day 32 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-02 (Sunday).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, taken verbatim from the 08-01 recommendations:** (1) replicate the lapse checkpoint on Coinbase / Bitpanda / Bitvavo / Gate; (2) resolve the geofence caveat; (3) sweep the remaining warning lists (watch v); (4) execute watch (w) with widened vocabulary; (5) re-run the watch-list audit with the (g) rule applied generally; (6) build the backfill in the upstream scanner lane; (7) escalate four items to Jukka.
**Dedup baseline read before writing:** `2026-08-01-corpus-run.md` in full; `findings/longitudinal-2026-06.md` (head + full 08-01 tail); `layoff-tracker/2026-layoff-tracker.csv` all 16 rows in full; `regulator-filings/` (11 files); `operator-statements/` (4); `marketing-campaigns/` (7); every populated `job-postings/*.csv` row-by-row; `_absence.csv`; `_backfill-queue.csv`. Cadence check: **08-02 run fired; the 07-31 gap remains the only miss.**

---

## Headline result

**Four things, in descending order of consequence.**

**1. The teardown finding replicated 3/3, then outgrew its own frame.** Kraken, OKX and Bitpanda were all still serving expired offers in the present tense with working CTAs on **day 2** after close. And the strongest instance of the failure mode is not a MiCA campaign at all: **BitMart is serving a UTM-tagged "Earn up to $14,000 in rewards — Register now" CTA on the same page that announces it stopped accepting registrations on 26 July.** The finding must be re-framed before Phase 2: *it is not "MiCA campaigns are not torn down", it is "promotional surfaces are not wired to the operational state of the business."* Four firms, four mechanics, one failure mode. → `../marketing-campaigns/promotional-teardown-checkpoint-2026-08-02.md` (NEW FILE).

**2. Bitvavo is a genuine control, and controls are worth more than another confirming case.** Bitvavo's capture campaign runs **25 June → 30 September 2026**, payout 14 October. It has not lapsed because it cannot: its window is still open. That converts a defect observation into a **design** observation — *campaigns keyed to the regulatory date inherit the regulatory date's cliff; campaigns keyed to a commercial horizon do not.* The finding is now falsifiable in a way it was not yesterday.

**3. Class 4 broke a 6-day static streak with the corpus's first-ever Binance operator statement — and it disclosed a CMO departure the corpus did not hold.** **Eowyn Chen, Interim CMO, Binance**, 2026-07-18, verbatim and on the record: *"marketing will be less about driving hype and more about building understanding"* / *"trust is earned through transparency, participation, and community – not through broadcast."* The same piece states that **long-time CMO Rachel Conlan stepped down in June 2026 — the MiCA deadline month** — and that Chen holds the seat on an interim basis. Theme-1 spine goes **n=2 → n=3 Tier-1 exchanges in ten weeks.** → `../operator-statements/binance-chen-marketing-not-hype-2026-07.md` (NEW FILE).

**4. Watch (v) was swept for three more jurisdictions and replicated 4/4. The expected non-replication did not occur.** Germany (BaFin, 22.07 primary), Italy (CONSOB, 01.06 primary) and Cyprus (CySEC, 10.07) all produce **perimeter enforcement against unauthorised entities and zero marketing-conduct action against an authorised CASP** — identical to France. And CySEC supplies the sentence that corroborates the null from the regulator's own mouth: *"NCAs **may, where necessary,** take coordinated action against unauthorised CASPs after the transitional period."* → `../regulator-filings/nca-warning-list-sweep-de-it-cy-2026-07-08.md` (NEW FILE).

**Day-32 named marketing-side enforcement silence HOLDS**, now four-jurisdiction-tested.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-08-02
source A (jobs)   scan_date: 2026-08-02
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**Feed-health guard: HEALTHY.** `scan_metadata` — `scanned_at_utc 2026-08-01T22:45:46Z`, `scan_date 2026-08-02`, 147 companies (87 API / 60 chrome-pending), **2,088 jobs fetched** (identical to 08-01), 27 after filter, **`new_count` 0**, **`url_verification_dropped` 0**, `still_open_count` 27 (flat, 27 → 27; no role closed). ATS breakdown: greenhouse 22, ashby 35, proprietary 59, lever 19, workable 5, breezy 2, teamtailor 2, personio 1, recruitee 1, comeet 1.

**Watch (x) confirmed closed, second observation.** `fetch_errors` is again a top-level key while `_absence.csv` carries the fully-detailed, today-dated Aave Lever 404. The 08-01 diagnosis — *reporting artefact, not data loss* — holds on a second day. No absence claim is affected.

Repo diff from the sync: `_absence.csv` and `_chrome-queue.csv` date re-stamps only. **The 0-new result is genuine idempotency.**

#### Watch-list audit under the (g) rule — EXECUTED (08-01 recommendation #5)

Method: read every populated `corpus/job-postings/*.csv` row-by-row, split by `captured_date` against the instrument epoch **2026-06-26**, then test every watch item that rests on a class-1 count.

**The honest size of class 1, stated plainly for the first time:**

| bucket | rows | firms |
|---|---|---|
| **Flow** — observed *newly open* after the epoch | **5** | Phantom (07-02), Coinbase (07-18), Kraken ×2 (07-24), Gemini (07-30) |
| **Stock** — captured on epoch day, already open | **6** | Ava Labs ×2, Optimism ×1, Solana ×3 |
| **Total populated rows** | **11** | 7 firms |
| Empty files (header only) | 5 | Bitpanda, Bitstamp, Bybit, Crypto.com, KuCoin |

> **Every genuine flow observation class 1 has ever made falls in a 28-day span in July 2026, and there are five of them.** Everything earlier is a snapshot of what happened to be open on one day. This is not a new defect — it is the (t′) finding measured from the other end — but it is the number that should govern how Phase 2 words class-1 claims.

**Per-item verdicts:**

| watch item | rests on class-1? | verdict under the (g) rule |
|---|---|---|
| **(g)** Coinbase brand-rebuild, n=1 | yes | **VOID** (already, 08-01). Coinbase's single row is post-epoch and *valid as flow*; the void is the "n=1" inference, not the row. |
| **(i)** Kraken paid-media build-out | yes | **SURVIVES.** Both rows post-epoch (posted 07-23, captured 07-24), **and verified this run not to be a dedup failure** — distinct Ashby IDs, distinct jurisdictions (US and UK), same title. A genuine two-market Director, Paid Marketing build. |
| **(r)** Gemini structural withdrawal | yes | **SURVIVES.** Row posted 07-29, captured 07-30. Post-epoch flow. |
| **OP Labs 03-12 → 05-21 sequence** (layoff-tracker) | yes | **SURVIVES WITH A NARROWED CLAIM.** `date_posted` 2026-05-21 comes from the ATS payload and is sound; `captured_date` is 2026-06-26, so it is a *stock* observation. **The sequence is safe. Any "only" or "first marketing hire since the cut" qualifier is not** — roles opened and closed between 03-12 and 06-26 are outside the instrument's memory. |
| **(q)** Agency matrix measures the crypto-native segment | no | unaffected |
| Sui "degraded on three instruments" | yes (by absence) | **INSTRUMENT.** Sui has no CSV at all. Any Sui class-1 statement is a statement about a broken ATS slug. |

**NEW defect found by the audit — the corpus's only pre-2026 rows are the least reliable rows it has.** Solana's three rows carry `date_posted` **derived from relative board labels** — the notes read *"board relative date '3 months' → posted_at approximate"* and, for the two 2025-12-26 rows, *"'6+ months' → posted_at approximate, near window edge."* **The only class-1 evidence that reaches back before 2026 is an arithmetic inference from a relative timestamp on a Getro board, and it sits on the exclusion boundary of `methodology.md`'s December-2024 rule.** This compounds the §1 re-scope escalation: not only can class 1 not evidence 12 months, the deepest rows it *does* have are approximations. **New watch (y).**

#### Absence panel — unchanged, and the four upstream gaps are unfixed for a third run
`_absence.csv`: Aave (Lever 404) + Binance, Bybit, HTX, KuCoin, MetaMask/ConsenSys (proprietary, chrome-pending). **OKX (Tier-1), Securitize, Rabby, Relai remain missing from the upstream company list.** No config write attempted — that is the sales funnel's repo, and an autonomous corpus run should not silently edit it. **Carried, escalated for the third consecutive run.**

**Note the irony worth recording:** OKX is absent from the class-1 instrument entirely, and is simultaneously one of the two firms supplying this run's strongest first-party marketing evidence. **Absence in one class is not absence of the firm.**

### 2. Agency claims / overlap matrix (deterministic)

18 agency-claims files rewritten; 8 matrix rows; **1 OVERLAP: Sui (coinbound, rzlt)** — unchanged. **`trend-data.json` `lastUpdated` is still 2026-06-15 — the panel is now 48 days stale.** Watch (d) stable-by-decision; `methodology.md` §6's phrase *"daily 18-agency panel"* is inaccurate as written and must be re-worded before Phase 2. Escalation (iv) stands, unchanged, third run.

### 3. Regulator — **1 NET-NEW FILE. Watch (v) 4/6 DISCHARGED. Watch (w) partially executed.**

→ `../regulator-filings/nca-warning-list-sweep-de-it-cy-2026-07-08.md` (NEW).

**Germany — BaFin, PRIMARY CAPTURED.** *"Bafin warnt vor Plattformreihe: „Verbessern Sie Ihr Krypto-Handelserlebnis""*, **22.07.2026**, § 37(4) KWG, sites `euroxnow(.)com` / `euroxone(.)com`. Perimeter. **Marketing-relevant detail worth the file on its own: BaFin's identification unit is the marketing artefact** — it groups the entities by a shared *slogan* and *near-identical site design*. A regulator reading creative-and-template reuse as a detection signal is a Theme-1 datum the corpus did not hold. Three adjacent July BaFin warnings (24.07 Quantum AI, 27.07 depothandel.com, 28.07 further platform series) noted, not entered as separate primaries.

**Italy — CONSOB, PRIMARY CAPTURED (June).** `comunicazione 2026-06-01`, five sites, delibere 24010–24014 of 28 May 2026, Art. 7-*octies* TUF. Running total **1,723 blocked since July 2019, of which 204 crypto**. Perimeter. **Captured first-party and directly Theme-2/4 relevant:** CONSOB warns on *"contenuti generati con sistemi di intelligenza artificiale - come immagini, voci o video"* used to induce harmful investment decisions, and publishes a standing AI-fraud factsheet. **An NCA issuing guidance on AI-generated marketing creative as a fraud vector is a crossover the corpus did not hold.**

**The July CONSOB action is held as SECONDARY and NOT entered.** Il Sole 24 Ore / Teleborsa-ANSA / Byte.it report 24 sites blocked (10 investment + 14 crypto), total to **1,793 of which 233 crypto**. No CONSOB primary for the July action was reachable; the search returned Jan/Feb/Mar/Apr/May/June `comunicazione` pages and not July. **No URL was guessed.** `[VERIFY]`. What is safe to say, because one endpoint is a captured primary: crypto-site blockings moved **204 (01 June, primary) → 233 (late July, secondary)**, ~+29 in under two months.

**Cyprus — CySEC, 2026-07-10.** Formal reminder relaying ESMA. **The operative sentence, and the most important thing this run captured for the null:**

> *"Within the ESMA cooperation framework, **NCAs may, where necessary, take coordinated action against unauthorised CASPs after the transitional period**."*

Plus: authorities are *"currently engaged directly with the relevant entities"* and will *"monitor whether significant unauthorised cross-border service providers wind down without delay."*

**This is not absence of evidence. It is the regulators describing enforcement in the prospective and conditional mood, ten days into the post-deadline window, scoped explicitly to *unauthorised* entities.** The day-N null is scoped to *named marketing-side actions against identified authorised firms* and is untouched — and is now supported rather than merely unfalsified.

**Cross-reference not to be lost:** CySEC is Kraken's MiFID derivatives regulator (Payward Europe Digital Solutions (CY) Ltd, licence 342/17 — stated first-party on `kraken.com/europe-switch`). **NCAs are not distant from the panel; they are inside its licence stacks.**

**NOT discharged: AFM and CNMV.** **AFM is upgraded to priority** and this is the run's most important open regulator item: the corpus already holds two AFM files on the **cost-information / advertising** axis, both pre-deadline. **AFM is the one NCA in the sweep with a documented history of acting on advertising rather than authorisation — so it is the one place a non-replication is actually likely.** Do not print any post-deadline enforcement claim before AFM is swept.

**Watch (w) — partially executed, honestly reported.** The widened vocabulary (product intervention / event contracts / financial promotion / advertising / inducements) was applied to the NCA sweeps and produced the BaFin creative-reuse and CONSOB AI-creative findings, neither of which a MiCA-keyed query would have surfaced. **But the sweeps were still run through a search engine, not against NCA/ESMA news indexes directly, which is what (w) actually asks for.** ESMA's own index was not swept. **(w) stays open and should be marked partially discharged, not discharged.**

### 4. Operator statements — **1 NET-NEW. First Binance item ever. Class 4: 4 → 5 files.**

→ `../operator-statements/binance-chen-marketing-not-hype-2026-07.md` (NEW).

**Eowyn Chen, Interim CMO, Binance**, CoinGape Block of Fame, published **2026-07-18** (modified 07-20). Role qualifies under §4 (CMO). Binance is Stratum 1. Static since 07-27 — streak broken.

**Three things it delivers:**

1. **Binance's first class-4 entry.** Binance was the corpus's most degraded tracked firm — absent from class 1 (proprietary ATS), absent from class 2, present only via one class-3 file. It now has a named, dated, verbatim senior-marketing primary.
2. **A senior marketing exit the corpus did not hold.** Publisher-stated: *"Following a major leadership reshuffle last month that saw its long-time Chief Marketing Officer **Rachel Conlan step down**…"* — "last month" relative to 18 July = **June 2026, the MiCA deadline month** — with Chen **interim**. `[VERIFY]` a Binance- or Conlan-owned primary before Phase 2 prints it. **Do not join it to the layoff sequence; Binance has no tracker row.** Watch (j) gains a second tracked-cohort instance alongside Bybit/Helen Liu (04-30), but as a *deadline-month* exit, not a contraction-trailing one — preserve the distinction.
3. **Theme-1 spine n=2 → n=3.** Coinbase/Armstrong (05-05, "AI-native pods") → Kraken/Gupta (05-19, "natively AI growth engine") → **Binance/Chen (07-18)**. Three of the largest exchanges in the world, three senior operators, ten weeks. **Coinbase and Kraken name an organisational answer; Chen names an editorial one** — *"the biggest job for marketers isn't defending crypto. It's creating the language that helps people understand this next era of finance."* That difference should be printed, not flattened.

**SOURCING CAVEAT, LOGGED AND LOAD-BEARING.** The piece sits in a vertical that **sells cover-story placement** — the same page carries an "Advertise" nav item, two *"Get your Cover Story Featured / Get Published"* Calendly CTAs, and the site disclosure *"This site may feature sponsored content and affiliate links."* It is filed under `/opinion/` and is **not** labelled sponsored. **There is no evidence this item was paid, and the corpus cannot distinguish an earned interview from a purchased one from outside.** Classification: **near-primary — usable for what Chen said, NOT usable as evidence of independent editorial selection.**

**This is watch (l)'s fourth costing and the first that is a QUALITY defect rather than a coverage defect:** a material share of the observable public-statement surface for crypto marketing leaders is a **paid-placement surface**, and `methodology.md` §4 — a podcast list — has no rule for branded-content verticals. **§4 now needs two changes: widen the inventory, and add an earned-vs-placed provenance field to every class-4 record.**

**And one silence worth recording.** The interim CMO of the firm that exited the EU gave a 3,000-word interview on the future of crypto marketing **17 days after the MiCA deadline** and did not mention **MiCA, the EU, or the exit** once. That is a Theme-4 absence with a named speaker and a date on it — the most citable kind.

**Refused this run:** Marie Tatibouet (CMO, Gate) on the Coinbound podcast — **Gate is not in the Stratum 1–4 cohort**; noted, not entered. Mashal Waqar (CMO, Octant Labs) — not a tracked firm.

### 5. Layoff tracker — **1 NET-NEW ROW (16 → 17). One 08-01 open item RESOLVED, and the answer reverses its category.**

**BitMart — RESOLVED, and it is not a layoff.** The 08-01 run left BitMart's 550 as *"worth one direct check next run purely for scale."* Checked. **BitMart's own primary was captured**: *"Important Notice Regarding the Orderly Cessation of BitMart Operations"*, published **2026-07-26 01:40**, on bitmart.com. It is a **full exchange wind-down**, not a headcount reduction: registrations/deposits/new orders suspended **2026-07-26 01:30 UTC**; all trading discontinued **2026-08-26 01:00 UTC**; operations officially cease **2027-01-31**. Stated rationale verbatim: *"After a careful evaluation of the Company's operating conditions, market environment, and future strategic direction…"* — **NON-AI, the fifth consecutive non-AI 2026 rationale.**

**The 550 figure is NOT entered.** BitMart's primary discloses no headcount; 550 is CryptoJobsList-via-crypto.news, and the Exodus row already documents why that aggregator's per-firm figures are not importable (77 SEC vs 54 aggregator). Recorded as aggregator context inside the row, not as a corpus number.

**The row exists for a marketing reason, and it is the run's sharpest artefact.** Served on the same page as the cessation notice, on 2026-08-02: **"Earn up to $14,000 in rewards — [Register now]"**, linking to `bitmart.com/en-US/register?utm_source=growth-frontend&utm_medium=support-article`. **A growth-attributed acquisition CTA inside the firm's own wind-down announcement, contradicting it within one document.** The UTM parameters show a growth system that is not reading the operational state of the business.

**Theme-4 structural note: three exchange wind-downs inside the first post-deadline month** — BitMEX (07-23), BitMart (07-26), plus wallet SecondFI (post-$2.4M theft) — **none EU-licensed.** The post-deadline month is producing **exchange exits, not marketing enforcement.** Same shape as the four-NCA perimeter-not-conduct result. **Bit.com was named in one secondary as a third exchange closure and is NOT entered — no primary captured.** `[VERIFY]`

**No new August-dated layoff was found.** Searches for August 2026 marketing-team cuts returned only already-tracked July events (Luno, BitMEX) and 2026-Q1 context. **Recorded as absence, not as "nothing happened."**

**Watch (h′) unchanged** — n=9 with a consumer-side non-AI counter-example (Uphold). Still not printable. BitMart is a wind-down, a distinct category, and should not be counted into h′.

### 6. Longitudinal shift for synthesis

Three shifts, written into `../../findings/longitudinal-2026-06.md`:

1. **The teardown finding generalises and acquires a control.** 3/3 replication at day 2, a same-page contradiction at a fourth firm, and one clean control (Bitvavo) that identifies the mechanism: deadline-keyed campaigns inherit the deadline's cliff.
2. **The regulator's post-deadline posture is uniform across four jurisdictions, and the regulators say so themselves.** Perimeter, not conduct — and CySEC states enforcement in the conditional.
3. **The observable operator-statement surface is partly a paid surface.** Class 4's evidentiary quality, not just its coverage, is now a known defect.

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged. **But Binance is no longer unobserved on the marketing axis** (class-4 entry added).
- **(b) First named post-deadline NCA marketing-side action** — **day-32 silence HOLDS, four-jurisdiction-tested, and now positively corroborated** by CySEC's conditional-mood statement. Scope unchanged: named marketing-side actions against identified authorised firms.
- **(c) Capture panel** — **REPLICATED 3/3 at day 2.** New sub-items: (i) EEA-egress re-read is now the single item blocking print; (ii) re-check all four on **08-09** to convert "lapsed" into a measured **time-to-teardown**; (iii) Gate + Coinbase own-channel sweep to close the panel.
- **(d) Agency panel staleness — 48 days.** Stable-by-decision; §6 wording must change.
- **(e′) Cadence unreliable** — **08-02 fired.** One clean day since the 07-31 miss. **Do not re-file as "trend is good"** — that phrasing is what watch (e) was falsified for. Escalation stands.
- **(f) Friday nomination cadence** — next check **08-07**. No `inbound-nominations.md` exists; none have ever arrived.
- **(g) Coinbase n=1** — **VOID as filed; the row itself is valid post-epoch flow.** Re-file only after backfill.
- **(h′) Layoff rationale correlates with firm type** — unchanged, n=9 with counter-example. **Do not print.** BitMart excluded (wind-down ≠ layoff).
- **(i) Kraken paid-media build-out** — **SURVIVES the (g) audit and is strengthened**: two distinct Ashby reqs, US + UK, verified not a dedup artefact. Kraken is now quadruple-loaded (05-14 cut · 07-23 reqs ×2 · lapsed `/europe-switch` · lapsed support article · internal date conflict).
- **(j) Senior-leader exits** — **second tracked-cohort instance: Rachel Conlan, CMO Binance, June 2026 (deadline month), publisher-stated, `[VERIFY]`.** Coinbase CPO still unverified, eighth run.
- **(k) Chrome-lane instrumentation gap** — unchanged.
- **(l) §4 inventory too narrow** — **fourth costing, and upgraded: the defect is now QUALITY, not coverage.** §4 needs an earned-vs-placed provenance field. Not optional for Phase 2.
- **(m) Ad-platform gating** — unchanged.
- **(n) Full-range re-sweep of classes 3 and 5** — classes 1 and 2 historical backfill still not run.
- **(o) Date the document, never an event held about it** — held.
- **(p) Absence claims tested against firms' OWN channels** — **advanced**: Kraken (2 surfaces), OKX (2 surfaces), Bitpanda, Bitvavo, BitMart all read first-party this run. **Still unswept: Coinbase, Gate, Bybit, Crypto.com, Gemini, Sui, all of Strata 2 and 4.**
- **(q) Agency matrix measures the crypto-native segment** — unchanged.
- **(r) Absence panel needs a "structural withdrawal" category** — **SURVIVES the (g) audit** (Gemini row is post-epoch flow). Reinforced by three July exchange wind-downs.
- **(s) Robinhood row misclassified** — unchanged, fourth run.
- **(t′) Class 1 is a FLOW register presented as a STOCK register** — **measured from the other end today: the entire flow register is 5 rows across 4 firms in a 28-day July span.** §1 re-scope remains forced.
- **(u) Brand absorption defeats name-keyed sweeps** — unchanged; alias table still unbuilt.
- **(v) NCA warning lists** — **DISCHARGED for FR, DE, IT, CY (4/4 replicate). OPEN for AFM (PRIORITY) and CNMV.** AFM is the likeliest non-replication because it is the only NCA in the set with a published advertising-conduct track record.
- **(w) Class-3 sweep vocabulary too narrow** — **PARTIALLY EXECUTED.** Widened vocabulary applied and it paid (BaFin creative-reuse, CONSOB AI-creative). **But sweeps still ran through a search engine, not NCA/ESMA indexes directly.** ESMA's own index unswept. **Stays open.**
- **(x) `fetch_errors` null** — **closed, and confirmed on a second day.**
- **(y) NEW — the corpus's only pre-2026 class-1 rows are arithmetic inferences from relative board labels.** Solana's three rows carry `posted_at approximate` derived from *"3 months"* / *"6+ months"* Getro labels; two sit on the December-2024 exclusion boundary. **Compounds the §1 re-scope: class 1 cannot evidence 12 months, and its deepest rows are approximations.** Do not use them to anchor any window claim.
- **(z) NEW — promotional surfaces are decoupled from operational state, and this is bigger than the MiCA campaigns.** BitMart serves a live growth-tagged signup CTA inside its own wind-down notice. Kraken serves two different start dates for the same €1M draw on two of its own pages. **The class of defect is "marketing systems that do not read the business", and it is testable at every panel firm.** Cheapest test: for each tracked firm, does any owned surface currently advertise a state the firm has publicly exited?

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2; 0 new postings, 18 agency files, 8 matrix rows.
2. Direct read of `prospects/open-positions.json` `scan_metadata`; `_absence.csv`; every populated `job-postings/*.csv` row-by-row → **(g)-rule watch audit; flow=5 / stock=6; watch (y) opened; Kraken dedup ruled out.**
3. WebSearch — Kraken europe-switch €1M draw → surfaced the campaign + support primaries.
4. **Fetch `https://www.kraken.com/europe-switch`** → HTTP 200, **live day 2**, full copy captured.
5. **Fetch `https://support.kraken.com/articles/1m-eur-prize-draw`** → HTTP 200, **second lapsed Kraken surface**, and **the 19-June vs 22-June conflict resolved from both sides**.
6. WebSearch — Bitvavo MiCA switch campaign → surfaced the Bitvavo primaries.
7. **Fetch `https://bitvavo.com/en/news/crypto-deposit-promo`** → HTTP 200, **the control case** (25 Jun – 30 Sep, payout 14 Oct).
8. WebSearch — Bitpanda MiCA Stichtag Aktion → surfaced the Bitpanda campaign page; **secondary claims (12 July close, 10,000 cap) later falsified by the primary.**
9. **Fetch `https://www.bitpanda.com/en/campaigns/bya-june-26`** → HTTP 200, **third lapsed campaign** (31 July 23:59, 15,000 cap, two-entity AT/EU/CH vs DE disclosure).
10. WebSearch — OKX Europe 8% MiCA campaign → surfaced the OKX primary.
11. **Fetch `https://www.okx.com/en-us/learn/okx-europe-deposit-bonus-mica-deadline`** → HTTP 200, **live day 2**; second OKX surface (`/learn/mica-deposit-bonus-campaign`, Jul 22) identified from its own rail; full MFSA licence stack captured.
12. WebSearch — BaFin Verbraucherwarnung Krypto Juli 2026 → surfaced the BaFin primary.
13. **Fetch BaFin `meldung_2026_07_22_plattformreihe_krypto-handelserlebnis`** → HTTP 200, **watch (v) leg 2**, § 37(4) KWG, creative-reuse detection finding.
14. WebSearch — CONSOB oscuramento luglio 2026 → surfaced CONSOB comunicazione pages + Italian secondaries.
15. **Fetch `consob.it/…/comunicazione-consob-del-2026-06-01-abusivismo`** → HTTP 200, **primary**; 1,723 / 204 crypto; AI-generated-creative fraud guidance captured.
16. WebSearch — CySEC warning list July 2026 → surfaced Cyprus Mail 07-10.
17. **Fetch `cyprus-mail.com/2026/07/10/…unauthorised-crypto-asset-services`** → HTTP 200, **the conditional-mood NCA quote.**
18. WebSearch — AFM waarschuwing crypto juli 2026 → **no dated July action reached. (v) stays open for AFM.**
19. WebSearch — crypto CMO / head of marketing statements July 2026 → surfaced the Binance/Chen piece.
20. **Fetch `coingape.com/block-of-fame/opinion/…eowyn-chen`** → HTTP 200, **class-4 net-new**, Conlan departure disclosed, paid-placement caveat established from the page's own furniture.
21. WebSearch — crypto layoffs August 2026 marketing → **nil net-new for August**; only already-tracked July events.
22. WebSearch — BitMart 550 July 2026 → surfaced the BitMart primary + PYMNTS.
23. **Fetch `bitmart.com/…/53544595916059`** → HTTP 200, **firm primary**, full wind-down timeline, **and the live "Register now" CTA on the cessation notice.**
24. **Fetch `pymnts.com/…bitmart-becomes-2nd-crypto-exchange-to-close-in-3-days`** → HTTP 200; three-closures-in-a-week framing; SecondFI; CoinDesk withdrawal-friction note.
25. **Not reached / not guessed:** CONSOB July `comunicazione`; AFM July warning list; CNMV `Advertencias`; ESMA news index; Gate and Coinbase own channels; Bit.com closure primary. **All recorded as open, none fabricated.**

---

## Net-new / changed this run

- `corpus/marketing-campaigns/promotional-teardown-checkpoint-2026-08-02.md` — **NEW.** 3/3 replication at day 2; second surfaces at Kraken and OKX; Kraken's two-start-date conflict resolved; Bitvavo control; BitMart same-page contradiction; Coinbase absence recorded.
- `corpus/operator-statements/binance-chen-marketing-not-hype-2026-07.md` — **NEW.** Class-4 net-new; first Binance item; Conlan departure `[VERIFY]`; Theme-1 spine n=3; paid-placement provenance caveat.
- `corpus/regulator-filings/nca-warning-list-sweep-de-it-cy-2026-07-08.md` — **NEW.** Watch (v) 4/4 replication; BaFin + CONSOB primaries; CySEC conditional-mood quote; AFM/CNMV open.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **+1 row (16 → 17): BitMart wind-down.** 550 explicitly not entered.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv` — date re-stamps (sync).
- `corpus/agency-claims/*.csv` (18), `corpus/agency-overlap-matrix.csv` — dated snapshots (sync).
- `findings/longitudinal-2026-06.md` — three shifts appended.

---

## Recommendation for next run

1. **EEA-egress re-read of all four lapsed surfaces via the chrome lane.** This is now the *only* thing between the teardown finding and print. Everything else about it is done.
2. **Sweep AFM.** Highest-value regulator item in the corpus: the one NCA with a published advertising-conduct track record, and therefore the one place watch (v) might break. Then CNMV.
3. **Execute watch (w) properly** — against ESMA's and each NCA's own news index, not through a search engine. Today's partial pass already found two things a MiCA-keyed query would not have; a direct index sweep should find more.
4. **Re-check the four lapsed surfaces on 08-09** to date the teardown. Converts a binary into a **time-to-teardown** metric no competing report will have.
5. **Test watch (z) across the panel:** for each tracked firm, does any owned surface currently advertise a state the firm has publicly exited? One run, high yield, and it is the generalised version of the run's best finding.
6. **Capture the CONSOB July primary** and close the 24 / 1,793 / 233 `[VERIFY]`.
7. **`[VERIFY]` the Conlan departure** against a Binance- or Conlan-owned primary before Phase 2 prints it.
8. **Escalate to Jukka — five items, in order:**
   - **(i) `methodology.md` §1 must be re-scoped, and today makes it worse, not better.** Measured from the other end, class 1's entire *flow* register is **5 rows across 4 firms inside a 28-day July window**; its only pre-2026 rows are **arithmetic inferences from relative board labels** sitting on the December-2024 exclusion boundary (watch y). The published "rolling 12 months" cannot be met. **Still the one thing in this repo that could embarrass the report.**
   - **(ii) `methodology.md` §4 needs two changes, not one** — widen the inventory *and* add an earned-vs-placed provenance field. The corpus's newest and most valuable class-4 item sits in a vertical that sells placement, and §4 currently has no way to say so.
   - **(iii) The four upstream company-list gaps — OKX (Tier-1), Securitize, Rabby, Relai — are unfixed, third run.** OKX supplied two of this run's strongest primaries while being invisible to the class-1 instrument. Needs an owner outside the corpus run.
   - **(iv) §6's "daily 18-agency panel" is inaccurate at 48 days stale.** Re-word or re-feed. Third run.
   - **(v) Cadence: 08-02 fired, one clean day since the 07-31 miss.** No trend claim is being made this time — that is what falsified watch (e).
