# Momelotinib Re-Docks Best on JAK2 (8BXH) With a PAINS Alert, and the Rank Correlation Flips Sign Between Kd and IC50

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-13 · **Health Papers Agent — Paper #56** (daily 5-paper run)

**Keywords:** JAK2; ruxolitinib; momelotinib; myelofibrosis; molecular docking; AutoDock Vina; rank correlation; PAINS

---

## Abstract

JAK2 inhibitors transformed myelofibrosis care: ruxolitinib first in 2011, then fedratinib, pacritinib and momelotinib, all ATP-competitive inhibitors of the same JH1 kinase domain, differing mainly in their selectivity and in which cytopenias they worsen or spare. The question is whether a standard docking screen can rank them by their measured potency on the JAK2 structure. We docked six compounds into 8BXH, the JAK2 JH1 structure co-crystallised with momelotinib (1.3 angstrom), with AutoDock Vina 1.2.7 under one protocol: the four myelofibrosis drugs, plus tofacitinib and baricitinib as cross-class comparators. Momelotinib re-docked best at minus 9.73 kcal/mol, ruxolitinib scored minus 8.73 and pacritinib worst at minus 7.67. The rank test depends on which potency measure is used: against the four drugs' IC50 values the Spearman rho is 0.2, against their Kd values it is minus 0.4, both on four compounds, so the screen has no defensible rank signal either way. Momelotinib also carries the screen's only PAINS alert, despite being an approved drug, and the most selective drug in the set, pacritinib at 26-fold over JAK1, docks worst — a property the single-target screen cannot measure at all. The falsifiable next step is a single-assay kinase comparison of all six compounds on JAK2, with JAK1 selectivity measured on the same plates: if the measured order matches the Kd record rather than the Vina order, docking alone must not be used to prioritise JAK2 inhibitors on this structure.

---

## 1. Introduction

Myelofibrosis is a myeloproliferative neoplasm driven in most patients by the JAK2 V617F mutation, which leaves the kinase constitutively active and the bone marrow progressively fibrotic. Four ATP-competitive JAK2 inhibitors are approved for it — ruxolitinib (2011), fedratinib (2019), pacritinib (2022) and momelotinib (2023) — and they are distinguished less by their JAK2 potency than by their selectivity and their haematologic cost: ruxolitinib worsens anaemia, pacritinib spares platelets, momelotinib improves anaemia through ACVR1 inhibition. Their JAK2 potencies were measured head-to-head in one study (Miao et al. 2024, Lance Ultra kinase assay, 1 mM ATP): by IC50, ruxolitinib 3.2 nM, fedratinib 10 nM, momelotinib 11 nM, pacritinib 14 nM; by Kd, ruxolitinib 0.8 nM, fedratinib 4.3 nM, pacritinib 6.6 nM, momelotinib 6.7 nM. The two measures give different orders — pacritinib and momelotinib swap — which is the first warning that any rank test on this set is assay-dependent. A second study (Celik et al. 2023, Blood abstract, 1 mM ATP) gives a different order again: IC50 ruxolitinib 4 nM, fedratinib 14 nM, momelotinib 51 nM, pacritinib 53 nM.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen on 8BXH will rank the four myelofibrosis drugs in the same order as their measured potencies. The test is the rank correlation, not the best score — and the reference drug must itself dock, or the comparison is void.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-13 (web search; PubMed via the daily digest of 2026-11-13, which screened 627 candidates and selected 8, none on JAK2 — the digest's relevance is methodological, not topical, for this paper). Key sources: Miao et al. 2024 for the head-to-head Kd and IC50 values and the 8BXH structure; Celik et al. 2023 for the second, assay-dependent potency set. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented). Miao et al. 2024 Table 1 is the primary potency source; Celik et al. 2023 is cited only to show that the potency order is assay-dependent, not as a second primary.

### 2.2 ChEMBL outage and the PubChem fallback

The ChEMBL API was down on the whole of 2026-11-13: target search, target-by-accession and activity endpoints all returned HTTP 500, verified by direct calls, by a browser fetch and by a delegated browser task. The standard pipeline therefore retrieved zero ligands. The compounds in this paper were taken from PubChem by CID, with measured potencies attached only where a verified literature value exists. No analogues were fetched for this paper: the four myelofibrosis drugs plus two cross-class comparators are the complete set the topic poses.

### 2.3 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt O60674 (JAK2, human). One structure: 8BXH, JAK2 JH1 kinase domain in complex with momelotinib, 1.3 A X-ray (Miao et al. 2024). Centre [−11.91, 15.38, 20.25] — the centroid of the co-crystallised momelotinib computed from the deposited coordinates with the pipeline's own `_ligand_center` function; the distance to the largest HETATM group centroid is 0.0 A, confirming the box sits on the ATP site. Best of three poses reported per compound. The same box (22.5 A) and exhaustiveness (8) were used for every compound, including ruxolitinib itself. Six compounds: ruxolitinib (PubChem CID 25126798, reference drug), fedratinib (CID 16722836), momelotinib (CID 25062766, re-dock control), pacritinib (CID 46216796), tofacitinib (CID 9926791) and baricitinib (CID 44205240). The pipeline's earlier ruxolitinib score on the same structure and centre (−8.71) is a reproducibility check, not a second dataset: this run re-docked it under the single protocol reported here.

### 2.4 PAINS screen

RDKit PAINS filter (the pipeline's own filter, classes A–C) applied to every docked compound. Five compounds are PAINS-clean. Momelotinib carries a PAINS alert — the only alert in the screen, and the only alert in any of the five papers of this day's run.

### 2.5 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds; the gap between fedratinib and ruxolitinib here is 0.09 kcal/mol, which is no gap at all. The rank test is n = 4, so both Spearman values reported are descriptive statistics, not significant correlations — the finding is that the sign flips between the two potency measures, not that either number is powered. The four potencies come from one head-to-head study (Miao et al. 2024) but a second study (Celik et al. 2023) gives a different order, so the "measured order" itself is assay-dependent. Tofacitinib and baricitinib carry no head-to-head JAK2 value from Miao et al. 2024 Table 1, so they enter the screen as comparators, not as ranked compounds. A single rigid structure was docked; the JAK2 JH1 domain is known to move on inhibitor binding. No molecular dynamics or free-energy refinement was run. No experimental data were generated.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | 8BXH (kcal/mol) | Measured potency | PAINS |
|---|---|---|---|
| Momelotinib | −9.73 (−9.73, −9.64, −9.53) | JAK2 Kd 6.7 nM, IC50 11 nM | alert |
| Fedratinib | −8.82 (−8.82, −8.77, −8.50) | JAK2 Kd 4.3 nM, IC50 10 nM | none |
| Ruxolitinib (reference) | −8.73 (−8.73, −8.57, −8.24) | JAK2 Kd 0.8 nM, IC50 3.2 nM | none |
| Baricitinib | −8.64 (−8.64, −8.50, −8.01) | No head-to-head JAK2 value from Miao 2024 Table 1 | none |
| Tofacitinib | −8.22 (−8.22, −8.00, −7.88) | No head-to-head JAK2 value from Miao 2024 Table 1 | none |
| Pacritinib | −7.67 (−7.67, −7.39, −7.07) | JAK2 Kd 6.6 nM, IC50 14 nM | none |

Momelotinib re-docks best at −9.73, 0.91 kcal/mol clear of fedratinib — the largest separation in the screen, and the only one that approaches a defensible margin. Its three poses are tight (−9.73, −9.64, −9.53), so the score is a stable pose result. Everything from fedratinib down to pacritinib spans 1.15 kcal/mol, inside Vina's noise: the order among those five compounds cannot be defended from these scores. Ruxolitinib's −8.73 reproduces the pipeline's earlier −8.71 on the same structure and centre to within 0.02 kcal/mol, so the protocol is stable; the ranking failure is in the scoring, not in the preparation.

The rank test the hypothesis posed, against the IC50 order: the measured order is ruxolitinib (3.2 nM) > fedratinib (10 nM) > momelotinib (11 nM) > pacritinib (14 nM). The Vina order is momelotinib (−9.73) > fedratinib (−8.82) > ruxolitinib (−8.73) > pacritinib (−7.67). Spearman rho = 0.2 (n = 4). Against the Kd order — ruxolitinib (0.8 nM) > fedratinib (4.3 nM) > pacritinib (6.6 nM) > momelotinib (6.7 nM) — the same Vina order gives Spearman rho = −0.4 (n = 4). The correlation flips sign depending on which potency measure is used, because pacritinib and momelotinib swap between the two measures. The hypothesis is falsified on either measure: a rho of 0.2 and a rho of −0.4 are both no rank signal, and the sign flip means the test cannot even say which direction the signal points.

### 3.2 The PAINS alert on an approved drug

Momelotinib is the only compound in the screen with a PAINS alert, and it is also the best-scoring compound and an FDA-approved drug. PAINS filters exist to flag assay-interference chemotypes in screening libraries; an approved drug tripping the filter is a reminder that the filter is a screening heuristic, not a drug-likeness test. The alert does not invalidate momelotinib — its clinical record does that work — but it does mean the best score in this screen carries a flag that a naive pipeline would use to discard it. A pipeline that filtered on PAINS before ranking would have removed the best-docking compound in the set, and a pipeline that ranked before filtering would have promoted a flagged one. Either order of operations changes the answer, which is itself a finding about the pipeline.

### 3.3 Selectivity is the property the screen cannot see

Miao et al. 2024 also report JAK2-over-JAK1 selectivity: pacritinib 26-fold, momelotinib 13-fold, fedratinib 6-fold. That selectivity is the property that distinguishes these drugs clinically — pacritinib's platelet-sparing profile and momelotinib's anaemia benefit both trace to it — and a single-target docking screen cannot measure it at all. Pacritinib, the most selective drug in the set, docks worst at −7.67; momelotinib, the second most selective, docks best. The screen's order and the selectivity order are unrelated, and the screen has nothing to say about the property that matters most for choosing between these drugs.

### 3.4 Comparison with published docking

No published Vina benchmark of these six compounds on 8BXH was found at drafting time, so there is no published docking comparison to make. The depositing study for 8BXH is a structure and medicinal-chemistry paper, not a docking benchmark. The absence of a published comparator is stated, not filled in.

## 4. Discussion

### 4.1 The reframe

The paper's question changed while running it. It started as "which JAK2 inhibitor beats ruxolitinib?" and became "can this screen rank JAK2 inhibitors at all, and on which measure?" The answer is no on both measures, and the two measures disagree with each other. A screen whose rank correlation flips sign when the potency measure changes is not a screen with a weak signal — it is a screen with no signal for this target at this setting, and the honest report is the flip, not the best score.

### 4.2 Why the "win" must not be over-read

Momelotinib's −9.73 is the best score in the screen, and it is also the score of the third-most-potent drug by IC50 and the weakest by Kd, carrying the screen's only PAINS alert. It is a re-dock of the co-crystallised ligand, so a good score is expected: the pocket in 8BXH is shaped around momelotinib, exactly as 6LUB was shaped around CH7233163 in the HP-027 run of the same day. The value of the −9.73 is that the protocol is not broken — the same box and preparation that give pacritinib −7.67 give the co-crystal ligand −9.73 — not that momelotinib is a lead. It is already a drug.

### 4.3 The assay-dependence warning

The sign flip is the paper's most portable finding. Two potency measures from the same head-to-head study give opposite rank correlations, and a second study gives a third order entirely (Celik et al. 2023: ruxolitinib 4 nM, fedratinib 14 nM, momelotinib 51 nM, pacritinib 53 nM — a much wider spread than Miao's 3.2–14 nM). Any docking benchmark that reports a single correlation against a single potency table is reporting a correlation against one arbitrary choice of measure. A benchmark that does not test both Kd and IC50, and does not check a second study, can report a positive correlation that a different table would reverse.

### 4.4 Testable hypotheses

1. **Rank hypothesis.** In one kinase assay on JAK2 (Lance Ultra, 1 mM ATP, as in Miao et al. 2024), the IC50 order of the four myelofibrosis drugs matches the Miao et al. 2024 Table 1 order (ruxolitinib > fedratinib > momelotinib > pacritinib). Falsified if the measured order differs — in which case the published head-to-head order itself does not reproduce, and the docking comparison has no stable ground truth.
2. **PAINS hypothesis.** Momelotinib's PAINS alert is a filter artefact, not an assay-interference liability: in the kinase assay it shows no time-dependent or detergent-sensitive inhibition. Falsified if its inhibition is detergent-sensitive — in which case the alert is real and the compound's assay behaviour needs re-examination.
3. **Selectivity hypothesis.** Pacritinib retains its reported 26-fold JAK2-over-JAK1 selectivity when re-measured on the same plates as the other three drugs. Falsified if the selectivity collapses below ten-fold — in which case the property that distinguishes pacritinib clinically is a literature artefact.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain ruxolitinib, fedratinib, momelotinib, pacritinib, tofacitinib and baricitinib; confirm identity and purity by LC-MS and NMR. Stage 2 (weeks 3–6): kinase assay (Lance Ultra, 1 mM ATP) on recombinant JAK2 JH1 for all six compounds on the same plates, in triplicate, with ruxolitinib as the reference — the single-assay comparison this paper could not make — plus a detergent-sensitivity check on momelotinib to test the PAINS alert. Stage 3 (weeks 7–10): the same assay on JAK1 for the four myelofibrosis drugs, to re-measure the selectivity ratios on the same plates. Stage 4 (weeks 11–12): if any compound's measured order differs from both published orders, repeat that compound's assay in triplicate on a second day; if the orders agree with Miao et al. 2024, dock the four drugs into the JAK1 structure and compare the poses with the JAK2 poses. Sample-size logic: three independent biological replicates per IC50 determination is the minimum for a defensible potency; the selectivity comparison needs the same, because a false "selective" call is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. The rank test is n = 4, so both Spearman values (0.2 vs IC50, −0.4 vs Kd) are descriptive, not powered; the finding is the sign flip, not either number.
3. The "measured order" is assay-dependent: Miao et al. 2024 and Celik et al. 2023 give different orders for the same four drugs.
4. Tofacitinib and baricitinib carry no head-to-head JAK2 value from Miao et al. 2024 Table 1; they are comparators, not ranked compounds.
5. Vina noise is ±1–2 kcal/mol; five of the six compounds sit inside one noise band.
6. Momelotinib's PAINS alert is reported as the pipeline filter returns it; the specific substructure flagged was not identified in this run.
7. The re-dock of the co-crystallised ligand is expected to score well because the pocket is shaped around it; its score validates the protocol, not a lead.
8. A single rigid structure was docked; the JAK2 JH1 domain moves on inhibitor binding, and selectivity against JAK1 cannot be measured from a single-target screen.
9. No molecular dynamics or free-energy refinement was run.
10. The ruxolitinib reproduction (−8.71 pipeline vs −8.73 here) is a protocol-stability check on one compound, not a full replicate of the screen.

## 6. Conclusion

Four myelofibrosis drugs dock in no defensible order on the JAK2 structure 8BXH: the rank correlation is 0.2 against their IC50 values and −0.4 against their Kd values (n = 4), flipping sign between the two measures, and the co-crystallised ligand momelotinib re-docks best at −9.73 kcal/mol while carrying the screen's only PAINS alert. The screen is therefore a reproduced negative result with an assay-dependent ground truth, not a lead claim. The next step is the single-assay kinase comparison in Section 4.5, with all six compounds and the JAK1 selectivity measured on the same plates.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Miao et al. J Med Chem. 2024;67:10012–10024. PMID: 38843875. (Table 1, Lance Ultra kinase assay, 1 mM ATP; structure 8BXH.)
2. Celik et al. Blood. 2023 (ASH abstract). (Second potency set: JAK2 IC50 ruxolitinib 4 nM, fedratinib 14 nM, momelotinib 51 nM, pacritinib 53 nM.)
3. UniProtKB. Tyrosine-protein kinase JAK2, human, O60674. Accessed 2026-11-13. https://www.uniprot.org/uniprotkb/O60674/entry
4. RCSB Protein Data Bank. Structure 8BXH (JAK2 JH1 with momelotinib, 1.3 A). Accessed 2026-11-13. https://www.rcsb.org/structure/8BXH
5. PubChem. Ruxolitinib, CID 25126798; fedratinib, CID 16722836; momelotinib, CID 25062766; pacritinib, CID 46216796; tofacitinib, CID 9926791; baricitinib, CID 44205240. Accessed 2026-11-13. https://pubchem.ncbi.nlm.nih.gov/

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-049-2026-11-13.json`; the run log is `hidden_files/dock-HP-049-2026-11-13.log`. The pipeline's earlier ruxolitinib score on the same structure is in `hidden_files/dock-HP-049-2026-11-13-PIPELINE-QUERY-ONLY.json`. UniProt accession O60674, PDB ID 8BXH, and PubChem CIDs are given in the text. No additional data were generated.
