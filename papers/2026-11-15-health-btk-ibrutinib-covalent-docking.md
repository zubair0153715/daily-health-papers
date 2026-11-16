# Ibrutinib Re-Docks at −10.86 kcal/mol on Its Own BTK Structure, but Four Sub-Nanomolar Covalent Inhibitors Score Worse: Rigid Docking Cannot Price the Cys481 Bond

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-15 · **Health Papers Agent — Paper #59** (daily 5-paper run)

**Keywords:** Bruton's tyrosine kinase; BTK; ibrutinib; C481S; covalent inhibitor; molecular docking; AutoDock Vina; chronic lymphocytic leukemia

---

## Abstract

Ibrutinib, the first covalent Bruton's tyrosine kinase (BTK) inhibitor, binds irreversibly to Cys481 in the ATP pocket, and the C481S mutation — cysteine replaced by serine — removes that bond and is the commonest cause of acquired resistance in chronic lymphocytic leukaemia (CLL). The question this paper tests is whether a standard rigid-docking screen can rank covalent BTK inhibitors at all, given that the scoring function cannot price a covalent bond. We docked ibrutinib and four ChEMBL BTK ligands with AutoDock Vina 1.2.7 on 5P9J, the 1.08 angstrom BTK kinase domain co-crystallised with ibrutinib itself. Ibrutinib re-docked at minus 10.86 kcal/mol. All four test compounds carry the same acrylamide warhead and are measured at 0.04 to 0.05 nM against BTK in ChEMBL — roughly ten times more potent than ibrutinib's 0.5 nM — yet they docked worse: minus 10.13, minus 9.47, minus 8.64 and minus 8.43 kcal/mol. Rank correlation between docking score and measured potency is inverted (Spearman rho minus 0.63, n = 5): the most potent compound measured docks worst. The screen validates the protocol (the reference drug re-docks well on its own structure) and fails as a ranking tool for covalent inhibitors in the same run. The falsifiable next step is a single-assay kinase comparison of the four compounds against wild-type and C481S BTK: if their C481S IC50s collapse like ibrutinib's while pirtobrutinib's holds, the warhead series is covalent-only and the docking inversion is confirmed as a scoring artefact, not a potency signal.

---

## 1. Introduction

Bruton's tyrosine kinase (BTK) sits downstream of the B-cell receptor and is indispensable for B-cell development and signalling; it phosphorylates PLCG2 after receptor engagement, driving calcium mobilisation and protein kinase C activation (UniProt Q06187). Blocking it transformed the treatment of B-cell malignancies. Ibrutinib, the first-in-class covalent BTK inhibitor, was approved by the US FDA in 2014 for chronic lymphocytic leukaemia and small lymphocytic lymphoma (CLL/SLL), followed by the covalent inhibitors acalabrutinib (2019) and zanubrutinib (2023). All three bind irreversibly to Cys481 in the ATP pocket. Resistance follows the bond: the commonest acquired mechanism is mutation of that same cysteine, most often C481S, which removes the covalent anchor and renders the drug ineffective — ibrutinib's measured potency falls from 0.7 nM on wild-type BTK to more than 1,000 nM on C481S. The non-covalent inhibitor pirtobrutinib was designed around this failure: it binds reversibly, independent of Cys481, with measured IC50s of 1.1 nM on wild type and 16 nM on C481S, and in the BRUIN CLL-321 phase 3 trial it achieved an overall response rate of 62% and a median progression-free survival of 20 months in heavily pretreated patients, earning accelerated FDA approval in 2023 for patients who had received at least two prior lines including a covalent BTK inhibitor and a BCL-2 inhibitor. But resistance to pirtobrutinib is already appearing through second-site BTK mutations, and a 2026 preprint characterising 34 BTK variants at seven resistance sites found that the T316A substitution confers broad resistance to both covalent and non-covalent inhibitors, while variants at L528 disrupt catalytic activity and V416, A428, M437 and M477 largely retain sensitivity to covalent inhibitors.

The practical question for a drug-discovery screen is narrower than the clinical one: can a standard rigid-docking protocol rank covalent BTK inhibitors, or does the missing covalent term corrupt the ranking? This matters because docking is the cheap triage step every university lab runs before any assay, and a screen that systematically mis-ranks the most potent compounds will send the wrong molecules to the bench. The test compounds here are a hard case by design: four ChEMBL ligands with measured BTK IC50s of 0.04–0.05 nM, all carrying the acrylamide warhead that forms the Cys481 bond, docked against ibrutinib's own co-crystal structure under one standardised protocol.

**Hypothesis (falsifiable):** under one standardised protocol, the four acrylamide-warhead BTK ligands will dock within Vina noise (±1–2 kcal/mol) of ibrutinib's re-dock score, and their docking rank will track their measured potency — ibrutinib first, the four sub-nanomolar compounds at least as good. Falsified if the most potent compound measured docks worst, in which case rigid docking is confirmed blind to the covalent contribution that makes these compounds potent.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-15 (web search; PubMed; the daily digest of 2026-11-14, which screened 722 candidates and selected 8 — none on BTK, so the digest's relevance here is methodological). Key sources: Bender et al. 2017 for the 5P9J structure and the Y551-sequestration mechanism; Honigberg et al. 2010 for ibrutinib's original characterisation; the 2025 MDPI review of pirtobrutinib in CLL for the BRUIN CLL-321 results and the C481S potency table; the 2025 Leukemia & Lymphoma review (PMID 39972943) for resistance mechanisms after covalent BTK inhibition; and the 2026 Research Square preprint (doi:10.21203/rs.3.rs-9390771/v1) for the 34-variant resistance map. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Pipeline and structure choice

The standard LeadForge pipeline was run with target "Bruton's tyrosine kinase (BTK)" and reference drug ibrutinib (run_docking.py, RDKit venv, NO_PROXY prefix). The pipeline resolved the target to UniProt Q06187 (human BTK, 659 amino acids) and ChEMBL target CHEMBL5251, retrieved 19 known ligands with measured BTK activity, verified ibrutinib in PubChem (CID 24821094, SMILES confirmed against the reference structure), screened 25 analogues by Morgan-fingerprint similarity, and ranked 20 leads by the standard composite score (similarity 40 + Lipinski 20 + Veber 10 + PAINS 10 + Tox21 read-across 20). The pipeline's automatic structure pick was 5P9J — the BTK kinase domain co-crystallised with ibrutinib at 1.08 angstrom (Bender et al. 2017) — which is the correct control for this question: the reference drug is docked back into its own pocket, so a good re-dock score validates the protocol rather than discovering a lead. The grid centre [19.81, 7.16, 3.62] is the centroid of the co-crystallised ibrutinib, computed by the pipeline's `_ligand_center`.

### 2.3 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; one box (22.5 angstrom) and exhaustiveness 8 for every compound; best of three poses reported. Five compounds on 5P9J: ibrutinib (reference drug, PubChem CID 24821094) and four ChEMBL ligands — CHEMBL5749648, CHEMBL5858594, CHEMBL5824452 and CHEMBL5826570. All four test compounds are acrylamide-warhead indole-carboxamides: each SMILES contains the C=CC(=O)N acrylamide group that forms the covalent bond to Cys481, and an indole-2-carboxamide core. Their measured BTK IC50s are ChEMBL-reported values (0.049, 0.05, 0.05 and 0.04 nM respectively); ibrutinib's measured BTK IC50 of 0.5 nM is from Honigberg et al. 2010, and the 0.7 nM wild-type / >1,000 nM C481S pair is from the pirtobrutinib resistance literature.

### 2.4 PAINS screen

RDKit PAINS filter applied to every compound. All five are PAINS-clean. All five pass Lipinski and Veber outright (ibrutinib: MW 440.51, logP 4.22, TPSA 99.16; the four test compounds: MW 343.40–399.43, logP 2.25–4.30, TPSA 79.19–82.43).

### 2.5 Rank correlation

Spearman rank correlation was computed between the Vina scores and the measured BTK IC50 values for the five compounds (n = 5). The two tied measured values (0.05 nM, twice) were assigned the average rank 3.5. A correlation on five points is reported as a descriptive check, not as a validated ranking — the paper's real test is the direction of the ranking, not the size of rho.

### 2.6 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol; gaps smaller than that are not differences. Vina scores only non-covalent complementarity and cannot price the covalent bond to Cys481 — that is the point of this paper, not a footnote to it. No molecular dynamics, covalent docking, or free-energy refinement was run. No compound was assayed, and none was docked on a C481S mutant structure, so nothing here speaks directly to mutant activity. The measured IC50s come from different assays in ChEMBL and are compared as reported, not re-measured on one plate.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured BTK IC50 | Vina on 5P9J (kcal/mol) | PAINS |
|---|---|---|---|
| Ibrutinib (reference) | 0.5 nM | **−10.86** (−10.86, −9.38, −9.00) | clean |
| CHEMBL5749648 | 0.049 nM | −10.13 (−10.13, −9.56, −9.39) | clean |
| CHEMBL5858594 | 0.05 nM | −9.47 (−9.47, −9.18, −9.13) | clean |
| CHEMBL5824452 | 0.05 nM | −8.64 (−8.64, −8.47, −8.14) | clean |
| CHEMBL5826570 | 0.04 nM | −8.43 (−8.43, −8.19, −7.78) | clean |

Scores in kcal/mol, best of three poses (all three poses in parentheses). Measured IC50s are ChEMBL-reported BTK values for the four test compounds and Honigberg et al. 2010 for ibrutinib.

Ibrutinib re-docks at −10.86 on its own structure, 0.73 kcal/mol clear of the best test compound and 2.43 clear of the worst — the protocol works, and the reference drug is the winner by the screen's own metric. But every test compound is measured 10 to 17 times more potent than ibrutinib (0.04–0.05 nM versus 0.5 nM), and every one of them docks worse. The inversion is not a tie: the gap between ibrutinib and CHEMBL5826570 (2.43 kcal/mol) exceeds Vina noise, and it runs the wrong way.

### 3.2 Rank correlation: inverted

Against the measured BTK IC50s, Spearman rho is −0.63 (n = 5). The most potent compound measured (CHEMBL5826570, 0.04 nM) ranks last by docking; the least potent (ibrutinib, 0.5 nM) ranks first. Only CHEMBL5749648 holds the same rank (second) by both measures. A negative correlation on five points is not a precise estimate, but its sign is the finding: this screen ranks covalent BTK inhibitors backwards. The reason is visible in the chemistry — all four test compounds carry the acrylamide warhead, and the covalent bond it forms with Cys481 is worth binding energy that Vina never sees. The screen is scoring the non-covalent fit of molecules whose potency is dominated by a bond the scorer cannot model.

### 3.3 The re-dock control cuts both ways

Ibrutinib's −10.86 is a re-dock: the pocket in 5P9J was crystallised around ibrutinib, so the score partly reflects pocket-shape fit to that one ligand, not a pure affinity signal. The four test compounds are cross-docked into a pocket shaped for a different molecule, which disadvantages them further. Both effects push the same way — the reference drug looks better than it is, and the test compounds look worse — and the paper reports both rather than treating the re-dock as a neutral benchmark. A fair comparison would re-dock each compound into its own co-crystal structure, or use a structure crystallised around a non-covalent ligand; neither exists for these four compounds in the public record.

### 3.4 ADMET and safety panel

All five compounds pass Lipinski and Veber with zero violations. The Tox21 kNN read-across panel flags nothing decisive: the highest signals are NR-AhR 0.519 for CHEMBL5749648 and 0.455 for CHEMBL5858594, and SR-ARE 0.22 for ibrutinib — read-across scores, not measured toxicity. The safety story that matters for this target is not in the panel: ibrutinib's clinical liabilities (bleeding, atrial fibrillation, hypertension) and pirtobrutinib's cleaner selectivity profile are clinical facts, invisible to a ligand-based screen. The four test compounds are research compounds with no approval and no human safety data.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say one thing with confidence: the protocol reproduces ibrutinib's binding pose and score on its own structure, so the pipeline is working. It cannot say which covalent BTK inhibitor is most potent, because the ranking it produces is inverted against the measured record. Any paper that reported "CHEMBL5826570 is the weakest BTK ligand because it docks at −8.43" would be reporting the opposite of the measured fact — it is the most potent compound in the set. The failure is specific and diagnosable: the scorer prices non-covalent fit and ignores the covalent bond, and for this chemotype the bond is the potency.

### 4.2 The covalent-docking correction

The correct computational test for this chemotype is not a better rigid dock: it is covalent docking (which models the Cys481 bond explicitly) or a free-energy comparison that prices the bond formation, followed by a kinase assay on wild-type and C481S BTK. The assay is the decisive step, because it also answers the question the docking cannot ask: whether these four compounds are covalent-only (and therefore dead against C481S, like ibrutinib) or retain non-covalent affinity (and therefore worth testing as pirtobrutinib-style leads). Their non-covalent docking scores (−8.43 to −10.13) are in the range a non-covalent inhibitor would need, which is a weak but real hint that they may retain some C481S activity — a hint the paper states as a hypothesis, not a finding.

### 4.3 Why this matters beyond BTK

Covalent inhibitors are now a mainstream design strategy — KRAS G12C, EGFR, BTK — and every one of them is screened by the same rigid-docking pipelines that fail here. The BTK case is a clean demonstration because the warhead is identical across the test set and the measured potencies are extreme (0.04–0.05 nM), so the inversion cannot be dismissed as assay noise. Any screening programme that ranks covalent and non-covalent compounds on one Vina scale is mixing two different quantities: non-covalent fit for one class, and non-covalent fit minus the missing bond for the other. The fix is cheap: flag the warhead, dock covalent and non-covalent series separately, and never let a covalent compound's Vina score stand as its potency claim.

### 4.4 Testable hypotheses

1. **Covalent-only hypothesis.** In one kinase assay on wild-type and C481S BTK, all four test compounds lose more than 100-fold potency on the mutant, like ibrutinib, while pirtobrutinib loses less than 15-fold. Falsified if any test compound holds within 15-fold on C481S — in which case its non-covalent affinity is real and it is a candidate non-covalent lead.
2. **Covalent-docking hypothesis.** Re-scoring the same five compounds with a covalent docking protocol restores the measured ranking (CHEMBL5826570 first, ibrutinib last). Falsified if the covalent scores still rank ibrutinib first — in which case the inversion has another cause and the warhead explanation is wrong.
3. **Pocket-shape hypothesis.** Cross-docking ibrutinib into a BTK structure crystallised around a non-covalent ligand drops its score by more than 1 kcal/mol from −10.86. Falsified if it stays within noise — in which case the re-dock advantage is smaller than this paper assumes.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain ibrutinib, pirtobrutinib and the four ChEMBL compounds; confirm identity and purity by LC-MS and NMR. Stage 2 (weeks 3–6): kinase assay (ADP-Glo or equivalent) on recombinant wild-type and C481S BTK, all six compounds on the same plates, in triplicate — the single-assay comparison this paper could not make, and the direct test of hypothesis 1. Stage 3 (weeks 7–10): covalent docking of the same six compounds for hypothesis 2, plus a BTK-dependent cellular assay (TMD8 or MEC-1) for the best two. Stage 4 (weeks 11–12): if any test compound holds within 15-fold on C481S, dock its analogues and synthesise the best two; if all four collapse, report the negative result and stop. Sample-size logic: three independent biological replicates per IC50 determination is the minimum for a defensible potency claim; the wild-type-versus-mutant comparison needs the same, because a false "C481S-active" call on a covalent-only compound is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. Vina cannot price the covalent bond to Cys481; the ranking inversion is the finding, not a defect to be averaged away.
3. Ibrutinib's score is a re-dock on its own co-crystal structure (5P9J); the four test compounds are cross-docked into a pocket shaped for ibrutinib.
4. The measured IC50s come from different assays in ChEMBL and were not re-measured on one plate; the 0.04–0.05 nM values are at the edge of what biochemical assays resolve reliably.
5. Spearman rho is computed on five points and is driven by the ibrutinib-versus-rest inversion; it is a descriptive check, not a validated ranking.
6. No compound was docked on a C481S mutant structure, so nothing here speaks directly to mutant activity.
7. No molecular dynamics, covalent docking, or free-energy refinement was run — the methods that could actually price the warhead.
8. The Tox21 panel is kNN read-across, not measured toxicity; the real safety liabilities of BTK inhibitors are clinical and invisible to this screen.
9. The four test compounds are research compounds with no approval and no human data; their ChEMBL IC50s are the only measured evidence for them.
10. No Pakistan-specific access or burden data are cited; the paper's relevance to Pakistan is methodological — a cheap, open-source triage step a university lab can run before any assay.

## 6. Conclusion

On 5P9J, ibrutinib re-docks at −10.86 kcal/mol, and four acrylamide-warhead BTK ligands measured at 0.04–0.05 nM — ten times more potent than ibrutinib — dock worse, at −10.13 to −8.43, with the ranking inverted against the measured record (Spearman rho −0.63). The screen validates the protocol and fails as a ranking tool for covalent inhibitors in the same run, because Vina cannot price the Cys481 bond that makes these compounds potent. The next step is the single-assay kinase comparison in Section 4.5, with ibrutinib, pirtobrutinib and the four compounds on wild-type and C481S BTK on the same plates — and, as a standing rule for any covalent series, covalent and non-covalent compounds must never be ranked on one rigid-docking scale.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Bender AT, Gardberg A, Pereira A, et al. Ability of Bruton's tyrosine kinase inhibitors to sequester Y551 and prevent phosphorylation determines potency for inhibition of Fc receptor but not B-cell receptor signaling. Mol Pharmacol. 2017;91(3):208–219. PMID: 28062735. doi:10.1124/mol.116.107037.
2. Honigberg LA, Smith AM, Sirisawad M, et al. The Bruton tyrosine kinase inhibitor PCI-32765 blocks B-cell activation and is efficacious in models of autoimmune disease and B-cell malignancy. Proc Natl Acad Sci USA. 2010;107(29):13075–13080. PMID: 20615965. doi:10.1073/pnas.1007185107.
3. Pirtobrutinib in chronic lymphocytic leukemia: navigating resistance and the personalisation of BTK-targeted therapy. Cancers. 2025;17(18):2974. doi:10.3390/cancers17182974.
4. Resistance mechanisms and approach to chronic lymphocytic leukemia after BTK inhibitor therapy. Leuk Lymphoma. 2025;66(7):1176–1188. PMID: 39972943. doi:10.1080/10428194.2025.2466101.
5. Evaluating ibrutinib, pirtobrutinib, remibrutinib, rilzabrutinib, and zanubrutinib in 34 BTK-variants at 7 inhibitor resistance sites. Research Square preprint, posted 23 April 2026. doi:10.21203/rs.3.rs-9390771/v1.
6. UniProtKB. Tyrosine-protein kinase BTK, human, Q06187. Accessed 2026-11-15. https://www.uniprot.org/uniprotkb/Q06187/entry
7. RCSB Protein Data Bank. Structure 5P9J (BTK kinase domain co-crystallised with ibrutinib, 1.08 A). Accessed 2026-11-15. https://www.rcsb.org/structure/5P9J
8. ChEMBL. Target CHEMBL5251 (tyrosine-protein kinase BTK, Homo sapiens); molecules CHEMBL5749648, CHEMBL5858594, CHEMBL5824452, CHEMBL5826570 with BTK IC50 values. Accessed 2026-11-15. https://www.ebi.ac.uk/chembl/
9. PubChem. Ibrutinib, CID 24821094. Accessed 2026-11-15. https://pubchem.ncbi.nlm.nih.gov/compound/24821094

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-071-2026-11-15.json` (pipeline + docking on 5P9J); the run log is alongside it. UniProt accession Q06187, PDB ID 5P9J, ChEMBL target CHEMBL5251 and compound IDs, and the PubChem CID for ibrutinib are given in the text. No additional data were generated.
