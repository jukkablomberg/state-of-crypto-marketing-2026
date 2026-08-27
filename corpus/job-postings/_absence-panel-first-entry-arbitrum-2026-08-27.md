# The absence panel gained its first member in the series — because a socket timed out

**Run:** 2026-08-27 (day 57 post-deadline). **Class 1.**
**Event:** `_absence.csv` **5 → 6.** **Arbitrum Foundation** entered the panel.
**Cause:** `network error fetching https://api.lever.co/v0/postings/arbitrumfoundation?mode=json: **The read operation timed out**`

---

## Headline

**On 08-25 a firm left the absence panel and it turned out it had never been absent. On 08-27 a firm entered it, and the firm did nothing at all.**

Watch **(ad)** — *"the absence panel has never contained an absence"* — was opened two days ago on an exit. Today it fires on an **entry**, and the entry is a stronger demonstration than the exit was.

---

## What is verifiable

**Arbitrum has never appeared in `_absence.csv` before today.** Checked programmatically across **all 30 commits** touching the file, back to 2026-07-20: `arbitrum_rows=0` in every one, `arbitrum_rows=1` today.

**Nothing about Arbitrum changed.** The panel's own `reason` column states the cause: a **Lever API read timeout**. And the timeout is not isolated —

| `fetch_errors` today (6) | ATS | Error |
|---|---|---|
| Wormhole Foundation | greenhouse | HTTP 404 |
| **Aave** | lever | HTTP 404 *(stable; in panel since long before today)* |
| **Arbitrum Foundation** | lever | **read operation timed out** |
| 1inch Network | lever | **read operation timed out** |
| Bitwise Asset Management | lever | HTTP 404 |
| Chainlink Labs | ashby | HTTP 404 |

**Two of the six errors are read timeouts and both are Lever.** This is a transient network condition on one morning affecting one ATS vendor, not a publishing decision by a Layer-2 foundation.

**The panel's membership is therefore a function of network luck.** Aave's 404 is stable and reproducible across weeks; Arbitrum's timeout is not. **They sit in the same file, in the same column, and mean entirely different things — and only the `reason` column distinguishes them.**

---

## Why this is load-bearing five days from ship

The 08-25 record established the prohibition:

> 🔴 **PROHIBITED:** any sentence of the form *"Binance / Bybit / HTX / KuCoin / Aave shows no public marketing-hiring signal."*

**Today extends it, and extends it in the harder direction.** The 08-25 case was a *systematic* defect — an upstream slug had been wrong for weeks, and fixing it revealed a posting that had been public for nineteen days. That is bad, but it is *stable*: the same firm would have been "absent" every day until someone fixed it.

**Arbitrum's case is worse, because it is not stable.** A firm can enter the absence panel and leave it again on consecutive days with no event at either end. **Any absence claim drawn from this file is therefore not merely biased — it is non-reproducible.** A reader who re-ran the scan tomorrow could get a different panel, and neither run would be wrong.

> 🔴 **PROHIBITED, added today:** any sentence of the form *"Arbitrum shows no public marketing-hiring signal"*, and any **count** of absent firms presented as a finding (*"six tracked firms show no hiring signal"*). The panel's cardinality moves with network conditions.
> 🟢 **The supportable sentence is unchanged and belongs in the appendix:** *"not reachable through the ATS APIs this corpus scans on the day of the scan."*

**Note the panel's composition, which the 08-25 record already flagged and today sharpens.** Six rows: **Aave** (stable 404) · **Arbitrum** (today's timeout) · **Binance ×2, Bybit, HTX, KuCoin** (proprietary recruiting SPAs). Five of the six are firms that own their hiring stack or whose ATS slug is broken. **It remains a sample of scanner reach, not a sample of silence.**

---

## The rest of class 1 today

```
date: 2026-08-27   source A (jobs) scan_date: 2026-08-27
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-26T22:00:47Z, age=14.6h,
  fingerprint total_jobs_fetched=3356, delta=+22 vs 2026-08-25 (3334))
job postings ADDED: 0  firms: []
```

### 🟢 The fingerprint is COMPARABLE today — verified by hand, watch (ac)

The 08-24 → 08-25 discontinuity (2,263 → 3,334) was **instrument growth**: `companies_via_api` moved 89 → 99. Watch **(ac)** recommended persisting that field and reporting UNCOMPARABLE when it moves. It was deliberately **not implemented** (watch (tt): do not ship a new guard days from ship).

**Checked by hand today, against the upstream feed's own `scan_metadata`:**

| Field | 2026-08-25 | 2026-08-27 |
|---|---:|---:|
| `companies_scanned` | 147 | **147** |
| `companies_via_api` | 99 | **99** |
| `companies_via_chrome_pending` | 48 | **48** |
| `total_jobs_fetched` | 3,334 | **3,356** |

**The denominator did not move. Today's +22 is the first genuinely comparable reading since the break** — and it is a *market* delta, not an instrument one.

⚠ **But it spans two calendar days, not one** (see cadence, below), so **+22 is not a daily rate.** Do not annualise it, do not compare it to a one-day delta.

**The guard remains unshipped, on purpose.** Today's check was manual, is recorded here, and is reproducible from the two `scan_metadata` blocks. **Five days from ship, a written verification beats an unproven predicate.**

### `job postings ADDED: 0` — and the reason is not silence

The upstream feed reports `new_count: 1`. **The one net-new marketing role is at Anthropic** (`greenhouse:anthropic:5406113008`, *Partner Marketing Lead, Cloud*, posted 2026-08-26, Tier 3, category AI) — **outside the tracked-firm cohort**, so the sync correctly admitted nothing.

> 🟢 **PERMITTED:** *the scan ran, found one net-new senior marketing role across 147 companies, and it was not at a cohort firm.*
> 🔴 **PROHIBITED:** *"the cohort posted no marketing roles today."* The scan reaches 99 of 147 companies and six tracked firms are unreachable, two of them for reasons that did not exist yesterday.

### 🔴 Cadence broken — this is a TWO-day gap, and the data says so from the inside

**Today's fingerprint comparison is against `2026-08-25`, not `2026-08-26`.** `_feed-fingerprint.json` has no 08-26 entry. **The corpus loop did not run on 2026-08-26.** Watch (e′) falls to **9 of 11**.

⚠ **The upstream feed was healthy throughout** — `scanned_at_utc: 2026-08-26T22:00:47Z`. **The ATS scan ran on the 26th; the corpus run did not.** The failure is in this loop, not its input.

**Corroborated outside the repo.** `situation.md` (nightly-reconcile, 64th run, 2026-08-27) records a *"FACTORY SILENT-FAILURE CLUSTER — 5 fired-runs-with-zero-artifacts in 72h"*, with the working hypothesis that the `/sessions` scratch volume is full. **Confirmed from inside this run's own sandbox:**

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1    9.8G  9.3G     0 100% /sessions
```

**0 bytes available.** A session that cannot materialise its workspace dies before its first tool call — which fits *fired-with-zero-trace* exactly. **This is infrastructure, not methodology, and it is Jukka's to fix** (`needs-jukka` row 545). **Recorded here because a missing corpus day is a corpus fact**, and because the gap is now attributable rather than mysterious.

### Class 2 — byte-identical, sixteenth consecutive run

`trend-data.json` `lastUpdated` **2026-06-15 — 73 days stale.** 18 agency-claims files written, byte-identical. 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)**, unchanged since first observation.

🔴 **Watch (d), 22nd run.** `methodology.md` §6 still calls this a *"daily 18-agency panel."* **Five days to ship.**

---

## Explicit non-claims

1. **No claim that Arbitrum has stopped or reduced marketing hiring.** The corpus has no Arbitrum job-postings file and has never had one; today it also has no reachable Arbitrum ATS endpoint. **Both facts are about this corpus.**
2. **No claim that the Lever timeouts are Lever's fault**, or that they will persist, or that they were absent before. They are recorded as observed on one morning.
3. **No absence count is published**, and the panel's size is explicitly disclaimed as unstable.
4. **The comparability check is a hand verification, not a guard.** It is recorded, not automated, and the run says so.
5. **`companies_via_api` was read from the live feed only.** No backup existed in the sandbox this run, so no field-by-field diff of the kind performed on 08-25 was possible; the comparison is against the figures **as recorded in the 08-25 run record**, which quotes them verbatim.
6. **The `/sessions` disk observation is this sandbox's, reported as such.** It corroborates `situation.md`'s hypothesis; it does not prove the cause of any specific missed run.
