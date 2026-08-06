# scripts/ — corpus automation

## daily-corpus-sync.py

Deterministic daily producer for source classes **1 (job postings)** and **2 (agency claims / overlap matrix)**. It exists so the corpus stops depending on WebSearch (which cannot date-stamp ATS postings or agency claims) and instead consumes the two daily data feeds NorthPoint already runs.

### What it reads (already-running daily feeds)
| Source | Path | Provides |
|---|---|---|
| A — job postings | `../northpoint/sales-funnel/prospects/open-positions.json` | Daily ATS API scan (greenhouse/ashby/lever/breezy/workable/…). URL-verified, dated, seniority-scored marketing/growth roles. Also lists `needs_chrome_fallback` (proprietary ATS not API-reachable) and `fetch_errors`. |
| B — agency intel | `../northpoint/sales-funnel/competitor-intelligence/trend-data.json` | Daily 18-agency panel. Each agency has dated entries with `recentClientsNamed`, `healthScore`, `threatLevel`. |

### What it writes (every run, into `corpus/`)
- `job-postings/<firm>.csv` — per tracked-firm marketing roles (Stratum 1–4 cohort only; dedup by `source_url`). Schema: `date_posted,title,jurisdiction,seniority,source_url,captured_date,notes`.
- `job-postings/_absence.csv` — tracked firms with **no API coverage** (proprietary ATS or fetch error) + their careers URL. Absence is data (methodology rule).
- `agency-overlap-matrix.csv` — tracked firm × claiming agencies, with `OVERLAP` flag where >1 agency claims the same firm (Theme 3).
- `agency-claims/<agency>.csv` — dated per-agency claimed-client snapshot, each client tagged tracked / not-tracked.

### Feed-health guard (added 2026-08-06 — watch bb)

"0 new postings" is ambiguous between **ABSENT** (the scan ran and found nothing) and **UNOBSERVED** (the scan did not run). On 2026-08-05 the upstream ATS scan had been frozen for ~66h and the sync reported 0 new postings anyway — the corpus was one step from publishing an absence claim it had not earned, which is the same defect it documents in other firms' promotional estates.

Every run now prints:

```
FEED HEALTH: HEALTHY|STALE|UNKNOWN (scanned_at_utc=..., age=..h, fingerprint total_jobs_fetched=...)
```

- **HEALTHY** — `scanned_at_utc` under 36h old. A zero is a genuine absence and may be written as one.
- **STALE** — over 36h. The run prints `CLASS-1 ABSENCE CLAIM REFUSED`; the run record must say **"class 1 unobserved"**, never "class 1 produced nothing."
- **UNKNOWN** — timestamp missing or unparseable. Treated as stale.

`total_jobs_fetched` is carried as a **fingerprint**: if it moves while `new_count` stays 0, the scan genuinely looked. If it is byte-identical to the prior run, the scan did not.

### Coverage rules honoured
Tracked-firm cohort only (alias table mirrors `tracked-firms.md`); every row carries a primary source URL; dedup against existing rows; **no fabrication** — only what the upstream feeds contain. Idempotent: re-running the same day adds nothing.

### Run
```
python3 scripts/daily-corpus-sync.py
# override paths if the repo is relocated:
python3 scripts/daily-corpus-sync.py --repo <repo> --sales <sales-funnel>
```

### Daily task ordering (recommended)
1. `python3 scripts/daily-corpus-sync.py` → classes 1 + 2 (deterministic, always produces output).
2. WebSearch pass → classes 3 (regulator), 4 (operator statements), 5 (layoffs) for net-new in-window items.
3. Write the dated run record in `corpus/weekly-runs/`, update `findings/`, commit.

### Known residual gap (bounded)
Proprietary-ATS exchanges (Binance, Bybit, KuCoin, HTX) + Solana/ConsenSys are not API-reachable and surface only in `_absence.csv`. Closing them = pointing the existing `chrome-supplemental-scan` lane at `open-positions.json`'s `needs_chrome_fallback` list and feeding rendered postings back through the same schema.
