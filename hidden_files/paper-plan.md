# Daily Research Papers — Plan (standing order 2026-11-02)

User order (2026-11-02 ~19:28 PKT): use the four installed research agents
(Denario, EvoScientist, Mimosa, Co-Scientist), combined or separately, to
their best use — write ONE full research paper per day, NEW research,
in three fields: **Health** (his Pharm-D field), **Brain** (neuroscience),
**Space** (asmaan — astronomy/space).

## Rotation (5-day cycle — EXPANDED 2026-11-14, his order)
- **Health → Brain → Space → Natural Science → Social Science → Health …**
- Natural Science scope: physics, chemistry, climate, energy, environment, materials, water — quantitative results a ministry or engineer can use (a budget, a rate, a threshold).
- Social Science scope: economics, education, health policy, institutions — causal claims about people, identified by RCT / natural experiment / quasi-experimental design, with an effect size and a named policy lever.
- **Method standard (2026-11-14): Harvard / MIT / Oxford policy-shaping professors.** Every run reads `files/method-brief-policy-shaping-professors.md` FIRST: Banerjee & Duflo (RCTs), Acemoglu/Johnson/Robinson (institutions), Raj Chetty (Opportunity Atlas), Thaler & Sunstein (nudges), Heckman (Perry Preschool), Hanushek (teacher value-added), Rodrik (growth diagnostics), Deaton (measurement), Haynes & Gawande (surgical checklist), Pacala & Socolow (climate wedges), Myles Allen (carbon budget). The 10-point checklist applies to EVERY paper: one falsifiable question + named falsifier; causal identification named; mechanism section; effect size + uncertainty (never p-values alone); analysis plan stated before results; replication + data availability; limitations that bite; **Policy implications section naming the decision-maker and the exact change**; comparison vs the strongest incumbent; one clean memorable number. What does NOT count: untested frameworks (the exact reason ChemRxiv rejected Papers #1/#3 v1), cherry-picked examples, claims without a falsifier. These scholars are the STANDARD, never co-authors — never claim their endorsement.
- Tracker: `hidden_files/paper-rotation.json` — `{"last_date": ..., "last_field": ..., "count": {...}}`. The daily run reads it, picks the next field, writes the paper, updates it.
- Today: Mon 2026-11-02 = Health #1 (thymoquinone / aldose reductase).

## Full-research standard — pattern stays the SAME every day (user's order 2026-11-03 ~08:26 PKT)
Every paper, every field, same complete pattern — nothing partial, nothing left half-done:
1. **Full research, not a summary** — fresh literature sweep (digest + targeted PubMed/bioRxiv/arXiv) + the paper's own analysis. No paper without its own falsifiable claim and how to test it.
2. **Health papers run the FULL AI drug-discovery process** — the complete LeadForge pipeline, not a piece of it: target → ChEMBL/PubChem ligands → RDKit descriptors → PAINS + ADMET check → Vina docking against the real structure (or an honest "no structure exists" note) → ranked leads vs the reference drug. A drug claim without docking/descriptors/PAINS is not a complete paper.
3. **Ready to send, same day** — manuscript + PDF + submission pack: abstract within the preprint limit (ChemRxiv ≤2,500 chars), 3–10 keywords, one primary subject area, AI-assistance disclosure in the text, author line (Zubair Ali, Pharm-D student, SMBBMU Larkana) + ORCID 0009-0001-5921-7509. A paper is only "done" when its submission pack is done.
4. **Every thing complete** — Title, Abstract, Keywords, Introduction, Methods (reproducible), Results (own numbers), Discussion, Limitations, Conclusion, References, Data availability. No section skipped, no number without a source.

## Health track — sharpened focus (user's order 2026-11-03 ~08:23 PKT)
- Health papers focus FIRST on: finding cures for diseases, discovering new drugs, improving existing medicines/drugs — plus tracking world-level research happening now.
- Quality bar: Harvard-level / professor-level PATTERN — top-tier structure and rigor: structured abstract, clear falsifiable hypothesis, methods reproducible from the text, honest limitations, real references only. The STANDARD is Harvard-level; the content stays honest: AI-assisted drafts, computational leads only, lab validation still required before any claim. Never present a draft as a published Harvard-level paper.
- Brain and Space tracks continue on rotation as before. **From 2026-11-14 the rotation is 5 fields (Health → Brain → Space → Natural Science → Social Science) — see Rotation above.**

## LeadForge drug-discovery papers — on the website (user's order 2026-11-14)
- Every LeadForge weekly paper draft (`leadforge-weekly-paper-YYYY-MM-DD.md`) is copied into `files/YYYY-MM-DD-drugdiscovery-leadforge-weekly-N.md` with a proper title + AI-assisted header, PDF generated via `hidden_files/md2pdf.py`, and shown on the papers website under the **Drug Discovery** section. New weekly papers are added the same way by the daily website-refresh run. The daily LeadForge run reports stay in the LeadForge goal folder (they are run logs, not manuscripts).

## What a paper is
- Full manuscript in English: Title, Abstract, Keywords, Introduction,
  Methods, Results, Discussion, Limitations, Conclusion, References,
  plus a "Data availability" note. Saved as
  `files/YYYY-MM-DD-<field>-<slug>.md`.
- Novelty: a NEW synthesis, hypothesis, or computational lead — never a
  copy of an existing paper, never a summary of one paper. Each paper must
  state its own falsifiable claim and how to test it.
- Sources: today's research digest (~/workspace/research-team/digests/),
  targeted PubMed / bioRxiv / arXiv checks, and his own lab/computational
  data where it exists (black-seed docking, LeadForge, ResistMap).
- HARD RULES: no invented data, no invented PMIDs/DOIs/citations, no fake
  results. Every number traces to a real source file or a real paper.
  Every paper carries the header: "AI-assisted draft — NOT peer-reviewed,
  NOT published. All claims require independent verification."
  Never submit or publish anywhere. His name as author (Zubair Ali,
  Pharm-D student, SMBBMU Larkana); Lapis credited as drafting assistant.

## Agent use (status 2026-11-02)
- **Registered as a skill 2026-11-02:** `~/workspace/custom-skills/research-agents/SKILL.md`
  — the four tools are now part of Lapis's own system (routing, launch
  commands, auth rules, known blockers). Read the skill before any agent
  run; keep it current when a blocker changes.
- Co-Scientist: INSTALLED, templates fixed, Gemini config ready — BLOCKED
  on auth: the stored Gemini key reaches Google only as a URL `?key=`
  surrogate; Co-Scientist needs it in the Authorization header. Needs the
  REAL key in the run shell (transient, user pastes once) — user has NOT
  agreed to that yet. Do not ask every day; the key question is his call.
- Denario: GUI only (localhost:8501, not reachable from his phone) — use
  via Co-Scientist goal text when Denario is reachable; otherwise skip.
- Mimosa: litellm patch in progress (subagent, 2026-11-02) to send the key
  as `?key=` to the native endpoint. If it lands, Mimosa does the daily
  literature synthesis step.
- EvoScientist: needs `EvoSci onboard` (his interactive step) — use for
  evolving hypotheses (SGLT2 analog) once onboarded.
- Until agents are fully live, the daily run drafts with the main agent's
  own research (digest + targeted searches) and uses any agent that works.

## Daily run (cron `daily-research-paper`, ~11:00 PKT)
1. Read this plan + rotation tracker; pick today's field.
2. Sweep fresh literature for that field (digest + targeted searches).
3. Draft the full manuscript; save to `files/`.
4. Update the rotation tracker.
5. Report in chat: title + 3-line summary + file link. Nothing else.
