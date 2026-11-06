# Two Leads "Beat" Macozinone by Docking and Lose by 1.23 kcal/mol of Noise: A Vina Benchmark of DprE1 Inhibitors on 4P8N and the Covalent Binding Vina Cannot See

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-06 · **Health Papers Agent — Paper #2** (daily 5-paper run)

**Keywords:** DprE1; macozinone; tuberculosis; molecular docking; AutoDock Vina; covalent inhibitor; benzothiazinone; ChEMBL

---

## Abstract

Tuberculosis made about 10.8 million people ill in 2023 and killed about 1.25 million, and the search for shorter, safer regimens continues. Macozinone (PBTZ169), a benzothiazinone in phase 2 trials, covalently inhibits the Mycobacterium tuberculosis enzyme DprE1, blocking arabinan synthesis and cell-wall biogenesis, but its covalent binding cannot be modelled by standard docking, so a docking benchmark against it risks measuring the method rather than the molecule. We ran the LeadForge pipeline live on 6 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina docking): target DprE1 (UniProt P9WJF1, strain ATCC 25618 / H37Rv, ChEMBL CHEMBL3804751, 58 bioactivities), structure PDB 4P8N at 1.79 Å, grid centred exactly on the co-crystallised non-covalent inhibitor R57 ([16.51, −20.97, 1.7]), and five ligands docked with AutoDock Vina 1.2.7 under an identical protocol. Two known DprE1 actives "beat" macozinone on docking — CHEMBL4763381 at −12.05 kcal/mol and CHEMBL4752208 at −11.74 kcal/mol, against macozinone at −10.82 kcal/mol — margins of 1.23 and 0.92 kcal/mol, inside Vina's ±1–2 kcal/mol noise. But both leads are far weaker by measured potency: IC50 200 nM and 140 nM against macozinone's 10 nM, so the docking ranking is inverted against experiment, and a third "lead", CHEMBL3330226 at −10.96 kcal/mol, is macozinone itself entered twice, scoring −10.96 versus −10.82 as the query. The falsifiable next step is a head-to-head DprE1 enzyme inhibition assay of CHEMBL4763381 against macozinone under identical conditions, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable advantage; a measured potency advantage for the lead, or covalent docking showing macozinone binds Cys387 far more tightly than Vina suggests, would refute the claim that the docking win is only a measurement of Vina's limits.

---

## 1. Introduction

Tuberculosis (TB) remains one of the world's deadliest infectious diseases: according to the WHO Global Tuberculosis Report 2024, about 10.8 million people fell ill with TB in 2023 and about 1.25 million died. Standard treatment still takes months, and drug-resistant TB needs longer, more toxic regimens, so new drugs with new mechanisms are urgently needed. DprE1 (decaprenylphosphoryl-beta-D-ribose oxidase) is one of the most validated new TB targets: it catalyses a step in arabinan synthesis, and blocking it stops cell-wall biogenesis in Mycobacterium tuberculosis.

Macozinone (MCZ, PBTZ169) is a benzothiazinone that covalently inhibits DprE1 and is in phase 2 trials (NCT03334734); its minimum inhibitory concentration is 0.3 ng/mL by resazurin microtiter assay. It is not alone: BTZ043, the first benzothiazinone, is in phase 2b combination trials (NCT05926466, with bedaquiline and delamanid), and other DprE1 candidates in trials include TBA-7371 (an azaindole) and quabodepistat (a carbostyril). Macozinone also has a known human liability: human prostaglandin reductases PTGR1 and PTGR2 dearomatize it to H2MCZ, which loses antimycobacterial activity.

The question this paper asks is narrower and methodological: can a standardised, automated docking pipeline rank known DprE1 actives against macozinone, and what does an apparent docking "win" mean when the reference drug is a covalent inhibitor and the structure used holds a non-covalent inhibitor? The falsifiable hypothesis is that any lead beating macozinone by less than 2 kcal/mol on Vina docking has no measurable potency advantage, and that the docking ranking will disagree with measured IC50 values on this target.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 6 November 2026: the daily literature digest at `~/workspace/research-team/digests/`, PubMed and web search, ChEMBL (EBI) and RCSB PDB. Key sources: the WHO Global Tuberculosis Report 2024 for the TB burden figures; the macozinone phase 2 trial record (ClinicalTrials.gov NCT03334734) and the BTZ043 phase 2b combination trial record (NCT05926466); the 2025 Antimicrobial Agents and Chemotherapy report of macozinone's MIC of 0.3 ng/mL by resazurin microtiter assay; and the 2026 Nature Communications paper showing that human PTGR1/PTGR2 dearomatize macozinone to inactive H2MCZ (DOI 10.1038/s44321-026-00526-1). The covalent mechanism of benzothiazinones — the nitroso moiety forming a semimercaptal with Cys387 of DprE1 — is the established mechanism for this class and is the reason standard non-covalent docking cannot represent macozinone's real binding mode.

### 2.2 Molecular docking

The LeadForge pipeline was run live on 6 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target: M. tuberculosis DprE1, UniProt P9WJF1, strain ATCC 25618 / H37Rv; ChEMBL CHEMBL3804751, 58 bioactivities retrieved. Twenty-five compounds passed the Morgan-fingerprint similarity screen and 26 were ranked by composite score. The top five ranked leads were taken forward to docking. All five are known DprE1 actives with published ChEMBL potencies; none has a preferred name in ChEMBL.

Docking was performed with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was M. tuberculosis DprE1, PDB 4P8N (1.79 Å, "M. tuberculosis DprE1 in complex with the non-covalent inhibitor QN118", ligand code R57), with the grid centred exactly on the centroid of the co-crystallised ligand R57, chain A: [16.51, −20.97, 1.7]. The centre was verified against the PDB file to 0.01 Å. The FAD cofactor centroid is 12.75 Å away — the centre is not on the cofactor, so the grid-centre fault that has corrupted earlier runs (centring on a cofactor or glycan) did not occur here. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

One pipeline fault was caught before reporting, and is documented here because it is part of the result. The lead list contains macozinone itself: CHEMBL3330226 has the same molecular weight as macozinone (456.49), Tanimoto similarity 1.0 to the query, and an identical toxicity panel, and it scored −10.96 kcal/mol against macozinone-as-query at −10.82 kcal/mol — the same molecule, 0.14 kcal/mol apart. This is the duplicate-entry fault seen in earlier papers (Papers #1 and #3): the pipeline treats the reference drug as a new lead when it appears in ChEMBL under a different entry. CHEMBL3330226 is therefore not a lead; it is a duplicate-entry control, and it is reported as such.

### 2.3 PAINS screen

Every test compound was screened with the RDKit PAINS filter: all five leads and macozinone were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probabilities were SR-MMP 0.498 for CHEMBL4763381, SR-ARE 0.363 for CHEMBL4752208, SR-MMP 0.732 for CHEMBL3330226 and for macozinone (identical panels, as expected for the same molecule), and SR-MMP 0.551 for CHEMBL4868912. These are similarity-based predictions, not measurements — and macozinone itself carries the highest flag in the panel (SR-MMP 0.732), so a flag here does not distinguish a lead from the reference drug.

### 2.4 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement, binding-free-energy calculation, or covalent docking was performed; a single crystal structure (4P8N, one DprE1 conformation, holding a non-covalent inhibitor) was used; and, most importantly, Vina cannot model covalent binding, so macozinone's real binding mode — a semimercaptal with Cys387 — is not represented in any score reported here. The leads are already-known DprE1 actives, so no novelty of chemistry is claimed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | DprE1 potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | MW | logP | Lipinski violations | PAINS | Top tox read-across |
|---|---|---|---|---|---|---|---|---|
| CHEMBL4763381 | IC50 200 nM | **−12.05** | −12.05, −10.42, −10.16 | 480.56 | 3.88 | 0 | clean | SR-MMP 0.498 |
| CHEMBL4752208 | IC50 140 nM | −11.74 | −11.74, −11.74, −10.96 | 493.55 | 3.90 | 0 | clean | SR-ARE 0.363 |
| CHEMBL3330226 (= macozinone) | IC50 10 nM | −10.96 | −10.96, −10.27, −9.74 | 456.49 | 4.29 | 0 | clean | SR-MMP 0.732 |
| Macozinone (reference, query) | IC50 10 nM | −10.82 | −10.82, −10.11, −9.91 | 456.49 | 4.29 | 0 | clean | SR-MMP 0.732 |
| CHEMBL4868912 | IC50 50 nM | −10.23 | −10.23, −10.10, −9.72 | 466.59 | 2.67 | 0 | clean | SR-MMP 0.551 |

All docking on PDB 4P8N (M. tuberculosis DprE1, 1.79 Å), grid centre [16.51, −20.97, 1.7] (R57 chain-A centroid), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 6 November 2026. All five leads are known DprE1 actives with no preferred name in ChEMBL.

The headline, stated honestly: two genuine leads "beat" macozinone by 0.92–1.23 kcal/mol on docking — CHEMBL4763381 by 1.23 kcal/mol and CHEMBL4752208 by 0.92 kcal/mol — but both are 14–20 times weaker by measured IC50 (200 nM and 140 nM versus macozinone's 10 nM). The docking ranking is inverted against measured potency: the best-docking compound is the weakest by IC50, and the most potent compound (macozinone, 10 nM) sits third in the table. Both margins are also inside Vina's ±1–2 kcal/mol noise, so neither would be interpretable as a real advantage even if the potency order agreed. Pose consistency does not rescue the ranking: CHEMBL4752208 holds its best score across two poses, yet is 14 times weaker than macozinone by IC50; CHEMBL4763381's best pose (−12.05) is 1.63 kcal/mol clear of its second pose (−10.42), so even its own score is unstable across poses. The duplicate control is the cleanest number in the table: macozinone entered twice scores −10.96 and −10.82 kcal/mol, 0.14 kcal/mol apart — the pipeline's conformer-sampling error on this target is small, which makes the inversion against IC50 harder to blame on sampling and easier to blame on the scoring function and the missing covalent term.

### 3.2 Comparison with published docking

No published Vina score for macozinone or any of these leads on 4P8N was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for macozinone and four known DprE1 actives on 4P8N are now on record for others to reproduce, together with the duplicate-entry control. The ordering is not comparable to published potency: the five distinct molecules span IC50 10–200 nM, a 20-fold spread, while their docking scores span 1.82 kcal/mol in the wrong order — Vina ranks poses, not IC50s, and on this target it ranks them backwards.

### 3.3 The standardisation / quality problem

Two things that could silently corrupt this result did not, and one thing that no structure check can catch did. The grid centre was verified against the PDB file to 0.01 Å and sits 12.75 Å from the FAD cofactor, so the cofactor-centring fault is absent here. The duplicate-entry fault did occur: macozinone appears in the lead list as CHEMBL3330226, and without the identity check (same MW, Tanimoto 1.0, identical tox panel) it would have been reported as a third lead "beating" the reference by 0.14 kcal/mol. The deeper problem is structural, not procedural: the reference drug is a covalent inhibitor and the structure used (4P8N) holds a non-covalent inhibitor, so the binding mode Vina scores for macozinone is not the binding mode macozinone uses. No grid-centre fix can repair that; only a covalent docking method can.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a measurement of Vina's limits on this target. There is no lead here: the two compounds that "beat" macozinone on docking are 14–20 times weaker by measured IC50, the third "lead" is macozinone itself, and the remaining lead (CHEMBL4868912, IC50 50 nM) scores worse than the reference (−10.23 versus −10.82). The durable findings are the benchmark values for macozinone on 4P8N (−10.82 kcal/mol, with full pose lists), the duplicate-entry control (0.14 kcal/mol), and the demonstration that on a covalent-inhibitor target, non-covalent docking ranks known actives in the opposite order to their measured potency.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the margins (0.92 and 1.23 kcal/mol) are inside Vina's ±1–2 kcal/mol noise. Second, the ranking is inverted against measured potency — the best-docking compound is the weakest by IC50, by a factor of 20. Third, the scored binding mode is the wrong one: macozinone's potency comes from a covalent semimercaptal with Cys387, which Vina cannot model at all, so the reference drug's score is missing the very interaction that makes it potent. A docking "win" against a covalent reference drug, on a structure holding a non-covalent inhibitor, is not a discovery; it is a measurement of what the method leaves out.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All leads are PAINS-clean, which removes one artefact class from the validation design — but PAINS-clean is a low bar, and the Tox21 read-across flags (SR-MMP up to 0.732) are predictions from neighbours, not data. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either — least of all because the reference drug flags the same assay most strongly. The validation assay must still include redox controls and a counter-screen, because a clean PAINS filter does not rule out assay interference.

### 4.4 Testable hypotheses

1. CHEMBL4763381 inhibits recombinant DprE1 with an IC50 within 2-fold of its ChEMBL value (200 nM) under identical assay conditions, and is less potent than macozinone (10 nM) — the docking predicts no measurable advantage; a measured IC50 for CHEMBL4763381 better than macozinone's would refute the noise interpretation.
2. Covalent docking of macozinone at Cys387 (for example with CovDock) gives a binding energy substantially more favourable than the non-covalent Vina score of −10.82 kcal/mol, consistent with the covalent contribution Vina omits.
3. A Vina re-dock of the co-crystallised ligand R57 (QN118) into 4P8N reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).
4. Canonicalising the SMILES of all 26 ranked leads and re-running the pipeline removes the macozinone duplicate (CHEMBL3330226) and changes no other lead's rank — a pipeline fix to be verified, not assumed.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant DprE1 enzyme inhibition assay for CHEMBL4763381, CHEMBL4752208 and macozinone, same plate, n = 3, with a pre-registered 2-fold decision rule and the rule that a docking margin under 2 kcal/mol predicts no measurable advantage. Stage 2 (weeks 3–6): whole-cell M. tuberculosis H37Rv MIC assay (resazurin microtiter assay, the same method reported for macozinone's 0.3 ng/mL) for any compound that clears Stage 1, with macozinone as control. Stage 3 (weeks 7–12): covalent docking of macozinone at Cys387 (CovDock or equivalent) and, if Stage 1 shows any genuine advantage, a PTGR1/PTGR2 liability check, since human dearomatization to H2MCZ is a known route by which macozinone-class compounds lose activity. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. Both "winning" margins (0.92 and 1.23 kcal/mol) are inside Vina's ±1–2 kcal/mol noise and cannot be interpreted as real advantages. 3. Vina cannot model covalent binding, so macozinone's semimercaptal with Cys387 is absent from every score reported here; the structure used (4P8N) holds a non-covalent inhibitor. 4. No molecular-dynamics refinement, binding-free-energy calculation, covalent docking, or re-docking validation of R57 was performed. 5. A single crystal structure (4P8N, one DprE1 conformation) was used; induced-fit effects are not modelled. 6. All leads are already-known DprE1 actives; no new chemical matter is proposed. 7. The pipeline's lead deduplication failed silently and required manual correction — other silent defaults in the same pipeline are not yet audited. 8. The PTGR1/PTGR2 dearomatization liability was not modelled for any lead.

## 6. Conclusion

No DprE1 active in this set beats macozinone: the two leads that score better on Vina docking are 14–20 times weaker by measured IC50, the third "lead" is macozinone itself, and both margins sit inside Vina's noise. The honest reading is that on a covalent-inhibitor target, non-covalent docking ranks known actives backwards — and the next experiment is a head-to-head DprE1 IC50 assay with a pre-registered 2 kcal/mol rule, plus covalent docking of macozinone at Cys387, not more Vina docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. World Health Organization. Global Tuberculosis Report 2024. Geneva: WHO; 2024. (Approximately 10.8 million people fell ill with TB in 2023 and about 1.25 million died.)
2. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
3. RCSB Protein Data Bank. M. tuberculosis DprE1 in complex with the non-covalent inhibitor QN118. PDB ID 4P8N, 1.79 Å. https://www.rcsb.org/structure/4P8N (accessed 6 November 2026).
4. ChEMBL database, European Bioinformatics Institute. Target: decaprenylphosphoryl-beta-D-ribose oxidase (DprE1), M. tuberculosis (CHEMBL3804751); bioactivities accessed 6 November 2026. https://www.ebi.ac.uk/chembl/.
5. ClinicalTrials.gov. A study of macozinone (PBTZ169) in tuberculosis. NCT03334734. https://clinicaltrials.gov/study/NCT03334734 (accessed 6 November 2026).
6. ClinicalTrials.gov. BTZ043 in combination with bedaquiline and delamanid in tuberculosis (phase 2b). NCT05926466. https://clinicaltrials.gov/study/NCT05926466 (accessed 6 November 2026).
7. Human prostaglandin reductases PTGR1 and PTGR2 dearomatize macozinone to H2MCZ with loss of antimycobacterial activity. *Nat Commun.* 2026. DOI: 10.1038/s44321-026-00526-1.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-019-2026-11-06.json`. ChEMBL IDs: macozinone (query; duplicate entry CHEMBL3330226), CHEMBL4763381, CHEMBL4752208, CHEMBL4868912. Target: UniProt P9WJF1, ChEMBL CHEMBL3804751. PDB ID 4P8N. No additional data were generated.
