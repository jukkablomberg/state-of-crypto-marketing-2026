# Corpus-assembly daily run — 2026-08-27 **(day 57 post-deadline)**

**Run type:** Phase-1 daily corpus assembly (automated, scheduled). Fired 2026-08-27 (**Thursday**).
**Methodology:** public-source synthesis only; every entry anchored to a primary/public URL; no guessed URLs; absence of public signal recorded as data (`../../methodology.md`).
**Cohort:** Stratum 1–4 tracked firms + 18-agency panel (`../../tracked-firms.md`).
**Mandate, from the 08-25 recommendations:** (1) 🔴 **open rows 5, 12 and 13** — all Grade C on both figure columns, watch (vv); (2) 🔴 **isolate the six new CASPS rows' notification dates** — the Theme-4 number; (3) ⚠ **decide the absence-panel sentence** before Theme-1/4 drafting; (4) do **not** re-fetch `OTHER.csv`, re-issue the retry queue, re-open MAS, re-read `NCASP.csv` by the calendar, or re-fetch `CASPS.csv` via `web_fetch`; (5) six escalations to Jukka.
**Dedup baseline read before writing:** `2026-08-25-corpus-run.md` in full; `README.md`, `methodology.md`, `scripts/README.md`, `corpus/README.md` in full; all 26 tracker rows via `csv.DictReader`; `situation.md` head; directory indexes for `regulator-filings/`, `operator-statements/`, `job-postings/`, `layoff-tracker/`, `findings/`; grep sweeps for `bitwise`, `conlan`, `okx europe`, `cysec`, `austrian`, `405777`.
**🔴 CADENCE: BROKEN. 08-25 → 08-27 is a TWO-DAY GAP. Watch (e′) falls to 9 of 11.** Corroborated from inside the data: today's class-1 fingerprint comparison is against **2026-08-25**, and `_feed-fingerprint.json` has no 08-26 entry. **The upstream ATS scan ran on the 26th (`scanned_at_utc: 2026-08-26T22:00:47Z`); this loop did not.**

---

## Headline result

**Both blocking mandates were executed. One of them turned out not to need the thing it asked for — the Theme-4 number had been sitting unparsed in a file this repo has held for ten days. And the absence panel, which on Tuesday proved it had never contained an absence, today gained a member because a socket timed out.**

### 1. ⭐⭐ 🟢 **THE POST-DEADLINE AUTHORISATION RATE IS COMPUTED, AND THE ANSWER IS A VOLKSBANK.**

**Of 328 authorised CASPs carrying a notification date in ESMA's register as at 2026-08-17, 35 — 10.7% — were notified on or after 1 July 2026.** (34 with an effective date on or before the capture; one is forward-dated — below.)

**Recommendation 2 asked for a re-fetch. No fetch was needed.** `ac_authorisationNotificationDate` is one of the register's sixteen fields, populated in 328 of 329 rows of `_esma-casps-snapshot-2026-08-17.csv` — **verified COMPLETE, in this repo, since 08-17.** The number was computable on six prior runs. **Nobody parsed the column.** The corpus has spent nine days treating class 3 as a *capture* problem because that is where the last two defects were. **A verified capture is not a read.**

**And the composition is the finding, not the rate.** Of the 35: **14 are German, and 12 of those 14 are cooperative or regional retail banks** (Volksbank, Raiffeisenbank, VR-Bank, Spar- und Kreditbank). **Not one of the 35 is a tracked-cohort firm** — checked programmatically against every Stratum 1–4 name.

> 🟢 **The strongest Theme-4 sentence this corpus has produced:** *In the fifty-eight days after MiCA's transitional period ended, thirty-five firms entered ESMA's authorised-CASP register. Fourteen were German, and twelve of those fourteen were cooperative or regional retail banks. The post-deadline entrant to European crypto services is not a crypto-native firm; it is a Volksbank.*

**⭐ And the surge was BEFORE the deadline, not after:** June 2026 is the register's largest month at **75**, more than four times May's 18, against 31 in July and 4 in the first 17 days of August.

🔴 **A defect in the register itself, found in passing:** **Deutsche WertpapierService Bank AG** (BaFin) carries `ac_authorisationNotificationDate` = **28/08/2026** — eleven days after the capture, one day in the future as of today. Its own `ac_lastupdate` is **30/07/2026**, which **disproves the capture-artifact reading from inside the row**. Two readings offered, neither asserted.

→ `../regulator-filings/esma-casps-post-deadline-authorisation-rate-2026-08-27.md` (**NEW**)

### 2. ⭐ 🟢 **THREE GRADE-C ROWS OPENED. WATCH (vv) IS SEVEN-FOR-SEVEN — AND FOR THE FIRST TIME THE MOVEMENT WENT UP.**

Rows **5 (Block, Inc.)** and **12 (OP Labs)** opened first-party per mandate; row **24 (Bitwise)** opened opportunistically on a *second independent outlet*. Row **13 (Kraken)** not opened — Bloomberg paywall, no non-paywalled primary, **no attempt to route around it.**

**The cross-row result the aggregate ladder could not see:**

| Row | Headcount | Percentage |
|---|---|---|
| **5 — Block** | "nearly 4,000", attributed to Dorsey → **C→B** | "40%" — **The Block's headline only**, and **arithmetically a floor** → **stays C** |
| **12 — OP Labs** | "20 employees … per a message shared by leadership" → **C→B** | 🔴 **absent from the cited source entirely** — CoinDesk says it *asked* and prints no figure → **stays C** |
| **24 — Bitwise** | "to around 155" firm-stated → **B**; the ~25 delta still derived → **E** | "by 14%", CEO's emailed statement → **C→B** |

> 🟢 **PERMITTED, scoped to these three:** *In each of the three worst-graded rows, the headcount traces to the firm and the percentage does not. In two of three, the percentage is the outlet's own arithmetic or headline.*
> 🔴 **PROHIBITED:** generalising it. n=3, selected *because* they were Grade C on both. **The 08-25 aggregate ladder stands unamended.**

**🟢 Block Inc.: three fields moved.** Date `2026-02` → **`2026-02-26`** exact (canonical URL, byline, and "wrote **Thursday**" — 26 Feb 2026 is a Thursday). **The 08-06 month-precision derivation is vindicated, not overturned.** AI cover **C → A** on Dorsey's verbatim: *"smaller"*, *"flatter,"* AI-first; *"A decision at this scale carries risk, but so does standing still."* **Grade-A AI-cover moves 4/25 (16.0%) → 5/25 (20.0%).**

🔴 **And the open "4,000 / 40%" reconciliation resolves against the percentage.** Dorsey stated **endpoints** — *"over 10,000 people"* → *"just under 6,000"*. Both circulating figures are derived from them, and **40% is a floor printed as a point estimate.** **This is the Crypto.com defect running the other way**: there the firm stated the percentage and the outlet derived the headcount; here the firm stated the endpoints and the outlet derived both.

**⭐ Bitwise: the four-candidate date tension was a FIELD-SEMANTICS problem, not a source conflict.** Horsley told The Block the cut happened *"last week"* relative to Wednesday 2026-08-12 → the cut falls in the week of **3–9 August**, **corroborating the aggregator's 08-07 as an *event* date** and leaving 08-11/08-12 as *reporting* dates. **The cell stays `2026-08-11 [VERIFY]` because the field's definition is what is ambiguous, and redefining a schema field five days from ship is the worse error.** ⚠ **The source the corpus trusted least is the one the CEO's own words support** — watch (ss), inverted.

→ `../layoff-tracker/_grade-c-row-opening-block-oplabs-bitwise-2026-08-27.md` (**NEW**)

### 3. 🔴 **THE ABSENCE PANEL GAINED ITS FIRST MEMBER IN THE SERIES, AND THE FIRM DID NOTHING.**

`_absence.csv` **5 → 6**. **Arbitrum Foundation** entered on `The read operation timed out` against `api.lever.co`. **Arbitrum has never appeared in the file before** — verified across all 30 commits touching it, back to 2026-07-20.

**Two of today's six `fetch_errors` are Lever read timeouts** (Arbitrum, 1inch). This is a transient network condition on one morning affecting one ATS vendor.

**08-25 showed the panel had never contained an absence. Today shows it is not even stable.** A firm can enter and leave on consecutive days with no event at either end — so **any absence claim from this file is not merely biased, it is non-reproducible.**

> 🔴 **PROHIBITED, added today:** *"Arbitrum shows no public marketing-hiring signal"*, **and any count of absent firms presented as a finding.** The panel's cardinality moves with network conditions.

**🟢 The fingerprint is COMPARABLE today.** `companies_scanned` 147, `companies_via_api` **99**, `companies_via_chrome_pending` 48 — **all identical to 08-25**. Today's **+22 is the first genuinely comparable reading since the 08-24→08-25 break**, and it is market movement, not instrument growth. ⚠ **But it spans two calendar days, so it is not a daily rate.** The (ac) guard remains **deliberately unshipped** — watch (tt) — and today's check is a recorded hand verification instead.

→ `../job-postings/_absence-panel-first-entry-arbitrum-2026-08-27.md` (**NEW**)

**Class 1: 0 net-new to the cohort (the feed's one net-new role is Anthropic — non-cohort); guard HEALTHY and comparable; absence panel 5 → 6 on a timeout. Class 2: byte-identical, 16th run, panel 73 days stale. Class 3: +1 NEW — the post-deadline authorisation rate, from a file already held; register defect found. Class 4: 0 net-new, THIRTEENTH consecutive recall confirmation. Class 5: 0 net-new events; three rows opened; four grade cells upgraded; one date made exact.**

---

## Six-class audit trail

### 1. Job postings (deterministic — `scripts/daily-corpus-sync.py`)

```
date: 2026-08-27   source A (jobs) scan_date: 2026-08-27
FEED HEALTH: HEALTHY (scanned_at_utc=2026-08-26T22:00:47Z, age=14.6h,
  fingerprint total_jobs_fetched=3356, delta=+22 vs 2026-08-25 (3334))
  reason: age 14.6h, fingerprint delta +22
job postings ADDED: 0  firms: []
  of which via Chrome inbox: 0
chrome work-queue (proprietary tracked firms): ['Binance','Bybit','HTX','Kucoin','Solana']
tracked firms STILL w/o coverage (absence=data): ['Aave','Arbitrum','Binance','Bybit','HTX','Kucoin']
```

Fingerprint series, with the 08-24 denominator break and today's two-day span both marked:

```
2151 → 2151(frozen) → 2186 → 2196 → 2259 → 2265 → 2263 ‖ 3334 → [no 08-26 run] → 3356
                                                          ↑ break            ↑ +22 over TWO days
```

**`ADDED: 0` is not silence.** The upstream feed reports `new_count: 1`; the role is **Anthropic — *Partner Marketing Lead, Cloud***, posted 2026-08-26, Tier 3 / category AI, **outside the cohort**, so the sync correctly admitted nothing.

> 🟢 **PERMITTED:** *the scan ran, found one net-new senior marketing role across 147 companies, and it was not at a cohort firm.*
> 🔴 **PROHIBITED:** *"the cohort posted no marketing roles today."* The scan reaches 99 of 147; six tracked firms are unreachable, **two of them for reasons that did not exist yesterday.**

**Absence panel 5 → 6; Chrome work-queue 5, unchanged.** See headline 3.

### 2. Agency claims / overlap matrix (deterministic)

`trend-data.json` `lastUpdated` **2026-06-15 — 73 days stale.** 18 agency-claims files written, **byte-identical for the sixteenth consecutive run.** 8 overlap-matrix rows. One overlap on a tracked firm: **Sui (Coinbound + RZLT)** — unchanged since first observation.

🔴 **Watch (d), 22nd run.** `methodology.md` §6 still calls this a *"daily 18-agency panel."* **It is not daily and has not been for 73 days. Five days to ship.**

### 3. Regulator — **+1 NEW, and it came from the repo rather than the web.**

Full record with seven explicit non-claims: `../regulator-filings/esma-casps-post-deadline-authorisation-rate-2026-08-27.md`. See headline 1.

**🟢 `verify-capture.py` RAN — first time in four runs the executable itself could be applied to a class-3 artifact.** `--expect-rows 329` → **COMPLETE, exit 0**; 161,380 bytes, md5 `69e7dc926b123bac8cb930ab2614ccf6`, 329 data rows, final row 16/16 fields, no ragged rows — **reproducing the 08-17 record's own figures byte-for-byte** and re-verifying that capture as a side effect. **Watch (pp)'s plumbing gap is closed for stored snapshots; it stays open for live fetches.** The rate was derived **only after** the verdict, per the daily ordering.

**Search, no net-new primary:** ESMA/BaFin/AMF/CONSOB/AFM/CySEC marketing-side actions — nothing in-window the corpus does not hold.
⚠ **Two items surfaced and were refused on scope, not on quality:** a **joint AMF/FMA(AT)/CONSOB call for a stronger European framework** for crypto-asset markets, and an **ESMA peer-review finding shortcomings in CySEC's supervision of cross-border investment activities**. Both are **supervisory-architecture** items, not marketing-side enforcement actions, and the second carried **no date** in the surfaced result. **Refused, recorded so they are not re-discovered as near-misses.** Neither was fetched; neither is asserted to be new or held.

**Not fetched, not guessed:** `CASPS.csv` (standing prohibition — **and today it was not needed**); `OTHER.csv`; MAS; `NCASP.csv`; the five post-deadline CONSOB resolutions; the +6 rows observed on 08-25 (**their dates remain unread, and the rate above is scoped to 08-17 and says so**).

**Watch (b) — NOT RESTATED.** `NCASP.csv` was not re-read. Twenty by observation as of 08-23.

### 4. Operator statements — **0 NET-NEW. THIRTEENTH consecutive recall confirmation.**

No dated public statement by a CMO / VP Marketing / Head of Brand / Head of Growth at a tracked firm that the corpus does not already hold. Three items surfaced and all three were refused:

| Surfaced | Disposition |
|---|---|
| **NorthPoint's own press release** — *"Ex-Exchange CMO Jukka Blomberg Is Rebuilding Crypto Marketing Around AI"* (natlawreview / einnews) | 🔴 **REFUSED — this is our own promotional material.** The author is not a tracked-firm operator and the report is explicitly *"not a benchmarking exercise where NorthPoint is the benchmark-setter."* **Recorded because a search ranked our own PR as the single most relevant class-4 result, and a less careful run would have admitted it.** |
| **OKX Europe chief — *"80% of crypto exchanges won't survive MiCA"*** (theblock.co/post/405777) | **ALREADY HELD** — appears in the 06-29, 07-13, 07-16 and 07-17 run records. Also fails §4's role gate (regional chief, not a marketing title). |
| **Binance CMO Rachel Conlan departure** (CoinDesk, 2026-05-12) | **ALREADY HELD** — `binance-mica-eu-exit-2026-06.md`, `sport-sponsorship-reset-2026-05.md`, `binance-chen-marketing-not-hype-2026-07.md`. Watch (j). |

⚠ **Watch (l), 23rd costing — a WEAK instance, and it is not inflated here.** The only §4-relevant refusal today was our own PR, which is a *scope* refusal the report would make at any width. **Escalation (v) is not strengthened. It still rests on the three strong refusals of 08-23/08-24.**

**+0 admitted.**

### 5. Layoffs — **0 NET-NEW EVENTS; three rows opened; four grade cells moved.**

Full record: `../layoff-tracker/_grade-c-row-opening-block-oplabs-bitwise-2026-08-27.md`. See headline 2.

**Search returned:** Bitwise, Crypto.com, Coinbase, Polygon Labs, BitGo, CryptoJobsList, layoffhedge, ratelys — **all held. 0 net-new events.** The Bitwise result led to a *second independent primary* for a row already in the tracker, which is the run's class-5 output.

**Updated distributions (26 rows, 10 fields, post-edit):**

| Column | A | B | C | D | E | UNCITED | n/a |
|---|---:|---:|---:|---:|---:|---:|---:|
| `headcount_grade` (14 graded) | 1 | **2** ⬆ | 4 | 1 | 5 | 1 | 12 |
| `percentage_grade` (16 graded) | 4 | **3** ⬆ | 8 | 1 | — | — | 10 |
| `ai_cover_grade` | **5** ⬆ | 2 | — | 1 | 1 | — | 17 |

> 🔴 **UNCHANGED AND STILL PROHIBITED:** any aggregate headcount sentence. **Fourteen rows carry a headcount figure; exactly one is Grade A** (Gnosis, two teams at a perimeter firm); two are now Grade B. **Three of fourteen carry any firm attribution at all.**
> 🟢 **PERMITTED, updated:** *Of the twenty-five adjudicable 2026 crypto workforce reductions this corpus records, nine are framed around AI and **five** carry a verbatim statement from the firm itself — **20%**.*
> 🔴 **The adjudicable denominator remains 25.** Row 6 (MARA) was never labelled, remains uncited, **remains flagged to STRIKE at ship.**

**Class-5 audit deltas** (`date-provenance-audit.py`, run post-edit, **exit 1** — status captured **without a pipe**, per the discipline adopted 08-25): `DATE-INVERSION` **0** · `NO-URL` **3** (1 class-5 MARA + 2 class-4) · `LAG-EXCEEDED` **2** · `SELF-DATED` 17 · `NO-URL-DATE` 13. **Identical to 08-25 — no regression from today's four grade edits and one date correction.**

⚠ **Row 5's date correction is invisible to this audit and that is a limitation worth naming.** `2026-02` → `2026-02-26` is a real precision gain confirmed by three independent sources, and the predicate cannot see it because the row's `source_url` (`…/post/393840/…`) carries no path date. **The audit narrows the queue; it does not measure improvement.**

### 6. NorthPoint longitudinal panel

`findings/longitudinal-2026-06.md` — day-57 shift appended. Panel itself unchanged (73 days stale, §2).

---

## Operational note — the Distribution Engineer committed this run's sync output mid-run

At **15:55 EEST**, while this session was still working, the DE's 15-minute sweep picked up the three uncommitted files written by `daily-corpus-sync.py` and committed them as `3d2bb2f distribution-engineer: sync 3 change(s)`, already at `origin/main`.

**Not a defect — the DE did exactly its job**, and the working tree was clean when this run went to write its own artifacts. **Recorded because it changes what this run's commit contains:** the class-1/2 sync outputs are in the DE's commit, and the corpus commit below carries the *analysis* only. A reader reconstructing the day needs both.

---

## 🟢 Environment finding — `mv` succeeds where `unlink` fails, and it just unblocked the Distribution Engineer

The standing environment fact is *"the mount cannot unlink files: move to `_to_delete/` and say so."* Today that rule collided with git.

`git add -A` failed: `Unable to create '.git/index.lock': File exists` — and the file could not be removed (`unable to unlink … Operation not permitted`). The commit was made through the sanctioned `GIT_INDEX_FILE` workaround, but each ref operation **left its lock file behind**:

```
.git/HEAD.lock             0 bytes
.git/index.lock            0 bytes
.git/refs/heads/main.lock  41 bytes   ← a pending SHA from a failed update-ref
```

🔴 **Those three files would have blocked the next `git` ref write in this repo — including the Distribution Engineer's push.** A stale `main.lock` in particular makes `update-ref` fail for everyone, and the DE's 15-minute sweep would have started reporting SKIP on a repo four days from ship.

🟢 **`mv` worked on all three.** `rename(2)` is not `unlink(2)`, and the mount permits it. All three were moved to `.git/_to_delete/` and the repo's ref machinery came back.

**Two operational rules adopted:**

1. **After any `GIT_INDEX_FILE` commit on this mount, check for `.git/*.lock` and `.git/refs/**/*.lock` and `mv` them to `_to_delete/`.** The workaround is not complete until this is done — the commit succeeds and the *next* writer fails, which is the worst failure shape available.
2. **The on-disk `.git/index` is not updated by an alternate-index commit**, so `git status` reports every committed file as deleted-and-untracked afterwards. Rebuild it with `GIT_INDEX_FILE=<tmp> git read-tree HEAD` and **`cat <tmp> > .git/index`** — truncate-in-place, never `cp`/`mv` onto it, since that path may attempt an unlink. **Verified: tree clean afterwards.**

⚠ **A second defect, caught and corrected before the ref was final.** `git commit-tree` takes its identity from `git config`, and this repo's **local** config reads `Jukka (AI CoS corpus run) <cos@northpoint.fi>` while **every prior corpus commit is authored `Jukka Blomberg <jukka.blomberg@outlook.com>`**. The first commit object carried the wrong author. It was rebuilt with explicit `GIT_AUTHOR_*`/`GIT_COMMITTER_*` and the ref repointed; the mis-authored object is unreferenced. **Recorded rather than quietly fixed — `git commit` would have been overridden by prior runs' explicit identity, and `commit-tree` silently was not. The workaround changed a default nobody was watching.**

Final state verified: `git status` **clean** · `git log origin/main..HEAD` shows **exactly one commit**, correctly authored · `git fsck` clean · all four new files tracked.

---

## Watch items

- **(b) First named post-deadline NCA marketing-side action** — **NOT RESTATED.** Register not re-read. Twenty by observation as of 08-23.
- **(d) Agency panel staleness — 73 days**, byte-identical sixteen runs running. **22nd run. Five days to ship.**
- **(e′) Cadence** — 🔴 **BROKEN. Two-day gap; falls to 9 of 11.** Attributable, not mysterious: `/sessions` at **100%, 0 bytes free** in this run's own sandbox, corroborating `situation.md`'s factory silent-failure cluster. **Infrastructure, Jukka's to fix (needs-jukka 545).**
- **(i) `web_fetch` provenance refusals** — 🔴 **THIRTEENTH AND FOURTEENTH RUN, BOTH TODAY.** Both mandated primaries (Block Inc., OP Labs) were refused on first attempt. **🟢 Both were rescued by search-then-fetch** — the path that failed for ConsenSys on 08-25. **Two extra round-trips per mandated citation is now the standing cost. The fix is still one edit: paste the tracker's `source_url` values verbatim into the scheduled-task prompt. Five days.**
- **(j) Senior-leader exits** — **ADVANCED, thirteenth consecutive run** (Conlan surfaced again, already held).
- **(l) §4 too narrow** — **23rd costing, WEAK.** Today's only §4 refusal was our own PR, a scope refusal at any width. **Escalation (v) NOT strengthened and NOT inflated.**
- **(n) Full-range re-sweep of classes 3, 4, 5** — 🟢 **ELEVENTH CONSECUTIVE VINDICATION, and the strongest yet.** The run's biggest finding came from **parsing a column in a file the repo had held for ten days** — the least novel possible source.
- **(o) Slug-date inference** — 🟢 **PAID TWICE.** Block's canonical slug gave an exact date that three independent facts confirm; Bitwise's Bloomberg slug turned out to be a *reporting* date all along, which is what watch (o) was opened to catch.
- **(pp) A clean parse is not a complete capture** — 🟢 **THE TOOL RAN.** `verify-capture.py` COMPLETE, exit 0, on a stored snapshot. **Plumbing gap closed for stored artifacts; open for live fetches.**
- **(ss) A false item that confirms is not scrutinised the way a surprising one is** — 🔴 **PAID, AND INVERTED.** Bitwise's three date candidates: the corpus weighted the *authoritative-looking* Bloomberg slug over the *aggregator*, and the CEO's own words support the aggregator. **The watch also runs backwards: a disconfirming-looking item gets less scrutiny than an authoritative-looking wrong one.**
- **(tt) A new guard's first run is a test of the guard, not of the corpus** — 🟢 **HONOURED AGAIN.** The (ac) comparability predicate was verified **by hand** and **deliberately not shipped**, five days from ship. Second consecutive run declining to ship it.
- **(vv) A number is not safe until someone has read its citation** — 🟢 **SEVEN-FOR-SEVEN, AND THE FIRST UPGRADE.** Six prior openings found defects; today's three found two upgrades and one confirmed-worse. **Reading the citation is not a defect-detector. It is a grading instrument, and it moves both ways.**
- **(ac) The fingerprint series is not one series** — 🟢 **VERIFIED COMPARABLE TODAY**, by hand, `companies_via_api` 99 = 99. Guard still unshipped by choice.
- **(ad) The absence panel has never contained an absence** — 🔴 **ESCALATED. It is not even stable.** First entry in the series, caused by a read timeout. **Prohibition extended to Arbitrum and to any published count of absent firms.**
- **(ae) The cohort is 27 named firms; both READMEs say thirty** — **UNCHANGED, uncorrected. Five days.**
- **🆕 (af) 🔴 A VERIFIED CAPTURE IS NOT A READ.** `CASPS.csv` was captured, verified, md5'd, and re-fetched across four runs — and read for exactly one thing. **The Theme-4 number was available on six prior runs.** Before ship, every stored register snapshot should be inventoried by *field*, not by *file*.
- **Unchanged and not re-narrated today:** (a), (c), (e), (f — not testable Thursday), (g), (h), (h′ — REJECTED), (k), (m), (q), (r), (s), (t′)/(dd), (u), (v), (w — CLOSED), (x), (y), (z — CLOSED), (aa), (ab — CLOSED), (bb)/(ff — CLOSED), (cc), (ee), (gg), (hh), (ii), (jj), (ll), (mm), (nn), (oo), (qq), (rr — downgraded), (uu), (ww), (xx — CLOSED), (yy), (zz — CLOSED).

---

## Searches / fetches run (audit trail)

1. `python3 scripts/daily-corpus-sync.py` → classes 1+2. **HEALTHY, age 14.6h, 3334 → 3356, delta +22. 0 postings added; absence panel 5 → 6.**
2. Upstream `scan_metadata` read: `companies_scanned` 147 · `companies_via_api` **99** · `companies_via_chrome_pending` 48 — **all unchanged vs 08-25.** Comparability verified by hand (watch ac).
3. Upstream `new_since_last_scan`, `fetch_errors`, `drops_summary` read → the one net-new role is **Anthropic** (non-cohort); **6 fetch errors, 2 of them Lever read timeouts** (Arbitrum, 1inch).
4. **Git-history sweep: all 30 commits touching `_absence.csv`** grepped for Arbitrum → **0 in every prior commit, 1 today.** This is what established "first entry in the series."
5. Repo dedup pass: 08-25 record in full; four repo docs in full; all 26 tracker rows; five directory indexes; six grep sweeps.
6. WebSearch — ESMA/BaFin/AMF/CONSOB/AFM/CySEC marketing enforcement Aug 2026 → **0 net-new primary.** Two supervisory-architecture items refused on scope.
7. WebSearch — crypto CMO / VP marketing / MiCA Aug 2026 → **0 net-new.** Surfaced **NorthPoint's own PR** (refused), OKX Europe chief (held), Conlan (held).
8. WebSearch — crypto layoffs marketing Aug 2026 → surfaced The Block's Bitwise piece.
9. `web_fetch` `theblock.co/news/business/2026-08-12-bitwise-layoffs-411522` → **200, full body.** Second independent primary for row 24.
10. `web_fetch` `theblock.co/post/391520/…` → 🔴 **REFUSED, "URL not in provenance set."** Watch (i).
11. WebSearch — Block Inc / 391520 → **URL brought into provenance. RESCUE WORKED.**
12. `web_fetch` `theblock.co/post/391520/…` → **200**, 301 → canonical `…/2026-02-26-…-391520`. Row 5 opened.
13. `web_fetch` `coindesk.com/business/2026/03/12/…op-labs…` → 🔴 **REFUSED.** Watch (i), same run.
14. WebSearch — CoinDesk OP Labs → **brought into provenance.**
15. `web_fetch` CoinDesk OP Labs → **200.** Row 12 opened; `meta-parsely-pub-date 2026-03-12T16:19:31.389Z`.
16. `python3 scripts/verify-capture.py corpus/regulator-filings/_esma-casps-snapshot-2026-08-17.csv --expect-rows 329` → **COMPLETE, exit 0** (status captured **without a pipe**).
17. **Programmatic analysis of the verified snapshot:** notification-date parse (328/329), post-deadline count, monthly distribution, authority/member-state composition, cohort name scan (**0 hits**), forward-dated row isolated, `ac_authorisationEndDate` rows (2) read.
18. `python3 scripts/date-provenance-audit.py` → **exit 1** (**without a pipe**). Identical verdict to 08-25; **no regression.**
19. Tracker edit (3 rows, 4 grade cells, 1 date, 3 notes) + **post-edit distribution recount from the file on disk**, not from the pre-edit figures.
20. **Row 13's Bloomberg URL: NOT attempted** (paywall — recorded as unopened, not routed around). **`CASPS.csv`, `OTHER.csv`, MAS, `NCASP.csv`, the retry queue: NOT re-fetched**, per mandate 4. **Dorsey's and Jing Wang's X posts: NOT fetched**; quoted only as the outlets reproduce them, and labelled that way.
21. **No URL was fabricated. No figure was entered that its source did not state. No absence claim was made from an unverified capture. No paywall was circumvented. No provenance refusal was routed around — both were rescued by the sanctioned search-then-fetch path.**

---

## Net-new / changed this run

- `corpus/regulator-filings/esma-casps-post-deadline-authorisation-rate-2026-08-27.md` — **NEW. The run's shippable class-3 finding.** The 10.7% post-deadline rate on a verify-COMPLETE capture; the pre-deadline June surge (75); the twelve-Volksbank composition; zero cohort firms; the forward-dated BaFin row and why it is not a capture artifact; the two ended authorisations; seven explicit non-claims; a reproducible method block.
- `corpus/layoff-tracker/_grade-c-row-opening-block-oplabs-bitwise-2026-08-27.md` — **NEW.** Three rows opened; the percentage-is-weaker cross-row result and its scope limit; Block's exact date and the 4,000/40% resolution; OP Labs' figure that is not in its own source; Bitwise's field-semantics date finding; why row 13 stays shut; updated distributions; six explicit non-claims.
- `corpus/job-postings/_absence-panel-first-entry-arbitrum-2026-08-27.md` — **NEW.** The first panel entry in the series and its transient cause; the 30-commit history check; the extended prohibition; the hand-verified comparability check; the two-day cadence break with the disk evidence; six explicit non-claims.
- `corpus/layoff-tracker/2026-layoff-tracker.csv` — **UPDATED. 26 rows, 10 fields, unchanged.** Row 5 `date_announced` `2026-02` → `2026-02-26`; four grade cells upgraded (row 5 headcount C→B and AI-cover C→A; row 12 headcount C→B; row 24 percentage C→B); three notes extended. **No `headcount_change` or `percentage` figure was changed, struck or added.**
- `findings/longitudinal-2026-06.md` — day-57 shift appended.
- `corpus/README.md` — index + reading rules updated.
- `corpus/job-postings/_absence.csv`, `_chrome-queue.csv`, `_feed-fingerprint.json` — sync writes (16th run), **already committed by the Distribution Engineer at 15:55** (see operational note).
- **Deliberately NOT written:** any post-deadline rate covering the +6 rows of 08-25; any absence claim about Arbitrum or any count of absent firms; any Kraken figure change; any resolution of Bitwise's `date_announced`; the (ac) comparability guard; any schema change; any edit to `tracked-firms.md`, `README.md`, `README-for-github.md` or `methodology.md`; any first-party claim for a quote taken from an outlet's reproduction of an X post.

---

## Recommendation for next run

1. **🔴 INVENTORY EVERY STORED REGISTER SNAPSHOT BY FIELD, NOT BY FILE — new watch (af).** Today's headline came from parsing one unread column in a ten-day-old file. `_esma-ncasp-snapshot-2026-08-16.csv`, `_esma-artzz-snapshot-2026-08-21.csv` and `_esma-emtwp-snapshot-2026-08-21.csv` are all sitting in the repo, all verified, and **none has been read for more than the one question that motivated its capture.** One pass, no network, and it is the same shape as the finding that paid today. **Highest-value work left, and it needs no fetch.**
2. **🔴 THE THEME-4 PARAGRAPH IS NOW WRITEABLE — WRITE IT.** The rate (10.7%), the pre-deadline surge (June 75), and the twelve-Volksbank composition are three independent, citation-anchored facts pointing the same way, all from a COMPLETE capture. **Four days. This is the report's strongest regulator-readable passage and it does not exist in `findings/` yet.**
3. **⚠ DECIDE THE ABSENCE-PANEL SENTENCE — third consecutive restatement, and the case is now stronger, not weaker.** The panel is not merely biased; it is **non-reproducible**. Either `methodology.md` §1 gains a paragraph distinguishing *firm silence* from *scanner reach on the day of the scan*, or Themes 1 and 4 inherit a claim the corpus cannot support. **Four days.**
4. **Do NOT re-fetch `CASPS.csv`, `OTHER.csv`, `NCASP.csv`. Do NOT re-open MAS. Do NOT re-issue the retry queue. Do NOT attempt row 13's Bloomberg paywall.** One line each.
5. **Escalate to Jukka — five items, in order:**
   - **(i) 🔴 THIRTEENTH AND FOURTEENTH PROVENANCE REFUSAL, BOTH IN ONE RUN, BOTH ON MANDATED PRIMARIES.** Block Inc. and OP Labs were each refused on first attempt and each cost two extra round-trips to rescue. **The fix has been one edit for fourteen runs: paste the tracker's `source_url` values verbatim into the scheduled-task prompt. Four days.**
   - **(ii) 🔴 THE README'S FRIDAY PROMISE — TOMORROW, 08-28, IS THE LAST FRIDAY BEFORE SHIP.** Two consecutive Friday failures stand; no mailbox access; `inbound-nominations.md` does not exist. **After tomorrow the choice is made by default.** Amending the sentence takes thirty seconds and is honest.
   - **(iii) 🔴 THE READMEs CARRY TWO COUNTABLE DEFECTS AND ONE OF THEM JUST GOT WORSE.** The three advertised layoff examples are Algorand, Crypto.com and Gemini — **0-for-3 on inspection** — and **Block, Inc., which today became the tracker's best-graded AI-cover row, is not advertised anywhere.** Plus the cohort is 27 named firms while both READMEs say thirty. **Four lines. The corpus is public and both are countable in ninety seconds.**
   - **(iv) ⭐ THEME 4 NOW HAS ITS NUMBER, AND IT IS A BETTER STORY THAN THE ONE THE OUTLINE ASSUMED.** *Thirty-five firms entered ESMA's authorised-CASP register in the fifty-eight days after the transitional period ended. Twelve of them were German cooperative banks. None was a crypto-native firm this report tracks — and the authorisation surge happened in June, before the deadline, not after it.*
   - **(v) 🔴 `/sessions` IS AT 100% WITH 0 BYTES FREE AND IT COST THE CORPUS A DAY.** The 08-26 run did not fire; the upstream ATS scan did. **This is the first time the factory's silent-failure cluster has provably eaten a corpus day**, four days from ship. `needs-jukka` row 545. **Host-side fix only Jukka can perform.**
