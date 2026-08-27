# ESMA CASPS register — the post-deadline authorisation rate, computed at last

**Captured:** 2026-08-27 (day 57 post-deadline)
**Source artifact:** `_esma-casps-snapshot-2026-08-17.csv` — **already held in this repo since 2026-08-17.**
**Capture verdict today:** `verify-capture.py … --expect-rows 329` → **COMPLETE, exit 0.** 161,380 bytes · chars 161,045 · md5 `69e7dc926b123bac8cb930ab2614ccf6` · header 16 fields / 329 data rows / final row 16 fields / no ragged rows.
**Class:** 3 (regulator filings and registers).

---

## 🟢 The recommendation asked for a re-fetch. The data was already on disk.

The 08-25 run closed the oldest queue entry by capturing `CASPS.csv` complete through a changed channel, then recorded that **the notification dates of the new rows were not read, so no post-deadline authorisation rate could be printed.** Recommendation 2 for today was to isolate those dates — framed as another retrieval.

**It was not a retrieval problem.** `ac_authorisationNotificationDate` is one of the register's sixteen fields and it is populated in **328 of 329 rows** of the snapshot this repo has held, verified COMPLETE, since 2026-08-17. The number the report wants was computable on 08-17, on 08-20, on 08-21, on 08-22, on 08-23, on 08-24 and on 08-25. **Nobody parsed the column.**

> ⚠ **Recorded as an instrument finding, not a scolding.** The corpus has spent nine days treating class 3 as a *capture* problem — truncation, channels, byte counts, md5s — because that is where the last two defects were. The register was captured correctly and then read for one thing (presence/absence of named firms) when it carries fifteen other fields. **A verified capture is not a read.**

---

## 🟢 THE NUMBER — permitted, because the capture is verified COMPLETE

> **Of 328 authorised CASPs carrying a notification date in ESMA's register as at 2026-08-17, 35 — 10.7% — were notified on or after 1 July 2026, the day the MiCA transitional period ended.**
>
> **34 of those 35 carry an effective date on or before the capture date.** One is forward-dated — see the defect below. **Print 34 if the sentence must be unarguable; print 35 with the footnote if it must be complete.**

**Denominator note.** 329 rows; one (**KBC Bank NV**) carries no notification date at all, so the rate is stated over the 328 dated rows and the blank is disclosed rather than silently dropped.

---

## ⭐ THE SHAPE MATTERS MORE THAN THE RATE — the surge was BEFORE the deadline, not after

Monthly distribution of `ac_authorisationNotificationDate`, 2026 (from the same 328 dated rows):

| Month | Authorisations notified |
|---|---:|
| 2025-12 | 44 |
| 2026-01 | 8 |
| 2026-02 | 14 |
| 2026-03 | 14 |
| 2026-04 | 12 |
| 2026-05 | 18 |
| **2026-06** | **75** ← the month *before* the deadline |
| 2026-07 | 31 |
| 2026-08 (to the 17th) | 4 |

> 🟢 **PERMITTED:** *The largest single month of MiCA CASP authorisation in the register is June 2026 — the last month of the transitional period — at 75, more than four times the preceding month. Authorisation raced the deadline rather than following it.*

Earliest date in the register: **2024-12-30.** Latest: **2026-08-28** (see defect).

---

## ⭐⭐ WHO ACTUALLY GOT AUTHORISED AFTER THE DEADLINE — and it is not who a crypto-marketing report would guess

The 35 post-deadline authorisations, by competent authority:

| Authority | n |
|---|---:|
| **Federal Financial Supervisory Authority (BaFin)** | **14** |
| Cyprus Securities and Exchange Commission (CySEC) | 4 |
| Autorité des Marchés Financiers (AMF) | 4 |
| Comisión Nacional del Mercado de Valores (CNMV) | 3 |
| Financial Supervision Commission (FSC, BG) | 2 |
| Finanzmarktaufsicht (FMA, LI) | 2 |
| Austrian FMA · NBB · CNB · CSSF · Latvijas Banka · AFM | 1 each |

Member states: DE 14 · CY 4 · FR 4 · ES 3 · BG 2 · LI 2 · AT/BE/CZ/LU/LV/NL 1 each. **Twelve member states out of thirty.**

**And inside BaFin's fourteen, twelve are German cooperative or regional retail banks:**

Donau-Iller-Bank eG · Volksbank Schwarzwald-Donau-Neckar eG · Spar- und Kreditbank Rheinstetten eG · VR-Bank Augsburg-Ostallgäu eG · Raiffeisenbank Falkenstein-Wörth · Volksbank Raiffeisenbank Oberbayern Südost eG · VR Bank Schleswig-Holstein Mitte eG · VR-Bank Landau-Mengkofen eG · Volksbank eG – Die Gestalterbank · VBU Volksbank im Unterland eG · VR-Bank Erding eG · Volksbank Beilstein-Ilsfeld-Abstatt eG

The other two German rows are **JT Technologies GmbH** and **Deutsche WertpapierService Bank AG** (dwpbank — securities-services infrastructure for, among others, the cooperative and savings-bank sector).

> 🟢 **PERMITTED, and it is the strongest Theme-4 sentence this corpus has produced:**
> *In the fifty-eight days after MiCA's transitional period ended, thirty-five firms entered ESMA's authorised-CASP register. Fourteen were German, and twelve of those fourteen were cooperative or regional retail banks. The post-deadline entrant to European crypto services is not a crypto-native firm; it is a Volksbank.*

> 🔴 **NOT ONE OF THE 35 IS A TRACKED-COHORT FIRM.** Checked programmatically against every Stratum 1–4 name and commercial name (Binance, OKX, Bybit, KuCoin, Coinbase, Kraken/Payward, Crypto.com/Foris, Gemini, Bitstamp, Bitpanda, HTX/Huobi, Sui, Aptos, Solana, Aave, Polygon, Optimism, Arbitrum, Ava Labs, ConsenSys/MetaMask, Phantom, Ledger, Trust Wallet, Rabby, Securitize, Tether, Relai): **zero hits.**
> **The permitted reading is narrow and factual: no tracked-cohort firm was newly authorised in this window.** It is **not** evidence that any of them was refused, withdrew, or is unauthorised — nine of the eleven Tier-1 exchanges already held an entry as of the 08-25 capture, so for those firms a post-deadline authorisation would be redundant by construction.

---

## 🔴 DEFECT FOUND IN THE REGISTER ITSELF — one row is forward-dated, and its own metadata proves it is not a capture artifact

| Field | Value |
|---|---|
| `ae_lei_name` | **Deutsche WertpapierService Bank AG** |
| `ae_competentAuthority` | Federal Financial Supervisory Authority (BaFin) |
| `ae_lei` | `529900EXG2PM316ISO63` |
| `ac_authorisationNotificationDate` | **28/08/2026** |
| `ac_lastupdate` | **30/07/2026** |

**A register captured on 2026-08-17 carries a notification date of 2026-08-28 — eleven days after the capture, and one day in the future as of today.**

This is **not** a truncation or a parse error, and the row disproves both readings from inside itself:

- **Not a DD/MM ambiguity.** The column is unambiguously DD/MM/YYYY across the file (values such as `15/10/2025` cannot be MM/DD).
- **Not a capture artifact.** `ac_lastupdate` is **30/07/2026** — the row was last touched *before* the capture and already carried a *later* notification date. The forward date was in the source, not introduced in transit.

**Two readings, neither asserted:** (a) BaFin records a forward *effective* date for an authorisation already granted; (b) a data-entry error at source. **The corpus takes no position.** What it records is that ESMA's authorised register contains at least one authorisation dated in the future relative to the capture — which is exactly the class of thing a hostile reader checks first.

---

## Authorisations that ENDED — both before the deadline, one voluntary

`ac_authorisationEndDate` is populated in **2 of 329 rows**:

| Firm | Authority | End date | Register comment |
|---|---|---|---|
| Stratos Europe Ltd | CySEC | 24/04/2026 | *(none)* |
| Decubate B.V. | AFM | 26/03/2026 | **"Voluntary request to revoke authorisation by the entity"** |

> 🟢 **PERMITTED:** *Two of the 329 authorisations in the register carry an end date, and both ended before the transitional period closed — one at the entity's own request.*
> 🔴 **PROHIBITED:** any characterisation of these as enforcement outcomes. Neither row carries an infringement, a sanction, or a reason beyond the AFM comment quoted verbatim above.

---

## Explicit non-claims

1. **No post-deadline authorisation rate is claimed for the window after 2026-08-17.** The +6 rows observed on 08-25 (329 → 335) are **not** in this snapshot and their dates were **not** read. The rate above is scoped to the 08-17 capture and says so.
2. **No claim that 35 is a complete count of post-deadline authorisations.** It is a count of rows *present in the register on 2026-08-17 bearing a notification date on or after 2026-07-01*. Registers lag.
3. **No claim about any tracked firm's authorisation status** beyond "not newly authorised in this window." The Binance/HTX absence finding stands where it was made — in the 08-25 record, from the 335-row capture — and is not restated or extended here.
4. **No inference from the June spike to firm intent.** 75 authorisations in June is what the register shows; *why* firms clustered there is not in this document.
5. **The forward-dated row is recorded, not adjudicated.**
6. **`CASPS.csv` was NOT re-fetched today** — by `web_fetch` (standing prohibition since 08-25) or by any other channel. **Every figure above comes from a file already in the repository**, re-verified COMPLETE by `verify-capture.py` before a single statistic was derived from it.
7. **The twelve cooperative-bank names are quoted from `ae_lei_name` verbatim.** No firm was researched, characterised, or described beyond what the register field states; "cooperative or regional retail bank" is an inference from the legal names (eG / Volksbank / Raiffeisenbank / VR-Bank), and it is labelled as one.

---

## Method — reproducible in one pass

```
python3 scripts/verify-capture.py corpus/regulator-filings/_esma-casps-snapshot-2026-08-17.csv --expect-rows 329
# → CAPTURE HEALTH: COMPLETE, exit 0

# then: parse ac_authorisationNotificationDate as %d/%m/%Y, count >= 2026-07-01,
#       group by ae_competentAuthority / ae_homeMemberState, scan ae_lei_name for cohort names.
```

**🟢 `verify-capture.py` RAN TODAY — the first time in four runs the executable itself could be applied to a class-3 artifact.** On 08-22, 08-24 and 08-25 the tool existed while the capture never became a file, and its predicates had to be applied by hand or by an equivalent implementation. Today the predicate and the executable are the same thing, and the run is auditable by anyone with the repo. **Watch (pp)'s plumbing gap is closed for stored snapshots; it remains open for live fetches.**
