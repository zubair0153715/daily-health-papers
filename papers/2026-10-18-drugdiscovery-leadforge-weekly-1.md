# Computational small-molecule triage against seven high-burden disease targets (week of 12-18 Oct 2026)

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan · **Drafting assistant:** Lapis (AI)

## Week of 2026-10-12 → 2026-10-18 (7 daily targets)

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
preparation) against the best available experimental structure. Across the week of 2026-10-12 to
2026-10-18 we screened seven targets spanning antimicrobial resistance (S. aureus DHFR, P. falciparum
DHFR-TS), oncology (CDK4, PARP1), and cardiometabolic disease (HMGCR, GLP1R, PCSK9). Each run included a
rediscovery control (verifying the pipeline recovers the reference drug or its scaffold from ChEMBL)
and a head-to-head docking comparison between ranked leads and the reference therapy. [TODO: add final
tallies once PCSK9 completes.] Honest interpretation is enforced at every step: docking margins within
±1 kcal/mol are reported as noise-equivalent, resistant-allele strain effects are flagged, and all
candidates are presented as computational starting points requiring wet-lab validation. No efficacy or
therapeutic claims are made.

**Keywords:** virtual screening; AutoDock Vina; ChEMBL; target triage; DHFR; CDK4; PARP1; HMGCR; GLP1R; PCSK9

## Introduction (draft)
Drug discovery for high-burden diseases in resource-limited settings needs a cheap, reproducible first
filter: a computational triage step that converts open chemical data into a short wet-lab shortlist.
This draft reports one week of daily automated screening from the LeadForge AI pipeline. The scope is
deliberately narrow — *computational candidate triage only* — and the methods are designed so any
other group can re-run them against the same live databases.

### Target selection rationale
Targets were chosen for disease burden and the presence of a marketed reference small molecule for
head-to-head comparison:
- **Antimicrobial:** S. aureus DHFR (dfrA, trimethoprim resistance), P. falciparum DHFR-TS (pyrimethamine resistance)
- **Oncology:** CDK4 (palbociclib), PARP1 (olaparib)
- **Cardiometabolic:** HMGCR (atorvastatin), GLP1R (orforglipron), PCSK9 (enlicitide)

## Methods (draft)
### 7.1 Daily pipeline (identical all 7 days)
1. Target identification: UniProtKB live search → human/pathogen protein, accession recorded.
2. Known-ligand retrieval: ChEMBL target (accession-mapped), top ~50 bioactivities by pChEMBL.
3. Query-drug verification: reference small-molecule drug confirmed live via PubChem PUG REST.
4. Similarity screen: RDKit Morgan fingerprints, Tanimoto vs known actives, top 25 kept.
5. ADMET screen: Lipinski / Veber rules, PAINS filters, ToxGuard Tox21 kNN read-across (12 assays).
6. Lead ranking: composite score (similarity 40 + Lipinski 20 + Veber 10 + PAINS 10 + tox 20).
7. Docking: AutoDock Vina, meeko ligand prep, best available experimental structure (X-ray preferred,
   cryo-EM where no X-ray exists), box 22.5 Å, exhaustiveness 8, 3 poses; reference drug docked
   head-to-head in the same grid.

### 7.2 Rediscovery control
Each run includes a rediscovery check: whether the pipeline recovers the reference drug's scaffold
from the ChEMBL ligand set (positive controls validate the screen; negatives bound its recall).

### 7.3 Honest-interpretation rules (applied in every run)
- Docking differences < ~1 kcal/mol = method noise, never "wins".
- Resistant-allele structures (K1 P. falciparum, Tn4003 S. aureus) are flagged; head-to-head results
  against them are interpreted accordingly.
- Measured Ki/IC50 values come from heterogeneous ChEMBL assays — directional, not rankings.
- ToxGuard outputs are kNN read-across: "no red flag found", not "proven safe".
- All leads are existing ChEMBL compounds; patent paths need university/teacher review.

## Results — weekly summary table
| Day | Target | Reference drug | Bioactivities | Top lead (computational pick) | Beat reference? |
|---|---|---|---|---|---|
| Mon 10-12 | S. aureus DHFR (P13955) | trimethoprim | 55 | CHEMBL120226 (Ki 4.0 nM) | Marginal (−8.23 vs −7.44) — noise; resistant isoform caveat |
| Tue 10-13 | P. falciparum DHFR-TS (P13922, K1) | pyrimethamine | 44 | CHEMBL21885 (Ki 0.6 nM) | +0.89 kcal/mol — noise; resistant allele caveat |
| Wed 10-14 | CDK4 (P11802) | palbociclib | 49 | CHEMBL6008170 (IC50 0.8 nM) | +0.55 kcal/mol — noise; pocket-bias caveat |
| Thu 10-15 | PARP1 (P09874) | olaparib | 51 | CHEMBL4845834 (IC50 0.19 nM) | Yes on paper: −11.87 vs −11.27 (+0.60) — *priority candidate, within noise* |
| Fri 10-16 | HMGCR (P04035) | atorvastatin | 54 | CHEMBL161829 / CHEMBL2220442 (ADMET-clean) | No docking winner (−8.98 reference); ADMET ranking win only |
| Sat 10-17 | GLP1R (P43220) | orforglipron | 58 | CHEMBL6167455 (EC50 0.016 nM) | No (−7.20 vs −7.74); beyond-rule-of-5 chemistry noted |
| Sun 10-18 | PCSK9 (Q8NBP7) | enlicitide (MK-0616) | 53 | CHEMBL5084416 (Ki 0.01136 nM) | N/A — docking infeasible, recorded honestly |

### Per-target result notes (from daily reports)
- **S. aureus DHFR (10-12):** pipeline hit the plasmid-encoded TMP-resistant dfrA isoform (P13955).
  Three low-nM organosilicon iminosugar scaffolds (CHEMBL120226 / 332802 / 120488) are genuine scaffold
  hops off the diaminopyrimidine family; docked −8.23 / −8.00 / −7.70 vs trimethoprim −7.44 (PDB 2W9S, 1.8 Å).
- **P. falciparum DHFR-TS (10-13):** K1 resistant isolate structure (PDB 1J3K, 2.1 Å). Analog-series
  output (2,4-diaminopyrimidines); best analog CHEMBL21885 (p-tert-butyl) docked −8.34 vs −7.45.
- **CDK4 (10-14):** CDK6 not modelled (scope limit). Abemaciclib-bound structure 7SJ3 (2.51 Å) used —
  pocket-bias caveat documented. CHEMBL6008170 docked −7.44 vs palbociclib −6.89.
- **PARP1 (10-15):** strongest run of the week. Rediscovery positive (CHEMBL521686 = olaparib, sim 1.00,
  IC50 0.1 nM). CHEMBL4845834 (−11.87) and CHEMBL493045 (−11.35) scored better than olaparib (−11.27)
  in the same 6NRH (1.5 Å) grid — within noise, reported as priority candidates, not winners.
- **HMGCR (10-16):** rediscovery positive (CHEMBL1487 = atorvastatin). Reference docked best (−8.98,
  2R4F, 1.7 Å). Method note: first docking pass mis-centered the grid (tetramer chain averaging);
  corrected mid-run with `_ligand_center` grouping by name+chain+seqnum. CHEMBL161829 and CHEMBL2220442
  outranked atorvastatin on composite ADMET score (cleaner, 0 Lipinski violations).
- **GLP1R (10-17):** 58 bioactivities, 26 ranked. No rediscovery (max lead similarity 0.197 —
  independent scaffolds). Reference docked −7.74 (PDB 4ZGM, 1.8 Å); best lead −7.20. Top leads are
  beyond-rule-of-5 scaffolds (MW ~595–637) — the nature of oral small-molecule GLP-1 chemistry.
- **PCSK9 (10-18):** reference enlicitide (MK-0616) chosen deliberately over the biologic PCSK9 drugs
  (evolocumab/alirocumab) and inclisiran (siRNA) — only a small-molecule reference suits the screen.
  53 bioactivities (CHEMBL2929), 26 ranked. Top lead CHEMBL5084416 (reported ChEMBL Ki 0.01136 nM —
  sub-10-picomolar) and CHEMBL5082483 (Ki 0.037 nM), both enlicitide-family macrocycles (sim 0.63 /
  0.56). **Docking failed honestly:** AutoDock Vina was SIGKILLed (OOM) on all five leads and the
  reference at exhaustiveness 8 and 4 — every ligand is a 1290–1612 Da macrocycle (91–114 heavy atoms),
  outside Vina's reliable range; a tiny-ligand control on the same receptor (7S5H, 1.27 Å) ran clean,
  isolating the failure to ligand size. No affinities produced, none reported, no head-to-head winner.
  Method lesson for the paper: Vina is unsuitable for macrocyclic ligand classes — flag as a stated
  pipeline limitation (future work: constrained docking / MD). Source: `leadforge-daily-PCSK9-2026-10-18.md`.

## Weekly tallies (final)
- 7/7 runs completed; 6/7 with docking numbers; 1 (PCSK9) docking infeasible (honest failure, documented).
- Rediscovery positives: 2 (PARP1, HMGCR) — screen calibration holds.
- Within-noise "better than reference" candidates: 3 runs (S. aureus DHFR, P. falciparum DHFR-TS, PARP1) —
  all reported as priority candidates, zero winners declared.
- Novelty: scaffold hops in 2 runs (S. aureus DHFR organosilicon, GLP1R independent scaffolds);
  analog series in 4 (Pf DHFR, CDK4, HMGCR, PCSK9); rediscovery-only in 1 top slot (none — all runs
  found novel lead slots).

## Discussion (draft)
1. **Rediscovery is the screen's calibration.** Two runs (PARP1, HMGCR) independently re-found the
   reference scaffold at Tanimoto 1.00 — evidence the similarity screen recovers genuine actives.
2. **Noise discipline kept every head-to-head honest.** No run declared a winner; the largest margin
   (PARP1's +0.60 kcal/mol for CHEMBL4845834) sits inside Vina's ±1 kcal/mol floor and is reported as a
   priority candidate, not a discovery.
3. **Structure choice shapes the answer.** The CDK4 run's abemaciclib-bound pocket (7SJ3) and the
   resistant-allele DHFR runs show how the experimental structure constrains what the screen can say —
   documented per-run, not averaged away.
4. **Novelty is uneven.** BRAF/SGLT2-style scaffold hops appeared for S. aureus DHFR (organosilicon)
   and GLP1R (independent scaffolds); CDK4 and P. falciparum outputs were analog series — weaker patent
   footing, flagged for analog design.
5. **Limitations.** Computational only; no synthesis, no assays, no wet-lab validation in this draft.
   ChEMBL assay heterogeneity, ToxGuard read-across weakness, ±1 kcal/mol docking noise, single-gene
   runs for CDK4/6 and HER2-style pairs. Weekly cadence means one target per method replicate — no
   cross-day replicates of the same target.

## What this paper is NOT (for the author)
- Not a discovery claim for any molecule.
- Not a therapeutic, efficacy, or cure claim for any disease.
- Not submission-ready: needs Zubair's authorship decisions, target-method narrative, figure set
  (workflow diagram, docking pose overlays, score distributions), and a chosen venue.

## References (draft — to verify/finalize before any submission)
- UniProtKB records: P13955, P13922, P11802, P09874, P04035, P43220, PCSK9 (Q8NBP7 — verify).
- ChEMBL targets: CHEMBL2074, CHEMBL1939, CHEMBL331, CHEMBL3105, CHEMBL402, CHEMBL1784.
- RCSB PDB structures: 2W9S, 1J3K, 7SJ3, 6NRH, 2R4F, 4ZGM.
- Reference drugs (PubChem): trimethoprim CID 5578; pyrimethamine CID 4993; palbociclib CID 5330286;
  olaparib CID 23725625; atorvastatin CID 60823; orforglipron (CID verify); enlicitide (CID verify).
- Pipeline stack: RDKit (Morgan fingerprints), AutoDock Vina, meeko, ToxGuard (Tox21 kNN).
- Daily run raw data: `leadforge-daily-*.json` audit files for each day (7 runs).

## Next steps for the author (Zubair)
1. Review this skeleton; decide target venue and authorship order.
2. Repeat runs for any target you want as a full methods replicate.
3. University-lab wet-lab assays decide which candidates advance — paper claims stay bounded by those assays.
4. Export figures; expand methods with run logs from each day's JSON.

*Skeleton compiled 2026-10-18 from the seven daily reports by the LeadForge daily-disease cron.
Weekly raw data archived in hidden_files/.*


---

*Source: LeadForge AI weekly paper draft (`leadforge-weekly-paper-2026-10-18.md`), LeadForge drug-discovery pipeline. Weekly papers are compiled from the daily LeadForge runs.*
