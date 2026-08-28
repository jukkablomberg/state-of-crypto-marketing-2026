# Every stored ESMA register, inventoried by field — and the passporting column that measures the promotional surface

**Class:** 3 (regulator filings). **Captured:** 2026-08-28 (day 58 post-deadline).
**Network used: none.** Every figure below is derived from snapshots already in this repo.
**Closes:** watch **(af)** — *"a verified capture is not a read"*, opened 2026-08-27, whose remedy was *"before ship, inventory every stored register snapshot by FIELD, not by file."*

---

## Method

Four stored ESMA register snapshots were parsed with `csv.DictReader` and every column profiled for **population rate, distinct-value count, and modal values**. No column was skipped because it looked uninteresting. Byte counts and md5s recorded so the reads are reproducible byte-for-byte.

| Snapshot | Data rows | Bytes | md5 | Columns |
|---|---:|---:|---|---:|
| `_esma-casps-snapshot-2026-08-17.csv` | **329** | 161,380 | `69e7dc926b123bac8cb930ab2614ccf6` | 16 |
| `_esma-ncasp-snapshot-2026-08-16.csv` | **167** | 24,614 | `31bffda0e62c3f0f33ea24bcc7aeea4b` | 12 |
| `_esma-emtwp-snapshot-2026-08-21.csv` | **42** | 15,305 | `10d30624347d0838503d5395490d23e1` | 19 |
| `_esma-artzz-snapshot-2026-08-21.csv` | **0** | 273 | `63043ec3c1a6f85a61fdc62dbb557d24` | 16 |

The CASPS md5 and row count **reproduce the 08-17 and 08-27 records exactly**, re-verifying that capture a third time as a side effect. The ARTZZ header-only result **reproduces the 08-21 finding** (zero asset-referenced-token white papers EU-wide) and is not restated as new.

---

## 1. ⭐⭐ 🟢 THE HEADLINE — `ac_serviceCode_cou` IS A REGULATOR-PUBLISHED MEASUREMENT OF EVERY AUTHORISED FIRM'S LAWFUL PROMOTIONAL REACH, AND IT IS SHARPLY BIMODAL

`ac_serviceCode_cou` lists the member states into which each authorised CASP may provide its services — the passporting field. It is populated in **324 of 329 rows (98.5%)** and had been read for exactly one thing before today: *"3 blank `ac_serviceCode_cou`"* in the 08-17 record's defect list.

**Read as a distribution, it is the cleanest Theme-4 instrument in the corpus.** A firm's passport set is the regulator's own statement of how many national markets its marketing may lawfully address.

| States authorised | Rows | Share of 324 |
|---|---:|---:|
| **1 (single-market only)** | **124** | **38.3%** |
| 2–9 | 37 | 11.4% |
| 10–25 | 14 | 4.3% |
| 26–28 | 17 | 5.2% |
| **29–30 (effectively EEA-wide)** | **132** | **40.7%** |

**Median 10. Mean 15.0. And the mean describes nobody** — only 68 of 324 firms (21.0%) sit anywhere between 2 and 28 states. The register is two populations wearing one licence name.

> 🟢 **PERMITTED, and it is the sentence Theme 4 has been missing:** *MiCA authorisation is not one status. Of the 324 authorised crypto-asset service providers carrying a passport list in ESMA's register as at 17 August 2026, **38.3% may operate in exactly one member state and 40.7% may operate in twenty-nine or thirty**. The median firm reaches ten markets; almost nobody actually reaches ten.*
> 🔴 **PROHIBITED:** printing the mean (15.0) as a typical figure, or any sentence of the form "the average authorised CASP markets into fifteen countries." **The distribution is bimodal and the mean falls in its empty middle.**

---

## 2. ⭐ 🟢 EVERY TRACKED-COHORT EXCHANGE SITS IN THE TOP MODE — WITH TWO INSTRUCTIVE EXCEPTIONS

The thirteen register entities matched to tracked firms in the 08-17 cross-match, read on this column for the first time:

| Tracked firm | Register entity | HMS | States |
|---|---|---|---:|
| Coinbase | Coinbase Luxembourg S.A. | LU | **30** |
| Kraken | Payward **Europe** Solutions Limited | IE | **30** |
| Bitstamp | Bitstamp Europe S.A. | LU | **30** |
| Bitpanda | Bitpanda GmbH | AT | **30** |
| Bitpanda | Bitpanda Asset Management GmbH | DE | **30** |
| OKX | OKX Europe Limited | MT | 29 |
| Bybit | Bybit EU GmbH | AT | 29 |
| KuCoin | KuCoin EU Exchange GmbH | AT | 29 |
| Crypto.com | Foris DAX MT Limited | MT | 29 |
| Gemini | Gemini Intergalactic EU Ltd | MT | 29 |
| *(ambiguous — Aave)* | Push Virtual Assets Ireland Limited | IE | 29 |
| Relai | RELAI EU SASU | FR | 26 |
| **Kraken** | **Payward Global Solutions Limited** | IE | **2 — CY, IE only** |
| **Bitpanda** | **BP23 CA Limited** | MT | **blank** |

**Eleven of thirteen are at 26–30.** The cohort this report tracks is, on the regulator's own measure, drawn almost entirely from the top mode: **the firms the report studies are the ones whose promotional surface is continental by construction.** That is a scope disclosure the report owes its reader, not just a finding.

**The two exceptions are worth naming precisely, because both are second entities of firms already at 30:**

- **Payward Global Solutions Limited** (Kraken) carries **CY | IE** while **Payward Europe Solutions Limited** carries all thirty. Two Irish entities, same day of authorisation (25/06/2025), radically different passport sets.
- **BP23 CA Limited** (Bitpanda, MFSA) has a **blank** `ac_serviceCode_cou` — one of only **five blanks in 329 rows**, alongside UAB Micar assets and UAB BLUE EMI LT (both Bank of Lithuania), Orcabay finančne storitve d.o.o. (ATVP/SI) and Safello AB (FI/SE).

> 🔴 **PROHIBITED:** reading either exception as a narrower licence *for the firm*. **Both firms hold a thirty-state passport through another entity in the same register.** A per-entity number is not a per-firm number, and this column cannot be aggregated to firm level without double-counting. **Report entity names, not firm names, whenever this column is quoted.**
> 🔴 **PROHIBITED:** treating a blank as a zero. Five blanks are a completeness defect in the register, not five firms confined to no market.

---

## 3. ⭐⭐ 🔴 THE COMPLEMENT TO THE VOLKSBANK FINDING — THE POST-DEADLINE ENTRANT IS ALSO A SINGLE-MARKET FIRM, AND EVERY GERMAN ONE IS

Yesterday's record established that of 328 dated authorisations, **35 (10.7%) were notified on or after 1 July 2026**, that **14 are German and 12 of those 14 are cooperative or regional retail banks**, and that **none is a tracked-cohort firm**. Cross-tabulating that same cohort against the passporting column completes it:

| Cohort | n | Single-state | Share |
|---|---:|---:|---:|
| **Pre-deadline** (notified before 2026-07-01) | 293 | 100 | **34.1%** |
| **Post-deadline** (notified 2026-07-01 or later) | **35** | **23** | **65.7%** |
| — of which **German** | **14** | **14** | **100%** |

**All fourteen German post-deadline entrants are authorised for Germany alone.** Not one took a passport. The non-German post-deadline group is mixed (nine at one state, five at thirty, three at twenty-six, two at twenty-nine, one each at three and fourteen).

> 🟢 **PERMITTED — the strongest Theme-4 passage this corpus has produced, and it now has both halves:** *In the fifty-eight days after MiCA's transitional period ended, thirty-five firms entered ESMA's authorised-CASP register. Fourteen were German, twelve of those fourteen were cooperative or regional retail banks — and **every one of the fourteen took a domestic-only authorisation**. Two-thirds of all post-deadline entrants may operate in a single member state, against one-third of the firms authorised before the deadline. **The post-deadline entrant to European crypto services is not a crypto-native firm building a European marketing function. It is a Volksbank adding a product line for its own customers.***
> ⚠ **The honest limit, which must ship attached:** this compares a 35-row window against a 293-row back-catalogue accumulated over years. A firm may passport later; the register records status at capture, not intent. **Nothing here says the post-deadline cohort will stay domestic.**
> 🔴 **Scope, unchanged from 08-27:** the rate and this cross-tab are both **as at the 08-17 capture**. The +6 rows observed on 08-25 remain unread and no figure covering them may be printed.

---

## 4. 🔴 A DEFECT IN ESMA'S OWN REGISTER — GREECE IS CODED TWICE, AND NINE ROWS LIST IT TWICE

`ac_serviceCode_cou` uses **both `EL` and `GR` for Greece**, inconsistently and within the same column:

- **71 rows** carry `EL`; **94 rows** carry `GR`; **9 rows carry both.**
- **All nine of those rows are the register's only "31-state" rows.** With Greece de-duplicated, the maximum passport breadth in the file is **30**, as it should be — there are thirty EEA states.

**A naive count of this column over-states nine firms' reach by one and invents a 31st member state.** Every figure in §§1–3 above is computed on the **normalised** set (`EL` folded into `GR`).

> 🟢 **PERMITTED:** *ESMA's CASP register codes Greece as both "EL" and "GR", and nine rows carry both codes in the same cell.* Verifiable in ninety seconds from the published register by anyone who disagrees.
> 🔴 **PROHIBITED:** characterising this as an error of substance, or suggesting any firm's authorisation is affected. **It is a coding inconsistency in a published dataset**, of exactly the kind this report says the regulator-readable appendix exists to surface. `EL` is the EU's own statistical code for Greece and `GR` is the ISO code; both are defensible in isolation, and mixing them in one column is what creates the artifact.

---

## 5. ⭐ 🔴 THE REGISTER HAS A FIELD FOR THE PROMOTIONAL ESTATE, AND IT IS EMPTY IN 99.4% OF ROWS

`ae_website_platform` is the CASPS register's field for the **trading-platform estate** — the consumer-facing surface, distinct from the corporate site in `ae_website`. This is the one column in the entire register that is *about* the promotional surface. Reading it:

| | Rows |
|---|---:|
| `ae_website_platform` populated | 47 / 329 (14.3%) |
| — literal string `n/a` | 4 |
| — known column-bleed rows (address fragments displacing the URL; identified 08-17) | 3 |
| **net real values** | **40** |
| **— where the platform URL actually differs from `ae_website`** | **2** |

The two are `BLOCKCHAIN PROCESS SECURITY (B.P.S)` — `feel-mining.com` → `wigl.fr` — and `Myntkaup ehf.` — `myntkaup.is` → `app.myntkaup.is`. **In the other 38 the firm supplied its corporate URL twice.**

> 🟢 **PERMITTED, and it is a Theme-4 sentence about regulatory visibility rather than about any firm:** *ESMA's authorised-CASP register contains a dedicated field for the trading-platform estate. Of 329 authorised firms, **two** use it to record a surface distinct from their corporate website. **The register that MiCA's marketing-communications obligations attach to cannot, from its own fields, see where those communications are published.***
> 🔴 **PROHIBITED:** treating a blank or duplicated `ae_website_platform` as non-compliance by any firm. **The field's completion rules are not published in the file**, no firm is named against this finding, and 3 of the 47 populated values are a parsing artifact this corpus documented itself.
> ⚠ **This is the class-3 mirror of the class-1 absence-panel rule.** An empty column measures the instrument, not the subject. It is admissible as a statement about the register and inadmissible as a statement about any entity in it.

---

## 6. 🔴 THE SAME COLUMN NAME MEANS DIFFERENT THINGS IN DIFFERENT REGISTERS — DO NOT POOL THEM

`ac_authorisationNotificationDate` appears in **three** of the four registers. It is not the same variable.

| Register | Population | Modal values | What it dates |
|---|---:|---|---|
| **CASPS** | 328/329 (99.7%) | 30/06/2026 (13), 29/06/2026 (11) | the **MiCA CASP** authorisation — clustered on the transitional deadline |
| **EMTWP** | 39/42 (92.9%) | **23/11/2022** (4), **26/04/2017** (3) | the underlying **e-money / credit institution** authorisation — years before MiCA existed |
| ARTZZ | — | — | zero rows |

EMTWP's `ae_authorisation_other_emt` confirms the reading: **29 of 42 rows read "Electronic money institution"** (plus 9 with variant capitalisation) and 2 "Credit institution". These are e-money licences pre-dating MiCA, surfaced in a MiCA register.

> 🔴 **PROHIBITED — a pooled authorisation-date series across registers.** Any chart of "MiCA authorisations over time" that includes EMTWP rows would place MiCA authorisations in **2017**. The 08-27 post-deadline rate is safe precisely because it was computed on CASPS alone; **it must never be recomputed over a union of registers.**
> ⚠ **Also note EMTWP's `ae_exemption48_4` / `ae_exemption48_5` carry `YES`/`NO`/`No` in mixed case** — 34 `No`, 3 `YES`, 1 `NO`. Any filter on these columns must be case-folded.

---

## 7. The NCASP register cannot express a reason, and this run re-derives that from the columns

Reproducing, from the field inventory rather than from the prior record: `ae_infrigment` is **`No` in 167 of 167 rows** (resolved 08-24 as a statement about *national competent authorities* under Art. 17 of Reg. 1095/2010, **not** about listed entities); `ae_reason` is **`None` in 166 of 167**; `ae_comments` is populated in **1 of 167**; `ae_lei` is **empty in 167 of 167**.

The single populated `ae_reason` and the single populated `ae_comments` are the same row — **MEXC Global**, AFM/Netherlands — already held.

**Nothing here is new. It is recorded because the field inventory reproduces it independently**, which is the point of the exercise: the 08-16, 08-20, 08-23 and 08-24 NCASP findings all survive a column-by-column re-read, and the standing limit stands unchanged — **a register in which 166 of 167 rows carry no reason could not express a marketing-communications action even if one existed.**

---

## Explicit non-claims

1. **No claim about any register's state after its capture date.** CASPS is as at 2026-08-17; NCASP 2026-08-16; EMTWP and ARTZZ 2026-08-21.
2. **No firm-level passport figure.** §2 reports entities. Firms with multiple entities are not aggregated.
3. **No compliance judgement about any named entity** from a blank, duplicated or mis-cased field.
4. **No claim that the post-deadline cohort will remain single-market.** §3's limit paragraph is binding.
5. **No pooled statistic across registers.** §6.
6. **No re-fetch was performed and none is claimed.** `CASPS.csv`, `OTHER.csv`, `NCASP.csv` and MAS were not touched; the standing prohibitions hold. Every figure comes from bytes already on disk, with md5s printed above.
7. **The 08-25 +6 CASPS rows remain unread.** No figure in this file covers them.
8. **`ac_authorisationEndDate`** is populated in 2 of 329 CASPS rows — already recorded 08-27, not restated or extended here.
