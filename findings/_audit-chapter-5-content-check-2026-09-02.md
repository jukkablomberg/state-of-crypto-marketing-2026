# Citation CONTENT audit — Chapter 5 (`04-mica-readiness.md`)

**Run:** 2026-09-02. **Publishes:** 2026-09-15. **Auditor pass:** content check, not provenance check.
**Scope of this audit:** does each source *support the sentence citing it*? The provenance gate already proves every printed URL exists in a corpus record. This pass opened the primaries and compared them, word by word, against the chapter's text.

**Method.** Every register figure was **re-derived from the committed snapshot CSVs with `python3`**, not read from a prior corpus record. Every regulator claim was checked by opening the primary document this run. Where a source could not be opened it is recorded as **NOT OPENED** and nothing is claimed from it.

**Result: 71 claims checked.**

| Verdict | Count |
|---|---:|
| **SUPPORTED** | **61** |
| **PARTIALLY SUPPORTED** | **6** |
| **CONTRADICTED** | **3** |
| **NOT OPENED** | **1** |

*(Two further sources were attempted and could not be opened — the Financial Times original behind claim 71, and the podcast audio behind `[VERIFY]` 6. Nothing is claimed from either. They are not counted as claim rows because the chapter's own text already fences both.)*

**Three contradictions, all in Priority 2, all arithmetic or completeness defects, all fixable with a one-line edit — and not one of them costs the chapter an argument.** Six further items are partially supported: four are derivation or wording repairs, one is a genuine mis-citation (a real quote attached to a URL that does not contain it), and one is an overstatement.

**The chapter's strongest passage — the FCA/HTX material — survives the audit intact and verbatim, including the block quote.** The FCA stay is **unchanged and still running**.

---

## The FCA stay — status as at 2026-09-02

**Checked at the FCA's own site this run.** `https://www.fca.org.uk/news/statements/htx-huobi-legal-proceedings` — fetched HTTP 200, full page text read.

- **Key documents list ends at "Order of Master Marsh dated 24 August 2026."** No document dated after 24 August 2026 is listed.
- Page header: **"Last updated: 26/08/2026"**; `article:modified_time` **2026-08-26T10:34:02+01:00**. No edit since.
- **No settlement, discontinuance, consent order, or hearing notice has been published.**
- The Consent Order PDF was fetched and read in full. Paragraph 1, verbatim: *"The Proceedings are stayed as between the Claimant and the First Defendant from the date of this Order until 8 September 2026 for the parties to try to settle the dispute by alternative dispute resolution or other means (the 'Stay')."*

**Verdict: the stay has NOT lapsed, settled or been extended. The chapter's sentence is correct as written today.**

⚠ **It remains the single most perishable sentence in the report.** The stay expires **8 September 2026 — seven days before publication.** Paragraph 3 of the order: *"Upon termination or expiration of the Stay, if no settlement has been reached the default provisions of the Civil Procedure Rules will apply thereafter."* **Re-check this page on 8 and 14 September.** If a settlement is lodged under paragraph 2, the chapter's sentence becomes false on the day it prints. Suggested pre-print hedge, which is true on every branch and needs no re-check:

> *As this chapter was finalised the proceedings were stayed by consent, as between the FCA and the First Defendant only, until 8 September 2026 for settlement talks. Readers should check the FCA's own case page for what followed.*

---

## The claim table

### PRIORITY 1 — FCA v Huobi Global S.A. & Others

Sources opened this run: FCA statement page (HTTP 200, full text), FCA press release (HTTP 200), **Consent Order of Master Marsh, 24 August 2026 (PDF, HTTP 200, 3 pages, read in full)**.

| # | Claim | What the chapter says | What the source says | Verdict | Action |
|---|---|---|---|---|---|
| 1 | Claim issue date | "claim issued **21 October 2025**" | Order: *"UPON the Claimant issuing a Claim Form on 21 October 2025"*. Statement page: *"On 21 October 2025, the FCA commenced proceedings in the Chancery Division of the High Court"*; *"Claim Form dated 21 October 2025"* | **SUPPORTED** | None |
| 2 | Court | "Chancery Division" | Order header: *"IN THE HIGH COURT OF JUSTICE / BUSINESS AND PROPERTY COURTS OF ENGLAND AND WALES / FINANCIAL SERVICES AND REGULATORY SUB-LIST (ChD)"* | **SUPPORTED** | None |
| 3 | Smart quote | *"This is the first time we've taken enforcement action against a crypto firm illegally marketing their products to UK consumers."* | Press release, verbatim: *"HTX's conduct stands in stark contrast to the majority of firms working to comply with the FCA's regime. **This is the first time we've taken enforcement action against a crypto firm illegally marketing their products to UK consumers.** We'll continue to act against firms who ignore our rules."* | **SUPPORTED** | None — exact match |
| 4 | Smart title | "joint executive director of enforcement and market oversight" | *"Steve Smart, joint executive director of enforcement and market oversight at the FCA, said:"* | **SUPPORTED** | None |
| 5 | Fourth defendant, verbatim block quote | *"(4) PERSONS UNKNOWN (who are the persons currently in control of promotions on behalf of the HTX Exchange on any of the following social media platforms and/or messenger services: X, Facebook, Instagram, Telegram, TikTok, YouTube, Discord, Medium and/or LinkedIn)"* | **Consent Order, verbatim, character for character — including "TikTok, YouTube" unspaced** | **SUPPORTED** | **None. See note below — this one nearly went the other way.** |
| 6 | Nine platforms | "nine named platforms" | X, Facebook, Instagram, Telegram, TikTok, YouTube, Discord, Medium, LinkedIn = **9** | **SUPPORTED** | None |
| 7 | Fifth defendant / 2028 | *"on or before 31 October 2028 … become controllers on behalf of the HTX Exchange of accounts"* on the same nine platforms | Order: *"(5) PERSONS UNKNOWN (who are such additional persons who on or before 31 October 2028 become owner or controller of the HTX Exchange and/or become legal and/or natural person within the meaning of HTX Operators … and/or become controllers on behalf of the HTX Exchange of accounts on any of the following social media platforms …)"* | **SUPPORTED** | The ellipsis is honest but elides two broader limbs. Optional: *"…extends that class forward to whoever, on or before 31 October 2028, becomes an owner or controller of the exchange or a controller of its accounts on the same nine platforms."* |
| 8 | Five defendants, four PERSONS UNKNOWN | "Five defendants are named; four are PERSONS UNKNOWN" | Order names (1) HUOBI GLOBAL S.A. and (2)–(5) PERSONS UNKNOWN | **SUPPORTED** | None |
| 9 | The stay | "By the Consent Order of Master Marsh dated **24 August 2026**, proceedings are stayed **until 8 September 2026**" | Order ¶1, quoted in full above | **SUPPORTED** | None |
| 10 | Stay scope | "scoped 'as between the Claimant and the First Defendant' only; defendants 2–5 … are not party to it" | Order ¶1 is so scoped; ¶5 requires service on D1–D4 and publicising to D5 | **SUPPORTED** | None — this caveat is correct and must stay |
| 11 | FCA reference | "ENF-UB00014/LLR/MS" | Order, service block: *"Ref: ENF-UB00014/LLR/MS"* | **SUPPORTED** | None |

> 🟢 **The near-miss worth recording.** The FCA's **web page** renders the fourth defendant with *"Tik Tok, You Tube"* — spaced. The **sealed order** renders it *"TikTok, YouTube"* — unspaced. The chapter quotes the order and attributes it to the order, so it is exactly right. Had the chapter quoted the page and cited the order, or vice versa, the block quote would have been wrong in a document read by compliance professionals. **Both renderings are on fca.org.uk. Whichever is quoted, cite the one actually quoted.**

### PRIORITY 2 — ESMA register arithmetic

All figures **re-derived from `_esma-casps-snapshot-2026-08-17.csv` (md5 `69e7dc926b123bac8cb930ab2614ccf6`, 329 data rows — md5 confirmed) and `_esma-ncasp-snapshot-2026-08-16.csv` (md5 `31bffda0e62c3f0f33ea24bcc7aeea4b`, 167 data rows — confirmed)**.

| # | Claim | What the chapter says | What the snapshot says | Verdict | Action |
|---|---|---|---|---|---|
| 12 | Capture integrity | 329 rows, md5 `69e7dc926b123bac8cb930ab2614ccf6` | 329 data rows; md5 matches exactly | **SUPPORTED** | None |
| 13 | Dated rows | "328 authorised CASPs carrying a notification date"; one blank, **KBC Bank NV, NBB/Belgium** | 328 dated, 1 blank; the blank row is **KBC Bank NV, National Bank of Belgium (NBB), BE** | **SUPPORTED** | None — naming the blank row is good practice |
| 14 | Post-deadline rate | "**35 — 10.7%** — notified on or after 1 July 2026" | 35 of 328 = **10.6707%** | **SUPPORTED** | None |
| 15 | June peak | "June 2026, at 75 — more than four times May's 18" | June 2026 = **75**; May = **18**; 75/18 = 4.17 | **SUPPORTED** | None |
| 16 | July | "31 in July" | July 2026 = **31** | **SUPPORTED** | None |
| 17 | August | "**4 to 17 August**" | **4 rows fall in August 2026, but one is dated 28/08/2026 — after the capture. Only 3 are dated on or before 17 August.** | 🔴 **CONTRADICTED** | **See Contradiction 1** |
| 18 | Forward-dated row | "Deutsche WertpapierService Bank AG, dated **28/08/2026** … with an earlier `ac_lastupdate`" | Confirmed: notification 28/08/2026, `ac_lastupdate` **30/07/2026** | **SUPPORTED** | None — the disclosure is exemplary |
| 19 | German entrants | "**14 are German**" | 14 of the 35 have `ae_homeMemberState` = DE (all BaFin) | **SUPPORTED** | None |
| 20 | Cooperative banks | "**twelve are cooperative or regional retail banks**" | 12 of the 14 carry eG / Volksbank / Raiffeisenbank / VR-Bank / Spar- und Kreditbank forms. The two that do not: **JT Technologies GmbH** and **Deutsche WertpapierService Bank AG** | **SUPPORTED** | None — the "inference from legal forms" label is correct and should stay |
| 21 | Names "quoted verbatim from `ae_lei_name`" | "Volksbank eG **–** Die Gestalterbank" (en dash) | Register: "Volksbank eG **-** Die Gestalterbank" (hyphen) | ⚠ **PARTIALLY SUPPORTED** | Trivial but the sentence claims verbatim. Restore the hyphen, or drop "verbatim" |
| 22 | German entrants domestic-only | "all fourteen German entrants took a domestic-only authorisation. Not one took a passport." | All 14 have `ac_serviceCode_cou` = exactly `DE` | **SUPPORTED** | None |
| 23 | No tracked firm among the 35 | "**Not one of the 35 is a firm this report tracks**" | Full-text scan of all 16 columns of the 35 rows against every tracked name: zero hits | **SUPPORTED** | None |
| 24 | Post-deadline single-market | "**23 of the 35 (65.7%)**" | 23 of 35 = **65.7143%**. All 35 rows have a populated passport cell | **SUPPORTED** | None |
| 25 | Pre-deadline comparator | "against **34.1% of the 293** pre-deadline firms" | 100 of 293 = **34.1297%** — reproduces as stated. Note 5 of the 293 have blank cells (counted as non-single-market); over the 288 populated it is 34.7% | **SUPPORTED** | Reproduces. Optional one-clause disclosure of the asymmetric denominator (see prose §3) |
| 26 | Passport population | "Populated in 324 of 329 rows" | 324 populated, 5 blank (**UAB Micar assets**, **UAB BLUE EMI LT**, **BP23 CA Limited**, **Orcabay finančne storitve d.o.o.**, **Safello AB**) | **SUPPORTED** | None |
| 27 | The bimodal table | 124 / 38.3% · 37 / 11.4% · 14 / 4.3% · 17 / 5.2% · 132 / 40.7% | Reproduces **exactly** as computed. But one row in the "1" bucket is a parsing artefact — see Contradiction 2 | ⚠ **PARTIALLY SUPPORTED** | **See Contradiction 2** |
| 28 | Median / mean | "Median 10. Mean 15.0 … only 68 of 324 sit between 2 and 28 states" | Median **10**, mean **15.04**, 68 rows in [2,28] | **SUPPORTED** | Becomes mean 15.08 / 69 rows after the repair in Contradiction 2 — both still round to "15.0" and "about 70" |
| 29 | EL/GR defect | "ESMA codes Greece as both `EL` and `GR`, and the nine rows carrying both are the register's only '31-state' rows" | **Exactly 9 rows carry both EL and GR, and all 9 are the only rows with 31 raw codes.** EL appears in 71 rows, GR in 94 | **SUPPORTED** | None — precisely stated |
| 30 | Five blank cells | "five blank passport cells are a register completeness defect, not five firms confined to no market" | 5 blanks, enumerated at #26 | **SUPPORTED** | None |
| 31 | "**Two** source defects govern any recomputation" | Two named: EL/GR, and the five blanks | **There are at least three, and the third changes a printed number.** `Validvent Technology GmbH` (FMA/AT, notified 15/04/2026) has `ac_serviceCode_cou` = `AT I DE I IE I BE I CY I CZ I  GR I IT I NL I PT I ES I LU I HU I RO` — **fourteen member states delimited by the letter "I" instead of the pipe "\|"**. Also `SL` (invalid) in 2 rows and lowercase `Fi` in 2 rows | 🔴 **CONTRADICTED** | **See Contradiction 2** |
| 32 | Cohort mapping | "Ten tracked firms map to thirteen register entities and eleven of the thirteen are authorised for 26–30 member states" | 13 entities located; **11** fall in 26–30. The two that do not: **Payward Global Solutions Limited (2)** and **BP23 CA Limited (blank)** | **SUPPORTED** | None |
| 33 | Tier-1 presence | "Tier-1 exchanges **9 of 11** (Binance and HTX absent)" | 9 Stratum-1 firms hold entries; Binance and HTX hold none | **SUPPORTED** | None |
| 34 | Binance/HTX absence | "**No occurrence of 'HTX' or 'Huobi' in any field of any row**"; Binance likewise | Case-insensitive scan of all 16 columns × 329 rows: **binance 0, htx 0, huobi 0**. Also confirmed **0 hits across all 335 rows of the live register today** | **SUPPORTED** | None |
| 35 | Push / Aave row | "commercial name 'Push / Aave Push', CBI/Ireland, notified 12/11/2025", `push.co` | `ae_commercial_name` = `Push  / Aave Push` (double space), CBI, 12/11/2025, `ae_website` = `push.co`, 29 states | **SUPPORTED** | None — AMBIGUOUS status and the exclusion are correct |
| 36 | `ae_website_platform` counts | "populated in **47 of 329** … four are the literal `n/a`, **three are column-bleed artifacts** … leaving **40 real values, of which 2** differ … the other 38 supplied the corporate URL twice" | 47 populated ✓; 4 literal `n/a` ✓; 40 http-prefixed ✓; 38 duplicates ✓; 2 genuinely distinct surfaces ✓ (**BLOCKCHAIN PROCESS SECURITY (B.P.S.) SAS** `feel-mining.com` → `wigl.fr`; **Myntkaup ehf.** `myntkaup.is` → `app.myntkaup.is`). **But the three excluded rows are not column-bleed.** They are `www.okx.com`, `www.zbx.com`, `www.safello.com` — valid domains lacking an `http` prefix, each identical to its own `ae_website`. The column bleed is in **`ae_website`**, in three *French* rows (`75012 Paris`, `92800 PUTEAUX`, `07160 LE CHEYLARD`) | ⚠ **PARTIALLY SUPPORTED** | **Every number survives. The stated derivation does not. See Correction 3** |
| 37 | NCASP size / Italy | "167 rows … **165 — 98.8% — are Italian, filed by CONSOB**" | 167 rows; 165 `IT`; 165/167 = **98.80%**; 165 filed by CONSOB (164 + 1 whitespace variant of the same string) | **SUPPORTED** | None |
| 38 | Italy's authorisation share | "Italy has authorised **9 of 324 CASPs, 2.8%**" | IT = **9**; 9/324 = **2.78%** | **SUPPORTED** | None |
| 39 | Germany's authorisation share | "Germany, which has authorised more than any other member state (**70 of 324, 21.6%**)" | **Germany = 73**, by every available key: `ae_homeMemberState` = DE → 73; `ae_competentAuthority` = BaFin → 73; `ae_lei_cou_code` = DE → 73. **73/324 = 22.5%** | 🔴 **CONTRADICTED** | **See Contradiction 4** |
| 40 | Germany absent from NCASP | "appears zero times" | DE rows in NCASP: **0** | **SUPPORTED** | None |
| 41 | 27 grant / 3 notify | "Twenty-seven authorities grant MiCA authorisations; **three** — CONSOB, the AFM and the National Bank of Slovakia — have ever notified" | CASPS: **27** distinct authority strings across 26 member states. NCASP: 4 raw strings → **3** authorities (CONSOB ×2 spellings, AFM, NBS) | **SUPPORTED** | None |
| 42 | `ae_reason` | "`None` in **166 of 167** rows" | 166 `None`, 1 populated | **SUPPORTED** | None |
| 43 | MEXC quote | *"provides crypto-asset services in the Netherlands without the required MiCAR license … in breach of section 59 MiCAR."* | Cell reads: *"MEXC Global provides crypto-asset services in the Netherlands without the required MiCAR license. MEXC is in breach of section 59 MiCAR."* AFM/NL, decision date 16/09/2025 | **SUPPORTED** | None — ellipsis faithful |
| 44 | `ae_infrigment` | "`No` on 167 of 167" | 167 of 167 `No` | **SUPPORTED** | None |
| 45 | Scorecard register cells | OKX 27/01/2025 · 29; Payward Europe 25/06/2025 · 30; Payward Global · **2 (CY, IE)**; Coinbase 20/06/2025 · 30 (`https.//coinbase.com`); Bitpanda GmbH 09/04/2025 · 30; Bitpanda AM 24/01/2025 · 30; BP23 blank; Bitstamp 15/05/2025 · 30; Bybit 28/05/2025 · 29; KuCoin 27/11/2025 · 29; Foris DAX 27/01/2025 · 29; Gemini 21/08/2025 · 29; RELAI 23/10/2025 · 26 (`ae_website` = ` 75012 Paris`) | **Every one reproduces**, including both register defects. Payward Global's cell is `CY \| IE` | **SUPPORTED** | Entity names: register says "Payward Europe Solutions **Limited**" / "Payward Global Solutions **Limited**"; chapter abbreviates to "Ltd". Expand for exactness |

### PRIORITY 2b — the live register, for scope-sentence checking only

**Fetched this run:** `https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv` — HTTP 200, 163,370 bytes.

| Quantity | 08-17 snapshot (what the chapter uses) | **Live, 2026-09-02** |
|---|---:|---:|
| Rows | 329 | **335** |
| Dated rows | 328 | 334 |
| Notified on/after 1 July 2026 | 35 (10.7%) | **41 (12.3%)** |
| German post-deadline entrants | 14 | **20** |
| Post-deadline single-market | 23/35 (65.7%) | **28/41 (68.3%)** |
| `ae_website_platform` populated | 47 | **47** |

🟢 **The live file's SHA-256 is `196090fa6fa15162fee56084dd0d0e53…` — byte-identical to the 2026-08-25 capture the chapter records.** The register has not changed since 25 August. The gap the scope sentence describes is **exactly six rows and has been stable for eight days.**

**The six previously-unread rows, now read:**

| Entity | State | Notified | States authorised |
|---|---|---|---:|
| Raiffeisenbank Aidlingen eG | DE | 07/08/2026 | 1 |
| Volksbank Euskirchen eG | DE | 14/08/2026 | 1 |
| Ihre Volksbank eG Neckar Odenwald Main Tauber | DE | 18/08/2026 | 1 |
| VR-Bank Mittelfranken Mitte eG | DE | 18/08/2026 | 1 |
| VR Bank Ried-Überwald eG | DE | 20/08/2026 | 1 |
| Volksbank Backnang eG | DE | 20/08/2026 | 1 |

*(The seventh apparent difference is `BitPay B.V.`, whose notification date was restated 15/07/2026 → 16/07/2026. Net new rows: exactly six, as the chapter states.)*

> **All six are German cooperative banks with domestic-only authorisations. None touches the tracked cohort.** The unread rows do not threaten the chapter's thesis — **they replicate it.** The scope sentence is an honest description of the gap, and the gap points the same way the finding does.

**Verdict on the scope sentence: SUPPORTED and still honest.** See prose §5 for the decision it now invites.

### PRIORITY 3 — the AFM material

| # | Claim | What the chapter says | What the source says | Verdict | Action |
|---|---|---|---|---|---|
| 46 | Baseline date | "AFM baseline study, **21 January 2025**" | afm.nl item, fetched: publication date **21/01/25** | **SUPPORTED** | None |
| 47 | Review date | "AFM thematic review, **16 April 2026**" | afm.nl item, fetched: **16 April 2026** | **SUPPORTED** | None |
| 48 | 33 examined | "33 examined" | *"For the study, the advertisements and cost information of **33 CASPs** were examined."* Report PDF adds scope: *"crypto advertisements published between August and October 2025 and publicly available cost information from 33 CASPs that were granted a MiCAR licence in 2024 or 2025"* | **SUPPORTED** | None |
| 49 | 14 / 19 split | "14 advertising / 19 cost" | *"significant shortcomings in advertising were found at **14 CASPs**, and significant shortcomings in cost information at **19 CASPs**"* | **SUPPORTED** | None |
| 50 | van Beusekom quote | *"the period of leniency has ended"* | Hanzo van Beusekom, verbatim: *"We see that some companies are really doing their best, but at the same time too many CASPs are lagging behind. Now is the time for the sector to take responsibility. **The period of leniency has ended.**"* | **SUPPORTED** | None — exact |
| 51 | Post-review instruments | "supervisory letters and cross-border referrals, and neither is public" | *"The Dutch firms concerned will soon receive a supervisory letter. For the **ten international firms**, we will inform the relevant national regulators of the shortcomings identified."* | **SUPPORTED** | None. The "ten international firms" figure is available if useful |
| 52 | One-click / two-click standard | "The AFM's **testable standard** is that cost policies sit *'one click away from the homepage, or two clicks if using a drop-down menu'*" | **Verbatim in both AFM report PDFs.** 2025: *"One way of ensuring that the information is in a prominent place is to locate it one click away from the homepage, or two clicks if using a drop-down menu."* **2026 (stronger, and the better anchor):** *"The AFM expects clients to be able to access such information from the homepage. This means that the information **must** be available within at least one click away from the homepage, or two clicks if using a drop-down menu."* | **SUPPORTED** | Cite the **2026** report PDF for this quote, not the 2025 one — the 2026 wording is mandatory ("must"), the 2025 wording is a safe harbour ("one way of ensuring"). The chapter's "testable standard" characterisation is right on the 2026 text |
| 53 | "Too generic" ruling | *(not used in Chapter 5)* | 2025 PDF, verbatim: *"The AFM considers the inclusion of a passage such as 'investing/trading in crypto-assets has/involves risks' to be **too generic** to indicate the risks associated with transactions in crypto-assets. According to the AFM, one of the ways in which to comply with the standard would be to make clear what the relevant risk is, for example that you could lose your investment."* | **SUPPORTED (source verified; claim not currently in the chapter)** | Available if wanted. It is the sharpest AFM sentence in either report and bears directly on the chapter's risk-language column |

### PRIORITY 4 — the remaining regulator anchors

| # | Claim | What the chapter says | What the source says | Verdict | Action |
|---|---|---|---|---|---|
| 54 | ESMA transitional statement | "ESMA Public Statement **ESMA75-113276571-1710, 23 June 2026**" | PDF opened. Reference and date confirmed. Title: *"ESMA calls on unauthorised crypto-asset service providers to wind down orderly, while also safeguarding clients' interests, as MiCA transitional period ends"* | **SUPPORTED** | None |
| 55 | "cease marketing" wording | *"cease marketing activities and solicitation"* | Verbatim, in context: *"immediately stop onboarding new EU clients, refrain from opening new client relationships or accounts, and **cease marketing activities and solicitation**."* | **SUPPORTED** | None |
| 56 | BaFin date | "*Risks in Focus 2026*, **28 January 2026**" | Press release opened: 28 January 2026, *"Risks in BaFin's Focus 2026: The risk is increasing that financial stability will be put to the test"* | **SUPPORTED** | None |
| 57 | BaFin finfluencer commitment | *"a random market screening of selected German-speaking finfluencers on … YouTube and Instagram"* | **The quote is real and verbatim — but it is NOT on the URL the chapter cites.** The cited press release mentions finfluencers exactly once (*"Social media and finfluencers in particular are playing a significant role in this trend"*) and contains **no screening commitment**. The commitment is on the report's own consumer chapter, which I opened: *"A random market screening of selected German-speaking finfluencers on the social media channels YouTube and Instagram will be the first step in this process."* | ⚠ **PARTIALLY SUPPORTED — quote correct, citation wrong** | **See Correction 5 (citation defect)** |
| 58 | ESMA finfluencer quote | *"Not in tiny text. Not just hashtags."* | Factsheet PDF opened, verbatim: *"If you're getting money, gifts or perks to promote something, don't hide it – say it loud and clear. **Not in tiny text. Not just hashtags.** Use words such as 'Ad', 'Paid partnership' or 'Sponsored', or use the platform's integrated 'ad' banner."* | **SUPPORTED** | None |
| 59 | Factsheet date | "published **January 2026** (month precision, ESMA's own file path)" | Confirmed. The document's own colophon asserts a **2025** production year (catalogue `EK-01-25-037-EN-N`); ESMA's landing page carries no visible publication date | **SUPPORTED** | The chapter's hedge is exactly right. Optional: add "(the document itself carries a 2025 production year)" so a reader who opens the PDF is not surprised |
| 60 | ESMA halo statement | "**ESMA35-1872330276-2329, 11 July 2025**", DON'T: *"The CASP's regulatory status is used as a promotional tool"* | PDF opened. Reference and date confirmed. DON'T row verbatim: *"The CASP's regulatory status is used as a promotional tool. When engaging in unregulated activities, information provided to the client or potential client, including marketing materials and other documentation, includes a reference to the CASP being authorised/regulated by an NCA."* | **SUPPORTED** | None |
| 61 | The narrowing of that DON'T | "that DON'T is narrower than the headline: status used as a promotional tool **in connection with unregulated activities**, and a failure to distinguish which products the authorisation covers" | Matches the source. The paired DO: *"The regulatory status of the product and/or service is clearly and effectively communicated in all dealings with clients, and at every stage of the sales process."* | **SUPPORTED** | None — this self-correction is the chapter at its best and must survive editing |
| 62 | ESMA sanctioning perimeter | "ESMA's own Sanctions and Enforcement page enumerates **six** entity classes … and **CASPs are not among them**" | Page opened. Six classes: CRAs · Securitisation Repositories · Trade Repositories (EMIR/SFTR) · Tier 2 TC-CCPs · Benchmark Administrators · DRSPs. **CASPs do not appear** | **SUPPORTED** | None |
| 63 | Google EU baseline | "effective **23 April 2025** across all 27 member states"; must *"Be licensed as a Crypto-Asset Service Provider (CASP) under the Markets in Crypto-Assets (MiCA) regulation by a relevant national competent authority"*; *"any national-level restrictions or requirements beyond MiCA"*; certified by Google | Page fetched raw. *"Effective April 23, 2025…"* ✓. Scope list enumerates **27** countries ✓. Both quotes appear **verbatim and in full** ✓. *"Be certified by Google."* ✓ | **SUPPORTED** | None |
| 64 | Art. 143(3) schedule | "Finland until 30 June 2025, Germany until 30 December 2025, France until 30 June 2026" keyed to "Article 143(3) of Regulation (EU) 2023/1114" | *"…recognized during the transitional periods established by each Member State in accordance with **Article 143(3) of Regulation (EU) 2023/1114** (MiCA). Specifically: Finland: Until June 30, 2025. France: Until June 30, 2026. Germany: Until December 30, 2025."* | **SUPPORTED** | None |
| 65 | France execution | "On **1 July 2026** … published the change that day, having announced it fifteen months earlier" | France page: *"(Posted on **July 1, 2026**)"*, and *"This update follows the expiration of France's transitional period outlined in the original … (April 2025) change log."* The EU baseline was *"(Posted March 24, 2025)"* → 15.2 months | **SUPPORTED** | None |
| 66 | EEA extension | "In **August 2026** the rule extended to Iceland, Liechtenstein and Norway, completing the EEA" | Page title: *"Update to Cryptocurrencies and related products policy (**August 2026**)"*; body: *"In August 2026, Google will be updating … in the following European Economic Area (EEA) countries: Iceland, Liechtenstein, and Norway."* Posted 22 July 2026 | **SUPPORTED** | None. Note the page is phrased prospectively ("will be updating"); by 15 September it is past. Fine as written |
| 67 | Remedy | "account suspension with at least seven days' warning" | *"Violations of this policy will not lead to immediate account suspension without prior warning. A warning will be issued, at least 7 days, before any suspension of your account."* | **SUPPORTED** | None |
| 68 | VARA / TON Foundation | "The Open Network Foundation, **24 July 2025**, whose sole stated reason is *'Breaches of the VARA Marketing Regulations'*" | Register opened. Row: **The Open Network Foundation · 2025/07/24 · Regulatory breaches · "Breaches of the VARA Marketing Regulations" · Cease-and-Desist Orders; Financial Penalties; Public Statement** | **SUPPORTED** | None — the quote is exact and the "sole stated reason" characterisation holds |
| 69 | VARA "throughout the window" | "VARA has published named, dated, fined marketing actions **throughout the window**" | The register's **most recent row is 2026/01/13** (Vesta Prime). **Zero rows are dated after the MiCA deadline of 2026-07-01.** No penalty amounts are published | ⚠ **PARTIALLY SUPPORTED** | **See Correction 6 (overstatement)** |
| 70 | CONSOB power and cadence | "art. 36, comma 2-*quaterdecies* TUF … publishes weekly, and across twenty-one weeks issued nothing but site-blocking orders"; "perimeter-scoped by statute" | **NOT RE-OPENED this run.** Rests on `esma-consob-post-deadline-index-sweep-2026-08-05.md`, which records the capture at source, quotes the statutory basis (introduced by *Legge n. 21 del 5 marzo 2024*), and records the perimeter scoping | **NOT OPENED** | Re-open `consob.it/web/area-pubblica/oscuramenti` before print, or attribute to the dated corpus sweep. The corpus record is careful and I found nothing against it — but I did not verify it, and it should not be recorded as verified |
| 71 | AMF forbearance | "the AMF has **deliberately declined to set an aggressive shutdown deadline** … on the record, for a stated consumer-protection reason" | **FT original: NOT OPENED — HTTP 403, "Security Verification".** The Block relay **was** opened (HTTP 200) and confirms verbatim: *"The AMF has also avoided setting an aggressive deadline for unlicensed exchanges to halt operations in an effort to limit such scams"*, attributed to FT reporting, author Timmy Shen, 6 August 2026; official named as **Stéphane Pontoizeau**, executive director, market intermediaries and market infrastructure supervision directorate | ⚠ **PARTIALLY SUPPORTED / underlying primary NOT OPENED** | **See [VERIFY] 7 and prose §6** |

---

# The corrections, in full, with proposed wording

*Items 1, 2 and 4 are the three **CONTRADICTED** rows. Items 3, 5 and 6 are **PARTIALLY SUPPORTED** rows whose numbers survive but whose wording or citation does not.*

**No edits have been made to the chapter. Each item below names the exact sentence and proposes the replacement.**

## Contradiction 1 — "4 to 17 August" is 3

**Sentence, §"The authorisation curve bends the wrong way":**

> The register's largest month is **June 2026, at 75 — more than four times May's 18** — against 31 in July and **4 to 17 August**.

**What the snapshot says.** Four rows carry an August 2026 notification date: `VBU Volksbank im Unterland eG` (03/08), `VR-Bank Erding eG` (04/08), `Volksbank Beilstein-Ilsfeld-Abstatt eG` (06/08) — and `Deutsche WertpapierService Bank AG`, dated **28/08/2026**. **Only three fall on or before the 17 August capture date.** The phrase "4 to 17 August" asserts four rows in a period that contains three.

**Why it matters.** The chapter *already* discloses the forward-dated row two sentences earlier, and tells the careful reader to "read 34" instead of 35. This sentence then quietly counts that same row inside a window it falls outside. It is the one place where the chapter's own scrupulousness about the forward date is not carried through.

**Proposed replacement:**

> The register's largest month is **June 2026, at 75 — more than four times May's 18** — against 31 in July and 3 in the first seventeen days of August (a fourth row carries the forward date noted above).

## Contradiction 2 — there are three source defects, not two, and the third moves a printed number

**Sentence, §"Two populations under one licence name":**

> **Two source defects govern any recomputation:** ESMA codes Greece as **both `EL` and `GR`** … and **five blank passport cells are a register completeness defect** …

**What the snapshot says.** A third defect is present and is not disclosed. `Validvent Technology GmbH` (Austrian FMA, notified 15/04/2026) carries this `ac_serviceCode_cou` cell, verbatim:

```
AT I DE I IE I BE I CY I CZ I  GR I IT I NL I PT I ES I LU I HU I RO
```

**The delimiter is the capital letter "I", not the pipe character.** Split on the pipe, the cell yields a single token, and the firm is counted as **single-market**. The register in fact records it as authorised in **fourteen** member states.

Two further, non-moving defects also exist and are worth one clause: `SL` — not a valid EEA code, almost certainly `SI` — appears in two rows (`AMINA (Austria) AG`, `FIOR Digital GmbH`), and lowercase `Fi` appears in two others (`Decubate B.V.`, `Fiat Republic Netherlands B.V.`). Neither changes any count.

**What changes if the delimiter is repaired:**

| Figure | As printed | Repaired |
|---|---:|---:|
| 1 state (single-market) | 124 / **38.3%** | 123 / **38.0%** |
| 10–25 states | 14 / 4.3% | 15 / **4.6%** |
| Rows between 2 and 28 | 68 | **69** |
| Mean | 15.04 | 15.08 |
| Median | 10 | 10 |
| 29–30 states | 132 / 40.7% | **unchanged** |
| Pre-deadline single-market | 100/293 = **34.1%** | 99/293 = **33.8%** |
| **Post-deadline single-market (23/35 = 65.7%)** | — | **unchanged — Validvent is pre-deadline** |

🟢 **The chapter's headline contrast is not damaged. It is slightly strengthened:** the post-deadline single-market share of 65.7% is untouched, and the pre-deadline comparator it is measured against falls from 34.1% to 33.8%, widening the gap.

**Proposed replacement:**

> **Three source defects govern any recomputation:** ESMA codes Greece as **both `EL` and `GR`**, and the nine rows carrying both are the register's only "31-state" rows, so every figure here uses the normalised set; **five blank passport cells are a register completeness defect, not five firms confined to no market**; and **one row (Validvent Technology GmbH) delimits its fourteen member states with the letter "I" rather than a pipe**, so a naive parse counts it as single-market. Figures below are stated on the unrepaired parse for reproducibility against the published file; repairing that one cell moves the single-market share from 38.3% to 38.0% and the pre-deadline comparator from 34.1% to 33.8%, and changes nothing else.

*(If the editors prefer to print repaired figures instead, the four numbers to change are in the table above, and the 65.7% headline does not move either way.)*

## Correction 3 — the `ae_website_platform` derivation misdescribes which column is corrupted

**Sentence, §"The register cannot see the promotional estate":**

> It is populated in **47 of 329 rows**: four are the literal string `n/a`, **three are column-bleed artifacts this corpus itself documented**, leaving **40 real values, of which 2** record a surface differing from the firm's corporate website.

**What the snapshot says.** Every number is right. The derivation is not.

- The three rows excluded to get from 43 to 40 are `www.okx.com`, `www.zbx.com` and `www.safello.com` — **ordinary valid domains that simply lack an `http` prefix**, each identical to its own `ae_website`. They are duplicates, not artefacts.
- The **column bleed is in `ae_website`, not in `ae_website_platform`**, and it affects three *French* rows whose address text displaced the URL: `RELAI EU SASU` → ` 75012 Paris`, `SOCIETE GENERALE - FORGE` → `92800 PUTEAUX`, `BANQUE DELUBAC ET CIE` → `07160 LE CHEYLARD`. In all three the `ae_website_platform` value is a **clean, valid URL**.
- Those three rows are why a naive text comparison returns **5** differences rather than 2: three of the five "differences" exist only because the *corporate-URL* field is corrupted. Excluding them leaves exactly the **2** genuine cases the chapter names.

**The chapter is internally inconsistent on this point** — its own scorecard correctly locates the bleed in `ae_website` ("Register defect at source: `ae_website` reads ` 75012 Paris` (column bleed)"), two sections after this paragraph puts it in `ae_website_platform`.

**Proposed replacement:**

> It is populated in **47 of 329 rows**: four are the literal string `n/a` and three are bare domains repeating the corporate URL without a scheme, leaving **40 URL-formed values.** Five of those differ textually from the firm's `ae_website` — but in three the *corporate* field is corrupted by a documented column bleed that put a postal address where the URL belongs, so the difference is a register defect rather than a declared platform. **Two rows genuinely record a trading-platform surface distinct from the corporate website.** In the other 38 the firm supplied its corporate URL twice.

The following clause must also change, since it repeats the same error:

> …and **three of the 47 populated values are a parsing artifact this corpus documented itself.**

→ **"…and three of the 47 populated values are bare domains that merely repeat the corporate URL."**

## Contradiction 4 — Germany is 73, not 70

**Sentence, §"The EU enforcement null is a reporting artefact":**

> **Germany, which has authorised more than any other member state (70 of 324, 21.6%), appears zero times.**

**What the snapshot says.** Germany has **73**. This is not a denominator or de-duplication question — it is 73 on every available key:

| Key | Count |
|---|---:|
| `ae_homeMemberState` = `DE` | **73** |
| `ae_competentAuthority` = `Federal Financial Supervisory Authority (BaFin)` | **73** |
| `ae_lei_cou_code` = `DE` | **73** |

73/324 = **22.5%**. (73/329 = 22.2%, so the error is not a 329-vs-324 slip either.) The next largest is France at 35.

**Everything the sentence is doing still works** — Germany is still by a wide margin the largest authoriser, and it still appears zero times in the non-compliance register. Only the number is wrong.

**Proposed replacement:**

> **Germany, which has authorised more than any other member state (73 of 324, 22.5% — more than twice second-placed France), appears zero times.**

⚠ **Check the same figure wherever else it appears in the report.** This number is a cross-chapter fact; if 70 was carried from an earlier draft it may be printed elsewhere.

## Correction 5 — the BaFin finfluencer quote is cited to a page that does not contain it

**Sentence, §"Four columns … cannot fill", item 1:**

> BaFin has committed to *"a random market screening of selected German-speaking finfluencers on … YouTube and Instagram"*

**Citation anchor as printed:** `https://www.bafin.de/SharedDocs/Veroeffentlichungen/EN/Pressemitteilung/2026/pm_2026_01_28_PK_Risiken_im_Fokus_en.html`

**The quote is genuine, exact, and correctly attributed to BaFin.** I opened the report's consumer chapter and found it verbatim: *"BaFin will expand the range of information it provides to consumers on trading in cryptoassets. **A random market screening of selected German-speaking finfluencers on the social media channels YouTube and Instagram will be the first step in this process.** BaFin will also continue to publish warnings about dubious crypto offers."*

**But it is not on the cited page.** The press release the chapter links mentions finfluencers exactly once — *"Social media and finfluencers in particular are playing a significant role in this trend"* — and contains **no screening commitment at all**. A compliance reader who follows the footnote to check the quote will not find it, and will reasonably conclude the quote was fabricated.

**This is precisely the defect class this audit exists to catch: a URL that exists, is correctly dated, is the right regulator and the right document family — and does not support the sentence citing it.**

**Action — no wording change needed, add the chapter URL to the anchor:**

> **BaFin *Risks in Focus 2026*, 28 January 2026** — press release (date and ranking): `https://www.bafin.de/SharedDocs/Veroeffentlichungen/EN/Pressemitteilung/2026/pm_2026_01_28_PK_Risiken_im_Fokus_en.html`; **consumer chapter, source of the finfluencer-screening commitment**: `https://www.bafin.de/EN/die-bafin/publikationen-daten/risiken-im-fokus/Fokusrisiken_2026/RIF_Verbraucher_2/RIF_verbraucher_sozialemedien_en.html`

*(The corpus record `bafin-risks-in-focus-crypto-finfluencer-2026-01.md` carries both URLs correctly and separates them explicitly. The loss happened between the corpus record and the chapter's anchor list, not in the research.)*

## Correction 6 — VARA "throughout the window" overstates a register that stops in January

**Sentence, §"The EU enforcement null", scope-corrections paragraph:**

> It is **EU-scoped**: Dubai's VARA has published named, dated, fined marketing actions **throughout the window**, including The Open Network Foundation, 24 July 2025 …

**What the source says.** The TON Foundation row is exact and the quote is exact. But the register's **most recent entry of any kind is 2026/01/13** (Vesta Prime Portal Co. L.L.C.), and there are **zero rows dated after the MiCA transitional deadline of 1 July 2026.** The sentence sits inside a paragraph whose subject is explicitly the *post-deadline* null ("Sixty-three days after the deadline…"), so "throughout the window" will be read as the post-deadline window — in which VARA published nothing. No fine amounts are published either.

**Proposed replacement:**

> It is **EU-scoped**: Dubai's VARA has published named, dated marketing enforcement actions carrying financial penalties — including The Open Network Foundation, 24 July 2025, whose sole stated reason is "Breaches of the VARA Marketing Regulations". **VARA's own register runs to 13 January 2026 and carries nothing after the MiCA deadline either**, so the contrast is one of regime and instrument, not of a jurisdiction currently outpacing the EU.

---

# `[VERIFY]` tags — all 8, with dispositions

| # | Line | Tag | Disposition |
|---|---:|---|---|
| **1** | 93 | OKX/Ghoos — MiFID II and Payment Institution limbs are the firm's own assertion; only the MFSA CASP authorisation of 27/01/2025 is corroborated by the register | **STILL OPEN — but the chapter already handles it correctly.** The register capture corroborates the CASP limb only, exactly as stated. Trade press (CoinDesk, Feb 2026; Finance Magnates) reports both an EU payments licence and a MiFID II entity acquisition, so the firm's claim is probably true — **but no primary was opened and none is cited.** The chapter attributes the claim to the firm and rules on nothing. **Recommend: keep as written, keep the tag's substance as a printed attribution, and drop the bracket.** Do not upgrade to corroborated on trade-press evidence |
| **2** | 99 | EEA-egress re-read of the campaign teardown | **STILL OPEN — cannot be closed from here.** This requires a fetch originating inside the EEA; this audit's egress is not EEA. **The caveat as drafted is accurate and sufficient to print** ("all fetches originate outside the EEA, and an authenticated EEA visitor may be served a closed state"), and the observation that OKX's geo-layer announced the non-EEA origin and served the campaign anyway is a real, dated finding that stands on its own. **Recommend: if no EEA re-read happens before 15 September, print the caveat and keep the finding narrow. Do not cut** |
| **3** | 109 | Google's standing *Cryptocurrencies and related products* policy was never fetched; may carry risk-warning requirements bearing on the credential/conduct distinction | ✅ **CLEARED.** Fetched this run (`support.google.com/adspolicy/answer/14009787`). The standing policy is **purely advertiser-eligibility and certification** — who may advertise and where. It imposes **no risk warning, no disclaimer, no fair-clear-not-misleading standard, and no accuracy requirement** on ad content. **This confirms the chapter's central distinction rather than complicating it.** Recommend: delete the bracket and, if wanted, strengthen — *"nothing in Google's standing crypto policy tests whether a communication is fair, clear and not misleading either; the gate is on the advertiser, at both layers"* |
| **4** | 142 | Whether the AFM's 33 examined CASPs overlap the tracked cohort | ✅ **CLEARED as unresolvable — and the chapter already states it correctly.** The AFM's 2026 report PDF, footnote 1: *"The examples are inspired by findings from the study and have been aggregated and anonymised."* **The AFM anonymises by design; no overlap can ever be established from this source.** Recommend: replace the bare `[VERIFY]` with the reason — *"the AFM anonymises its examples by design, so the overlap is not merely unknown but unknowable from this source"* |
| **5** | 144 | Chapter 1's "quiet copy" paragraph forward-references an audit sweep that does not exist in this corpus | **STILL OPEN — and it is a Chapter 1 problem, not a Chapter 5 problem.** Out of this audit's scope to resolve, but Chapter 5 is right that the corpus holds no such sweep: no observation in the regulator-filings or campaign captures matches "maximum safety" heroes, three-digit APY promotions, or non-rendering disclaimers across "dozens of firms". **Recommend: escalate to the Chapter 1 editor. Either the sweep runs before ship, or Chapter 1's sentence narrows to the firms actually captured.** Chapter 5's flag is correct and should stay until Chapter 1 moves |
| **6** | 146 | Ferdon quote — third-party machine transcript; check against episode audio | **STILL OPEN — cannot be closed from here** (no audio capability; the *Marketing Vanguard* episode page did not surface in search). The chapter's handling is already conservative: the quote is attributed, dated 9 April 2026, and explicitly fenced as **pre-deadline** with an instruction not to print it as post-deadline. ⚠ **The risk is a machine transcript of a named executive at a tracked firm — the highest-consequence quote type in the report.** **Recommend: if the audio is not checked before 15 September, cut the three quoted fragments and keep the paraphrase.** The paragraph's argument survives without them: *"Coinbase's CMO described, in April 2026, the pull toward caution created by operating under regulatory scrutiny across many jurisdictions at once."* **A cut claim beats a fake anchor, and this is the clearest instance of that rule in the chapter** |
| **7** | 154 | AMF forbearance — verify against the FT original before the quote is printed | **NOT OPENED — FT returned HTTP 403 ("Security Verification"). Recorded as not opened; nothing is claimed from it.** The relay **was** opened and verified: The Block, Timmy Shen, 6 August 2026, HTTP 200, crediting FT reporting, quoting Stéphane Pontoizeau by name and full title. **The chapter prints no direct quote here — only a paraphrase — so the tag's own condition ("before the quote is printed") is satisfied by not printing one.** But the paraphrase still rests on a paywalled primary this report has never seen. **Recommend: keep the paraphrase, make the chain visible in the body, and do not print an FT quote.** Proposed: *"In France the AMF has, on the record, deliberately declined to set an aggressive shutdown deadline for unlicensed exchanges, for a stated consumer-protection reason — reported by the Financial Times and relayed verbatim by The Block; the FT original sits behind a paywall this report did not open."* |
| **8** | 154 | Ferdon quote in the citation-anchor block — duplicate of #6 | **STILL OPEN — resolves with #6.** Whatever is decided for #6 must be applied here too, or the anchor block will carry a tag the body no longer has |

**Summary: 2 CLEARED, 5 STILL OPEN, 1 NOT OPENED. One CUT-RECOMMENDED — #6/#8, the Ferdon quote, if the audio is not checked before 15 September.**

---

# Things that need a decision

## 1. The FCA passage is the strongest thing in the chapter and it survived the audit untouched

Every limb checked. The claim date, the court, the quote, the speaker's title, the defendant structure, the nine platforms, the 2028 long-stop, the stay's dates and its two-party scoping, the case reference — **all verbatim against the FCA's own press release, its court-ordered publication page, and the sealed Consent Order PDF, all three opened this run.**

It is worth recording *why* the block quote survived, because it was the one place a plausible failure was waiting. The FCA publishes the fourth defendant's description in **two different renderings on its own site**: the statement page writes *"Tik Tok, You Tube"*, the sealed order writes *"TikTok, YouTube"*. The chapter quotes the order and attributes the quote to the order. Had it quoted one and cited the other, the report's single most-quoted block quote would have been wrong in a document read by compliance professionals. **The discipline of citing the artifact actually quoted is what saved it. Do not let a copy-edit "normalise" either rendering.**

## 2. Three arithmetic corrections, and none of them costs the chapter an argument

This is the most important thing an editor needs to hear. **All three contradictions are fixable with one-line edits, and not one of them weakens a finding:**

- **Germany 70 → 73** *(Contradiction 4)*: the point was that Germany authorises more than anyone and appears zero times in the non-compliance register. **Both halves survive; 73 makes the first half stronger** (more than twice second-placed France).
- **August 4 → 3** *(Contradiction 1)*: a rounding of the chapter's own disclosed forward-dated row into a window it falls outside. **The June-vs-May shape argument is untouched.**
- **The third source defect** *(Contradiction 2)*: repairing it moves the pre-deadline comparator from 34.1% to **33.8%** and leaves the 65.7% post-deadline figure **exactly where it is**. **The contrast the chapter is built on gets slightly wider.**

**The chapter does not need to retreat anywhere.** That is an unusual audit result and it should be said plainly rather than buried under six correction headings.

## 3. The pre/post denominators are not symmetric, and one clause fixes it

The post-deadline share (23/35) has **no blank passport cells** in its denominator. The pre-deadline share (100/293) has **five**, counted as not-single-market. Over populated rows only, the pre-deadline figure is 34.7% rather than 34.1%.

The direction is conservative — the asymmetry makes the pre-deadline comparator *smaller* and the contrast *larger* — so the chapter is not flattering itself. But a compliance reader recomputing from the CSV will land on a different number and want to know why. **Recommend one clause:** *"(over the 288 pre-deadline rows with a populated passport cell, 34.7%)"*.

## 4. `ae_website_platform`: right answer, wrong reason, and the chapter contradicts itself internally

Worth flagging separately because it is the only place where the chapter's two halves disagree with each other. §"The register cannot see the promotional estate" puts the column bleed in `ae_website_platform`; the scorecard, two sections later, correctly puts it in `ae_website` and names the row (`RELAI EU SASU` → ` 75012 Paris`). **The scorecard is right.** The numbers 47 / 40 / 2 / 38 are all correct and reproduce; only the derivation sentence needs replacing.

**The underlying finding is untouched and remains, in my view, the best single fact in the chapter:** ESMA's register has one field about the promotional surface, and two firms in three hundred and twenty-nine use it to say anything their corporate website does not already say.

## 5. The six unread rows are now readable, and they argue *for* the chapter

The live register today is **byte-identical** to the 2026-08-25 capture (SHA-256 confirmed against the value the chapter prints). The gap has been stable for eight days. **All six net-new rows are German cooperative banks with domestic-only authorisations, and none touches the tracked cohort.**

This turns a standing caution into a choice, and both branches are safe:

- **Branch A — keep the scope sentence as-is.** Costs nothing, remains literally true, and is the position the spine file recommends as the safe default. The chapter's scope discipline is one of its strengths and no reader is misled.
- **Branch B — read the six rows and restate.** Post-deadline 35→41 (10.7%→12.3%), German 14→20, single-market 65.7%→68.3%, and `ae_website_platform` stays at 47. **Every figure moves in the direction the chapter already argues.** The German-cooperative-bank finding goes from 14 of 35 to 20 of 41 and every one of the twenty is still domestic-only.

⚠ **If Branch B is taken it must be taken wholesale.** The chapter's standing caution — *"No figure here may be silently restated against a later register state"* — is correct, and a half-migrated chapter with some figures at 329 rows and some at 335 would be worse than either branch. **My recommendation is Branch A** unless there is time to redo the whole section and re-verify the scorecard against the 335-row file: the chapter ships in thirteen days, the finding does not change, and the scope sentence is honest. **Either way, note in the record that the six rows are no longer unreadable — they were read in this audit and are listed above.**

## 6. Two anchors that are not what they look like

**The BaFin finfluencer citation is the one genuine mis-citation in the chapter** *(Correction 5)*. The quote is real and exact; the URL beside it does not contain it. This is the exact failure mode the provenance gate cannot catch — the URL resolves, the date is right, the regulator is right, the document family is right, and the sentence is not in it. **Fix the anchor, not the quote.**

**The AMF forbearance chain should be visible in the body, not only in the anchor list** *(tag 7)*. The FT is paywalled and returned 403 to this audit; the report has never seen it. The Block relay is solid, named, dated and quotes the official in full — but it is a relay. The chapter's paraphrase is load-bearing: it is the sentence that stops the EU null reading as inattention. **A reader entitled to weigh it should be able to see that the primary is a paywalled FT report the authors did not open.** One clause does it, and the finding survives at full strength.

## 7. Two date-sensitive numbers to re-check on the morning of publication

- **"Sixty-three days after the deadline"** is computed from the 2026-09-02 draft date. On 15 September it is **seventy-six**. Either restate at press or rephrase to something that does not decay (*"Ten weeks after the deadline"*, or scope it: *"As at 2 September 2026, sixty-three days after the deadline…"*).
- **The FCA stay** expires **8 September**, seven days before publication. See the status block at the top. **Re-check `fca.org.uk/news/statements/htx-huobi-legal-proceedings` on 8 and 14 September** — new documents appear in "Key documents" and in `article:modified_time`, and, as this corpus already documented, **not necessarily in the page's visible update log.**

## 8. One thing I did not check, recorded so no one assumes I did

**The campaign and teardown material was not audited in this pass** — the OKX, Kraken, Bitpanda, Bitvavo, Gate and BitMart captures, the timestamps, the offer terms, the surface counts, and the Kraken and OKX quoted copy. That material is class 4/5 own-estate capture and sits outside the five priorities set for this run. **It has not been content-checked and must not be recorded as verified on the strength of this file.**

**The CONSOB claim (row 70) was also not re-opened this run** and rests on a dated corpus sweep. Nothing I found contradicts it; I simply did not verify it.

---

## Audit provenance

**Opened and read this run:** FCA statement page (raw HTML) · FCA press release · **Consent Order of Master Marsh, 24 August 2026 (PDF, full text)** · ESMA CASPS live register CSV · ESMA Public Statement ESMA75-113276571-1710 (PDF) · ESMA Statement ESMA35-1872330276-2329 (PDF) · ESMA *Finfluencers* factsheet (PDF) · ESMA Sanctions and Enforcement page · AFM baseline item + **2025 report PDF** · AFM thematic-review item + **2026 report PDF** · BaFin press release · **BaFin *Risks in Focus 2026* consumer chapter** · Google Ads answers 16089943, 17218519, 17264747, 14009787 (all raw HTML) · VARA enforcement register · The Block, 6 August 2026.

**Attempted and NOT OPENED — nothing claimed from any of them:** Financial Times, `ft.com/content/b0b7db1d-5c9e-42d7-8aed-176e0acd00a9` — **HTTP 403, "Security Verification"** · *Marketing Vanguard* (Adweek) episode audio — **no audio capability; episode page not located** · CONSOB `oscuramenti` register — **not attempted this run**.

**Re-derived with `python3` from the committed snapshots, not read from any prior corpus record:** every figure in Priority 2. Both snapshot md5s were confirmed against the values the chapter prints before any figure was computed.
