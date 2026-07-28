# SUPERSEDED — see `bafin-risks-in-focus-crypto-finfluencer-2026-01.md`

**This file is a tombstone. Do not cite it.**

The BaFin *Risks in Focus 2026* corpus entry was created on 2026-07-27 with a publication date of **18 February 2026**, taken from a secondary source (SAFE Frankfurt's write-up of a presentation of the report). It was flagged `[VERIFY]` in that same entry.

On **2026-07-28** the date was checked against BaFin's own press release and found to be **wrong by three weeks**. The report was published **28 January 2026**.

**Canonical file:** `./bafin-risks-in-focus-crypto-finfluencer-2026-01.md`
**Primary date source:** https://www.bafin.de/SharedDocs/Veroeffentlichungen/EN/Pressemitteilung/2026/pm_2026_01_28_PK_Risiken_im_Fokus_en.html

## Why this stub exists rather than a clean rename

Two reasons, both recorded rather than smoothed:

1. **Audit trail.** This path is cited in `../weekly-runs/2026-07-27-corpus-run-2.md`, in `../../findings/longitudinal-2026-06.md`, and in commit `225500c`, which is already on `origin/main`. Under the precedent set on 2026-07-27 (do not overwrite or vanish audit-trail files), a dangling citation is worse than a stub.
2. **Mount constraint.** The repo mount returns `Operation not permitted` on `unlink`, so autonomous runs cannot delete files or complete a `git mv`. This is the same defect that blocks `.git/index.lock` removal and requires the `GIT_INDEX_FILE` workaround. Logged for Jukka; a manual `git rm` on a local checkout will retire this stub cleanly.
