# Belzutifan Re-Docks at −10.94 kcal/mol on the Belzutifan-Bound HIF-2α Structure — but Two Analogues Lead by Less Than Vina Noise and the Least Potent Compound Docks Best

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-21 · **Health Papers Agent — Paper #90** (daily 5-paper run)

**Keywords:** HIF-2α; belzutifan; EPAS1; von Hippel-Lindau disease; clear-cell renal cell carcinoma; molecular docking; ChEMBL; PAS-B domain

---

## Abstract

Kidney cancer caused 434,840 new cases and 155,953 deaths worldwide in 2022, and most clear-cell renal cell carcinomas are driven by loss of the von Hippel-Lindau (VHL) tumour suppressor, which leaves hypoxia-inducible factor 2-alpha (HIF-2α) permanently switched on — yet only one drug, belzutifan, directly inhibits HIF-2α, and it works in only a minority of advanced cases. We asked whether any measured HIF-2α ligand binds the drug's own PAS-B pocket more strongly than belzutifan itself. Using the LeadForge pipeline (UniProtKB Q99814 → ChEMBL CHEMBL1744522 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked belzutifan and four ChEMBL analogues with measured potency on the 2.75 Å belzutifan-bound HIF-2α–ARNT structure 7W80, centred exactly on the co-crystallised belzutifan (centre audit via dock._ligand_center). Belzutifan re-docked at −10.94 kcal/mol, a strong self-dock control. Two analogues out-scored it on best pose — CHEMBL5723338 at −11.40 and CHEMBL4453227 at −11.22 — but both margins (0.46 and 0.28 kcal/mol) lie inside Vina's ±1–2 kcal/mol noise, and the ranking contradicts measured potency: the best-docking analogue is the least potent by assay (IC50 16.0 nM), while the most potent (EC50 4.0 nM) docks second and belzutifan itself (IC50 9.0 nM) docks last. On median pose the order scrambles again, with CHEMBL4173075 leading by 0.33 kcal/mol. Docking therefore cannot rank this scaffold series, and no analogue can be claimed to beat belzutifan on this evidence. The honest limit: the structure is the mouse heterodimer (no human belzutifan-bound HIF-2α structure exists), all five compounds share one scaffold, and no laboratory data exist for any compound in this study. The claim that any analogue beats belzutifan would be refuted if a TR-FRET HIF-2α–ARNT dimer-disruption assay shows a Ki worse than belzutifan's 20 nM. The falsifiable next step is an 8–12-week TR-FRET plus luciferase-reporter test of the two best-scoring analogues against belzutifan.

---

## 1. Introduction

In 2022 there were an estimated 434,840 new cases of kidney cancer and 155,953 deaths from it worldwide, and the burden is projected to rise to 745,791 new cases and 304,861 deaths by 2050. Clear-cell renal cell carcinoma (ccRCC) accounts for about 70% of renal cell carcinomas, and about 90% of sporadic ccRCCs carry inactivation of the VHL gene through mutation, deletion of chromosome 3p or promoter methylation. Under normal oxygen conditions the VHL protein targets the alpha subunits of hypoxia-inducible factor for proteasomal degradation; when VHL is lost, HIF-α — particularly HIF-2α — accumulates even in the presence of oxygen ("pseudohypoxia") and switches on genes driving angiogenesis, glucose uptake and proliferation. The same pathway drives von Hippel-Lindau disease, the rare hereditary syndrome in which a germline VHL pathogenic variant predisposes to ccRCC, central nervous system haemangioblastomas and pancreatic neuroendocrine tumours. In Pakistan, where cancer registration is incomplete and targeted therapy is largely paid for out of pocket, a drug that works in only a minority of patients is a drug most patients cannot reach twice — once for the price, once for the response rate.

Belzutifan (Welireg; PT2977/MK-6482, Merck, originally developed by Peloton Therapeutics) is the first drug that binds HIF-2α directly. It occupies a small hydrophobic cavity in the PAS-B domain of HIF-2α and allosterically destabilises the HIF-2α–ARNT heterodimer, mainly through the key residue M252 near the dimer interface, with a Ki of 20 nM for dimer disruption and an IC50 of 17 nM for inhibition of HIF-2α transcriptional activity. The US FDA approved it in August 2021 for VHL-associated renal cell carcinoma, central nervous system haemangioblastomas and pancreatic neuroendocrine tumours, on the LITESPARK-004 trial, in which the objective response rate in VHL-associated renal cell carcinoma was 49%. In December 2023 it was approved for advanced ccRCC after PD-1/PD-L1 and VEGFR-targeted therapy, on the phase 3 LITESPARK-005 trial, in which belzutifan produced an objective response rate of 22.7% versus 3.5% for everolimus and a progression-free survival hazard ratio of 0.75, with no overall-survival superiority. The drug therefore works — and works in fewer than one in four patients with advanced disease. Anaemia and hypoxia are the class-defining adverse effects, because HIF-2α also drives erythropoietin production.

The pipeline behind belzutifan is now moving. Casdatifan (AB521, Arcus Biosciences), a next-generation HIF-2α inhibitor, reported a monotherapy objective response rate of 33% with a disease control rate of 85% at 100 mg once daily (N=29) in the ARC-20 phase 1/2 trial (NCT05536141), and 46% in combination with cabozantinib; a phase 3 trial (PEAK-1, NCT07011719) is under way. NKT2152 (NiKang Therapeutics) reported an objective response rate of 20% among 100 efficacy-evaluable heavily pretreated patients, with median progression-free survival of 7.4 months (NCT05119335). DFF332 (Novartis) reported disease control of about 50% in heavily pretreated renal cell carcinoma. None of these is approved, and none has yet been shown to beat belzutifan head to head. The question this paper asks is narrower and cheaper than a trial: among compounds with measured HIF-2α potency already in ChEMBL, does any bind belzutifan's own pocket more strongly than belzutifan itself — and can docking even tell them apart?

The classical medical canon discussed kidney disease centuries before the VHL gene was known: Ibn Sina's Canon of Medicine (c. 1025) treats diseases of the kidney (amrad al-kulya), including swellings and obstructions, with entirely supportive management — the Canon knows the organ and the syndrome, not the target. These texts are hypothesis sources, not evidence, but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL ligands with measured HIF-2α potency bind the belzutifan pocket of the HIF-2α–ARNT structure (PDB 7W80) at scores beyond re-docked belzutifan, and would that binding translate into stronger HIF-2α inhibition? **Falsifier:** a TR-FRET HIF-2α–ARNT dimer-disruption assay showing a Ki worse than belzutifan's 20 nM, or a luciferase reporter assay showing an IC50 worse than belzutifan's 17 nM, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the approved drug re-docked on a co-crystal structure of its own target, with the co-crystallised ligand as the control — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-21: the belzutifan structural paper (Ren et al., Mol Pharmacol 2022), the LITESPARK-004 trial (Jonasch et al., N Engl J Med 2021), the LITESPARK-005 trial (Choueiri et al., N Engl J Med 2024), the FDA approval announcements (August 2021, December 2023), the GLOBOCAN 2022 kidney-cancer estimates, the RCSB records for PDB 7W80 and 7Q5V, and the ARC-20 and NKT2152 trial records (NCT05536141, NCT05119335). The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Target identification — two wrong turns, caught and corrected

This paper's most important methodological finding is that the pipeline resolved the target wrong twice before it resolved it right, and both errors would have produced a publishable-looking but false paper if they had not been audited.

**First wrong turn: the wrong protein.** The target name "Hypoxia-inducible factor 2-alpha" resolved to UniProtKB Q9NWT6 — which is HIF1AN, the asparaginyl hydroxylase also called FIH-1 (factor-inhibiting HIF-1), not HIF-2α. The ChEMBL target was CHEMBL5909, "Hypoxia-inducible factor 1-alpha inhibitor". The pipeline docked belzutifan analogues on a FIH structure (PDB 7A1Q) and returned scores (−5.73 for belzutifan) that describe binding to the wrong enzyme. That run is discarded in full and preserved only as an audit record.

**Second wrong turn: the wrong structure.** Re-running with the gene name "EPAS1" resolved correctly to UniProtKB Q99814 (endothelial PAS domain-containing protein 1, human HIF-2α) and ChEMBL target CHEMBL1744522, with 44 bioactivities retrieved. But the pipeline's PDB picker then chose 7Q5V — a 1.17 Å structure of PHD2/EGLN1 in complex with N-oxalylglycine and a 20-residue HIF-2α C-terminal oxygen-dependent degradation-domain peptide (residues 523–542). HIF-2α appears in that structure only as a short substrate peptide bound to a different enzyme; it contains no PAS-B pocket at all. Every docking score on 7Q5V came back positive (+10.95 to +12.21 kcal/mol): the belzutifan analogues clash with the PHD2 active site because there is no pocket for them to occupy. That run is also discarded in full.

**The correction.** The correct structure is PDB 7W80, the HIF-2α–ARNT heterodimer in complex with belzutifan at 2.75 Å (Ren et al., Mol Pharmacol 2022). The re-dock reported here uses 7W80 only, with the grid centre at the centroid of the co-crystallised belzutifan (residue 72Q), computed with the pipeline's own `dock._ligand_center` — [−13.03, −22.77, 21.72] — the same audited centre-pick that the TYK2 correction established for this series. One caveat is unavoidable and is stated in the paper, not buried: **7W80 is the mouse heterodimer**. No human belzutifan-bound HIF-2α structure exists. The PAS-B pocket is the drug's binding site in both species, but species is a limitation of the docking, not a detail to be smoothed over.

### 2.3 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: human HIF-2α (EPAS1), UniProtKB Q99814; ChEMBL target CHEMBL1744522 (Endothelial PAS domain-containing protein 1, SINGLE PROTEIN, Homo sapiens — verified live 2026-11-21). Structure: PDB 7W80, the mouse HIF-2α–ARNT heterodimer in complex with belzutifan, 2.75 Å X-ray resolution. Grid centre: centroid of the co-crystallised belzutifan (ligand 72Q, 26 atoms), [−13.03, −22.77, 21.72], verified by direct computation from the PDB file with `dock._ligand_center`; box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for belzutifan and all four analogues. Belzutifan is therefore the self-dock control on its own structure: a method that could not recover strong binding for a 20 nM binder would be broken.

The comparison set is five compounds from the corrected EPAS1 ChEMBL run (26 ranked leads from 44 bioactivities): belzutifan itself and the four highest-ranked analogues with measured potency. All five share the belzutifan scaffold — a difluoro-indanol methylsulfone series — so the set tests scaffold variation, not chemotype diversity. Their measured potencies are ChEMBL bioactivities, not new measurements: belzutifan IC50 9.0 nM (pChEMBL 8.05); CHEMBL5723338 IC50 16.0 nM (pChEMBL 7.80); CHEMBL4453227 EC50 4.0 nM (pChEMBL 8.40); CHEMBL4173075 IC50 8.5 nM (pChEMBL 8.07); CHEMBL5764181 IC50 11.0 nM (pChEMBL 7.96). Note the endpoint mismatch, flagged wherever it matters: CHEMBL4453227's value is an EC50, not an IC50, so its "most potent" status is not directly comparable with the other four.

### 2.4 PAINS screen

RDKit PAINS filter applied to belzutifan and the four analogues. All five are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for belzutifan: molecular weight 383.35, logP 3.29, 1 hydrogen-bond donor, 5 acceptors, TPSA 87.39 Å², 3 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. ToxGuard Tox21 kNN read-across (12 assays) for belzutifan: maximum predicted probability 0.196 (SR-MMP), with a maximum neighbour similarity of only 0.28 — a weak read-across, not a measurement, and it does not clear the compound for development. The four analogues share the profile closely: CHEMBL5723338 (MW 365.36, logP 2.82, HBD 1, HBA 5, TPSA 87.39 Å², 3 rotatable bonds, 0 violations; max Tox21 probability 0.184, SR-MMP), CHEMBL4453227 (MW 401.34, logP 3.59, HBD 1, HBA 5, TPSA 87.39 Å², 3 rotatable bonds, 0 violations; max 0.191, SR-MMP), CHEMBL4173075 (MW 383.35, logP 3.12, HBD 1, HBA 5, TPSA 87.39 Å², 3 rotatable bonds, 0 violations; max 0.102, SR-ARE) and CHEMBL5764181 (MW 383.35, logP 3.12, HBD 1, HBA 5, TPSA 87.39 Å², 3 rotatable bonds, 0 violations; max 0.102, SR-ARE). The whole set is small, rigid and drug-like by these counts — which is expected, because all five are variations on one optimised scaffold, and which is itself a warning that these descriptor counts cannot rank this class.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for the four analogues against HIF-2α in this study beyond their published ChEMBL potencies. The structure is mouse, not human. The five measured potency values in this paper are published ChEMBL bioactivities, not new measurements, and one of them (CHEMBL4453227) is an EC50 where the others are IC50 values.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured HIF-2α potency (ChEMBL) | Best affinity, 7W80 (kcal/mol) | Top-3 poses (kcal/mol) | Median pose | Margin vs belzutifan |
|---|---|---|---|---|---|
| Belzutifan (reference) | IC50 9.0 nM | −10.94 | −10.94, −9.37, −4.41 | −9.37 | — |
| CHEMBL5723338 | IC50 16.0 nM | −11.40 | −11.40, −9.58, −5.20 | −9.58 | +0.46 (best pose only) |
| CHEMBL4453227 | EC50 4.0 nM | −11.22 | −11.22, −9.63, −4.00 | −9.63 | +0.28 |
| CHEMBL4173075 | IC50 8.5 nM | −10.76 | −10.76, −9.70, −6.13 | −9.70 | −0.18 |
| CHEMBL5764181 | IC50 11.0 nM | −10.82 | −10.82, −9.31, −6.16 | −9.31 | −0.12 |

Belzutifan re-docks at −10.94 kcal/mol on its own structure. That is a strong self-dock control: the method recovers strong binding for a 20 nM binder in the pocket it was crystallised in, so the protocol is not broken. Two analogues out-score it on best pose, but neither margin survives the noise test: 0.46 and 0.28 kcal/mol against Vina's ±1–2 kcal/mol. The other two analogues score below belzutifan, by 0.18 and 0.12 kcal/mol — also inside noise. On best pose, the whole series spans 0.64 kcal/mol, from −11.40 to −10.76: the five compounds are indistinguishable by this method.

The median poses tell a different story from the best poses, and that is itself the finding. On medians, CHEMBL4173075 leads at −9.70, ahead of CHEMBL4453227 (−9.63), CHEMBL5723338 (−9.58), belzutifan (−9.37) and CHEMBL5764181 (−9.31) — an order that shares only one compound with the best-pose order, and whose largest margin (0.33 kcal/mol) is again inside noise. The pose spread within each compound is also wide: belzutifan's three poses span 6.53 kcal/mol (−10.94 to −4.41), and every compound's third pose is 5–7 kcal/mol worse than its best. The PAS-B pocket is small and hydrophobic, and Vina finds one good pose and then much worse ones; the best pose is a single-point estimate, not a robust ranking.

The decisive check is the comparison with measured potency. The best-docking analogue, CHEMBL5723338, is the *least* potent compound in the set by assay (IC50 16.0 nM). The most potent, CHEMBL4453227 (EC50 4.0 nM), docks second. Belzutifan itself (IC50 9.0 nM) docks last on best pose. A scoring function that ranks the weakest binder first and the reference drug last, inside one scaffold family on the reference drug's own structure, cannot rank this family at all. The honest reading of the table is therefore a null result: no analogue beats belzutifan beyond noise, and the method itself fails its own positive control.

### 3.2 Comparison with published docking

No published Vina study of belzutifan or these four analogues on 7W80 was found in the sweep; the comparison here is internal (analogues vs re-docked reference drug on the same structure, same protocol). The crystal structure itself (7W80) is the published ground truth for the binding mode; this paper tests whether a rigid scoring function can rank compounds inside that mode. The two discarded pipeline runs are the paper's other comparison: docking belzutifan analogues on the wrong protein (FIH-1, 7A1Q) returned −5.73 kcal/mol for belzutifan, and docking them on the wrong structure (PHD2, 7Q5V) returned +11.38 kcal/mol — a spread of 17 kcal/mol for the same compound from structure choice alone, which is a measure of how much of a docking "result" is the structure, not the molecule.

### 3.3 The clinical confounder that docking cannot see

Belzutifan's clinical record is the paper's most important context, and docking cannot see any of it. The drug's 22.7% response rate in advanced ccRCC is not a binding problem — it binds at 20 nM — it is a biology problem: tumours escape HIF-2α inhibition through HIF-1α compensation, VEGF-pathway rewiring, and resistance mutations in the PAS-B pocket itself, and the patients who do respond are the ones whose tumours remain HIF-2α-dependent. A compound that out-scores belzutifan here by 0.46 kcal/mol would still face the same escape biology, and the casdatifan and NKT2152 programmes — which are, in effect, the clinical test of "a better belzutifan" — have so far reported response rates of 33% and 20%, not a step-change. The docking order cannot explain why belzutifan works in VHL disease (49% response) and in only a minority of advanced ccRCC (22.7%), and it cannot predict which patient will respond. That is a limitation of the question, not of the execution.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since belzutifan was approved. Before approval, the question was "can HIF-2α be drugged at all?" — now it is "which molecule, if any, beats the approved drug, and in which patients?" The docking benchmark is therefore a screen for successors, not for proof of concept, and its bar is higher: a new compound must beat belzutifan on the target and then survive the resistance biology that limits belzutifan itself. This paper's null result is useful precisely as a null: it says the next screen must be an enzyme assay, not a bigger docking set of the same scaffold.

### 4.2 Why the "win" must not be over-read

Four reasons. First, every margin in §3.1 lies inside Vina's ±1–2 kcal/mol noise unless stated otherwise. Second, the ranking contradicts measured potency — the least potent compound docks best — which is the method failing its own positive control. Third, all five compounds share one scaffold, so even a genuine docking advantage would be a variation on the approved chemotype, not a new one, and would inherit its developability profile and its resistance liabilities. Fourth, the structure is mouse: the pocket is the drug's site, but a human-structure confirmation does not exist, so every score here carries a species asterisk that only an assay can remove.

### 4.3 The target-resolution lesson

The two discarded runs deserve a paragraph of their own, because they are the failure mode this series must keep auditing for. The pipeline resolved a protein name to the wrong UniProt accession (HIF1AN instead of EPAS1) and then resolved the right accession to the wrong structure (a PHD2 complex in which HIF-2α is a peptide, not the PAS-B domain). Both errors produced complete, plausible-looking outputs — scores, tables, a "pipeline OK" — and both would have survived any check that did not verify the protein and the structure independently. The TYK2 correction in this series (JH2 vs JH1) was the same lesson in a different domain. The rule that follows is mechanical, not judgmental: **verify the UniProt accession, the ChEMBL target name, the PDB title and the ligand identity before any score is quoted**, and discard and disclose the runs that fail the audit. This paper does that; the discarded 7Q5V docking is preserved in `hidden_files/dock-HP-083-2026-11-21.json`, and the FIH-1 first attempt (which returned no UniProt hit and no docking) is recorded in the run log and in the re-dock script's docstring — its output file was overwritten by the corrected EPAS1 run, which is itself a bookkeeping gap worth naming.

### 4.4 Mechanism

Belzutifan occupies the PAS-B cavity of HIF-2α and allosterically destabilises the HIF-2α–ARNT heterodimer, mainly through M252 near the dimer interface; without the heterodimer there is no binding to hypoxia-response elements and no transcription of VEGF, GLUT1, EPO and the rest of the HIF-2 program. Test for each link: (i) a TR-FRET HIF-2α–ARNT dimer-disruption assay measures Ki directly against belzutifan (20 nM) as comparator; (ii) a luciferase reporter assay in VHL-null 786-O cells measures transcriptional inhibition against belzutifan (IC50 17 nM); (iii) an erythropoietin counter-readout in the same cells measures whether the analogue kept the on-target pharmacology that causes the class anaemia — loss of EPO suppression would mean the analogue is not engaging HIF-2α in cells at all, whatever it scores in silico.

### 4.5 Testable hypotheses

1. The best-scoring analogue inhibits HIF-2α–ARNT dimerisation with a Ki within 3-fold of belzutifan's 20 nM in a TR-FRET assay. Falsifier: Ki > 60 nM.
2. The same analogue inhibits HIF-2α-driven transcription with an IC50 within 3-fold of belzutifan's 17 nM in a 786-O luciferase reporter assay. Falsifier: IC50 > 50 nM.
3. The analogue suppresses erythropoietin transcription in the same cells at least as strongly as belzutifan at matched concentration. Falsifier: no EPO suppression below 1 µM.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): TR-FRET HIF-2α–ARNT dimer-disruption assay for the two candidate analogues — CHEMBL5723338 (best best-pose, −11.40) and CHEMBL4453227 (most potent measured, EC50 4.0 nM) — plus belzutifan control; readout Ki, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): luciferase reporter assay in VHL-null 786-O cells plus EPO transcription readout for the same set. Stage 3 (weeks 9–12): if any analogue passes stages 1–2, solubility and plasma-protein-binding measurement; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin.
2. The structure is the mouse HIF-2α–ARNT heterodimer (7W80); no human belzutifan-bound HIF-2α structure exists, so every score carries a species asterisk.
3. All five docked compounds share one scaffold (the belzutifan difluoro-indanol methylsulfone series); no chemotype diversity was tested.
4. One compound's measured value is an EC50 where the others are IC50 values, so the "most potent" label is not directly comparable.
5. A single rigid structure was used; the PAS-B pocket adapts to different chemotypes, so one structure under-samples the binding landscape.
6. The pipeline mis-resolved the target twice before the correction (FIH-1, then a PHD2 structure); the audit caught both, but the episode shows the pipeline's target and structure picks need independent verification every run.
7. No data on the clinical confounder: docking cannot distinguish VHL disease (where belzutifan responds in 49%) from advanced ccRCC (22.7%), and cannot predict resistance.
8. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon; the full Arabic text was not read, and other classical works on kidney disease were not individually consulted.

## 6. Conclusion

Belzutifan, the only approved direct HIF-2α inhibitor, re-docks at −10.94 kcal/mol on its own 2.75 Å structure 7W80, with a strong self-dock control and no PAINS alert — a validated control, not a discovery. No analogue beats it: the best best-pose margin (CHEMBL5723338, +0.46 kcal/mol) lies inside Vina noise, the most consistent analogue on medians (CHEMBL4173075, −9.70) leads by only 0.33 kcal/mol, and the method fails its own positive control — the least potent compound by measured assay docks best, and belzutifan itself docks last. The docking verdict is a null result, and it is useful precisely as one: this scaffold series cannot be ranked by rigid Vina scoring on a mouse structure, and the next screen must be a TR-FRET dimer-disruption assay, not a bigger docking set. What the docking cannot do is resolve the clinical split: the same drug responds in 49% of VHL-associated renal cell carcinomas and 22.7% of advanced ccRCC, and no binding score explains that. The next step is the cheap, decisive test — a TR-FRET assay plus a 786-O luciferase reporter for the best-scoring analogue against belzutifan — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Higher Education Commission research-funding panels, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of HIF-2α inhibition as an academic drug-discovery exercise, and whether to prepare DRAP's assessment pathway for a first-in-class drug whose successor pipeline is already in phase 3. **Exact change:** commission the 8–12-week TR-FRET plus luciferase-reporter screen proposed in §4.6 for the two best-scoring analogues against belzutifan, instead of funding another purely computational screen of the same target; and, in parallel, ask DRAP's registration reviewers to note the response-rate split explicitly in any future belzutifan dossier — approval for VHL disease is not evidence for advanced ccRCC, where the drug works in fewer than one in four patients. **If evidence Z appears, reverse this:** if the best analogue loses >3-fold to belzutifan in the TR-FRET assay or fails the reporter assay, drop this scaffold set and redirect the same screen to the next HIF-2α chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable HIF-2α inhibitor from a useless one for a disease that killed 155,953 people in 2022, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Ren X, Diao X, Zhuang J, Wu D. Structural basis for the allosteric inhibition of hypoxia-inducible factor (HIF)-2 by belzutifan. Mol Pharmacol. 2022;102(6):376-383. doi:10.1124/molpharm.122.000525. PMID: 36167425.
2. Jonasch E, Donskov F, Iliopoulos O, et al. Belzutifan for renal cell carcinoma in von Hippel-Lindau disease. N Engl J Med. 2021;385(22):2036-2046. doi:10.1056/NEJMoa2103425.
3. Choueiri TK, Powles T, Peltola K, et al. Belzutifan versus everolimus for advanced renal-cell carcinoma. N Engl J Med. 2024;391(8):710-721. doi:10.1056/NEJMoa2313906.
4. US Food and Drug Administration. FDA approves belzutifan for cancers associated with von Hippel-Lindau disease. 13 August 2021.
5. US Food and Drug Administration. FDA approves belzutifan for advanced renal cell carcinoma. 14 December 2023.
6. Bray F, Laversanne M, Sung H, et al. Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. CA Cancer J Clin. 2024;74(3):229-263. doi:10.3322/caac.21834.
7. Figg WD Jr, Fiorini G, Chowdhury R, et al. Structural basis for binding of the renal carcinoma target hypoxia-inducible factor 2 alpha to prolyl hydroxylase domain 2. Proteins. 2023;91(11):1510-1524. doi:10.1002/prot.26541. PMID: 37449559.
8. RCSB PDB entry 7W80: HIF-2α–ARNT heterodimer (Mus musculus) in complex with belzutifan, 2.75 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
9. RCSB PDB entry 7Q5V: PHD2/EGLN1 in complex with N-oxalylglycine and HIF-2α CODD (523–542), 1.17 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
10. ChEMBL target CHEMBL1744522: Endothelial PAS domain-containing protein 1 (EPAS1), Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-21.
11. UniProtKB Q99814: Endothelial PAS domain-containing protein 1 (EPAS1), Homo sapiens. UniProt. Accessed 2026-11-21.
12. ClinicalTrials.gov. NCT05536141: ARC-20 — casdatifan (AB521) in advanced clear-cell renal cell carcinoma. Accessed 2026-11-21.
13. ClinicalTrials.gov. NCT05119335: NKT2152 in advanced clear-cell renal cell carcinoma. Accessed 2026-11-21.
14. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; diseases of the kidney, amrad al-kulya.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-083-redock-2026-11-21.json` (belzutifan + four ChEMBL analogues on 7W80) and `hidden_files/dock-HP-083-2026-11-21.json` (corrected EPAS1 pipeline run, including the discarded 7Q5V docking; the FIH-1 first attempt returned no hit and its output file was overwritten by the corrected run — see §4.3). Reference drug belzutifan, PubChem CID 117947097 (ChEMBL4585668); analogues ChEMBL5723338, ChEMBL4453227, ChEMBL4173075, CHEMBL5764181. Structure: PDB 7W80 (2.75 Å, mouse). Target: UniProtKB Q99814; ChEMBL target CHEMBL1744522. No additional data were generated.
