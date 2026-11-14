# Vemurafenib Still Docks Best: Five Sub-nanomolar BRAF V600E Inhibitors Dock Worse Than the Drug They Outperform by ~300-Fold

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification.**

**Author:** Zubair Ali, Pharm-D student, Faculty of Pharmacy, SMBBMU, Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-04
**Paper:** #9 (Health Papers series, 2026-11-04, fifth of the day)

## Abstract

BRAF V600E drives about half of metastatic melanomas, and vemurafenib, the first inhibitor approved for it, extended median overall survival to 13.6 months in the BRIM-3 trial — but roughly 15% of patients never respond and about half of responders acquire resistance within 6–8 months. We asked whether standardised docking against the V600E kinase domain could rank five known sub-nanomolar BRAF inhibitors against vemurafenib. Compounds came from ChEMBL bioactivities against BRAF (CHEMBL5145), were screened with RDKit (Lipinski/Veber/PAINS) and a Tox21 kNN panel, and were docked with AutoDock Vina 1.2.7 into the BRAF V600E kinase domain (PDB 3OG7, 2.45 Å, co-crystallised with vemurafenib itself), under an identical protocol. The pipeline's first automated structure was wrong — a 14-3-3/BRAF-phosphopeptide complex, not the kinase domain — and its scores were discarded. On 3OG7, vemurafenib docked best (−11.52 kcal/mol) and the best-measured lead, CHEMBL3651664 (IC50 0.08 nM), docked fifth (−10.18 kcal/mol); the five leads measure 0.08–0.13 nM, roughly 240–390-fold more potent than vemurafenib's 31 nM, yet none out-docked it, and the docking order showed no positive correlation with measured potency (Spearman ρ = −0.21, n = 6). The falsifiable next step is a head-to-head BRAF V600E enzyme assay for CHEMBL3651664 and CHEMBL3752213 against vemurafenib under identical conditions: if the ChEMBL values hold, CHEMBL3651664 will inhibit at sub-nanomolar concentration while vemurafenib needs ~30 nM, and any docking-based claim to the contrary should be discarded.

**Keywords:** BRAF V600E; melanoma; vemurafenib; molecular docking; AutoDock Vina; kinase inhibitor; paradoxical activation; drug resistance

## Introduction

Melanoma of the skin caused an estimated 331,722 new cases and 58,667 deaths worldwide in 2022 (GLOBOCAN 2022), and its incidence continues to rise. About half of metastatic melanomas carry a BRAF mutation, and the V600E substitution — valine to glutamic acid at residue 600, mimicking activation-loop phosphorylation — accounts for 70–88% of BRAF mutations, producing a constitutively active kinase that drives the MAPK pathway (RAS–RAF–MEK–ERK) independent of upstream signals.

Vemurafenib (PLX4032), an ATP-competitive type I½ BRAF inhibitor, was the first drug approved for BRAF V600E melanoma. In the BRIM-3 phase III trial it improved median progression-free survival to 6.9 months and median overall survival to 13.6 months versus dacarbazine chemotherapy, with response rates near 50%. The benefit is real but short-lived: about 15% of patients show primary resistance, and among responders about half develop acquired resistance after a median of 6–8 months, through NRAS or MEK secondary mutations, BRAF amplification, the p61 BRAF V600E splice variant that dimerises independently of RAS, receptor-tyrosine-kinase upregulation, or PI3K/AKT activation. BRAF plus MEK inhibition (dabrafenib + trametinib, vemurafenib + cobimetinib, encorafenib + binimetinib) extends median overall survival beyond 25 months and is now standard, but resistance still arrives, and the search for better BRAF inhibitors continues.

A second, structural problem shadows vemurafenib: as a type I½ inhibitor it stabilises the αC-helix OUT in one protomer of the RAF dimer, which promotes dimerisation and paradoxically activates ERK in cells with wild-type BRAF or mutant RAS — the mechanism behind its cutaneous squamous-cell carcinoma toxicity. Any ranking of new BRAF inhibitors therefore has to be judged against measured potency, not against a docking score alone, and docking against a vemurafenib-shaped pocket carries an obvious bias: the pocket was crystallised around vemurafenib itself.

This paper tests that bias directly. We take five ChEMBL compounds with measured BRAF IC50 values of 0.08–0.13 nM — roughly 240–390-fold more potent than vemurafenib's 31 nM — and dock them, with vemurafenib, into the BRAF V600E kinase domain under one standardised protocol. The question is narrow and falsifiable: does the docking score order match the measured potency order?

## Methods

### Target and compound selection

The target was human BRAF, resolved by gene symbol to UniProt P15056 (serine/threonine-protein kinase B-raf) and ChEMBL CHEMBL5145 (SINGLE PROTEIN, Homo sapiens). Compounds were drawn from ChEMBL bioactivities against CHEMBL5145, screened by RDKit Morgan-fingerprint similarity to vemurafenib (Tanimoto), Lipinski and Veber drug-likeness, PAINS filters, and a Tox21 kNN read-across panel (12 assays), then ranked by a composite score (similarity × 40 + Lipinski × 20 + Veber × 10 + PAINS × 10 + tox × 20). Vemurafenib itself was included as the QUERY reference (PubChem-verified SMILES, MW 489.93, logP 5.54). The five distinct leads were CHEMBL3651664, CHEMBL3651680, CHEMBL2047875, CHEMBL3752213 and CHEMBL3651701. Measured IC50 values were retrieved from the ChEMBL activity API for each compound against CHEMBL5145 (see Results).

### Structure selection — the automated pick was wrong

The pipeline's automated structure picker selected PDB 8VSO (1.5 Å) and centred the grid on a phosphoserine residue. Inspection of the entry showed 8VSO is a ternary complex of 14-3-3 sigma, a BRAF phosphopeptide (pS365) and compound 78 — it contains no BRAF kinase domain at all, so docking a kinase inhibitor into its phosphopeptide groove is meaningless. All 8VSO scores were discarded and are not reported as results.

The structure used instead is PDB 3OG7, "B-Raf Kinase V600E oncogenic mutant in complex with PLX4032" (2.45 Å), the vemurafenib-bound V600E kinase domain. Residue 600 is glutamic acid in chain B, confirming the V600E mutant. The grid was centred on the co-crystallised PLX4032 ligand (code 032, chain A) centroid [1.87, −2.64, −19.92].

### Docking protocol

AutoDock Vina 1.2.7, box 22.5 Å, exhaustiveness 8, 3 poses per ligand, identical for all six compounds. Receptor and ligands were prepared with the same RDKit/meeko pipeline used throughout this series. Vina carries ±1–2 kcal/mol noise; differences inside that band are not rankings.

### Statistics

Spearman rank correlation between the docking-score order and the measured-IC50 order was computed from the six paired ranks.

## Results

### The five leads are measured sub-nanomolar; vemurafenib is not

Measured BRAF IC50 values (ChEMBL, against CHEMBL5145):

| Compound | Measured BRAF IC50 | Assay / source |
|---|---|---|
| CHEMBL3651664 | 0.08 nM | Raf/MEK AlphaScreen (CHEMBL3639377) |
| CHEMBL3752213 | 0.10 nM | LanthaScreen (CHEMBL3751850) |
| CHEMBL3651680 | 0.11 nM | Raf/MEK AlphaScreen (CHEMBL3639377) |
| CHEMBL2047875 | 0.11 nM | B-raf V600E enzyme assay (CHEMBL2046386); pERK IC50 2.5 nM |
| CHEMBL3651701 | 0.13 nM | Raf/MEK AlphaScreen (CHEMBL3639377) |
| Vemurafenib (QUERY) | 31 nM | Discovery report (Bollag et al., 2010); wild-type BRAF 100 nM |

Three of the five leads (CHEMBL3651664, CHEMBL3651680, CHEMBL3651701) share a sulfonamide-bearing aminopyrimidine scaffold from a single source series; CHEMBL2047875 is a quinazoline-4-amine amide and CHEMBL3752213 a quinoline sulfonamide. All five are PAINS-clean. Drug-likeness: CHEMBL3752213 carries one Lipinski violation (MW 522.57); vemurafenib carries one (logP 5.54); the other four pass Lipinski with zero violations. Tox21 read-across maxima are low (0.17–0.40 across the 12 assays; highest single value 0.40, SR-MMP, for CHEMBL3752213).

### Docking: vemurafenib wins; the best-measured lead ranks fifth

Docking scores against BRAF V600E (PDB 3OG7, Vina 1.2.7), best pose [all three poses]:

| Compound | Docking score (kcal/mol) | Measured IC50 |
|---|---|---|
| Vemurafenib (QUERY) | **−11.52** [−11.52, −10.82, −10.71] | 31 nM |
| CHEMBL3752213 | −11.17 [−11.17, −10.11, −9.88] | 0.10 nM |
| CHEMBL2047875 | −10.48 [−10.48, −10.47, −10.09] | 0.11 nM |
| CHEMBL3651680 | −10.19 [−10.19, −8.77, −8.71] | 0.11 nM |
| CHEMBL3651664 | −10.18 [−10.18, −8.44, −8.40] | 0.08 nM |
| CHEMBL3651701 | −8.80 [−8.80, −8.80, −8.66] | 0.13 nM |

Vemurafenib, the worst-measured compound by a factor of ~240–390, docked best. CHEMBL3651664, the best-measured compound, docked fifth of six, 1.34 kcal/mol behind vemurafenib. CHEMBL3651701, measured at 0.13 nM, docked worst by a wide margin (−8.80 kcal/mol, 2.72 kcal/mol behind vemurafenib — beyond Vina's noise band, so the mis-ranking is confident, not marginal). The docking order shows no positive correlation with measured potency: Spearman ρ = −0.21 (n = 6).

## Discussion

This is the cleanest negative result in this series: the docking ranking is not merely noisy, it is inverted at the extremes. Three points follow.

**First, the co-crystallised ligand wins its own pocket.** 3OG7 was crystallised around vemurafenib; the ATP pocket in that structure is moulded to vemurafenib's shape, including the αC-OUT/DFG-IN conformation characteristic of type I½ inhibitors. Re-docking vemurafenib into its own pocket is close to a self-consistency check, and it scores best. The five leads, built on different scaffolds, pay a penalty for a pocket that was never shaped for them. Any benchmark that docks candidates into a structure co-crystallised with the reference drug inherits this bias, and the bias is invisible unless the measured values are placed beside the scores — as they are here.

**Second, the inversion is large enough to matter.** A 2.72 kcal/mol gap between vemurafenib and CHEMBL3651701 exceeds Vina's ±1–2 kcal/mol noise, so a naive reader would confidently discard CHEMBL3651701 — a compound measured at 0.13 nM, ~240-fold more potent than vemurafenib. The same pattern, in milder form, appeared in this series' COX-2 paper (docking selectivity did not track measured selectivity). Docking scores are a shape-complementarity heuristic for one static conformation; they do not encode induced fit, the dimer interface, or the paradoxical activation that defines this drug class.

**Third, nothing here is a drug candidate yet.** All five leads are enzyme-potent but unproven in cells (only CHEMBL2047875 carries a cellular read-out, pERK IC50 2.5 nM), with no data on BRAF selectivity versus CRAF/ARAF, no data on the p61 splice variant or NRAS-mutant backgrounds where paradoxical activation matters, and no pharmacokinetic data. Their value is as a test set: any method that claims to rank BRAF inhibitors should be required to reproduce the measured order — vemurafenib last — before it is trusted to rank unknowns.

The honest reading of this paper is therefore a warning label for the rest of the series: when a docking score and a measured IC50 disagree, the measurement wins, and when the reference drug is also the co-crystallised ligand, the docking score should be treated as a lower bound on the bias, not as evidence.

## Limitations

1. **Single static structure.** All docking used one conformation (3OG7, αC-OUT/DFG-IN). BRAF samples multiple conformations, and type I, type I½ and type II inhibitors prefer different ones; a compound that binds another conformation well will score poorly here.
2. **Co-crystallised-ligand bias.** The pocket is vemurafenib-shaped (see Discussion); the ranking cannot be read as an intrinsic potency ranking.
3. **No dimer or paradoxical activation.** Vina docks a monomer; it cannot capture RAF dimerisation, negative allostery, or paradoxical ERK activation — the properties that distinguish useful BRAF inhibitors from toxic ones.
4. **Assay heterogeneity.** Measured IC50 values come from different assay formats (AlphaScreen, LanthaScreen, fluorescence-based enzyme assays) across different source documents; the 0.08–0.13 nM cluster is tight, but cross-assay comparisons of that size should be confirmed in one assay (see Conclusion).
5. **No laboratory data.** No compound in this paper has been synthesised, assayed or tested in cells by us; all measured values are ChEMBL records, and all docking is computation.
6. **Vina noise.** ±1–2 kcal/mol; only gaps beyond that band (e.g. vemurafenib vs CHEMBL3651701) support a confident ordering claim.

## Conclusion

Five ChEMBL compounds measure 0.08–0.13 nM against BRAF — roughly 240–390-fold more potent than vemurafenib's 31 nM — yet none out-docked vemurafenib against the BRAF V600E kinase domain, and the docking order correlated negatively with measured potency (Spearman ρ = −0.21). The falsifiable next step is a head-to-head BRAF V600E enzyme assay for CHEMBL3651664 and CHEMBL3752213 against vemurafenib under identical conditions: if the ChEMBL values hold, CHEMBL3651664 will inhibit at sub-nanomolar concentration while vemurafenib needs ~30 nM. Until that assay exists, the docking scores in this paper should be read as a demonstration of co-crystallised-ligand bias, not as a ranking of these compounds.

## Acknowledgments

This manuscript was drafted with AI assistance (Lapis) under the author's direction; the author reviewed the data, the docking outputs and the cited sources. **AI disclosure:** all text, structure and interpretation were produced by an AI drafting assistant and reviewed by the author; no part of this draft has been peer-reviewed, and no laboratory work was performed for it. All docking was performed with open-source tools (RDKit, AutoDock Vina 1.2.7); compound data are from ChEMBL (EBI) and structural data from the RCSB Protein Data Bank (PDB 3OG7).

## References

1. Bollag G, Hirth P, Tsai J, et al. Clinical efficacy of a RAF inhibitor needs broad target blockade in BRAF-mutant melanoma. *Nature*. 2010;467:596–599. PMID: 20823850.
2. Chapman PB, Hauschild A, Robert C, et al. Improved survival with vemurafenib in melanoma with BRAF V600E mutation. *N Engl J Med*. 2011;364:2507–2516. PMID: 21639808.
3. Robert C, Karaszewska B, Schachter J, et al. Improved overall survival in melanoma with combined dabrafenib and trametinib. *N Engl J Med*. 2015;372:30–39.
4. Long GV, Stroyakovskiy D, Gogas H, et al. Combined BRAF and MEK inhibition versus BRAF inhibition alone in melanoma. *N Engl J Med*. 2014;371:1877–1888.
5. Karoulia Z, Gavathiotis E, Poulikakos PI. New perspectives for targeting RAF kinase in human cancer. *Nat Rev Cancer*. 2017;17:676–691.
6. Poulikakos PI, Persaud Y, Janakiraman M, et al. RAF inhibitor resistance is mediated by dimerization of aberrantly spliced BRAF(V600E). *Nature*. 2011;480:387–390.
7. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model*. 2021;61:3891–3898. PMID: 34278794.
8. GLOBOCAN 2022 melanoma burden: 331,722 new cases and 58,667 deaths worldwide. *Chin Med J*. 2025;138:185–192. PMID: 39682020. DOI: 10.1097/CM9.0000000000003416.
9. Gaulton A, Hersey A, Nowotka M, et al. The ChEMBL database in 2017. *Nucleic Acids Res*. 2017;45:D945–D954.

## Data availability

Docking inputs and outputs: `hidden_files/dock-HP-029-2026-11-04.json` (pipeline run; auto-picked PDB 8VSO, discarded — see Methods) and `hidden_files/dock-HP-029c-2026-11-04.json` (manual re-dock against PDB 3OG7, the scores reported here). Re-dock script: `health-papers-agent/redock_3og7.py`. Measured IC50 values were retrieved from the ChEMBL activity API (target CHEMBL5145) on 2026-11-04 and are reproduced in the Results table. PDB 3OG7 is available from the RCSB Protein Data Bank. No new experimental data were generated.
