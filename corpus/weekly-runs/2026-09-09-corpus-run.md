# 2026-09-09 — corpus run (day 70, eighth full post-window day) — **STEP 0 ONLY; BUNDLE FROZEN, NO EXCEPTION REMAINS**

**KPI — 11 of 11 units done. Bundle FROZEN; publish 2026-09-15 (T-6).** This run owed no unit and took no
exception: the unit ladder closed 2026-09-02, the second-pass audit closed 09-03, and the last scheduled change —
the 09-08 FCA v Huobi stay-expiry check — was taken and adjudicated NO CHANGE yesterday. Under the **REMAINING RUNS**
row of `synthesis-plan.md` this run is STEP 0 plus this record. **No chapter, report or bundle artefact was touched.**

**Not a FAILED run.** The FAILED-run rule attaches to a run that owed a unit and produced none. This run owed no
unit; the contract's own binding row names STEP 0 + one run-record line as the whole of the work from 09-09 to
09-14. What it produced: a completed post-window sweep, three explicit zeroes, a re-verified freeze (both bundle
SHA-256 values checked against the values recorded in `PUBLISH.md`, not assumed), and this record.

---

## STEP -1 — system map

`python3 _meta/verify_system_map.py` → **exit 0, clean** (16 active loops · 10 retired · 35 edge artifacts · 45
prompt checks). No findings. The counts moved since 09-08 (15→16 active, 34→35 edges, 39→45 prompt checks) because
the **Art Director** loop went live this morning at 06:44Z with edge E37 — **not** a change to this loop's mandate.

**E22 unchanged and still mine.** Producer: this loop. Consumer: the report. Gate: Jukka publishes. Nothing was
assigned to another loop this run, so no other loop's prompt needed editing.

⚠ **Scheduler note, recorded because it is new and is not a defect.** The Art Director now shares the **15:07**
slot with this loop, Mon–Fri, until this loop retires on the 09-15 publish. Per SYSTEM-MAP § 1 the two do not
collide: this loop is a STEP-0 no-op writing only its own run record and `_feed-fingerprint.json` around ~15:10,
and the Art Director writes under `design/` at the end of its run. **This run wrote nothing outside
`projects/state-of-crypto-marketing-2026/`.**

**Repo state:** level with `origin/main` before this run's commit (`git log origin/main..HEAD` empty); working tree
clean apart from the fingerprint. The DE shipped 09-08 as designed.

---

## STEP 0 — post-window corpus check

`python3 repo/scripts/daily-corpus-sync.py`. **Class-1 capture window CLOSED 2026-08-31 and honoured in code**
(`CAPTURE_WINDOW_END = "2026-08-31"`, untouched). `_absence.csv` and `_chrome-queue.csv` were **not** rewritten —
their `as_of` reads 2026-08-31, verified by direct read of the file this run, not inferred from the script's
summary. Only `_feed-fingerprint.json` was written: an instrument log, not a corpus claim.

| class | net-new |
|---|---|
| 1 — job postings | **0 admitted** (window closed; 0 offered) |
| 2 — agency claims | **0** new relationships; 18 snapshot files written, 8 matrix rows, 1 tracked-firm overlap (Sui — Coinbound + RZLT); panel as-of **2026-06-15**, unchanged and not stale by Jukka's 07-10 Path-2 decision |
| 3 — regulator filings | **0** |
| 4 — operator statements | **0** |
| 5 — layoff tracker | **0** |
| 6 — campaigns | **0** |

**Feed health: HEALTHY, third consecutive day.** `scanned_at_utc` 2026-09-08T21:46:25Z, **age 15.2 h** (limit 36 h),
`total_jobs_fetched` **3422, delta −1** vs 09-08's 3423. The `scan_metadata` cross-check guard **passes**. As on
09-08, a small negative delta is postings closing marginally faster than they open, not a scanner fault. **No report
consequence either way:** the class-1 exhibit is frozen at 08-31 and no feed state can now reach the report body.
The five tracked firms still without coverage (Aave, Binance, Bybit, HTX, KuCoin) remain a **live read only**,
unchanged and unwritten.

**Drop-everything sweep — three explicit zeroes.**

1. **First named NCA marketing-side enforcement case: NO.** Unchanged for a 70th day. What is published remains
   *supervisory practice and vendor commentary describing the regime* — NCAs sampling marketing communications
   against the Art. 7 / Art. 66 fair-clear-not-misleading standard, risk-warning prominence and finfluencer
   supervision, with information requests, inspections and authorisation suspension as available remedies. **No
   named case against a named CASP.** No addendum box is owed; Chapter 1's thesis holds. The one *named* marketing
   enforcement action in this corpus remains the FCA's, in a non-MiCA jurisdiction, whose stay lapsed 09-08 without
   a published outcome. **The EU null is untouched.**
2. **Class-4 statement by a senior operator at a tracked firm about the marketing function: NO.** The sweep returned
   only material already held and already cited: Conlan→Chen (CoinDesk 2026-05-12 + the CoinGape Chen interview,
   both in Chapters 2 and 3) and Kalifowitz. The one non-held candidate is the Bitget CMO interview
   (crypto.news), **rejected on cohort grounds for the second time** — Bitget is perimeter, not tracked — so not
   fetched and not entered. Nothing net-new.
3. **2026 marketing-team layoff with a stated rationale: NO.** Every candidate the sweep surfaced is already a row
   in `corpus/layoff-tracker/2026-layoff-tracker.csv`, checked by direct grep rather than by memory: **Luno**
   (perimeter, −20% Bloomberg-reported, CEO said *automation* not *AI*, added 07-30), **BitMEX / HDR Global**
   (perimeter, full wind-down effective **2026-09-23**, added 07-24), **Crypto.com** (−12%, AI-framed),
   **Gemini** (−25%, SEC-filed). **Not one names marketing as the function.** The one row that names marketing —
   Gnosis — is perimeter and rests on an X hiring-referral post, exactly as the tracker already bounds it. Theme 5's
   headline thesis is unmoved.

**Watch items (POST-WINDOW — recorded, not admitted).**

- The **">7,254 disclosed job cuts across 47 companies"** aggregator figure resurfaced a **seventh** time, again
  with the ">7,000" headline variant and the "894 across twelve companies in July" sibling. Non-admission stands:
  aggregator arithmetic against an unstated base is not a primary figure. Entered nowhere.
- **BitMEX cessation effective 2026-09-23** — eight days after publication. Already a tracker row; perimeter; a
  wind-down, not a marketing cut. Noted only so a later reader does not mistake it for a missed event. **Not a
  report change and not a reason to touch the frozen bundle.**
- **FCA v Huobi — SPENT.** The next and last look at that page is Jukka's, on the morning of 15 September, per
  `PUBLISH.md` check 1. Chapter 7's `[VERIFY]` tag stays deliberately open until then.

**Inbound nominations:** the Friday duty; today is Wednesday. Not due, not checked.

**Re-date side duty:** closed since 09-02 (applied to all three public surfaces, live-verified). Nothing owed.

---

## Bundle state — re-verified, unchanged

Checked by recomputing both hashes this run rather than restating yesterday's:

| artefact | state |
|---|---|
| `report/state-of-crypto-marketing-2026.md` | 23,070 words ≈ **21.0pp** of a 25pp budget |
| provenance gate | **250 URLs / 0 untraced** |
| `publish-bundle/report.html` | 176 live citation links · sha256 `07cbfd25…638a9bc0` — **matches the frozen tripwire value** |
| `publish-bundle/report.pdf` | 44pp A4 (WeasyPrint) · sha256 `fe651b02…0dedb9ef38` — **matches the frozen tripwire value** |
| `publish-bundle/PUBLISH.md` | unchanged this run (no Changelog line owed — no check was scheduled) |

No file in `findings/`, `report/` or `publish-bundle/` was touched by this run.

---

## What Jukka has to do

Nothing new from this loop. **No new needs-jukka row was filed and none is owed** — the standing ask is the
existing 2026-09-02 row: **PUBLISH on 15 September, bundle at `publish-bundle/`, steps in `PUBLISH.md`**, verified
still OPEN this run. Two further SoCM rows filed 09-08 by the network/funnel session (the single-post exception and
the seven Tier-1 pre-publication notes) are **Jukka's decisions and another lane's work — this loop neither owns
nor touches them, and does not re-escalate them.**

Runs 09-10 → 09-14 are STEP 0 plus one line each. On 09-15 Jukka does the three morning-of checks and the
three-step publish; this loop then retires and the register continues as NorthPoint research Lane H.

**Sources opened this run:** search-level only. No candidate cleared the admissibility bar to justify a fetch —
every drop-everything candidate was either already held in the corpus (checked by grep against the tracker and the
findings tree) or rejected on cohort grounds before fetching. **No secondary source was permitted to add a fact.**
