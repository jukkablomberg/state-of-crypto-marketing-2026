# 2026-09-03 — corpus run (day 64, second full post-window day)

**KPI — 11 of 11 units done. Bundle rebuilt and now FROZEN; publish 2026-09-15.** This run took the one bounded
exception the re-based cadence allows on 09-03 → 09-05: **the second-pass citation audit.** Ten narrowings shipped,
the report re-assembled and both bundle artefacts rebuilt. **Not a FAILED run** — a unit was advanced and committed.

**STEP -1.** `verify_system_map.py` exit 0, clean (15 active loops · 10 retired · 31 edge artifacts · 25 prompt
checks). E22 still names this loop as producer and Jukka as the publisher. No loop was assigned work.

---

## STEP 0 — post-window corpus check

`daily-corpus-sync.py`: **class-1 window CLOSED at 2026-08-31 and honoured in code.** `_absence.csv` and
`_chrome-queue.csv` were not rewritten; their `as_of` stays 08-31. Feed read and reported, nothing admitted.

| class | net-new |
|---|---|
| 1 — job postings | **0** (0 offered post-window, 0 admitted) |
| 2 — agency claims | **0** new relationships; 18 snapshot files written, 8 matrix rows, 1 tracked-firm overlap (Sui — Coinbound + RZLT), panel as-of **2026-06-15** unchanged |
| 3 — regulator filings | **0** |
| 4 — operator statements | **0** |
| 5 — layoff tracker | **0** |
| 6 — campaigns | **0** |

**FEED HEALTH: HEALTHY** — `scanned_at_utc` 2026-09-02T21:50:30Z (age 14.4 h), fingerprint `total_jobs_fetched`
3419, delta **+64** vs 09-02. The `scan_metadata` cross-check guard passed, so the five still-uncovered tracked
firms (Aave, Binance, Bybit, HTX, KuCoin) are a live read only and were **not** written to the shipped exhibit.

**Drop-everything sweep — three explicit zeroes.** No first named NCA marketing-side enforcement case (searched;
NCAs are still at the supervisory-review and spot-check stage, which is exactly Chapter 1's thesis). No class-4
statement by a senior operator at a tracked firm about the marketing function. No 2026 marketing-team layoff with a
stated rationale.

**Watch items (POST-WINDOW — recorded here, not admitted to the report body).**
- HDR Global Trading (BitMEX) announced 23 July it will cease trading operations 23 September 2026 after a strategic
  review. **Perimeter, not tracked; no marketing-function content.** Watch only.
- A third-party aggregator now counts "more than 7,254 disclosed job cuts across 47 companies" in 2026 and a Luno
  cut of "around 20%". Aggregator arithmetic against an unstated base — **not admissible** as a primary figure and
  not entered anywhere.

---

## THE UNIT — second-pass citation audit (bounded exception (a) of the re-based cadence)

The 09-02 content audit adjudicated 318 claims: 254 SUPPORTED, 30 PARTIAL, 25 CONTRADICTED (all fixed that day),
9 NOT OPENED. **The 25 contradictions were fixed; the 30 PARTIALs and 9 NOT-OPENEDs were adjudicated but their
proposed narrowings were mostly not applied to the chapters.** This run re-opened all 39 and closed them.

**Twenty of the 39 were already fixed on 09-02** and were verified as such, not re-edited: the Ch5
`ae_website_platform` derivation (the three excluded rows are schemeless domains, and the column bleed is in
`ae_website`, in three French rows); the VARA overstatement (now "VARA's own register runs to 13 January 2026");
the AMF forbearance chain (FT paywalled, The Block relay named in the body, no FT quote printed); the CONSOB
weekly/twenty-one-weeks limb (cut); the BitGo and Uphold exclusions (now "firm-stated relayed", with the tracker's
C grades named as understating them); the Luno quotation marks (now paraphrase, attributed to the outlet); the
Crypto.com CEO attribution; the Ferdon quotations (cut to paraphrase); the Ch7 "four seats" anchor; the Ledger
Studio limb; the triangulation share; the Reuters anchor (retired, FCA primary substituted); the Gemini comma quote
(no longer printed anywhere).

**Ten narrowings applied this run.** Every one narrows or corrects; none adds a claim, none strengthens one.

| # | chapter | change |
|---|---|---|
| 21 | 5 — MiCA readiness | `Volksbank eG – Die Gestalterbank` → hyphen, matching `ae_lei_name` at source. The sentence claims the names are quoted **verbatim**, so an en dash made it false as written. |
| 20 | 2 — shape of the function | "put every leader in an IC seat" → the memo's reporter's actual words: cut what is rendered as *"pure managers"* in favour of *"player-coaches"* who are also strong individual contributors. |
| 85 | 2 + 7 | Section header "Four seats, one month" contradicted its own body ("three of the eleven Stratum-1 exchanges"). Retitled **"Four seats examined, three vacant — in one month"**; Chapter 7's anchor citation updated in the same pass. |
| 86 | 2 | Ava Labs ×2 rows: `Director / comms-PR` → `Director / regulatory-comms/PR`, matching the CSV `seniority` field. |
| 98 | 7 | "Private gatekeepers moved before public ones" → **"A private gatekeeper's gate closed before any public one did"**. On dates the AFM's operational guidance (21 Jan 2025) *precedes* Google's EU policy effective date (23 Apr 2025); the plural claim was not sustainable, the singular one is what the following clause actually argues. |
| 58 | 4 | ESMA finfluencers factsheet in the **body**: "published January 2026" → "published to ESMA's site in January 2026 — month precision, from ESMA's own file path; the document's imprint carries a 2025 production year". The anchor block already carried the qualifier; the body did not. |
| 31 | 4 | "four localised language versions" → "four language versions (EN original plus DE, FR and IT localisations)" — the EN original is not a localisation. |
| 25 | 4 | Kraken anchor: "role corroboration" → **"person/firm corroboration only"**, naming the press release's date (19 April 2022) and the title it actually gives (CMO). The CGMO title rests on the Incrypted page alone and now says so. |
| 50 + 51 | 4 | Two mis-cites of `methodology.md`: the claim-vs-relationship rule is a **standing corpus rule** consistent with §2's "publicly claims as a client", not §2's text; and the 2026-06-15 as-of date is in **§6**, not §2. Both re-pointed. |
| 23 | 6 | Bitwise `date_announced` `[VERIFY]` **cleared by splitting the field**: `event 2026-08-07; reported 2026-08-11/08-12`. Horsley told The Block the team was trimmed "last week" relative to publication on Wednesday 2026-08-12, which places the event in the week of 08-03…08-09. Announced vs effective stay separate fields, per the standing rule. |

**One NOT-OPENED source re-attempted and recorded honestly.** `jobs.ashbyhq.com/ledger` — the absence half of
Chapter 6's standout datum — is **still NOT OPENED**: it is JavaScript-rendered and returns nothing to a static
fetch, the browser pane refused the domain, and the Ashby posting API is outside this session's fetch provenance
set. **That is a second independent failed capture, which is itself the honest result.** A negative check was run
in its place and passed: every Ledger listing findable off-board is roughly a year old or older, and the one
marketing-adjacent title among them (Senior Employer Brand Specialist, London) is employer-brand recruitment, not
a marketing-function role. **Chapter 6 now carries that limit inline** rather than resting the absence silently on
this corpus's own scanner. The other NOT-OPENEDs stay closed for stated reasons and none is claimed from: FT
(HTTP 403), Kraken (paywalled, deliberately), the Gnosis X post (ROBOTS_DISALLOWED), the Ferdon episode audio (no
audio capability, no publisher transcript in existence), Reuters (retired as an anchor).

## Rebuild — all four instruments re-run in this run

- `verify_chapter_citations.py` → **PASS: 250 URLs across 7 chapters, 0 untraced.** 37 `[VERIFY]` tags remain, all
  deliberate and labelled.
- `assemble_report.py` → **citation guard 261 in / 261 through**; 23,070 words ≈ **21.0 pages of a 25-page budget**;
  8 items of drafting apparatus dropped and listed.
- `build_publish_bundle.py` → `report.html`, self-contained, **176 live citation links**, 9 tables.
- `report.pdf` → re-rendered with **WeasyPrint 69.0**. No headless Chrome exists in this sandbox; the contract names
  WeasyPrint as an accepted renderer, so **no needs-jukka row was filed** and no second PUBLISH row was created.
  **44 pages.** Proofed against the 09-02 Chrome render before replacing it: Chrome was 44 pages with one blank page
  and two half-empty ones; WeasyPrint is 44 with one blank page (between Chapters 3 and 4) and none half-empty, so
  the swap is not a regression. Text extracts cleanly and all ten narrowings verified present in the rendered PDF.
  `PUBLISH.md` records the renderer change, the blank page, and the one-line Chrome re-export if Jukka prefers it.

**Side duty — nothing owed.** The "SoCM re-date" row reads CLEARED (2026-09-02 16:58Z, live-verified) and the
README lines from `PUBLIC-REDATE-2026-09-02.md` are already applied: `repo/README.md` says "Publishes
**September 15, 2026**" with the dated note. Left alone.

**Public-repo gate re-checked** on everything this run touched: zero references to the sales pipeline, prospects,
outreach, pricing, or Ron Pruett / Boston Associates in `findings/` or `report/`. ⚠ The **pre-existing** exposure
flagged on 09-02 is unchanged and still recommended for a fix before publish: `scripts/daily-corpus-sync.py` and
`scripts/README.md` document their input paths verbatim, and those paths name a sales funnel's prospect scanner. No
prospect data is exposed — paths, not rows — and it has been public since the scripts were written. Deliberately
not patched here: the script carries `CAPTURE_WINDOW_END` and the frozen-window behaviour the report's integrity
now depends on, and this is the wrong run to change it in. Already recorded on 09-02; **not re-escalated.**

## What is left

**Nothing until 09-08.** The bundle is frozen. 09-04 → 09-07 and 09-09 → 09-14: STEP 0 plus one line here. On
**09-08** the FCA v Huobi stay expires — re-open the FCA proceedings page and, only if an outcome is published,
update the one sentence in Chapters 5 and 7 and rebuild. Publishing is Jukka's act on **15 September**.
