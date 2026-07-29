# Corpus-assembly daily run — 2026-07-29 **(day 28 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-07-29 ~16:10 CEST.
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (per `../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency comparison panel (`../../tracked-firms.md`).
**Mandate for this run, taken directly from the 07-28 recommendations:** execute **watch (p)** — sweep tracked firms' **own blogs / newsrooms / press pages**, starting with the firms recorded at zero (Bitstamp, Sui, Phantom, Ledger, Bybit, OKX) — before Phase 2 writes any absence sentence.
**Dedup baseline read before searching:** `2026-07-28-corpus-run.md` in full; `findings/longitudinal-2026-06.md` tail; `layoff-tracker/2026-layoff-tracker.csv` (13 rows pre-run); `regulator-filings/` (8 files); `operator-statements/` (3 files); `marketing-campaigns/` (3 files); `job-postings/` listing + `_absence.csv` + `_chrome-queue.csv`. Repo-wide greps for `ledger`, `wengroff`, `spurs`, `moonpay`, `x games`, `holographik`, `thelen`, `jordan francis`, `defi casino`, `robinhood crypto`, `bitstamp by robinhood`, `bakken`, `f37` run before any file was written.

---

## Headline result

**Watch (p) was the right call and it broke the class-1 instrument open as a side effect.**

The mandate was to test whether absence claims survive a sweep of firms' own channels. They did not. But the more serious finding is what the sweep revealed about the deterministic feed underneath it.

**1. Ledger — a tracked Stratum-3 firm recorded at ZERO across every source class — is one of the most marketing-visible firms in the cohort.** On its own blog, in window: an **NBA jersey-patch partnership** (San Antonio Spurs, 2025-06-25, three-year, global, still live in the site footer), an **X Games League sponsorship with a 30-second national TV spot on ESPN and ABC plus Nippon TV in Japan** (2026-07-24), athlete gifting, venue build, a named editorial franchise ("Revenge of the Atoms"), a published brand-vision document, MiCA consumer content, and a self-declared in-house content unit ("Ledger Studio").

**2. And it has a named EVP of Marketing — the corpus did not know the seat existed.** → **NET-NEW CLASS-4 CAPTURE.**

**3. Sui / Holographik — watch (q) is confirmed at the agency matrix's own flagship row.** `agency-overlap-matrix.csv` flags exactly one OVERLAP in the entire cohort: `Sui (coinbound, rzlt)`. Sui's actual brand system — logo, palette, custom typeface, icon library, motion, gradient governance, "across products, events, websites and motion" — was built by **Holographik**, a non-crypto-native studio the panel cannot see.

**4. Bitstamp — a third category of absence.** Its owned channel is fully rebranded **"Bitstamp by Robinhood"** and its X handle is **`@RobinhoodCrypto`**, verified from the firm's own metadata today. It has not exited (that is Gemini, watch (r)) and it is not quiet. **It no longer markets under the name every sweep in this corpus searches on.**

**5. The class-1 instrument does not cover 12 of 27 tracked firms — and does not record them as absent either.** Including **two Tier-1 exchanges (Gemini, OKX)** and **Ledger, whose careers board is a standard Ashby API endpoint**. → new watch **(t)**, and it supersedes (p) as the top method item.

**The headline null survives intact. Day-28 named marketing-side enforcement silence HOLDS** — none of today's five additions is an enforcement case.

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

**Net-new: 0.** Printed summary:

```
=== daily-corpus-sync summary ===
date: 2026-07-29
source A (jobs)   scan_date: 2026-07-29
source B (agency) lastUpdated: 2026-06-15
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys', 'Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave', 'Binance', 'Bybit', 'HTX', 'Kucoin', 'MetaMask / ConsenSys']
agency-claims files written: 18
agency-overlap-matrix rows: 8
agency OVERLAPS on tracked firms: ['Sui (coinbound, rzlt)']
```

**Feed-health guard: HEALTHY.** `scan_metadata` — `scanned_at_utc 2026-07-28T22:45:05Z`, `scan_date 2026-07-29`, 147 companies scanned (87 API, 60 pending Chrome), **2,109 jobs fetched**, 28 after filter, **`new_count` 0**, **`url_verification_dropped` 0**, `still_open_count` 28. Six fetch-errors, **only Aave tracked** (Lever 404, unchanged for weeks); the other five (Wormhole, Injective, Bitwise, Chainlink Labs, Elliptic) are non-cohort. Drops: 1,596 excluded function · 360 no marketing keyword · 86 no seniority signal · 23 excluded seniority · 12 tracker · 4 excluded location. Working-tree change was **date re-stamps only** in `_absence.csv` and `_chrome-queue.csv` (7 rows each, 2026-07-28 → 2026-07-29, no row added or removed).

Kraken's two 07-23 Director, Paid Marketing reqs remain the most recent class-1 event.

#### **But the instrument is broken in a way the summary line cannot show. This is the run's most important technical finding.**

The printed line *"tracked firms STILL w/o coverage (absence=data)"* lists **six** firms. That number is not the cohort's uncovered count. It is **the count of firms the upstream lead-generator both scans and fails on.**

Reconciled against the script's own `TRACKED` alias table (27 canonical slugs, Stratum 1–4):

| bucket | count | firms |
|---|---|---|
| has a `job-postings/*.csv` | 11 | ava-labs, bitpanda, bitstamp, bybit, coinbase, crypto-com, kraken, kucoin, optimism, phantom, solana |
| recorded in `_absence.csv` | 6 | aave, binance, bybit, htx, kucoin, metamask-consensys |
| **SILENT — neither** | **12** | **aptos, arbitrum, gemini, ledger, okx, polygon, rabby, relai, securitize, sui, tether, trust-wallet** |

**Only 15 of 27 tracked slugs are accounted for in either direction. Twelve are invisible to both the coverage output and the absence output.**

`_absence.csv` is generated from the upstream feed's `needs_chrome_fallback` + `fetch_errors` arrays. A firm the upstream feed **never scans at all** appears in neither array, so it cannot appear in `_absence.csv`. **The file the methodology designates as "absence = data" is not a record of the cohort's absence. It is a record of the prospecting list's fetch failures.**

Worked examples, in ascending order of how bad they are:

- **Polygon** — a tracked Stratum-2 firm with a **layoff row in this corpus** (2026-07-16). Class 5 sees it; class 1 has never looked.
- **Relai** — added to the cohort on 2026-05-06 *specifically* for its **"strong public posting velocity in DACH + IT."** That posting velocity has never been captured.
- **Sui** — `tracked-firms.md` records *"79 open roles per web3.career; three open IC marketing seats."* Manually observed, never reproduced by the feed. Also the **only OVERLAP row in the agency matrix**.
- **Gemini and OKX** — **Tier-1 exchanges.** OKX is marked *"yes (EU entity); Strong MiCA-relevance."* Neither is even classified as proprietary-ATS in `_chrome-queue.csv`.
- **Ledger** — worst case. Its careers board is **`https://jobs.ashbyhq.com/ledger`**, read this run from **Ledger's own site footer**. Ashby is the *most* API-reachable ATS in the scan — **35 Ashby boards are already covered**. This is not a rendering problem, a sign-in wall or a slug error. The firm is simply **not in the upstream company list.**

**Written to `../job-postings/_absence-cohort-audit.csv`** — a script-independent, cohort-keyed audit of all 27 slugs. It is deliberately a **separate file**: `_absence.csv` is regenerated from the feed on every run and would silently discard manual rows. **The real fix is upstream** — add the 12 firms to the lead-generator's company list — and is escalated to Jukka below.

**Caveat recorded:** the Ledger Ashby API endpoint could **not** be tested this run (the fetch tool refused the URL under its provenance rule). The board's existence is primary-sourced from Ledger's footer; its API reachability is **inferred from ATS type and `[VERIFY]`-flagged**.

### 2. Agency claims / overlap matrix (deterministic)

**Net-new: 0.** Source B `trend-data.json` `lastUpdated` **2026-06-15 — 44th day unchanged.** Matrix idempotent at 8 tracked firms / 1 OVERLAP. 18 per-agency snapshots rewritten identically. **NOT re-escalated** — stable-by-decision per the 07-10 Path-2 ruling.

**The matrix took its second substantive hit in two days, and this one lands inside its loudest row.** See class 4 / Sui below. Zero rows changed; what they mean changed again.

### 3. Regulator — **0 net-new. Day-28 silence HOLDS.**

Swept for net-new marketing-side actions across ESMA / BaFin / AMF / CONSOB / AFM / CySEC / FCA / MAS / VARA. **No named marketing-side enforcement case surfaced.** Everything returned was already in the corpus or already excluded:

- **ESMA / AMF transitional-period statements (June 2026)** — already held in `../regulator-filings/esma-mica-transitional-period-end-2026-06.md` and `amf-mica-transitional-period-end-2026-06.md`. One clause worth re-noting because it is the marketing hook in an otherwise perimeter instrument: unauthorised CASPs must **"cease marketing activities and solicitation"** on wind-down. That is a *prohibition on marketing*, not a *rule about marketing content* — a distinction Chapter 1 already draws and should keep drawing.
- **Article 111 penalty exposure** (up to €15M or 5% of annual turnover for post-2026-07-02 unauthorised provision) — perimeter, not marketing-side. Not entered.
- **CNMV (Spain)** — carried from 07-28 for a direct site read. **Not executed this run** — the class-4 sweep consumed the run's budget once Ledger opened up. **Carried again**, and it is now two runs old.
- **AFM finfluencer study** — recommendation #3 from the last run. **Not executed** (the one domain-restricted `afm.nl` search issued this run returned a transient tool error and was not retried). **Carried.** Still the highest-value outstanding class-3 target: a second NCA on BaFin's exact channel.

**Recorded honestly: two class-3 targets were carried, not worked.** The run traded them for the class-4 material below. That was the right trade on value, and it is the second consecutive run in which the class-3 backlog did not move.

### 4. Operator statements — **1 NET-NEW CONFIRMED + 1 QUALIFIED; three absence claims destroyed**

#### (a) NET-NEW — **Ariel Wengroff, EVP Marketing & Communications, Ledger (TRACKED, Stratum 3), 2025-06-25**

→ `../operator-statements/ledger-wengroff-spurs-partnership-2025-06.md`

> "The Spurs' fanbase is not just an audience—it's a generation shaping what comes next. And they're looking for tools that give them real agency in the digital world."

**Role: unambiguously eligible** (EVP Marketing and Communications). **Date: three-point verified** — `meta-article:published_time 2025-06-25T15:49:07+00:00`, on-page `Company | 06/25/2025`, four `uploads/2025/06/` asset paths. **Source: the firm's own channel.**

**This is the first named senior marketing operator ever identified at Ledger by this corpus.** `tracked-firms.md` lists exactly one Ledger individual — *"Pascal Gauthier CEO"* — and that is NorthPoint sales context, not corpus signal. The corpus did not know the seat existed.

**Role exclusion held twice on the same page.** CEO **Pascal Gauthier** is quoted twice and is **not** entered as class 4 — consistent with Demuth, Armstrong, Ghoos, Liniger and Gauthier himself in earlier runs. His words are recorded as **corporate disclosure**, a separate object, and labelled as such. Two of them are load-bearing anyway:

> "**The U.S. is Ledger's top market globally**, and aligning ourselves with an historic U.S. sports team … will help us onboard the next generation of sovereign individuals."

**Modification flag preserved:** the Spurs post carries `meta-article:modified_time 2025-07-14T09:26:34+00:00`. Edited three weeks after publication; wording not diffed against the original. `[VERIFY]` against an archive snapshot if a quote becomes load-bearing.

**Refused, and recorded because it was tempting:** Ledger's two audience figures — *"nearly 1 in 3 NBA fans in the U.S. say they're interested in learning more about digital assets"* and *"over 1.6 million enrolled"* Texas students — are **unsourced by Ledger**. They would have been useful Theme-4 sizing data. **Entered as firm marketing claims, not as statistics. Do not print either as fact.**

#### (b) QUALIFIED — **Jordan Francis, Head of Design & Creative (Sui Foundation `[VERIFY]`), 2026-06-15**

→ `../marketing-campaigns/sui-holographik-brand-system-2026-06.md`

> "As the ecosystem scaled, Holographik became a genuine long-term creative partner. Less a delivery, more a living system built together."
> "You see the visual language being adopted and remixed across the ecosystem without being mandated. That's the real signal."

**Two open flags, both printed rather than resolved by assumption:**

1. **Employer unstated in the source.** The client-side reading rests on internal evidence (speaks of Holographik as a *"partner"* that *"became"* one as the ecosystem scaled; the agency's own contributor is separately labelled *"Art Director Philipp Thelen"*). Strong, circumstantial, **unconfirmed**.
2. **Role boundary.** `methodology.md` §4 names CMO / VP Marketing / Head of Brand / Head of Growth. *Head of Design & Creative* is **not on that list by title but is on it by function**. Every prior exclusion (Demuth, Armstrong, Gauthier, Ghoos, Liniger) removed someone *above* the marketing function; this is the first question about a title *inside* it. **Ruling: eligible in function, flagged in title.**

**Sui's confirmed, unambiguous class-4 count therefore stays at 0.** This entry does not silently move it, and Phase 2 should report Sui both ways.

#### (c) The Sui / Holographik finding — **watch (q) confirmed at the matrix's own flagship row**

`agency-overlap-matrix.csv` flags **exactly one OVERLAP in the whole cohort: `Sui (coinbound, rzlt)`**. It is the anchor of the report's three-agencies-on-one-firm framing.

**Sui's actual brand system was built by Holographik** — a non-crypto-native digital studio, invisible to the 18-agency panel by construction. Scope, from the source: symbol distillation, colour system (Blue/500 hero on Blue/900), a **custom single typeface** (TWK Everett by Weltkern), a derived icon library, two governed gradient constructions, and deployment *"across products, events, websites and motion."*

Watch (q) was opened yesterday on one instance at a firm with an **empty** matrix row (Bitpanda / Serviceplan). It is now demonstrated **inside the matrix's most-cited row**. The finding upgrades:

> **The matrix does not measure agency relationships. It measures presence in the crypto-native segment. At the one firm where it reports the richest structure, the deepest engagement is the one it cannot see.**

**Theme 4 gains a third point and becomes an axis with a mechanism.** Agency-side, Holographik's **Philipp Thelen** (recorded as agency claim, not class 4):

> "A lot of crypto brands lean into hyper-volatility, which naturally reinforces ideas of speculation. For Sui, we wanted to position the brand as a trustworthy long-term infrastructure layer … **The visual language needed to say 'reliable stack' and 'data integrity' rather than 'hype.'**"

Set against Coinbase CMO **Catherine Ferdon**, ten weeks earlier (2026-04-09): *"constant regulatory scrutiny … the first instinct is really to generate like a very sterile brand"*; *"strong gravitational pull towards being beige."*

**Two operators, ten weeks apart, converging on an identical aesthetic through opposite reasoning** — for Ferdon a pull to be resisted, for Thelen a brief executed on purpose. Chapter 5 prints both and lets the tension stand, with the asymmetry named: Coinbase sells a regulated consumer service, a Layer-1 foundation does not, and the audience Thelen is de-risking for is institutional.

#### (d) Ledger's campaign portfolio → `../marketing-campaigns/ledger-sports-sponsorship-portfolio-2025-2026.md`

Spurs jersey patch (2025-06-25, three-year, global, live in the footer today via a `uploads/2026/06/` asset) + MoonPay X Games League (2026-07-24: venue signage, Team LA jersey, **30-second spot on ESPN and ABC**, Nippon TV Japan, VIP booth, athlete gifting to Filipe Mota / Dashawn Jordan / Tom Schaar / Mia Kretzer; earlier stops Sacramento 06-26/28 and Chiba 07-04/05).

**Theme 4, stated as sequence with no causal claim:** across the twelve months into the MiCA deadline, the publicly visible sponsorship and broadcast spend of this **Paris-domiciled** tracked firm lands in **non-EU jurisdictions**, and its CEO says on the same channel that the US is its top market. **The report must not imply regulatory avoidance** — Ledger sells hardware, not a regulated crypto-asset service, and the corpus has no evidence connecting the two facts.

**A June-2026 date collision is recorded and explicitly de-fanged:** the FCA's Premier League sponsorship warning (`../regulator-filings/fca-premier-league-sponsorship-warning-2026-06.md`) and the sponsorship-reset material (`../operator-statements/sport-sponsorship-reset-2026-05.md`) sit in the same months as Ledger's Sacramento jersey placement and its June-2026 Spurs footer re-upload. **This is a timeline coincidence between a UK regulator and a French firm's US/Japan activations. It is not a compliance event and must never be printed as one.**

**Theme 3, second instance in two days:** no agency is named anywhere in either Ledger announcement, and Ledger holds **zero** matrix rows. Under watch (q) that reading is now known-ambiguous — no agency, in-house ("Ledger Studio", self-declared), or a mainstream agency the panel cannot see. **Do not read Ledger's empty row as "agency-light."**

#### (e) Verified and NOT entered, with reasons

- **Phantom — "Introducing Phantom's new brand identity"** (`phantom.com/learn/blog/introducing-phantom-s-new-brand-identity`). Fetched and read in full. **Dated 2023-06-21 — OUT OF WINDOW** per `methodology.md` (pre-December-2024). **Not entered.** Recorded because it is a genuine first-ever rebrand with a named agency (**Bakken & Baeck**) and a custom typeface (**F37 Foundry**) — i.e. a **third** non-crypto-native agency relationship at a **third** tracked firm, invisible to the matrix. Out of window for the corpus; **in scope as further evidence for watch (q)**, which is a claim about the instrument, not about 2026.
- **Bitstamp product/company posts** (O/EMS integrations 2026-07-03; Multi-Asset Perpetual Futures 2026-07-02; perpetual-futures launch 2026-04-09; Kaiko AA ranking 2026-03-06; BVI VASP 2026-02-06). Product and corporate news, **no marketing-function content, no named marketing operator, no campaign**. Not entered. **But this is now a substantiated absence for Bitstamp rather than an untested one** — the channel was read, in full, page 1.
- **Ledger CEO piece "Who Controls Your Digital Future: Ledger CEO on Digital Sovereignty"** (2026-07-03) — **role exclusion**, not entered.
- **"Ledger Becomes Official Naming Partner of Young Star Game"** — surfaced in search, **page not fetched, date not verified. Deliberately left undated and unentered.** Carried.
- **`bitstamp.net/bitstamp-way`** ("The Bitstamp + Robinhood Way") — fetched, **returned an empty body** (client-rendered). A likely brand-positioning artefact, **unread**. Carried.

#### (f) Bitstamp — a third category of absence → `../marketing-campaigns/bitstamp-robinhood-brand-absorption-2025-2026.md`

Directly verified on `blog.bitstamp.net` today: page title **"The Bitstamp Blog by Robinhood"**, `og:site_name` the same, **`meta-twitter:site` and `meta-twitter:creator` both `@RobinhoodCrypto`**, every post bylined **"Bitstamp by Robinhood"**, footer nav **"The Bitstamp + Robinhood Way"**, copyright **"© 2026 Bitstamp by Robinhood"**, listed X link `x.com/RobinhoodCrypto`. From the same page's legal footer: the MiCA licence sits with **Bitstamp Europe S.A., CSSF Luxembourg, CASP licence N00000003**.

**So the CASP licence markets under a US parent's brand.**

**The absence panel now needs three categories, not two:**

1. **Present and quiet** — reticence. What the report actually wants to measure.
2. **Structurally withdrawn** — Gemini, 2026-02-05. No EU surface exists to be quiet on. (watch **r**)
3. **Brand-absorbed** — Bitstamp. Surface exists, is active, and **is not searchable under the tracked firm's name.**

**Category 3 silently corrupts the instrument**, because every sweep in this corpus is keyed on *"Bitstamp"*. This is watch (p)'s defect by a different mechanism: not the wrong surface — **the wrong name on the right surface.** → new watch **(u)**.

**Dating discipline:** acquisition completion **2025-06-02/03** is solid (Robinhood's own newsroom + CNBC + CoinDesk + The Block). The **X-handle rename date (reported 2026-07-14)** and the **display name "Robinhood Crypto EU"** are **aggregator/search-title sourced and `[VERIFY]`-flagged**. Neither is load-bearing; the finding rests on directly-verified owned-channel metadata.

### 5. Layoff tracker — **0 net-new. Holds at 13 rows.**

Full-range sweep for 2026 marketing-team contractions returned **only rows already held**: Exodus (07-17, SEC Exhibit 99.1), Coinbase (05-05), Crypto.com (03-19), Block, Polygon Labs (07-16). No new firm, no new function-level disclosure, **nothing naming marketing as the affected function**. Standing finding intact: **across all 13 rows, not one names marketing.**

Watch **(h′)** unchanged at n=6 (consumer exchanges AI-framed 4/4; infrastructure/protocol non-AI 2/2). **Still not safe to print** — small n, and Kraken's leg is anonymously sourced.

**One reclassification raised and deliberately NOT executed.** The tracker's **Robinhood** row (2026-06-16, ~290, -10%) is filed *"Crypto-adjacent perimeter (broker)."* **Robinhood has owned Stratum-1 tracked firm Bitstamp since June 2025.** "Perimeter" is now the wrong label. **Row not rewritten this run** — there is no evidence either way that the cuts touched Bitstamp Europe or any marketing function, and the classification deserves a deliberate ruling rather than a drive-by edit. → new watch **(s)**.

Two `[VERIFY]`s carried unchanged: Gemini's ~30% YTD aggregate (only 25% is citable) and Block's tracker date (row says Q2; Cointelegraph says February). Coinbase CPO departure **still unentered for a fifth consecutive run** — watch (j) unchanged.

### 6. Longitudinal shift for synthesis

Recorded in `../../findings/longitudinal-2026-06.md` (2026-07-29 section):

1. **Class 1's absence file is not an absence file.** 12 of 27 tracked slugs are silent in both directions, including two Tier-1 exchanges and one firm with a public Ashby board. → watch **(t)**, now the top method item.
2. **Watch (p) vindicated at a second firm and on a larger scale than Bitpanda** — Ledger, recorded at zero, holds an NBA jersey patch, a national TV buy, an in-house studio and an EVP of Marketing.
3. **Class 4 +1 confirmed (Wengroff, Ledger) and +1 qualified (Francis, Sui).** First named marketing operator at Ledger; first title-boundary ruling in the corpus.
4. **Watch (q) confirmed at the agency matrix's flagship OVERLAP row** (Sui / Holographik), with Phantom / Bakken & Baeck as a third, out-of-window instance.
5. **Theme 4's aesthetic question becomes an axis with a mechanism** — Ferdon (beige-by-scrutiny, 04-09) vs. Thelen (trust-by-design, 06-15).
6. **The absence panel needs a third category — brand absorption** (Bitstamp). → watch **(u)**.
7. **Layoff tracker static at 13; the Robinhood/Bitstamp ownership link makes one existing classification wrong.** → watch **(s)**.

Methodology guards applied and satisfied: multi-point date verification before every entry (Ledger Spurs: `published_time` + on-page + four asset paths; Ledger X Games: `published_time` + on-page; Sui: on-page date; Bitstamp: direct metadata read); verbatim reproduction without silent correction (including the unspaced em-dash in the Wengroff quote); **role exclusion enforced twice on a page the corpus wanted quotes from** (Gauthier ×2); **a title-boundary call made explicitly and flagged rather than resolved by convenience** (Francis); **two firm-stated statistics refused** (Ledger's NBA-fan and student figures); **an out-of-window item excluded despite being directly on-point** (Phantom 2023 rebrand); **a tempting reclassification declined for lack of evidence** (Robinhood row); **two carried class-3 targets recorded as not worked rather than quietly dropped** (CNMV, AFM finfluencer).

---

## Watch items

- **(a) Binance re-file jurisdiction** — unchanged; still France-reported-only.
- **(b) First named post-deadline NCA marketing-side action** — **day-28 silence HOLDS.** CNMV direct read and the **AFM finfluencer study** both carried a second run without being worked. Flagged as a real backlog, not a null.
- **(c) Capture panel** — **07-31 is two days out**: Kraken MiCA-lapse checkpoint + OKX 8% campaign end + Friday nomination check. **Kraken is triple-loaded and OKX is now known to be class-1 invisible** (watch t) — prepare both captures before the date.
- **(d) Agency panel staleness — 44 days.** Stable-by-decision; not re-escalated.
- **(e) Loop cadence** — 07-29 fired normally and on schedule; **second clean single-fire day running.** Ninth consecutive run carrying this item; the trend is now genuinely improving. Still needs Jukka's eyes once.
- **(f) Friday nomination cadence** — next check **07-31**. No `inbound-nominations.md` exists.
- **(g) Coinbase brand-rebuild signal** — unchanged at n=1 on postings.
- **(h′) Layoff rationale correlates with firm type** — unchanged at n=6. Do not print.
- **(i) Kraken paid-media build-out** — unchanged; three dated legs, sequence only.
- **(j) Senior-leader exits trailing contractions** — Coinbase CPO still unverified, **fifth run**.
- **(k) Chrome-lane instrumentation gap** — unchanged; the 07-25 Binance Dubai req remains unrecoverable.
- **(l) `methodology.md` §4 inventory too narrow** — **now costed twice.** §4 lists podcasts and conferences. Bitpanda's campaign sat on its own blog for ten months; **Ledger's entire marketing existence sits on its own blog and has for thirteen.** The §4 rewrite (marketing trade press + regional-language media + **firm-owned channels**) is no longer optional for Phase 2.
- **(m) Ad-platform gating** — unchanged (Google France, 2026-07-01).
- **(n) Full-range re-sweep of classes 3 and 5** — executed 07-28 for those classes. **Classes 1 and 2 historical backfill still not run**, and watch (t) now shows why it matters.
- **(o) Date the document, never an event held about it** — held. Applied cleanly to the Ledger `modified_time` flag.
- **(p) Absence claims must be tested against firms' OWN channels** — **✅ EXECUTED, and it returned the largest single-firm finding of the cycle.** Ledger. **Not closed:** only Bitstamp, Phantom, Sui and Ledger were swept. **Bybit, OKX, Bitpanda (beyond the campaign), Kraken, Coinbase, Crypto.com, Gemini, and all of Strata 2 and 4 remain unswept.**
- **(q) The agency matrix measures the crypto-native segment, not "agency relationships"** — **CONFIRMED at the matrix's own flagship OVERLAP row** (Sui / Holographik), with Ledger (empty row, in-house studio) and Phantom (Bakken & Baeck, out of window) as second and third instances. **No Theme-3 absence sentence is safe until Phase 2 adopts the distinction.**
- **(r) The absence panel needs a "structural withdrawal" category** — unchanged (Gemini).
- **(s) NEW — the layoff tracker's Robinhood row is misclassified.** Robinhood has owned Stratum-1 Bitstamp since June 2025. "Crypto-adjacent perimeter" is wrong. **Not corrected this run by choice** — no marketing-function evidence exists either way. Needs a deliberate ruling.
- **(t) NEW — `_absence.csv` is not a cohort absence record, and 12 of 27 tracked firms are invisible in both directions.** Including Gemini and OKX (Tier-1) and Ledger (public Ashby board). **This supersedes (p) as the highest-priority method item**, because (p) is a sweep discipline the corpus can execute, while (t) is a defect in the deterministic feed that no amount of sweeping fixes. **No Theme-1 claim about hiring patterns, and no absence-panel row derived from class 1, is safe until this is closed.**
- **(u) NEW — brand absorption defeats name-keyed sweeps.** Bitstamp markets as "Bitstamp by Robinhood" from `@RobinhoodCrypto`. Every sweep in this corpus searches on the tracked firm's name. **Before Phase 2, each tracked firm's current public brand name and primary social handles must be resolved and recorded** — the cohort needs a name-alias table for sweeping, exactly as the sync script has one for matching.

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2 deterministic; 0 net-new both; date re-stamps only. Summary captured above.
2. Feed-health guard: direct read of `prospects/open-positions.json` `scan_metadata` / `drops_summary` / `new_since_last_scan` / `fetch_errors`.
3. **Cohort-coverage reconciliation** — parsed the `TRACKED` table out of `scripts/daily-corpus-sync.py` and diffed its 27 slugs against `corpus/job-postings/*.csv` and `_absence.csv`. **→ the 12 silent firms. → `_absence-cohort-audit.csv`.**
4. `git status` / `git diff --stat` / `git log origin/main..HEAD` → clean tree at 98906ea, already on origin/main.
5. Dedup baseline reads: 07-28 run in full, `longitudinal-2026-06.md` tail, layoff tracker (13 rows), `regulator-filings/` + `operator-statements/` + `marketing-campaigns/` listings, Ferdon file head for format.
6. WebSearch (domain-restricted, `afm.nl`) `AFM finfluencer study crypto exploratory research report` → **transient tool error; not retried. Target carried.**
7. WebSearch `Bitstamp newsroom press release 2026 brand campaign marketing` → surfaced `blog.bitstamp.net` **already branded "by Robinhood."**
8. `web_fetch` `blog.bitstamp.net` → **primary metadata verification** of the brand absorption + the Bitstamp Europe S.A. CASP licence number + page-1 post inventory. **→ ADDED as marketing-campaigns; Bitstamp's class-4 zero substantiated rather than assumed.**
9. WebSearch `Phantom wallet blog brand campaign 2026 marketing announcement` → surfaced the Phantom rebrand post + Forbes Feb-2026 piece.
10. `web_fetch` `phantom.com/learn/blog/introducing-phantom-s-new-brand-identity` → **dated 2023-06-21, OUT OF WINDOW. Not entered.** Bakken & Baeck + F37 Foundry recorded as watch-(q) evidence only.
11. `web_fetch` `bitstamp.net/bitstamp-way` → **empty body (client-rendered). Nothing extracted.** Carried.
12. WebSearch `"Bitstamp by Robinhood" rebrand announcement name change 2026` → acquisition completion 2025-06-02/03; **X-handle rename reported 2026-07-14 (aggregator only, `[VERIFY]`).**
13. WebSearch `Bitstamp X account renamed RobinhoodCrypto July 2026 Robinhood Chain` → corroborated the handle; **display name "Robinhood Crypto EU" from a search-result title only, `[VERIFY]`.**
14. `web_fetch` `blog.bitstamp.net/category/company-news` → partial render, older posts only. No net-new.
15. WebSearch `Ledger newsroom 2026 brand campaign marketing announcement press` → surfaced `ledger.com/blog`.
16. `web_fetch` `ledger.com/blog` → **full page-1 inventory**: X Games (07-24), Ledger Wallet campaign (07-08), *Revenge of the Atoms* franchise (03-13 flagship), CEO piece (07-03), Poland/MiCA (07-01), **and the global-footer Spurs jersey-patch lockup with a `uploads/2026/06/` asset path**. Also captured the **Ashby careers URL from Ledger's own footer** — the evidence behind watch (t).
17. WebSearch `Sui Foundation blog 2026 marketing campaign brand announcement` → surfaced the Holographik case study, `blog.sui.io`, `sui.io/press-center`, Sui Basecamp 2026 (Oct 7–8, Marina Bay Sands).
18. `web_fetch` `the-brandidentity.com/project/holographik-steers-suis-brand-clear-of-the-defi-casino-aesthetic` → **full read**: date 2026-06-15, Thelen and Francis verbatim, complete design-system scope. **→ ADDED as marketing-campaigns; watch (q) confirmed.**
19. `web_fetch` `ledger.com/blog-ledger-moonpay-bring-digital-ownership-to-the-x-games` → `published_time 2026-07-24T16:29:58Z`; ESPN/ABC/Nippon TV, jersey, venue, athletes, prior stops. **→ ADDED.**
20. WebSearch `Ledger San Antonio Spurs official jersey patch partner announcement 2026` → team-side + trade coverage; MarketBeat `2025-06-24` date slug.
21. `web_fetch` `ledger.com/ledger-and-san-antonio-spurs-partnership` → **`published_time 2025-06-25T15:49:07Z`; Wengroff verbatim + role; Gauthier ×2 (excluded); "U.S. is Ledger's top market globally"; Ledger Studio; two unsourced audience figures (refused); `modified_time 2025-07-14` flagged. → ADDED as class 4.**
22. `web_fetch` Ashby API endpoint for Ledger → **refused by the fetch tool's provenance rule. Board existence primary-sourced from Ledger's footer; API reachability `[VERIFY]`.**
23. WebSearch `ESMA BaFin AMF CONSOB marketing communication enforcement crypto CASP July 2026 misleading advertising` → **no net-new marketing-side enforcement.** Transitional/perimeter material only, all already held.
24. WebSearch `crypto company marketing team layoffs July 2026 growth brand department cut` → **no net-new.** All returned rows already in the tracker.
25. Repo-wide dedup greps (`ledger`, `wengroff`, `spurs`, `moonpay`, `x games`, `holographik`, `thelen`, `jordan francis`, `defi casino`, `robinhood crypto`, `bitstamp by robinhood`, `bakken`, `f37`) → all additions confirmed net-new before writing.

## Net-new / changed this run

- `corpus/operator-statements/ledger-wengroff-spurs-partnership-2025-06.md` (**NEW FILE — 1 net-new confirmed class-4 statement.** Ariel Wengroff, EVP Marketing & Communications, Ledger, 2025-06-25, verbatim + role + three-point date verification; Gauthier role-excluded but recorded as corporate disclosure; two firm-stated statistics refused; "Ledger Studio" flagged; `modified_time` caveat preserved)
- `corpus/marketing-campaigns/ledger-sports-sponsorship-portfolio-2025-2026.md` (**NEW FILE.** Spurs jersey patch 2025-06-25 three-year global + MoonPay X Games 2026-07-24 with ESPN/ABC/Nippon TV; jurisdiction-of-spend finding stated as sequence; June-2026 FCA date collision recorded and explicitly de-fanged; Theme-3 empty-row ambiguity; Young Star Game left unverified and undated)
- `corpus/marketing-campaigns/sui-holographik-brand-system-2026-06.md` (**NEW FILE.** Watch (q) confirmed at the matrix's flagship OVERLAP row; Francis quote entered as QUALIFIED with employer + title flags both open; Thelen verbatim; full design-system scope; Theme-4 axis with Ferdon; gradient-governance read as a Theme-1 gate-stack artefact)
- `corpus/marketing-campaigns/bitstamp-robinhood-brand-absorption-2025-2026.md` (**NEW FILE.** Directly-verified owned-channel metadata; CASP licence N00000003 under a US parent brand; third absence category proposed; Robinhood-row misclassification raised and deliberately not executed; two dates `[VERIFY]`-flagged)
- `corpus/job-postings/_absence-cohort-audit.csv` (**NEW FILE — 27 rows, all tracked slugs.** Script-independent cohort audit: 11 COVERED, 6 ABSENCE-RECORDED, 2 COVERED+ABSENCE, **12 SILENT**. Deliberately separate from `_absence.csv`, which the sync regenerates from the feed every run and would discard manual rows)
- `findings/longitudinal-2026-06.md` (2026-07-29 section)
- `corpus/weekly-runs/2026-07-29-corpus-run.md` (this record)
- **Not changed:** `job-postings/*.csv` (0 adds; `_absence.csv` + `_chrome-queue.csv` date re-stamps only); `agency-overlap-matrix.csv` + `agency-claims/*` (idempotent); `layoff-tracker/*` (0 adds, 0 corrections — the one candidate reclassification was declined for lack of evidence); `regulator-filings/*` (0 adds — day-28 silence holds)

## Recommendation for next run

1. **Close watch (t) — it is now the top item and it is upstream work, not sweep work.** Add the 12 silent firms to the lead-generator's company list. **Ledger first**: public Ashby board, standard API, zero technical blocker. Then Gemini and OKX (Tier-1). Until then, treat every class-1-derived absence claim as unsafe.
2. **07-31 is two days out and carries three things at once:** Kraken MiCA lapse, OKX 8% campaign end, Friday nomination check. **Prepare the captures before the date.** Note OKX is class-1 invisible — the checkpoint will need a manual read.
3. **Continue watch (p) on the unswept firms** — Bybit, OKX, Kraken, Coinbase, Crypto.com, Gemini, and all of Strata 2 and 4. Two firms swept properly in two days have each returned a load-bearing finding; the base rate here is extraordinary and the sweep is nowhere near done.
4. **Work the class-3 backlog, which has now not moved in two runs:** CNMV direct read, and the **AFM finfluencer study** (a second NCA on BaFin's channel). Do these *first* next run, before the class-4 sweep consumes the budget again.
5. **Resolve two open attributions:** Jordan Francis's employer (Sui Foundation `[VERIFY]`), and Sui's own account of the rebrand on `blog.sui.io` / `sui.io/press-center` — neither was read this run, so watch (p) is **not** discharged for Sui.
6. **Build the name-alias table for sweeping (watch u).** Resolve each tracked firm's current public brand name and primary social handles. Bitstamp proves a name-keyed instrument reports an active firm as silent.
7. **Phase 2 blocker, restated and now stronger:** six absence claims have been exposed as instrumentation artefacts in three days, and the class-1 absence file itself has been shown not to measure the cohort. **No "no public signal" sentence is written until (i) the firm's own channels have been read, (ii) the source class has had a full-range sweep, and (iii) for class 1, watch (t) is closed.**
8. **Escalate to Jukka:** (i) **watch (t) — the upstream company-list gap, 12 of 27 tracked firms, two of them Tier-1.** This is the single highest-value fix available and it is a data-entry task, not an engineering one. (ii) The mount's `unlink` block (still costing a stub file per rename). (iii) Scheduler cadence — two clean days running, close to resolvable.
