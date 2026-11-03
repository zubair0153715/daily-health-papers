# Health Papers Agent — 5 health papers per day

**Ordered by Zubair 2026-11-03 ~18:24 PKT:** "ek agent banao jo daily 5 papers
bana ke submit karta jae health-related problems ke solutions ke liye."
Built 2026-11-03. Goal: `pharmacy-research-paper-team-daily-digest-and-manuscripts`.
This is SEPARATE from the existing `daily-research-paper` cron (1/day,
Health→Brain→Space rotation) — that cron is untouched.

## What it does

Every day the agent picks **5 different health problems** (solutions-oriented,
computational drug-discovery style, same pattern as Papers #1 and #3) and for
each produces a full manuscript + PDF + validated submission-pack entry, then
prepares a ChemRxiv draft up to the final review page and STOPS.

**Submission rule (standing, non-negotiable): the agent NEVER presses submit.
The author presses submit himself, via browser takeover, one draft at a time.**

## Daily flow (one paper at a time — checkpointed)

For each of the 5 topics, in order, finish the paper completely before
starting the next. A timeout or failure therefore leaves finished papers,
never five half-papers.

1. **Pick topics** — `pick_topics.py --n 5 --date <today> --mark-used`.
   Reads `topics-pool.json` + `hidden_files/health-papers-tracker.json`.
   Never repeats a topic id or a used title. Spreads across areas
   (max 2 per area per day).
2. **Literature sweep** — latest digest at `~/workspace/research-team/digests/`
   + targeted PubMed / bioRxiv / ChEMBL checks for that topic. Research
   agents per `~/workspace/custom-skills/research-agents/SKILL.md` where
   they work; today they are mostly blocked (Co-Scientist 429 on free key,
   Mimosa smoke run incomplete, Denario GUI-only, EvoScientist not
   onboarded) — so the run drafts from the digest + targeted searches +
   own computation, exactly how Papers #1–#3 were written. A blocked agent
   never blocks a paper.
3. **Computation** — `run_docking.py --target "<target>" --ref "<drug>"`
   (LeadForge pipeline: UniProtKB → ChEMBL → PubChem → RDKit →
   PAINS/ADMET → Vina docking vs the reference drug, same protocol).
   Run with `~/workspace/.venv-fc/bin/python` (only env with RDKit) and
   the cleaned `NO_PROXY=localhost,127.0.0.1,::1`. If no experimental
   structure exists, docking is SKIPPED and the paper says so honestly.
   Budget ~15–30 min per topic.
4. **Manuscript** — full paper from `manuscript-template.md`: Title,
   Abstract, Keywords, Introduction, Methods, Results, Discussion,
   Limitations, Conclusion, Acknowledgments (AI disclosure REQUIRED in
   the text), References (verified only), Data availability. Header on
   every paper: "AI-assisted draft — NOT peer-reviewed, NOT published.
   All claims require independent laboratory verification."
   Save as `files/YYYY-MM-DD-health-<slug>.md`.
5. **PDF** — `hidden_files/md2pdf.py <md> <pdf>` (reportlab, no pandoc).
6. **Pack** — `make_pack.py <md> --append files/submission-pack-YYYY-MM-DD.md`.
   Fails loudly if the abstract is >2,500 chars or keywords are not 3–10.
   A paper is only "done" when its pack entry validates.
7. **Tracker** — append the paper to
   `hidden_files/health-papers-tracker.json` (topic id, date, title, file,
   status `drafted`, draft_url once the ChemRxiv draft exists).
8. **ChemRxiv draft** — one browser task per paper (normal browser-task
   route, signed in as Zubair Ali via ORCID): new submission, upload the
   PDF, fill title / verbatim abstract / keywords / subject area
   (Medicinal Chemistry / Chemical Biology → closest form label
   "Biological and Medicinal Chemistry") / CC BY 4.0 / Working Paper /
   Ethics "Not relevant" / Conflicts "No", affiliation
   "SMBBMU, Larkana, Pakistan", stop at the final review (Summary) page.
   Do NOT press submit. Record the draft URL in the tracker. If a draft
   fails (Cloudflare verify-then-reset loops are the known failure mode —
   Paper #1's first attempt burned 6.5h and failed), log it and move to
   the next paper; retry that paper's draft next day, never loop on it.
9. **GitHub** — commit + push the day's papers, pack, tracker and any
   pipeline changes to `github.com/zubair0153715/daily-health-papers`
   (public). Everything built goes to GitHub, per his standing rule.
10. **Report** — in the main chat: the 5 titles + draft URLs (or which
    drafts failed and why) + count. Compact, numbered, Roman-Urdu.

## Files

| File | What it is |
|---|---|
| `README.md` | this file |
| `topics-pool.json` | 60 seed topics (source of truth) |
| `topics-pool.md` | readable rendering of the pool (generated) |
| `pick_topics.py` | dedup picker (stdlib only) |
| `run_docking.py` | LeadForge pipeline + Vina wrapper |
| `make_pack.py` | pack extraction + ChemRxiv limit validation |
| `manuscript-template.md` | paper skeleton (Papers #1/#3 pattern) |
| `../hidden_files/health-papers-tracker.json` | every paper: topic, date, status, draft URL |
| `../hidden_files/md2pdf.py` | md → PDF renderer (shared with the 1/day cron) |

## ChemRxiv facts (verified live 2026-11-02/03)

- ORCID required for the submitting author; sign-in via ACS CONNECT.
- Main file: PDF up to 100 MB. Abstract max 2,500 chars. Keywords 3–10,
  each 3–50 chars. Exactly one primary subject area.
- Affiliation institution ≤40 chars: "SMBBMU, Larkana, Pakistan" (26).
  NOTE: the metadata editor 404'd on both Paper #1 and Paper #3, so both
  submitted with the auto-extracted full university name — accepted as-is.
  Try the editor once per draft; never block on it.
- Screening 2–3 business days; DOI on posting; default CC BY 4.0.
- AI disclosure must be IN the preprint text (no form field).

## Hard rules

- No card ever, free tiers only. No purchase, no paid API.
- No invented data, PMIDs, DOIs or citations. Every number traces to a
  real source or a real computation. Every paper states its limits
  honestly (Vina ±1–2 kcal/mol noise, PAINS alerts, no lab data).
- Never auto-submit anything. Never store or reuse any credential from
  chat. The real Gemini key (if ever pasted) is transient-only, never
  written to any file, log or memory.
- Never repeat a topic. Never ship a partial paper.

## Honest feasibility — read this before judging the first week

**Target: 5 papers/day. Floor: 2 complete papers/day, guaranteed.**
The pipeline is built to attempt 5 every day and to report the real count.
5/day at the Papers #1/#3 standard is the stretch goal, not a proven rate —
the binding constraints are:

1. **Browser drafts (biggest risk).** One ChemRxiv draft takes 10–20 min
   when Cloudflare cooperates and can fail outright when it does not
   (Paper #1's first attempt: 6.5h, failed, form never filled). Five
   drafts/day = 1–2h of browser work with a real daily chance that one
   fails. The design isolates failures per paper so one bad draft cannot
   kill the other four.
2. **Author's own submit load.** Each draft still needs HIM to take over
   the browser and press submit — five manual submits a day is a heavy
   ask on top of his Pharm-D term and the 4 Nov exam. If he cannot keep
   up, drafts pile up (which is fine — drafts wait in My Documents).
3. **ChemRxiv load.** 5 submissions/day = ~35/week from one account.
   No published daily limit was found, but a sudden 35/week from a new
   account may draw moderation scrutiny or throttling. Watch the first
   week's screening times; if they stretch past 3 business days, drop
   the target to 3/day and tell him.
4. **Manuscript quality at volume.** One dense paper is ~2,000–2,500
   words of technical English plus a literature sweep and a docking run.
   Five in one agent run is a lot of output; papers 4–5 are where
   repetition and thin grounding will show first. The per-paper
   checkpoint + the template + the pack validator are the guards; the
   author still reads before submitting.
5. **Research-agent limits.** The four installed agents cannot carry
   this load today (see §2 above). The pipeline runs on the main agent's
   own research + own computation, which is proven (Papers #1–#4) but
   is the reason the floor is 2, not 5.

**Realistic steady state until proven otherwise: 2–3 papers/day.**
If the first week delivers 5/day cleanly (5 manuscripts + 5 drafts,
screening on time), raise the floor. If it delivers 2–3, that is the
rate — say so, do not fake 5 by thinning papers.

## Manual run

```bash
cd ~/workspace/goals/pharmacy-research-paper-team-daily-digest-and-manuscripts/health-papers-agent
python3 pick_topics.py --n 5 --date $(date +%F) --mark-used
NO_PROXY=localhost,127.0.0.1,::1 ~/workspace/.venv-fc/bin/python run_docking.py \
  --target "<target>" --ref "<drug>" \
  --out ../hidden_files/dock-HP-XXX-$(date +%F).json
# draft the manuscript from manuscript-template.md, then:
python3 ../hidden_files/md2pdf.py ../files/YYYY-MM-DD-health-<slug>.md ../files/YYYY-MM-DD-health-<slug>.pdf
python3 make_pack.py ../files/YYYY-MM-DD-health-<slug>.md --append ../files/submission-pack-$(date +%F).md
```

## Schedule

Cron `daily-health-papers-5`, daily ~15:00 PKT (flexible), owner
`goal:pharmacy-research-paper-team-daily-digest-and-manuscripts`,
timeout 6h requested. Does NOT touch the `daily-research-paper` cron
(11:23 PKT, 1/day rotation) — both run.
