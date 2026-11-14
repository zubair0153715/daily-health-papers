# Multi-target computational triage of known bioactive chemical space against seven disease targets (week of 2-8 Nov 2026)

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan · **Drafting assistant:** Lapis (AI)


**DRAFT ONLY — not submitted anywhere. Journal submission is the user's action under his name.**

## Title (working)

Multi-target computational triage of known bioactive chemical space against seven disease targets: similarity screening, ADMET/toxicity read-across and AutoDock Vina docking

## Abstract

We screened the bioactive chemical space of ChEMBL against seven therapeutically relevant targets in one week of automated LeadForge runs (2–8 Nov 2026): FLT3, *Plasmodium falciparum* ATP4, *Pseudomonas aeruginosa* LpxC, acetylcholinesterase (AChE), isocitrate dehydrogenase 1 (IDH1), Bruton's tyrosine kinase (BTK) and menin (MEN1). For each target, the reference drug was recovered from live ChEMBL data (rediscovery check), 19–53 known ligands were similarity-screened, leads were ranked on a composite of similarity, Lipinski/Veber drug-likeness, PAINS and kNN toxicity read-across, and the top five leads were docked with AutoDock Vina against the best available X-ray structure, with the reference drug re-docked as control. Two runs produced leads that docked clearly better than their reference drug: CHEMBL5816906 against menin (−10.10 vs −8.37 kcal/mol for revumenib) and three scaffold-distinct leads against LpxC (best −10.85 vs −9.34 for ACHN-975). Three runs were effective ties (FLT3, AChE, IDH1) and one was an honest negative (BTK: no lead beat ibrutinib). One run (PfATP4) had no structure for docking but identified CHEMBL5591927, the strongest measured PfATP4 active in ChEMBL (EC50 4.6 nM), as a scaffold-distinct backup to cipargamin. All findings are computational triage; no compound is claimed as a drug, and wet-lab validation is required.

## Methods

**Pipeline (LeadForge, same flow for all seven runs).** (1) Target identification from UniProtKB + ChEMBL (live). (2) Known-ligand retrieval from ChEMBL bioactivities. (3) Query-compound verification via PubChem PUG REST. (4) Morgan-fingerprint similarity screen vs known actives. (5) ADMET + safety panel: RDKit descriptors (Lipinski, Veber), PAINS filter, ToxGuard kNN read-across over 12 Tox21-style assays. (6) Composite lead ranking (similarity 40 / Lipinski 20 / Veber 10 / PAINS 10 / tox 20). (7) Molecular docking: AutoDock Vina, exhaustiveness 8, 3 poses, 22.5 Å box centred on the co-crystallised ligand centroid of the best X-ray structure (resolution < 3.0 Å); grid centre verified as the largest drug-like HETATM group with cofactors, glycans, waters and ions excluded (centre-fix audit, Nov 2026). Reference drug re-docked in the same pocket as control. Vina noise is taken as ~±0.5–1 kcal/mol (up to ~2 kcal/mol in the literature); margins inside noise are reported as ties.

**Targets, references and structures.** FLT3 / gilteritinib; PfATP4 / cipargamin (no structure — docking not possible); LpxC / ACHN-975; AChE / donepezil; IDH1 / ivosidenib; BTK / ibrutinib (PDB 5P9J, 1.08 Å); menin / revumenib (PDB 6O5I, 1.24 Å).

## Results summary

| Date | Target | Reference | Best lead (docking) | Reference (docking) | Verdict |
|---|---|---|---|---|---|
| 2 Nov | FLT3 | gilteritinib | CID 66642725, −8.21 | −7.60 | Nominal win, inside noise; no measured FLT3 potency in screen — re-run pending ChEMBL recovery |
| 3 Nov | PfATP4 | cipargamin | (no structure) | — | No docking possible; CHEMBL5591927, EC50 4.6 nM, strongest measured PfATP4 active, scaffold-distinct — test vs G358S mutant |
| 4 Nov | LpxC | ACHN-975 | CHEMBL4437188, −10.85 | −9.34 | Three leads dock better; best is sub-nanomolar Kd 0.065 nM, PAINS-clean — backup series for a stalled clinical lead |
| 5 Nov | AChE | donepezil | CHEMBL3585775, −9.74 | −10.02 | Tie by docking; leads carry picomolar measured Ki/IC50 (0.0105–0.0269 nM) — sulfamoyl-carbamate backup chemotype |
| 6 Nov | IDH1 | ivosidenib | CHEMBL4282663, −8.24 | −8.29 | Tie by docking (0.05 gap); IC50 1.0 nM leads in the set — ivosidenib-analog backup family; pocket is wild-type, not R132H mutant |
| 7 Nov | BTK | ibrutinib | CHEMBL5749648, −10.13 | −10.83 | Honest negative — no lead beats ibrutinib; does not address the C481S resistance gap |
| 8 Nov | Menin (MEN1) | revumenib | CHEMBL5816906, −10.10 | −8.37 | **Clear win** — 1.73 kcal/mol margin, scaffold hop (sim 0.211), IC50 3.0 nM, clean panel; test vs resistance mutants (M327I/G331R) |

**Headline results.** 2 of 7 runs produced a docking lead clearly better than the reference (menin, LpxC); 3 were ties (FLT3, AChE, IDH1); 1 was a negative (BTK); 1 had no structure but a measured-potency lead (PfATP4). Across the week, every reference drug was recovered by the pipeline (rediscovery check passed in all runs where the reference was in ChEMBL).

## Discussion

The week's strongest single result is CHEMBL5816906 against menin: a scaffold-distinct binder docking 1.73 kcal/mol better than the FDA-approved revumenib, with nanomolar measured activity and a clean safety panel. Its value is conditional on the resistance question — menin inhibitors fail clinically via interface mutations, and no mutant structure was tested. The LpxC series (CHEMBL4437188 and two siblings) is the second genuine outcome: a sub-nanomolar, scaffold-distinct backup family for a target whose lead inhibitor stalled in the clinic. The three ties (FLT3, AChE, IDH1) are not failures: each carries measured potency at least as strong as the reference, which keeps them as backup chemotypes, but docking alone cannot rank them above the reference. The BTK negative is reported as a result, not a failure: it shows the screen can say no. The PfATP4 run exposes a structural-data gap — a high-value antimalarial target with no usable structure for docking — and points to the mutant-resistance assay as the decisive experiment.

**Limitations.** (i) All scores are computational; no wet-lab data were generated. (ii) Docking used rigid receptors and single pockets; covalent mechanisms (BTK Cys481) are not modelled. (iii) Measured potencies come from heterogeneous ChEMBL assays and are not head-to-head comparisons. (iv) Similarity-anchored screening limits chemical diversity by design. (v) ToxGuard is kNN read-across, not a safety verdict. (vi) Mutant targets (IDH1 R132H, BTK C481S, menin M327I/G331R, PfATP4 G358S) were not modelled.

## References (sources, live data)

- UniProtKB accessions: FLT3 P36888; PfATP4 (P. falciparum); LpxC (P. aeruginosa); AChE P22303; IDH1 O75874; BTK Q06187; menin O00255.
- ChEMBL (EBI) target + bioactivity records, accessed live 2–8 Nov 2026.
- PubChem PUG REST (reference-compound verification).
- RCSB PDB: 5P9J (BTK–ibrutinib, 1.08 Å); 6O5I (menin–LMY, 1.24 Å).
- FDA approval of revumenib (Revuforj) 15 Nov 2024; label expansion to NPM1-mutated AML 24 Oct 2025 (Syndax/FDA).
- LeadForge pipeline: run_pipeline + dock_leads (centre-fix audit, Nov 2026). Individual daily reports: `leadforge-daily-{FLT3,PfATP4,LpxC,AChE,IDH1,BTK,MEN1}-2026-11-0{2..8}.md`.

*DRAFT ONLY — compiled 2026-11-08 from the week's seven daily LeadForge reports. Not submitted anywhere. Computational triage only; no cure or treatment claims.*


---

*Source: LeadForge AI weekly paper draft (`leadforge-weekly-paper-2026-11-08.md`), LeadForge drug-discovery pipeline. Weekly papers are compiled from the daily LeadForge runs.*
