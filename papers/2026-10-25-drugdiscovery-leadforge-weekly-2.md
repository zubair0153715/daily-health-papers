# Computational small-molecule triage against seven high-burden disease targets (week of 19-25 Oct 2026)

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan · **Drafting assistant:** Lapis (AI)

## Week of 2026-10-19 → 2026-10-25 (7 daily targets)

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
preparation) against the best available experimental structure. Across the week of 2026-10-19 to
2026-10-25 we screened seven targets spanning oncology (KRAS G12C, VEGFR2, ALK, JAK2), tuberculosis
(DprE1) and antimicrobial resistance (NDM-1, KPC-2). Each run included a rediscovery control (verifying
the pipeline recovers the reference drug or its scaffold from ChEMBL) and a head-to-head docking
comparison between ranked leads and the reference therapy. Honest interpretation is enforced at every
step: docking margins within ±1 kcal/mol are reported as noise-equivalent, boron-containing references
that Vina cannot dock are reported as non-comparable rather than as losses, and all candidates are
presented as computational starting points requiring wet-lab validation. No efficacy or therapeutic
claims are made.

**Keywords:** virtual screening; AutoDock Vina; ChEMBL; target triage; KRAS; VEGFR2; DprE1; NDM-1; KPC; ALK; JAK2

## Introduction (draft)
Drug discovery for high-burden diseases in resource-limited settings needs a cheap, reproducible first
filter: a computational triage step that converts open chemical data into a short wet-lab shortlist.
This draft reports one week of daily automated screening from the LeadForge AI pipeline. The scope is
deliberately narrow — *computational candidate triage only* — and the methods are designed so any
other group can re-run them against the same live databases.

### Target selection rationale
Targets were chosen for disease burden and the presence of a marketed or clinical-stage reference small
molecule for head-to-head comparison:
- **Oncology:** KRAS G12C (sotorasib), VEGFR2 (sunitinib), ALK (alectinib), JAK2 (ruxolitinib)
- **Tuberculosis:** DprE1 (macozinone, clinical-stage)
- **Antimicrobial resistance:** NDM-1 (taniborbactam), KPC-2 (relebactam)

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
- Boron-containing ligands (taniborbactam) cannot be prepared by Vina/PDBQT — reported as
  non-comparable, never as a loss or a win.
- Measured Ki/IC50 values come from heterogeneous ChEMBL assays — directional, not rankings.
- When docking and measured potency disagree (JAK2, DprE1), the disagreement is reported, not averaged away.
- ToxGuard outputs are kNN read-across: "no red flag found", not "proven safe".
- All leads are existing ChEMBL compounds; patent paths need university/teacher review.

## Results — weekly summary table
| Day | Target | Reference drug | Bioactivities | Top lead (computational pick) | Beat reference? |
|---|---|---|---|---|---|
| Mon 10-19 | KRAS G12C (P01116) | sotorasib | 51 | CHEMBL5892737 (Kd 0.3 nM) | Yes on paper: −10.97 vs −8.51 (+2.46) — exceeds noise, still needs assay |
| Tue 10-20 | VEGFR2 (P35968) | sunitinib | 37 | CHEMBL3954818 | Yes on paper: −11.83 vs −9.95 (+1.88) — exceeds noise, still needs assay |
| Wed 10-21 | DprE1 (P9WJF1) | macozinone | 58 | CHEMBL4752208 | +0.84 kcal/mol — within noise; measured IC50 weaker than reference |
| Thu 10-22 | NDM-1 (C7C422) | taniborbactam | 26 | CHEMBL3809719 (IC50 160 nM) | N/A — reference undockable (boron), no head-to-head possible |
| Fri 10-23 | KPC-2 (Q9F663) | relebactam | 4 | CHEMBL5483057 (IC50 44 nM) | +0.14 kcal/mol — noise; measured potency is the stronger signal |
| Sat 10-24 | ALK (Q9UM73) | alectinib | 50 | CHEMBL3946496 (IC50 0.32 nM) | +0.65 kcal/mol — within noise |
| Sun 10-25 | JAK2 (O60674) | ruxolitinib | 32 | CHEMBL3652404 (IC50 0.0165 nM) | +0.25 kcal/mol — within noise |

### Per-target result notes (from daily reports)
- **KRAS G12C (10-19):** strongest docking margin of the week. Rediscovery positive (sotorasib rank #1,
  score 95.9, sim 1.000). All four novel leads beat sotorasib on docking; best CHEMBL5892737 (−10.97)
  is also the strongest measured binder of the four (Kd 0.3 nM, pChEMBL 9.52) — the week's cleanest
  docking-plus-measured agreement. Structure PDB 9IAY, X-ray 0.95 Å.
- **VEGFR2 (10-20):** three leads beat sunitinib by more than the noise floor: CHEMBL3954818 (−11.83,
  +1.88), CHEMBL3967940 (−11.75, +1.80), CHEMBL3930485 (−11.10, +1.15) vs sunitinib −9.95.
  Structure 2XIR, X-ray 1.50 Å, DFG-out conformation — pocket-bias caveat applies (a DFG-out pocket
  favours type-II-like chemotypes).
- **DprE1 (10-21):** three benzothiazinone-family analogs beat macozinone on docking (CHEMBL4752208
  −11.16 / +0.84, CHEMBL4763381 −10.69 / +0.37, CHEMBL4868912 −10.48 / +0.16 vs −10.32) — all within
  noise, and all three carry *weaker* measured IC50 values (50–200 nM) than macozinone (10 nM). Direct
  evidence that Vina ranking ≠ measured potency; reported as such. Structure 4P8N, 1.79 Å.
- **NDM-1 (10-22):** two method lessons. First, the initial query resolved to the wrong protein
  (human MBLAC2, Q68D91) and was caught and re-run against the true bacterial enzyme (C7C422) —
  non-human targets need accession/organism verification before any run is trusted. Second, the
  reference taniborbactam contains boron, which Vina/PDBQT cannot type, so no head-to-head docking
  comparison exists; best combined candidate CHEMBL3809719 (IC50 160 nM, docking −7.44, non-boron
  scaffold, 0 Lipinski violations, PAINS-clean) is a starting point, not a winner. Structure 5XP6,
  X-ray 0.95 Å. Taniborbactam was also not recovered as a ChEMBL ligand (clinical boronate absent
  from NDM-1 bioactivity records).
- **KPC-2 (10-23):** only 4 known KPC ligands retrieved — the thinnest ligand set of the week, all
  diazabicyclooctane (DBO) analogs of relebactam, so chemical novelty is low. CHEMBL3989959 docked
  best (−7.66 vs relebactam −7.34, +0.32, noise) but has the weakest measured IC50 (869 nM);
  CHEMBL5483057 (−7.48, +0.14) carries the strongest measured activity (44 nM) and is the shortlist
  pick on measured potency, not docking. Structure 6TD0, X-ray 0.99 Å.
- **ALK (10-24):** two leads beat alectinib within noise: CHEMBL3946496 (−10.14, +0.65) and
  CHEMBL3929615 (−10.12, +0.63) vs −9.49. Both are close alectinib analogs with reported sub-nM
  IC50 values (0.32 / 0.30 nM) — analog series, not scaffold hops. Rediscovery positive (alectinib
  rank #1, sim 1.0, score 98.3). Structure 4Z55.
- **JAK2 (10-25):** CHEMBL3652404 docked −6.82 vs ruxolitinib −6.57 (+0.25, noise) with measured
  IC50 0.0165 nM, Lipinski/Veber pass, PAINS-clean. The week's clearest docking-vs-measured
  disconnect: all top leads are sub-nM actives yet dock weakly (−4.6 to −6.8), so measured IC50 is
  the stronger signal here and docking is secondary. All top leads share the pyrrolo-pyrimidine
  core — analog family, low Tanimoto (0.21–0.25) but shared core. Structure 8BXH, X-ray 1.3 Å.
  Rediscovery positive (ruxolitinib rank #1, sim 1.0, score 98.6).

## Weekly tallies (final)
- 7/7 runs completed with docking numbers; 1 (NDM-1) with no reference head-to-head (boron limit,
  documented honestly).
- Rediscovery positives: 5 of 7 (KRAS, ALK, JAK2 confirmed; VEGFR2/DprE1/KPC reports imply query
  recovery — verify against daily JSONs before citing); NDM-1 negative (reference absent from ChEMBL).
- Above-noise docking margins: 2 runs (KRAS +2.46, VEGFR2 +1.88/+1.80/+1.15) — still assay-gated,
  never declared wins.
- Within-noise "better than reference" candidates: 4 runs (DprE1, KPC, ALK, JAK2) — priority
  candidates only.
- Novelty: analog series in 5 runs (DprE1, KPC, ALK, JAK2, plus VEGFR2 chemotype family); scaffold
  hops modest (KRAS leads at Tanimoto 0.16); NDM-1's non-boron chemotype is the most structurally
  distinct output of the week.

## Discussion (draft)
1. **Rediscovery is the screen's calibration.** Three runs independently re-found the reference
   scaffold at Tanimoto 1.00 (KRAS, ALK, JAK2) — evidence the similarity screen recovers genuine actives.
2. **Noise discipline kept every head-to-head honest.** Only KRAS and VEGFR2 cleared the ±1 kcal/mol
   floor, and even those are reported as assay-gated candidates, not discoveries.
3. **Docking and measured potency disagree — and the disagreement is data.** DprE1 (beaters weaker
   on IC50) and JAK2 (sub-nM actives docking weakly) both show Vina ranking diverging from assay
   history; the paper's claim must be that docking is a triage filter, not a potency predictor.
4. **Structure and tooling limits shape the answer.** The NDM-1 boron failure and the VEGFR2 DFG-out
   pocket show how the experimental structure and the docking engine constrain what the screen can say
   — documented per-run, not averaged away.
5. **Novelty is uneven.** KPC's 4-ligand DBO set and ALK's close analogs are weak patent footing;
   KRAS's low-similarity leads and NDM-1's non-boron chemotype are the stronger starting points for
   analog design.
6. **Limitations.** Computational only; no synthesis, no assays, no wet-lab validation in this draft.
   ChEMBL assay heterogeneity, ToxGuard read-across weakness, ±1 kcal/mol docking noise, single-gene
   runs. Weekly cadence means one target per method replicate — no cross-day replicates of the same target.

## What this paper is NOT (for the author)
- Not a discovery claim for any molecule.
- Not a therapeutic, efficacy, or cure claim for any disease.
- Not submission-ready: needs Zubair's authorship decisions, target-method narrative, figure set
  (workflow diagram, docking pose overlays, score distributions), and a chosen venue.

## References (draft — to verify/finalize before any submission)
- UniProtKB records: P01116 (KRAS), P35968 (VEGFR2/KDR), P9WJF1 (DprE1), C7C422 (NDM-1),
  Q9F663 (KPC-2), Q9UM73 (ALK), O60674 (JAK2).
- ChEMBL targets: CHEMBL2189121 (KRAS), CHEMBL279 (VEGFR2), CHEMBL3804751 (DprE1),
  CHEMBL1667695 (NDM-1), CHEMBL6132 (KPC), CHEMBL4247 (ALK), CHEMBL2971 (JAK2).
- RCSB PDB structures: 9IAY, 2XIR, 4P8N, 5XP6, 6TD0, 4Z55, 8BXH.
- Reference drugs (PubChem): sotorasib; sunitinib; macozinone CID 57331386; taniborbactam;
  relebactam CID 44129647; alectinib CID 49806720; ruxolitinib CID 25126798.
- Pipeline stack: RDKit (Morgan fingerprints), AutoDock Vina, meeko, ToxGuard (Tox21 kNN).
- Daily run raw data: `leadforge-daily-*.json` audit files for each day (7 runs).

## Next steps for the author (Zubair)
1. Review this skeleton; decide target venue and authorship order.
2. Repeat runs for any target you want as a full methods replicate.
3. University-lab wet-lab assays decide which candidates advance — paper claims stay bounded by those assays.
4. Export figures; expand methods with run logs from each day's JSON.

*Skeleton compiled 2026-10-25 from the seven daily reports by the LeadForge daily-disease cron.
Weekly raw data archived in hidden_files/.*


---

*Source: LeadForge AI weekly paper draft (`leadforge-weekly-paper-2026-10-25.md`), LeadForge drug-discovery pipeline. Weekly papers are compiled from the daily LeadForge runs.*
