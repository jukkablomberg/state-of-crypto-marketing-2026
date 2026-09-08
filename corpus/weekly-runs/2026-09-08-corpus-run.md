# 2026-09-08 — corpus run (day 69, seventh full post-window day) — **FCA v HUOBI CHECK: NO CHANGE**

**KPI — 11 of 11 units done. Bundle FROZEN; publish 2026-09-15.** This run took the cadence's second and last
bounded exception, **(b) the 09-08 FCA v Huobi stay-expiry check**. The check was performed against the FCA's own
proceedings page. **Nothing new is published. No sentence in any chapter was changed, and no bundle artefact was
rebuilt.** From here the bundle is frozen with no scheduled exception remaining before Jukka publishes on 09-15.

**Not a FAILED run.** The unit ladder is complete (11 of 11 since 09-02) and the REMAINING RUNS row in
`synthesis-plan.md` binds this run to STEP 0 + the named exception + this record. The exception was executed to its
end — a primary source opened and read, an adjudication made — which is the unit of work this run owed.

---

## STEP -1 — system map

`python3 _meta/verify_system_map.py` → **exit 0, clean** (15 active loops · 10 retired · 34 edge artifacts · 39
prompt checks). No findings.

**E22 unchanged.** This loop is still the producer; the report is still the consumer; Jukka still publishes. No work
was assigned to any other loop, so no other loop's prompt needed editing. The repo was **level with `origin/main`**
before this run's commit (`git log origin/main..HEAD` empty); the DE shipped 09-07 as designed.

---

## THE JOB — exception (b): FCA v Huobi Global S.A. & Others, stay expiry

**Primary source opened:** `https://www.fca.org.uk/news/statements/htx-huobi-legal-proceedings` — the FCA's own
court-ordered publication page, fetched in full this run.

**What the page says today, read as a record rather than as a search snippet:**

| field | value as read 2026-09-08 |
|---|---|
| page `Last updated` | **26/08/2026** (also `meta-article:modified_time` `2026-08-26T10:34:02+01:00`) |
| last document in the Key documents list | **Order of Master Marsh dated 24 August 2026** — the consent order the report already cites |
| documents added since 24 August | **none** |
| `Page updates` log | last two entries 29/06/2026 and 02/04/2026 — nothing for September |
| settlement, discontinuance, judgment or further extension | **none published** |

**Adjudication: NO CHANGE. No outcome is published, so nothing in Chapters 5 or 7 is updated and the bundle is not
rebuilt.** The stay ran by consent to 8 September 2026 — today — and lapses on the public record without a published
outcome. That is the state the report already describes, in the past tense, without predicting an outcome: the
Chapter 5 sentence (the Master Marsh order, and the scoping caveat that the stay binds only the Claimant and the
First Defendant, not defendants 2–5) and the Chapter 7 sentence are both accurate as written on 09-15.

⚠ **The `[VERIFY]` tag in Chapter 7 — "re-check the FCA's own HTX/Huobi proceedings page on the morning of
publication and re-date this sentence" — is deliberately NOT cleared by this run.** Today's reading is seven days
before publication. A check performed a week early cannot discharge a check the report itself promises the reader
will be performed on the morning of publication. The tag is the report telling the truth about itself; clearing it
with a stale reading would make it a lie. `PUBLISH.md` morning-of check 1 already carries the same instruction and
the same URL, so the duty has a named holder (Jukka) and does not depend on this loop, which retires at publication.

**One 09-08-dated line was appended to `publish-bundle/PUBLISH.md`'s Changelog** recording that the scheduled check
ran and returned no change. **This is a note about the check, not an edit to the report**: no chapter, no
`report/state-of-crypto-marketing-2026.md`, no `report.html`, no `report.pdf`, and therefore **both frozen SHA-256
tripwire values in `PUBLISH.md` step 2 stand unchanged**. The choice is recorded here rather than left silent
because the freeze rule is otherwise absolute, and a reader of the bundle a week from now should not have to
wonder whether the 09-08 check was skipped or performed.

**Secondary material, read and not used.** The mid-August trade coverage of the settlement talks (Reuters-sourced
syndication) restates the March exchange of emails and the 25 June two-month extension — both already on the record
via the Chief Master Shuman order this corpus holds. It adds no fact and reports no outcome. **No secondary source
was permitted to speak for the FCA's own page.**

---

## STEP 0 — post-window corpus check

`python3 repo/scripts/daily-corpus-sync.py`. **Class-1 capture window CLOSED 2026-08-31 and honoured in code**
(`CAPTURE_WINDOW_END` untouched). `_absence.csv` and `_chrome-queue.csv` were **not** rewritten; their `as_of` stays
2026-08-31. Only `_feed-fingerprint.json` was written — an instrument log, not a corpus claim.

| class | net-new |
|---|---|
| 1 — job postings | **0 admitted** (window closed; 0 offered) |
| 2 — agency claims | **0** new relationships; 18 snapshot files written, 8 matrix rows, 1 tracked-firm overlap (Sui — Coinbound + RZLT); panel as-of **2026-06-15**, unchanged and not stale by Jukka's 07-10 Path-2 decision |
| 3 — regulator filings | **0** |
| 4 — operator statements | **0** |
| 5 — layoff tracker | **0** |
| 6 — campaigns | **0** |

**Feed health: HEALTHY.** `scanned_at_utc` 2026-09-07T21:46:00Z, **age 14.4 h** (limit 36 h),
`total_jobs_fetched` **3423, delta −35** vs 09-07's 3458. The `scan_metadata` cross-check guard **passes** — the feed
is moving, second consecutive healthy day after the 09-05/09-06 stall. **The delta is negative, and that is normal
and not a defect:** the fingerprint counts roles *open at the moment of the scan*, so a net −35 is postings closing
faster than they open, not a scanner failure. **No report consequence and no back-fill**: the class-1 exhibit is
frozen at 08-31 and neither a healthy nor a stale feed can now reach the report body. The five tracked firms still
without coverage (Aave, Binance, Bybit, HTX, KuCoin) remain a **live read only**, unchanged and unwritten.

**Drop-everything sweep — three explicit zeroes.**

1. **First named NCA marketing-side enforcement case: NO.** Unchanged from 09-03 → 09-07. What is published remains
   *supervisory practice and vendor commentary describing the regime* — NCAs sampling marketing communications
   against the Art. 7 / Art. 66 fair-clear-not-misleading standard, risk-warning prominence, finfluencer
   supervision, with information requests, inspections and authorisation suspension as available remedies. **No
   named case against a named CASP.** No addendum box is owed. Chapter 1's thesis holds for a 69th day — and note
   that the one *named* marketing enforcement action in this corpus is the FCA's, in a non-MiCA jurisdiction, whose
   stay lapsed today without a published outcome. **The EU null is untouched.**
2. **Class-4 statement by a senior operator at a tracked firm about the marketing function: NO.** The sweep returned
   only the Conlan→Chen and Kalifowitz material, both long held and cited. Nothing net-new.
3. **2026 marketing-team layoff with a stated rationale: NO.** The record is unchanged: whole-company cuts under
   AI-efficiency (Coinbase, Crypto.com), automation-and-B2B-pivot (Luno) or market-conditions rationales. **Not one
   names marketing as the function.** Theme 5's headline thesis is unmoved.

**Watch items (POST-WINDOW — recorded, not admitted).**

- The **">7,254 disclosed job cuts across 47 companies"** aggregator figure resurfaced a **sixth** time, again with
  a ">7,000" headline variant and a "894 across twelve companies in July" sibling. Non-admission stands: aggregator
  arithmetic against an unstated base is not a primary figure. Entered nowhere.
- **FCA v Huobi — the scheduled check is now SPENT.** Adjudicated above. The next and last look at this page is
  Jukka's, on the morning of 15 September, per `PUBLISH.md` check 1.

**Inbound nominations:** the Friday duty; today is Tuesday. Not due, not checked.

**Re-date side duty:** closed since 09-02. Nothing owed.

---

## Bundle state — unchanged

| artefact | state |
|---|---|
| `report/state-of-crypto-marketing-2026.md` | 23,070 words ≈ **21.0pp** of a 25pp budget |
| provenance gate | **250 URLs / 0 untraced** |
| `publish-bundle/report.html` | 176 live citation links · sha256 `07cbfd25…a9bc0` **unchanged** |
| `publish-bundle/report.pdf` | 44pp A4 (WeasyPrint) · sha256 `fe651b02…b9ef38` **unchanged** |
| `publish-bundle/PUBLISH.md` | one 09-08 Changelog line added (the check, not the report) |

No file in `findings/` or `report/` was touched by this run.

---

## What Jukka has to do

Nothing new. The single open ask is the existing row — **PUBLISH on 15 September, bundle ready at
`publish-bundle/`, steps in `PUBLISH.md`**. No second row was filed and none will be.

**The last scheduled change to this report has now come and gone without changing it.** Every remaining run
(09-09 → 09-14) is STEP 0 plus one line in a run record. On 09-15 Jukka does the three morning-of checks and the
three-step publish; this loop then retires and the register continues as NorthPoint research Lane H.

**Sources opened this run:** `https://www.fca.org.uk/news/statements/htx-huobi-legal-proceedings` (primary, full
fetch — the exception's named source). Search-level only otherwise; no other candidate cleared the admissibility
bar to justify a fetch.
