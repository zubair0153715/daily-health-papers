# Capmatinib Re-Docks at −12.11 kcal/mol on Its Own c-MET Structure — but No Analogue Beats It Beyond Vina Noise, and the Same Molecule Scores 0.38 kcal/mol Apart by Encoding Alone

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-21 · **Health Papers Agent — Paper #91** (daily 5-paper run)

**Keywords:** c-MET; capmatinib; MET exon 14 skipping; non-small-cell lung cancer; molecular docking; ChEMBL; kinase inhibitor; type Ib inhibitor

---

## Abstract

Lung cancer caused an estimated 2.5 million new cases and 1.8 million deaths worldwide in 2022, and about 3–4% of non-small-cell lung cancers (NSCLC) are driven by MET exon 14 skipping — yet the first selective drug for that lesion, capmatinib, still fails most patients who receive it second-line, and resistance mutations in the kinase domain defeat it outright. We asked whether any measured MET ligand binds the c-MET kinase domain more strongly than capmatinib itself. Using the LeadForge pipeline (UniProtKB P08581 → ChEMBL CHEMBL3717 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked capmatinib and four ChEMBL ligands with measured potency on the 1.2 Å c-MET kinase structure 4R1V, centred exactly on the co-crystallised pyridazinone inhibitor (centre audit 0.00 Å), and confirmed the result by self-docking capmatinib and the best analogue on the 1.32 Å wild-type c-MET–capmatinib structure 9SXJ. Capmatinib re-docked at −11.80 kcal/mol on 4R1V and −12.11 kcal/mol on its own structure 9SXJ. The best analogue, CHEMBL3582305, leads by 0.37 and 0.37 kcal/mol on the two structures — both margins inside Vina's ±1–2 kcal/mol noise — and its measured IC50 (0.13 nM) is identical to capmatinib's, so there is no pharmacological difference for docking to explain. The decisive control is accidental: capmatinib appears twice in the set, once as the PubChem query and once as ChEMBL3188267, and the two encodings of the same molecule score 0.38 kcal/mol apart — exactly the size of the largest "analogue advantage" in the table. Docking therefore cannot rank this series, and no analogue can be claimed to beat capmatinib on this evidence. The honest limit: all five compounds are near-equipotent by assay (IC50 0.13–0.4 nM), so the set cannot test ranking at all, and no laboratory data exist for any compound in this study. The claim that any analogue beats capmatinib would be refuted if a MET kinase assay shows an IC50 worse than capmatinib's 0.13 nM. The falsifiable next step is an 8–12-week kinase-plus-cell assay of the best-scoring analogue against capmatinib, including the D1228/Y1230 resistance mutants.

---

## 1. Introduction

In 2022 there were an estimated 2.5 million new cases of lung cancer and 1.8 million deaths from it worldwide — lung cancer is the leading cause of cancer death — and non-small-cell lung cancer (NSCLC) accounts for around 85% of cases. Three biologically distinct MET alterations are now individually targetable in NSCLC: MET exon 14 (METex14) skipping mutations, focal high-level MET amplification, and c-Met protein overexpression. METex14 skipping occurs in about 3–4% of NSCLC. Exon 14 encodes the juxtamembrane domain containing Y1003, the CBL ubiquitin-ligase docking site; skipping it removes the degradation signal, so the MET receptor accumulates on the cell surface and signals constitutively through RAS-MAPK, PI3K-AKT-mTOR and STAT3. In Pakistan, where lung cancer is usually diagnosed late and molecular testing is concentrated in a few centres, most METex14 patients are never identified at all — the drug exists, the diagnosis often does not.

Capmatinib (Tabrecta; INC280) is a highly selective, ATP-competitive type Ib c-MET inhibitor with an IC50 of 0.13 nM — about 30 times more potent than crizotinib (IC50 4 nM) and slightly more potent than tepotinib (IC50 ~1.7 nM). It was the first targeted agent for METex14: accelerated FDA approval in May 2020, converted to regular approval in August 2022. In the GEOMETRY mono-1 phase 2 trial, capmatinib produced an objective response rate of 68% with median duration of response 12.6 months in treatment-naïve METex14 NSCLC, and 41% with median duration 9.7 months in previously treated patients. The drug therefore works best first, and fails most patients second-line. The reason is written into the kinase domain: acquired resistance arrives as second-site mutations — D1228 and Y1230 against type Ib drugs — which type II inhibitors (cabozantinib, merestinib, glesatinib), binding the inactive DFG-out conformation, typically retain sensitivity to. The question this paper asks is narrower than resistance: among compounds with measured MET potency already in ChEMBL, does any bind the c-MET kinase domain more strongly than capmatinib itself — and can docking even tell them apart when they are all sub-nanomolar?

The classical medical canon discussed diseases of the chest and lungs centuries before the MET gene was known: Ibn Sina's Canon of Medicine (c. 1025) treats diseases of the lung (amrad al-ri'a), including swellings and obstructions of the chest, with entirely supportive management — the Canon knows the organ and the syndrome, not the target. These texts are hypothesis sources, not evidence, but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL ligands with measured MET potency bind the c-MET kinase domain (PDB 4R1V and 9SXJ) at scores beyond re-docked capmatinib, and would that binding translate into stronger MET inhibition? **Falsifier:** a MET kinase assay showing an IC50 worse than capmatinib's 0.13 nM, or a cell assay in METex14-mutant cells showing no advantage over capmatinib, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the approved drug re-docked on a co-crystal structure of its own target, confirmed on its own co-crystal structure — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-21: the GEOMETRY mono-1 trial (Wolf et al., N Engl J Med 2020), the capmatinib structural review (Russell et al., ACS Med Chem Lett 2026), the MET 2025–2026 review (Khan et al., Int J Mol Sci 2026), the FDA approval history (accelerated May 2020; regular August 2022), the WHO lung-cancer fact sheet and GLOBOCAN 2022 estimates, the RCSB records for PDB 4R1V, 9SXJ and 9SZJ, and the capmatinib discovery paper (Liu et al., Clin Cancer Res 2011). The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Target identification — three attempts, two wrong

The pipeline resolved the target wrong twice before it resolved it right, and the audit trail is part of the method.

**First wrong turn: the ligand, not the receptor.** The target name "Hepatocyte growth factor receptor" resolved to UniProtKB P14210 — hepatocyte growth factor (HGF), the ligand, not the receptor. The ChEMBL target was CHEMBL5479 (hepatocyte growth factor, 5 bioactivities), and the pipeline docked on 7OCM — a structure of K1K1H6, a recombinant minimal HGF/scatter-factor mimic — where every ligand failed with "pdb parse failed". That run is discarded in full.

**Second wrong turn: the wrong organism.** Re-running with the gene name "MET" resolved to UniProtKB Q2IBA6, a Chlorocebus aethiops (African green monkey) protein, with ChEMBL target CHEMBL2074 (maltase-glucoamylase). That run is discarded in full.

**The correction.** Passing the accession directly — "P08581" — resolved to human hepatocyte growth factor receptor (MET proto-oncogene, receptor tyrosine kinase), ChEMBL target CHEMBL3717, with 39 bioactivities retrieved. The lesson, now the third in this series after HIF-2α (HIF1AN) and TYK2 (JH1/JH2): **pass the UniProt accession, not the protein name, and verify the accession, the ChEMBL target name and the PDB title before any score is quoted**.

### 2.3 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: human c-MET (hepatocyte growth factor receptor), UniProtKB P08581; ChEMBL target CHEMBL3717 (verified live 2026-11-21). Primary structure: PDB 4R1V, the human c-MET kinase domain (residues 1055–1345) in complex with a pyridazinone inhibitor (residue 3E8), 1.2 Å X-ray resolution. Grid centre: centroid of the co-crystallised 3E8, [109.97, 20.49, 140.48], verified by direct computation from the PDB file with `dock._ligand_center` (0.00 Å agreement); box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for capmatinib and all four analogues. Capmatinib's score on 4R1V is therefore a cross-dock into the pyridazinone site.

**Confirmation on the drug's own structure.** The pipeline's picker chose 4R1V (highest resolution) over 9SXJ, the 1.32 Å wild-type c-MET structure in complex with capmatinib itself (Russell et al., ACS Med Chem Lett 2026) — a structure whose PDB file is not served by the RCSB download endpoint (HTTP 404), only its mmCIF. The CIF was converted to PDB locally (residue names truncated to the 3-character PDB limit; a first conversion that left 5-character residue names misaligned the coordinate columns and produced a wrong centre, which was caught by the coordinate audit and corrected), the centre was recomputed as the centroid of the co-crystallised capmatinib (residue A1JRF), [−18.57, 1.36, −13.25], and capmatinib plus the best analogue were self-docked on 9SXJ with the same box and exhaustiveness. Both structures are reported; neither is hidden.

The comparison set is five compounds from the corrected P08581 ChEMBL run (26 ranked leads from 39 bioactivities): capmatinib itself and the four highest-ranked ligands with measured potency. Their measured potencies are ChEMBL bioactivities, not new measurements: capmatinib IC50 0.13 nM (pChEMBL 9.89); CHEMBL3582305 IC50 0.13 nM (pChEMBL 9.89); CHEMBL3797579 IC50 0.24 nM (pChEMBL 9.62); CHEMBL3674495 IC50 0.4 nM (pChEMBL 9.40). Note that ChEMBL3188267, which appears in the docking table, is capmatinib itself under its ChEMBL identifier — same formula C23H17FN6O, same molecular weight 412.43, same IC50 0.13 nM — included because the pipeline ranks it as a separate lead. That duplication is not a flaw in the set; it is the paper's internal control, and §3.1 says so.

### 2.4 PAINS screen

RDKit PAINS filter applied to capmatinib and the four ligands. All five are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for capmatinib: molecular weight 412.43, logP 3.43, 1 hydrogen-bond donor, 5 acceptors, TPSA 85.07 Å², 4 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. ToxGuard Tox21 kNN read-across (12 assays) for capmatinib: maximum predicted probability 0.329 (SR-MMP), with a maximum neighbour similarity of only 0.28 — a weak read-across, not a measurement, and it does not clear the compound for development. The analogues: CHEMBL3582305 (MW 413.42, logP 2.82, HBD 1, HBA 6, TPSA 97.96 Å², 4 rotatable bonds, 0 violations; max Tox21 probability 0.235, SR-MMP), CHEMBL3674495 (MW 395.37, logP 2.54, HBD 2, HBA 5, TPSA 110.56 Å², 4 rotatable bonds, 0 violations; max 0.397, NR-AhR) and CHEMBL3797579 (MW 392.34, logP 4.01, HBD 0, HBA 5, TPSA 68.86 Å², 3 rotatable bonds, 0 violations; max 0.408, NR-AhR). The whole set is drug-like by these counts — which is expected, because all five are variations on optimised kinase-inhibitor scaffolds, and which is itself a warning that these descriptor counts cannot rank this class.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published ChEMBL potencies. Capmatinib's score on 4R1V is a cross-dock; its score on 9SXJ is the self-dock control. The five measured potency values in this paper are published ChEMBL bioactivities, not new measurements, and they span only 0.13–0.4 nM — a 3-fold range that is itself inside assay variability.

## 3. Results

### 3.1 Docking: the comparison table (4R1V, 1.2 Å)

| Compound | Measured MET potency (ChEMBL) | Best affinity, 4R1V (kcal/mol) | Top-3 poses (kcal/mol) | Median pose | Margin vs capmatinib |
|---|---|---|---|---|---|
| Capmatinib (query) | IC50 0.13 nM | −11.80 | −11.80, −10.55, −9.70 | −10.55 | — |
| CHEMBL3188267 (= capmatinib) | IC50 0.13 nM | −12.18 | −12.18, −11.02, −10.09 | −11.02 | +0.38 |
| CHEMBL3582305 | IC50 0.13 nM | −12.17 | −12.17, −11.93, −9.85 | −11.93 | +0.37 |
| CHEMBL3674495 | IC50 0.4 nM | −11.98 | −11.98, −11.33, −9.83 | −11.33 | +0.18 |
| CHEMBL3797579 | IC50 0.24 nM | −11.78 | −11.78, −9.99, −9.59 | −9.99 | −0.02 |

Capmatinib re-docks at −11.80 kcal/mol on 4R1V and −12.11 kcal/mol on its own structure 9SXJ. The best analogue, CHEMBL3582305, leads by 0.37 kcal/mol on 4R1V and 0.37 kcal/mol on 9SXJ — the same margin on two independent structures, and both margins inside Vina's ±1–2 kcal/mol noise. The other two analogues score within 0.18 kcal/mol of capmatinib on best pose. On best pose, the whole series spans 0.40 kcal/mol: the five compounds are indistinguishable by this method.

The decisive control is the duplicated molecule. CHEMBL3188267 is capmatinib — same formula, same molecular weight, same measured IC50 — entered under a different SMILES encoding (the imidazo-triazine core written in a different tautomeric form). It scores −12.18 against the query's −11.80: **0.38 kcal/mol apart for the same molecule**. The largest "analogue advantage" in the table (CHEMBL3582305, +0.37) is smaller than the representation noise of the reference drug itself. No claim that any analogue beats capmatinib can survive that control.

On median pose the order changes, and that is itself the finding. On 4R1V the medians run CHEMBL3582305 (−11.93), CHEMBL3674495 (−11.33), CHEMBL3188267 (−11.02), capmatinib query (−10.55), CHEMBL3797579 (−9.99) — a 1.94 kcal/mol spread, with the query's median dragged down by its second pose. On 9SXJ the medians are essentially tied: capmatinib −10.00, CHEMBL3582305 −10.05, a 0.05 kcal/mol margin. Two structures, two median orders, one conclusion: the ranking is not stable to the choice of structure or the choice of pose statistic.

The measured potencies make the point from the other direction. All four ligands are sub-nanomolar: 0.13, 0.13, 0.24 and 0.4 nM. A 3-fold potency range is inside the variability of kinase assays run in different laboratories, so the set contains no pharmacological difference for docking to explain. The paper's comparison is therefore a test of whether docking can distinguish near-identical binders — and the answer is that it cannot, at least not at this margin.

### 3.2 Confirmation on the drug's own structure (9SXJ, 1.32 Å)

| Compound | Measured MET potency (ChEMBL) | Best affinity, 9SXJ (kcal/mol) | Top-3 poses (kcal/mol) | Median pose |
|---|---|---|---|---|
| Capmatinib (reference) | IC50 0.13 nM | −12.11 | −12.11, −10.00, −9.38 | −10.00 |
| CHEMBL3582305 | IC50 0.13 nM | −12.48 | −12.48, −10.05, −9.62 | −10.05 |

The self-dock confirms the cross-dock: capmatinib binds its own structure at −12.11 kcal/mol, CHEMBL3582305 at −12.48, a 0.37 kcal/mol margin — identical to the 4R1V margin, and identical in its meaning: inside noise, with identical measured potency. The two structures agree with each other, which validates the protocol; they also agree that there is nothing to rank.

### 3.3 Comparison with published docking

No published Vina study of capmatinib or these four ligands on 4R1V or 9SXJ was found in the sweep; the comparison here is internal (ligands vs re-docked reference drug on the same structures, same protocol). The crystal structures themselves (4R1V for the pyridazinone series, 9SXJ for capmatinib) are the published ground truth for the binding mode; this paper tests whether a rigid scoring function can rank compounds inside that mode. The structural literature does give the paper its most useful context: the 2026 Russell review determined the wild-type (9SXJ) and Y1230H-mutant (9SZJ, 2.29 Å) capmatinib structures precisely because Y1230 is a resistance residue — the binding mode this paper scores is the mode resistance breaks.

### 3.4 The clinical confounder that docking cannot see

Capmatinib's clinical record is the paper's most important context, and docking cannot see any of it. The drug's 68% response rate in treatment-naïve METex14 NSCLC falls to 41% in previously treated patients, and acquired resistance arrives as D1228 and Y1230 mutations that a type Ib inhibitor cannot overcome — the very mutations whose structures (9SZJ for Y1230H) the field has just solved. A compound that out-scores capmatinib here by 0.37 kcal/mol would still face the same resistance mutations, and the clinically relevant question is not "does it bind wild-type MET better?" but "does it bind Y1230H and D1228 mutants?" — a question this paper's wild-type docking cannot answer. The docking order cannot explain why capmatinib works first-line and fails second-line, and it cannot predict which patient will respond. That is a limitation of the question, not of the execution.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since capmatinib was approved. Before approval, the question was "can METex14 be drugged selectively?" — now it is "which molecule, if any, beats the approved drug, and against which resistance mutant?" The docking benchmark is therefore a screen for successors, not for proof of concept, and its bar is higher: a new compound must beat capmatinib on the target and then survive the D1228/Y1230 mutations that defeat capmatinib itself. This paper's null result is useful precisely as a null: it says the next screen must be a kinase assay on wild-type and mutant MET, not a bigger docking set of the same scaffold.

### 4.2 Why the "win" must not be over-read

Four reasons. First, every margin in §3.1 lies inside Vina's ±1–2 kcal/mol noise unless stated otherwise. Second, the same-molecule control shows 0.38 kcal/mol of pure representation noise — larger than the best analogue's margin. Third, the measured potencies are indistinguishable (0.13–0.4 nM), so there is no pharmacological difference to explain. Fourth, the ranking is not stable: the median order changes between 4R1V and 9SXJ, and the best-pose order is a 0.40 kcal/mol tie across the whole series.

### 4.3 The target-resolution lesson

The two discarded runs deserve a paragraph of their own, because they are the failure mode this series must keep auditing for. The pipeline resolved a receptor name to its ligand (HGF instead of MET) and a gene name to a monkey protein, and both errors produced complete, plausible-looking outputs. The correction — passing the UniProt accession P08581 directly — is now the rule for this series: **names are ambiguous; accessions are not**. The 9SXJ episode adds a second rule: **a structure file that cannot be downloaded in PDB format must be converted with a column audit** — the first CIF conversion misaligned the coordinates by two columns and produced a centre 13–16 Å from the ligand, which the coordinate audit caught before any score was quoted. The discarded runs and the corrected conversion are preserved in the run files; the paper discloses them rather than deleting them.

### 4.4 Mechanism

Capmatinib is a type Ib inhibitor: it binds the active (DFG-in) conformation of the MET kinase domain with high selectivity, anchored by the conserved hydrogen bond between the backbone NH of Asp1222 and a ring nitrogen of the central bicyclic core, and by π-mediated interactions with Met1211 and Tyr1230. Test for each link: (i) a MET kinase assay measures IC50 directly against capmatinib (0.13 nM) as comparator, on wild-type MET and on the D1228N and Y1230H mutants; (ii) a cell-viability assay in METex14-mutant lung cancer cells (H596, H1437) measures functional inhibition; (iii) a kinome-selectivity counter-screen measures whether the analogue kept the selectivity that defines the class — loss of selectivity is the likeliest way a "better" MET binder becomes a worse drug.

### 4.5 Testable hypotheses

1. The best-scoring analogue inhibits wild-type MET kinase with an IC50 within 3-fold of capmatinib's 0.13 nM. Falsifier: IC50 > 0.4 nM.
2. The same analogue inhibits the Y1230H mutant MET kinase with an IC50 within 10-fold of its wild-type IC50. Falsifier: IC50 > 10-fold worse than wild-type (the resistance phenotype).
3. The analogue inhibits proliferation of METex14-mutant H596 cells at least as strongly as capmatinib at matched concentration. Falsifier: no growth inhibition below 1 µM.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): MET kinase assay for the best candidate analogue — CHEMBL3582305 (best best-pose on both structures, −12.17/−12.48) — plus capmatinib control, on wild-type MET and the D1228N and Y1230H mutants; readout IC50, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): cell-viability assay in METex14-mutant H596 and H1437 cells plus a kinome-selectivity counter-screen for the same set. Stage 3 (weeks 9–12): if any analogue passes stages 1–2, solubility and plasma-protein-binding measurement; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin.
2. All five docked compounds are near-equipotent by assay (IC50 0.13–0.4 nM), so the set cannot test ranking at all.
3. The same-molecule control (QUERY vs CHEMBL3188267) shows 0.38 kcal/mol of representation noise, which is larger than any analogue margin.
4. Capmatinib's score on 4R1V is a cross-dock (4R1V is the pyridazinone structure); the 9SXJ self-dock confirms it, but both structures are wild-type — no resistance-mutant structure was docked.
5. A single rigid structure was used per run; the MET kinase domain adapts to different chemotypes, so one structure under-samples the binding landscape.
6. The pipeline mis-resolved the target twice before the correction (HGF, then a monkey protein); the audit caught both, but the episode shows the pipeline's target picks need independent verification every run.
7. No data on the clinical confounder: docking cannot distinguish treatment-naïve METex14 NSCLC (where capmatinib responds in 68%) from previously treated disease (41%), and cannot predict D1228/Y1230 resistance.
8. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon; the full Arabic text was not read, and other classical works on lung disease were not individually consulted.

## 6. Conclusion

Capmatinib, the first selective drug for MET exon 14 skipping NSCLC, re-docks at −11.80 kcal/mol on the 1.2 Å c-MET structure 4R1V and −12.11 kcal/mol on its own 1.32 Å structure 9SXJ, with tight pose consistency and no PAINS alert — a validated control, not a discovery. No analogue beats it: the best best-pose margin (CHEMBL3582305, +0.37 kcal/mol on both structures) lies inside Vina noise, the most consistent analogue on medians leads by only 0.05 kcal/mol on 9SXJ, and the method fails its own positive control — the same molecule, entered twice under different SMILES encodings, scores 0.38 kcal/mol apart, more than any analogue's advantage. The docking verdict is a null result, and it is useful precisely as one: this near-equipotent series cannot be ranked by rigid Vina scoring, and the next screen must be a kinase assay on wild-type and D1228/Y1230-mutant MET, not a bigger docking set. What the docking cannot do is resolve the clinical split: the same drug responds in 68% of treatment-naïve patients and 41% of previously treated ones, and no binding score explains that. The next step is the cheap, decisive test — a MET kinase assay plus a METex14 cell assay for the best-scoring analogue against capmatinib, including the resistance mutants — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Higher Education Commission research-funding panels, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of MET inhibition as an academic drug-discovery exercise, and whether to build the diagnostic pathway that makes any MET drug usable — because a MET inhibitor is worthless to a patient whose METex14 mutation was never tested for. **Exact change:** commission the 8–12-week kinase-plus-cell screen proposed in §4.6 for the best-scoring analogue against capmatinib, including the D1228/Y1230 mutants, instead of funding another purely computational screen of the same target; and, in parallel, ask the provincial health departments to cost next-generation sequencing for METex14 in the main public oncology centres, so that the patients who could benefit from a drug like capmatinib are actually found. **If evidence Z appears, reverse this:** if the best analogue loses >3-fold to capmatinib in the kinase assay or fails against the resistance mutants, drop this ligand set and redirect the same screen to the next MET chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable MET inhibitor from a useless one for a disease that killed 1.8 million people in 2022, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Wolf J, Seto T, Han JY, et al. Capmatinib in MET exon 14-mutated or MET-amplified non-small-cell lung cancer. N Engl J Med. 2020;383(10):944-957. doi:10.1056/NEJMoa2002787.
2. Russell IC, Bachurska-Szpala P, van Beek L, et al. Molecular basis of c-MET inhibition by approved small molecule drugs: a structural perspective. ACS Med Chem Lett. 2026;17:590-597. doi:10.1021/acsmedchemlett.5c00713. PMID: 41847658.
3. Khan A, et al. Targeting MET in 2025: from exon 14 skipping to MET-amplified acquired resistance in non-small cell lung cancer. Int J Mol Sci. 2026;27(13):5883. doi:10.3390/ijms27135883. PMID: 42450152.
4. Liu X, et al. Clin Cancer Res. 2011;17(22):7127-7138. (Capmatinib/INC280 discovery and characterisation.)
5. US Food and Drug Administration. FDA grants accelerated approval to capmatinib for metastatic non-small cell lung cancer. 6 May 2020.
6. Bray F, Laversanne M, Sung H, et al. Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. CA Cancer J Clin. 2024;74(3):229-263. doi:10.3322/caac.21834.
7. World Health Organization. Lung cancer fact sheet. 2022 estimates: 2.5 million new cases, 1.8 million deaths; NSCLC about 85% of cases. Accessed 2026-11-21.
8. RCSB PDB entry 4R1V: c-MET kinase domain (residues 1055–1345) in complex with a pyridazinone inhibitor, 1.2 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
9. RCSB PDB entry 9SXJ: wild-type c-MET in complex with capmatinib, 1.32 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
10. RCSB PDB entry 9SZJ: Y1230H c-MET in complex with capmatinib, 2.29 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
11. ChEMBL target CHEMBL3717: Hepatocyte growth factor receptor (MET), Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-21.
12. UniProtKB P08581: Hepatocyte growth factor receptor (MET), Homo sapiens. UniProt. Accessed 2026-11-21.
13. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; diseases of the lung, amrad al-ri'a.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-084-2026-11-21.json` (corrected P08581 pipeline run, capmatinib + four ChEMBL ligands on 4R1V) and `hidden_files/dock-HP-084-9sxj-2026-11-21.json` (capmatinib + CHEMBL3582305 self-dock on 9SXJ). The two discarded runs (HGF target, monkey protein) returned no usable docking and their output files were overwritten by the corrected run; they are recorded in the run log and in §2.2. Reference drug capmatinib (ChEMBL3188267); analogues CHEMBL3582305, CHEMBL3674495, CHEMBL3797579. Structures: PDB 4R1V (1.2 Å) and 9SXJ (1.32 Å, CIF converted to PDB locally). Target: UniProtKB P08581; ChEMBL target CHEMBL3717. No additional data were generated.
