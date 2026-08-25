# Class 1 — the feed grew by 47% overnight, a firm left the absence panel for the first time, and both facts are about the instrument

**Class:** 1 (job postings)
**Date:** 2026-08-25
**Trigger:** `scripts/daily-corpus-sync.py` reported `FEED HEALTH: HEALTHY … fingerprint total_jobs_fetched=3334, delta=+1071 vs 2026-08-24 (2263)` and `job postings ADDED: 1 firms: ['MetaMask / ConsenSys']`.

---

## 1. 🔴 THE FINGERPRINT PREDICATE PASSED, AND IT PASSED FOR THE WRONG REASON

The guard's rule (added 2026-08-14, watches bb + ff) is: *a delta of 0 degrades the verdict to STALE; the predicate tests **movement**, not direction.* On 08-24 that rule correctly admitted a **negative** delta (−2) as liveness evidence.

Today it admitted **+1071 — a 47% jump in one day.** It was right that the scan ran. **It was right by accident.**

The upstream scan metadata, compared against the 2026-08-24 backup of `open-positions.json`:

| Field | 2026-08-24 | 2026-08-25 |
|---|---|---|
| `companies_scanned` | 147 | 147 |
| **`companies_via_api`** | **89** | **99** |
| **`companies_via_chrome_pending`** | **58** | **48** |
| `ats_breakdown.greenhouse` | 24 | **29** |
| `ats_breakdown.ashby` | 37 | **42** |
| `ats_breakdown.proprietary` | 57 | **47** |
| `total_jobs_fetched` | 2,263 | **3,334** |
| `fetch_errors` | 4 | 4 (identical set) |

**Ten companies moved from proprietary/chrome-pending to API-reachable:** Circle, ConsenSys, FalconX, Fireblocks, Ondo Finance, OpenAI, Parity (Polkadot), Ripple, Starknet Foundation, Stellar Development Foundation. Five gained a Greenhouse slug, five an Ashby one. `companies_scanned` never moved.

**The denominator changed. The job market did not.** The +1071 measures the instrument getting bigger, not hiring getting busier.

### The finding, stated for the methodology

**The fingerprint series is now discontinuous, and any longitudinal reading across 2026-08-24 → 2026-08-25 is invalid.**

```
2151 → 2151 (frozen) → 2186 → 2196 → 2259 → 2265 → 2263 ‖ 3334
                                                        ↑
                                            denominator break
```

The guard cannot distinguish *"the scan looked and the world moved"* from *"the scan looked at more of the world."* Both produce a non-zero delta. **This is not a bug in the predicate — liveness is all it was ever built to certify — but it is a limit that was never written down, and today is the first time it mattered.**

**⚠ And it is watch (ss) landing inside our own instrumentation.** A +1071 delta *confirms* the thing the guard wants to be true. A confirming result gets less scrutiny than a surprising one. Had this run not opened the upstream metadata, the record would have printed *"HEALTHY, delta +1071"* as evidence of a live scan — a true statement resting on a false reason.

**RECOMMENDED PREDICATE (not implemented this run):** persist `companies_via_api` alongside `total_jobs_fetched` in `_feed-fingerprint.json`, and report the delta as **UNCOMPARABLE** whenever the API-reachable company count changes. One field, one comparison. It is deliberately left unimplemented rather than shipped untested seven days from ship — **a new guard's first run is a test of the guard, not of the corpus** (watch tt).

## 2. ⭐ THE FIRST FIRM EVER TO LEAVE THE ABSENCE PANEL — AND WHAT ITS ABSENCE ACTUALLY MEASURED

**MetaMask / ConsenSys** exited `_absence.csv` and `_chrome-queue.csv` today. The panel drops 6 → 5 (Aave, Binance, Bybit, HTX, KuCoin); the Chrome queue drops 6 → 5 (Binance, Bybit, HTX, KuCoin, Solana). **No tracked firm had ever left either list before.**

The blocker note the sync has carried for weeks read: *"Greenhouse-embedded — fix the API slug (`boards-api.greenhouse.io/v1/boards/consensys`)."* Upstream fixed the slug. The firm did nothing.

**The posting that arrived is dated 2026-08-06.**

```
date_posted : 2026-08-06
title       : Product Marketing Lead - Trade
jurisdiction: UNITED STATES - Remote, EMEA - Remote, LATAM - Remote
seniority   : Lead / PMM
source_url  : https://consensys.io/open-roles/8048308?gh_jid=8048308
captured    : 2026-08-25   (ATS=greenhouse; url_verified=True)
```

**The role was public for nineteen days before this corpus could see it.** It was never absent. *We* were.

### 🔴 THE CONSEQUENCE FOR THE REPORT, AND IT IS LOAD-BEARING

`methodology.md` says: *"Where a firm has shipped no public signal on a theme, that absence is itself a finding."* That rule is sound. **The absence panel does not implement it.**

Every row in `_absence.csv` today, and every row it has ever held, carries a `reason` of either `api-fetch-error` or `proprietary-ATS/needs-chrome`. **Not one row has ever meant "this firm published nothing." Every row has always meant "our scanner could not reach this firm's ATS."**

The file itself is honest — the `reason` column has recorded the distinction all along. **The reading was not.** Two different things have been sitting in one panel:

- **(a) the firm shipped no public signal** — a finding about the firm. **Count in the corpus: zero.**
- **(b) our scanner cannot reach the firm** — a finding about NorthPoint. **Count: all of them.**

**PROHIBITED, and it must be stated in the methodology before ship:** the report may not print, for Binance, Bybit, HTX, KuCoin or Aave, any sentence of the form *"shows no public marketing-hiring signal."* The only supportable sentence is *"is not reachable through the ATS APIs this corpus scans,"* which is a statement about our method and belongs in the appendix, not in Theme 1 or Theme 4.

**⚠ Directional note.** Four of the five remaining absence-panel firms are Tier-1 exchanges on proprietary SPAs (Binance, Bybit, HTX, KuCoin). The panel is not a random sample of silence — **it is a sample of firms that run their own recruiting stack**, which is itself correlated with size. Any absence-flavoured claim inherits that bias.

## 3. What the 47% expansion produced for this report: one posting

Of the ten newly API-reachable companies, **one is in the Stratum 1–4 tracked cohort** (ConsenSys). The alias table in `daily-corpus-sync.py` correctly matched it and correctly excluded the other nine.

**But three of the nine map onto Stratum 4's three unresolved TBD slots:**

| Newly reachable | `tracked-firms.md` Stratum 4 placeholder |
|---|---|
| Fireblocks | *(CASP-licensed custodians)* — TBD since May |
| Ondo Finance | *(additional CASP-licensed asset managers)* — TBD since May |
| Circle | *(additional CASP-licensed asset managers)* — TBD since May |

**Not added.** Resolving the cohort seven days before ship is a scope change, not a corpus task, and it is escalated rather than taken. Recorded because the coverage that would have supported those slots did not exist in May and does exist now.

## 4. 🔴 THE COHORT IS 27 NAMED FIRMS. BOTH READMEs SAY THIRTY.

Counted from `tracked-firms.md` this run:

| Stratum | Named firms | TBD placeholder lines |
|---|---|---|
| 1 — Tier-1 exchanges | **11** (header says "target ~10") | 0 |
| 2 — L1/L2 foundations | 8 | 0 |
| 3 — Wallets / consumer | 5 | 0 |
| 4 — CASP-licensed non-exchange | **3** (Securitize, Tether, Relai) | **3** |
| **Total** | **27** | 3 |

`README.md` states *"Tracked firms — substantive synthesis cohort (~30)"* and Theme 1 promises *"who owns what across thirty firms."* `README-for-github.md` carries the same. `tracked-firms.md` line 69 asserts *"Tracked-firm count: 40 (10 exchanges + 8 foundations + 5 wallets + 6 CASP incl. Relai + 11 to-be-resolved)"* — which does not reconcile with its own tables (Stratum 1 lists 11, not 10; Stratum 4 lists 3 named, not 6).

**This is the same defect class as the three advertised layoff examples: a number in a published README that a hostile reader can count in ninety seconds.** The corpus is public. Someone will count.

**Neither README was edited this run** — the fix is a wording decision (say 27, or resolve the three slots), and it belongs to Jukka. Escalated.

## 5. Explicit non-claims

1. **No claim that crypto marketing hiring rose.** The +1071 is instrument growth; the tracked-cohort net-new is **one posting**.
2. **No claim that ConsenSys began hiring on 2026-08-06.** That is the posting's date; the corpus has no view of when the requisition opened.
3. **No first-party capture of the ConsenSys posting.** `web_fetch` refused `consensys.io/open-roles/8048308?gh_jid=8048308` — *"URL not in provenance set"* — and the search-then-fetch route used successfully on 08-24 did not surface this URL (it surfaced a different ConsenSys role, `/open-roles/6841507`). **The row rests on the ATS feed's own `url_verified=True` flag, not on a first-party read.** Marked as such; see watch (i).
4. **The Chrome channel was NOT used to route around that refusal.** It was used only where `web_fetch` succeeded and returned unusably truncated content (the CASPS register). **A provenance refusal is a refusal; a truncation is a channel defect. The two were not treated the same way, deliberately.**
5. **No new firms added to the cohort**, and no edit to `tracked-firms.md`.
6. **No new guard implemented.** The `companies_via_api` predicate is a recommendation, not a shipped change.
