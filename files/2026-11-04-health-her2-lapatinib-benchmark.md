# Five Known HER2 Inhibitors Dock Within Noise of Lapatinib on the HER2 Kinase Domain: A Standardised Vina Benchmark and a Caution on Automated Structure Selection

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-04 · **Health Papers Agent — Paper #5** (daily 5-paper run)

**Keywords:** HER2; lapatinib; molecular docking; AutoDock Vina; breast cancer; drug resistance; ChEMBL; structure selection

---

## Abstract

HER2-positive breast cancer accounts for 15–20% of breast cancers, and acquired resistance to the dual EGFR/HER2 inhibitor lapatinib is a major cause of treatment failure, with more than 70% of patients becoming refractory and relapsing within five years. We asked whether a standardised, fully automated docking pipeline could rank five known potent HER2 inhibitors against lapatinib on the HER2 kinase domain, and whether the pipeline's automated structure choice could be trusted. Compounds were drawn from ChEMBL bioactivities against human HER2 (CHEMBL1824), screened with RDKit (Lipinski/Veber/PAINS) and a Tox21 kNN read-across panel, and docked with AutoDock Vina 1.2.7 into the HER2 kinase domain (PDB 3PP0, 2.25 Å) at the co-crystallised TAK-285 centroid, under an identical protocol for all six ligands. The pipeline's first automated structure pick was wrong — it selected PDB 8JYR, the HER2 extracellular domain I in an antibody complex, which is not the kinase pocket — and its first target query resolved to EGFR rather than HER2; both errors were caught by manual verification and corrected before any number was reported. On the correct structure, lapatinib scored −10.86 kcal/mol and the five known inhibitors scored −10.29 to −11.71 kcal/mol; the best pose of CHEMBL4105329 beat lapatinib by 0.85 kcal/mol, a margin inside Vina's ±1–2 kcal/mol scoring noise, and its second pose fell to −9.66 kcal/mol, below lapatinib. All five leads are already published sub-nanomolar HER2 inhibitors (ChEMBL IC50 0.7–1.0 nM), so this is a benchmark, not a discovery: Vina on 3PP0 reproduces the known-active band but cannot resolve potency differences among known actives. The falsifiable next step is a HER2 kinase inhibition assay (IC50) of CHEMBL4105329 against lapatinib under identical conditions, with a pre-registered decision rule that a margin under 2 kcal/mol in docking predicts no measurable IC50 advantage.

---

## 1. Introduction

Breast cancer is the most commonly diagnosed cancer in women worldwide: the International Agency for Research on Cancer recorded approximately 2.3 million new cases and 667,000 deaths in 2022, and World Health Organization estimates for 2024 put the figures at 2.4 million diagnoses and 694,000 deaths. HER2-positive disease — amplification or overexpression of the receptor tyrosine-protein kinase erbB-2 — accounts for 15–20% of cases and is among the most aggressive subtypes, with historically poor prognosis. In Pakistan the burden is acute: the country has the highest breast-cancer incidence in Asia, with roughly 44,000 new cases a year (Shaukat Khanum Memorial Cancer Hospital, citing WHO estimates, 2026), about one in nine women at lifetime risk, and more than 100 deaths a day.

Lapatinib, a reversible dual EGFR/HER2 tyrosine kinase inhibitor approved by the US FDA in 2007, binds the intracellular ATP pocket of the HER2 kinase domain and blocks PI3K/Akt and MAPK signalling. Its measured potency is high — apparent Ki 3 nM against EGFR and 13 nM against HER2, with HER2 kinase IC50 values of 9.2–9.8 nM in cell-free assays — and its slow off-rate gives prolonged pathway inhibition. But resistance is the rule, not the exception: primary or acquired resistance arises through HER2 signalling aberrations (receptor mutation, p95HER2 truncation, PIK3CA mutation, PTEN loss), bypass pathways, and tumour-microenvironment remodelling, and an integrative proteo-genomic study of lapatinib-resistant HER2-positive cells reported that over 70% of patients become refractory and relapse within five years, identifying a nine-marker resistance signature (SCIN, EGFR, HPGD, TPM1, CALD1, PCP4, AKR7A3, KRT81, FASN). Newer HER2-selective inhibitors such as tucatinib — HER2 IC50 6.9 nM versus lapatinib's 109 nM in one head-to-head assay, and the backbone of the HER2CLIMB trial, which cut progression events by 46% (hazard ratio 0.54) — show the class can still be improved, particularly for brain metastases.

The question this paper asks is narrower and methodological: can a standardised, automated docking pipeline reproduce the known potency band of HER2 inhibitors against lapatinib, and can its automated choices be trusted without manual verification? The falsifiable hypothesis is that five ChEMBL-reported sub-nanomolar HER2 inhibitors, docked under an identical protocol, will score within Vina's noise of lapatinib on the HER2 kinase domain — and that any apparent "win" smaller than 2 kcal/mol is not a discovery.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 4 November 2026: the daily literature digest (2026-11-04), PubMed E-utilities (verified PMIDs below), and ChEMBL (EBI). Key sources: the 2026 review of anti-HER2 resistance mechanisms (IARC 2022 burden figures; 15–20% HER2-positive share); Wood et al. for the lapatinib–kinase crystal structure and binding kinetics; Steggall et al. for the lapatinib-resistance signature and the >70% refractory figure; Murthy et al. (HER2CLIMB) for tucatinib as the current benchmark; Ishikawa et al. for TAK-285, the co-crystallised ligand of the structure used here.

### 2.2 Compound selection (LeadForge pipeline)

The LeadForge pipeline was run live on 4 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target identification used the gene query "ERBB2" (UniProt P04626, receptor tyrosine-protein kinase erbB-2, human, 1,255 aa); the ChEMBL target was CHEMBL1824 (single-protein, human). Thirty-eight bioactivities (pChEMBL ≥ 5) were retrieved; lapatinib was verified in PubChem (CID 208908; SMILES CS(=O)(=O)CCNCC1=CC=C(O1)C2=CC3=C(C=C2)N=CN=C3NC4=CC(=C(C=C4)OCC5=CC(=CC=C5)F)Cl). Twenty-five compounds passed the Morgan-fingerprint similarity screen and 26 were ranked by composite score (similarity ×40 + Lipinski ×20 + Veber ×10 + PAINS ×10 + tox ×20). The top five ranked leads were taken forward to docking. All five are known HER2 inhibitors with published ChEMBL IC50 values of 0.7–1.0 nM against HER2 (pChEMBL 9.00–9.15); none has a preferred name, an approval, or a development phase in ChEMBL.

### 2.3 Molecular docking

Docking was performed 4 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was the HER2 kinase domain, PDB 3PP0 (2.25 Å, "Crystal Structure of the Kinase domain of Human HER2 (erbB2)"), with the grid centred on the centroid of its co-crystallised ligand 03Q (TAK-285): [17.10, 16.55, 26.60]. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

Two automated-pipeline errors were caught and corrected before reporting, and are documented here because they are part of the result. First, the initial target query "Human epidermal growth factor receptor 2 (HER2)" resolved in UniProtKB to EGFR (P00533), not HER2; the resulting run docked against the EGFR kinase domain (PDB 8A27) and its numbers are not reported as HER2 results. Second, even with the correct accession (P04626), the pipeline's automatic PDB picker chose PDB 8JYR (1.69 Å) — the highest-resolution HER2 structure, but an anti-HER2 antibody complex of the extracellular domain I, not a kinase-domain structure with a small-molecule pocket. Docking a kinase inhibitor into that pocket would have been biologically meaningless. The correct structure, 3PP0, was selected manually, and all six ligands were re-docked into it with the same protocol. The raw JSON of every run is preserved (see Data availability), including the two discarded runs, so the correction is auditable.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all five leads and lapatinib were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probabilities were SR-MMP 1.0 for CHEMBL203599 and SR-ARE 0.687 for CHEMBL203661; the remaining leads peaked at 0.30–0.54. These are similarity-based predictions, not measurements — and lapatinib itself carries a measured SR-ARE flag of 1.0 in the same panel, so a flag in this panel does not distinguish a lead from the approved reference drug.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; a single crystal structure (3PP0, one conformation) was used; the five "leads" are already-known HER2 inhibitors, so no novelty of chemistry is claimed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | HER2 IC50, ChEMBL (nM) | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL4105329 | 1.0 | **−11.71** | −11.71, −9.66, −8.77 | clean |
| Lapatinib (reference) | 9.2–9.8 | −10.86 | −10.86, −10.07, −9.51 | clean |
| CHEMBL203599 | 0.7 | −10.59 | −10.59, −10.45, −10.19 | clean |
| CHEMBL203661 | 0.8 | −10.40 | −10.40, −10.12, −10.04 | clean |
| CHEMBL258282 | 1.0 | −10.29 | −10.29, −9.56, −9.03 | clean |
| CHEMBL483332 | 1.0 | −10.29 | −10.29, −8.73, −8.40 | clean |

All docking on PDB 3PP0 (HER2 kinase domain, 2.25 Å), grid centre [17.10, 16.55, 26.60], box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 4 November 2026. Lapatinib's own drug-likeness is poor by the pipeline's rules (MW 581.07, logP 6.14, 2 Lipinski violations, Veber fail) — it passes no Lipinski/Veber gate, yet is the approved drug; the five leads all pass Lipinski, with MW 454.89–494.99 and logP 3.14–6.10.

The headline number is a non-result, stated plainly: the best pose of CHEMBL4105329 beats lapatinib by 0.85 kcal/mol, inside Vina's noise, and its pose consistency is the worst in the set — the second pose drops 2.05 kcal/mol to −9.66, below lapatinib's best pose. The other four leads sit 0.27–0.57 kcal/mol above lapatinib's best pose, i.e. statistically tied. Two of them (CHEMBL203599, CHEMBL203661) carry acrylamide warheads, the covalent motif of neratinib-class inhibitors; Vina does not model covalent bond formation, so their scores understate any covalent contribution and cannot be compared directly with reversible binders on affinity alone.

### 3.2 Comparison with published docking

Published docking on the same structure exists: a lapatinib-congener study docked novel HER2 inhibitors into 3PP0 (GOLD software) and reported HER2 IC50 values of 5.4–12 nM for its derivatives versus 95.5 nM for lapatinib in the same assay, with compound 17d forming two hydrogen bonds (Met801, Ser728). Our Vina numbers are not directly comparable to GOLD scores, and no published Vina score for lapatinib on 3PP0 was found to benchmark against — which is itself a gap this paper fills: a Vina 1.2.7 reference value for lapatinib on 3PP0 (−10.86 kcal/mol, poses −10.86/−10.07/−9.51) is now on record for others to reproduce.

### 3.3 The standardisation problem

Two of the three automated steps that could silently corrupt this result did corrupt it, and both were caught only because a human checked the target accession and the PDB title before writing. The UniProtKB free-text search for "Human epidermal growth factor receptor 2 (HER2)" returns EGFR first; the PDB picker ranks by resolution and ligand presence, which selects an antibody complex of the extracellular domain over the kinase domain. Any pipeline that trusts either default without verification will publish EGFR numbers, or extracellular-domain numbers, labelled as HER2. The fix is cheap — verify accession, verify PDB title and domain, verify the co-crystallised ligand is a kinase inhibitor — but it is not optional.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a benchmark: five known sub-nanomolar HER2 inhibitors and lapatinib all land in a −10.3 to −11.7 kcal/mol band on 3PP0, and Vina cannot separate them. That is consistent with their measured potencies (all within one log unit of each other) and is, in itself, a useful validation — the protocol reproduces the known-active band. What it does not do is identify a better drug. CHEMBL4105329 is not a lead; it is a known 1.0 nM HER2 inhibitor whose top pose is an outlier.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 0.85 kcal/mol margin is inside Vina's ±1–2 kcal/mol noise. Second, pose inconsistency: a genuine binder should hold its score across poses; CHEMBL4105329 loses 2.05 kcal/mol between pose 1 and pose 2, while lapatinib and CHEMBL203599/203661 hold within ~0.8 kcal/mol across all three poses. Third, all five compounds are already known HER2 actives — there is no new chemistry here, only a new comparison.

### 4.3 The PAINS/tox picture is clean but thin

No PAINS alerts is good, but PAINS-clean is a low bar for kinase inhibitors, and the Tox21 read-across flags (SR-MMP 1.0 for CHEMBL203599) are predictions from neighbours, not data. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either — least of all because the reference drug flags the same assays.

### 4.4 Testable hypotheses

1. CHEMBL4105329 inhibits recombinant HER2 kinase with an IC50 within 2-fold of lapatinib's under identical assay conditions (the docking predicts no measurable advantage; a >5-fold advantage would refute the noise interpretation).
2. CHEMBL203599 and CHEMBL203661, as acrylamide-bearing analogues, show time-dependent (covalent) HER2 inhibition in a pre-incubation assay, which reversible docking cannot predict.
3. A Vina re-dock of the co-crystallised ligand TAK-285 into 3PP0 reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant HER2 kinase inhibition assay (ADP-Glo or equivalent) for CHEMBL4105329, CHEMBL203599 and lapatinib, same plate, n = 3, with a pre-registered 2-fold decision rule. Stage 2 (weeks 3–6): time-dependence test for the two acrylamide compounds (IC50 with and without 60-minute pre-incubation). Stage 3 (weeks 7–12): HER2-positive cell-line viability (BT-474, SK-BR-3) for any compound that clears Stage 1, with lapatinib as control and a HER2-negative line (MDA-MB-231) as selectivity check. Total compound cost is the binding constraint; all five leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. The best-pose margin (0.85 kcal/mol) is inside Vina's ±1–2 kcal/mol noise. 3. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of TAK-285 was performed. 4. A single crystal structure (3PP0, one HER2 conformation) was used; lapatinib binds an inactive-like conformation and induced-fit effects are not modelled. 5. Vina does not model covalent binding, so the two acrylamide compounds are under-scored relative to their likely mechanism. 6. All five leads are already-known HER2 inhibitors; no new chemical matter is proposed. 7. No Pakistani-market or clinical data are presented; the Pakistan burden figures are contextual, not part of the result. 8. The pipeline's automated target and structure selection failed twice and required manual correction — other silent defaults in the same pipeline are not yet audited.

## 6. Conclusion

Five known HER2 inhibitors dock within noise of lapatinib on the HER2 kinase domain (PDB 3PP0): the largest apparent margin, 0.85 kcal/mol for CHEMBL4105329, is inside Vina's scoring noise and rests on a single inconsistent pose. The durable finding is methodological — a standardised Vina protocol reproduces the known-active band for HER2, but automated target resolution and PDB selection fail silently and must be verified by hand. The next experiment is a head-to-head HER2 kinase IC50 assay, not more docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Research advances in drug resistance mechanisms to anti-HER2 therapy in HER2-positive breast cancer. *Oncol Res.* 2026. doi:10.32604/or.2026.085387.
2. Wood ER, Truesdale AT, McDonald OB, Yuan D, et al. A unique structure for epidermal growth factor receptor bound to GW572016 (lapatinib): relationships among protein conformation, inhibitor off-rate, and receptor activity in tumor cells. *Cancer Res.* 2004;64(18):6652–6659. PMID: 15374980.
3. Steggall J, Rajeeve V, Al-Subaie N, et al. Integrative proteo-genomic profiling uncovers key biomarkers of lapatinib resistance in HER2-positive breast cancer. *Br J Cancer.* 2025;133:1471–1482. PMID: 40946111.
4. Murthy RK, Loi S, Okines A, et al. Tucatinib, trastuzumab, and capecitabine for HER2-positive metastatic breast cancer. *N Engl J Med.* 2020;382:597–609. doi:10.1056/NEJMoa1914609.
5. Ishikawa T, Seto M, Banno H, et al. Design and synthesis of novel human epidermal growth factor receptor 2 (HER2)/epidermal growth factor receptor (EGFR) dual inhibitors. *J Med Chem.* 2011;54(23):8030–8050. PMID: 22003817.
6. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
7. Shaukat Khanum Memorial Cancer Hospital & Research Centre, citing WHO estimates. Nearly 44,000 new breast cancer cases occur annually in Pakistan. Reported 1 October 2026. https://pakobserver.net/breast-cancer-awareness-must-lead-to-action/ (accessed 4 November 2026).
8. RCSB Protein Data Bank. Crystal structure of the kinase domain of human HER2 (erbB2). PDB ID 3PP0, 2.25 Å. https://www.rcsb.org/structure/3PP0 (accessed 4 November 2026).
9. ChEMBL database, European Bioinformatics Institute. Target: receptor tyrosine-protein kinase erbB-2 (CHEMBL1824); bioactivities accessed 4 November 2026. https://www.ebi.ac.uk/chembl/.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-028b-2026-11-04.json` (pipeline run: UniProt P04626, ChEMBL CHEMBL1824, 26 ranked leads; auto-picked PDB 8JYR results retained for audit) and `hidden_files/dock-HP-028c-2026-11-04.json` (authoritative re-dock: PDB 3PP0, 2.25 Å, TAK-285 centroid [17.10, 16.55, 26.60], Vina 1.2.7). The discarded EGFR run is in `hidden_files/dock-HP-028-2026-11-04.json`. ChEMBL IDs: lapatinib (query), CHEMBL4105329, CHEMBL203599, CHEMBL203661, CHEMBL258282, CHEMBL483332. PDB ID 3PP0. No additional data were generated.
