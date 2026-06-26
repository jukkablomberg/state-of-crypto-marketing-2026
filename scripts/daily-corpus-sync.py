#!/usr/bin/env python3
"""
daily-corpus-sync.py — State of Crypto Marketing 2026

Deterministic daily corpus producer. Turns NorthPoint's already-running daily
data feeds into citation-anchored corpus output WITHOUT depending on web search:

  Source A (job postings):  northpoint/sales-funnel/prospects/open-positions.json
                            (daily ATS API scan: greenhouse/ashby/lever/breezy/... ,
                             URL-verified, dated, seniority-scored)
  Source B (agency intel):  northpoint/sales-funnel/competitor-intelligence/trend-data.json
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

def main():
    ap=argparse.ArgumentParser()
    here=os.path.dirname(os.path.abspath(__file__))
    repo_default=os.path.dirname(here)
    ap.add_argument("--repo", default=repo_default)
    # repo lives at <projects>/state-of-crypto-marketing-2026/repo ; sales-funnel is a sibling project
    ap.add_argument("--sales", default=os.path.join(repo_default, "..", "..", "northpoint", "sales-funnel"))
    args=ap.parse_args()
    repo=os.path.abspath(args.repo); sales=os.path.abspath(args.sales)
    today=datetime.date.today().isoformat()
    jp_dir=os.path.join(repo,"corpus","job-postings")
    ac_dir=os.path.join(repo,"corpus","agency-claims")
    os.makedirs(jp_dir,exist_ok=True); os.makedirs(ac_dir,exist_ok=True)

    summary={"job_added":0,"job_firms":set(),"absence_firms":[],"matrix_rows":0,
             "agency_files":0,"overlaps":[],"src_jobs_date":None,"src_agency_date":None}

    # ---------- Source A: job postings ----------
    op_path=os.path.join(sales,"prospects","open-positions.json")
    if os.path.exists(op_path):
        op=load_json(op_path)
        summary["src_jobs_date"]=op.get("scan_metadata",{}).get("scan_date")
        roles=[]
        for key in ("new_since_last_scan","still_open_from_prior_scans"):
            roles += op.get(key,[])
        by_firm={}
        for j in roles:
            slug=match_tracked(j.get("company",""))
            if not slug: continue
            by_firm.setdefault(slug,[]).append(j)
        for slug,js in sorted(by_firm.items()):
            path=os.path.join(jp_dir,f"{slug}.csv")
            existing=read_existing_urls(path)
            new_rows=[]
            for j in js:
                url=(j.get("url") or j.get("apply_url") or "").strip()
                if not url or url in existing: continue
                existing.add(url)
                new_rows.append([
                    j.get("posted_at") or j.get("first_seen") or "",
                    j.get("title",""),
                    j.get("location",""),
                    f"{seniority_of(j.get('title',''))} / {func_of(j.get('title',''))}",
                    url, today,
                    f"ATS={j.get('ats','')}; url_verified={j.get('url_verified')}; src=open-positions.json {summary['src_jobs_date']}",
                ])
            if new_rows:
                write_header=not os.path.exists(path) or os.path.getsize(path)<=len(",".join(JOB_HEADER))+3
                # rewrite cleanly if file is just an empty scaffold
                scaffold = os.path.exists(path) and read_existing_urls(path)==set()
                mode="w" if (not os.path.exists(path) or scaffold) else "a"
                with open(path,mode,newline="") as f:
                    w=csv.writer(f)
                    if mode=="w": w.writerow(JOB_HEADER)
                    for r in new_rows: w.writerow(r)
                summary["job_added"]+=len(new_rows); summary["job_firms"].add(disp(slug))
        # absence-as-data: tracked firms in needs_chrome_fallback / fetch_errors
        absent=[]
        for item in op.get("needs_chrome_fallback",[]):
            slug=match_tracked(item.get("company",""))
            if slug: absent.append((disp(slug),"proprietary-ATS/needs-chrome", item.get("careers_url","")))
        for item in op.get("fetch_errors",[]):
            slug=match_tracked(item.get("company",""))
            if slug: absent.append((disp(slug),"api-fetch-error", item.get("error","")[:120]))
        if absent:
            with open(os.path.join(jp_dir,"_absence.csv"),"w",newline="") as f:
                w=csv.writer(f); w.writerow(["firm","reason","detail","as_of"])
                for fm,rs,dt in sorted(set(absent)): w.writerow([fm,rs,dt,today])
            summary["absence_firms"]=sorted({a[0] for a in absent})

    # ---------- Source B: agency intelligence ----------
    td_path=os.path.join(sales,"competitor-intelligence","trend-data.json")
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
                                f"competitor-intelligence/trend-data.json {summary['src_agency_date']}"])
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
    print(f"source A (jobs)   scan_date: {summary['src_jobs_date']}")
    print(f"source B (agency) lastUpdated: {summary['src_agency_date']}")
    print(f"job postings ADDED: {summary['job_added']}  firms: {sorted(summary['job_firms'])}")
    print(f"tracked firms w/o API coverage (absence=data): {summary['absence_firms']}")
    print(f"agency-claims files written: {summary['agency_files']}")
    print(f"agency-overlap-matrix rows: {summary['matrix_rows']}")
    print(f"agency OVERLAPS on tracked firms: {summary['overlaps']}")
    return summary

if __name__=="__main__":
    main()
