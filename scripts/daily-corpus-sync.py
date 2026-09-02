#!/usr/bin/env python3
"""
daily-corpus-sync.py — State of Crypto Marketing 2026

Deterministic daily corpus producer. Turns NorthPoint's already-running daily
data feeds into citation-anchored corpus output WITHOUT depending on web search:

  Source A (job postings):  northpoint/sales-funnel/prospects/open-positions.json
                            (daily ATS API scan: greenhouse/ashby/lever/breezy/... ,
                             URL-verified, dated, seniority-scored)
  Source B (agency intel):  northpoint/research/legacy/agency-panel-trend-data-asof-2026-06-15.json (frozen 2026-06-15)
                            (daily 18-agency panel with recentClientsNamed per agency)

Outputs (every run, concrete):
  corpus/job-postings/<firm>.csv          — per tracked-firm marketing roles (dedup by URL)
  corpus/agency-overlap-matrix.csv        — agency × tracked-firm claim matrix + overlap flags
  corpus/agency-claims/<agency>.csv       — per-agency claimed-clients snapshot (dated)
  corpus/job-postings/_absence.csv        — tracked firms with no API coverage (absence = data)

Run: python3 scripts/daily-corpus-sync.py [--repo <path>] [--sales <path>]
Prints a one-screen concrete summary (counts) for the daily run record.

Coverage rules honoured: tracked-firm cohort only (Stratum 1-4 in tracked-firms.md),
every row carries a source URL, dedup against existing CSV rows, absence recorded
explicitly. No fabrication: only what the source feeds actually contain.
"""
import argparse, csv, json, os, sys, datetime, re

# ---- CLASS-1 CAPTURE WINDOW (watch (ao)/(ai), added 2026-09-02) ----------------
# methodology.md §1, README.md and README-for-github.md all state the class-1
# capture window as "rolling 12 months ending August 31, 2026". Until today this
# script had NO concept of that end date: it answered "did the scan look?" — which
# it answers correctly every day, including days whose answer the report may not use.
#
# On 2026-09-01 (ship day) that gap bit for the first time. The feed was HEALTHY,
# 0 postings were added, and the sync nonetheless rolled the `as_of` column of
# _absence.csv and _chrome-queue.csv from 2026-08-31 to 2026-09-01 — making a
# SHIPPED Theme-1/Theme-4 exhibit assert an observation date outside the window all
# three public documents advertise. It was restored by hand. On 2026-09-02 the same
# roll recurred AND the absence panel gained a new member (Gemini, greenhouse read
# timeout) — i.e. a post-window class-1 observation was one write from entering a
# shipped exhibit. Restored by hand again. Two hand corrections is the signal to
# put the rule in code.
#
# The rule, exactly as ruled on 2026-09-01 and re-applied 2026-09-02:
#   * class-1 CORPUS CLAIMS (per-firm job rows, _absence.csv, _chrome-queue.csv)
#     are FINAL at the window close and are not rewritten afterwards;
#   * the INSTRUMENT LOG (_feed-fingerprint.json) keeps recording every run, because
#     "a 09-02 scan ran" is a true fact about the instrument and belongs on the record.
# The distinction is the whole point: a fingerprint entry is not a corpus claim.
#
# Post-window the script still READS the feed and still PRINTS what it saw, so the
# daily run record can report the live instrument state without the corpus absorbing
# it. Set CAPTURE_WINDOW_END to None to disable the freeze (e.g. a next cycle).
CAPTURE_WINDOW_END = "2026-08-31"

def window_closed(today, window_end=CAPTURE_WINDOW_END):
    """True when `today` falls after the class-1 capture window's last day."""
    return bool(window_end) and today > window_end

# ---- Tracked-firm cohort (Stratum 1-4, tracked-firms.md) + alias -> canonical file slug
TRACKED = {
    # Stratum 1 — exchanges
    "binance": "binance", "okx": "okx", "bybit": "bybit", "kucoin": "kucoin",
    "coinbase": "coinbase", "kraken": "kraken", "crypto.com": "crypto-com",
    "foris": "crypto-com", "gemini": "gemini", "bitstamp": "bitstamp",
    "bitpanda": "bitpanda", "htx": "htx", "huobi": "htx",
    # Stratum 2 — L1/L2 foundations
    "sui": "sui", "sui foundation": "sui", "mysten labs": "sui",
    "aptos": "aptos", "solana": "solana", "solana foundation": "solana",
    "aave": "aave", "polygon": "polygon", "optimism": "optimism",
    "optimism foundation": "optimism", "op labs": "optimism",
    "arbitrum": "arbitrum", "arbitrum foundation": "arbitrum", "offchain labs": "arbitrum",
    "ava labs": "ava-labs", "avalanche": "ava-labs",
    # Stratum 3 — wallets / consumer
    "metamask": "metamask-consensys", "consensys": "metamask-consensys",
    "phantom": "phantom", "ledger": "ledger", "trust wallet": "trust-wallet",
    "rabby": "rabby",
    # Stratum 4 — CASP non-exchange
    "securitize": "securitize", "tether": "tether", "relai": "relai",
}
# Display names for files
DISPLAY = {
    "crypto-com": "Crypto.com", "ava-labs": "Ava Labs", "metamask-consensys": "MetaMask / ConsenSys",
    "trust-wallet": "Trust Wallet", "htx": "HTX", "okx": "OKX",
}
def disp(slug): return DISPLAY.get(slug, slug.replace("-", " ").title())

# 18-agency comparison panel (Stratum 5)
AGENCY_PANEL = ["coinbound","lunar-strategy","ninjapromo","marketacross","icoda",
    "tokenminds","serotonin","crowdcreate","guerrillabuzz","blockwiz","blue-manakin",
    "rzlt","x10","single-grain","flexe","outset-pr","bond-finance","majinx"]

JOB_HEADER = ["date_posted","title","jurisdiction","seniority","source_url","captured_date","notes"]

# Known blockers for proprietary-ATS tracked firms (why a naive render won't close them).
# Foundation/Getro boards render fine; exchange SPAs are sign-in/API-walled; some are standard
# ATS behind a wrong/missing slug (upstream lead-generator slug fix, not a browser render).
CHROME_BLOCKERS = {
    "Bybit": "Moka SPA, sign-in-walled — needs authed session or Moka API",
    "Binance": "JS SPA — needs bapi careers endpoint, not naive render",
    "Kucoin": "MokaHR SPA — needs Moka API/authed session",
    "HTX": "JS SPA (crm recruitment) — needs API/authed session",
    "MetaMask / ConsenSys": "Greenhouse-embedded — fix the API slug (boards-api.greenhouse.io/v1/boards/consensys)",
    "Solana": "Getro board — renders; closeable via Chrome lane",
    "Aave": "Lever slug 404 — correct the slug upstream",
}

def norm(s): return re.sub(r"[^a-z0-9. ]","",(s or "").lower()).strip()

def match_tracked(company):
    n = norm(company)
    if n in TRACKED: return TRACKED[n]
    for alias, slug in TRACKED.items():
        if n == alias or n.startswith(alias + " ") or (" " + alias) in (" " + n):
            return slug
    return None

def seniority_of(title):
    t = (title or "").lower()
    for kw in ["chief","cmo","vp ","vice president","head of","director","lead","principal","senior","manager"]:
        if kw in t: return kw.replace(" ","").upper() if kw in ("vp ",) else kw.title().strip()
    return "IC"

def func_of(title):
    t=(title or "").lower()
    if "product marketing" in t or "pmm" in t: return "PMM"
    if "growth" in t or "demand gen" in t or "performance" in t: return "growth"
    if "community" in t: return "community"
    if "communications" in t or "comms" in t or "pr " in t or "social" in t: return "regulatory-comms/PR"
    if "brand" in t or "creative" in t or "content" in t or "copy" in t or "events" in t: return "brand"
    if "seo" in t: return "growth"
    return "marketing"

def load_json(p):
    with open(p) as f: return json.load(f)

def read_existing_urls(path):
    urls=set()
    if os.path.exists(path):
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                if row.get("source_url"): urls.add(row["source_url"].strip())
    return urls

def count_new_rows(jp_dir, slug, rows):
    """Dry run of append_firm_rows: how many rows WOULD be admitted. Writes nothing.
    Used when the capture window has closed, so the run record can state what the live
    feed offered without the corpus admitting it (watch ao)."""
    path=os.path.join(jp_dir,f"{slug}.csv")
    existing=read_existing_urls(path)
    return len([r for r in rows if r[4] and r[4] not in existing])

def append_firm_rows(jp_dir, slug, rows):
    """rows: list of [date_posted,title,jurisdiction,seniority,source_url,captured_date,notes].
    Dedups by source_url against the existing file; rewrites cleanly if file is an empty scaffold.
    Returns number of rows actually added."""
    path=os.path.join(jp_dir,f"{slug}.csv")
    existing=read_existing_urls(path)
    new_rows=[r for r in rows if r[4] and r[4] not in existing]
    if not new_rows: return 0
    scaffold = os.path.exists(path) and existing==set()
    mode="w" if (not os.path.exists(path) or scaffold) else "a"
    with open(path,mode,newline="") as f:
        w=csv.writer(f)
        if mode=="w": w.writerow(JOB_HEADER)
        for r in new_rows: w.writerow(r)
    return len(new_rows)

def main():
    ap=argparse.ArgumentParser()
    here=os.path.dirname(os.path.abspath(__file__))
    repo_default=os.path.dirname(here)
    ap.add_argument("--repo", default=repo_default)
    # repo lives at <projects>/state-of-crypto-marketing-2026/repo ; sales-funnel is a sibling project
    ap.add_argument("--sales", default=os.path.join(repo_default, "..", "..", "northpoint", "sales-funnel"))
    # --window-end exists so the freeze is RED-PROOFABLE (lessons L16): a guard that
    # cannot be made to return the other verdict has not been tested. "none" disables it.
    ap.add_argument("--window-end", default=CAPTURE_WINDOW_END,
                    help="class-1 capture window last day (YYYY-MM-DD), or 'none' to disable the freeze")
    args=ap.parse_args()
    win_end=None if str(args.window_end).lower()=="none" else args.window_end
    repo=os.path.abspath(args.repo); sales=os.path.abspath(args.sales)
    today=datetime.date.today().isoformat()
    jp_dir=os.path.join(repo,"corpus","job-postings")
    ac_dir=os.path.join(repo,"corpus","agency-claims")
    os.makedirs(jp_dir,exist_ok=True); os.makedirs(ac_dir,exist_ok=True)

    summary={"job_added":0,"job_firms":set(),"absence_firms":[],"matrix_rows":0,
             "agency_files":0,"overlaps":[],"src_jobs_date":None,"src_agency_date":None,
             "chrome_ingested":0,"chrome_queue_firms":[],
             # class-1 window freeze (watch ao/ai)
             "window_end":win_end,"window_closed":False,
             "frozen_job_rows":0,"frozen_job_firms":[],"frozen_absence_firms":[]}
    frozen = window_closed(today, win_end)
    summary["window_closed"]=frozen

    # ---------- Source A: job postings ----------
    op_path=os.path.join(sales,"prospects","open-positions.json")
    if os.path.exists(op_path):
        op=load_json(op_path)
        meta=op.get("scan_metadata",{})
        summary["src_jobs_date"]=meta.get("scan_date")
        # ---- FEED-HEALTH GUARD (watch bb, added 2026-08-06) ----
        # "0 new postings" is ambiguous between ABSENT (feed ran, found nothing)
        # and UNOBSERVED (feed did not run). Distinguish them, and refuse to let
        # the run record make an absence claim for class 1 in the stale case.
        summary["feed_scanned_at"]=meta.get("scanned_at_utc")
        summary["feed_fingerprint"]=meta.get("total_jobs_fetched")
        age_h=None
        try:
            ts=datetime.datetime.strptime(meta.get("scanned_at_utc",""),"%Y-%m-%dT%H:%M:%SZ")
            age_h=round((datetime.datetime.utcnow()-ts).total_seconds()/3600.0,1)
        except Exception:
            pass
        summary["feed_age_hours"]=age_h
        # ---- SECOND PREDICATE: FINGERPRINT DELTA (watches bb + ff, added 2026-08-14) ----
        # 2026-08-13: age said HEALTHY (14.0h) while the fingerprint was byte-identical
        # to the prior run across a two-calendar-day gap. scripts/README.md's own rule
        # says a byte-identical fingerprint means the scan did not look — but the banner
        # printed only the age half, so the guard passed on a run it should have refused.
        # Fix: persist the fingerprint, print the DELTA, and degrade to STALE on a zero
        # delta regardless of age. Same-day re-runs stay idempotent (they compare against
        # the last observation from a PRIOR calendar date, not against themselves).
        fp_state_path=os.path.join(repo,"corpus","job-postings","_feed-fingerprint.json")
        fp_now=summary["feed_fingerprint"]
        fp_hist=[]
        if os.path.exists(fp_state_path):
            try: fp_hist=load_json(fp_state_path).get("history",[])
            except Exception: fp_hist=[]
        prior=None
        for h in reversed(fp_hist):
            if h.get("observed_date")!=today:
                prior=h; break
        fp_delta=None
        if prior is not None and isinstance(fp_now,int) and isinstance(prior.get("fingerprint"),int):
            fp_delta=fp_now-prior["fingerprint"]
        summary["feed_fingerprint_delta"]=fp_delta
        summary["feed_fingerprint_prior"]=(prior or {}).get("fingerprint")
        summary["feed_fingerprint_prior_date"]=(prior or {}).get("observed_date")
        # HEALTHY iff the scan is under 36h old AND the fingerprint moved since the last
        # observation from a prior date. Either predicate failing means the corpus cannot
        # claim the upstream ATS scan looked.
        if age_h is None:
            summary["feed_health"]="UNKNOWN"; summary["feed_health_reason"]="scanned_at_utc missing or unparseable"
        elif age_h>36:
            summary["feed_health"]="STALE"; summary["feed_health_reason"]=f"scan age {age_h}h exceeds 36h"
        elif fp_delta==0:
            summary["feed_health"]="STALE"; summary["feed_health_reason"]=(
                f"fingerprint delta 0 vs {prior.get('observed_date')} "
                f"({prior.get('fingerprint')}) — by scripts/README.md's own rule the scan did not look")
        elif fp_delta is None:
            summary["feed_health"]="HEALTHY"; summary["feed_health_reason"]=(
                "age OK; no prior-date fingerprint on record, delta unmeasurable this run")
        else:
            summary["feed_health"]="HEALTHY"; summary["feed_health_reason"]=f"age {age_h}h, fingerprint delta {fp_delta:+d}"
        summary["absence_claim_permitted"]=(summary["feed_health"]=="HEALTHY")
        # persist today's observation (idempotent: one entry per calendar date)
        fp_hist=[h for h in fp_hist if h.get("observed_date")!=today]
        fp_hist.append({"observed_date":today,"fingerprint":fp_now,
                        "scanned_at_utc":summary["feed_scanned_at"],
                        "scan_date":summary["src_jobs_date"],
                        "age_hours":age_h,"delta_vs_prior_date":fp_delta})
        fp_hist=sorted(fp_hist,key=lambda h:h.get("observed_date") or "")[-90:]
        try:
            os.makedirs(os.path.dirname(fp_state_path),exist_ok=True)
            with open(fp_state_path,"w") as fh:
                json.dump({"note":"feed-health guard state (watches bb+ff). "
                                  "Fingerprint = open-positions.json scan_metadata.total_jobs_fetched. "
                                  "A zero delta across calendar dates degrades FEED HEALTH to STALE.",
                           "history":fp_hist},fh,indent=2)
                fh.write("\n")
        except Exception as e:
            print(f"  !! could not persist fingerprint state: {e}")
        roles=[]
        for key in ("new_since_last_scan","still_open_from_prior_scans"):
            roles += op.get(key,[])
        by_firm={}
        for j in roles:
            slug=match_tracked(j.get("company",""))
            if not slug: continue
            by_firm.setdefault(slug,[]).append(j)
        for slug,js in sorted(by_firm.items()):
            rows=[]
            for j in js:
                url=(j.get("url") or j.get("apply_url") or "").strip()
                if not url: continue
                rows.append([
                    j.get("posted_at") or j.get("first_seen") or "",
                    j.get("title",""), j.get("location",""),
                    f"{seniority_of(j.get('title',''))} / {func_of(j.get('title',''))}",
                    url, today,
                    f"ATS={j.get('ats','')}; url_verified={j.get('url_verified')}; src=open-positions.json {summary['src_jobs_date']}",
                ])
            if frozen:
                # Class 1 is closed. Report what the live feed offered; admit none of it.
                would = count_new_rows(jp_dir, slug, rows)
                if would:
                    summary["frozen_job_rows"]+=would
                    summary["frozen_job_firms"].append(disp(slug))
                continue
            added=append_firm_rows(jp_dir, slug, rows)
            if added: summary["job_added"]+=added; summary["job_firms"].add(disp(slug))

        # ---- Source A2: Chrome inbox (proprietary-ATS firms rendered by the Chrome lane) ----
        # A browser pass writes corpus/job-postings/_chrome-inbox.json: list of
        # {company,title,location,posted_at,url,ats,source}. We ingest it the same way.
        inbox_path=os.path.join(jp_dir,"_chrome-inbox.json")
        ingested_firms=set()
        if os.path.exists(inbox_path):
            try: inbox=json.load(open(inbox_path))
            except Exception: inbox=[]
            inbox_by_firm={}
            for it in inbox:
                slug=match_tracked(it.get("company",""))
                if slug: inbox_by_firm.setdefault(slug,[]).append(it)
            for slug,items in sorted(inbox_by_firm.items()):
                rows=[]
                for it in items:
                    url=(it.get("url") or "").strip()
                    if not url: continue
                    rows.append([
                        it.get("posted_at",""), it.get("title",""), it.get("location",""),
                        f"{seniority_of(it.get('title',''))} / {func_of(it.get('title',''))}",
                        url, today,
                        f"ATS={it.get('ats','proprietary')}; via=chrome-lane; src={it.get('source','careers-page')}",
                    ])
                if frozen:
                    would = count_new_rows(jp_dir, slug, rows)
                    if would:
                        summary["frozen_job_rows"]+=would
                        summary["frozen_job_firms"].append(disp(slug))
                    ingested_firms.add(slug)
                    continue
                added=append_firm_rows(jp_dir, slug, rows)
                if added:
                    summary["job_added"]+=added; summary["job_firms"].add(disp(slug))
                    summary["chrome_ingested"]+=added
                ingested_firms.add(slug)

        # ---- absence-as-data + Chrome work-queue ----
        absent=[]; chrome_queue=[]
        for item in op.get("needs_chrome_fallback",[]):
            slug=match_tracked(item.get("company",""))
            if not slug: continue
            status = "ingested" if slug in ingested_firms else "pending-chrome"
            chrome_queue.append((disp(slug), item.get("ats","proprietary"), item.get("careers_url",""), status))
            if slug not in ingested_firms:
                absent.append((disp(slug),"proprietary-ATS/needs-chrome", item.get("careers_url","")))
        for item in op.get("fetch_errors",[]):
            slug=match_tracked(item.get("company",""))
            if slug and slug not in ingested_firms:
                absent.append((disp(slug),"api-fetch-error", item.get("error","")[:120]))
        # write the actionable Chrome work-queue (tracked proprietary firms + what to fetch)
        # POST-WINDOW: both of these are SHIPPED corpus exhibits carrying an `as_of`.
        # They are not rewritten after the window closes — not even when their content
        # is unchanged, because the `as_of` column alone would re-date them (watch ai).
        if chrome_queue and not frozen:
            with open(os.path.join(jp_dir,"_chrome-queue.csv"),"w",newline="") as f:
                w=csv.writer(f); w.writerow(["firm","ats","careers_url","status","blocker","target_functions","as_of"])
                for fm,ats,url,st in sorted(set(chrome_queue)):
                    w.writerow([fm,ats,url,st,CHROME_BLOCKERS.get(fm,""),"brand|growth|PMM|community|comms",today])
        if chrome_queue:
            summary["chrome_queue_firms"]=sorted({c[0] for c in chrome_queue})
        if absent and not frozen:
            with open(os.path.join(jp_dir,"_absence.csv"),"w",newline="") as f:
                w=csv.writer(f); w.writerow(["firm","reason","detail","as_of"])
                for fm,rs,dt in sorted(set(absent)): w.writerow([fm,rs,dt,today])
        summary["absence_firms"]=sorted({a[0] for a in absent})
        if frozen:
            # What the live instrument saw today, reported but NOT admitted. A firm here
            # that is not in the shipped _absence.csv is an instrument change AFTER the
            # window — never evidence about the firm (methodology.md §1).
            shipped=set()
            _ap=os.path.join(jp_dir,"_absence.csv")
            if os.path.exists(_ap):
                with open(_ap,newline="") as f:
                    for row in csv.DictReader(f):
                        if row.get("firm"): shipped.add(row["firm"].strip())
                summary["frozen_absence_firms"]=sorted(set(summary["absence_firms"])-shipped)

    # ---------- Source B: agency intelligence ----------
    # 2026-09-02: legacy competitor-intelligence/ deleted; the frozen 2026-06-15 panel now lives in
    # ../research/legacy/ (projects/northpoint/research/legacy/agency-panel-trend-data-asof-2026-06-15.json).
    td_path=os.path.join(sales,"..","research","legacy","agency-panel-trend-data-asof-2026-06-15.json")
    if not os.path.exists(td_path): td_path=os.path.join(sales,"competitor-intelligence","trend-data.json")
    if os.path.exists(td_path):
        td=load_json(td_path)
        summary["src_agency_date"]=td.get("lastUpdated")
        comp=td.get("competitors",{})
        firm_to_agencies={}  # tracked firm slug -> set(agency)
        for agency in AGENCY_PANEL:
            info=comp.get(agency) or comp.get(agency.replace("-"," ")) or {}
            entries=info.get("entries",[]) if isinstance(info,dict) else []
            if not entries: continue
            last=entries[-1]
            clients=last.get("recentClientsNamed",[]) or []
            # per-agency dated claim snapshot
            with open(os.path.join(ac_dir,f"{agency}.csv"),"w",newline="") as f:
                w=csv.writer(f); w.writerow(["date","claimed_client","is_tracked_firm","health_score","threat_level","source"])
                for cl in clients:
                    slug=match_tracked(cl)
                    if slug: firm_to_agencies.setdefault(slug,set()).add(agency)
                    w.writerow([last.get("date"),cl,"yes" if slug else "no",
                                last.get("healthScore"),last.get("threatLevel"),
                                f"research/legacy/agency-panel-trend-data-asof-2026-06-15.json {summary['src_agency_date']}"])
            summary["agency_files"]+=1
        # overlap matrix: tracked firm x agencies that claim it
        mpath=os.path.join(repo,"corpus","agency-overlap-matrix.csv")
        with open(mpath,"w",newline="") as f:
            w=csv.writer(f)
            w.writerow(["tracked_firm","claiming_agencies","agency_count","overlap_flag","as_of","source"])
            for slug,ags in sorted(firm_to_agencies.items(), key=lambda kv:(-len(kv[1]),kv[0])):
                w.writerow([disp(slug), "; ".join(sorted(ags)), len(ags),
                            "OVERLAP" if len(ags)>1 else "single",
                            summary["src_agency_date"],
                            "competitor-intelligence/trend-data.json"])
                summary["matrix_rows"]+=1
                if len(ags)>1: summary["overlaps"].append(f"{disp(slug)} ({', '.join(sorted(ags))})")

    # ---------- concrete summary ----------
    print("=== daily-corpus-sync summary ===")
    print(f"date: {today}")
    if summary.get("window_closed"):
        print(f"CLASS-1 CAPTURE WINDOW CLOSED ({summary['window_end']}) — class-1 corpus files FROZEN.")
        print("  _absence.csv / _chrome-queue.csv NOT rewritten (their as_of would re-date a shipped exhibit).")
        print("  Per-firm job rows NOT admitted. The feed is still read and reported below.")
        print("  _feed-fingerprint.json IS still written: an instrument log, not a corpus claim.")
    print(f"source A (jobs)   scan_date: {summary['src_jobs_date']}")
    _d=summary.get("feed_fingerprint_delta")
    _ds=("n/a" if _d is None else f"{_d:+d}")
    print(f"FEED HEALTH: {summary.get('feed_health','UNKNOWN')} "
          f"(scanned_at_utc={summary.get('feed_scanned_at')}, "
          f"age={summary.get('feed_age_hours')}h, "
          f"fingerprint total_jobs_fetched={summary.get('feed_fingerprint')}, "
          f"delta={_ds} vs {summary.get('feed_fingerprint_prior_date')} "
          f"({summary.get('feed_fingerprint_prior')}))")
    print(f"  reason: {summary.get('feed_health_reason','—')}")
    if not summary.get("absence_claim_permitted", False):
        print("  !! CLASS-1 ABSENCE CLAIM REFUSED: upstream ATS scan is stale, "
              "undatable, or did not move. A result of 0 new postings today means "
              "UNOBSERVED, not ABSENT. Do not write an absence claim for class 1.")
    print(f"source B (agency) lastUpdated: {summary['src_agency_date']}")
    print(f"job postings ADDED: {summary['job_added']}  firms: {sorted(summary['job_firms'])}")
    print(f"  of which via Chrome inbox: {summary['chrome_ingested']}")
    if summary.get("window_closed"):
        print(f"  post-window rows OFFERED but NOT admitted: {summary['frozen_job_rows']} "
              f"firms: {sorted(set(summary['frozen_job_firms']))}")
    print(f"chrome work-queue (proprietary tracked firms): {summary['chrome_queue_firms']}")
    print(f"tracked firms STILL w/o coverage (absence=data): {summary['absence_firms']}"
          + ("  [LIVE READ — not written to the shipped exhibit]" if summary.get("window_closed") else ""))
    if summary.get("window_closed") and summary.get("frozen_absence_firms"):
        print(f"  !! POST-WINDOW ABSENCE-PANEL DRIFT: {summary['frozen_absence_firms']} "
              "appear in today's live read but NOT in the shipped _absence.csv. "
              "This is a change in INSTRUMENT REACH after the window, not evidence about the firm. "
              "Not written. Report it as instrument state, never as a class-1 finding.")
    print(f"agency-claims files written: {summary['agency_files']}")
    print(f"agency-overlap-matrix rows: {summary['matrix_rows']}")
    print(f"agency OVERLAPS on tracked firms: {summary['overlaps']}")
    return summary

if __name__=="__main__":
    main()
