# Citation CONTENT audit — Chapter 4 (agency stack) and Chapter 7 (closing)

**Run date: 2026-09-02. Auditor pass: content, not provenance.** The repo's provenance gate proves every printed URL exists in a corpus record. It does **not** prove that a source supports the sentence citing it. This audit tests the second thing only, for `03-agency-stack.md` (Chapter 4) and `06-closing-implications.md` (Chapter 7).

**Method.** Every panel figure re-derived independently with `python3` from the eighteen `corpus/agency-claims/*.csv` files and `corpus/agency-overlap-matrix.csv`. Every external primary opened first-party this run (raw fetch, text extracted, quotes matched character-by-character) unless marked **NOT OPENED**. Failures retried once before being recorded as NOT OPENED.

**Two standing rules observed throughout.** (1) An agency's public client claim is a **claim**, never a confirmed engagement; this audit checked that the chapter never upgrades one, and it never does. (2) The `health_score` and `threat_level` columns in the agency CSVs are internal scoring, not public-source data: they were **excluded from every derivation below and appear nowhere in this file.**

**Verdict counts — 99 claims checked** (numbered rows 1–68 in Section A and 70–98 in Section B; no claim is numbered 69; plus the two time-sensitive re-checks in B3)**.**

| Verdict | n |
|---|---:|
| SUPPORTED | 76 |
| PARTIALLY SUPPORTED | 15 |
| **CONTRADICTED** | **7** |
| NOT OPENED | 1 |

**Headline: the panel arithmetic reproduces exactly — every one of the eleven figures, to the row.** The seven contradictions are one in Chapter 4's Bitpanda passage, two in its regulator anchors, and four in Chapter 7, all of the same species: a claim that widened in the retelling.

---

# SECTION A — CHAPTER 4 (`03-agency-stack.md`)

## A1. PRIORITY 1 — the panel arithmetic

Re-derived from the eighteen per-agency CSVs and the overlap matrix. Script logic: rows counted per file; a row is "category-only" iff `claimed_client` is one of the five generic strings; tracked-cohort membership read from `is_tracked_firm`; overlaps computed by grouping tracked firms by claiming agency file.

| # | Claim | What the chapter says | What the data says (re-derived) | Verdict | Action |
|---|---|---|---|---|---|
| 1 | Claim rows | "twenty-six client relationships" | 26 rows across 18 files | SUPPORTED | none |
| 2 | Specific-entity rows | "twenty-one naming a specific entity" | 21 | SUPPORTED | none |
| 3 | Category-only rows | "five naming only a category ('DeFi protocols', 'NFT projects', 'SaaS clients', 'early-stage tokens', 'fundraising clients')" | 5 — and the five strings match exactly, verbatim | SUPPORTED | none |
| 4 | Distinct named entities | "Twenty distinct entities are named" | 20 (21 specific rows − Sui claimed twice) | SUPPORTED | none |
| 5 | Tracked-cohort firms | "Eight are firms this report tracks" | 8: Binance, Bybit, KuCoin, MetaMask, OKX, Polygon, Solana, Sui | SUPPORTED | none |
| 6 | Claiming agencies | "four agencies account for all eight: Coinbound, MarketAcross, RZLT and Blockwiz" | exactly those 4 | SUPPORTED | none |
| 7 | Agencies with no tracked firm | "fourteen of the eighteen publicly claim no firm in this report's cohort at all" | 14: blue-manakin, bond-finance, crowdcreate, flexe, guerrillabuzz, icoda, lunar-strategy, majinx, ninjapromo, outset-pr, serotonin, single-grain, tokenminds, x10 | SUPPORTED | none |
| 8 | Agencies with no client at all | "seven of those fourteen name no client of any kind" | 7 zero-row files: blue-manakin, flexe, guerrillabuzz, majinx, outset-pr, serotonin, x10 — all 7 inside the 14 | SUPPORTED | none |
| 9 | Overlaps | "exactly one overlap (Sui — Coinbound + RZLT)" | exactly one: Sui = {coinbound, rzlt}. No other tracked firm has >1 claiming agency | SUPPORTED | none |
| 10 | Distribution | "seven of the eight claimed firms are claimed by one agency and the eighth by two" | 7 single + 1 double | SUPPORTED | none |
| 11 | Matrix ↔ CSV consistency | 8-row matrix table | `agency-overlap-matrix.csv` has 8 rows and every row reproduces from the claims files; no row in one and not the other | SUPPORTED | none |
| 12 | As-of date | "as of 2026-06-15" throughout | every one of the 26 rows carries `date = 2026-06-15`; matrix `as_of` likewise | SUPPORTED | none |
| 13 | Panel membership | 18 agencies | 18 CSV files; names match `tracked-firms.md` Stratum 5 and `methodology.md` §2 one-for-one | SUPPORTED | none |
| 14 | Class-1 status of the eight | "5 unobservable, 1 true absence (Polygon), 2 with rows" | `_absence-cohort-audit.csv` (2026-07-30) confirms all eight rows individually — Sui IN-FEED-BROKEN-SLUG (URL-encoded space, silent empty return, Getro board unreadable); Binance/Bybit/KuCoin ABSENCE-RECORDED or COVERED+ABSENCE with header-only CSVs; OKX NOT-IN-FEED (absent from the 147-company scanner config); Polygon IN-FEED-TRUE-ABSENCE; Solana 3 rows all institutional/BD growth; MetaMask 1 row, Product Marketing Lead – Trade, 2026-08-06, surfaced 2026-08-25 after the slug fix | SUPPORTED | none |
| 15 | Triangulation share | "available for a quarter of the claimed set" | 2 of 8 hold rows = 25%. But Polygon is a **clean scan returning zero** — a test that ran and produced a negative. On that reading the instrument produced a result for 3 of 8 (37.5%) | PARTIALLY SUPPORTED | Optional tightening: *"produces rows for two of the eight and a clean negative for a third; for the remaining five it cannot produce a test at all."* |

**The panel arithmetic reproduces exactly.** Nothing in PRIORITY 1 requires a change.

## A2. PRIORITY 2 — the Kraken / Gupta repudiation

Primary opened first-party: `https://incrypted.com/en/krakens-chief-growth-officer-depth-interview/` (HTTP 200; JSON-LD `datePublished` `2026-05-19T11:10:58+03:00`, `dateModified` `2026-05-19T11:39:28+03:00`).

| # | Claim | What the chapter prints | What the source says (verbatim) | Verdict | Action |
|---|---|---|---|---|---|
| 16–17 | KOL/tournament passage | "partner with local KOLs, run a tournament, claim the win. **Ukrainian users see right through that.** What they actually want is fiat ramps that work smoothly, a product that matches the sophistication of this market, and a partner that will invest in the ecosystem over the long-run." | *"The mistake many global players have made in Ukraine is treating it like other markets and running a standard marketing playbook: partner with local KOLs, run a tournament, claim the win. Ukrainian users see right through that. What they actually want is fiat ramps that work smoothly, a product that matches the sophistication of this market, and a partner that will invest in the ecosystem over the long-run."* | SUPPORTED | none — **exact, including the lead-in "running a standard marketing playbook"** |
| 18 | Organic claim | "we have never run a local campaign here. That success was largely organic. It was spread by word of mouth…" | *"Hundreds of thousands of Ukrainians are already registered with Kraken, and Ukraine is one of our strongest emerging markets by per-capita penetration – and we have never run a local campaign here. That success was largely organic. It was spread by word of mouth, from developers, from professional traders, from people who wanted a platform they could trust during the most difficult years of their lives."* | SUPPORTED | none — exact, whole paragraph |
| 19 | Operating model | "the operating model is what actually changed" | *"The title is almost the least interesting part. The operating model is what actually changed."* | SUPPORTED | none |
| 20 | AI engine | "a **natively AI growth engine**… Engineers are designing product ideas, marketers are shipping products." | *"We are now pushing towards being a natively AI growth engine where these lines blur even more. Engineers are designing product ideas, marketers are shipping products and the velocity of identifying growth opportunities in a multi-asset, multi-product, multi-geo ecosystem has suddenly 100x."* | SUPPORTED | none |
| 21 | Date | "On 19 May 2026" | page JSON-LD `datePublished 2026-05-19` | SUPPORTED | none |
| 22 | Outlet's marketing arm | "The outlet operates a marketing arm and a KOL network" | incrypted.com: *"Incrypted KEY — Comprehensive marketing services for your project"*; incrypted.com/key/: *"KOL marketing — The most influential and performing KOL's in our region"*, *"50+ successful campaigns"* | SUPPORTED | none |
| 23 | Affiliate link | "the page carries a Kraken affiliate link with no paid-placement disclosure visible" | `href="https://proinvite.kraken.com/9f1e/g5hwlmcf"` present in the article body; no sponsored/advertorial/partner-material disclosure anywhere in the fetched page | SUPPORTED | none |
| 24 | Written Q&A | "It is a written Q&A, not a recording." | page carries text only; no audio/video element | SUPPORTED | none |
| 25 | Speaker title | "Mayur Gupta, Chief Growth & Marketing Officer of Kraken" | Incrypted page: "Chief Growth & Marketing Officer". **The corroborating anchor `kraken.com/press/releases/kraken-appoints-mayur-gupta-as-cmo` is dated 19 April 2022** and reads *"appointment of Mayur Gupta as its Chief Marketing Officer (CMO)"* — it corroborates the person and the firm, **not the CGMO title** | PARTIALLY SUPPORTED | Anchor-block wording: replace *"role corroboration https://www.kraken.com/press/releases/…"* with *"person/firm corroboration only — Kraken press release, 19 April 2022, titles him CMO; the CGMO title rests on the Incrypted page alone."* |
| 26 | Paid-marketing reqs | "two 'Director, Paid Marketing' requisitions, US and UK, both posted 2026-07-23" | `corpus/job-postings/kraken.csv` — two rows, 2026-07-23, United States and United Kingdom, both Ashby, `url_verified=True` | SUPPORTED | none |

**Chapter 4's strongest material survives intact.** All four quoted passages are verbatim at the primary, and both provenance caveats the chapter prints are true.

## A3. PRIORITY 3 — the campaigns outside the panel's frame

### Bitpanda — `https://blog.bitpanda.com/en/experience-our-new-brand-campaign-now` (opened; on-page byline `25.09.2025`)

| # | Claim | What the chapter says | What the source says | Verdict | Action |
|---|---|---|---|---|---|
| 27 | Date | "25 September 2025" | on-page `25.09.2025` | SUPPORTED | none |
| 28 | Agency | "Its creative agency was **Serviceplan**… production was the German house 27km" | *"The campaign was directed by Carlo Oppermann and shot by one of Germany's leading production houses, 27km, and award-winning photographer Alex Waltl, with creative concept and execution by Serviceplan."* | SUPPORTED | none |
| 29 | Clubs | "five football clubs including Arsenal" | Paris Saint-Germain, FC Bayern Munich, AC Milan, FC Basel, Arsenal FC = 5 | SUPPORTED | none |
| **30** | **Creators** | **"named German-language Instagram creators"** | **The page names Melissa Satta and Caro Daur as "creators" and attributes to them NO nationality, NO language and NO platform. The only occurrence of "Instagram" on the page is Bitpanda's own footer social link.** | **CONTRADICTED** | **See A3-fix below** |
| 31 | Language versions | "four localised language versions" (anchor); "in four languages" (body) | EN original + DE, FR, IT links = **four language versions, three of them localisations** | PARTIALLY SUPPORTED | Anchor: change "four localised language versions" → **"four language versions (EN original plus DE, FR and IT localisations)"**. Body's "in four languages" is fine as printed. |
| 32 | Self-label | "self-labels — 'This Promotion'" | *"**This Promotion** does not constitute an investment advice or an invitation to conclude a transaction."* | SUPPORTED | none |
| 33 | Specific-loss warning | "warns that 'the invested amount may be lost completely'" | *"In extreme cases, the invested amount may be lost completely."* | SUPPORTED | none |
| 34 | Scope | "global brand campaign… across TV, out-of-home, digital and social" | *"our new global brand campaign"*; *"You'll soon see it everywhere, on TV, out-of-home, digital channels, and across social media."* | SUPPORTED | none |

**A3-fix — CONTRADICTION 1 (Chapter 4, Bitpanda passage).**

The chapter's phrase "named German-language Instagram creators" reads as sourced to the announcement page. It is not. The page names two creators and describes neither by nationality, language or platform. The descriptor was imported from the corpus file's *Theme-4(b)* cross-reference passage, which says "it names **Caro Daur** — a German creator whose primary surface is Instagram" — a single creator, and the corpus file's own inference, not the page's words. In the chapter it became plural, became "German-language", and acquired a platform. Compounding it: Melissa Satta, the other named creator, is not German-language on any reading.

This matters more than a wording slip, because the sentence's only job in the chapter is to set up the BaFin finfluencer collision — the German-speaking / Instagram configuration. Printing it as a fact of the announcement page overstates a real but weaker link.

> **Proposed replacement (body):** *"…with five football clubs including Arsenal and two named creators, Melissa Satta and Caro Daur. (The page attributes no nationality, language or platform to either; the German-language and Instagram limbs of the BaFin comparison are this corpus's reading of who Caro Daur is, not the announcement's words.)"*
>
> **Or, if the shorter line is wanted:** *"…with five football clubs including Arsenal and two named creator partners."* — and drop the descriptor entirely.

### Ledger — both announcements opened first-party

| # | Claim | What the chapter says | What the source says | Verdict | Action |
|---|---|---|---|---|---|
| 35 | Spurs deal | "a three-year NBA jersey-patch partnership with the San Antonio Spurs (announced 2025-06-25)" | `ledger.com/ledger-and-san-antonio-spurs-partnership`, `article:published_time 2025-06-25T15:49:07+00:00`, on-page `Company \| 06/25/2025`. Lede: *"official jersey patch sponsor of the San Antonio Spurs in a multi-year global partnership"*; body: *"This three-year partnership extends beyond the jersey patch…"* | SUPPORTED | none — "three-year" and "global" both on the page |
| 36 | X Games spot | "a 2026 X Games League activation carrying a 30-second national spot on ESPN and ABC" | `ledger.com/blog-ledger-moonpay-bring-digital-ownership-to-the-x-games`, `article:published_time 2026-07-24`: *"a 30-second TV spot airing on ESPN and ABC in the U.S."*; and *"a national TV commercial on ESPN and ABC, with international reach on Nippon TV in Japan"* | SUPPORTED | none |
| 37 | No agency | "**No agency is named anywhere in either announcement**" | Confirmed by full-text search of both pages. The X Games page contains no instance of the word "agency". The Spurs page's only instance is inside a Wengroff quote — *"tools that give them real agency in the digital world"* — which is not an agency name | SUPPORTED | none |
| **38** | **Ledger Studio** | **"the firm declares an in-house unit, 'Ledger Studio'"** | **The name IS on ledger.com — Spurs page: *"But we're also an educational platform… Through Ledger Academy, Ledger Studio, and our cultural work, we're making digital ownership simple, powerful, and personal."* That is the ONLY appearance. It is not on the X Games page. `ledger.com/ledger-studio` and `ledger.com/studio` both return HTTP 404. Search returns no Ledger crypto studio. Nowhere does any source say what Ledger Studio is, that it is a unit, that it is in-house, or that it does creative or production work.** | PARTIALLY SUPPORTED | **See A3-fix-2** |
| 39 | Wengroff | EVP, cited via corpus file | Spurs page: *"Ariel Wengroff, Ledger's Executive Vice President, Marketing and Communications."* | SUPPORTED | none |
| 40 | Matrix rows | "Ledger appears in zero matrix rows" | Ledger absent from all 18 claims files and from the matrix | SUPPORTED | none |

**A3-fix-2 — the "Ledger Studio" limb, and a correction to the sibling audit.**

The sibling audit recommended **cutting** this limb as unsourced, on the ground that it is absent from ledger.com, the X Games page and search. **That finding is itself wrong, and should not be actioned as written.** The string "Ledger Studio" is on ledger.com, in the Spurs announcement, in Ledger's own voice. Cutting it would remove a true fact.

What is genuinely unsupported is the **characterisation**. The page lists Ledger Studio alongside "Ledger Academy" and "our cultural work" in a sentence about being *an educational platform*. It never calls it a unit, never calls it in-house, and never connects it to producing marketing. Chapter 4 places the phrase immediately after "no agency is named anywhere in either announcement", where it functions as the implied answer to *who made the work* — an inference no source supports. Chapter 6 goes further still, calling it "a self-declared in-house **content** unit", which the source does not say at all.

> **Proposed replacement (Chapter 4 body):** *"**No agency is named anywhere in either announcement.** The firm names something called 'Ledger Studio' once, on its own site, alongside Ledger Academy and 'our cultural work' — with no description of what it is, and no statement connecting it to this work."*
>
> **Anchor block:** change *"'Ledger Studio' self-declared in-house"* → *"'Ledger Studio' named once on ledger.com (Spurs post) with no description; no ledger.com/studio page exists; NOT established as a production or creative unit."*
>
> **Flag to the Chapter 6 audit:** `05-next-twelve-months.md` prints "a self-declared in-house **content** unit called 'Ledger Studio'". "Content unit" appears in no source and should be narrowed the same way.

### Sui / Holographik — `https://the-brandidentity.com/project/holographik-steers-suis-brand-clear-of-the-defi-casino-aesthetic` (opened; on-page `Date Jun 15 2026`)

| # | Claim | What the chapter says | What the source says | Verdict | Action |
|---|---|---|---|---|---|
| 41 | Date | article published 2026-06-15, "the date of public disclosure, not of the work" | on-page `Date Jun 15 2026`; article describes the engagement as ongoing (*"constantly being built rather than delivered once"*) | SUPPORTED | none |
| 42 | The quote | "a genuine long-term creative partner. Less a delivery, more a living system built together." | *"As the ecosystem scaled, Holographik became a genuine long-term creative partner. Less a delivery, more a living system built together,"* he tells us | SUPPORTED | none — exact |
| 43 | Speaker `[VERIFY]` | "the speaker, Jordan Francis, 'Head of Design & Creative', is not attributed to an organisation in the source" | Article: *"for Jordan Francis, Head of Design & Creative…"* — no organisation stated anywhere. Contrast the agency side, explicitly labelled: *"Art Director Philipp Thelen"* | SUPPORTED | The `[VERIFY]` is correct and must be retained |
| 44 | Scope of the system | deployed "across products, events, websites and motion" | *"…to evolve the main Sui brand, expanding the identity and design system across products, events, websites and motion."* | SUPPORTED | Optional: "deployed" → "expanded", to match the source verb |
| 45 | Panel membership | "a studio outside the panel by construction"; anchor: "Holographik is NOT in the 18-agency panel and is not proposed for it" | Holographik has no file in `corpus/agency-claims/` and appears in neither `methodology.md` §2 nor `tracked-firms.md` Stratum 5 | SUPPORTED | none |

## A4. PRIORITY 4 — the standing corrections Chapter 4 declines to print

Each of these is a public assertion by the chapter that a corpus annotation is unsupported. Each was tested against the re-derived panel.

| # | Correction asserted | Test | Verdict | Action |
|---|---|---|---|---|
| 46 | `tracked-firms.md` annotates KuCoin "Three-agency overlap (RZLT + Blockwiz + MarketAcross)" — chapter says unsupported | KuCoin appears in **one** claims file: `blockwiz.csv`. RZLT claims Sui, Internet Computer, Near. MarketAcross claims Binance, Polygon, Solana. Neither names KuCoin | SUPPORTED — the correction is right | Chapter is correct to decline. Recommend the annotation in `tracked-firms.md` be struck or dated as pre-panel |
| 47 | HTX "NinjaPromo agency relationship" — chapter says unsupported | `ninjapromo.csv` holds exactly two rows: TRON, Polymath. HTX appears in **no** agency's claim list, anywhere | SUPPORTED — the correction is right | as above |
| 48 | `sport-sponsorship-reset-2026-05.md` §Synthesis: "MarketAcross holds PR retainers at Binance and Crypto.com simultaneously" | MarketAcross claims Binance, Polygon, Solana. **Crypto.com appears in no agency's claim list.** And "retainer" upgrades a public claim into a confirmed commercial relationship, which the standing rule forbids | SUPPORTED — the correction is right on both limbs | Chapter is correct to decline. The sentence should be struck from the corpus file, not merely left unprinted |
| 49 | May planning note's "three agencies on one firm" (Bybit, KuCoin, Sui) | Bybit: 1 (Blockwiz). KuCoin: 1 (Blockwiz). Sui: 2 (Coinbound, RZLT). **Maximum is two, at Sui alone** | SUPPORTED — the correction is right | none |
| 50 | "Per `methodology.md` §2 and the standing corpus rule, an agency's public client claim is a claim, not a confirmed relationship" | §2 says *"which firms each agency publicly claims as a client"* — consistent with the rule but **does not state it**. The rule is a standing corpus rule; §2 is not its text | PARTIALLY SUPPORTED | Change to *"Per the standing corpus rule (and consistent with `methodology.md` §2's 'publicly claims as a client')…"* |
| 51 | "panel provenance and the 2026-06-15 as-of date recorded in `methodology.md` §2 and §6" | §6 carries the date: *"NorthPoint competitor-intelligence pipeline (⚠ last refreshed 2026-06-15)"*. **§2 carries no date at all** — it carries the 18-agency list and the storage convention | PARTIALLY SUPPORTED | Change to *"panel membership in §2; the 2026-06-15 as-of date in §6"* |

**Note for the corrections block.** All four substantive corrections hold. This is the strongest part of the chapter's self-policing and should ship as written, subject only to the two citation-precision fixes at #50 and #51.

## A5. PRIORITY 5 — the zero-endings claim

| # | Claim | Test | Verdict | Action |
|---|---|---|---|---|
| 52 | "zero named agency-relationship endings, corpus-wide" | Repo-wide sweep of `corpus/` for ending/termination/loss/non-renewal/parted-ways/no-longer-client language intersected with agency names and retainer vocabulary. **No hit describes an agency relationship ending.** The only "parted ways" hits are the Messari layoff row (employees, not agencies) and the same phrase quoted in a citation-opening sweep. No firm-side announcement ending a named agency relationship; no agency announcement losing a named client | SUPPORTED | none |
| 53 | Sponsorship-reset §1, §6, §7 excluded as uncited | File carries `🔴 UNSOURCED — DO NOT CITE` inline at §1 (Bybit / Red Bull), §6 (Crypto.com — McGhee) and §7 (Tour de Suisse / Zondacrypto). **§1 and §7 are the actual sponsorship endings** — the Red Bull non-renewal and the Zondacrypto termination — so the two incidents that would most support a "sponsorship endings" reading are precisely the two that cannot be cited | SUPPORTED | none — and the chapter's phrasing *"even that is only partly citable"* is exactly right |
| 54 | "three of the seven incidents… carry no citation anywhere in this corpus" | Correct as of the 2026-08-31 state: §2, §3, §4, §5 anchored; §1, §6, §7 not. ⚠ **The corpus file contradicts itself**: its top disposition block says four anchored / three unsourced (post-08-31), while its closing "Public-record verifiability" section still says *"three of seven incidents are anchored… four carry no citation at all"* (the pre-08-31 state). **The chapter follows the correct, updated reading** | SUPPORTED | Flag to corpus maintenance: the closing section of `sport-sponsorship-reset-2026-05.md` is stale by one incident and should be reconciled with its own header |

## A6. PRIORITY 6 — the regulator anchors

### ESMA finfluencer factsheet — PDF opened first-party (HTTP 200, `application/pdf`, full text extracted)

| # | Claim | What the chapter says | What the source says | Verdict | Action |
|---|---|---|---|---|---|
| 55 | Paid-partnership line | "If you're getting money, gifts or perks to promote something, don't hide it – say it loud and clear. **Not in tiny text. Not just hashtags.**" | *"If you're getting money, gifts or perks to promote something, don't hide it – say it loud and clear. Not in tiny text. Not just hashtags."* | SUPPORTED | none — exact |
| 56 | Disclaimer line | "**Disclaimers such as 'This is not investment advice' will not protect you in these cases.**" | *"Disclaimers such as 'This is not investment advice' will not protect you in these cases."* | SUPPORTED | none — exact |
| 57 | Audience | "it is addressed to nobody who holds a licence. Not one sentence is directed at a CASP, an issuer or an authorised firm, and the document disclaims its own legal force" | Second person throughout, addressed to the influencer. The only licensing references are to *the influencer's own* potential need for one (§5) and to checking *whether the promoted firm* is authorised (§4). Colophon: *"This factsheet is not intended as legal advice or regulatory interpretation of possible applicable rules. It is intended as general guidance only."* | SUPPORTED | none |
| 58 | Publication date | "published January 2026" | The PDF's own imprint reads **"© European Securities and Markets Authority, 2025"**, "Luxembourg: Publications Office of the European Union, **2025**", catalogue code `EK-01-25-037-EN-N`. The ESMA landing page carries **no publication date at all** (verified). The only January-2026 evidence is ESMA's file path `/sites/default/files/2026-01/` | PARTIALLY SUPPORTED | The corpus file handles this correctly (*"produced in 2025 and published in January 2026"*). The **chapter body** states "published January 2026" bare. Recommend the body carry the month-precision qualifier once: *"published to ESMA's site in January 2026 (month precision — ESMA's own file path; the document's imprint carries a 2025 production year)"* |
| 59 | CONSOB amplification | "amplified by CONSOB on 12 January 2026" | CONSOB press release PDF opened: *"Finfluencers, ESMA issues tips for responsible conduct"*, closing line **"Rome, 12 January 2026"** | SUPPORTED | none |

### BaFin — press release AND chapter page both opened first-party

| # | Claim | What the chapter says | What the source says | Verdict | Action |
|---|---|---|---|---|---|
| 60 | Date | "BaFin's *Risks in Focus 2026* (28 January 2026)" | Press release `pm_2026_01_28_PK_Risiken_im_Fokus_en.html`: on-page date `28/01/2026`, byline `| Press release | 28 January 2026`, and *"Press Conference 'Risks in BaFin's Focus', 28 January 2026"* | SUPPORTED | none |
| **61** | **Screening commitment, and where it is anchored** | Body: "committing to random screening of German-speaking finfluencers on YouTube and Instagram". Anchor: *"…German-speaking finfluencer screening commitment on YouTube and Instagram (corpus file …; **press release `pm_2026_01_28_PK_Risiken_im_Fokus_en.html`**)"* | **The press release does NOT contain this commitment.** Full-text search of the fetched press release: "screening" = **0 occurrences**; "YouTube" = **0**; "Instagram" = **0**; "German-speaking" = **0**. The commitment is on the **chapter page** `RIF_verbraucher_sozialemedien_en.html`: *"A random market screening of selected German-speaking finfluencers on the social media channels YouTube and Instagram will be the first step in this process."* | **CONTRADICTED** | **See A6-fix** |

**A6-fix — CONTRADICTION 2 (Chapter 4, BaFin anchor). This is the same defect the sibling audit found in Chapter 5, and Chapter 4 has it too.**

The substance is right — BaFin did make the commitment, in those exact words. The anchor is wrong: it points at a URL that does not contain the sentence. The press release establishes the **date** and nothing else about the screening; the chapter page establishes the **commitment** and carries no publication date of its own. The citation needs both, doing different jobs.

> **Proposed replacement (anchor block):** *"**BaFin *Risks in Focus 2026*, 28 January 2026 — German-speaking finfluencer screening commitment on YouTube and Instagram.** Commitment verbatim from the consumer chapter `https://www.bafin.de/EN/die-bafin/publikationen-daten/risiken-im-fokus/Fokusrisiken_2026/RIF_Verbraucher_2/RIF_verbraucher_sozialemedien_en.html` (the chapter page carries no publication date of its own); **date** from BaFin's press release `https://www.bafin.de/SharedDocs/Veroeffentlichungen/EN/Pressemitteilung/2026/pm_2026_01_28_PK_Risiken_im_Fokus_en.html`, which does **not** contain the screening sentence. Corpus file `../corpus/regulator-filings/bafin-risks-in-focus-crypto-finfluencer-2026-01.md`."*

Note the corpus file itself is correct — it attributes the quote to the chapter page under "Verbatim capture". The error was introduced in the chapter's anchor block. **Recommend a repo-wide check of every BaFin citation for the same substitution.**

### FCA Premier League warning — the `[VERIFY]` is dischargeable, and it changes the date

| # | Claim | What the chapter says | What the source says | Verdict | Action |
|---|---|---|---|---|---|
| 62 | Castledine quote | "Millions of football fans trust their club's badge." | FCA's own press release, verbatim: *"'Millions of football fans trust their club's badge. Clubs should not let unauthorised financial firms exploit that loyalty by putting potentially dodgy products in front of millions of fans."* Title on the FCA's own page: *"director of consumer investments at the FCA"* | SUPPORTED | none — exact at the FCA primary |
| **63** | **Date** | Anchor: "FCA warning to Premier League clubs on unauthorised crypto sponsorship, **2026-06-02**" | **FCA's own press release: "First published: 03/06/2026. Last updated: 03/06/2026."** The 2026-06-02 date comes from the Reuters URL slug, which this audit **could not open** | **CONTRADICTED** | **See A6-fix-2** |
| 64 | The `[VERIFY]` | "`[VERIFY]` the FCA's own press-release URL on fca.org.uk as top-line primary — the corpus currently anchors to Reuters" | **DISCHARGED.** Found and opened: `https://www.fca.org.uk/news/press-releases/football-clubs-warned-questionable-sponsorship-deals-unauthorised-firms` (HTTP 200). Also opened the underlying letter: `https://www.fca.org.uk/publication/correspondence/sponsorship-arrangements-football-clubs.pdf` | SUPPORTED — resolved | Replace the Reuters anchor with the FCA primary and clear the `[VERIFY]` |
| **65** | **Reuters anchor** | top-line primary in the anchor block | **NOT OPENED.** `curl` → HTTP 401; retried once via WebFetch → proxy HTTP 403. Recorded as unopened per the rule; **not treated as verified in any respect** | **NOT OPENED** | Retire it as the top-line anchor; if retained at all, retain as a secondary and mark it unopened at audit |
| 66 | Clubs' exposure | "could expose them to liability" | FCA press release, *For clubs: what the FCA expects*: *"Sponsorship deals with unauthorised financial services firms don't just harm fans. They potentially expose clubs to legal liability, money laundering risks and serious reputational damage."* The letter adds the statutory basis: breaches of **s.19** and **s.21 FSMA**, *"Both activities are criminal offences"*, and *"Football clubs entering into sponsorship arrangements with unauthorised firms may face legal, operational, and reputational risk"* | SUPPORTED | none — the FCA primary supports this **better** than the Reuters anchor did |
| 67 | Addressee | "the FCA warned Premier League clubs" | FCA: *"The FCA has written directly to football clubs, **mainly in the Premier League**"* — and the letter is addressed to football clubs generally | PARTIALLY SUPPORTED | Narrow to *"warned football clubs, mainly in the Premier League"* |

**A6-fix-2 — CONTRADICTION 3 (Chapter 4, FCA date and anchor).**

The chapter's body says only "in June 2026", which is safe. The **anchor block** prints `2026-06-02`, which the FCA's own release contradicts (First published 03/06/2026). Under the repo's own rule — date the artifact from the fetched document — the FCA primary dates itself 3 June 2026. The 2 June date survives only as the date of a Reuters story this audit could not open.

> **Proposed replacement (anchor block):** *"**FCA warning to football clubs, mainly in the Premier League, on sponsorship by unauthorised firms — FCA press release, first published 3 June 2026** (`https://www.fca.org.uk/news/press-releases/football-clubs-warned-questionable-sponsorship-deals-unauthorised-firms`), with the underlying letter to clubs (`https://www.fca.org.uk/publication/correspondence/sponsorship-arrangements-football-clubs.pdf`, ss.19 and 21 FSMA). Lucy Castledine, director of consumer investments, verbatim. `[VERIFY]` **cleared 2026-09-02** — FCA primary opened first-party; the previous Reuters anchor (dated 2 June by its URL slug) is retired and was not openable at audit."*

Also update the corpus file `fca-premier-league-sponsorship-warning-2026-06.md`, whose closing line still says *"To strengthen before synthesis: locate and attach the FCA's own press-release URL"* — that task is now done.

### MAS

| # | Claim | Test | Verdict | Action |
|---|---|---|---|---|
| 68 | "MAS's *Guidelines on Standards of Conduct for Digital Advertising Activities*… remains uncaptured. `[VERIFY]`… the corpus holds only a consultation record, and the widely-repeated 25 March 2026 effective date is expressly not admitted" | `_mas-digital-advertising-guidelines-provenance-2026-08-16.md` confirms: the named URL serves a **consultation record** (P003-2023, start 25/04/2023, closing 30/06/2023, MAS response date 22/05/2026), not the guidelines. Instrument UNADMITTED | SUPPORTED | none — the chapter handles this correctly and does not print the unadmitted date |

---

# SECTION B — CHAPTER 7 (`06-closing-implications.md`)

Chapter 7 introduces no new primary sources. The test applied here is different: **is every restatement faithful to the chapter it cites, and has any claim widened in the retelling?** Chapter 7's own preamble sets the standard — *"Where a limit was attached upstream it is repeated here rather than dropped."* Four sentences fail it.

## B1. The six-instrument summary

| # | Chapter 7 sentence | Source chapter | Verdict | Action |
|---|---|---|---|---|
| **70** | "Its field for the trading-platform estate… is **populated in forty rows of three hundred and twenty-nine**, and differs from the corporate website in two" | Chapter 5: *"It is populated in **47 of 329 rows**: four are the literal string `n/a`, three are column-bleed artifacts this corpus itself documented, leaving **40 real values, of which 2 record a surface differing from the firm's corporate website.**"* | **CONTRADICTED** | **See B1-fix** |
| 71 | "differs from the corporate website in two" | Ch5: "of which 2 record a surface differing from the firm's corporate website" | SUPPORTED | none |
| 72 | "watched twenty-seven firms for twelve months and captured twelve qualifying marketing requisitions, none of whose job-description bodies were ever read" | Ch3: *"twelve qualifying marketing or growth postings across the entire twenty-seven-firm tracked cohort for the whole twelve-month window"*; *"not one of the twelve has had its JD body read"*. Ch2: *"Twelve requisitions, eight firms, twelve months."* | SUPPORTED | Optional: "marketing **or growth** requisitions", to match Ch3's scope exactly |
| **73** | "**Five of the cohort's firms were never reachable at all**; the panel that records this is a fact about the scanner, never about them" | Ch3: *"Five tracked firms sit in the absence panel because their careers infrastructure is **unreachable by the API scan** — Aave on a Lever 404; Binance, Bybit, HTX and KuCoin on proprietary applicant-tracking systems — a fact about the scanner, not about them."* Ch2 prints the same five **frozen at 2026-08-31** and notes *"any count drawn from the panel [is] non-reproducible"* | PARTIALLY SUPPORTED | **See B1-fix-2** |
| **74/75** | "**The eighteen-agency panel** found that fourteen of eighteen crypto-native agencies publicly claim no firm in this cohort, while **the two largest brand campaigns in the window ran through agencies the panel is structurally unable to see**" | Ch4: *"the two largest brand campaigns **the corpus captured** in the window — Bitpanda's… and Ledger's… — ran through agencies this panel is structurally incapable of seeing, **one of them through no named agency whatsoever**."* | 74 SUPPORTED / **75 CONTRADICTED** | **See B1-fix-3** |
| **76** | "**The layoff record** holds **twenty-six contractions in which no tracked firm names a function at all**" | Ch6: *"Twenty-six public workforce contractions… — **seven inside the tracked Stratum 1–4 cohort, nineteen at the perimeter. Not one of the seven tracked rows names a function at all.**"* And Ch6's own correction block: *"**two name marketing** — Gnosis (2026-07-17) and MANTRA (2026-01-14), both perimeter"* | **CONTRADICTED** | **See B1-fix-4** |
| 77 | "the single most specific description of AI inside a marketing team in this entire corpus arrived from a perimeter firm's quarterly report to its token holders, and had to be filed under a class name that did not previously exist" | Ch3: Gnosis Q2-2026 quarterly report, *"a dated document addressed to token holders rather than to press or recruits"*; *"The corpus file names the class, because it had no name before"*; *"No interview in this corpus does both."* | SUPPORTED | Attribution reads "(Chapters 2 and 3)"; the material is Chapter 3's. Optional tidy |
| 78 | "a press page that is a logo-download portal and an investor feed that last built in September 2022; a second Tier-1's leadership page has not moved in twenty-eight months" | Ch2, verbatim on all three limbs (Coinbase press page, IR RSS `lastBuildDate` September 2022, OKX leadership page 28 months) | SUPPORTED | none |

**B1-fix — CONTRADICTION 4 (Chapter 7, the register figure).**

Chapter 5 states a **raw** population (47) and a **cleaned** count (40 real values, after removing four `n/a` strings and three documented column-bleed rows). Chapter 7 prints the cleaned number as though it were the raw population: "populated in forty rows of three hundred and twenty-nine". That is not what the register says — the field is populated in 47 rows — and it silently discards the derivation that makes 40 defensible. A reader checking `ae_website_platform` against the snapshot will count 47 and conclude the report is wrong.

> **Proposed replacement:** *"Its field for the trading-platform estate — the surface where marketing actually happens — carries a real value in **forty of three hundred and twenty-nine rows** (populated in forty-seven, less four `n/a` strings and three documented column-bleed rows), and in only two of those forty does the value differ from the firm's corporate website (Chapter 5, as at the 2026-08-17 capture)."*

**B1-fix-2 — the absence panel (Chapter 7 widens Chapter 3).**

Chapter 3 scopes the claim to the instrument: "unreachable **by the API scan**". Chapter 7 drops the scope and adds two absolutes: "**never** reachable **at all**". That is precisely the reading the corpus's own class-1 reading rules forbid — *"The supportable sentence is 'not reachable through the ATS APIs this corpus scans.'"* It is also demonstrably false as an absolute: MetaMask/ConsenSys sat in that panel and left it on 2026-08-25 when a slug was fixed, surfacing a posting that had been public for nineteen days. The trailing clause ("a fact about the scanner") repairs part of the damage, but the sentence a reader quotes will be the first half.

Second, smaller point: the corpus reading rule of 2026-08-27 extends its prohibition to *"any published count of absent firms"*, on the ground that membership moves with network conditions on the morning of the scan. Chapter 2 handles this by printing the five as a **frozen enumeration at 2026-08-31**. Chapter 7 prints a bare count with no freeze date.

> **Proposed replacement:** *"Five of the cohort's firms — the panel as frozen on 31 August 2026 — were not reachable through the applicant-tracking APIs this scan uses at all; the panel that records this is a fact about the scanner, never about them."*

**B1-fix-3 — CONTRADICTION 5 (Chapter 7 widens Chapter 4's campaign claim, twice in one clause).**

Two separate widenings:

1. Chapter 4 says "the two largest brand campaigns **the corpus captured** in the window". Chapter 7 says "the two largest brand campaigns **in the window**" — converting a claim about what this corpus saw into a claim about the market. Nothing in the report establishes that these were the two largest campaigns the industry ran.
2. Chapter 4 says they ran through agencies the panel cannot see, **"one of them through no named agency whatsoever."** Chapter 7 drops that clause and asserts both ran "through agencies". For Ledger this is affirmatively unsupported: I confirmed first-party this run that **no agency is named anywhere in either Ledger announcement**. Chapter 7 asserts the existence of an agency no source establishes.

> **Proposed replacement:** *"**The eighteen-agency panel** found that fourteen of eighteen crypto-native agencies publicly claim no firm in this cohort — while the two largest brand campaigns the corpus captured in the window sat outside its frame entirely: one run by a mainstream agency the panel is structurally unable to see, the other naming no agency at all (Chapter 4, as of 2026-06-15)."*

**B1-fix-4 — CONTRADICTION 6 (Chapter 7 widens Chapter 6's layoff null).**

Chapter 6's null is scoped to the **seven tracked rows**, and Chapter 6 explicitly retired the tracker-wide version of the claim: *"The tracker-scoped claim is retired; the cohort-scoped claim — no tracked firm's 2026 contraction names marketing — holds across all seven tracked rows and is the version used here."*

Chapter 7's sentence — "twenty-six contractions in which no tracked firm names a function at all" — reinstates the tracker-wide reading by attaching the property to all twenty-six. Nineteen of the twenty-six are perimeter rows, which are not tracked firms at all, and **two of them do name marketing** (Gnosis, MANTRA). On the most natural reading Chapter 7 states the exact claim Chapter 6 retired.

Chapter 7's later refusal section gets this right — *"We cannot say that the marketing function was cut in 2026. No tracked firm's contraction names it. The two rows in the entire record that name marketing are perimeter firms"* — so the chapter contradicts itself internally as well.

> **Proposed replacement:** *"**The layoff record** holds twenty-six contractions, seven of them inside the tracked cohort, and not one of those seven names a function at all (Chapter 6)."*
>
> **And the same fix in the closing absence-read (#97):** *"twenty-six contraction announcements, of which the seven from tracked firms name no function"* — replacing *"twenty-six contraction announcements that name no function"*.

## B2. The clocks, the refusals and the implications

| # | Chapter 7 sentence | Source chapter | Verdict | Action |
|---|---|---|---|---|
| 79 | "The Dutch supervisor published operational guidance in January 2025, waited fifteen months, re-tested the market and found the same defects" | Ch1: AFM baseline **21 January 2025**; April-2026 review; *"Fifteen months separate them, and the defects are the same in both."* | SUPPORTED | none |
| 80 | "roughly twenty-eight months from rulebook to first named case against a major exchange" | Ch1: *"took effect in October 2023; its first landmark enforcement action against a major exchange landed in February 2026 — a lag of roughly twenty-eight months"* | SUPPORTED | ⚠ Inherited tension, flag to the Ch1/Ch5 audits: Ch1 measures to the **February 2026 announcement** (28 months); Ch5 records the **claim issued 21 October 2025** (~24 months). Both chapters hedge with "roughly", so no fix required here |
| 81 | "that case is live: **proceedings stayed by consent until 8 September 2026**" | Ch5 carries the same facts **plus a limit Chapter 7 drops**: *"⚠ The stay is scoped 'as between the Claimant and the First Defendant' only; defendants 2–5, including the promotions-controllers class, are not party to it, **so do not write 'the case is paused' without that qualification.**"* | PARTIALLY SUPPORTED | Chapter 7's own rule requires the limit to travel. **Proposed:** *"…proceedings stayed by consent until 8 September 2026 as between the FCA and the first defendant only — defendants 2 to 5, including the promotions-controllers class, are not party to that stay."* |
| 82 | "an advertising platform now requires **MiCA/CASP certification** for EU and EEA crypto ads" | Ch5 / corpus: Google's policy requires advertisers to *"Be **licensed** as a Crypto-Asset Service Provider (CASP) under… MiCA by a relevant national competent authority"* **and separately** *"Be **certified by Google**."* Two distinct requirements | PARTIALLY SUPPORTED | In a report about regulated marketing language this distinction matters. **Proposed:** *"an advertising platform now requires a MiCA CASP licence — plus its own advertiser certification — for EU and EEA crypto ads"* |
| 83 | "Two Tier-1 CMO seats went vacant in the deadline month itself and neither firm has publicly named a permanent successor" | Ch2: *"both vacancies fell in June, the MiCA transitional period's final month"*; *"**No permanent successor to either the Binance or the Crypto.com seat has been publicly named**"* | SUPPORTED | none — and **re-verified today**, see B3 |
| 84 | "a third firm's marketing seat cannot be established from any public source" | Ch2: *"the top marketing seat at three of the eleven Stratum-1 exchanges… became vacant, interim, or unestablishable from any public source"* | SUPPORTED | none |
| 85 | Anchor block: "**The four** vacant, interim or unestablishable senior seats" | Ch2's **section header** reads "Four seats, one month"; Ch2's **body** says "three of the eleven Stratum-1 exchanges". Chapter 7's own body says **three** (two vacancies + one unestablishable) | PARTIALLY SUPPORTED | Chapter 7 is internally inconsistent: body says three, anchor says four. **Proposed:** anchor → *"The vacant, interim and unestablishable senior seats (Ch2's 'Four seats, one month' section; three Stratum-1 firms)"* — and flag the header/body mismatch to the Chapter 2 audit |
| 86 | "No requisition anywhere in the twelve-month record names MiCA, regulated marketing communications, or marketing compliance in its title" | Ch2: *"**No title names compliance, regulatory marketing communications, or MiCA**"* | SUPPORTED | none |
| 87 | "the interim CMO of the firm that withdrew from the European Union giving a long interview… seventeen days after the deadline without mentioning MiCA, the EU or the exit once" | Ch2, verbatim including "seventeen days after the deadline" and "exactly zero times" | SUPPORTED | none. ⚠ Ch2 labels this an **indexed-visibility** claim; Chapter 7 does not repeat the label, but its own preamble and anchor list flag Chapter 2's press-and-search-visibility caveat, so the limit does travel |
| 88 | "of twenty-six contractions, nine carry an AI framing and five carry a firm's verbatim words, with one reaching the public only through an anonymous source and one being this corpus's own inference from the word 'automation'" | Ch3/Ch6: *"nine of twenty-six rows carry an AI framing and five carry a verbatim firm statement. **One of the nine** is anonymously sourced, one is this corpus's own inference from the word 'automation,' and a tenth row is labelled `Y-ADJACENT` and barred from the count."* | SUPPORTED | ⚠ One clarity fix: Chapter 7's "with one… and one…" attaches ambiguously and can be read as qualifying **the five**, when both belong to **the nine**. **Proposed:** *"…nine carry an AI framing — of those nine, one reaches the public only through an anonymous source and one is this corpus's own inference from the word 'automation' — and five carry a firm's verbatim words."* ⚠ Separately, flag to the Ch3/Ch6 audits: the corpus README states *"the adjudicable denominator is 25, not 26"* and that row 6 (MARA) is flagged to strike at ship. Chapter 7 faithfully restates 26; the denominator question is upstream, not here |
| 89 | "Two firms refused the framing outright" | Ch3 table: Robinhood *"declined the AI-blame framing"* → `N` explicit refusal; Uphold *"explicitly non-AI"* → `N` explicit refusal | SUPPORTED | none |
| 90 | "The two rows in the entire record that name marketing are perimeter firms… a governance forum reply and a hiring-referral post" | Ch6: *"two name marketing — Gnosis (2026-07-17) and MANTRA (2026-01-14), both perimeter"*; closing: *"a governance forum reply and a hiring-referral post on X"* | SUPPORTED | none |
| 91 | "for fourteen of the sixteen tracked firms absent from ESMA's CASP register the absence is a category error" | Ch5: *"Fourteen of the sixteen absent tracked firms are a **category error**"* | SUPPORTED | none |
| 92 | "98.8% Italian… Italy has authorised 2.8%… Germany appears zero times having authorised more than any other member state… reason field is empty in 166 of 167 rows — so it could not express a marketing-communications action even if one existed" | Ch5, verbatim on all four limbs, including *"the register could not express a marketing-communications action even if one existed"* | SUPPORTED | none. Ch7 also carries Ch5's *"at least as much a notification artefact as an enforcement one"* — the upstream limit travels correctly |
| 93 | FCA defendant class — *"the persons currently in control of promotions"*, nine platforms, successors bound to 31 October 2028 | Ch5, verbatim from the sealed order; fifth defendant class extends to *"on or before 31 October 2028"* on the same nine platforms | SUPPORTED | none |
| 94 | "In the only live marketing-side action in this record, the marketing function is not a compliance stakeholder. It is a defendant class." | Ch5: *"The one live marketing-side action is not in the EU"*; *"The marketing function is not a compliance stakeholder in that document. It is a defendant class."* | SUPPORTED | none |
| 95 | "The marketing function in crypto in 2026 is simultaneously the industry's **most heavily resourced public activity** and its least documented one" | Nothing in Chapters 1–6 establishes marketing as the industry's most heavily resourced public activity. No spend figure of any kind is admitted anywhere in the report; the one market-spend number in the corpus (£130M Premier League, via Bloomberg-as-cited-by-BeInCrypto) is explicitly logged as secondary context | PARTIALLY SUPPORTED | Rhetorical superlative with no upstream anchor. **Proposed:** *"…is simultaneously one of the industry's most visible public activities and its least documented one."* |
| 96 | Closing: "an agency panel **looking at the wrong segment**" | Ch4 explicitly disclaims exactly this framing: *"**The finding is not 'the panel is wrong.' It is that the panel measures a specific market segment**"*; and *"It is not a census of the agency market, and that is what explains the segment boundary — it does not excuse it."* | PARTIALLY SUPPORTED | **Proposed:** *"an agency panel photographing one segment of the market while the money moved outside its frame"* |
| **97** | Closing: "twenty-six contraction announcements that name no function" | Same defect as #76 | **CONTRADICTED** | Fix as at B1-fix-4 |
| 98 | "**Private gatekeepers moved before public ones**" | Defensible on the "gate that actually fires" reading, which the next clause supplies. But on dates the AFM's operational guidance (21 January 2025) **precedes** Google's EU policy effective date (23 April 2025) | PARTIALLY SUPPORTED | **Proposed:** *"A private gatekeeper's gate closed before any public one did"* — which is what the following clause actually argues |

## B3. The two time-sensitive claims — re-checked today, 2026-09-02

Chapter 7 flags both itself and requires both to be re-checked on the day of publication. The report publishes **15 September 2026**.

| Claim | Status as at 2026-09-02 | Publication risk | Action |
|---|---|---|---|
| **The FCA stay expires 8 September 2026** | **Still stayed.** FCA's own proceedings page (`fca.org.uk/news/statements/htx-huobi-legal-proceedings`) opened first-party: First published 10/02/2026, **Last updated 26/08/2026**, `article:modified_time 2026-08-26T10:34:02+01:00` — no update recording an outcome. Public reporting through mid-August confirms settlement talks and no resolution | 🔴 **HIGHEST.** Chapter 7 currently reads *"that case is live: proceedings stayed by consent until 8 September 2026, **seven days after this report's original ship date**."* On a 15 September publication the stay will have **expired seven days before** the report appears. The sentence will read as forward-looking on a date when it is already past | Rewrite to be publication-date-safe **and** re-check on 15 September. **Proposed:** *"…and that case was live as this report closed: proceedings stayed by consent, as between the FCA and the first defendant only, until 8 September 2026 — a date that falls one week before publication. **Status as at [publication date]: [re-check].**"* Add the FCA proceedings page to the day-of-publication check list |
| **The succession null** | **Holds.** No permanent successor publicly named at either Binance or Crypto.com as at 2026-09-02. Binance coverage still describes Eowyn Chen as **interim** CMO; no Crypto.com CMO appointment has been announced since Kalifowitz stepped down on 30 June 2026 (the only "Crypto.com appoints CMO" results remain the 2020 Kalifowitz announcement — the same stale-article false positive Chapter 2 already documents and refuses) | 🟡 Moderate — a single announcement between now and 15 September would falsify it | Re-check on 15 September. Chapter 7 should carry the date on which it was last true. **Proposed:** *"…and neither firm had publicly named a permanent successor as at [publication date]."* ⚠ Whoever re-checks must apply Chapter 2's stale-article rule: a search for "Crypto.com names new CMO" returns a **12 August 2020** page announcing Kalifowitz himself |

---

# SECTION C — decisions needed

## C1. The seven contradictions, ranked by what a reader would catch first

**1. Chapter 4, Bitpanda — "named German-language Instagram creators."** The announcement page names two creators and attributes to neither a nationality, a language or a platform. This is the easiest contradiction in either chapter to check: a reader opens one URL and reads one paragraph. It also sits directly under the BaFin collision it is there to set up, so getting it wrong weakens the very comparison it supports. **Fix at A3-fix. Decision: adopt the longer replacement (which keeps the BaFin link, correctly labelled as this corpus's reading) or the shorter one (which drops it).**

**2. Chapter 4, BaFin anchor — the screening quote is anchored to a URL that does not contain it.** Identical in kind to the defect the sibling audit found in Chapter 5. The substance is right and the corpus file is right; the chapter's anchor block points at the press release, which contains none of "screening", "YouTube", "Instagram" or "German-speaking". **Fix at A6-fix. Decision: adopt the two-URL anchor (chapter page for substance, press release for date). Then sweep every other BaFin citation in the report for the same substitution — this is now two chapters with the same error, which makes it a pattern rather than a slip.**

**3. Chapter 7 — the layoff null reinstated at tracker scope (twice).** Chapter 6 explicitly *retired* the tracker-wide version of this claim, because two perimeter rows name marketing. Chapter 7 reinstates it in the six-instrument summary and again in the closing absence-read, and contradicts its own refusal section in the process. **Fix at B1-fix-4, in both places.**

**4. Chapter 7 — the two brand campaigns.** Two widenings in one clause: "the corpus captured" dropped (a claim about the corpus becomes a claim about the market), and "one of them through no named agency whatsoever" dropped (asserting an agency at Ledger that no source names — verified first-party this run). **Fix at B1-fix-3.**

**5. Chapter 7 — "populated in forty rows of three hundred and twenty-nine."** The field is populated in 47; 40 is the count after cleaning. Presenting the cleaned figure as the raw one both misstates the register and discards the derivation that makes it defensible. **Fix at B1-fix.**

**6. Chapter 4, FCA date — 2026-06-02 against the FCA's own 03/06/2026.** The chapter's body ("in June 2026") is safe; the anchor is not. The 2 June date derives from a Reuters URL slug this audit could not open. **Fix at A6-fix-2.**

**7. Chapter 4, the FCA anchor itself.** Related to 6 but a separate decision: the `[VERIFY]` asking for the FCA's own release is now **dischargeable** — I opened both the press release and the underlying letter to clubs. The FCA primary supports the chapter's "could expose them to liability" clause **better** than Reuters did, in the FCA's own words and with the statutory basis (ss.19 and 21 FSMA) attached. **Decision: promote the FCA release to top-line primary, retire Reuters, clear the `[VERIFY]`, and update the corpus file's outstanding to-do.**

## C2. The "Ledger Studio" question — the sibling audit's recommendation should not be actioned as written

The sibling audit recommended cutting the limb as **unsourced**, on the ground that it is absent from ledger.com, the X Games page and search. Two of those three are right. **It is on ledger.com**, in Ledger's own voice, in the Spurs announcement: *"Through Ledger Academy, Ledger Studio, and our cultural work…"*. Cutting it would delete a true statement.

What fails is the characterisation, in both chapters that carry it. No source says Ledger Studio is a unit, is in-house, is a content operation, or has anything to do with the sponsorship work — and `ledger.com/ledger-studio` and `ledger.com/studio` both 404. **Decision: narrow rather than cut, in Chapter 4 (A3-fix-2) and in Chapter 6, where "self-declared in-house content unit" is the furthest overreach of the three.**

## C3. Two systemic observations for the audit as a whole

**The anchor block is where the errors live.** In Chapter 4, every defect I found sits in the citation-anchor block or in a descriptive clause attached to a citation — never in the argument. The panel arithmetic, the Gupta quotations, the campaign facts and the four standing corrections are all clean. The BaFin URL, the FCA date, the methodology §-references and the Kraken title corroboration are all anchor-block errors. That suggests the anchor blocks were assembled from corpus-file headers rather than re-derived from the fetched documents, and it argues for a mechanical pass that re-opens every anchor URL and greps it for the sentence it is cited against — which is exactly the gap the sponsorship-reset file's own §5 post-mortem identified: *"every guard the repo has checks whether a citation exists — none checks whether it says what the row claims."*

**Chapter 7's failure mode is compression, not invention.** Every one of its four contradictions is a shortened sentence that dropped a scoping clause: "the corpus captured", "of the seven tracked rows", "by the API scan", "less four `n/a` strings and three column-bleed rows". None invents a fact. All four make the report say something broader than its own evidence. Chapter 7's preamble already states the rule that catches all four — *"Where a limit was attached upstream it is repeated here rather than dropped"* — so the fix is enforcement, not new policy. **Recommendation: after Chapters 1–6 are finalised, re-read Chapter 7 sentence-by-sentence against its cited chapter with the specific question "what qualifier did this sentence drop?", not the general question "is this true?".**

## C4. Items to carry forward, not fixed here

- `tracked-firms.md` still carries the KuCoin three-agency and HTX/NinjaPromo annotations that Chapter 4 correctly refuses to print. They are not printed, but they remain in a file the report ships alongside. **Recommend striking them or dating them as pre-panel.**
- `sport-sponsorship-reset-2026-05.md` §Synthesis still asserts the MarketAcross retainer claim, and its closing "Public-record verifiability" section is stale by one incident against its own header. **Recommend both be reconciled.**
- `fca-premier-league-sponsorship-warning-2026-06.md` closes with a to-do that this audit has now completed.
- Chapter 2's "Four seats, one month" header versus its body's "three of the eleven" — flagged to the Chapter 2 audit; Chapter 7 inherits the four into its anchor block while its body says three.
- The 25-vs-26 adjudicable denominator on the layoff tracker (corpus README) versus the 26 printed in Chapters 3, 6 and 7 — upstream question, flagged not adjudicated here.

---

*Audit complete. Chapter 4's argument survives its own arithmetic without a single figure moving. Its defects are four citation anchors and one imported descriptor. Chapter 7 introduces no new evidence and no new errors of fact — only four sentences that say more than the chapters they cite, and one superlative with no anchor at all. Nine fixes, all of them narrowings, and none of them costs the report a finding.*
