# MRTX1133 Re-Docks at −12.71 kcal/mol on the KRAS G12D Switch-II Pocket and Sotorasib Scores Worst: A Corrected Docking Benchmark After a Wrong-Target Pipeline Run

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-15 · **Health Papers Agent — Paper #60** (daily 5-paper run)

**Keywords:** KRAS G12D; MRTX1133; sotorasib; switch-II pocket; molecular docking; AutoDock Vina; pancreatic cancer

---

## Abstract

KRAS G12D is the commonest KRAS allele, driving about 42% of KRAS-mutant pancreatic cancers, and it has no approved inhibitor: the covalent KRAS G12C drugs cannot work because G12D has no cysteine to bind. MRTX1133 is the first non-covalent, selective KRAS G12D inhibitor, with a pERK IC50 of 2 nM in AGS cells, but the standard pipeline run for this paper resolved the target to the wrong enzyme and docked it into the wrong pocket, so both numbers from that run are discarded here and the correction is documented in full. We docked MRTX1133, three analogues from the same discovery paper, and the G12C inhibitor sotorasib as a negative control with AutoDock Vina 1.2.7 on 7RPZ, the 1.3 angstrom KRAS G12D structure co-crystallised with MRTX1133 in the switch-II pocket. MRTX1133 re-docked at minus 12.71 kcal/mol; the analogues scored minus 11.62, minus 11.13 and minus 9.34 against measured pERK IC50s of 24, 530 and 24 nM; sotorasib scored worst at minus 7.74, as a G12C drug should on G12D. Rank correlation against measured potency is moderate (Spearman rho 0.65, n = 4), but two compounds with identical measured potency differ by 2.28 kcal/mol in docking, and the re-dock sits 2.52 kcal/mol clear of its own second pose. The screen ranks the series roughly right and cannot resolve equal potencies. The falsifiable next step is a single-assay pERK comparison of the four Wang-series compounds in one KRAS G12D cell line: if compounds 25 and 36 again measure identically while docking differs by more than 2 kcal/mol, the gap is confirmed as a scoring artefact, not a potency signal.

---

## 1. Introduction

KRAS is the most frequently mutated oncogene in human cancer, and G12D is its commonest allele — about 33% of all KRAS-mutant tumours, and about 42% of KRAS mutations in pancreatic ductal adenocarcinoma (PDAC), where roughly 93% of tumours carry a KRAS mutation. PDAC is among the most lethal common cancers, with a five-year survival rate in single digits, and KRAS G12D has been called undruggable for decades: the protein binds GDP/GTP with picomolar affinity, leaving no obvious pocket, and unlike G12C it offers no reactive cysteine for a covalent warhead. The G12C inhibitors sotorasib and adagrasib proved that the induced switch-II pocket could be drugged, but they depend on Cys12 and are inactive against G12D. MRTX1133, reported by Wang et al. in 2022, was the first non-covalent, potent and selective KRAS G12D inhibitor: an estimated KD of about 0.0002 nM against KRAS G12D, an AlphaLISA IC50 of 5 nM, a pERK IC50 of 2 nM and a 2D-viability IC50 of 6 nM in AGS cells, with more than 500-fold selectivity over wild-type KRAS (MKN1 viability IC50 above 3,000 nM), and 94% growth inhibition with tumour regressions in a Panc 04.03 xenograft at 30 mg/kg twice daily. Its phase 1/2 trial (NCT05737706) was later terminated before phase 2, and a 2026 study reported antimetastatic effects in a liver-metastatic PDAC model (Sci Rep 2026;16:4144). The follow-up candidates now include the covalent G12D inhibitor RMC-9805 and the PROTAC ASP3082, but no KRAS G12D drug is approved.

The question this paper tests is whether a standard rigid-docking screen can rank a congeneric KRAS G12D series — the same scaffold, the same pocket, potencies spanning 2 to 530 nM — and whether it can recognise a negative control. The test is strict because the series comes from one paper with one assay, so the measured ranking is as clean as published data gets. A second, methodological question is also answered here: the standard pipeline run for this topic failed twice (Section 2.2), and the correction is part of the paper, not hidden in a supplement.

**Hypothesis (falsifiable):** under one standardised protocol on the MRTX1133 co-crystal structure, docking rank will track the measured pERK ranking (MRTX1133 first, compound 15 last), and sotorasib will score worst, because it has no covalent anchor and no measurable G12D activity. Falsified if two compounds with identical measured potency differ by more than Vina noise, or if sotorasib scores within noise of the actives.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-15 (web search; PubMed; the daily digest of 2026-11-14, which screened 722 candidates and selected 8 — none on KRAS, so the digest's relevance here is methodological). Key sources: Wang et al. 2022 (J Med Chem 65:3123–3133, PMID 34889605) for the MRTX1133 discovery, all measured potencies, and structures 7RPZ/7RT1/7RT2/7RT5; the 2025 Cancers review of KRAS-mutant pancreatic cancer (Cancers 2025;17:2453, doi:10.3390/cancers17152453) for the clinical context and the NCT05737706 status; the 2024 Clin Cancer Res review of MRTX1133 (Clin Cancer Res 2024;30:655–662, doi:10.1158/1078-0432.CCR-23-2098) for the PDAC mutation frequencies; and the 2026 Scientific Reports antimetastatic study (Sci Rep 2026;16:4144, PMID 41501279). Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Pipeline failure and correction

The standard LeadForge pipeline was run with target "KRAS G12D" and reference drug MRTX1133 (run_docking.py, RDKit venv, NO_PROXY prefix). It failed in two independent ways, and both numbers from that run are DISCARDED (kept in `hidden_files/dock-HP-069-2026-11-15.json` for audit only).

First, the target resolution: UniProt returned the TrEMBL entry A0ABF7PHA5 for the KRAS G12D variant, which has no ChEMBL target mapping, so the pipeline's fallback picked the first text-search candidate — CHEMBL2074, maltase-glucoamylase. The four "leads" it retrieved are silylated iminosugars (alpha-glucosidase inhibitors, Ki 4–28 nM against maltase-glucoamylase), not KRAS ligands at all.

Second, the structure and centre: the pipeline picked 9S84 (KRAS G12D D38C, GDP-bound, 1.64 angstrom — the protein is correct) but `_ligand_center` fell back to the GDP centroid, because GDP is the only HETATM group with six or more atoms once cofactors are excluded. That is the nucleotide pocket, not the switch-II pocket where MRTX1133 binds. The MRTX1133 score of −9.13 on 9S84 is therefore meaningless, and the iminosugar scores (−6.13 to −7.69) are scores of the wrong molecules in the wrong pocket.

The correction (documented fallback, HP-027 precedent; script `health-papers-agent/dock_kras_7rpz_correction.py`) uses structure 7RPZ — KRAS G12D in complex with MRTX1133, 1.3 angstrom (Wang et al. 2022) — with the centre from `D._ligand_center`, the centroid of the co-crystallised MRTX1133 in the switch-II pocket. The centre [1.71, 4.93, −23.16] was audited: 9.55 angstrom from the Asp12 alpha carbon (the mutant residue's side chain points into the pocket) and 17.81 angstrom from the GDP centroid, confirming the box sits on the switch-II pocket and not on the nucleotide site.

### 2.3 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; one box (22.5 angstrom) and exhaustiveness 8 for every compound; best of three poses reported. Five compounds on 7RPZ: MRTX1133 (reference drug; SMILES PubChem-verified by the pipeline run, formula C33H31F3N6O2, MW 600.65) and three analogues from Wang et al. 2022 — compound 25 (the eutomer of the 24/25 pair, co-crystal 7RT2), compound 36 (co-crystal 7RT5) and compound 15 (co-crystal 7RT1) — plus sotorasib (PubChem CID 137278711) as the negative control. The three analogues' SMILES were obtained from the RCSB chemical-component InChI for their co-crystal ligands (7NL, 7OE, 7L8) and verified by molecular-formula match (C31H32F2N6O2, C33H32F2N6O, C29H31FN6O2); a first attempt to extract SMILES from the deposited PDB coordinates produced wrong, saturated structures and was discarded. Measured potencies are all pERK AGS IC50s from Wang et al. 2022 (same assay, same paper): MRTX1133 2 nM; 25: 24 nM; 36: 24 nM; 15: 530 nM. Sotorasib carries no measured G12D potency and is excluded from the rank correlation.

### 2.4 PAINS screen

RDKit PAINS filter applied to every compound. All five are PAINS-clean. MRTX1133 carries one Lipinski violation (MW 600.65); compound 36 carries one (logP 5.05); the other three pass Lipinski and Veber outright.

### 2.5 Rank correlation

Spearman rank correlation was computed between the Vina scores and the measured pERK IC50 values for the four Wang-series compounds (n = 4). The two tied measured values (24 nM, twice) were assigned the average rank 2.5. A correlation on four points is reported as a descriptive check, not as a validated ranking — the paper's real tests are the 25/36 pair and the sotorasib negative control.

### 2.6 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol; gaps smaller than that are not differences. MRTX1133's score is a re-dock on its own co-crystal structure (7RPZ), so the pocket is shaped for it — that advantage is reported, not hidden. The measured IC50s are cellular pERK values from one paper, not biochemical KDs, and they conflate binding with cell permeability; the KD ranking (MRTX1133 ~0.0002 nM, compound 15 0.8 nM, compound 5B 3.5 µM) is quoted in the text but the correlation uses the single-assay pERK values. No molecular dynamics or free-energy refinement was run. No compound was assayed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured pERK AGS IC50 | Vina on 7RPZ (kcal/mol) | PAINS |
|---|---|---|---|
| MRTX1133 (reference) | 2 nM | **−12.71** (−12.71, −10.19, −10.03) | clean |
| Compound 36 | 24 nM | −11.62 (−11.62, −10.74, −9.89) | clean |
| Compound 15 | 530 nM | −11.13 (−11.13, −9.82, −9.13) | clean |
| Compound 25 | 24 nM | −9.34 (−9.34, −9.27, −9.00) | clean |
| Sotorasib (negative control) | no G12D activity | −7.74 (−7.74, −7.63, −7.49) | clean |

Scores in kcal/mol, best of three poses (all three poses in parentheses). Measured IC50s are pERK AGS values from Wang et al. 2022.

MRTX1133 is first by 1.09 kcal/mol over compound 36, and sotorasib is last by 1.60 kcal/mol behind compound 25 — the negative control behaves as it should. The ranking is roughly right. But the middle of the table is wrong in a specific way: compounds 25 and 36 have identical measured potency (24 nM) yet differ by 2.28 kcal/mol in docking, more than Vina noise; and compound 15, the weakest measured (530 nM, 22-fold weaker than 25), docks better than 25 by 1.79 kcal/mol. The screen gets the ends right and the middle wrong.

### 3.2 Rank correlation: moderate, and carried by the extremes

Against the measured pERK IC50s, Spearman rho is 0.65 (n = 4). The value is carried by MRTX1133 sitting first and compound 15 sitting last in the measured ranking while docking puts 15 third; remove the two extremes and the remaining pair (25 vs 36) is ranked backwards by 2.28 kcal/mol. A correlation of 0.65 on four points, with the tied pair inverted, is not a validated ranking — it is a screen that works at the extremes and fails in the middle, which is where a real screening programme makes its decisions.

### 3.3 The re-dock advantage

MRTX1133's best pose (−12.71) sits 2.52 kcal/mol clear of its second pose (−10.19), while the other compounds' poses are tightly grouped (compound 25's three poses span only 0.34 kcal/mol). The 7RPZ pocket was crystallised around MRTX1133, and the scoring function rewards that fit heavily — the same pocket-shape effect reported for ponatinib on 3OXZ in Paper #58. The −12.71 value is therefore partly a pocket-shape effect, not a pure affinity signal, and the 1.09 kcal/mol gap to compound 36 is inside the range that effect can produce. A fair comparison would re-dock each compound into its own co-crystal structure (7RT1/7RT2/7RT5 exist for exactly this purpose); that cross-structure comparison was not run here, and the paper does not pretend the single-structure ranking is final.

### 3.4 The 25/36 pair: what docking misses

Compounds 25 and 36 differ in the naphthyl substituent: 36 carries the optimised 7-fluoro-8-ethynylnaphthyl group that fills a hydrophobic pocket near Val9, Thr58, Phe78, Met72, Tyr96 and Ile100 and engages the conserved water network, while 25 carries a naphthalen-2-ol. The paper that discovered them reports that the 8-ethynyl group bridges the lipophilic and polar regions of the switch-II pocket through a non-classical hydrogen bond to the conserved water. Rigid docking scores 36 better than 25 by 2.28 kcal/mol, which is the right direction for the wrong reason if the water network is the mechanism — Vina's scoring of water-mediated contacts is crude, and the paper cannot tell from these numbers whether the gap reflects the water interaction or a pose artefact. What it can say is that two compounds the assay cannot distinguish are distinguished by the screen by more than noise, so the screen is resolving something the assay does not — and that something is as likely to be error as signal.

### 3.5 ADMET and safety panel

All five compounds are PAINS-clean. The Tox21 kNN read-across panel was not run for the three analogues (they are not in the pipeline's lead set); the pipeline's panel for MRTX1133 flags nothing decisive (highest signals SR-ARE 0.20, NR-AhR 0.18). The safety story that matters for this target is clinical, not computational: MRTX1133's phase 1/2 trial was terminated before phase 2, with pharmacokinetic variability and suboptimal exposure reported as the reason — a reminder that a picomolar KD does not make a drug. The three analogues are research compounds with no approval and no human safety data.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say two things with confidence: MRTX1133 binds its own pocket better than its analogues do, in the same direction as its measured potency; and sotorasib, a G12C drug, scores worst on G12D, as it should. It cannot say that compound 36 is better than compound 25 — the assay says they are equal, and the 2.28 kcal/mol docking gap is an unvalidated claim. Nor can it say that compound 15 is nearly as good as compound 36 — the assay says it is 22-fold weaker, and docking puts them 0.49 kcal/mol apart, inside noise. The screen is a validated positive control with a failed middle: useful for confirming MRTX1133 and rejecting sotorasib, useless for ranking the analogues against each other.

### 4.2 The pipeline failure is the second finding

The standard pipeline run failed twice on this topic — wrong enzyme (maltase-glucoamylase) and wrong pocket (GDP site) — and both failures were silent: the run exited 0, printed "PIPELINE OK: True", and saved a JSON with confident-looking numbers. The failure modes are systematic, not one-off: a TrEMBL accession with no ChEMBL mapping falls back to the first text-search candidate, and a structure whose only ligand is a cofactor falls back to the cofactor centroid. Any pipeline that can fail this quietly needs a target-identity check (does the ChEMBL target name match the query?) and a pocket check (is the centre within 10 angstrom of a catalytic or known-ligand residue?) before any number is trusted. This paper is the control experiment that shows why.

### 4.3 Testable hypotheses

1. **Equal-potency hypothesis.** In one pERK assay on AGS cells, compounds 25 and 36 again measure within 2-fold of each other while their Vina scores on 7RPZ differ by more than 2 kcal/mol. Falsified if 36 measures more than 5-fold more potent than 25 — in which case the docking gap is real and the assay, not the screen, missed it.
2. **Cross-structure hypothesis.** Re-docking each compound into its own co-crystal structure (15 into 7RT1, 25 into 7RT2, 36 into 7RT5) restores the measured ranking (36 and 25 tied, 15 last). Falsified if the ranking is unchanged — in which case the single-structure result is not a pocket-shape artefact.
3. **Sotorasib hypothesis.** Sotorasib shows no measurable pERK inhibition in AGS cells at 10 µM. Falsified if it inhibits pERK by more than 50% at that concentration — in which case the negative control is not negative and the G12C/G12D selectivity claim needs revisiting.

### 4.4 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain MRTX1133, compounds 25, 36 and 15, and sotorasib; confirm identity and purity by LC-MS and NMR. Stage 2 (weeks 3–6): pERK assay on AGS cells, all five compounds on the same plates, in triplicate — the single-assay comparison this paper could not make, and the direct test of hypothesis 1. Stage 3 (weeks 7–10): cross-structure re-docking for hypothesis 2, plus a 2D-viability assay on AGS and on MKN1 (wild-type KRAS) for selectivity. Stage 4 (weeks 11–12): if any analogue measures within 2-fold of MRTX1133 on pERK, dock its analogues and synthesise the best two; if all three are more than 10-fold weaker, report the negative result and stop. Sample-size logic: three independent biological replicates per IC50 determination is the minimum for a defensible potency claim; the 25-versus-36 comparison needs the same, because a false "36 is better" call on a tied pair is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. MRTX1133's score is a re-dock on its own co-crystal structure (7RPZ); the three analogues are cross-docked into a pocket shaped for MRTX1133.
3. The measured IC50s are cellular pERK values from one paper, conflating binding with permeability; the KD ranking is quoted but not used for the correlation.
4. Spearman rho is computed on four points with a tie; it is a descriptive check, not a validated ranking.
5. The pipeline run's numbers are discarded, not corrected in place; the corrected docking is a separate script and file, and the two must not be mixed.
6. No molecular dynamics, flexible-side-chain docking, or free-energy refinement was run — the methods that could actually price the water network in the switch-II pocket.
7. Sotorasib's negative-control status rests on the absence of reported G12D activity, not on a measured G12D IC50 in this paper.
8. The phase 1/2 termination reason (pharmacokinetic variability, suboptimal exposure) is as reported in secondary sources; the primary trial record states the status, not the reason.
9. No Pakistan-specific access or burden data are cited; the paper's relevance to Pakistan is methodological — a cheap, open-source triage step a university lab can run before any assay.

## 6. Conclusion

On 7RPZ, MRTX1133 re-docks at −12.71 kcal/mol, and three analogues from the same discovery paper score −11.62, −11.13 and −9.34 against measured pERK IC50s of 24, 530 and 24 nM, with sotorasib worst at −7.74 as a G12C drug should be on G12D. The ranking is roughly right (Spearman rho 0.65) but two compounds the assay cannot distinguish differ by 2.28 kcal/mol in docking, and the re-dock sits 2.52 kcal/mol clear of its own second pose. The screen validates MRTX1133 and the negative control and fails in the middle, where real screening decisions are made. The next step is the single-assay pERK comparison in Section 4.4, with all four Wang-series compounds and sotorasib on the same plates — and, as a standing rule, no pipeline docking number is trusted until the target name and the pocket have both been checked against the query.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Wang X, Allen S, Blake JF, et al. Identification of MRTX1133, a noncovalent, potent, and selective KRAS G12D inhibitor. J Med Chem. 2022;65(4):3123–3133. PMID: 34889605. doi:10.1021/acs.jmedchem.1c01688.
2. Treatment of KRAS-mutated pancreatic cancer: new hope for the patients? Cancers. 2025;17(15):2453. doi:10.3390/cancers17152453.
3. A small molecule with big impact: MRTX1133 targets the KRAS G12D mutation in pancreatic cancer. Clin Cancer Res. 2024;30(4):655–662. doi:10.1158/1078-0432.CCR-23-2098.
4. Antimetastatic effects of MRTX1133 KRAS G12D specific inhibitor in a liver metastatic model of pancreatic ductal adenocarcinoma. Sci Rep. 2026;16(1):4144. PMID: 41501279. doi:10.1038/s41598-025-34204-y.
5. UniProtKB. GTPase KRAS, G12D variant, A0ABF7PHA5; canonical KRAS, P01116. Accessed 2026-11-15. https://www.uniprot.org/uniprotkb/A0ABF7PHA5/entry
6. RCSB Protein Data Bank. Structures 7RPZ (KRAS G12D with MRTX1133, 1.3 A), 7RT1, 7RT2, 7RT5, 9S84 (KRAS G12D D38C, GDP-bound, 1.64 A). Accessed 2026-11-15. https://www.rcsb.org/structure/7RPZ
7. ChEMBL. Target CHEMBL2074 (maltase-glucoamylase, Homo sapiens) — the wrong target the pipeline picked; the KRAS G12D ligands in this paper are from Wang et al. 2022, not from ChEMBL. Accessed 2026-11-15. https://www.ebi.ac.uk/chembl/
8. PubChem. MRTX1133, CID 156124857; sotorasib, CID 137278711. Accessed 2026-11-15. https://pubchem.ncbi.nlm.nih.gov/compound/137278711
9. ClinicalTrials.gov. NCT05737706, MRTX1133 phase 1/2 in KRAS G12D-mutant advanced solid tumours (terminated). Accessed 2026-11-15. https://clinicaltrials.gov/study/NCT05737706

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-069-2026-11-15-7RPZ.json` (corrected docking on 7RPZ); the discarded pipeline run is in `hidden_files/dock-HP-069-2026-11-15.json` (wrong ChEMBL target, GDP-pocket centre — do not use its numbers). The correction script is `health-papers-agent/dock_kras_7rpz_correction.py`. PDB IDs 7RPZ/7RT1/7RT2/7RT5/9S84, RCSB chemical-component IDs 7L8/7NL/7OE/6IC, and the PubChem CID for sotorasib are given in the text. No additional data were generated.
