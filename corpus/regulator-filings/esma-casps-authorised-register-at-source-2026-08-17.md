# The EU's authorisation register, at source: 325 CASPs, 27 authorities — and the authority that files 98.8% of the EU's non-compliance record has authorised 2.8% of its CASPs

**Captured:** 2026-08-17 (day 47 post-deadline)
**Source class:** 3 (regulator filings and registers)
**Capture method:** direct first-party fetch of ESMA's interim MiCA register CSV. Machine-parsed with `csv.DictReader`, not read by eye. No secondary relay. Counts recomputed independently a second time before writing.
**Status:** PRIMARY (`esma.europa.eu`, first-party). A register, not an enforcement action.
**Snapshot committed alongside:** `_esma-casps-snapshot-2026-08-17.csv` (329 data rows, 161,380 bytes, md5 `69e7dc926b123bac8cb930ab2614ccf6`, byte-identical to the fetch, UTF-8 BOM and embedded newlines preserved).
**Companion instrument note:** `_esma-register-fetch-truncation-instrument-2026-08-17.md` — **the first fetch of this file was silently truncated at 49%.** Read that note before trusting any large-file capture in this repo.

---

## What was fetched

| | |
|---|---|
| Instrument | Interim MiCA Register — file **1 of 5**, **"Crypto-asset service providers"** |
| Legal basis | MiCA Articles 63 (authorisation) and 109 (ESMA central register); content supplied by NCAs |
| URL requested | `https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv` |
| Schema document also fetched | `https://www.esma.europa.eu/sites/default/files/2024-12/Description_of_the_fields_in_the_interim_MiCA_register.csv` — ESMA's own field definitions for all five register files. **Net-new to the repo.** It is the reason every field in this note can be named with ESMA's own definition rather than our inference. |
| Rows | **329** data rows / **386** physical lines (57 lines are continuations of newlines embedded inside quoted fields) |
| Distinct CASPs | **325** (see the counting note below — 324 by strict LEI-key, 325 is the true population) |
| Register's own freshness | max `ac_lastupdate` = **10/08/2026** — the register self-reports as **7 days stale** at capture |

**Why this file.** The 08-16 run opened register file 5 of 5 (`NCASP.csv`, non-compliant entities) and produced the day-46 enforcement null. That null had no denominator. **This file is the denominator.** Every Theme-4 claim the report will make about which tracked firms hold a MiCA licence has until now been sourced from the *firms' own marketing*. It is now sourced from the register.

This file was listed under *"Not fetched, not guessed"* in the 08-16 capture note. **It was pulled off that list before any new search was opened, per watch (oo).** That rule has now paid out on two consecutive runs.

---

## 1. 🔴 THE HEADLINE — the EU's enforcement visibility runs *inversely* to its authorisation activity

Both halves are ESMA's own registers, captured at source eight days apart, machine-parsed both times.

| Authority | Authorises (CASPS.csv) | Files non-compliance (NCASP.csv) |
|---|---|---|
| **CONSOB (Italy)** | **9 of 324 — 2.8%** | **165 of 167 — 98.8%** |
| **BaFin (Germany)** | **70 of 324 — 21.6%** | **0 of 167 — 0.0%** |
| AMF (France) | 34 — 10.5% | 0 |
| AFM (Netherlands) | 29 — 9.0% | 1 |
| CySEC (Cyprus) | 25 — 7.7% | 0 |
| MFSA (Malta) | 22 — 6.8% | 0 |
| NBS (Slovakia) | 6 — 1.9% | 1 |
| **Authorities appearing at all** | **27** | **4** |

**Stated as the report can print it:** the EU's consolidated non-compliance record is 98.8% Italian, and Italy has authorised 2.8% of the EU's CASPs. Germany, which has authorised more CASPs than any other member state — nearly a quarter of the entire EU population — appears in the non-compliance register **zero times**. Twenty-seven authorities grant MiCA authorisations; **four** have ever notified a non-compliant entity.

**This is a stronger finding than the null it replaces.** "No EU marketing enforcement has appeared" invites the reply *"give it time."* This does not. It says: the visible enforcement record is not a thin early sample of a maturing regime — **it is one national authority's reporting practice, and it is not the practice of the authority that licenses the most firms.**

⚠ **The honest limit, and it must ship attached.** This is a *notification* asymmetry as much as an *enforcement* asymmetry. The register is fed by NCAs; a zero can mean an authority took no action, or took action and did not notify ESMA, or notifies on a different cadence. **These two files cannot separate those.** The 08-16 limit also still binds: with `ae_infrigment: No` on 167 of 167 NCASP rows and `ae_reason: None` on 166 of 167, the non-compliance register **could not express a marketing-communications action even if one existed.** Neither half of this finding alleges a breach by anyone, and neither half should be printed without the limit sentence.

---

## 2. 🔴 The cohort × register cross-match — authorisation is an exchange-stratum phenomenon and nothing else

All 27 named Stratum 1–4 tracked firms tested against `ae_lei_name`, `ae_commercial_name`, `ae_website`, `ae_website_platform`. Case-insensitive substring, then **every hit manually adjudicated** — this corpus has been burned three times by name-collision false positives (watch (u)).

### GENUINE — 10 tracked firms → 13 register entities

| Tracked firm | Register entity | Commercial name | NCA | HMS | Authorised |
|---|---|---|---|---|---|
| OKX | OKX Europe Limited | OKX | MFSA | MT | 27/01/2025 |
| Bybit | Bybit EU GmbH | Bybit | Austrian FMA | AT | 28/05/2025 |
| KuCoin | KuCoin EU Exchange GmbH | KuCoin EU | Austrian FMA | AT | 27/11/2025 |
| Coinbase | Coinbase Luxembourg S.A. | Coinbase | CSSF | LU | 20/06/2025 |
| Kraken | Payward Global Solutions Limited | Kraken, Kraken Digital Asset Exchange | CBI | IE | 25/06/2025 |
| Kraken | Payward Europe Solutions Limited | Kraken Digital Asset Exchange | CBI | IE | 25/06/2025 |
| Crypto.com | Foris DAX MT Limited | Crypto.com | MFSA | MT | 27/01/2025 |
| Gemini | Gemini Intergalactic EU Ltd | Gemini | MFSA | MT | 21/08/2025 |
| Bitstamp | Bitstamp Europe S.A. | Bitstamp | CSSF | LU | 15/05/2025 |
| Bitpanda | Bitpanda GmbH | Bitpanda | Austrian FMA | AT | 09/04/2025 |
| Bitpanda | Bitpanda Asset Management GmbH | — | BaFin | DE | 24/01/2025 |
| Bitpanda | BP23 CA Limited | Bitpanda | MFSA | MT | 27/01/2025 |
| Relai | RELAI EU SASU | RELAI | AMF | FR | 23/10/2025 |

### By stratum — this is the finding

| Stratum | Authorised | Absent |
|---|---|---|
| **1 — Tier-1 exchanges** (11) | **9 of 11** | **Binance, HTX** |
| **2 — L1 / L2 foundations** (8) | **0 of 8** | Sui, Aptos, Solana, Aave*, Polygon, Optimism, Arbitrum, Avalanche/Ava Labs |
| **3 — Wallet / consumer** (5) | **0 of 5** | MetaMask/ConsenSys, Phantom, Ledger, Trust Wallet, Rabby |
| **4 — CASP-licensed non-exchange** (3 named) | **1 of 3** | Securitize, Tether |

*Aave is the one AMBIGUOUS case — see below.

**MiCA CASP authorisation in this cohort is, with one exception, an exchange phenomenon.** Not one L1/L2 foundation and not one wallet in the tracked panel appears in the EU's authorisation register. Relai — added to the panel on 2026-05-06 specifically because it is MiCA-licensed with a named senior marketing leader — is the only non-exchange hit.

**Read carefully, because the obvious inference is wrong.** Absence here is *not* evidence of non-compliance, and in most of these cases it is not even surprising: a foundation issuing a token or a self-custody wallet provider may fall entirely outside the CASP perimeter, and several are non-EU entities. **What the absence establishes is narrower and more useful: the cohort's two most marketing-active strata operate outside the register that Article 68's marketing-communications obligations attach to.** That is a Theme-1 and Theme-4 observation about *where the regime bites*, not an allegation about anyone.

**Binance and HTX are the two that matter.** Both are Stratum-1 exchanges with EU-facing consumer marketing surfaces, and both return zero across all 16 columns of all 329 rows. For Binance this **corroborates** an existing corpus file (`binance-mica-eu-exit-2026-06.md`) from an independent instrument — the first time that file has had register-level confirmation. For HTX the corpus holds no equivalent explanation, and this is now the sharpest open question in the cohort.

### AMBIGUOUS — 1

**Aave** → `Push Virtual Assets Ireland Limited`, commercial name **`Push  / Aave Push`**, CBI/IE, authorised 12/11/2025, `push.co`, licensed for services `c.` and `d.` only.

The regulator-supplied commercial name **names Aave directly**, which is categorically stronger evidence than a third-party domain coincidence. But the legal name and the `push.co` domain establish no corporate link to the tracked Aave/Avara entity **from this file alone**. **Not admitted as an Aave authorisation.** Recorded as a named open question for one targeted check, not resolved by assertion.

### FALSE POSITIVES — 3, and all three from one substring

Every false positive came from the token `crypto.com`, which is a substring of ordinary domains:

| Register entity | Domain | Why it matched |
|---|---|---|
| PROSEGUR CUSTODIA DE ACTIVOS DIGITALES (CNMV/ES) | `www.prosegurcrypto.com` | Prosegur's own custody brand |
| BASQUE PAY S.L. (CNMV/ES) | `https://fazilcrypto.com/es/` | unrelated Spanish CASP |
| NorthCrypto Oy (FIN-FSA/FI) | `https://www.northcrypto.com/` | unrelated Finnish CASP |

Two further rejected hits from Stratum-2 tokens: `sui` → `Bitcoin Suisse (Europe) AG`, and `sui` inside SwissBorg's LEI `969500PZJWT3TD1SUI59`. **No Sui Foundation presence.**

**Watch (u), fourth distinct mechanism in ten days:** brand collision (08-11), document-reference collision (08-15), clone-domain collision (08-16), and today **dot-bearing-brand-as-substring**. A firm whose brand *is* a domain (`crypto.com`) cannot be swept by substring at all. The alias table (vii) must treat it as a special case.

⚠ **One correction to make elsewhere, not here.** A parallel analysis of this file suggested the 08-16 `HTXcoin-az` clone-domain finding needed correcting because `htx` returns zero in CASPS.csv. **That suggestion is itself a misreading and is rejected.** The 08-16 sweep was explicitly against `NCASP.csv`, where the hit is real. Both statements are true of their own file. **Recorded because it is a live example of how easily a cross-file finding gets mis-attributed — the corpus must always name which register a register-claim came from.**

---

## 3. Register composition — the numbers the report can use

**Services held (distinct CASPs, after normalising ESMA's free-text `ac_serviceCode` to MiCA service letters):**

| Service | CASPs |
|---|---|
| a. custody & administration | 218 |
| j. transfer services | 203 |
| c. exchange for funds | 181 |
| e. execution of orders | 168 |
| d. exchange for other crypto-assets | 149 |
| g. reception & transmission of orders | 94 |
| i. portfolio management | 56 |
| h. advice on crypto-assets | 43 |
| f. placing of crypto-assets | 36 |
| **b. operation of a trading platform** | **21** |

**Only 21 of 325 CASPs hold `b.` — operation of a trading platform — the scarcest permission in the register.** Of the tracked cohort, OKX, Bitstamp and Payward Global Solutions (Kraken) hold it.

**Authorisation timing:** earliest 30/12/2024 (MoonPay Europe B.V., AFM/NL — the register's first day). **289 distinct CASPs authorised before 2026-07-01; 34 on or after.** The post-deadline window is producing authorisations at roughly a tenth of the pre-deadline stock.

**Withdrawals — only 2 in the register's entire history:**
1. **Stratos Europe Ltd** (`Tradu`), CySEC/CY — authorised 14/10/2025, withdrawn **24/04/2026**, no stated reason.
2. **Decubate B.V.**, AFM/NL — authorised 31/07/2025, withdrawn **26/03/2026** — *"Voluntary request to revoke authorisation by the entity"*.

**Neither withdrawal is marketing-related, and both are the only exits from a 325-firm register.** For Theme 4 this is the third independent instrument saying the same thing: the MiCA perimeter is being *populated*, not *policed*.

---

## 4. Source data-quality defects — recorded, none corrected

The snapshot is committed verbatim. Eleven defects were found in ESMA's own file and are logged so that anyone recomputing our numbers hits the same ground:

1. **Duplicate LEI across two different firms** — `984500AB011S3AEF6706` is held by both **APLO SAS** and **FLOWDESK EUROPE SAS** (both AMF). This is why strict LEI-keyed dedup gives 324 and the true population is **325**.
2. **Future-dated authorisation** — Deutsche WertpapierService Bank AG, `ac_authorisationNotificationDate` **28/08/2026**, eleven days after capture, with an *earlier* `ac_lastupdate` (30/07/2026).
3. **`ac_lastupdate` predating authorisation** — AvianLabs Netherlands B.V., 15/04/2024 vs authorisation 02/04/2025.
4. **Column bleed from unquoted commas in `ae_address`** — 3 AMF rows (**RELAI EU SASU**, SOCIETE GENERALE - FORGE, BANQUE DELUBAC ET CIE) carry an address fragment in `ae_website` and the real URL in `ae_website_platform`. **This affects a tracked firm:** Relai's `ae_website` reads `75012 Paris`.
5. **`ae_website` containing page titles rather than URLs** — N26 Bank SE, Commerzbank AG.
6. **Malformed URLs** — **Coinbase: `https.//coinbase.com`**; MINOS GLOBAL: `ttps://minos.global`.
7. **Encoding damage** — literal U+FFFD replacement characters inside Payward Europe's commercial name.
8. **Whitespace inside grouping keys** — leading space on ` Financial Supervision Commission (FSC)`, trailing on `Finansinspektionen `. **These silently split naive `GROUP BY` counts** — and the same defect exists in NCASP.csv, where CONSOB appears under two spellings (164 + 1).
9. **Blank fields** — 1 blank `ae_lei` (BASQUE PAY S.L.), 1 blank authorisation date (KBC Bank NV, NBB/BE), 2 blank `ac_lastupdate`, 3 blank `ac_serviceCode_cou`.
10. **`ac_serviceCode` is free text** — **183 distinct strings for 10 underlying services**, with inconsistent lettering, separators (`|`, `I`, `/`, `,`, newline) and several outright letter errors (a row listing `c.` twice; a row reading `b. operation of a trading platform for crypto-assetse execution of orders`).
11. **Register self-reported staleness** — 7 days, against ESMA's stated weekly cadence. Consistent with the 08-16 observation of a 12-day gap. **Two observations now; still not asserted as a pattern.**

**Why this list is in the corpus rather than in a footnote.** Defect 10 in particular means **no one can compute service-level MiCA statistics from this register without a normalisation step and a disclosure of it.** Our figures in section 3 are normalised; the normalisation is stated; the raw file is committed so the step is auditable. That is the standard this report holds other people's promotional estates to.

---

## What this file does NOT establish

- **Nothing about any tracked firm's compliance.** Presence in the authorisation register is not a finding of compliant marketing. Absence from it is not a finding of non-compliance, and for foundations and self-custody wallets is frequently not even evidence of anything.
- **Nothing about whether the 27-vs-4 asymmetry is enforcement behaviour or notification behaviour.** It cannot separate those.
- **Nothing about the Aave/Push relationship.** One targeted check would settle it; that check was not made.
- **Nothing about the 34 post-deadline authorisations beyond their dates.** No individual case was examined.
- **Nothing about HTX's absence.** Zero rows is what the register says; the corpus holds no explanation and does not supply one.

---

## Theme mapping

- **Theme 4 (MiCA readiness) — spine.** The report now has a register-anchored numerator *and* denominator: 325 authorised CASPs across 27 authorities, 167 non-compliance entries across 4, **inversely distributed**, with zero marketing-communications actions in either. Pairs with `esma-halo-effect-regulatory-status-as-marketing-argument-2025-07.md`: ESMA warned in July 2025 against using regulated status as a marketing argument; thirteen months later 325 firms hold that status and no authority has enforced the warning.
- **Theme 1 (gate-stack visibility).** The regime's marketing obligations attach to the CASP perimeter, and **two entire strata of the cohort — the L1/L2 foundations and the wallets — sit outside it.** Where the gate stack does not reach is as much a Theme-1 finding as where it does.
- **Theme 3 (agency overlap).** Not touched by this file.

---

## Provenance table

| Field | Value |
|---|---|
| Document | Interim MiCA Register — crypto-asset service providers (`CASPS.csv`) |
| Publisher | ESMA (first-party) |
| URL | `https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv` |
| Schema URL | `https://www.esma.europa.eu/sites/default/files/2024-12/Description_of_the_fields_in_the_interim_MiCA_register.csv` |
| Captured | 2026-08-17 |
| Snapshot | `_esma-casps-snapshot-2026-08-17.csv`, 329 rows, 161,380 bytes, md5 `69e7dc926b123bac8cb930ab2614ccf6` |
| Parse method | `csv.DictReader`; all counts computed twice, independently, before writing |
| Register's own freshness | max `ac_lastupdate` 10/08/2026 |
| **Fetch caveat** | **First fetch truncated at 49%. See `_esma-register-fetch-truncation-instrument-2026-08-17.md`.** |
| Not fetched, not guessed | The other three register CSVs (`OTHER` — white papers, `ARTZZ`, `EMTWP`) · the 34 post-deadline authorisation records at NCA level · any corporate filing linking Push Virtual Assets Ireland to Aave/Avara · the Stratos Europe / Decubate withdrawal notices · the AFM MEXC public-warning page · the five post-deadline CONSOB notice bodies · the ESMA 2026-02 statement PDF |
