# MiCA capture campaigns — the day-after-close checkpoint (Kraken + OKX)

**Class:** firm-side marketing action (companion to `mica-competitive-capture-2026-06.md`)
**Checkpoint date:** **2026-08-01** — the first day after both campaigns' stated end date of **31 July 2026**
**Scheduled:** this checkpoint was calendared on 07-29 and 07-30 for **07-31**. **The 07-31 corpus run did not fire** (no `2026-07-31-corpus-run.md` exists; git log shows no 07-31 corpus commit). Executed one day late — which, for a lapse checkpoint, is the more informative day. **Recorded as a cadence miss, not as a design choice.** See run record.
**Method:** direct primary fetch of each firm's own live campaign page on 2026-08-01.

## Result: 2 of 2 campaigns were still publicly live, in the present tense, the day after they closed

### Kraken — `https://www.kraken.com/europe-switch` (fetched 2026-08-01, HTTP 200)

Still serving, unchanged, with live CTAs:

- H1: **"Most exchanges aren't licensed after July 1. Kraken is."**
- Sub: *"MiCA licensed. MiFID licensed. Operating since 2011. **Switch now and enter our €1M prize draw**."*
- CTA buttons live: **"Switch to Kraken"** and **"Enter the €1M draw"** (→ `proapp.kraken.com/9f1e/hg0aq9gh`)
- Standing legend: **"Lottery closes July 31. T&Cs apply."**
- Section H2: **"Switch to Kraken before July 31. Enter for €1M."**
- Body: *"Every euro you deposit on Kraken enters you into our €1M prize draw… Open to new and existing users."* / *"Draw closes July 31, 2026. One entry per €1 deposited."*
- Step 2: *"Every euro deposited **from June 22 to July 31** earns one entry into the €1M draw."*
- Page `meta-description` **and** OG/Twitter description all still read: *"…Switch now and enter our €1M prize draw. Every euro deposited earns one entry. **Closes July 31**."*

**Note the internal date conflict, unchanged from the 07-12 correction:** the page body says entries run **June 22 – July 31**, while the firm's own sweepstakes T&Cs page was previously recorded as stating a **19 June** start. Primary-vs-primary conflict inside one firm's own estate; still unresolved. `[VERIFY]`

### OKX — `https://www.okx.com/en-us/learn/okx-europe-deposit-bonus-mica-deadline` (fetched 2026-08-01, HTTP 200)

Still serving, present tense, with live CTAs:

- *"**From 29 June until 31 July 2026**, anyone who resides in the European Economic Area (EEA), transfers crypto or deposits cash to OKX Europe and opts in **receives an 8% bonus (up to €20,000 in USDC)** on their net deposit, with a minimum of just €10 to qualify."*
- *"New users get even more: **an enhanced welcome bonus of up to €400** on top of the deposit bonus and a 30-day VIP upgrade."*
- Live CTA: **"Claim your deposit bonus"** (→ `my.okx.com/ul/LhoH7A`), repeated twice.
- Page metadata: *"Transfer **before the 1 July 2026 MiCA deadline** to a fully regulated exchange."*
- **Published Jun 12, 2026 · Updated Jul 07, 2026.** The page was updated during the campaign and **not** at its close.

## The finding

> **Both dated, quantified, EEA-geofenced MiCA capture campaigns outlived their own stated end dates on their own primary pages.** On 2026-08-01 a prospective EEA customer reading either firm's official campaign page is invited, in the present tense, with a working button, to enter a draw that has closed and to claim a bonus whose qualifying window has shut.

Two firms, two different mechanics (prize draw vs deposit bonus), two different NCAs (CBI Ireland; MFSA Malta), **same failure mode**. n=2 is small, but it is 2/2 of the panel members whose windows expired on this date, and both were checked by direct primary read on the same day. This is not a claim about intent — pages lapse, CMS jobs run on Mondays, and a page can be geofenced so an EEA visitor sees something an outside fetch does not. **All of that is worth saying, and none of it changes what is publicly served.**

**Why the corpus cares (Theme 4).** The report's central premise is visibility-as-analysis: the marketing surface a regulator can verify is the surface that matters. A live, present-tense offer page for an expired promotion sits precisely inside the *fair, clear and not misleading* standard that MiCA Art. 7 and every NCA's promotion regime applies to marketing communications. **The corpus does not assert a breach and must not.** What it records is that the panel's two most sophisticated, most compliance-dressed capture campaigns — the ones prior runs praised for shipping "elaborate equal-prominence risk apparatus" — both left the same loose edge, and it is the *lifecycle* edge rather than the *disclosure* edge. **Campaign compliance is being designed at launch and not maintained at teardown.**

That is a printable, falsifiable, useful finding for a report aimed at CMOs.

## Secondary capture — OKX has folded the capture offer into a permanent rewards stack

From OKX's own related-articles rail, all first-party, all dated:

| date | item | significance |
|---|---|---|
| 2026-07-22 | *"50 million up for grabs! Deposit Crypto or Cash on OKX and Get an 8% Bonus (Up to €20,000)"* — https://www.okx.com/en-us/learn/mica-deposit-bonus-campaign | **Confirms the €50M reward pool on a primary OKX page** (previously press-reported only) |
| **2026-07-29** | *"Rewardmaxxing on OKX: How to Stack Various Campaign Rewards at Once"* — https://www.okx.com/en-us/learn/rewardmaxxing-okx-stack-rewards — *"OKX is running multiple reward programs for users residing in the EEA at the same time, such as: The 8% MiCA Deposit Bonus, X Drops Club…"* | **The MiCA capture offer is no longer a discrete event — it is now marketed as one component of a stackable, ongoing EEA rewards programme** |
| 2026-07-29 | *"OKX Card — Happy Weekend Campaign August 2026"* — https://www.okx.com/en-us/learn/okx-card-happy-weekend-august | An **August** EEA campaign was already staged before the capture window closed |

**Theme-3 read.** The prior runs' framing was that the MiCA licence became a *time-boxed* acquisition weapon around a regulatory event. That framing is now incomplete. At OKX the licence-led capture offer has been **absorbed into standing promotional infrastructure** — a rewards stack with an August successor already published two days before the capture window closed. The regulatory event did not create a campaign; it created a **channel**, and the channel outlives the event.

## Licence detail captured (primary, first-party) — Theme 3/4

OKX Europe Limited, per its own page: **MiCA CASP licence from the MFSA issued 27 January 2025** covering **nine of the ten** MiCA services, passported across **all 30 EEA states**; **MiFID II** licence (OKX EUROPE MARKETS LTD, MFSA, April 2022) for X-Perps derivatives; **Payment Institution licence (MFSA, February 2026)** for OKX Card and OKX Pay. Kraken, per its own page: **MiCA via the Central Bank of Ireland**, **MiFID via CySEC** (licence no. 342/17, Payward Europe Digital Solutions (CY) Limited), both passported across 27 EU states.

**Both firms now lead with a licence *stack*, not a licence.** Kraken: *"Two of the EU's highest regulatory standards, held simultaneously. This is not a compliance minimum — it is the deepest regulatory standing available to a crypto exchange operating in Europe."* That sentence is the Theme-3 thesis stated by a tracked firm in its own words, and it is quotable.

## What was NOT done

- **Not fetched:** `kraken.com/legal/deposit-sweepstakes-terms` (would resolve the 19-vs-22 June conflict) and `my.okx.com/en-eu/campaigns/switch-to-okx-deposit-bonus` (the in-app EEA campaign surface, as opposed to the `/learn` explainer). Both carried.
- **Not tested:** whether an EEA-geolocated visitor is served a different, closed-state page. **This is the single most important caveat on the finding above** and it cannot be resolved from this run's fetch layer. → chrome lane, EEA egress. `[VERIFY]`
- **Coinbase 5%** (lapsed 07-13), **Bitpanda** (lapsed 07-05), **Bitvavo**, **Gate**: not re-checked this run. If the lapse pattern is real, they are the replication set. **This is the highest-value cheap follow-up in the corpus right now** — it converts n=2 into n=6 in one run.
