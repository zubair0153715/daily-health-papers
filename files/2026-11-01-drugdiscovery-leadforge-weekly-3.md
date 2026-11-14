# Computational small-molecule triage against seven high-burden disease targets (week of 26 Oct-1 Nov 2026)

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan · **Drafting assistant:** Lapis (AI)

## Week of 2026-10-26 → 2026-11-01 (7 daily targets)

**STATUS: DRAFT ONLY — never submit. Journal submission is Zubair's action under his own name.**

---

## Proposed title (placeholder)
"Computational small-molecule triage against seven high-burden disease targets using live public chemical data (LeadForge AI pipeline): a seven-day screening campaign"

## Abstract
We describe a reproducible, fully automated computational triage pipeline that runs daily against one
high-burden disease target, using only live public data sources (UniProtKB, ChEMBL, PubChem, the RCSB
Protein Data Bank). Each daily run executes seven steps: (1) target identification from UniProtKB,
(2) known-ligand retrieval from ChEMBL, (3) query-drug verification from PubChem, (4) Morgan-fingerprint
/ Tanimoto similarity screening with RDKit, (5) ADMET screening (Lipinski, Veber, PAINS, ToxGuard
Tox21 kNN read-across), (6) composite-score lead ranking, and (7) AutoDock Vina docking (meeko ligand
preparation) against the best available experimental structure. Across the week of 2026-10-26 to
2026-11-01 we screened seven targets spanning antifungal (Candida CYP51), antiviral (SARS-CoV-2 Mpro,
influenza neuraminidase, HIV-1 integrase — attempted), antimicrobial resistance (MRSA PBP2a) and
tuberculosis (MmpL3) and Alzheimer's disease (BACE1). Each run included a rediscovery control
(verifying the pipeline recovers the reference drug or its scaffold from ChEMBL) and a head-to-head
docking comparison between ranked leads and the reference therapy. Honest interpretation is enforced
at every step: docking margins within ±1 kcal/mol are reported as noise-equivalent, failed or
wrong-target runs are reported as failures rather than re-labelled, and all candidates are presented
as computational starting points requiring wet-lab validation. No efficacy or therapeutic claims are
made. Two runs this week produced above-noise docking margins (CYP51, PBP2a); two runs were invalid
or corrected mid-run (HIV-1 integrase, MmpL3) and are reported as such.

**Keywords:** virtual screening; AutoDock Vina; ChEMBL; target triage; CYP51; Mpro; PBP2a; MmpL3; BACE1; neuraminidase; HIV-1 integrase

## Introduction (draft)
Drug discovery for high-burden diseases in resource-limited settings needs a cheap, reproducible first
filter: a computational triage step that converts open chemical data into a short wet-lab shortlist.
This draft reports one week of daily automated screening from the LeadForge AI pipeline. The scope is
deliberately narrow — *computational candidate triage only* — and the methods are designed so any
other group can re-run them against the same live databases. This week is notable for its failures
as much as its hits: two of the seven runs exposed target-mapping traps (polyprotein accessions,
missing ChEMBL components) that the pipeline caught and reported rather than silently passing.

### Target selection rationale
Targets were chosen for disease burden and the presence of a marketed or clinical-stage reference small
molecule for head-to-head comparison:
- **Antifungal:** Candida albicans CYP51/ERG11 (fluconazole)
- **Antiviral:** SARS-CoV-2 Mpro (nirmatrelvir), influenza A neuraminidase (oseltamivir), HIV-1 integrase (dolutegravir — attempted, invalid run)
- **Antimicrobial resistance:** MRSA PBP2a (ceftaroline)
- **Tuberculosis:** M. tuberculosis MmpL3 (SQ109)
- **Alzheimer's disease:** BACE1 (verubecestat)

## Methods (draft)
### 7.1 Daily pipeline (identical all 7 days)
1. Target identification: UniProtKB live search → human/pathogen protein, accession recorded.
2. Known-ligand retrieval: ChEMBL target (accession-mapped), top bioactivities by pChEMBL.
3. Query-drug verification: reference small-molecule drug confirmed live via PubChem PUG REST.
4. Similarity screen: RDKit Morgan fingerprints, Tanimoto vs known actives, top 25 kept.
5. ADMET screen: Lipinski / Veber rules, PAINS filters, ToxGuard Tox21 kNN read-across (12 assays).
6. Lead ranking: composite score (similarity 40 + Lipinski 20 + Veber 10 + PAINS 10 + tox 20).
7. Docking: AutoDock Vina, meeko ligand prep, best available experimental structure (X-ray preferred),
   box 22.5 Å, exhaustiveness 8, 3 poses; reference drug docked head-to-head in the same grid.

### 7.2 Rediscovery control
Each run includes a rediscovery check: whether the pipeline recovers the reference drug's scaffold
from the ChEMBL ligand set (positive controls validate the screen; negatives bound its recall).

### 7.3 Honest-interpretation rules (applied in every run)
- Docking differences < ~1 kcal/mol = method noise, never "wins".
- Measured Ki/IC50 values come from heterogeneous ChEMBL assays — directional, not rankings.
- When docking and measured potency disagree, the disagreement is reported, not averaged away.
- ToxGuard outputs are kNN read-across: "no red flag found", not "proven safe".
- All leads are existing ChEMBL compounds; patent paths need university/teacher review.
- A run whose docking structure or ChEMBL target is wrong is reported as invalid, with the
  corrected re-run (if any) replacing it — never silently re-labelled.

## Results — weekly summary table
| Day | Target | Reference drug | Bioactivities | Top lead (computational pick) | Beat reference? |
|---|---|---|---|---|---|
| Mon 10-26 | HIV-1 integrase (P04585 Gag-Pol) | dolutegravir | 52 | CHEMBL3683705 | NO VERDICT — docking ran against HIV-1 protease (6DV4), not integrase; +0.03 kcal/mol is noise at the wrong target |
| Tue 10-27 | C. albicans CYP51/ERG11 (P10613) | fluconazole | 33 | CHEMBL5566404 (IC50 256 nM) | Yes on paper: −10.70 vs −7.13 (+3.57) — exceeds noise, still needs assay |
| Wed 10-28 | SARS-CoV-2 Mpro (P0DTD1) | nirmatrelvir | 51 | CHEMBL5574604 (Ki 0.04 nM) | +0.95 kcal/mol — just under the noise floor; close analog (sim 0.913), not a scaffold hop |
| Thu 10-29 | MRSA PBP2a / MecA (Q93IC2) | ceftaroline | 4 | CHEMBL4862632 (Kd 264 nM) | Yes on paper in BOTH structures: −10.52/−10.08 vs −8.84/−8.88 (+1.68/+1.20) — exceeds noise; wet-lab pick is CHEMBL4847813 (Kd 129 nM) instead |
| Fri 10-30 | M. tuberculosis MmpL3 (P9WJV5) | SQ109 | 3 (smegmatis homologue) | CHEMBL5436935 (Ki 158.5 nM, smegmatis) | +1.14 kcal/mol — above noise, but homologue-guided only; Mtb activity unconfirmed |
| Sat 10-31 | Influenza A neuraminidase (Q6DPL2) | oseltamivir | 1,152 (60 pulled, 23 unique) | CHEMBL5417759 (carboxylate analog) | +0.39 kcal/mol — within noise; validation run, not a discovery |
| Sun 11-01 | BACE1 (P56817) | verubecestat | 54 | CHEMBL4861687 (IC50 0.25 nM) | +0.16 kcal/mol — within noise; no meaningful win |

### Per-target result notes (from daily reports)
- **HIV-1 integrase (10-26): INVALID RUN, no verdict.** UniProt P04585 is the whole Gag-Pol
  polyprotein (protease + RT + integrase), and the PDB auto-pick returned 6DV4 — an HIV-1
  **protease** structure. Dolutegravir's −9.88 and CHEMBL3683705's −9.91 are cross-docking at a
  protease site, meaningless for integrase. Lesson recorded for the rotation: an integrase re-run
  needs an integrase-specific UniProt entry / ChEMBL integrase target, never the polyprotein.
- **CYP51 (10-27):** strongest docking margin of the week. CHEMBL5566404 −10.70 (+3.57 vs
  fluconazole −7.13), CHEMBL5094280 −9.88 (+2.75), and CHEMBL638 = **voriconazole** −7.69
  (+0.56) — an approved antifungal recovered by the screen. Fluconazole's own ChEMBL record
  (CHEMBL106, Kd 45 nM) docked −6.91. All three beating leads carry prior reported ChEMBL
  activity (IC50/Kd 45–323 nM) — known chemotypes, not novel molecules. Structure 5TZ1, X-ray
  2.0 Å. Human CYP51A1 was explicitly excluded; this is the fungal ERG11 target.
- **Mpro (10-28):** CHEMBL5574604 −9.21 vs nirmatrelvir −8.26 (+0.95, just under the ±1
  kcal/mol floor) with measured Ki 0.04 nM — more potent than nirmatrelvir's reported Ki
  0.26 nM — but similarity 0.913, a close analog, not a new scaffold. Docking used 7VH8
  (1.59 Å), the reference drug's own co-crystal, after two failed attempts: the stock run
  picked maltase-glucoamylase (CHEMBL2074) and the auto-picked PDB 7TX0 was the NSP3
  macrodomain, not Mpro. Polyprotein accessions defeat PDB auto-pick — verify the structure
  title before docking.
- **PBP2a (10-29):** the week's most careful run. Two independent structures (1MWS, 2.00 Å;
  3ZG0, 2.60 Å, ceftaroline's own co-crystal) both agree: CHEMBL4862632 beats active
  ceftaroline by +1.68/+1.20 kcal/mol, and CHEMBL4847813 beats it in both too. But the
  docking winner is NOT the wet-lab pick: CHEMBL4847813 has the strongest measured MecA
  binding (Kd 129 nM) and clean ADMET, while CHEMBL4862632 has the weakest Kd (264 nM),
  a Veber fail and a higher tox flag. Docking ≠ potency, stated in the report. Data is
  thin — only 4 ChEMBL MecA ligands exist (CHEMBL3512 PBP2a has zero bioactivities) — and
  the first attempt (wrong MecA adapter protein P60185 → maltase-glucoamylase) was
  discarded. Ceftaroline itself was not recovered in the mined set (no pChEMBL record).
- **MmpL3 (10-30):** CHEMBL5436935 −9.02 vs SQ109 −7.88 (+1.14) and CHEMBL5428840 −8.78
  (+0.90) — above/near noise — but all measured activities are against **M. smegmatis**
  MmpL3, the laboratory homologue: ChEMBL holds no M. tuberculosis MmpL3 target, so the
  ranking is homologue-guided triage and Mtb activity is unconfirmed. Rediscovery positive
  (CHEMBL561057 = SQ109 chemotype, sim 1.000). Stock run picked maltase-glucoamylase and
  was discarded. Structure 7NVH, 3.02 Å (cryo-EM-era resolution, noted honestly).
- **Neuraminidase (10-31):** validation, not discovery. Rediscovery positive (oseltamivir
  CHEMBL1229, sim 1.000, IC50 0.06 nM, score 100). Top docking hits are oseltamivir
  itself, its active metabolite (carboxylate, −6.97) and a close analog (−6.98) vs
  reference −6.59 — all within noise, and docking was against the H274Y resistant mutant
  (3CKZ, 1.9 Å), not wild-type. Stock run picked human ABL1 kinase (CHEMBL1862) via the
  "NA"-in-"kiNAse" substring trap and was discarded. Same bug class as MmpL3: viral /
  non-human targets need an explicit ChEMBL target check, never the stock fallback.
- **BACE1 (11-01):** no meaningful win. CHEMBL4861687 −10.11 (+0.16) and CHEMBL5092328
  −10.00 (+0.05) vs verubecestat −9.95 — inside noise. The strongest measured binder,
  CHEMBL3982593 (IC50 0.011 nM, pChEMBL 10.96), docks *worse* than the reference
  (−9.50) — another docking-vs-measured disconnect. All top leads are amidine/thiazine
  analogs of verubecestat — low novelty. Target-level context: verubecestat failed Phase
  III (EPOCH stopped Feb 2017 for futility; APECS Feb 2018; NEJM 2018 no benefit, worsened
  cognition), so BACE1 carries clinical target risk beyond any binding score. Structure
  7MYI, X-ray 1.25 Å (LY3202626 series co-crystal). Rediscovery negative — verubecestat
  absent from the 54 screened ligands. SR-MMP ToxGuard read-across 0.42–0.81 flagged for
  follow-up.

## Weekly tallies (final)
- 7/7 runs completed with docking numbers; 1 (HIV-1 integrase) with NO valid verdict — docking
  ran against the wrong protein and is reported as invalid, not as a result.
- Rediscovery positives: 3 of 7 (MmpL3 SQ109 chemotype, neuraminidase oseltamivir, CYP51
  fluconazole record CHEMBL106); negatives: BACE1, PBP2a (reference absent from the mined
  ChEMBL set); Mpro/PBP2a notes per daily reports — verify against daily JSONs before citing.
- Above-noise docking margins: 2 runs (CYP51 +3.57/+2.75; PBP2a +1.68/+1.20 in two
  structures) plus MmpL3 +1.14 (homologue-guided only) — all still assay-gated, never
  declared wins.
- Within-noise "better than reference" candidates: 3 runs (Mpro +0.95, neuraminidase +0.39,
  BACE1 +0.16) — priority candidates only, or validation-only in the neuraminidase case.
- Stock-pipeline target bugs caught and discarded: 5 incidents across 4 runs (HIV-1 integrase auto-pick,
  Mpro attempt 1 target + auto-pick, MmpL3, neuraminidase, PBP2a attempt 1) — the week's dominant method
  lesson is that polyprotein accessions and non-human targets defeat the stock fallback;
  accession/organism verification before any run is trusted is now a standing rule.
- Novelty: low across the week — analog series in 5 runs (CYP51, Mpro, PBP2a's DBO-adjacent
  set, neuraminidase metabolite family, BACE1 amidine family); MmpL3's adenosine-derived
  sulfonamides are the most structurally distinct output; PBP2a's non-beta-lactam leads
  (sim 0.09–0.30 to ceftaroline) are the most novel chemotypes.

## Discussion (draft)
1. **The week's real product is the failure catalogue.** Three stock runs picked unrelated
   human targets (maltase-glucoamylase twice, ABL1 kinase once) and one auto-picked PDB was
   the wrong domain of a polyprotein (NSP3 macrodomain for Mpro; protease for integrase).
   Every one was caught by accession/organism/structure-title verification and discarded
   with its evidence kept — the pipeline's honesty rules worked as designed.
2. **Rediscovery is the screen's calibration — and its limits are visible.** Where the
   reference drug was in the ChEMBL set (neuraminidase, MmpL3, CYP51), the screen found it
   at the top; where it was absent (BACE1, PBP2a), the run says so rather than faking a
   positive. A negative rediscovery bounds recall, it does not invalidate the run.
3. **Noise discipline kept every head-to-head honest.** Only CYP51 and PBP2a cleared the
   ±1 kcal/mol floor, and even those are reported as assay-gated candidates, not
   discoveries. Mpro's +0.95 sits just under the floor and is reported as such.
4. **Docking and measured potency disagree — and the disagreement is data.** PBP2a (docking
   winner has the weakest Kd) and BACE1 (strongest measured binder docks worse than the
   reference) both show Vina ranking diverging from assay history; the paper's claim must
   be that docking is a triage filter, not a potency predictor. In both cases the report
   picks the wet-lab candidate on measured potency, not on docking.
5. **Thin data is the week's second theme.** PBP2a (4 ligands) and MmpL3 (3 ligands,
   homologue only) show how little measured data exists for some high-burden targets —
   the screen can only rank what ChEMBL holds, and the report says so.
6. **Target risk outranks binding scores.** BACE1's Phase III history (verubecestat:
   EPOCH futility 2017, APECS 2018, NEJM 2018) means a better binder would still face the
   same clinical question — a point the daily report states, and the paper must keep.
7. **Limitations.** Computational only; no synthesis, no assays, no wet-lab validation in
   this draft. ChEMBL assay heterogeneity, ToxGuard read-across weakness, ±1 kcal/mol
   docking noise, single-gene runs, one invalid run (integrase) with no re-run yet.
   Weekly cadence means one target per method replicate — no cross-day replicates of the
   same target.

## What this paper is NOT (for the author)
- Not a discovery claim for any molecule.
- Not a therapeutic, efficacy, or cure claim for any disease.
- Not submission-ready: needs Zubair's authorship decisions, target-method narrative, figure set
  (workflow diagram, docking pose overlays, score distributions), and a chosen venue.
- The HIV-1 integrase run must NOT be cited as an integrase result — it is a documented
  method failure, and a correct integrase re-run is still owed.

## References (draft — to verify/finalize before any submission)
- UniProtKB records: P04585 (HIV-1 Gag-Pol), P10613 (Candida ERG11), P0DTD1 (SARS-CoV-2
  pp1ab), Q93IC2 (MRSA PBP2a, strain 27r), P9WJV5 (Mtb MmpL3), Q6DPL2 (influenza A NA),
  P56817 (BACE1).
- ChEMBL targets: CHEMBL3638360 (Gag-Pol), CHEMBL1780 (Candida CYP51), CHEMBL4523582
  (SARS-CoV-2 pp1ab), CHEMBL6187 (MecA), CHEMBL5465372 (smegmatis MmpL3), CHEMBL6135
  (influenza NA), CHEMBL4822 (BACE1).
- RCSB PDB structures: 6DV4 (protease — invalid for integrase), 5TZ1, 7VH8, 1MWS, 3ZG0,
  7NVH, 3CKZ, 7MYI.
- Reference drugs (PubChem): dolutegravir; fluconazole; nirmatrelvir CID 155903259;
  ceftaroline CID 9852981 (fosamil) / active CID 74316801; SQ109 CID 5274428; oseltamivir
  CID 65028; verubecestat CID 51352361.
- Clinical context: Egan MF et al., NEJM 2018;378:1691–703 (verubecestat EPOCH).
- Pipeline stack: RDKit (Morgan fingerprints), AutoDock Vina, meeko, ToxGuard (Tox21 kNN).
- Daily run raw data: `leadforge-daily-*.json` audit files for each day (7 runs) plus
  run and dock JSON evidence files.

## Next steps for the author (Zubair)
1. Review this skeleton; decide target venue and authorship order.
2. Re-run HIV-1 integrase correctly (integrase-specific target, not Gag-Pol polyprotein).
3. Repeat runs for any target you want as a full methods replicate.
4. University-lab wet-lab assays decide which candidates advance — paper claims stay bounded by those assays.
5. Export figures; expand methods with run logs from each day's JSON.

*Skeleton compiled 2026-11-01 from the seven daily reports by the LeadForge daily-disease cron.
Weekly raw data archived in hidden_files/.*


---

*Source: LeadForge AI weekly paper draft (`leadforge-weekly-paper-2026-11-01.md`), LeadForge drug-discovery pipeline. Weekly papers are compiled from the daily LeadForge runs.*
