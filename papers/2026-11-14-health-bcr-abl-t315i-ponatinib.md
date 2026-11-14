# Ponatinib Scores −14.36 kcal/mol on BCR-ABL1 T315I and Imatinib Scores the Same on Wild Type and Mutant: Rigid Docking Fails the Gatekeeper Negative Control

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-14 · **Health Papers Agent — Paper #58** (daily 5-paper run)

**Keywords:** BCR-ABL1; T315I; ponatinib; imatinib; chronic myeloid leukemia; molecular docking; AutoDock Vina; gatekeeper mutation

---

## Abstract

Imatinib transformed chronic myeloid leukaemia (CML), but the T315I gatekeeper mutation — threonine 315 replaced by isoleucine — removes the hydrogen bond imatinib needs and sterically blocks the ATP pocket, conferring resistance to imatinib, dasatinib and nilotinib. Ponatinib was designed around this mutation, and asciminib now offers a myristoyl-pocket alternative, but no docking screen has been tested against the gatekeeper as a negative control. We docked ponatinib, imatinib and three ChEMBL ABL1 ligands (a GNF-7-series type-II inhibitor and two DFG-out hybrid ureas) with AutoDock Vina 1.2.7 on three murine Abl1 kinase-domain structures: wild type 3KFA (1.22 angstrom) and 3OXZ (2.2 angstrom, ponatinib-bound), and the T315I mutant 3OY3 (1.95 angstrom, AP24589-bound). Ponatinib re-docked at minus 14.33 kcal/mol on its own wild-type structure and scored minus 14.36 on T315I — indistinguishable, matching its measured sub-nanomolar potency on both forms (0.37 nM wild type, 2.0 nM T315I). But imatinib scored minus 10.41 on wild type and minus 9.60 on T315I, a 0.81 gap inside Vina noise, although its measured potency collapses from 10.8 nM on wild type to essentially inactive on T315I. The three other ligands cluster at minus 9.29 to minus 9.92 on both structures, and the choice of wild-type structure alone moves ponatinib's score by 2.79 kcal/mol — more than the mutation does. Rank correlation against measured ABL1 IC50s is weak (Spearman rho 0.5 on wild type, 0.6 on T315I, n = 5). The screen validates ponatinib's pan-BCR-ABL profile and fails its negative control in the same run. The falsifiable next step is a single-assay kinase comparison of ponatinib, imatinib and the GNF-7-series compound on wild-type and T315I ABL1: if imatinib's T315I IC50 is more than 100-fold weaker while its docking score is unchanged, rigid docking is confirmed blind to gatekeeper resistance.

---

## 1. Introduction

Chronic myeloid leukaemia (CML) is uncommon — about 35,380 new cases worldwide in 2021, roughly 15% of adult leukaemias — but it is the disease where targeted therapy advanced furthest, and where resistance has kept pace. The BCR::ABL1 fusion kinase drives the disease, and imatinib, approved in 2001, turned a fatal leukaemia into a chronic one. About a quarter of patients respond poorly to imatinib, and the commonest cause is a point mutation in the BCR::ABL1 kinase domain: more than 90 such mutations are reported, and each carries its own pattern of sensitivity to the available inhibitors.

The most treatment-resilient of them is T315I. Threonine 315 is the gatekeeper residue: it sits where inhibitors form a hydrogen bond that anchors them in the ATP pocket. Replacing threonine with isoleucine removes that hydrogen bond and puts a bulkier, hydrophobic side chain where the drug needs to sit. The result is resistance to imatinib and to the second-generation inhibitors dasatinib, nilotinib and bosutinib. T315I accounts for 4–19% of resistance mutations in published series, and in a 2025 prospective study from the Armed Forces Institute of Pathology in Pakistan (133 imatinib-resistant CML patients), kinase-domain mutations were found in 42.9% — but T315I in only 1 patient (0.8%), while the P-loop mutation E255K dominated at 33.8% and was the only mutation found in patients who had progressed to blast crisis. In that same cohort, only 2 patients were receiving ponatinib and 1 asciminib: the drugs that work against T315I are barely reaching the patients who need them in Pakistan.

Ponatinib was designed specifically for this mutation: a carbon–carbon triple bond (ethynyl linker) threads past the isoleucine side chain where other inhibitors clash. It inhibits native BCR-ABL at 0.37 nM and the T315I mutant at 2.0 nM in cell-free assays, and in the phase 2 PACE trial (449 heavily pretreated patients) 70% of the 64 patients with T315I achieved a major cytogenetic response and 56% a major molecular response. The price is vascular toxicity: arterial occlusive events reached 31% of chronic-phase patients at five years, and the label carries a boxed warning for arterial occlusion, venous thromboembolism, heart failure and hepatotoxicity. Asciminib, which binds the myristoyl pocket instead of the ATP site, is the newer alternative: at 200 mg twice daily in T315I chronic-phase CML, 48.9% of patients achieved a major molecular response at two years (68.4% of ponatinib-naive patients, 34.6% of ponatinib-pretreated).

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen on the T315I mutant structure will rank ponatinib above imatinib and above the other ABL1 ligands, in the same direction as the measured potencies — and, crucially, imatinib will score clearly worse on the mutant than on wild type, because that is what resistance means. The test is the negative control: a screen that cannot see imatinib's failure on T315I cannot be trusted to rank anything else on this target. The reference drug must itself dock, or the comparison is void.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-14 (web search; PubMed; the daily digest of 2026-11-14, which screened 722 candidates and selected 8, none on CML — the digest's relevance is methodological, not topical, for this paper). Key sources: Cortes et al. 2013 (PACE trial, NEJM) and Cortes et al. 2018 (final five-year PACE results, Blood) for ponatinib efficacy and vascular toxicity; O'Hare et al. 2009 for the ponatinib IC50 values; Zhou et al. 2011 for the 3OXZ and 3OY3 structures; Choi et al. 2010 for the GNF-7 type-II series; Dietrich et al. 2010 for the DFG-out hybrid ureas; Cortes et al. 2024 for asciminib in T315I; and the 2025 AFIP Pakistan cohort for the local mutation spectrum. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Pipeline, the mouse-target correction, and the structure choice

The standard LeadForge pipeline was run with target "BCR-ABL1 T315I" and reference drug ponatinib (run_docking.py, RDKit venv, NO_PROXY prefix). The pipeline retrieved 37 known ligands from ChEMBL target CHEMBL3099, verified ponatinib in PubChem (CID 24826799), screened 25 analogues by Morgan-fingerprint similarity, and ranked 26 leads by the standard composite score (similarity, Lipinski, Veber, PAINS, Tox21 read-across). Two corrections are recorded here rather than hidden.

First, the pipeline resolved the target to UniProt P00520 — **murine** Abl1 — and to ChEMBL CHEMBL3099, annotated *Mus musculus*. The human target is ABL1 (P00519). This is not a pipeline error to hide: the entire crystallographic literature for ABL1 T315I is built on the murine Abl1 kinase-domain construct (residues 229–511), because that is what crystallised. Both structures used here are murine constructs, and the gatekeeper numbering (Thr315) is identical. The measured potencies quoted in this paper are ChEMBL-reported ABL1 values under that murine target, and the paper says so wherever they appear.

Second, the pipeline's automatic structure pick (best resolution with a drug-like ligand) chose 3KFA, a **wild-type** Abl1 structure (1.22 angstrom, vinyl-purine inhibitor B91). A wild-type structure cannot test a gatekeeper-mutant question, so the T315I docking was re-run on 3OY3 — the T315I mutant kinase domain in complex with the ponatinib analogue AP24589, 1.95 angstrom (Zhou et al. 2011) — and ponatinib was re-docked on its own wild-type co-crystal structure 3OXZ (2.2 angstrom) as the protocol control, with imatinib cross-docked into the same 3OXZ pocket to complete the matched wild-type/mutant pair. The 3KFA scores are kept as a second wild-type control, which turns out to matter: the choice of wild-type structure moves ponatinib's score by 2.79 kcal/mol (Section 3.4).

### 2.3 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; one box (22.5 angstrom) and exhaustiveness 8 for every compound. Three structures, all murine Abl1 kinase domain (residues 229–511):

- **3KFA**, wild type, 1.22 angstrom, with the vinyl-purine dual Src-Abl inhibitor B91. Centre [16.72, −8.41, 15.16] — the centroid of B91 computed by the pipeline's `_ligand_center`.
- **3OXZ**, wild type, 2.2 angstrom, with ponatinib (0LI). Centre [15.33, −7.55, 16.58] — the centroid of co-crystallised ponatinib; the re-dock control.
- **3OY3**, T315I mutant, 1.95 angstrom, with the ponatinib analogue AP24589 (XY3). Centre [15.64, 7.23, 3.76] — the centroid of the chain-A AP24589, computed with `_ligand_center`; the Ile315 CA is 8.89 angstrom from the centre, confirming the box sits on the ATP site. The chain-B ligand copy was not used.

Best of three poses reported per compound. Five compounds on 3KFA and 3OY3: ponatinib (reference drug, PubChem CID 24826799), imatinib (CHEMBL941, approved 2001), CHEMBL459850 (a 3,4-dihydropyrimido[4,5-d]pyrimidin-2(1H)-one from the T315I-active type-II series of Choi et al. 2010, whose exemplar GNF-7 inhibited wild-type and T315I Bcr-Abl in biochemical and cellular assays and showed in-vivo efficacy in a T315I xenograft), and CHEMBL1213975 and CHEMBL1213976 (diaryl-urea DFG-out hybrids built from Gleevec/Nexavar/BIRB-796 fragments, Dietrich et al. 2010). Ponatinib was docked twice on 3OY3 in independent Vina runs (−14.36 and −14.29, delta 0.07); the −14.36 run is tabulated. One control was attempted and discarded: an AP24589 re-dock on 3OY3 was abandoned because PubChem has no AP24589 record under that name and the SMILES extracted from the deposited coordinates by RDKit's MolFromPDBBlock was mangled (the ethynyl linker and imidazole were lost); the −9.10 value it produced is not reported anywhere in this paper.

### 2.4 PAINS screen

RDKit PAINS filter applied to every compound. All five are PAINS-clean. Ponatinib carries one Lipinski violation (molecular weight 532.57); the other four pass Lipinski and Veber outright.

### 2.5 Rank correlation

Spearman rank correlation was computed between the Vina scores and the measured ABL1 IC50 values for the five compounds (n = 5). The measured values are wild-type ABL1 IC50s from ChEMBL, except ponatinib, for which the T315I value (2.0 nM) is also known. A correlation on five points is reported as a descriptive check, not as a validated ranking — the paper's real test is the imatinib negative control (Section 3.2).

### 2.6 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol; any gap smaller than that is not a difference. No molecular dynamics or free-energy refinement was run. No compound was assayed. The structures are murine kinase domains, not human BCR-ABL1, and both mutant and wild-type structures are rigid snapshots in one (DFG-out) conformation.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured ABL1 IC50 | 3KFA (WT) | 3OXZ (WT, ponatinib pocket) | 3OY3 (T315I) | PAINS |
|---|---|---|---|---|---|
| Ponatinib (reference) | 0.37 nM (WT); 2.0 nM (T315I) | −11.54 (−11.54, −10.83, −10.67) | **−14.33** (−14.33, −10.48, −10.12) | **−14.36** (−14.36, −10.81, −10.50) | clean |
| CHEMBL1213976 | 244 nM | −9.42 (−9.42, −9.31, −8.87) | — | −9.81 (−9.81, −9.09, −8.77) | clean |
| CHEMBL459850 (GNF-7 series) | 243 nM | −9.92 (−9.92, −9.62, −8.78) | — | −9.78 (−9.78, −9.61, −9.23) | clean |
| Imatinib | 10.8 nM (WT); inactive on T315I | −9.57 (−9.57, −9.03, −8.99) | −10.41 (−10.41, −9.52, −9.49) | −9.60 (−9.60, −8.96, −8.90) | clean |
| CHEMBL1213975 | 572.4 nM | −9.84 (−9.84, −9.71, −8.98) | — | −9.29 (−9.29, −8.98, −8.66) | clean |

Scores in kcal/mol, best of three poses (all three poses in parentheses). Measured IC50s are ChEMBL-reported ABL1 values (target CHEMBL3099, murine Abl1) except ponatinib's, which are from O'Hare et al. 2009. "—" means not docked on that structure.

Ponatinib is the clear winner on every structure: 1.62 kcal/mol clear of the next compound on 3KFA, and 4.55 clear on 3OY3. The other four compounds sit within 0.63 kcal/mol of each other on T315I (−9.29 to −9.81) and within 0.50 on 3KFA (−9.42 to −9.92) — one noise band, no ranking among them.

### 3.2 The negative control fails: imatinib scores the same on mutant and wild type

This is the result the paper was designed to test, and it fails. Imatinib scores −9.57 on wild type (3KFA) and −9.60 on T315I (3OY3): a difference of 0.03 kcal/mol, zero. On the matched pair — the same pocket family, 3OXZ wild type versus 3OY3 mutant — it scores −10.41 versus −9.60, a gap of 0.81, inside Vina noise. The measured record says the opposite: imatinib inhibits wild-type ABL1 at 10.8 nM and is essentially inactive against T315I, which is why T315I patients cannot be treated with it. Rigid docking with a fixed box finds a pose for imatinib in the mutant pocket and scores it as if nothing changed. The gatekeeper mechanism — a lost hydrogen bond plus a steric clash — is invisible to this protocol. Any ranking this screen produces on T315I is therefore unvalidated against the one compound whose behaviour on the mutant is known with certainty.

### 3.3 Rank correlation: weak, and driven by one compound

Against the measured wild-type ABL1 IC50s (ponatinib 0.37 nM, imatinib 10.8 nM, CHEMBL459850 243 nM, CHEMBL1213976 244 nM, CHEMBL1213975 572.4 nM), Spearman rho is 0.5 on the wild-type structure 3KFA and 0.6 on the mutant structure 3OY3 (n = 5). Both values are carried entirely by ponatinib sitting first; remove ponatinib and the remaining four compounds are ranked by Vina in an order that has no relationship to their measured potencies — imatinib, the second most potent compound measured (10.8 nM), ranks fourth of five by Vina on both structures, tied with compounds 20–50 times weaker. The two near-tied potencies (243 vs 244 nM) make the swap between CHEMBL459850 and CHEMBL1213976 meaningless, but the imatinib mis-ranking is not a tie artefact: it is a 20-fold potency error. A correlation of 0.5–0.6 on five points, with the negative control failed, is not a validated ranking.

### 3.4 The structure matters more than the mutation

Ponatinib scores −11.54 on wild type 3KFA but −14.33 on wild type 3OXZ: the same drug, the same wild-type protein, a 2.79 kcal/mol difference from the choice of structure alone — larger than any mutation effect in this study (ponatinib WT→T315I: 0.03; imatinib WT→T315I: 0.81). The reason is visible in the poses: on 3OXZ and 3OY3 the best pose (−14.33, −14.36) sits 3.5–3.9 kcal/mol clear of the second pose (−10.48, −10.81), while on 3KFA the poses are tightly grouped. The 3OXZ/3OY3 pocket was crystallised around ponatinib-class ligands in the DFG-out conformation, and the scoring function rewards that fit heavily. The −14.3 values are therefore partly a pocket-shape effect, not a pure affinity signal — and the measured record agrees that the direction is right but the magnitude is overstated: ponatinib is 5-fold *less* potent on T315I than on wild type (0.37 → 2.0 nM), while docking scores them identical. Any paper that reports a single-structure docking score as a potency claim is reporting the structure it picked as much as the molecule it docked.

### 3.5 ADMET and safety panel

All five compounds pass Lipinski and Veber (ponatinib with one violation, MW 532.57, logP 4.46, TPSA 65.77); all are PAINS-clean. The Tox21 read-across panel flags nothing decisive: ponatinib's highest signals are SR-MMP 0.917 and SR-ARE 0.881 (kNN read-across, not measured). The safety story that matters for this target is not in the panel: ponatinib's arterial occlusive events (31% of chronic-phase patients at five years in PACE) are a clinical toxicity, not a property any ligand-based screen predicts. The GNF-7-series compound and the two hybrid ureas are research compounds with no approval, no human safety data, and no measured T315I potency in the public record beyond the series-level claims in their source papers.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say one thing with confidence: ponatinib binds the T315I pocket at least as well as it binds the wild-type pocket, in the same direction as its measured profile. It cannot say that imatinib fails on T315I, which is the best-established fact in this field — and because it cannot say that, it cannot rank the three research compounds either. Their scores (−9.29 to −9.92) are noise, and the most interesting of them — CHEMBL459850, from a series *published* as T315I-active in cells and in a mouse xenograft — scores −9.78, indistinguishable from imatinib's −9.60. A paper that reported "CHEMBL459850 is a T315I lead because it docks at −9.78" would be reporting the same number that the known-inactive drug gets.

### 4.2 The gatekeeper mechanism docking cannot see

T315I defeats imatinib through two effects Vina cannot model in a rigid receptor: the loss of a hydrogen bond to the threonine hydroxyl, and a steric clash with the isoleucine side chain that forces the drug out of its preferred pose. A fixed box and a rigid side chain let the docking algorithm find an alternative pose that avoids the clash and then score it as if the clash did not exist. The correct computational test of gatekeeper resistance is not a single rigid dock: it is a free-energy comparison (e.g. MM-GBSA or alchemical free-energy perturbation) that prices the lost hydrogen bond and the clash, or a flexible-side-chain dock that lets Ile315 move. Neither was run here, and the paper does not pretend otherwise. The honest conclusion is that standard rigid docking is the wrong tool for gatekeeper mutations, and this paper is the control experiment that shows it.

### 4.3 Ponatinib's safety price, and the asciminib alternative

Even where docking validates ponatinib, the clinical question is not potency but price. Ponatinib works in T315I — 70% major cytogenetic response in the PACE T315I subgroup — but a third of chronic-phase patients develop arterial occlusive events by five years, and dose reductions (from 45 mg to 15 mg) are the standard mitigation. Asciminib attacks the same kinase from the myristoyl pocket, where the gatekeeper is irrelevant: at 200 mg twice daily, 48.9% of T315I patients achieved a major molecular response at two years, with a different toxicity profile (lipase elevation 18.8% grade ≥3, thrombocytopenia 14.6%). For a Pakistani patient, the practical question is access: in the AFIP cohort, 2 of 133 resistant patients were on ponatinib and 1 on asciminib. A docking paper cannot fix access, but it can stop pretending that a better docking score is the bottleneck — the bottleneck is the drug reaching the patient.

### 4.4 Testable hypotheses

1. **Negative-control hypothesis.** In one kinase assay on wild-type and T315I ABL1, imatinib's IC50 weakens by more than 100-fold on the mutant while ponatinib's weakens by less than 10-fold. Falsified if imatinib's T315I IC50 is within 10-fold of its wild-type value — in which case the published resistance is an artefact, which no one expects.
2. **GNF-7-series hypothesis.** CHEMBL459850 inhibits T315I ABL1 in a kinase assay at an IC50 within 10-fold of ponatinib's 2.0 nM. Falsified if it is more than 10-fold weaker — in which case its docking score (−9.78) is noise, as this paper suspects.
3. **Structure-choice hypothesis.** Ponatinib's docking score on a third wild-type ABL1 structure (neither 3KFA nor 3OXZ) falls outside the −11.54 to −14.33 range. Falsified if it lands inside it — in which case the 2.79 kcal/mol pocket effect is specific to this pair, not a general property of structure choice.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain ponatinib, imatinib, CHEMBL459850 and asciminib (as the myristoyl-pocket control); confirm identity and purity by LC-MS and NMR. Stage 2 (weeks 3–6): kinase assay (ADP-Glo or equivalent) on recombinant wild-type and T315I ABL1, all four compounds on the same plates, in triplicate — the single-assay comparison this paper could not make, and the direct test of hypothesis 1. Stage 3 (weeks 7–10): Ba/F3 cellular assay on Bcr-Abl wild-type and T315I lines, plus a wild-type ABL1 counter-screen for selectivity. Stage 4 (weeks 11–12): if CHEMBL459850 is within 10-fold of ponatinib on T315I, dock its analogues and synthesise the best two; if it is not, report the negative result and stop. Sample-size logic: three independent biological replicates per IC50 determination is the minimum for a defensible potency claim; the imatinib wild-type-versus-mutant comparison needs the same, because a false "resistant" call on the control is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. All structures are murine Abl1 kinase domains, not human BCR-ABL1; the gatekeeper numbering is identical, but the construct is not the fusion protein.
3. Rigid-receptor docking cannot model the hydrogen-bond loss and steric clash that define T315I resistance; the imatinib negative control fails, and the paper reports that failure rather than hiding it.
4. Vina noise is ±1–2 kcal/mol; four of the five compounds sit inside one noise band on both structures.
5. The choice of wild-type structure moves ponatinib's score by 2.79 kcal/mol — more than the mutation does — so absolute scores are not comparable across structures.
6. The re-dock control is ponatinib on its own structure (3OXZ); a competent protocol is expected to recover a good score there, so −14.33 validates the protocol, not a lead.
7. Only ponatinib carries a measured T315I potency; the three research compounds carry only wild-type ABL1 IC50s, so the T315I rank correlation cannot be computed against T315I measurements.
8. Spearman rho is computed on five points and is driven by ponatinib; it is a descriptive check, not a validated ranking.
9. The AP24589 re-dock on 3OY3 was attempted and discarded (no PubChem record; PDB-derived SMILES unreliable); no co-crystallised-ligand re-dock exists for the mutant structure.
10. No molecular dynamics, flexible-side-chain docking, or free-energy refinement was run — the methods that could actually price gatekeeper resistance.
11. The Tox21 panel is kNN read-across, not measured toxicity; ponatinib's real safety liability (arterial occlusion) is clinical and invisible to this screen.

## 6. Conclusion

On the T315I mutant structure 3OY3, ponatinib scores −14.36 kcal/mol — the same as its −14.33 re-dock on its own wild-type structure 3OXZ — matching its measured sub-nanomolar potency on both forms and validating its pan-BCR-ABL profile. But imatinib scores −10.41 on wild type and −9.60 on T315I, a gap inside Vina noise, although its measured potency collapses from 10.8 nM to essentially inactive: rigid docking cannot see the gatekeeper resistance it was asked to detect. The three research compounds cluster at −9.29 to −9.92 on both structures, inside noise, and the choice of wild-type structure alone moves ponatinib's score by 2.79 kcal/mol. The screen is a validated positive control with a failed negative control — useful for confirming ponatinib, useless for ranking anything else on T315I. The next step is the single-assay kinase comparison in Section 4.5, with ponatinib, imatinib, the GNF-7-series compound and asciminib on wild-type and T315I ABL1 on the same plates.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Cortes JE, Kim DW, Pinilla-Ibarz J, et al. A phase 2 trial of ponatinib in Philadelphia chromosome-positive leukemias. N Engl J Med. 2013;369(19):1783–1796. PMID: 24180494. doi:10.1056/NEJMoa1306494.
2. Cortes JE, Kim DW, Pinilla-Ibarz J, et al. Ponatinib efficacy and safety in Philadelphia chromosome-positive leukemia: final 5-year results of the phase 2 PACE trial. Blood. 2018;132(4):393–404. PMID: 29567798. doi:10.1182/blood-2016-09-739086.
3. O'Hare T, Shakespeare WC, Zhu X, et al. AP24534, a pan-BCR-ABL inhibitor for chronic myeloid leukemia, potently inhibits the T315I mutant and overcomes mutation-based resistance. Cancer Cell. 2009;16(5):401–412. PMID: 19878872.
4. Zhou T, Commodore L, Huang WS, et al. Structural mechanism of the pan-BCR-ABL inhibitor ponatinib (AP24534): lessons for overcoming kinase inhibitor resistance. Chem Biol Drug Des. 2011;77:1–11. PMID: 21118377. doi:10.1111/j.1747-0285.2010.01054.x.
5. Choi HG, Ren P, Adrian F, et al. A type-II kinase inhibitor capable of inhibiting the T315I "gatekeeper" mutant of Bcr-Abl. J Med Chem. 2010;53(15):5439–5448. PMID: 20604564. doi:10.1021/jm901808w.
6. Dietrich J, Hulme C, Hurley LH. The design, synthesis, and evaluation of 8 hybrid DFG-out allosteric kinase inhibitors: a structural analysis of the binding interactions of Gleevec, Nexavar, and BIRB-796. Bioorg Med Chem. 2010;18(15):5738–5748. PMID: 20621496. doi:10.1016/j.bmc.2010.05.063.
7. Cortes JE, et al. Asciminib monotherapy in patients with chronic-phase chronic myeloid leukemia with the T315I mutation after ≥1 prior tyrosine kinase inhibitor: 2-year follow-up results. Leukemia. 2024;38(7):1522–1533. doi:10.1038/s41375-024-02278-8.
8. Decoding BCR::ABL1 kinase domain mutations in chronic myeloid leukemia: implications for tyrosine kinase inhibitor resistance in a South Asian population. Hematol Transfus Cell Ther. 2026 (published 28 June 2026; Armed Forces Institute of Pathology, Pakistan cohort, Jan–Jun 2025). Accessed 2026-11-14. https://new.scielo.br/j/htct/a/4TwvwMjQ5Cr9f94rtfGDLHP/
9. Pierro F, Stella S, Fazio M, et al. Chronic myeloid leukemia and the T315I BCR::ABL1 mutation. Int J Mol Sci. 2025;26(23):11285. doi:10.3390/ijms262311285.
10. T315I — a gatekeeper point mutation and its impact on the prognosis of chronic myeloid leukemia. 2024. doi:10.1515/almed-2024-0069. PMCID: PMC11661532.
11. UniProtKB. Tyrosine-protein kinase ABL1, mouse, P00520; human, P00519. Accessed 2026-11-14. https://www.uniprot.org/uniprotkb/P00520/entry
12. RCSB Protein Data Bank. Structures 3KFA (wild-type Abl1, 1.22 A), 3OXZ (wild-type Abl1 with ponatinib, 2.2 A), 3OY3 (Abl1 T315I with AP24589, 1.95 A). Accessed 2026-11-14. https://www.rcsb.org/structure/3OY3
13. ChEMBL. Target CHEMBL3099 (tyrosine-protein kinase ABL1, Mus musculus); molecules CHEMBL941 (imatinib), CHEMBL459850, CHEMBL1213975, CHEMBL1213976 with ABL1 IC50 values. Accessed 2026-11-14. https://www.ebi.ac.uk/chembl/
14. PubChem. Ponatinib, CID 24826799. Accessed 2026-11-14. https://pubchem.ncbi.nlm.nih.gov/compound/24826799

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-032-2026-11-14.json` (pipeline + wild-type 3KFA docking), `hidden_files/dock-HP-032-2026-11-14-T315I.json` (corrected T315I docking on 3OY3), `hidden_files/dock-HP-032-2026-11-14-3OXZ-redock.json` (ponatinib re-dock on 3OXZ) and `hidden_files/dock-HP-032-2026-11-14-3OXZ-imatinib.json` (imatinib cross-dock on 3OXZ); run logs are alongside them. The correction script is `health-papers-agent/dock_t315i_correction.py`. The discarded AP24589 re-dock attempt is documented in Methods 2.3; its value is not reported. UniProt accessions P00520/P00519, PDB IDs 3KFA/3OXZ/3OY3, ChEMBL IDs and the PubChem CID are given in the text. No additional data were generated.
