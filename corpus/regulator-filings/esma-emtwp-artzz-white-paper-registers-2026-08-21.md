# ESMA interim MiCA register — the other two white-paper files opened, and the third refuses to be read

**Source class:** 3 (regulator filings).
**Themes:** Theme 4 (MiCA readiness — exposure surface by firm) · Theme 1 (gate-stack visibility).
**Captured:** 2026-08-21. All three URLs read from ESMA's own MiCA page, fetched first-party this run. **None pattern-guessed.**
**Register page state at capture:** *"Last update: 18 August 2026"* — **unchanged from the 2026-08-20 reading, three days earlier**, against ESMA's own stated weekly republication cadence.
**Mandate:** recommendation 1 (re-fetch `OTHER.csv` complete) and recommendation 2 (work the not-fetched list — `ARTZZ.csv` / `EMTWP.csv` were its two oldest live entries) of `../weekly-runs/2026-08-20-corpus-run.md`.

---

## Why this file exists

Under MiCA, **marketing communications must be consistent with the crypto-asset white paper.** The white paper is the anchor object of the entire promotional-compliance stack this report is about. On 2026-08-20 the corpus opened one of ESMA's three white-paper register files (`OTHER.csv`, Title II) and found the majority filer was a third-party intermediary rather than the token issuers themselves.

That left two of the three unopened — and an obvious objection standing: *maybe the tracked firms appear in the other two.*

**They do not.** This run opened both. One capture verified COMPLETE and permits absence claims. One did not, and the guard refused it.

---

## 1. `EMTWP.csv` — e-money tokens (Title IV). **VERIFIED COMPLETE. Absence claims permitted.**

```
python3 scripts/verify-capture.py corpus/regulator-filings/_esma-emtwp-snapshot-2026-08-21.csv
  bytes: 15305   chars: 15273   md5: 10d30624347d0838503d5395490d23e1
  rows:  header 19 fields / 42 data rows (last row 19 fields)
  CAPTURE HEALTH: COMPLETE   exit 0
```

Snapshot committed at `_esma-emtwp-snapshot-2026-08-21.csv` so every figure below is recomputable.

**Shape:** 42 records · 22 distinct issuing entities · 12 member states (CZ 3 · DE 4 · DK 1 · FI 4 · FR 8 · IS 1 · LT 2 · LU 3 · LV 2 · MT 4 · NL 9 · PL 1) · 12 distinct competent authorities.

### 🔴 THE FINDING: NOT ONE TRACKED FIRM APPEARS AS AN E-MONEY-TOKEN ISSUER.

A whole-record scan for all 32 tracked-cohort identifiers (Stratum 1–4 firms plus their chain and token names) returns **seven hits, and every one of them is a blockchain name inside a deployment field of somebody else's stablecoin.**

| Hit | Where it actually is | Issuer of that record |
|---|---|---|
| Solana ×2 | file path of the white-paper URL | **Société Générale — Forge** |
| Solana, Polygon, Optimism, Arbitrum, Avalanche | `ae_DTI` deployment list, one row | **Bridge Building S.A.** (Luxembourg) |

**Zero hits in `ae_lei_name`. Zero in `ae_commercial_name`. Zero as an issuer of anything.**

The category is held entirely by regulated payment and banking institutions: Circle, Paxos, Société Générale — Forge, Banking Circle, CACEIS, Oddo BHF, AllUnity, Monerium, Quantoz, StablR, Stable mint, Fiat Republic, Bridge Building, SALVUS/Schuman, HEURO, GR8 Pay, Newrails, Blue EMI, Payment Corporation, Eurodollar, AIEU, StaBillon.

**Tether — the cohort's only stablecoin issuer, Stratum 4 — is absent from the EU's e-money-token register entirely.** Because this capture verified COMPLETE, that absence is a claim the methodology permits us to make. It is also unsurprising and independently well-documented; it is recorded here because the corpus can now cite it at source rather than by reputation.

### The structural echo, and it is the point

08-20 found the tracked foundations present in `OTHER.csv` only as **tokens filed for by a third party.** Today finds them present in `EMTWP.csv` only as **chains other people's stablecoins are deployed on.**

> Across both EU white-paper registers the corpus can read, no tracked Stratum 1–4 firm appears as the filer of its own disclosure document — with a single exception, Bitpanda, found on 08-20. In both files the cohort appears only as infrastructure inside someone else's filing.

⚠ **The limits ship attached, and they are not small.**
- Most tracked firms are **exchanges and foundations, not e-money-token issuers.** Absence from an EMT register is largely a statement about what business they are in. **This is a visibility finding about where the cohort does and does not appear in the EU's disclosure record — not a compliance finding, and not a claim that any firm should be in this file.**
- Article 4 MiCA expressly permits a person other than the issuer to notify a white paper. Third-party filing is lawful.
- `ARTZZ.csv` (Title III) is **not** readable at the required standard — see §2. Any "across all three registers" phrasing is therefore **not yet available** and must not be written.

### Twelve source data-quality defects, logged uncorrected

Recorded because the corpus's standing position is that the register's own defects are evidence about the register, and because **08-17's "4 authorities" error came from exactly this class of defect going unlogged.**

1. **The authority name is misspelled in 3 of 9 Dutch rows** — `De Nederlandsche Bank (DNB)` (6) vs **`De Nederlansche Bank (DNB)`** (3).
2. **A second name collision:** `Bank of Lithuania` (1) vs `Bank of Lithuania (LSC)` (1).
   → **A naive `GROUP BY` on this file returns 14 competent authorities. The true count is 12.** Two independent collisions in a 42-row file.
3. **Exact duplicate row** — StablR Ltd, rows 29 and 30, byte-identical. (Same defect class as `OTHER.csv`'s VeChain ×2.)
4. **`wp_url` values that are not URLs** — `EMT_NO_WP` on Eurodollar ApS and StaBillon. A register of white papers whose white-paper field says there is no white paper.
5. **2 of 42 rows carry a blank `wp_lastupdate`** (Eurodollar, Banking Circle).
6. **Multi-line, tab-indented values inside a quoted field** — Bridge Building's `ae_DTI` spans eight physical lines. Same defect that made `OTHER.csv`'s record count un-exact.
7. **Malformed trailing quote** — four ACPR comment fields end `...other MiCA compliant WP""`. Survives the parser silently.
8. **Pre-MiCA dates in a MiCA field** — `ac_authorisationNotificationDate` of **19/05/1979** (CACEIS) and **26/06/2007** (Oddo BHF). These are banking-licence dates.
9. **Authorisation dated after its own white paper** — AllUnity EURAU: authorisation `20/06/2026`, white paper notified `20/06/2025`.
10. **Empty element inside a delimited list** — Monerium `ae_DTI`: `JVM0S87GB||3P9X6K6P2`.
11. **Duplicate element inside a delimited list** — Circle EURC `ae_DTI` contains `FJM594L0V` twice.
12. **Case and vocabulary drift in controlled fields** — `YES`/`Yes`, `NO`/`No`, `N/A`/`n/a`, `Electronic money institution`/`Electronic money Institution`/`Credit institution`/`Credit Institution`.

**Cross-register consequence:** eleven defects were logged in `OTHER.csv` on 08-20 and twelve here. The defects are of the same kinds in both files. **The data-quality problem is a property of the interim register as a whole, not of its largest file.**

---

## 2. `ARTZZ.csv` — asset-referenced tokens (Title III). **CAPTURE REFUSED. NO CLAIM MADE.**

The fetch returned HTTP 200, `Content-Type: text/csv`, **273 bytes: a 16-field header row and nothing else.**

```
python3 scripts/verify-capture.py corpus/regulator-filings/_esma-artzz-snapshot-2026-08-21.csv
  bytes: 273   chars: 273   md5: 63043ec3c1a6f85a61fdc62dbb557d24
  rows:  header 16 fields / 0 data rows
  CAPTURE HEALTH: TRUNCATED   exit 1
  ⚠ CLASS-3 ABSENCE CLAIM REFUSED
```

### 🔴 What this run wanted to write, and did not

*"The EU's register of asset-referenced token issuers is empty. Zero ART issuers exist in ESMA's interim MiCA register as of 18 August 2026."*

That would have been the single most striking sentence the corpus has produced. **It is refused, and the refusal is the more important result.**

**A header with zero data rows is exactly what an empty register looks like AND exactly what a truncation-at-the-header looks like. This capture cannot tell them apart, so it does not get to assert either.**

The circumstantial case for "genuinely empty" is decent — 273 bytes is nowhere near any retrieval budget, the header terminates cleanly with a newline, and the same channel returned a 15KB file whole minutes later. **It is still circumstantial**, and watch (ss), adopted 08-20, says precisely this: *when an item would close an open question or strengthen an existing finding, date it first and read it second.* An empty ART register is the most welcome finding available to Theme 4. That is the reason to distrust it, not the reason to print it.

**Status: UNRESOLVED. Work queue. Needs one hand-verification in a browser** — see the run record's escalation list. **`verify-capture.py` is two days old and has now refused the corpus's most attractive claim on its second outing. That is the instrument working, not failing.**

---

## 3. `OTHER.csv` re-fetch — **THE TRUNCATION IS DETERMINISTIC AND REPRODUCIBLE. THE FILE IS UNREACHABLE THROUGH THIS CHANNEL.**

Recommendation 1 of the 08-20 run, executed. Result:

| | 2026-08-20 | 2026-08-21 |
|---|---|---|
| chars | 64,556 | **64,556** |
| lines | 241 | **241** |
| final row | cut mid-URL, CBI record | **cut mid-URL, same CBI record** |

Line 241 both days terminates inside the same `assets-cms.kraken.com` query string, at `...JGo2MCRsMCRoMA`, missing its closing `..` and two trailing fields.

**Two fetches, three calendar days apart, from a register whose publisher republished it on 18 August — byte-identical cut point.** The truncation is not a transient and re-fetching will not fix it. **Recommendation 1 is now CLOSED as unreachable rather than carried, and it should not be re-attempted.**

The 08-20 record specified the escalation as *"a chunked or ranged retrieval — not a second full attempt."* **That escalation is unavailable to an autonomous run**: the permitted retrieval channel is the only one, and range-header or scripted retrieval is out of scope. **This is a hard block that only Jukka can clear**, and it is escalated as such.

**Consequence, unchanged and restated:** the capture stops inside the **IE** block. **IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK are outside it. Malta and the Netherlands — the two most likely to matter for this cohort — are among them. No absence claim may be derived from `OTHER.csv`.** Positive hits inside the captured portion stand, including the 127-of-~230 Crypto Risk Metrics concentration.

One incidental corroboration: lines 239–241 are three `Payward Global Solutions LTD` (LEI `9845003D98SCC2851458`) records in the admitting-CASP column, consistent with 08-20's Kraken=8 count.

---

## Explicit non-claims

1. **No claim that `ARTZZ.csv` is empty.** The capture is refused.
2. **No claim that any tracked firm is absent from `OTHER.csv`.** That capture is truncated.
3. **No claim that absence from `EMTWP.csv` is a compliance defect.** Most of the cohort are not EMT issuers and have no reason to appear.
4. **No claim about the complete EU white-paper picture.** One of three files is readable at the required standard.
5. **No trend claim from the register page's "Last update" date.** Three observations (08-16, 08-20, 08-21) is not a cadence.
6. **No claim that third-party white-paper filing is improper.** Article 4 MiCA permits it.

## Not reached, not guessed

The complete `OTHER.csv` (**unreachable, escalated**) · `ARTZZ.csv` at a verifiable standard (**refused, escalated**) · `CASPS.csv` at its 18/08 version (deliberately not re-fetched; the 08-17 CONSOB/BaFin inversion is **not restated**) · `NCASP.csv` (not re-read today; the 08-20 null is **not re-advanced**) · any of the ~230 `wp_url` documents · the Description-of-fields CSV · Crypto Risk Metrics GmbH corporate filings. **No URL was fabricated.**

## Sources

- ESMA, *Markets in Crypto-Assets Regulation (MiCA)* — register landing page, all five file links and the "Last update" date read here: https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica
- ESMA interim MiCA register, e-money tokens: https://www.esma.europa.eu/sites/default/files/2024-12/EMTWP.csv
- ESMA interim MiCA register, asset-referenced tokens: https://www.esma.europa.eu/sites/default/files/2024-12/ARTZZ.csv
- ESMA interim MiCA register, other crypto-assets: https://www.esma.europa.eu/sites/default/files/2024-12/OTHER.csv
