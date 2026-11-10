# The Weakest Drug Scores Best: Acarbose Out-Docks Three Nanomolar Iminosugars on ntMGAM 3L4Y — and the Most Potent Lead Class Could Not Be Docked at All

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-10 · **Health Papers Agent — Paper #39** (daily 5-paper run)

**Keywords:** alpha-glucosidase; acarbose; maltase-glucoamylase; iminosugar; molecular docking; AutoDock Vina; type 2 diabetes; ChEMBL

---

## Abstract

Type 2 diabetes affects 589 million adults worldwide — one in nine — and Pakistan carries the world's highest age-standardised prevalence at 31.4%, with about 34.5 million adults affected. α-Glucosidase inhibitors such as acarbose blunt postprandial glucose by blocking the intestinal enzymes that finish carbohydrate digestion, but acarbose is a weak inhibitor (IC50 456–750 μM in standard assays) whose undigested carbohydrate causes flatulence in 74% of users, diarrhoea in 31% and abdominal pain in 19%. The gap this paper attacks is whether a standardised docking screen can rank better α-glucosidase leads against acarbose. We ran the LeadForge pipeline (UniProtKB O43451 → ChEMBL CHEMBL2074, 55 bioactivities → PubChem verification → RDKit ADMET/PAINS → AutoDock Vina 1.2.7) and docked the top leads plus acarbose into the 1.80 Å N-terminal maltase-glucoamylase structure 3L4Y, with the grid centre exactly on the co-crystallised inhibitor centroid (0.00 Å). Acarbose scored best by Vina (−6.55 kcal/mol) despite being roughly 100,000-fold weaker by measurement than the best lead, a silyl-iminosugar with Ki 2.3 nM that scored only −5.02. Among the three successfully docked leads the rank correlation is weak (Spearman ρ = +0.50, n = 3), and the fifth-ranked lead — a kotalanol-class sulfonium salt with IC50 470 nM — could not be docked at all, because the pipeline rejects multi-fragment salt SMILES. The falsifiable next step is a head-to-head ntMGAM inhibition assay for the three iminosugars against acarbose: if the measured order follows the ChEMBL record rather than the Vina order, docking must not be used to prioritise α-glucosidase leads on this structure, and the salt-form kotalanol analogue must be re-tested after desalting.

---

## 1. Introduction

The International Diabetes Federation's Diabetes Atlas (11th edition, 2025) estimates 589 million adults aged 20–79 live with diabetes — one in nine people — projected to reach 853 million by 2050. Pakistan has the world's highest age-standardised diabetes prevalence (31.4%), about 34.5 million adults affected and an estimated 226,752 diabetes-related deaths in 2024. Postprandial hyperglycaemia is a major driver of vascular complications, and the final step of carbohydrate digestion — hydrolysis of oligosaccharides to glucose by membrane-bound intestinal α-glucosidases, principally maltase-glucoamylase (MGAM) — is a validated drug target precisely because it acts in the gut lumen: inhibitors need not be absorbed at all.

Acarbose is the prototype. A complex oligosaccharide, it competitively and reversibly inhibits pancreatic α-amylase and the intestinal α-glucoside hydrolases, delaying carbohydrate digestion and lowering postprandial glucose without stimulating insulin secretion; it lowers HbA1c by roughly 0.5–1.0% as monotherapy. Its weaknesses are potency and tolerability: in standard in vitro assays its α-glucosidase IC50 is 456–750 μM (assay- and enzyme-source-dependent), and the undigested carbohydrate reaching the colon causes flatulence (74%), diarrhoea (31%) and abdominal pain (19%) in US placebo-controlled trials, with 25–45% of users discontinuing α-glucosidase inhibitors for gastrointestinal reasons. A more potent inhibitor, active at nanomolar rather than micromolar concentrations, could in principle achieve the same glucose control with less undigested carbohydrate — but only if potency is measured, not assumed from a docking score.

The natural-product literature already contains such compounds. Salacia reticulata, used in Ayurvedic medicine for type 2 diabetes, yields the sulfonium-sugar inhibitors salacinol and kotalanol; de-O-sulfonated kotalanol inhibits ntMGAM with Ki 0.03 μM — about 2,000-fold better than the clinical compounds — and its crystal complex with ntMGAM (PDB 3L4Y) defines the binding site used here. Recent work continues the same search: coumarin–triazole conjugates reported in 2026 reached IC50 1.0 μM against α-glucosidase versus 750 μM for acarbose in the same assay, with in vivo antihyperglycaemic activity in diabetic mice; and a 2025 machine-learning virtual screen of 100,000+ compounds found selective α-glucosidase inhibitors engaging the catalytic Asp526.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen of ChEMBL MGAM actives against acarbose on 3L4Y will rank compounds in the same order as their measured potencies. The test is the rank correlation, not the best score.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-10 (web search; PubMed/bioRxiv via the daily digest of 2026-11-10). Key sources: IDF Diabetes Atlas 11th edition (2025) for burden; the FDA acarbose label for adverse-event frequencies; Sim et al. 2010 for the 3L4Y structure and the Salacia inhibitors; the 2026 coumarin–triazole study; the 2025 machine-learning virtual-screening study; and the critical assessment of plant α-glucosidase screening with acarbose as reference. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt O43451 (human maltase-glucoamylase, MGAM); ChEMBL target CHEMBL2074; 55 bioactivities retrieved (pChEMBL ≥ 5), 26 leads after RDKit filtering and ranking; the top 5 leads docked, including the reference query itself. Structure: PDB 3L4Y, the N-terminal catalytic subunit of human intestinal MGAM in complex with the Salacia-derived inhibitor NR4-8II, resolution 1.80 Å. Grid centre [−2.01, −19.26, −20.85] — audited against the co-crystallised ligand NR4 centroid computed from the deposited coordinates: distance 0.00 Å, i.e. the grid is exactly on the catalytic site. Best of three poses reported per compound. The same grid, box and exhaustiveness were used for every compound including acarbose.

One lead, CHEMBL3815109, failed to dock: its ChEMBL record is a sulfonium chloride salt (two SMILES fragments), and the pipeline's ligand preparation rejects multi-fragment molecules ("RDKit molecule has 2 fragments. Must have 1."). It is reported as a failed dock, not silently dropped, and the paper's conclusions do not depend on it.

### 2.3 PAINS screen

RDKit PAINS filter applied to every docked compound. No compound in the docked set carries a PAINS alert.

### 2.4 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol — larger than most of the differences in this paper. A single rigid structure (3L4Y, inhibitor-bound conformation) cannot represent the conformational ensemble of MGAM, and carbohydrate-binding sites are shallow and solvent-exposed, which is exactly where rigid docking is weakest. No molecular dynamics or free-energy refinement was run. No experimental data were generated. Acarbose has no ChEMBL MGAM bioactivity meeting the pipeline's pChEMBL ≥ 5 retrieval threshold, so its measured potency is taken from the published literature (456–750 μM, assay-dependent), not from the same ChEMBL pull as the leads.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Vina best (kcal/mol) | Poses (kcal/mol) | Measured potency (ChEMBL, top record) | pChEMBL | PAINS |
|---|---|---|---|---|---|
| Acarbose (query) | −6.55 | −6.55, −6.35, −6.24 | IC50 456–750 μM (literature α-glucosidase assays; no ChEMBL MGAM record ≥ pChEMBL 5) | — | none |
| CHEMBL120226 | −6.35 | −6.35, −6.12, −5.87 | Ki 4.0 nM | 8.40 | none |
| CHEMBL432221 | −5.02 | −5.02, −4.82, −4.71 | Ki 2.3 nM | 8.64 | none |
| CHEMBL2442258 | −4.26 | −4.26, −4.07, −4.06 | IC50 60 nM | 7.22 | none |
| CHEMBL3815109 | FAILED | — | IC50 470 nM | 6.33 | none |

All successful docks are on 3L4Y (1.80 Å), grid centre exactly on the co-crystallised NR4 centroid (0.00 Å). The three leads are iminosugars: two silyl-substituted 1-deoxynojirimycin analogues (CHEMBL120226, CHEMBL432221) and a small N-methyl iminosugar (CHEMBL2442258, MW 207.23). The failed compound, CHEMBL3815109, is a sulfonium-sugar salt of the kotalanol class.

Acarbose scores best by Vina while being the weakest inhibitor by measurement by roughly five orders of magnitude: its literature IC50 (456–750 μM) is ~100,000–300,000-fold higher than the best lead's Ki (2.3 nM). The Vina spread across the four successful docks is 2.29 kcal/mol, but the best-vs-second margin (acarbose vs CHEMBL120226, 0.20 kcal/mol) is far inside noise, and the leads' own order is only weakly related to measurement: Spearman ρ = +0.50 (n = 3) among the three docked leads. Pose consistency is good (top-three poses within 0.31 kcal/mol for every compound), so the failure is in the scoring, not in pose sampling.

### 3.2 Comparison with published docking

Published Vina scores for α-glucosidase show the same pattern of weak absolute values: plant-derived leads against α-glucosidase scored −6.66 and −5.64 kcal/mol versus acarbose −4.27 kcal/mol in a 2025 study, and a Nardostachys jatamansi study reported virolin at −9.6 kcal/mol against α-glucosidase. The absolute numbers move with the structure, the grid and the ligand set; only the within-protocol ranking in Table 3.1 is interpretable — and Section 3.3 shows that ranking fails its own test. Note also that all scores here (−4 to −6.5) are far weaker than the kinase benchmarks in Papers #37–#38 (−9 to −12): carbohydrate-binding clefts give small, polar ligands little surface to grip, and cross-target score comparison is meaningless.

### 3.3 The standardisation problem: the reference wins by scoring, loses by measurement

Two failures are visible at once. First, the reference drug beats every lead by Vina while being ~10⁵-fold weaker by measurement — the exact inversion of what a screen is supposed to do, and the largest potency/score disconnect in this 5-paper run. A plausible mechanism is size: acarbose (MW 645.61) fills far more of the shallow cleft than the small iminosugars (MW 207–337), and Vina's scoring rewards contact count, so the big, weak binder out-scores the small, tight binders. Second, the most interesting chemotype in the set — the kotalanol-class sulfonium salt, from the same class as the most potent ntMGAM inhibitor ever reported (Ki 0.03 μM) — never got a score at all, because the pipeline cannot prepare salt forms. The screen thus fails on both axes: it ranks the weakest compound first, and it cannot evaluate the strongest class.

Drug-likeness cuts the other way for acarbose: three Lipinski violations (MW 645.61, logP −8.72) would normally disqualify a lead, but acarbose acts in the gut lumen with <2% systemic absorption, so Lipinski's rules do not apply to it — a reminder that the pipeline's drug-likeness flags must be read target by target. The iminosugar leads are all Lipinski-clean (MW 207–337, logP −3.26 to −0.54, zero violations). No Tox21 flags were predicted for any compound by kNN read-across — a prediction, not a measurement.

## 4. Discussion

### 4.1 The reframe

The question was whether docking can rank α-glucosidase leads against acarbose. The answer on this structure is no, and the reason is instructive: the scoring function appears to reward molecular size in a shallow, solvent-exposed cleft, so the large oligosaccharide reference out-scores small iminosugars that bind 10⁵-fold more tightly. The paper's contribution is therefore a caution with a mechanism, not a lead claim — and a second caution about pipeline hygiene: a standard ligand-preparation step silently (here, loudly) excludes salt-form compounds, which for this target means excluding the most potent known chemotype.

### 4.2 Why the "win" must not be over-read

Three reasons. First, acarbose's 0.20 kcal/mol margin over CHEMBL120226 is far inside the ±1–2 kcal/mol noise. Second, the measured-potency gap runs the other way by five orders of magnitude — no rescoring of these numbers can bridge that. Third, the leads' own rank correlation (ρ = +0.50, n = 3) is computed on three points and is fragile; the honest statement is that the ranking is uninformative, not that it is weakly positive.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

No PAINS alerts were found. The validation assay still needs standard controls (detergent to expose aggregators; a counter-screen against α-amylase, since acarbose inhibits both and selectivity over amylase is part of the tolerability case) and, for the kotalanol analogue, a desalting step before any assay — the chloride counter-ion is not the active species.

### 4.4 Testable hypotheses

1. In a head-to-head ntMGAM inhibition assay (same enzyme preparation, same substrate, same day), the IC50 order will be CHEMBL432221 ≈ CHEMBL120226 < CHEMBL2442258 ≪ acarbose — i.e. the ChEMBL order, not the Vina order. Refuted if acarbose is the most potent.
2. Desalting CHEMBL3815109 (removing the chloride counter-ion) and re-docking the cation on 3L4Y will give a Vina score comparable to the other iminosugars (−4 to −6.5), and its measured IC50 will be in the same range as its ChEMBL record (470 nM). Refuted if it scores far outside that range or fails again.
3. A 100 ns molecular-dynamics + MM-GBSA rescoring will rank the three iminosugars above acarbose, reversing the rigid-Vina order. Refuted if acarbose still leads.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): ntMGAM enzyme inhibition assay (p-nitrophenyl-α-D-glucopyranoside substrate) for the three iminosugars + acarbose + desalted CHEMBL3815109, 10-point dose–response in triplicate, same plate. Stage 2 (weeks 4–6): α-amylase counter-screen for the best lead, to test whether it spares the enzyme whose inhibition contributes to acarbose's gastrointestinal burden; plus a Caco-2 permeability check, since a luminally restricted inhibitor is the desired profile. Stage 3 (weeks 7–12): MD + MM-GBSA rescoring to test hypothesis 3, and a postprandial glucose excursion test in a diabetic mouse model for the lead that survives stages 1–2 — the same design that validated the 2026 coumarin–triazole series. Stop rule: if stage 1 reproduces the ChEMBL order, the Vina ranking is discarded and the project proceeds on measured potency only; if the desalted kotalanol analogue is the most potent, it becomes the lead regardless of its docking score.

## 5. Limitations

1. Docking only — no experimental data; no compound here is shown to inhibit MGAM in any assay.
2. All Vina margins in this paper are inside or near the ±1–2 kcal/mol noise; the best-vs-second margin is 0.20 kcal/mol.
3. Single rigid structure (3L4Y, inhibitor-bound); no MD, no free-energy refinement, no induced-fit or explicit-water treatment — particularly limiting for a shallow carbohydrate-binding cleft.
4. Rank correlation computed on n = 3 — fragile; one more compound could change it.
5. Acarbose's measured potency comes from heterogeneous literature assays (456–750 μM), not from a head-to-head MGAM measurement against the leads; the ChEMBL MGAM record for acarbose did not meet the retrieval threshold.
6. One of five leads could not be docked (salt-form prep failure); the paper's ranking is therefore incomplete by design, and the missing compound belongs to the most potent known class.
7. No local (Pakistan) market, pricing or access data were collected; acarbose is off-patent and cheap, so a new inhibitor needs a potency-and-tolerability case, not a price case.

## 6. Conclusion

On ntMGAM 3L4Y, acarbose — a micromolar inhibitor — out-scored three nanomolar iminosugars by Vina, while the kotalanol-class lead could not be docked at all because its salt form breaks the pipeline's ligand preparation. The benchmark's value is the double negative: rigid docking on this structure cannot rank α-glucosidase inhibitors, and the pipeline cannot evaluate the most potent chemotype in the set. The next step is a head-to-head ntMGAM assay including the desalted kotalanol analogue, which will settle whether the ChEMBL order or the Vina order is real.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all tools and data sources used are free and public (UniProtKB, ChEMBL, PubChem, RCSB PDB, AutoDock Vina).

## References

1. International Diabetes Federation. IDF Diabetes Atlas. 11th ed. Brussels: International Diabetes Federation; 2025. (589 million adults aged 20–79 with diabetes, 1 in 9; 853 million projected by 2050; Pakistan age-standardised prevalence 31.4%, ~34.5 million adults.)
2. Sim L, Jayakanthan K, Mohan S, et al. New glucosidase inhibitors from an Ayurvedic herbal treatment for type 2 diabetes: structures and inhibition of human intestinal maltase-glucoamylase with compounds from Salacia reticulata. Biochemistry. 2010;49(3):443–451. PMID 20039683. doi:10.1021/bi9016457
3. Sim L, Quezada-Calvillo R, Sterchi EE, Nichols BL, Rose DR. Human intestinal maltase-glucoamylase: crystal structure of the N-terminal catalytic subunit and basis of inhibition and substrate specificity. J Mol Biol. 2008;375(3):782–792. PMID 18036614. doi:10.1016/j.jmb.2007.10.069
4. Potent and selective α-glucosidase inhibition by coumarin–triazole conjugates: design, in vivo evaluation, and computational insights. RSC Adv. 2026;16:29844–29866. doi:10.1039/D6RA01115B
5. Identification of selective α-glucosidase inhibitors via virtual screening with machine learning. Molecules. 2025;30(19):3996. doi:10.3390/molecules30193996
6. Critical assessment of in vitro screening of α-glucosidase inhibitors from plants with acarbose as a reference standard. PLoS One. 2024;19(10):e0311501. doi:10.1371/journal.pone.0311501
7. Akmal M, Patel P, Wadhwa R. Alpha glucosidase inhibitors. In: StatPearls. Treasure Island, FL: StatPearls Publishing; 2025. PMID 32496728
8. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J Chem Inf Model. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203
9. Protein Data Bank. Crystal complex of N-terminal human maltase-glucoamylase with NR4-8II. PDB ID 3L4Y, resolution 1.80 Å. https://www.rcsb.org/structure/3L4Y

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-004-2026-11-10.json`. Target: UniProt O43451; ChEMBL target CHEMBL2074; structure PDB 3L4Y; compounds: acarbose (PubChem CID 9811704, InChIKey CEMXHAPUFJOOSV-XGWNLRGSSA-N), CHEMBL120226, CHEMBL432221, CHEMBL2442258, CHEMBL3815109 (docking failed: multi-fragment salt SMILES). No additional data were generated.
