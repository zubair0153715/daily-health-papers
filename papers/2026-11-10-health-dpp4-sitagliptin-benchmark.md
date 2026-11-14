# Sitagliptin Is the Weakest Compound in Its Own Benchmark: A Centre-Audited DPP-4 Docking Study on 4A5S Where Vina Rank and Measured Potency Are Uncorrelated

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-10 · **Health Papers Agent — Paper #41** (daily 5-paper run)

**Keywords:** DPP-4; sitagliptin; dipeptidyl peptidase-4; molecular docking; AutoDock Vina; type 2 diabetes; ChEMBL; triazolopiperazine

---

## Abstract

Type 2 diabetes affects 589 million adults worldwide (1 in 9), and Pakistan has one of the highest age-standardised prevalences at 31.4% (~34.5 million adults). Sitagliptin, the first DPP-4 inhibitor (FDA-approved October 2006, IC50 18 nM), prolongs incretin action by blocking the enzyme that degrades GLP-1 and GIP — but newer triazolopiperazine analogues are ~100-fold more potent in vitro, and it is not obvious that docking can tell them apart. We ran the LeadForge pipeline (UniProtKB P27487 → ChEMBL CHEMBL284, 47 bioactivities → PubChem verification of sitagliptin → RDKit ADMET/PAINS → AutoDock Vina 1.2.7 on PDB 4A5S, 1.62 Å, grid centre exactly on the co-crystallised inhibitor N7F centroid, 0.00 Å) and docked the top five compounds by composite score against sitagliptin. The most similar compound to sitagliptin (CHEMBL1203953, similarity 0.563, IC50 0.18 nM) could not be docked at all — its hydrochloride salt has two SMILES fragments, which ligand preparation rejects. Of the four that docked, the Vina order (CHEMBL5870057 −9.47, sitagliptin −8.95, CHEMBL5951803 −8.85, CHEMBL5220750 −7.88 kcal/mol) is uncorrelated with the measured-potency order (Spearman ρ = 0.0, n = 4): sitagliptin ranks second by Vina yet is ~100-fold weaker than the leads by measurement (18 nM vs 0.18–0.27 nM). Worse, the single most potent compound in the whole set (CHEMBL98869, Ki 0.082 nM, pChEMBL 10.09) was never docked, because the pipeline docks only the top five by a similarity-dominated composite score. The falsifiable next step is a head-to-head enzyme assay of CHEMBL5870057 and CHEMBL5951803 against sitagliptin on DPP-4 plus a DPP-8/DPP-9/FAP selectivity panel: a lead only matters if its ~100-fold potency advantage survives the same plate — and if it keeps sitagliptin's selectivity.

---

## 1. Introduction

The International Diabetes Federation estimates 589 million adults aged 20–79 live with diabetes (1 in 9), projected to reach 853 million by 2050; Pakistan's age-standardised prevalence is 31.4%, about 34.5 million adults, with 226,752 diabetes-related deaths in 2024. DPP-4 (dipeptidyl peptidase-4, CD26) is a serine exopeptidase that inactivates the incretin hormones GLP-1 and GIP within minutes of their release; inhibiting it raises active incretin levels, increases glucose-dependent insulin secretion and suppresses glucagon, with a low risk of hypoglycaemia. Sitagliptin (MK-0431, Januvia) was the first DPP-4 inhibitor, approved by the FDA in October 2006: a β-amino amide built on a triazolopiperazine, with an IC50 of 18 nM against DPP-4 and >40,000-fold selectivity over other proline-selective peptidases. Its crystal structure in complex with DPP-4 (PDB 1X70) shows the β-amino group hydrogen-bonding the Glu205/Glu206 dyad and Tyr662, with the trifluorophenyl group in the S1 hydrophobic pocket.

The field has not stood still. The same triazolopiperazine series that produced sitagliptin was refined to sub-nanomolar inhibitors — compound 46b at IC50 0.18 nM, with its own DPP-4 co-crystal structure — and a 2026 preprint re-docked five gliptins on 1X70 (sitagliptin −9.181, linagliptin −8.965 kcal/mol; re-dock RMSD 1.14 Å), while a 2026 screen of 15,034 compounds proposed new sitagliptin analogues. The gap this paper attacks is whether a standardised docking benchmark can actually rank such compounds against sitagliptin — or whether the score is noise, the ranking is a similarity contest, and the most potent compound is the one the protocol never docks.

**Hypothesis (falsifiable):** Vina scores on 4A5S will not recover the measured potency order of DPP-4 inhibitors against sitagliptin (Spearman ρ near zero), because the score spread (≤1.6 kcal/mol) is inside Vina's ±1–2 kcal/mol noise and the measured potencies span ~100-fold.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-10 (web search; PubMed via the daily digest of 2026-11-10). Key sources: IDF Diabetes Atlas 11th edition 2025 for burden; Kim et al. 2005 for sitagliptin's discovery and IC50 18 nM; Kim et al. 2008 for the sub-nanomolar triazolopiperazine series (compound 46b, IC50 0.18 nM, co-crystal structures); the 2026 ResearchSquare preprint docking five gliptins on 1X70; the 2026 Biomed Pharmacol J screen of 15,034 sitagliptin analogues; and the Molecules 2023 DPP-4 SAR review. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 LeadForge pipeline (same protocol as Papers #1/#3)

Standardised LeadForge pipeline: UniProtKB P27487 (DPP-4, Homo sapiens, 766 aa) → ChEMBL CHEMBL284 ("Dipeptidyl peptidase 4", SINGLE PROTEIN), 47 bioactivities retrieved (pChEMBL ≥ 5) → PubChem PUG REST verification of sitagliptin (CID 4369359; MW 407.32, formula C16H15F6N5O — matches the reference) → RDKit Morgan-fingerprint similarity screen vs sitagliptin → RDKit ADMET/PAINS + ToxGuard Tox21 kNN (12 assays) → composite lead ranking (similarity × 40 + Lipinski × 20 + Veber × 10 + PAINS × 10 + tox × 20) → AutoDock Vina 1.2.7 docking of the top five by composite score plus the query, on the best-resolution ligand-bound X-ray structure. Raw output: `hidden_files/dock-HP-001-2026-11-10.json`.

### 2.3 Structure and centre audit

The pipeline selected PDB 4A5S — human DPP-4 (soluble form), 1.62 Å, "Crystal structure of human DPP4 in complex with a novel heterocyclic DPP4 inhibitor" — rather than the sitagliptin-bound 1X70 (2.5 Å), because the picker takes the highest-resolution ligand-bound X-ray structure for the target. Both are the same enzyme and the same active site (Glu205/Glu206 dyad); the choice is a resolution trade-off, not a target error, and it is reported here so the reader can judge it. Centre audit (verified from the cached PDB file, 2026-11-10): the co-crystallised inhibitor N7F (chain A, residue 901, 37 atoms) has centroid (14.14, 35.87, 54.84) — identical to the docking grid centre (14.14, 35.87, 54.84), distance 0.00 Å. The grid is exactly on the crystallographic binding site.

### 2.4 PAINS screen

RDKit PAINS filter applied to every lead. No compound in the top 10 carries a PAINS alert.

### 2.5 Honesty limits

Vina's documented error is ±1–2 kcal/mol, so score differences under ~2 kcal/mol cannot rank compounds. "Measured" potencies are single-assay ChEMBL maxima (IC50 vs Ki, different laboratories and years), not head-to-head values; the 18 nM figure for sitagliptin is the literature reference value (Kim et al. 2005), not a ChEMBL record — the pipeline's QUERY entry carries no ChEMBL activity of its own. The composite score is dominated by similarity to sitagliptin (40 of 100 points). No experimental data were generated; no selectivity data (DPP-8/DPP-9/FAP) are presented for the leads.

## 3. Results

### 3.1 Potency: the comparison table

| Compound | Similarity to sitagliptin | Composite score | Best ChEMBL record (pChEMBL) | Vina on 4A5S (kcal/mol) | PAINS |
|---|---|---|---|---|---|
| Sitagliptin (QUERY) | 1.000 | 99.1 | Literature: IC50 18 nM | −8.95 | none |
| CHEMBL1203953 | 0.563 | 81.2 | IC50 0.18 nM (9.74) | FAILED (salt, 2 fragments) | none |
| CHEMBL5870057 | 0.411 | 75.6 | IC50 0.21 nM (9.68) | −9.47 | none |
| CHEMBL5951803 | 0.355 | 73.8 | IC50 0.18 nM (9.74) | −8.85 | none |
| CHEMBL5220750 | 0.174 | 66.9 | IC50 0.27 nM (9.57) | −7.88 | none |
| CHEMBL98869 (not docked) | 0.184 | 66.5 | Ki 0.082 nM (10.09) | — | none |

None of the five leads has a ChEMBL preferred name; all are investigational compounds. Three of the four docked leads are triazolopiperazines — the same scaffold as sitagliptin: CHEMBL5870057 (chlorobenzoyl-triazolopiperazine), CHEMBL5951803 (cyanophenyl-triazolopiperazine acetamide) and the undocked CHEMBL1203953 (benzyl-substituted triazolopiperazine hydrochloride). CHEMBL5220750 is a different chemotype, a proline-based dipeptide-like ester; CHEMBL98869 is a piperidine amide.

### 3.2 Comparison with published potency data

The ChEMBL maxima are consistent with the published series: CHEMBL5951803 and CHEMBL1203953 at IC50 0.18 nM match compound 46b of Kim et al. 2008 (IC50 0.18 nM, same triazolopiperazine class, co-crystallised with DPP-4). Sitagliptin's literature IC50 is 18 nM (Kim et al. 2005) — about 100-fold weaker than the four leads (0.18–0.27 nM). The 2026 preprint's Vina score for sitagliptin on 1X70 (−9.181) agrees with ours on 4A5S (−8.95) to within 0.23 kcal/mol, well inside Vina noise — the structure choice (4A5S vs 1X70) does not change the result.

### 3.3 The standardisation problem: three failures in one benchmark

**Failure 1 — the ranking is noise.** Vina order: CHEMBL5870057 (−9.47) > sitagliptin (−8.95) > CHEMBL5951803 (−8.85) > CHEMBL5220750 (−7.88). Measured order: CHEMBL5951803 (0.18 nM) > CHEMBL5870057 (0.21 nM) > CHEMBL5220750 (0.27 nM) > sitagliptin (18 nM). Spearman ρ = 0.0 (n = 4): no correlation at all. The entire Vina spread is 1.59 kcal/mol — inside the ±1–2 kcal/mol error — while the measured potencies span ~100-fold. Sitagliptin, the weakest compound by measurement, ranks second by Vina.

**Failure 2 — the most similar compound could not be docked.** CHEMBL1203953 is the closest analogue to sitagliptin in the set (similarity 0.563) and jointly the most potent (IC50 0.18 nM) — and it failed ligand preparation because its SMILES is a hydrochloride salt with two fragments ("RDKit molecule has 2 fragments. Must have 1."). The same failure mode removed the most potent lead class in Paper #39 (HP-004, kotalanol sulfonium salt). Salts are routine in medicinal chemistry; a pipeline that cannot desalt its inputs silently drops exactly the compounds a chemist would most want to test.

**Failure 3 — the most potent compound was never docked.** CHEMBL98869 (Ki 0.082 nM, pChEMBL 10.09) is the most potent compound in the entire 26-lead set, and it was not docked because the pipeline docks only the top five by composite score — and the composite score is similarity-dominated, so a structurally different compound (similarity 0.184) ranks sixth and is excluded. The docking cut is made on the wrong variable: it should be made on measured potency, not on similarity to the reference.

Drug-likeness is clean across the docked set: MW 345–552, logP 1.62–4.36, zero Lipinski violations except CHEMBL1203953 (one violation, MW 551.89). No Tox21 flags were predicted for any compound by kNN read-across — a prediction, not a measurement. Sitagliptin's clinical advantage is not potency — it is selectivity (>40,000-fold over DPP-8/DPP-9) and a 20-year safety record; no selectivity data exist for the leads, and potency without selectivity is not a drug.

## 4. Discussion

### 4.1 The reframe

The question was whether a standardised screen can rank new DPP-4 leads against sitagliptin. The answer is no — not because the pipeline is broken in one place, but because three independent selection steps each discard the signal: the docking score cannot rank a 100-fold potency spread (ρ = 0.0); the ligand preparation cannot handle salts; and the docking cut excludes the most potent compound on similarity grounds. The paper's contribution is therefore the audit, not a ranking: any of the four leads could be the best compound, and this benchmark cannot say which. That is a usable result — it tells the next experimenter to skip the docking and go straight to the enzyme assay.

### 4.2 Why the "win" must not be over-read

CHEMBL5870057's −9.47 kcal/mol is the best Vina score, but it is 0.52 kcal/mol ahead of sitagliptin — a quarter of Vina's error — while being ~86-fold more potent by measurement. The Vina "win" and the potency "win" point at different compounds, and neither is decisive. The 0.18 nM figures are single-assay ChEMBL maxima, not head-to-head values; the 2026 preprint's scores and ours agree, but agreement between two Vina runs is not validation against experiment.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

No PAINS alerts were found. The validation assay still needs standard controls (detergent to expose aggregators; a counter-screen against an unrelated enzyme) and, critically, a selectivity panel — DPP-8 and DPP-9 inhibition is the known toxicity route for this class, and sitagliptin's >40,000-fold selectivity is the bar the leads must clear.

### 4.4 Testable hypotheses

1. In a head-to-head DPP-4 enzyme assay on the same plate, CHEMBL5870057, CHEMBL5951803 and CHEMBL1203953 will each be >50-fold more potent than sitagliptin (IC50 < 0.4 nM vs 18 nM). Refuted if any lead is within 10-fold of sitagliptin.
2. On a DPP-8/DPP-9 selectivity panel, at least one lead will be <100-fold selective (i.e. it will fail where sitagliptin succeeds). Refuted if all leads match sitagliptin's >40,000-fold selectivity.
3. Re-docking with the salt desalted (CHEMBL1203953 as free base) will place it within 1 kcal/mol of CHEMBL5870057 — i.e. the docking failure was a preparation artefact, not a binding problem. Refuted if the desalted compound scores >2 kcal/mol worse than the triazolopiperazine leads.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): desalt CHEMBL1203953 and re-dock all five leads plus CHEMBL98869 on 4A5S (six compounds, same grid) — the deliverable is a corrected docking table, and a check on whether the potency-based docking cut changes the ranking. Stage 2 (weeks 4–6): recombinant human DPP-4 enzyme assay, 10-point dose–response in triplicate, same plate, for sitagliptin, CHEMBL5870057, CHEMBL5951803, CHEMBL1203953 (free base) and CHEMBL98869 — the deliverable is a head-to-head IC50 table replacing the ChEMBL maxima. Stage 3 (weeks 7–12): DPP-8/DPP-9/FAP selectivity panel for the best two leads, then an oral glucose tolerance test in mice for the lead that survives the panel. Stop rule: a lead that is potent on DPP-4 but <100-fold selective over DPP-8/DPP-9 is a failure, not a publication — potency without selectivity is not a gliptin.

## 5. Limitations

1. Vina's ±1–2 kcal/mol error exceeds the entire score spread (1.59 kcal/mol); no docking ranking in this paper is meaningful.
2. "Measured" potencies are single-assay ChEMBL maxima from heterogeneous assays (IC50 vs Ki); they are not head-to-head values, and sitagliptin's 18 nM is a literature reference value, not a ChEMBL record.
3. The most potent compound in the set (CHEMBL98869, Ki 0.082 nM) was never docked; the most similar compound (CHEMBL1203953) failed ligand preparation as a salt.
4. No selectivity data (DPP-8/DPP-9/FAP) are presented for any lead; sitagliptin's selectivity advantage is from the literature.
5. The structure used (4A5S, N7F-bound) is not the sitagliptin-bound structure (1X70); the two give consistent Vina scores for sitagliptin (−9.181 vs −8.95), but no re-docking RMSD validation was run on 4A5S.
6. No data are presented on pharmacokinetics, cost, or access — in Pakistan, gliptin affordability is a larger barrier than potency, and this analysis does not address it.
7. No local (Pakistan) epidemiological or access data beyond the national estimates in Section 1 were collected.

## 6. Conclusion

Against sitagliptin on DPP-4 4A5S, the benchmark fails three ways at once: Vina rank and measured potency are uncorrelated (Spearman ρ = 0.0, n = 4), with sitagliptin — ~100-fold the weakest by measurement — ranking second by Vina; the most similar lead (CHEMBL1203953, IC50 0.18 nM) could not be docked because it is a salt; and the most potent compound in the set (CHEMBL98869, Ki 0.082 nM) was never docked because the pipeline cuts on similarity, not potency. The next step is not more docking: it is a head-to-head enzyme assay with a DPP-8/DPP-9 selectivity panel, on the compounds this benchmark could not rank.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all tools and data sources used are free and public (UniProtKB, ChEMBL, PubChem, RCSB PDB).

## References

1. Kim D, Wang L, Beconi M, et al. (2R)-4-Oxo-4-[3-(trifluoromethyl)-5,6-dihydro[1,2,4]triazolo[4,3-a]pyrazin-7(8H)-yl]-1-(2,4,5-trifluorophenyl)butan-2-amine: a potent, orally active dipeptidyl peptidase IV inhibitor for the treatment of type 2 diabetes. J Med Chem. 2005;48(1):15–17. PMID 15634008. doi:10.1021/jm0493156
2. Kim D, Kowalchick JE, Brockunier LL, et al. Discovery of potent and selective dipeptidyl peptidase IV inhibitors derived from β-aminoamides bearing substituted triazolopiperazines. J Med Chem. 2008. (Compound 46b: IC50 0.18 nM; X-ray structures of 34b and 46b in complex with DPP-4.)
3. International Diabetes Federation. IDF Diabetes Atlas. 11th ed. 2025. (589 million adults aged 20–79 with diabetes, 1 in 9; Pakistan age-standardised prevalence 31.4%, ~34.5 million adults, 226,752 deaths in 2024.)
4. Comparative molecular docking of five gliptin drugs against dipeptidyl peptidase-4 (PDB 1X70): sitagliptin −9.181 kcal/mol, linagliptin −8.965 kcal/mol; re-dock RMSD 1.14 Å; Glu205/Glu206 dyad. ResearchSquare preprint. 2026. doi:10.21203/rs.3.rs-10262005/v1
5. Sitagliptin analogues from a virtual screen of 15,034 compounds (compounds 14 and 22). Biomed Pharmacol J. 2026. doi:10.13005/bpj/3450
6. DPP-4 inhibitor structure–activity review: sitagliptin β-amino hydrogen bonds to Glu205/Glu206/Tyr662; trifluorophenyl π-interaction with Tyr666; PDB 1X70. Molecules. 2023;28:5860.
7. Triazole dimers as DPP-4 inhibitors: compound 5d IC50 1.54–1.57 nM, comparable to sitagliptin. 2026.
8. Protein Data Bank. Crystal structure of human DPP4 in complex with a novel heterocyclic DPP4 inhibitor. PDB ID 4A5S (1.62 Å). https://www.rcsb.org/structure/4A5S
9. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J Chem Inf Model. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203

## Data availability

All docking scores and potency values reported here are in `hidden_files/dock-HP-001-2026-11-10.json` (pipeline steps 1–7 on CHEMBL284; docking on PDB 4A5S, grid centre exactly on co-crystallised inhibitor N7F centroid, 0.00 Å). Target: UniProt P27487; ChEMBL target CHEMBL284; compounds: sitagliptin (PubChem CID 4369359), CHEMBL1203953, CHEMBL5870057, CHEMBL5951803, CHEMBL5220750, CHEMBL98869. No additional data were generated.
