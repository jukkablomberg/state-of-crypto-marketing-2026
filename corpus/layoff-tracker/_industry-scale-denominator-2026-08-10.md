# The corpus has been measuring its recall against the wrong universe

**Written:** 2026-08-10 (corpus run, day 40 post-deadline)
**Supersedes nothing. Constrains:** `_aggregator-crossref-2026-08-07.csv`, `_aggregator-date-integrity-2026-08-08.md`, and the recall statement in both the 08-07 and 08-08 run records.
**capture_ai_disclosure:** the captured source carries no per-article AI disclosure; its two named authors and editor are human bylines. CoinDesk's estate-wide AI use is documented in `../operator-statements/okx-rafique-role-reclassification-2026-08-10.md` §4.

---

## The three-day arc, stated plainly

| Run | Statement about class-5 recall | Status |
|---|---|---|
| **08-07** | "The corpus holds **19 of 54** rows listed by CryptoJobsList — **35%**." Called *"the single most important honest figure this corpus has produced about itself."* | Superseded within 24h |
| **08-08** | At least one of the 54 is a **2022** event. **35% is a FLOOR, not an estimate**, against a *"demonstrably contaminated"* denominator. | Still true, and still too generous |
| **08-10 (today)** | **The denominator was never the right object.** | Below |

---

## The datum

**Captured first-party this run, HTTP 200:** CoinDesk, *"Crypto is going through a massive dot-com style shakeout as over 100 projects fold in 2026"*, published **2026-08-09 13:00 UTC**, updated 16:03, by **Oliver Knight and Margaux Nijkerk**, edited by **Cheyenne Ligon**.

Verbatim:

> "**Over 100 crypto projects have shut down, filed for bankruptcy or gone permanently dark in 2026**, according to data from **RootData**, and the pace is accelerating. **Four major firms announced closures or filings within a single week in late July alone: BitMEX, BitMart, Movement Labs and Storj Labs.**"

Also in the piece, and each of these is a dated in-window artefact the corpus does not hold:

- **Moonbeam**, a Polkadot parachain, **stopped producing blocks 2026-07-31** — assets in on-chain protocols including Moonwell now inaccessible.
- **$1.1 billion** lost to on-chain exploits in H1 2026 (Blockaid), more than all of 2025 combined; **April 2026 the most-hacked month in crypto history** by incident count.
- **TRM Labs:** DPRK-linked actors = **66%** of H1-2026 hack losses.
- Named shutdowns with stated rationale: **Tally** (DAO tooling, >500 protocols, >$1bn payments processed — *"There isn't a venture-backed business in governance tooling for decentralized protocols, at least not yet"*, co-founder Dennison Bertram); **Step Finance** (Feb 2026, after a January phishing attack drained 261,854 SOL ≈ $35m); **Everclear** (*"Despite reaching $500M in monthly volume, the cross-chain solvers segment never developed the commercial depth we needed"*).
- **Survivors named with revenue-in-dollars-not-token as the common factor:** Hyperliquid ($1bn cumulative fees, crossed 2026-06-30; 70% of decentralised perps), Aave (>$12bn deposits Jul-2026, >$100m annualised borrow fees, absorbed $8.4bn of April outflows), Ether.fi ($7.8bn TVL; card product ≈50% of protocol revenue; record $2.72m Q2 transaction fees).

---

## What this does to the recall measure — and it is not a rounding correction

**RootData's 100+ and CryptoJobsList's 54 are not the same object and must never be divided by one another.**

- **CryptoJobsList counts LAYOFF EVENTS** — a firm continues to exist and sheds staff.
- **RootData counts PROJECT DEATHS** — shutdown, bankruptcy, or gone dark.

A firm can appear in one, both, or neither. BitMEX, BitMart and Movement Labs are deaths; Coinbase, Kraken and Polygon Labs are layoff events at going concerns. **Any attempt to state corpus recall as a single percentage requires first choosing which universe is being sampled, and the corpus has never made that choice explicitly.**

**Therefore, the only three sentences Phase 2 may write about class-5 completeness:**

1. *The corpus holds **23** rows, every one of which has had its date read at its own source.*
2. *Against one public aggregator's 2026 layoff table (n=54), the corpus holds at least 19 — a floor, against a denominator demonstrably contaminated with at least one pre-window event.*
3. ***The corpus does not know how many 2026 crypto contractions exist, and a second public tracker counts a different object at roughly twice the scale.***

**Nothing stronger. No single recall percentage. No "we hold X% of the market."**

---

## Why this is a good result and not a bad one

Three consecutive runs have now degraded the corpus's own headline self-measurement — 35% → floor → wrong universe. That looks like decay. It is not.

**On 08-07 the corpus had a number it could not defend. On 08-10 it has a bounded, honest, defensible statement about what it does and does not know, arrived at by opening the sources instead of citing them.** The 08-08 entry called this pattern *"what happens the first time a corpus is systematically audited."* This is the fourth consecutive instance, and the audited instrument was again the audit.

**The failure mode this avoids is specific and it is the one the report exists to criticise.** A report that printed *"NorthPoint's corpus captures 35% of 2026 crypto layoffs"* would be doing exactly what the corpus documents Kraken, OKX, Bitpanda and BitMart doing on their promotional estates: **publishing a claim whose supporting surface no longer matches the operational state behind it.** Phase 2 is days away. This is the last cheap moment to catch it.

---

## Consequences to carry

1. **`methodology.md` §5 names three 2026 layoffs (Crypto.com, Gemini, Algorand) "plus any new ones through August."** The tracker holds 23 and the industry-scale figure is 100+ deaths. **§5's framing implies a completeness the corpus has now measured itself as not having. Rewrite or caveat it.** Joins the standing §1 / §4 / §7 rewrite queue.
2. **Two of the four late-July names in the captured sentence are already tracker rows; one is added today (Movement Labs); one — STORJ LABS — is entirely new to this corpus and unresearched.** Named so it is not lost.
3. **RootData's list is a linked, addressable source and was NOT fetched** (`rootdata.com/archives/detail/2026 Crypto Dead Projects List`). It is the single highest-value unfetched class-5 instrument the corpus has ever identified. **Fetch it next run.** This is watch (ee) — *a source cited once is a source not used as an instrument* — firing for the third time in four runs, and this run is naming it before it costs anything rather than after.
4. **Moonbeam (2026-07-31) is a dated in-window closure at a named chain and is not in the tracker.** Not added today because no primary was captured; queued.

## Provenance

- **Fetched, HTTP 200:** `https://www.coindesk.com/business/2026/08/09/crypto-is-going-through-a-massive-dot-com-style-shakeout-as-over-100-projects-fold-in-2026`.
- **Linked by the capture, NOT fetched, NOT claimed:** the RootData dead-projects list; the Tally shutdown newsletter; FinanceFeeds on Step Finance; The Block on Everclear; the Blockaid, TRM Labs and Crowdfund Insider hack reports; the KuCoin Moonbeam notice; three X posts (Puckrin, Valente, Blockaid). **No URL fabricated.**
