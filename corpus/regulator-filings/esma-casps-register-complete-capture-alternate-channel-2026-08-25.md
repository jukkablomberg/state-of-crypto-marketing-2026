# ESMA authorised-CASP register — COMPLETE capture via an alternate channel, and the Theme-4 absence claim it finally permits

**Class:** 3 (regulator filings / registers)
**Captured:** 2026-08-25
**Source (primary):** `https://www.esma.europa.eu/sites/default/files/2024-12/CASPS.csv` — ESMA's register of authorised crypto-asset service providers under MiCA.
**Retrieval channel:** browser-context `fetch()` (Claude-in-Chrome), **not** the `web_fetch` channel that truncated this file on 2026-08-17 and again on 2026-08-24.
**Verdict:** 🟢 **COMPLETE.** Absence claims about named entities are **PERMITTED** from this capture.

---

## 1. Why this run changed the channel instead of spending a third fetch

The 08-24 record's recommendation 3 read, verbatim: *"`CASPS.csv` — TRUNCATED ON TWO ATTEMPTS. STOP RE-FETCHING IT THE SAME WAY… It needs a channel that persists bytes to disk, or it ships unread… Decide which — do not spend a third fetch on the same failing route."*

The route was changed. The result settles the question the retired size heuristic could not:

| Attempt | Channel | Chars | Rows | Verdict |
|---|---|---|---|---|
| 2026-08-17 | `web_fetch` | 161,380 (after re-fetch) | 329 | COMPLETE (baseline) |
| 2026-08-17 (first) | `web_fetch` | 82,445 | ~205 lines | 🔴 TRUNCATED, cut mid-field |
| 2026-08-24 | `web_fetch` | 82,445 | ~205 lines | 🔴 TRUNCATED, cut mid-field, byte-identical to 08-17 |
| **2026-08-25** | **browser `fetch()`** | **163,026** | **335** | 🟢 **COMPLETE** |

**The cut point was a property of the retrieval channel, exactly as the 08-20 finding said.** Two channels were pointed at one unchanged URL on consecutive days and returned 82,445 and 163,026 characters. This is the cleanest confirmation the corpus has that **structure, not size** is the only usable predicate — and it is now confirmed by construction rather than by inference.

## 2. Verification — `verify-capture.py`'s predicates, applied programmatically

`verify-capture.py` **could not be run**, for the third consecutive run: the fetch again never became a file on a filesystem the script can open. **But unlike 08-24, the predicates were not applied by hand.** They were evaluated programmatically in the retrieval context against an RFC-4180 parser (quoted fields containing commas and newlines handled correctly):

- **Primary predicate — final-row termination:** ✅ final data row carries **16 of 16** fields. Final row: `National Bank of Slovakia (NBS)` / `Okazio s.r.o.`
- **Secondary predicate — field-count consistency:** ✅ **335 of 335 data rows carry exactly 16 fields. Zero ragged rows.** (Prior captures of ESMA registers have contained legitimately ragged quoted fields; this one does not.)
- **Cross-check against a prior verified capture:** 329 rows verified COMPLETE on 2026-08-17 → **335 today, +6.** Above expectation, which `verify-capture.py --expect-rows` treats as *"the source may have gained rows; re-baseline before claiming a delta."* Re-baselined here.
- **Auditable anchor:** **SHA-256 of the raw bytes = `196090fa6fa15162fee56084dd0d0e53c158bb7347991538ce683b0b256d6b3e`, 163,370 bytes.** Any future capture is comparable byte-for-byte against this without re-deriving anything.

### ⚠ Why no snapshot file was written — and it is not the 08-23/08-24 reason

The bytes could not be persisted. Transferring them out of the retrieval context as base64 was **blocked by the channel**, and that block was respected rather than routed around.

**A byte-exact text transfer was also ruled out, on evidence rather than caution.** The raw file is **163,370 bytes**; the same content decoded as UTF-8 and re-encoded is **163,367 bytes**. The file therefore contains at least one byte sequence that is not valid UTF-8 — almost certainly a legacy-encoded character in an address field. **A text round-trip would have produced a file that was three bytes different from the register and looked identical.** That is precisely the failure class this corpus exists to catch, so it was not done.

**What is recorded is therefore: a complete capture, structurally verified, hash-anchored — and no stored artifact.** The 08-23 precedent (*hand-transcribing would produce a fabricated artifact, not a capture*) is upheld and extended: **a lossy re-encode is also a fabrication, even when it is automated.**

## 3. 🟢 THE ABSENCE CLAIM, PERMITTED FOR THE FIRST TIME SINCE 08-17

Register composition: **335 authorised CASP entries · 27 distinct competent authorities · 26 member states.**

**Of the eleven Tier-1 exchanges in the tracked cohort, nine appear on the register. Two do not.**

| Tracked Tier-1 firm | Register entity | MS | Notified |
|---|---|---|---|
| OKX | OKX Europe Limited | MT | 27/01/2025 |
| Bybit | Bybit EU GmbH | AT | 28/05/2025 |
| KuCoin | KuCoin EU Exchange GmbH | AT | 27/11/2025 |
| Coinbase | Coinbase Luxembourg S.A. | LU | 20/06/2025 |
| Kraken | Payward Global Solutions Ltd **+** Payward Europe Solutions Ltd | IE | 25/06/2025 |
| Crypto.com | Foris DAX MT Limited | MT | 27/01/2025 |
| Gemini | Gemini Intergalactic EU Ltd | MT | 21/08/2025 |
| Bitstamp | Bitstamp Europe S.A. | LU | 15/05/2025 |
| Bitpanda | Bitpanda GmbH **+** Bitpanda Asset Management GmbH (DE) **+** BP23 CA Limited (MT) | AT/DE/MT | 09/04/2025 → |
| 🔴 **Binance** | **no occurrence in any field of any of the 335 rows** | — | — |
| 🔴 **HTX** | **no occurrence of "HTX" or "Huobi" in any field of any of the 335 rows** | — | — |

Also present, outside Stratum 1: **Aave** — `Push Virtual Assets Ireland Limited`, commercial name **"Push / Aave Push"**, IE, notified 12/11/2025. **Relai** — `RELAI EU SASU`, FR, notified 23/10/2025.

**The shippable sentence, and the limit on it:**

> Fifty-five days after the MiCA transitional period ended, nine of the eleven Tier-1 exchanges this report tracks hold an entry on ESMA's register of authorised crypto-asset service providers. **Binance and HTX hold none.** Binance's absence has a published explanation — the firm announced in June 2026 that it would cease providing crypto-asset services in EU markets. **HTX's absence has no published explanation at all.**

→ Binance corroboration already in corpus: `binance-mica-eu-exit-2026-06.md`.

## 4. 🔴 THE ABSENCE THAT IS NOT A FINDING — AND THE REPORT MUST SAY SO

Sixteen tracked firms return zero hits. **Fourteen of those sixteen absences are analytically empty, because the entity is outside the CASP perimeter by category.** Printing them as absences would be technically true and worthless:

- **L1/L2 foundations** (Sui, Aptos, Solana, Polygon, Optimism, Arbitrum, Ava Labs) — foundations are not crypto-asset *service providers*.
- **Non-custodial wallets** (MetaMask/ConsenSys, Phantom, Rabby, Trust Wallet, Ledger) — non-custodial software sits outside MiCA's CASP definition.
- **Tether** — an asset-referenced/e-money token *issuer*, governed by MiCA Titles III–IV, not the CASP title. It would not appear in this register even in full compliance.

**RULE ADOPTED: an absence from `CASPS.csv` is evidence only for an entity that provides crypto-asset services to EU clients. For everything else it is a category error.** Only **Binance** and **HTX** clear that bar among the sixteen.

### 🔴 And one absence is an internal inconsistency in our own cohort file

`tracked-firms.md` titles Stratum 4 **"CASP-licensed EU firms (non-exchange)"** and lists **Securitize** under it. **Securitize returns zero hits anywhere in the register.** Either the stratum label is wrong, or the firm is misclassified in our own cohort definition. Relai — listed in the same stratum and described as MiCA-licensed — *is* present, so the label is not uniformly wrong. **Resolve before ship; do not print Stratum 4 as "CASP-licensed" until it is resolved.**

## 5. What this run did NOT claim

1. **No stored snapshot exists for 2026-08-25.** The last stored artifact remains `_esma-casps-snapshot-2026-08-17.csv` (329 rows, md5 `69e7dc…`). Today's capture is anchored by SHA-256 only.
2. **No claim that the +6 rows are post-deadline authorisations.** Six rows were gained against an 8-day-old baseline; the notification dates of the new rows were not isolated. **Do not print a post-deadline authorisation rate from this.**
3. **No claim about why HTX is absent.** The register records absence; it does not record cause. No inference to enforcement, withdrawal, or non-application is made.
4. **No claim that the nine present firms are MiCA-marketing-compliant.** Authorisation is not a marketing-comms finding. Theme 4 asks whether a firm has a publicly visible MiCA-marketing-comms seat — that is a different question and this register does not answer it.
5. **No absence claim about the fourteen out-of-perimeter firms**, per §4.
6. **No claim that `verify-capture.py` returned an exit code today.** It did not run. Its predicates were applied programmatically by an equivalent implementation, which is weaker than the tool and is labelled as such.
7. **The Decubate B.V. row surfaced on a whole-row substring search for "aave" and is not counted as an Aave entity** — the match is not in either name field. Recorded so it is not re-discovered as a hit.
