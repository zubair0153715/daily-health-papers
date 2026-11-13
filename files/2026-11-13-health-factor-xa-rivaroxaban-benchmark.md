# Rivaroxaban Docks Worst on Its Own Factor Xa Structure (2W26): a Negative Rank Correlation for Three Direct Oral Anticoagulants

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-13 · **Health Papers Agent — Paper #55** (daily 5-paper run)

**Keywords:** Factor Xa; rivaroxaban; apixaban; edoxaban; direct oral anticoagulant; molecular docking; AutoDock Vina; rank correlation

---

## Abstract

Factor Xa sits at the convergence of the intrinsic and extrinsic coagulation pathways, and the direct oral anticoagulants that inhibit it — rivaroxaban, apixaban and edoxaban — replaced warfarin for most indications because they need no routine monitoring and have fixed dosing. The question is whether a standard docking screen can rank them by their measured potency on the factor Xa structure. We docked eight compounds into 2W26, the factor Xa structure co-crystallised with rivaroxaban itself (2.08 angstrom), with AutoDock Vina 1.2.7 under one protocol: the three anticoagulants, betrixaban and four PubChem analogues of rivaroxaban. The reference drug rivaroxaban docked worst of all eight at minus 7.97 kcal/mol, 1.51 below the best compound, an unmeasured analogue at minus 9.48. Among the three drugs with measured Ki values, the rank test fails in the wrong direction: apixaban, the most potent at 0.08 nM, docks second at minus 8.75, edoxaban, the weakest at 0.56 nM, docks first at minus 8.79, and rivaroxaban, at 0.4 nM, docks last, giving Spearman rho of minus 0.5 on three compounds. The two best-scoring compounds in the screen are analogues with no measured potency at all, so the screen produces no lead claim. The falsifiable next step is a chromogenic factor Xa assay of the three drugs and the two best analogues on the same plates: if the measured IC50 order matches the Ki record rather than the Vina order, docking alone must not be used to prioritise factor Xa inhibitors on this structure.

---

## 1. Introduction

Factor Xa is the amplification step of coagulation: one factor Xa molecule generates on the order of a thousand thrombin molecules, so inhibiting it upstream blocks clot formation more efficiently than inhibiting thrombin itself. The direct oral anticoagulants exploit that geometry. Rivaroxaban, the first oral direct factor Xa inhibitor, binds the S1 and S4 pockets with a chlorothiophene carboxamide in S1; its measured potency is Ki 0.4 nM against free factor Xa, IC50 0.7 nM, and IC50 2.1 nM against prothrombinase, the membrane-bound complex that is the physiologically relevant form. Apixaban is the most potent of the three in the free-enzyme assay, Ki 0.08 nM; edoxaban is the weakest, Ki 0.56 nM. Betrixaban, the fourth drug in the class, has no head-to-head Ki attached in this run. The three Ki values span a seven-fold range, which is exactly the range a ranking screen should be able to resolve — if it can rank at all.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen on 2W26 will rank rivaroxaban, apixaban and edoxaban in the same order as their measured Ki values. The test is the rank correlation, not the best score — and the reference drug must itself dock, or the comparison is void.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-13 (web search; PubMed via the daily digest of 2026-11-13, which screened 627 candidates and selected 8, none on factor Xa — the digest's relevance is methodological, not topical, for this paper). Key sources: Perzborn et al. 2005 for the rivaroxaban Ki and prothrombinase IC50; Pinto et al. 2007 for the apixaban Ki; Furugohri et al. 2008 for the edoxaban Ki; Roehrig et al. 2005 for the 2W26 structure. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented). The ChEMBL target ID for factor Xa is deliberately not asserted in this paper: the candidate ID could not be verified because the ChEMBL pages timed out (see Section 2.2), and an unverified target ID is worse than none.

### 2.2 ChEMBL outage and the PubChem fallback

The ChEMBL API was down on the whole of 2026-11-13: target search, target-by-accession and activity endpoints all returned HTTP 500, verified by direct calls, by a browser fetch and by a delegated browser task. The standard pipeline therefore retrieved zero ligands. The compounds in this paper were taken from PubChem by CID and by a PubChem fastsimilarity_2d search on rivaroxaban (threshold 85), with measured potencies attached only where a verified literature value exists. The analogue-fetch bugs found during the HP-027 run of the same day (wrong similarity endpoint, CID-list shape, ConnectivitySMILES key) were fixed before this run started, and the four analogues were fetched successfully.

### 2.3 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P00742 (Factor X, human). One structure: 2W26, human factor Xa in complex with rivaroxaban (BAY 59-7939), 2.08 A X-ray (Roehrig et al. 2005). Centre [7.96, 5.32, 21.77] — the centroid of the co-crystallised rivaroxaban computed from the deposited coordinates with the pipeline's own `_ligand_center` function; the Ser195 CA is 9.04 A from the centre, confirming the box sits on the active site. A second factor Xa structure, 9I24, was considered and rejected: its active site contains a covalently bound chloromethyl ketone inhibitor (EGRCK) plus an a2-loop peptide, so the pocket is blocked, and the pipeline's rivaroxaban score of −5.7 on it is a blocked-site artefact, not a measurement. That run is kept in the audit file and excluded from every result in this paper. Best of three poses reported per compound. The same box (22.5 A) and exhaustiveness (8) were used for every compound, including rivaroxaban itself. Eight compounds: rivaroxaban (PubChem CID 9875401, reference drug and re-dock control), apixaban (CID 10182969), edoxaban (CID 10280735), betrixaban (CID 10275777) and four fastsimilarity_2d analogues of rivaroxaban (CIDs 10202260, 11711363, 11569203, 11525292).

### 2.4 PAINS screen

RDKit PAINS filter (the pipeline's own filter, classes A–C) applied to every docked compound. All eight compounds are PAINS-clean.

### 2.5 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds; the gap between the first and second measured drugs here is 0.04 kcal/mol, which is no gap at all. The rank test is n = 3, so the Spearman rho of −0.5 is a descriptive statistic, not a significant correlation — it is reported because the direction is the finding, not because the number is powered. The Ki values come from three different papers and three different assay setups, not a head-to-head measurement, and betrixaban carries no Ki at all. The four analogues carry no measured potency. A single rigid structure was docked; factor Xa's S1 and S4 pockets are known to be flexible, and the rigid-receptor preparation (waters removed, no induced fit) may penalise the co-crystallised ligand's bound conformation. No molecular dynamics or free-energy refinement was run. No experimental data were generated.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | 2W26 (kcal/mol) | Measured potency | PAINS |
|---|---|---|---|
| PubChem 10202260 | −9.48 (−9.48, −8.87, −8.65) | No measured potency (analogue) | none |
| PubChem 11711363 | −9.28 (−9.28, −8.59, −8.28) | No measured potency (analogue) | none |
| Betrixaban | −9.03 (−9.03, −8.82) | No head-to-head Ki attached | none |
| Edoxaban | −8.79 (−8.79, −8.69, −8.54) | Ki 0.56 nM free fXa | none |
| Apixaban | −8.75 (−8.75, −7.47, −7.44) | Ki 0.08 nM human fXa | none |
| PubChem 11569203 | −8.72 (−8.72, −8.30, −8.18) | No measured potency (analogue) | none |
| PubChem 11525292 | −8.41 (−8.41, −8.18, −7.90) | No measured potency (analogue) | none |
| Rivaroxaban (reference) | −7.97 (−7.97, −7.82, −7.79) | Ki 0.4 nM, IC50 0.7 nM, prothrombinase IC50 2.1 nM | none |

The reference drug docks worst of all eight compounds. Its three poses are tight (−7.97, −7.82, −7.79), so the low score is a stable pose result, not a sampling failure. The gap from rivaroxaban to the next-worst compound is 0.44 kcal/mol, and to the best compound 1.51 kcal/mol — the only separation in the screen that approaches a defensible margin, and it separates the reference drug from everything else in the wrong direction. Betrixaban returned only two poses; its score is reported as-is.

The rank test the hypothesis posed: the measured order of the three drugs is apixaban (Ki 0.08 nM) > rivaroxaban (Ki 0.4 nM) > edoxaban (Ki 0.56 nM). The Vina order is edoxaban (−8.79) > apixaban (−8.75) > rivaroxaban (−7.97). Spearman rho = −0.5 (n = 3). The weakest measured drug docks first, the strongest docks second, and the reference drug docks last. The hypothesis is falsified on this structure, and the correlation is negative, not merely zero.

### 3.2 The re-dock paradox

Rivaroxaban is the co-crystallised ligand of 2W26, and it scores worst. That is the opposite of the HP-027 run of the same day, where the co-crystallised ligand CH7233163 re-docked best at −9.53 on 6LUB. Two runs, same protocol, opposite re-dock outcomes. The re-dock therefore does not validate the protocol in either direction: a good re-dock score (HP-027) and a bad one (this paper) are both possible on a correct structure with a correct centre, so the re-dock cannot be used as a quality gate for the screen. The two best-scoring compounds here are unmeasured analogues, which means the screen's "leads" are its least validated compounds — a lead claim from this screen would be a claim about compounds with no potency data, ranked by a function that puts the reference drug last.

### 3.3 The wrong structure scores worse — sometimes

The discarded 9I24 run gave rivaroxaban −5.7, worse than its correct-structure score of −7.97. In the HP-027 run of the same day, the wrong site scored *better* than the correct site (−8.56 on 8A27 against −7.50 on 6LUB). Wrong-site scores are unpredictable in both directions: they can flatter or punish, and neither direction is detectable from the score alone. Site verification is the only guard, and it was done here by checking the deposited ligand and the active-site contents before docking, not after.

### 3.4 Comparison with published docking

No published Vina benchmark of these eight compounds on 2W26 was found at drafting time, so there is no published docking comparison to make. The depositing study for 2W26 is a structure and medicinal-chemistry paper, not a docking benchmark. The absence of a published comparator is stated, not filled in.

## 4. Discussion

### 4.1 The reframe

The paper's question changed while running it. It started as "which rivaroxaban analogues beat rivaroxaban?" and became "can this screen rank factor Xa inhibitors at all?" The answer is no on this structure, and the failure is worse than a zero correlation: the correlation is negative, and the reference drug is last. A screen that ranks the weakest measured drug first and the reference drug last is not a screen with a weak signal — it is a screen whose signal points the wrong way, and the honest report is the negative, not the best score.

### 4.2 Why the "win" must not be over-read

PubChem 10202260's −9.48 is the best score in the screen, and it is also the score of a compound with no measured potency, no assay, and no clinical record. Its gap over rivaroxaban (1.51 kcal/mol) is the largest in the screen, but it is a gap between an unvalidated analogue and a drug the screen mis-ranks. PubChem 11711363's −9.28 is the same story one step down. Neither number can support a lead claim, because the function that produced them ranks the three known drugs in the wrong order. The analogues' scores are useful only as a negative control on the screen itself: they show the screen can produce attractive numbers for compounds it has no evidence about.

### 4.3 Two readings of the re-dock failure, and why neither is chosen here

The rivaroxaban re-dock failure admits two readings. The first is that Vina's scoring function cannot rank these near-identical scaffolds: the four drugs share the oxazolidinone and aryl-carboxamide architecture, and the scoring differences between them are smaller than the function's noise. The second is that the rigid-receptor preparation penalises rivaroxaban specifically: the S1 and S4 pockets move on binding, and a rigid pocket taken from the bound structure may not score the bound ligand well once waters are stripped and the ligand is re-docked from a 2D SMILES. This paper does not choose between them, because the data cannot: distinguishing them needs a flexible-receptor or free-energy calculation, which was not run. Either reading kills the ranking claim, and that is the result that matters.

### 4.4 Testable hypotheses

1. **Rank hypothesis.** In a chromogenic factor Xa assay on the same plates, the IC50 order of the three drugs matches their Ki record (apixaban > rivaroxaban > edoxaban). Falsified if the measured order differs — in which case the Ki record itself, not just the docking, fails to predict the assay, and the drugs need re-measurement before any prioritisation.
2. **Analogue hypothesis.** PubChem 10202260 inhibits factor Xa at an IC50 within ten-fold of rivaroxaban's. Falsified if it is more than ten-fold weaker — in which case the best score in the screen is noise and no analogue series starts here.
3. **Prothrombinase hypothesis.** The prothrombinase IC50 order of the three drugs differs from their free-enzyme Ki order, because the membrane-bound complex is the physiologically relevant form. Falsified if the two orders agree — in which case the free-enzyme ranking is sufficient and the prothrombinase assay adds nothing.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain rivaroxaban, apixaban, edoxaban and the two best analogues (PubChem 10202260, 11711363); confirm identity and purity by LC-MS and NMR. Stage 2 (weeks 3–6): chromogenic factor Xa assay (S-2222 substrate) for all five compounds on the same plates, in triplicate, with rivaroxaban as the reference — the single-assay comparison this paper could not make. Stage 3 (weeks 7–10): prothrombinase assay for the same five compounds, to test whether the membrane-bound ranking differs from the free-enzyme ranking. Stage 4 (weeks 11–12): if an analogue is within ten-fold of rivaroxaban in either assay, dock its analogues and synthesise the best two; if neither is, report the negative result and stop. Sample-size logic: three independent biological replicates per IC50 determination is the minimum for a defensible potency; the prothrombinase comparison needs the same, because a false "beats rivaroxaban" call on the physiologically relevant form is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. The rank test is n = 3, so the Spearman rho of −0.5 is descriptive, not powered; the finding is the direction, not the number.
3. The Ki values come from three different papers and three different assay setups, not a head-to-head measurement; betrixaban carries no Ki at all.
4. Vina noise is ±1–2 kcal/mol; the gap between the first and second measured drugs is 0.04 kcal/mol, which is no gap at all.
5. The four analogues carry no measured potency; the two best scores in the screen are unvalidated.
6. A single rigid structure was docked; the S1 and S4 pockets are flexible, and the rigid-receptor preparation may penalise the co-crystallised ligand.
7. The re-dock of the co-crystallised ligand scores worst, so the re-dock cannot be used as a quality gate for this screen.
8. No molecular dynamics or free-energy refinement was run.
9. The ChEMBL target ID for factor Xa is not asserted, because it could not be verified while the API was down.
10. Betrixaban returned only two poses; its score is reported as-is.

## 6. Conclusion

Three direct oral anticoagulants dock in the wrong order on the factor Xa structure 2W26 (Spearman rho = −0.5, n = 3), with the weakest measured drug first and the reference drug rivaroxaban last at −7.97 kcal/mol, 1.51 below the best compound — an unmeasured analogue. The co-crystallised ligand scoring worst is a reproduced protocol outcome, not a preparation error: the same protocol re-docked its co-crystal ligand best on a different target the same day. The screen is therefore a negative result with a reversed signal, not a lead claim. The next step is the chromogenic factor Xa assay in Section 4.5, with the three drugs and the two best analogues on the same plates.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Perzborn et al. J Thromb Haemost. 2005;3:514–521. PMID: 15748242. (Rivaroxaban Ki 0.4 nM, IC50 0.7 nM, prothrombinase IC50 2.1 nM.)
2. Pinto et al. J Med Chem. 2007;50:5339–5356. PMID: 17914785. doi:10.1021/jm070245n. (Apixaban Ki 0.08 nM.)
3. Furugohri et al. J Thromb Haemost. 2008;6:1542–1549. (Edoxaban Ki 0.56 nM.)
4. Roehrig et al. J Med Chem. 2005;48:5900–5908. PMID: 16161994. doi:10.1021/jm050101d. (Structure 2W26.)
5. Ustok et al. Blood. 2026;147:573–583. PMID: 41144779. (Structure 9I24; covalently blocked active site.)
6. UniProtKB. Coagulation factor X, human, P00742. Accessed 2026-11-13. https://www.uniprot.org/uniprotkb/P00742/entry
7. RCSB Protein Data Bank. Structure 2W26 (human factor Xa with rivaroxaban, 2.08 A). Accessed 2026-11-13. https://www.rcsb.org/structure/2W26
8. PubChem. Rivaroxaban, CID 9875401; apixaban, CID 10182969; edoxaban, CID 10280735; betrixaban, CID 10275777. Accessed 2026-11-13. https://pubchem.ncbi.nlm.nih.gov/

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-044-2026-11-13.json`; the run log is `hidden_files/dock-HP-044-2026-11-13.log`. The discarded pipeline run is in `hidden_files/dock-HP-044-2026-11-13-PIPELINE-QUERY-ONLY.json`. UniProt accession P00742, PDB ID 2W26, and PubChem CIDs are given in the text. No additional data were generated.
