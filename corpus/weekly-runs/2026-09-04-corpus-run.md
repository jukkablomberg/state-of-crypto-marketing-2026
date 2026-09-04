# 2026-09-04 — corpus run (day 65, third full post-window day)

**KPI — 11 of 11 units done. Bundle FROZEN; publish 2026-09-15.** Per the re-based cadence's REMAINING RUNS row
(`synthesis-plan.md`, set 2026-09-03), the unit ladder is complete and no chapter is re-drafted. Today is not one of
the two bounded exceptions: exception (a), the second-pass citation audit, was taken and closed by the 09-03 run;
exception (b), the FCA v Huobi stay expiry, falls on **09-08**. This run is therefore STEP 0 plus this record.

**Not a FAILED run.** The prompt's failure test is a run that ends without a unit written or advanced. There is no
undone unit to advance — all eleven are done and the plan's own binding row defines this run's output as the
post-window check plus one dated record. Writing an unrequested twelfth unit would edit a frozen bundle, which the
same plan forbids.

---

## STEP -1 — system map

`python3 _meta/verify_system_map.py` → **exit 1**, one finding, not mine:

- `[MIRROR] prompts-mirror auto-sync stale: .auto is 2.3 h old (limit 2 h)` — the launchd prompt-mirror job
  (`com.jukka.prompts-mirror`) is dead or blocked. **Recorded, not escalated:** it is an OS-plumbing artefact with a
  named owner (`os-plumber`, Mondays, via E3 `cos-feedback.md`), it does not block this loop, and re-escalating a
  known machinery fault is exactly what the escalation rules forbid. Everything else clean: 15 active loops · 10
  retired · 31 edge artifacts · 25 prompt checks.

**E22 unchanged.** This loop is still the producer; the report is still the consumer; Jukka still publishes. No work
was assigned to any other loop, so no other loop's prompt needed editing.

---

## STEP 0 — post-window corpus check

`python3 repo/scripts/daily-corpus-sync.py`. **Class-1 capture window CLOSED 2026-08-31 and honoured in code**
(`CAPTURE_WINDOW_END` untouched). `_absence.csv` and `_chrome-queue.csv` were **not** rewritten; their `as_of` stays
2026-08-31. The feed is read and reported; nothing was admitted.

| class | net-new |
|---|---|
| 1 — job postings | **0** (0 offered post-window, 0 admitted) |
| 2 — agency claims | **0** new relationships; 18 snapshot files written, 8 matrix rows, 1 tracked-firm overlap (Sui — Coinbound + RZLT); panel as-of **2026-06-15**, unchanged and not stale by Jukka's 07-10 Path-2 decision |
| 3 — regulator filings | **0** |
| 4 — operator statements | **0** |
| 5 — layoff tracker | **0** |
| 6 — campaigns | **0** |

**FEED HEALTH: HEALTHY** — `scanned_at_utc` 2026-09-03T21:47:05Z (age 14.6 h), fingerprint `total_jobs_fetched`
3452, delta **+33** vs 09-03 (3419). The standing `scan_metadata` cross-check guard passed, so the five tracked
firms still without coverage (Aave, Binance, Bybit, HTX, KuCoin) remain a **live read only** and were not written to
the shipped exhibit — the absence exhibit keeps its 08-31 state.

**Drop-everything sweep — three explicit zeroes.**

1. **First named NCA marketing-side enforcement case: NO.** Searched. The public picture is unchanged from 09-03:
   NCAs (BaFin, AMF, AFM) are described as running thematic reviews, supervisory reviews and spot checks. No named
   marketing-side case against a CASP has been published. This is not a gap in the corpus — it is Chapter 1's thesis
   holding for a 65th day.
2. **Class-4 statement by a senior operator at a tracked firm about the marketing function: NO.**
3. **2026 marketing-team layoff with a stated rationale: NO.** Cuts continue to be announced at the whole-company
   level with AI-efficiency or market-conditions rationales; not one names marketing as the function. Theme 5's
   headline thesis is unmoved.

**Watch items (POST-WINDOW — recorded here, not admitted to the report body).**

- The third-party aggregator figure resurfaced unchanged (">7,254 disclosed job cuts across 47 companies" in 2026;
  Luno "around 20%", CEO citing automation investment). **Same non-admission as 09-03:** aggregator arithmetic
  against an unstated base is not a primary figure. Entered nowhere. Noted a second time only so a later run does
  not mistake it for new.
- **FCA v Huobi — the 09-08 check is live and unchanged.** The stay expires Tuesday. That run re-opens the FCA
  proceedings page and, **only if an outcome is published**, updates the one sentence in Chapters 5 and 7 and
  rebuilds report → HTML → PDF with a dated `PUBLISH.md` changelog line. If nothing is published, the bundle stays
  frozen and the run says so.

**Friday duty — inbound nominations: checked, none.**

---

## SIDE DUTY — the SoCM re-date row

The 2026-09-02 needs-jukka row *"SoCM re-date"* reads **CLEARED 2026-09-02 16:58Z**, live-verified. The README lines
from `PUBLIC-REDATE-2026-09-02.md` were **already applied and pushed the same day** (DE push 16:37Z) — `repo/README.md`
now carries "Publishes **September 15, 2026** (first announced for September 1; the capture window closed August 31)",
the dated Phase-3 note and the September-15 citation line. **Nothing to apply. Duty closed; it does not recur.**

---

## Bundle state — unchanged, and deliberately so

| artefact | state |
|---|---|
| `report/state-of-crypto-marketing-2026.md` | 23,070 words ≈ **21.0pp** of a 25pp budget |
| provenance gate | **250 URLs / 0 untraced** |
| `publish-bundle/report.html` | 176 live citation links |
| `publish-bundle/report.pdf` | 44pp A4 (WeasyPrint) |
| `publish-bundle/PUBLISH.md` | written; the PUBLISH needs-jukka row is **OPEN** since 09-02 |

No file in `findings/`, `report/` or `publish-bundle/` was touched by this run.

---

## What Jukka has to do

Nothing new. The single open ask is the existing row — **PUBLISH on 15 September, bundle ready at
`publish-bundle/`, steps in `PUBLISH.md`.** No second row was filed and none will be.

**Next run (09-05 → 09-07):** STEP 0 and one line. **09-08:** the FCA v Huobi check.
