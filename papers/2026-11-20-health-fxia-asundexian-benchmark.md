# Asundexian Re-Docks at −9.05 kcal/mol on the Milvexian-Bound Factor XIa Structure — but the First Approved FXIa Inhibitor Still Leaves the Decisive Question Open

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-20 · **Health Papers Agent — Paper #85** (daily 5-paper run)

**Keywords:** Factor XIa; asundexian; milvexian; anticoagulation; stroke prevention; molecular docking; ChEMBL; factor XI deficiency

---

## Abstract

Stroke killed 6.8 million people in 2023, yet every anticoagulant that prevents it also causes the bleeding it is meant to avoid — and the first drug designed to break that trade-off has just split its own evidence in two. Asundexian, an oral factor XIa (FXIa) inhibitor, failed its atrial-fibrillation trial (OCEANIC-AF: stroke or systemic embolism 1.3% vs 0.4% on apixaban, hazard ratio 3.79) but succeeded as add-on therapy after noncardioembolic stroke (OCEANIC-STROKE: ischaemic stroke 6.2% vs 8.4%, hazard ratio 0.74, no increase in major bleeding) and was approved by the US FDA on 9 November 2026 — the first FXIa inhibitor approved anywhere. We asked whether asundexian and its closest chemical analogues bind the true FXIa active site more strongly than the co-crystallised inhibitor milvexian. Using the LeadForge pipeline (UniProtKB P03951 → ChEMBL CHEMBL2820 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked asundexian, four PubChem analogues and milvexian on the 0.92 Å FXIa structure 7MBO, centred exactly on the co-crystallised milvexian (centre audit 0.00 Å). Asundexian re-docked at −9.05 kcal/mol with tight pose consistency (−9.05, −9.04, −8.89), no PAINS alert, and one Lipinski violation (molecular weight 593). Two of four PubChem analogues out-scored it on best pose — 135205642 at −10.03 and 135205940 at −9.88 — but both margins (0.98 and 0.83 kcal/mol) lie inside Vina's ±1–2 kcal/mol noise, and the first is a single-pose outlier whose other poses (−8.99, −8.89) tie or trail asundexian; the other two scored −9.19 and −8.99. The decisive check is the self-dock control: milvexian, the co-crystallised ligand of this structure and the more potent drug by measured Ki (0.11 nM vs 0.26 nM), re-docked worst at −7.83 kcal/mol — 1.22 kcal/mol behind asundexian. Docking therefore ranks this scaffold family inversely to measured potency, and no analogue can be claimed to beat asundexian on this evidence. The honest limit: ChEMBL's activity endpoint returned HTTP 500 all day, so the analogues carry no measured potency and the comparison is structural, not pharmacological; no laboratory data exist for any compound in this study. The claim that any analogue beats asundexian would be refuted if a chromogenic FXIa enzyme assay shows a Ki worse than asundexian's 0.26 nM. The falsifiable next step is an 8–12-week enzyme-plus-aPTT test of the two best-scoring analogues against asundexian and milvexian.

---

## 1. Introduction

In 2023 there were 13.2 million new strokes worldwide, 6.8 million stroke deaths, and 104.8 million people living after a stroke, accounting for 156.5 million disability-adjusted life-years; stroke was the second leading cause of death and the third leading cause of death and disability combined, and more than 80% of the deaths and disability occurred in low- and middle-income countries. Ischaemic stroke accounted for 63.9% of incident cases. In Pakistan, where stroke care is concentrated in a few tertiary centres and rehabilitation is scarce, a prevented stroke is worth far more than a treated one — and prevention is where anticoagulation fails its own patients: the drugs that stop clots cause the bleeding that kills or disables, so the most vulnerable patients are the ones left unprotected.

Factor XI sits at the hinge of that dilemma. It is a serine protease of the intrinsic (contact) pathway that amplifies thrombin generation once a clot has started, but it contributes little to the initial haemostatic plug, which is driven by the extrinsic tissue-factor pathway. The human genetics agree: people born without factor XI (factor XI deficiency, formerly haemophilia C) usually have a mild, variable bleeding disorder — prolonged bleeding after trauma or surgery, mostly at mucosal surfaces — and many never bleed at all; severe deficiency affects about 1 in 1 million people worldwide and about 1 in 450 Ashkenazi Jews. A drug that inhibits FXIa should therefore, in theory, uncouple antithrombotic efficacy from bleeding risk. That theory has now been tested in 27,000 randomised patients, and the answer depends on the indication.

Asundexian (BAY 2433334, Sunharbo; Bayer) is an oral, direct, reversible FXIa inhibitor from a substituted-oxopyridine series, with a human FXIa Ki of 0.26 nM and >38,000-fold selectivity over factor Xa and thrombin (nearest off-target plasma kallikrein, Ki 110 nM). In OCEANIC-AF, 14,810 high-risk atrial-fibrillation patients were randomised to asundexian 50 mg once daily or standard-dose apixaban; the trial was stopped early because asundexian was inferior for stroke or systemic embolism (1.3% vs 0.4%; hazard ratio 3.79, 95% CI 2.46–5.83) even though major bleeding was lower (0.2% vs 0.7%; hazard ratio 0.32). In OCEANIC-STROKE, 12,327 patients within 72 hours of a noncardioembolic ischaemic stroke or high-risk transient ischaemic attack were randomised to the same 50 mg dose or placebo, added to planned single or dual antiplatelet therapy; ischaemic stroke fell from 8.4% to 6.2% (cause-specific hazard ratio 0.74, 95% CI 0.65–0.84; P < 0.001) with no significant increase in major bleeding (1.9% vs 1.7%; hazard ratio 1.10). On 9 November 2026 the FDA approved asundexian with antiplatelet therapy to reduce stroke risk after a recent mild-to-moderate noncardioembolic ischaemic stroke or high-risk TIA — the first FXIa inhibitor approved in the United States, and the first new antithrombotic class for this population. The second drug in the class, milvexian (BMS-986177/JNJ-70033093; Ki 0.11 nM, >5,000-fold selective over related serine proteases except chymotrypsin and plasma kallikrein), has had the opposite split: its phase 3 LIBREXIA-ACS trial (14,194 patients after acute coronary syndrome) was stopped for futility in November 2025 with identical event rates (5.4% vs 5.1%; hazard ratio 1.05), while its stroke and atrial-fibrillation programmes continue.

The classical medical canon discussed this disease class long before the enzyme was known: Ibn Sina's Canon of Medicine (c. 1025) discusses al-saktah (apoplexy/stroke) as a sudden loss of movement and sensation, and the management it proposes is entirely supportive — the Canon knows the syndrome, not the target. These texts are hypothesis sources, not evidence, but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do asundexian and its closest PubChem analogues bind the true FXIa active site (PDB 7MBO) at scores beyond re-docked milvexian, the co-crystallised inhibitor, and would that binding translate into stronger FXIa inhibition? **Falsifier:** a chromogenic FXIa enzyme assay showing a Ki worse than asundexian's 0.26 nM, or an aPTT assay showing no advantage over asundexian, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the approved drug re-docked on a co-crystal structure of its own target, with the co-crystallised inhibitor re-docked as a second control — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-20: the OCEANIC-AF and OCEANIC-STROKE trial records (NEJM 2025 and 2026), the asundexian design paper (Roehrig et al., J Med Chem 2023), the milvexian discovery paper (Dilger et al., J Med Chem 2022), the LIBREXIA-ACS result (NEJM 2026), the GBD 1990–2023 stroke fact sheet, and the RCSB records for PDB 7MBO and 8BO3. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: human coagulation factor XI, UniProtKB P03951 (F11 gene; 625 residues; "Factor XI triggers the middle phase of the intrinsic pathway of blood coagulation by activating factor IX"); ChEMBL target CHEMBL2820 (Coagulation factor XI, SINGLE PROTEIN, Homo sapiens — verified live 2026-11-20). Structure: PDB 7MBO, the FXIa protease domain (Pichia pastoris expression; C500S mutation) in complex with milvexian, 0.92 Å X-ray resolution — the highest-resolution FXIa structure available. Grid centre: centroid of the co-crystallised milvexian (ligand YXG, 66 atoms), [−1.06, 9.92, −17.80], verified by direct computation from the PDB file and by the pipeline's own `dock._ligand_center` (0.00 Å agreement); box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for asundexian, all four analogues and milvexian. Note that 7MBO is the milvexian structure, not the asundexian structure (asundexian's own co-crystal is PDB 8BO3, 1.84 Å): asundexian's score here is therefore a cross-dock into the milvexian site, and milvexian's score is the self-dock control.

**A ChEMBL outage, stated plainly.** On 2026-11-20 the ChEMBL activity endpoint returned HTTP 500 for every target queried (verified directly against the EBI API; the target endpoint still worked). The pipeline's step 2 therefore retrieved zero bioactivities for CHEMBL2820, and the run contains no ChEMBL lead set. Rather than ship a one-compound paper, the comparison set was built from PubChem `fastsimilarity_2d` against asundexian (Tanimoto ≥ 0.85, 30 analogues returned; four picked for docking: the smallest, the closest-to-asundexian formula, the largest, and one N7 variant). This is the established fallback from the 2026-11-11 FLT3 run, with the same rule: **no measured potency is attached to any PubChem analogue**, and the paper's comparison is structural only. All four analogues come from the same Bayer oxopyridine series as asundexian (PubChem CIDs 13520xxxx), so the set tests scaffold variation, not chemotype diversity. The discarded thin pipeline run is preserved in `hidden_files/dock-HP-098-2026-11-20.json`; the re-dock is in `hidden_files/dock-HP-098-redock-2026-11-20.json`.

### 2.3 PAINS screen

RDKit PAINS filter applied to asundexian and the four analogues. Asundexian carries no PAINS alert. All four analogues are PAINS-clean (PubChem CIDs 135205642, 135205940, 135205866, 135205878), as is milvexian.

### 2.4 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for asundexian: molecular weight 592.94, logP 4.6, 2 hydrogen-bond donors, 6 acceptors, TPSA 134.13 Å², 8 rotatable bonds, 1 Lipinski violation (molecular weight > 500) with an overall Lipinski pass and Veber pass. ToxGuard Tox21 kNN read-across (12 assays) for asundexian: maximum predicted probability 0.38 (SR-MMP), with a maximum neighbour similarity of only 0.263 — a weak read-across, not a measurement, and it does not clear the compound for development. The four analogues share asundexian's profile: each carries exactly one Lipinski violation (molecular weight > 500) with a Veber pass — PubChem-135205642 (MW 545.36, logP 3.85, HBD 2, HBA 6, TPSA 134.13 Å², 7 rotatable bonds), PubChem-135205940 (MW 578.91, logP 4.21, HBD 2, HBA 6, TPSA 134.13 Å², 7 rotatable bonds), PubChem-135205866 (MW 588.97, logP 4.91, HBD 2, HBA 6, TPSA 134.13 Å², 10 rotatable bonds), PubChem-135205878 (MW 553.98, logP 3.76, HBD 2, HBA 7, TPSA 147.02 Å², 10 rotatable bonds). Milvexian is the least drug-like of the set by these counts (MW 626.46, logP 5.80, HBD 1, HBA 7, TPSA 125.41 Å², 4 rotatable bonds, two Lipinski violations) — and the most potent by measured Ki — which is itself a warning that these descriptor counts do not rank this class.

### 2.5 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for the four analogues against FXIa in this study, and no measured potency is attached to them. The two measured Ki values in this paper (asundexian 0.26 nM; milvexian 0.11 nM) are published enzyme-assay values, not new measurements.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured FXIa potency | Best affinity, 7MBO (kcal/mol) | Top-3 poses (kcal/mol) | Median pose | Margin vs asundexian |
|---|---|---|---|---|---|
| Asundexian (reference) | Ki 0.26 nM | −9.05 | −9.05, −9.04, −8.89 | −9.04 | — |
| PubChem-135205642 | none (PubChem analogue) | −10.03 | −10.03, −8.99, −8.89 | −8.99 | +0.98 (best pose only) |
| PubChem-135205940 | none (PubChem analogue) | −9.88 | −9.88, −9.33, −9.16 | −9.33 | +0.83 |
| PubChem-135205866 | none (PubChem analogue) | −9.19 | −9.19, −9.09, −8.66 | −9.09 | +0.14 |
| PubChem-135205878 | none (PubChem analogue) | −8.99 | −8.99, −8.73, −8.65 | −8.73 | −0.06 |
| Milvexian (co-crystallised ligand) | Ki 0.11 nM | −7.83 | −7.83, −7.46, −6.80 | −7.46 | −1.22 |

Two analogues out-score asundexian on best pose, but neither margin survives the noise test: 0.98 and 0.83 kcal/mol against Vina's ±1–2 kcal/mol, and PubChem-135205642's margin is a single pose — its median pose (−8.99) is actually worse than asundexian's median (−9.04). On medians, only PubChem-135205940 beats asundexian, by 0.29 kcal/mol. The control that settles the interpretation is milvexian: it is the ligand this structure was crystallised with, it is the more potent drug by measured Ki (0.11 nM vs 0.26 nM), and Vina scores it 1.22 kcal/mol *worse* than asundexian. A scoring function that ranks the weaker binder first and the stronger binder last, inside one scaffold family on one structure, cannot rank this family at all. The honest reading of the table is therefore a null result: no analogue beats asundexian beyond noise, and the method itself fails its own positive control.

Asundexian re-docked at −9.05 kcal/mol with tight pose consistency (top-3 spread 0.16 kcal/mol), which is the validated control that anchors the comparison: a method that could not recover strong binding for a 0.26 nM binder would be broken. It did.

### 3.2 Comparison with published docking

No published Vina study of asundexian or these four analogues on 7MBO was found in the sweep; the comparison here is internal (analogues vs re-docked reference drugs on the same structure, same protocol). The crystal structures themselves (7MBO for milvexian, 8BO3 for asundexian) are the published ground truth for the binding mode; this paper tests whether a rigid scoring function can rank compounds inside that mode.

### 3.3 The clinical confounder that docking cannot see

The OCEANIC split is the paper's most important context: the same drug, the same dose, the same target — inferior in atrial fibrillation, superior after noncardioembolic stroke. The docking order cannot explain that split, and it cannot even rank the drugs: milvexian, the more potent binder by measured Ki, re-docks worst. The split is about indication, background therapy and thrombus biology (fibrin-rich cardioembolic clot versus platelet-rich atherosclerotic clot under antiplatelet cover), not about binding affinity. A compound that out-scores asundexian here would still face the same indication question, and the OCEANIC-AF failure is a standing warning that FXIa potency does not guarantee efficacy where factor Xa inhibition already works.

## 4. Discussion

### 4.1 The reframe

The FDA approval of 9 November 2026 changes the question this paper can ask. Before it, the question was "can an FXIa inhibitor work at all?" — now it is "which chemotype, if any, beats the approved drug, and in which indication?" The docking benchmark is therefore a screen for successors, not for proof of concept, and its bar is higher: a new compound must beat asundexian on the target and then survive the indication test that asundexian itself failed in atrial fibrillation.

### 4.2 Why the "win" must not be over-read

Three reasons. First, every margin in §3.1 lies inside Vina's ±1–2 kcal/mol noise unless stated otherwise. Second, the four analogues carry no measured potency, so the ranking is a structural hypothesis with no pharmacological anchor — unlike the MDM2 and BCR-ABL papers in this series, where ChEMBL potencies disciplined the ranking. Third, all five compounds share the oxopyridine scaffold, so even a genuine docking advantage would be a variation on the approved chemotype, not a new one, and would inherit its developability profile (molecular weight near 600, logP 4.6, TPSA 134).

### 4.3 Mechanism

FXIa amplifies thrombin generation by activating factor IX; its inhibition prolongs the activated partial thromboplastin time (aPTT) without changing prothrombin time, which is the laboratory signature of intrinsic-pathway selectivity. Test for each link: (i) a chromogenic FXIa enzyme assay measures Ki directly against asundexian (0.26 nM) and milvexian (0.11 nM) as comparators; (ii) aPTT prolongation in human plasma measures functional anticoagulation; (iii) a plasma-kallikrein counter-screen (asundexian Ki 110 nM; milvexian Ki 44 nM) measures whether the analogue kept the selectivity that defines the class — loss of kallikrein selectivity is the likeliest way a "better" FXIa binder becomes a worse drug, because kallikrein inhibition drives bradykinin-mediated angioedema risk.

### 4.4 Testable hypotheses

1. The best-scoring analogue inhibits human FXIa with a Ki within 3-fold of asundexian's 0.26 nM in a chromogenic enzyme assay. Falsifier: Ki > 0.8 nM.
2. The same analogue prolongs aPTT in human plasma at least as strongly as asundexian at matched concentration. Falsifier: no aPTT prolongation below 1 µM.
3. The analogue keeps ≥100-fold selectivity over plasma kallikrein. Falsifier: kallikrein Ki within 10-fold of the FXIa Ki.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): chromogenic FXIa enzyme assay for the two candidate analogues — PubChem-135205940 (most consistent: median pose −9.33) and PubChem-135205642 (best single pose, −10.03) — plus asundexian and milvexian controls; readout Ki, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): aPTT and plasma-kallikrein counter-screen in human plasma for the same set. Stage 3 (weeks 9–12): if any analogue passes stages 1–2, solubility and plasma-protein-binding measurement; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin.
2. ChEMBL was down (HTTP 500) on the run date, so the comparison set is four PubChem similarity analogues with no measured potency; the ranking is structural, not pharmacological.
3. All five docked compounds share one scaffold (the Bayer oxopyridine series); no chemotype diversity was tested.
4. Asundexian's score is a cross-dock (7MBO is the milvexian structure); its own co-crystal is 8BO3 at 1.84 Å, which was not used.
5. A single rigid structure was used; the FXIa active site adapts to different chemotypes, so one structure under-samples the binding landscape.
6. The 7MBO structure carries the C500S mutation and is a Pichia-expressed protease domain, not full-length human FXI.
7. No data on the clinical confounder: docking cannot distinguish the atrial-fibrillation indication (where asundexian failed) from the post-stroke indication (where it succeeded).
8. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon; the full Arabic text was not read, and other classical works on stroke were not individually consulted.

## 6. Conclusion

Asundexian, the first FXIa inhibitor approved anywhere (FDA, 9 November 2026), re-docks at −9.05 kcal/mol on the 0.92 Å milvexian-bound FXIa structure 7MBO, with tight pose consistency and no PAINS alert — a validated control, not a discovery. No analogue beats it: the best best-pose margin (PubChem-135205642, +0.98 kcal/mol) is a single-pose outlier inside Vina noise, the most consistent analogue (PubChem-135205940, median −9.33) leads by only 0.29 kcal/mol on medians, and the method fails its own positive control — milvexian, the more potent drug by measured Ki, re-docks 1.22 kcal/mol worse than asundexian. The docking verdict is a null result, and it is useful precisely as one: this scaffold family cannot be ranked by rigid Vina scoring, and the next screen must be an enzyme assay, not a bigger docking set. What the docking cannot do is resolve the OCEANIC split: the same drug failed in atrial fibrillation and succeeded after stroke, and no binding score explains that. The next step is the cheap, decisive test — a chromogenic FXIa enzyme assay plus aPTT and kallikrein counter-screen for the best-scoring analogue against asundexian and milvexian — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Higher Education Commission research-funding panels, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of FXIa inhibition as an academic drug-discovery exercise, and whether to prepare DRAP's assessment pathway for a first-in-class anticoagulant that will arrive with a split indication record. **Exact change:** commission the 8–12-week enzyme-plus-aPTT screen proposed in §4.5 for the best-scoring analogue against asundexian and milvexian, instead of funding another purely computational screen of the same target; and, in parallel, ask DRAP's registration reviewers to note the OCEANIC split explicitly in any future asundexian dossier — approval for post-stroke secondary prevention is not evidence for atrial fibrillation, where the drug was inferior to apixaban. **If evidence Z appears, reverse this:** if the best analogue loses >3-fold to asundexian in the enzyme assay or loses kallikrein selectivity, drop this scaffold set and redirect the same screen to the next FXIa chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable anticoagulant from a useless one for a disease that kills 6.8 million people a year, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Sharma M, Dong Q, Hirano T, et al.; OCEANIC-STROKE Investigators. Asundexian for secondary stroke prevention. N Engl J Med. 2026;394(15):1467-1479. doi:10.1056/NEJMoa2513880.
2. Piccini JP, Patel MR, Steffel J, et al.; OCEANIC-AF Steering Committee and Investigators. Asundexian versus apixaban in patients with atrial fibrillation. N Engl J Med. 2025;392(1):23-32. doi:10.1056/NEJMoa2407105. PMID: 39225267.
3. Roehrig S, Ackerstaff J, Jimenez Nunez E, et al. Design and preclinical characterization program toward asundexian (BAY 2433334), an oral factor XIa inhibitor for the prevention and treatment of thromboembolic disorders. J Med Chem. 2023;66:12203-12224. doi:10.1021/acs.jmedchem.3c00795. PMID: 37669040.
4. Dilger AK, Pabbisetty KB, Corte JR, et al. Discovery of milvexian, a high-affinity, orally bioavailable inhibitor of factor XIa in clinical studies for antithrombotic therapy. J Med Chem. 2022;65:1770-1785. doi:10.1021/acs.jmedchem.1c00613. PMID: 34494428.
5. Wong PC, Crain EJ, Bozarth JM, et al. Milvexian, an orally bioavailable, small-molecule, reversible, direct inhibitor of factor XIa: in vitro studies and in vivo evaluation in experimental thrombosis in rabbits. J Thromb Haemost. 2022;20(2):399-408. doi:10.1111/jth.15588.
6. Gibson CM, Steg PG, Bahit MC, et al. Milvexian after a recent acute coronary syndrome (LIBREXIA-ACS). N Engl J Med. 2026 (published online 29 August 2026). doi:10.1056/NEJMoa2608717.
7. Feigin VL, et al. The latest Global Stroke Fact Sheet 1990–2023: Global Burden of Disease Study. Neuroepidemiology. 2026. doi:10.1159/000552065.
8. Asundexian receives FDA approval for secondary stroke prevention. HCPLive. 9 November 2026.
9. RCSB PDB entry 7MBO: Factor XIa (Pichia pastoris; C500S) in complex with milvexian, 0.92 Å. RCSB Protein Data Bank. Accessed 2026-11-20.
10. RCSB PDB entry 8BO3: Factor XI protease domain in complex with asundexian, 1.84 Å. RCSB Protein Data Bank. Accessed 2026-11-20.
11. ChEMBL target CHEMBL2820: Coagulation factor XI, Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-20 (activity endpoint returning HTTP 500 on this date).
12. MedlinePlus Genetics. Factor XI deficiency. US National Library of Medicine. Accessed 2026-11-20.
13. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; al-saktah, apoplexy/stroke.)
14. UniProtKB P03951: Coagulation factor XI, Homo sapiens. UniProt. Accessed 2026-11-20.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-098-2026-11-20.json` (pipeline run: asundexian re-dock on 7MBO) and `hidden_files/dock-HP-098-redock-2026-11-20.json` (four PubChem analogues + milvexian re-dock on 7MBO). Reference drug asundexian, PubChem CID 135206011; milvexian, PubChem CID 118277544; analogues PubChem CIDs 135205642, 135205940, 135205866, 135205878. Structure: PDB 7MBO (0.92 Å). Target: UniProtKB P03951; ChEMBL target CHEMBL2820. No additional data were generated.
