# ESMA interim MiCA register, file 1/5 — `OTHER.csv` (crypto-asset white papers) — PARTIAL CAPTURE

**Class:** 3 (regulator filings). **Captured:** 2026-08-20. **Status: ⚠ PARTIAL — the capture is TRUNCATED and is recorded as such.**

- **Source URL (read from ESMA's own page, not constructed):** `https://www.esma.europa.eu/sites/default/files/2024-12/OTHER.csv`
- **Provenance of the URL:** `https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica`, fetched first-party this run (HTTP 200, full body). The page lists all five interim-register files by name and link. **No URL was pattern-guessed.**
- **ESMA's own stated register update date on that page: 18 August 2026.**
- **Retrieval result:** HTTP 200, `text/csv`, **64,556 characters / 241 physical lines**, **final row cut mid-field.**

---

## 1. The capture is truncated, and the 08-17 truncation rule did not catch it

The final physical line ends mid-URL inside a Central Bank of Ireland record and carries **no trailing `wp_comments` / `wp_lastupdate` fields**. The two rows above it terminate normally. The body is a clean prefix of the file, cut inside a record.

**This is the second consecutive large-register capture this repo has taken that was silently incomplete** (08-17: `CASPS.csv`, 49% missing, cut mid-field inside a French entity's address).

🔴 **And it falsifies one of the rules 08-17 wrote in response to the first one.** Watch (pp) rule 1 said: *"any `web_fetch` result near ~82,000 characters is presumed truncated."*

| Capture | Chars | Actually |
|---|---|---|
| `CASPS.csv`, 08-17 | 82,445 | truncated |
| `NCASP.csv`, 08-16 and again today | 24,614 | **complete** |
| `OTHER.csv`, 08-20 | **64,556** | **truncated** |

**A byte threshold cannot discriminate.** The cut point is a property of the retrieval channel's budget on the day, not of the file. **Rule 1 is RETIRED as a predicate and kept only as a printed note.**

✅ **Rule 3 — "does the final row terminate cleanly" — caught both.** It is now the primary predicate in `scripts/verify-capture.py`, built this run, with a two-way discrimination test at both historical cut points (see the run record).

## 2. What the capture does and does not cover

The file is ordered by competent authority, grouped by home Member State roughly alphabetically. The capture runs from **AT (Austrian FMA)** through **IE (Central Bank of Ireland)** and stops inside the CBI block.

**Present in the captured portion:** AT · CY · CZ · DE · DK · EE · ES · FI · FR · HR · IE.
**Absent because the capture ends before them — NOT because they hold no records:** IT · LT · LU · LV · MT · NL · PL · PT · RO · SE · SI · SK, and any authority after the CBI block.

⛔ **BINDING ON PHASE 2: no claim of the form "firm X does not appear in the EU white-paper register" may be made from this file.** The two member states most likely to matter for the cohort — **Malta and the Netherlands** — are entirely outside the capture. Positive hits inside the captured portion are usable; absences are not.

## 3. 🔴 THE HEADLINE THE CAPTURE *DOES* SUPPORT: THE EU'S WHITE-PAPER REGISTER IS DOMINATED BY ONE GERMAN COMPANY FILING FOR TOKENS IT DOES NOT ISSUE

**`Crypto Risk Metrics GmbH` (LEI `39120077M9TG0O1FE242`, DE, BaFin) appears on 127 rows of the ~230 records in the captured portion — roughly 55%.**

Counted by exact string match on the full company name; the LEI is constant across all 127, so this is one legal entity, not a name collision.

The tokens it has filed white papers for, read from its own `wp_url` values, include:

> Bitcoin · Ethereum · Litecoin · Ethereum Classic · Dogecoin · Cardano · Ripple (XRP) · Solana · **Sui** · **Uniswap** · **Aptos** · **Arbitrum** · **Avalanche** · **Algorand** · **Polygon (POL)** · **Cronos** · **Binance Coin** · Polkadot · Cosmos · Tezos · Stellar · Bitcoin Cash · Toncoin · Chainlink · Compound · Celestia · Filecoin · Dash · Injective · Basic Attention Token · 0x · Rocket Pool · Osmosis · Axelar · Helium · The Graph · Ondo · Pendle · Raydium · Jupiter · Shiba Inu · Pepe · Floki · dogwifhat · Fartcoin · Pudgy Penguins · Official TRUMP · Melania Meme · Goatseus Maximus · Peanut the Squirrel · Moo Deng · Book of Meme · …

**Why this matters to this report rather than to a MiCA lawyer.** Under MiCA, the white paper is the disclosure document that **marketing communications must be consistent with** (Title II). It is the anchor object of the entire promotional-compliance stack the report's Theme 1 is about. **In the captured half of the EU's register of that anchor object, the majority filer is a third-party German intermediary, and the tokens it has filed for include seven of the cohort's tracked Stratum-2 foundations.**

Bolded above: **Sui, Uniswap, Aptos, Arbitrum, Avalanche, Algorand, Polygon** — plus **Cronos**, the chain of tracked Stratum-1 firm Crypto.com. **None of these filings is in the foundation's own name.**

⚠ **The inference to avoid.** This does **not** establish that the foundations were uninvolved, unaware, or non-compliant. Article 4 MiCA expressly allows a person other than the issuer to notify a white paper for admission to trading — one row in this very file says so in terms (*"Issuer of ANITA is not identified; Moonlabs, as applicant, is notifying admission to trading on its behalf pursuant to Article 4 of MiCA"*). **The finding is about visibility, not culpability**, and visibility is this report's subject: *the entity whose name is on the EU disclosure record for a tracked foundation's token is, in every cohort case in this capture, not the foundation.*

**This closes a gap left open on 08-17.** That run established **0 of 8 tracked foundations are authorised CASPs** and correctly declined to read it as non-compliance, noting several sit outside the CASP perimeter entirely. Today supplies the other half: **the foundations are also absent from the disclosure register as filers — while their tokens are present in it under a third party's name.** Where the gate stack does not reach, and who is standing in the gap, is a Theme-1 finding.

## 4. The tracked Tier-1 exchanges appear — as the *admitting CASP*, never as the issuer

Twelve rows in the captured portion name a tracked exchange. **Every one of them is in the `ae_lei_name_casp` column** — the CASP seeking admission to trading — **not the `ae_lei_name` issuer column.**

| Tracked firm | Register identity | Rows | Tokens / issuers named |
|---|---|---|---|
| **Kraken** | `Payward Europe Solutions Limited (trading as "Kraken")`, LEI `254900641D8KNHUZYX24`; `Payward Global Solutions LTD/LIMITED`, LEI `9845003D98SCC2851458` | 8 | ABC Labs LLC (×3, AMF) · Risk Labs (CBI) · two CBI rows with issuer `Not Available` · Nexus Sub (BVI) Limited (×2, AMF) |
| **Coinbase** | `Coinbase Luxembourg S.A.`, LEI `984500F14CA4571AAC11` | 2 | Leondra GmbH (BaFin), first notification 06/02/2026 + Modification 26/05/2026 |
| **Bitstamp** | `Bitstamp` (no LEI supplied by the NCA) | 1 | Morpho Association (AMF), first notification 23/04/2026 |
| **Bitpanda** | `Bitpanda GmbH`, LEI `5493007WZ7IFULIL8G21` — **issuer column**, AT/FMA | 1 | `https://www.bitpanda.com/en/legal/vsn-white-paper`, `wp_lastupdate` **11/08/2026** |

**Bitpanda is the exception and it is the interesting one: the only tracked firm in the captured portion that appears as an issuer in its own name**, and its record carries the second-newest `wp_lastupdate` in the whole capture. Consistent with the Stratum-4 expectation recorded in `tracked-firms.md` ("Vienna HQ; deep MiCA readiness signal expected"), now with a dated register row behind it rather than an expectation.

⚠ **Two rows list the issuer as literally `Not Available` with Kraken as the admitting CASP** (CBI, 12/06/2025). A register of disclosure documents in which the discloser is recorded as unavailable is a data-quality observation worth carrying to Theme 4; it is **not** adjudicated here.

## 5. Source data-quality defects observed (logged, not corrected)

1. **Records span multiple physical lines** — unquoted newlines inside `wp_url` and `wp_comments` (rows for DELOREAN TECHNOLOGIES, BILLIONS, CheerBitcoin ×2). Naive line counting overstates the record count; the ~230 figure above is line count minus observed continuations and is stated as approximate for that reason.
2. **Leading tab inside a quoted `ae_DTI_FFG`** — `"\t76QS7QCXB"` (Cardano), `"\tKK12JMBTX"` (gram). Whitespace inside a grouping key, the exact defect that produced the 08-17 "4 authorities" error. Any `GROUP BY` on this file must normalise.
3. **A `ae_DTI_FFG` value reused across two different tokens** — `KK12JMBTX` appears on both `toncoin` (13/01/2026) and `gram` (03/08/2026).
4. **`ae_DTI` separators are inconsistent within one column** — `|`, `;`, `,`, and in one row a stray `>` (`WF9C3FK6M> X5B92NG0R`, axelar).
5. **A future-dated record** — CNMV / DELOREAN TECHNOLOGIES GLOBAL, `wp_lastupdate` **02/12/2026**, over three months after capture.
6. **`wp_url` values that are not URLs** — `N/A` (Heldfor GmbH), `xl1-mica-white-paper.pdf` (a bare filename, CySEC), an empty value with the comment `URL Not yet published` (Deblock SAS).
7. **`ae_lei` free-text** — `N/A`, `Not available`, `7404987 (US Deleware File Number)` [*sic*, ESMA's spelling], `2187906`, `890898372`.
8. **Near-duplicate entity names one letter apart under the same LEI** — `The Horizen Foundation` (24/11/2025) and `The Horizon Foundation` (22/05/2026), both LEI `25490025UDB7IZN7JM76`, differing also in `ae_lei_cou_code` (KY vs NL).
9. **Exact duplicate rows** — VeChain Foundation San Marino S.r.l. (CBI) appears twice, identically, 13/03/2025.
10. **`wp_url` values with trailing whitespace and trailing full stops** that break naive link extraction (`…/layer3-ffg-gcg7s59xf/index.html. `, `…/bitcoin-ffg-v15wlzjmf/index.html.`).
11. **A comment field carrying a forward promise instead of a fact** — 20+ rows read *"note that the publication date for the white paper is DD.MM.2026 at which point this record will be updated with the link."* Several of those dates are months past. **The register records an intention to publish as though it were a publication.**

## 6. Explicit non-claims

- **Not claimed:** any total row count for `OTHER.csv`. The capture is a prefix.
- **Not claimed:** that Crypto Risk Metrics' 55% share holds across the full register. **127 is a floor; the share is computed on the captured portion and is stated as such.**
- **Not claimed:** that any named firm is absent from this register. See §2.
- **Not claimed:** that a third-party Article 4 filing is a deficiency, a breach, or evidence of firm inattention.
- **Not claimed:** that ESMA's "Last update: 18 August 2026" applies file-by-file. It is the page's statement about the register collection.
- **Not fetched, not guessed:** the complete `OTHER.csv` · `ARTZZ.csv` · `EMTWP.csv` · any of the ~230 `wp_url` white-paper documents themselves · Bitpanda's VSN white paper · any Crypto Risk Metrics white paper · Crypto Risk Metrics GmbH's own corporate filings or its relationship (if any) to the foundations it has filed for.

## 7. Work queue this capture creates

1. **Re-fetch `OTHER.csv` complete**, through a channel that does not truncate, and re-run `scripts/verify-capture.py` until it returns `COMPLETE`. Only then may the register be read for absences. **Oldest live item on the not-fetched list from this run.**
2. **`ARTZZ.csv` and `EMTWP.csv`** — the last two unopened register files.
3. **Crypto Risk Metrics GmbH** — establish, from public sources only, what the company is and whether the foundations it files for have any public relationship with it. **This is the single highest-value open question the capture produces**, and it is answerable from public record.
