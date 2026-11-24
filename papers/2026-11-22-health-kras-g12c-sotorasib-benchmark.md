# Sotorasib Self-Docks at −8.71 kcal/mol on Its Own KRAS G12C Structure — but Vina Scores Only the Non-Covalent Pose, and the 4.77 kcal/mol Cross-Dock Spread Is a Pocket Artefact

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-22 · **Health Papers Agent — Paper #99** (daily 5-paper run)

**Keywords:** KRAS G12C; sotorasib; covalent inhibitor; lung cancer; molecular docking; AutoDock Vina; ChEMBL; switch-II pocket

---

## Abstract

KRAS was considered undruggable for decades until covalent inhibitors of the G12C mutant reached the clinic; sotorasib received FDA accelerated approval on 28 May 2021, with a 37.1% objective response rate in CodeBreaK 100. We asked whether Vina docking on the sotorasib-bound KRAS G12C structure ranks known KRAS G12C inhibitors by their measured potency. The pipeline resolved KRAS (UniProtKB P01116) to ChEMBL CHEMBL2189121, retrieved 51 bioactivities, and ranked 26 leads; docking ran on 6OIM (KRAS G12C covalently bound to sotorasib, 1.65 Å) and on 9IAY (GDP-KRAS in complex with a different inhibitor, 0.953 Å). On 6OIM, sotorasib self-docked at −8.71 kcal/mol and the four analogues scored −8.20 to −9.21, a 1.01 kcal/mol spread for compounds spanning 0.3–0.6 nM — docking cannot separate them. On the cross-dock structure 9IAY the spread exploded to 4.77 kcal/mol, with sotorasib worst at −7.54 and an analogue best at −12.31. The cross-dock spread is a pocket artefact, not a potency signal, and Vina cannot model the covalent bond to Cys12 that gives these drugs their potency, so every score here is a non-covalent pose score only. The falsifier is a covalent docking or free-energy calculation (or a head-to-head biochemical assay with fixed pre-incubation time) of sotorasib, CHEMBL5892737 and CHEMBL5905084 under identical conditions: if the covalent-aware ranking does not separate the 0.3 nM compound from the 0.6 nM compound, the docking approach is confirmed uninformative for this series, and future KRAS G12C work must use covalent-aware methods from the start.

---

## 1. Introduction

KRAS mutations occur in 43% of lung adenocarcinomas, and the G12C mutation accounts for about 13% of lung adenocarcinomas. For decades KRAS was called undruggable: the protein lacks a deep pocket, and its picomolar affinity for GTP seemed to rule out competitive inhibition. The breakthrough was the switch-II pocket, a shallow groove that opens only in the GDP-bound state, and the cysteine at position 12, which the G12C mutation places within reach of a covalent warhead. Sotorasib (AMG 510) exploits both: it binds the switch-II pocket and forms a covalent bond to Cys12, locking KRAS in its inactive GDP-bound state.

Sotorasib received FDA accelerated approval on 28 May 2021 for KRAS G12C-mutated non-small-cell lung cancer. In the CodeBreaK 100 phase II trial the objective response rate was 37.1%, median overall survival 12.5 months, median progression-free survival 6.8 months and median duration of response 11.1 months; the two-year analysis (Dy et al., J Clin Oncol 2023) reported a 41% response rate, 12.5 months median overall survival and 33% two-year overall survival. Resistance emerges through secondary KRAS mutations, bypass signalling and histological transformation, and newer covalent G12C inhibitors are in development. This paper tests one falsifiable hypothesis: **Vina docking on the sotorasib-bound KRAS G12C structure (6OIM) ranks known KRAS G12C inhibitors in the same order as their measured potency.** The falsifier is stated in the Abstract.

## 2. Methods

### 2.1 Literature basis

Sources verified on 22 November 2026: Hong et al., N Engl J Med 2020;383:1207–17 (first-in-human sotorasib, PMID 32955176, doi:10.1056/NEJMoa1917239); Dy et al., J Clin Oncol 2023;41:3311–17 (two-year CodeBreaK 100 outcomes, PMID 37098232, doi:10.1200/JCO.22.02524); FDA accelerated approval 28 May 2021; ChEMBL bioactivities for KRAS (CHEMBL2189121), retrieved live. The Islamic literature sweep found no canonical work that addresses KRAS or covalent oncology drugs: the classical authors described tumours and their treatment, but the gene, the mutation and the drug are all modern, so no classical source can inform the docking question; this is recorded as a limitation, not hidden.

### 2.2 Molecular docking

The standardised AutoDock Vina protocol of Papers #1 and #3 was used. Target: human KRAS, UniProtKB P01116, resolved live to ChEMBL CHEMBL2189121 (SINGLE PROTEIN, *Homo sapiens*), 51 bioactivities, 26 leads after similarity screening. Two structures were docked. **6OIM** (human KRAS G12C covalently bound to AMG 510/sotorasib, 1.65 Å): the grid centre [1.87, −8.26, −1.36] is the centroid of the co-crystallised sotorasib ligand (HETATM group MOV, 41 atoms), computed with `dock._ligand_center`, which excludes GDP, the magnesium ion and waters — the centre audit is mandatory after the TYK2 wrong-domain precedent. **9IAY** (GDP-KRAS in complex with inhibitor "10", 0.953 Å): centre [21.83, −0.61, 4.76], the compound-10 centroid; this is a cross-dock for sotorasib, not its own structure. Box 22.5 Å on both. Best of three poses reported; the reference drug and the analogues were docked under the identical protocol on each structure. Ligands: sotorasib (PubChem CID 137278711) and ChEMBL leads with their ChEMBL activities. **Covalent caveat:** sotorasib and the four analogues are covalent G12C inhibitors whose potency comes from bond formation with Cys12. Vina does not model covalent bond formation; every score in this paper is therefore a non-covalent pose score, and the covalent contribution is invisible to the method.

### 2.3 PAINS screen

RDKit PAINS filter applied to every compound. All five compounds reported here are PAINS-clean.

### 2.4 Honesty limits

Docking is not activity, and for covalent inhibitors it is not even a complete affinity estimate. Vina's scoring noise is ±1–2 kcal/mol, so gaps smaller than ~1 kcal/mol cannot rank compounds. No experimental data were generated; no covalent docking, molecular dynamics or free-energy refinement was run.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured activity (ChEMBL) | 6OIM best affinity (kcal/mol) | 6OIM poses | 9IAY best affinity (kcal/mol) | 9IAY poses | PAINS |
|---|---|---|---|---|---|---|
| Sotorasib (reference) | — | −8.71 | −8.71, −8.65, −8.35 | −7.54 | −7.54, −7.53, −7.44 | clean |
| CHEMBL5892737 | Kd 0.3 nM | −9.21 | −9.21, −8.97, −8.82 | −11.66 | −11.66, −10.43, −10.07 | clean |
| CHEMBL5905084 | IC50 0.4 nM | −8.20 | −8.20, −8.03, −7.91 | −12.31 | −12.31, −11.11, −10.16 | clean |
| CHEMBL5948638 | IC50 0.5 nM | −8.96 | −8.96, −8.95, −8.16 | −10.50 | −10.50, −10.16, −9.20 | clean |
| CHEMBL4876243 | IC50 0.6 nM | −8.57 | −8.57, −8.49, −8.24 | −10.61 | −10.61, −10.28, −10.26 | clean |

On the self-dock structure 6OIM, the five compounds score within 1.01 kcal/mol of each other (−9.21 to −8.20) while their measured potencies span 0.3–0.6 nM. The most potent, CHEMBL5892737 (Kd 0.3 nM), scores best (−9.21), but the second-most-potent, CHEMBL5905084 (IC50 0.4 nM), scores worst (−8.20). The ranking is a null: docking cannot separate sub-nanomolar covalent inhibitors by non-covalent pose score, and the 1.01 kcal/mol spread is inside Vina's noise.

On the cross-dock structure 9IAY the picture is dramatically different — and misleading. The spread explodes to 4.77 kcal/mol: CHEMBL5905084 scores −12.31, CHEMBL5892737 −11.66, and sotorasib worst at −7.54. Sotorasib's three 9IAY poses are nearly identical (−7.54, −7.53, −7.44), which suggests Vina found only one shallow minimum for it in the compound-10 pocket. A reader who saw only the 9IAY table would conclude sotorasib is a poor binder and CHEMBL5905084 is a breakthrough — both conclusions are artefacts of the pocket, not of the molecules. The 6OIM table corrects them: on sotorasib's own structure, the five compounds are indistinguishable.

### 3.2 Compound properties

| Compound | MW | logP | HBD | HBA | Rotatable bonds | TPSA (Å²) | Lipinski violations | Veber | Tox21 max |
|---|---|---|---|---|---|---|---|---|---|
| Sotorasib | 560.61 | 4.48 | 1 | 7 | 5 | 104.45 | 1 | pass | 0.599 |
| CHEMBL5892737 | 549.05 | 4.67 | 2 | 8 | 5 | 86.64 | 1 | pass | 0.214 |
| CHEMBL5905084 | 549.05 | 4.76 | 2 | 8 | 5 | 86.64 | 1 | pass | 0.197 |
| CHEMBL5948638 | 540.64 | 4.64 | 2 | 8 | 5 | 86.64 | 1 | pass | 0.232 |
| CHEMBL4876243 | 588.66 | 4.40 | 2 | 9 | 6 | 95.87 | 1 | pass | 0.370 |

All five are close analogues by properties (MW 540–589, logP 4.40–4.76, 5–6 rotatable bonds, one Lipinski violation each, Veber pass). Sotorasib's Tox21 kNN maximum of 0.599 is the highest in the set and above 0.5, the only compound in this run's five papers to cross that threshold; the analogues sit at 0.197–0.370. All are PAINS-clean.

### 3.3 Comparison with published docking

No published Vina benchmark of sotorasib against these specific ChEMBL analogues on 6OIM was found in the literature sweep; the numbers here are the first report of this comparison. The 6OIM structure itself is the published sotorasib complex. The covalent nature of these inhibitors is well established in the literature, and the non-covalent-only limitation of Vina for this series is a known methods gap, not a new finding — the new finding is how large the cross-dock artefact is (4.77 kcal/mol) relative to the true spread (1.01 kcal/mol).

## 4. Discussion

### 4.1 The reframe

The question was whether docking can rank KRAS G12C inhibitors. The answer is no, twice over. On the right structure, the scores are too close to separate (a null). On the wrong structure, the scores separate dramatically — and wrongly (an artefact). The 9IAY table is the most dangerous result in this run's five papers, because it looks like a discovery: a 4.77 kcal/mol spread with a clear winner. It is not a discovery. It is the pocket of a different inhibitor doing the ranking.

### 4.2 Why the "win" must not be over-read

CHEMBL5905084's −12.31 on 9IAY must not be quoted as a finding. On 6OIM it scores −8.20, the worst of the five. Its 9IAY advantage comes from fitting the compound-10 pocket, not from binding KRAS G12C better. Equally, sotorasib's −7.54 on 9IAY must not be quoted as a failure: on its own structure it scores −8.71, and its clinical efficacy is established by trial data, not by any docking score. The covalent bond to Cys12 — the source of these drugs' potency — is invisible to Vina, so the method cannot, even in principle, rank this series by affinity.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five compounds are PAINS-clean, so the validation assay does not need redox and aggregation controls. The assay's controls instead need to cover the known confounder for covalent inhibitors: time-dependent inhibition. IC50 values for covalent drugs depend on pre-incubation time, so the validation design must fix the incubation time and report it, and must include a non-covalent control (a warhead-free analogue) to separate the covalent contribution from the pose contribution.

### 4.4 Testable hypotheses

1. Covalent docking (or a free-energy calculation that includes the Cys12 bond) ranks CHEMBL5892737 (Kd 0.3 nM) ahead of CHEMBL4876243 (IC50 0.6 nM) by more than 1 kcal/mol. Settled by the covalent-aware calculation.
2. A head-to-head biochemical assay with fixed pre-incubation time reproduces the ChEMBL potencies (0.3–0.6 nM) for all five compounds, confirming that the 6OIM null is correct and the 9IAY spread is an artefact.
3. A warhead-free analogue of sotorasib docks at the same −8.71 on 6OIM but shows no KRAS G12C inhibition in assay, confirming that the covalent bond, not the pose, carries the potency.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): source the five compounds (commercial, ≥95% purity) and recombinant KRAS G12C (GDP-loaded); set up a nucleotide-exchange or SOS1-mediated exchange assay with sotorasib as the internal control and a fixed pre-incubation time. Stage 2 (weeks 3–6): dose–response curves for all five compounds in triplicate, same plate, same incubation time; report IC50 with 95% confidence intervals. Stage 3 (weeks 7–8): repeat with a second KRAS G12C lot and a warhead-free sotorasib analogue as the non-covalent control. Stage 4 (weeks 9–12): covalent docking of the top two compounds on 6OIM to check whether the covalent-aware ranking separates them.

## 5. Limitations

1. Docking only — no experimental data; Vina cannot model the covalent Cys12 bond, so every score here omits the main source of these drugs' potency.
2. Vina noise ±1–2 kcal/mol; the 6OIM spread (1.01 kcal/mol) is inside the noise.
3. Single-structure analysis per compound set; no covalent docking, molecular dynamics or free-energy refinement was run.
4. ChEMBL activities come from different assays and laboratories, and covalent IC50 values depend on pre-incubation time, which was not standardised across the source assays — the head-to-head assay is the correction.
5. No canonical Islamic medical work addresses KRAS or covalent oncology drugs; the literature sweep covers the available digitised canon and names this gap rather than claiming a classical precedent that does not exist.
6. Nothing here supports a clinical recommendation; sotorasib's clinical record comes from the CodeBreaK trials, not from this paper.

## 6. Conclusion

Sotorasib self-docks at −8.71 kcal/mol on its own KRAS G12C structure 6OIM, and four sub-nanomolar analogues score within 1.01 kcal/mol of it — docking cannot rank this covalent series by non-covalent pose score. On the cross-dock structure 9IAY the spread explodes to 4.77 kcal/mol, a pocket artefact that would mislead any reader who quoted it. For covalent inhibitors, Vina's numbers are pose scores, not affinities. The next step is a covalent-aware calculation or a head-to-head assay with fixed pre-incubation time.

## 7. Policy implications

**Decision-maker:** the ORIC director and the laboratory supervisor at SMBBMU Larkana (Prof. Dr. Nadeem Baloch, ORIC), who control the university's small research budget. **Decision:** whether to fund the 8–12-week head-to-head KRAS G12C assay proposed in §4.5, including a warhead-free control, before any further docking work on this series. **Exact change:** approve the assay for sotorasib and the four analogues as the next funded step, capped at the cost of five commercial compounds and one recombinant KRAS G12C lot, and spend nothing on further Vina benchmarks of covalent inhibitors until a covalent-aware method is in place. **Reversal condition:** if the assay reproduces the ChEMBL potencies and the warhead-free analogue shows no inhibition, close the Vina line for covalent series and adopt covalent docking as the standard for any future KRAS work. The Islamic principle is *hifz al-nafs* (preservation of life, one of the maqasid al-sharia): lung cancer is a leading killer, and a better KRAS inhibitor would serve that end — but the same principle forbids spending scarce university funds on a ranking the paper itself shows is an artefact, and forbids any clinical claim before the assay exists.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content.

## References

1. Hong DS, Fakih MG, Strickler JH, et al. KRAS(G12C) inhibition with sotorasib in advanced solid tumors. N Engl J Med. 2020;383(13):1207–17. doi:10.1056/NEJMoa1917239. PMID 32955176.
2. Dy GK, Govindan R, Velcheti V, et al. Long-term outcomes and molecular correlates of sotorasib efficacy in patients with KRAS G12C-mutated non-small-cell lung cancer: 2-year analysis of CodeBreaK 100. J Clin Oncol. 2023;41(17):3311–17. doi:10.1200/JCO.22.02524. PMID 37098232.
3. US Food and Drug Administration. FDA grants accelerated approval to sotorasib for KRAS G12C mutated NSCLC. 28 May 2021. https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-sotorasib-kras-g12c-mutated-nsclc
4. ChEMBL. GTPase KRas (CHEMBL2189121) bioactivity data, retrieved live 22 November 2026. https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2189121/
5. Protein Data Bank. 6OIM: Crystal structure of human KRAS G12C covalently bound to AMG 510, 1.65 Å. https://www.rcsb.org/structure/6OIM
6. Protein Data Bank. 9IAY: Structure of compound 10 in complex with GDP-KRAS, 0.953 Å. https://www.rcsb.org/structure/9IAY

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-081-2026-11-22.json` (pipeline: ChEMBL CHEMBL2189121, 51 bioactivities, 26 leads; 9IAY cross-dock) and `hidden_files/dock-HP-081-6oim-2026-11-22.json` (6OIM self-dock, centre [1.87, −8.26, −1.36]). Ligands: sotorasib PubChem CID 137278711; CHEMBL5892737, CHEMBL5905084, CHEMBL5948638, CHEMBL4876243 (ChEMBL). Target: human KRAS, UniProtKB P01116. No additional data were generated.
