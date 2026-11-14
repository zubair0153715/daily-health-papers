# Vina Ranks the Most Potent KRAS G12C Binders Last: A Centre-Audited Benchmark of Sotorasib, Adagrasib, Divarasib and Two Sub-Nanomolar ChEMBL Leads on 6OIM

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan · ORCID 0009-0001-5921-7509
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-12 · **Health Papers Agent — Paper #47** (daily paper run)

**Keywords:** KRAS G12C; sotorasib; adagrasib; divarasib; molecular docking; AutoDock Vina; covalent inhibitor; switch-II pocket; drug resistance; Y96D

---

## Abstract

KRAS G12C was the first "undruggable" oncogene to fall: the covalent switch-II pocket inhibitors sotorasib and adagrasib are FDA-approved, and divarasib is in Phase I, yet acquired resistance — most often the Y96D switch-II pocket mutation — limits their benefit, and the field still ranks new candidates with non-covalent docking scores. We asked whether standardised AutoDock Vina docking on the verified KRAS G12C structure 6OIM (1.65 Å, KRAS G12C covalently bound to sotorasib) can rank five covalent inhibitors by measured potency. The LeadForge pipeline (UniProtKB P01116, ChEMBL, PubChem, RDKit ADMET and PAINS screen, Vina 1.2.7) failed twice at target resolution — once returning zero bioactivities, once resolving KRAS to the wrong target, maltase-glucoamylase (CHEMBL2074) — so the lead set was rebuilt by direct verified queries against the correct ChEMBL target CHEMBL2189121 (4,666 activities at pChEMBL ≥ 5) plus PubChem verification of the three clinical drugs. On 6OIM, with the grid centre exactly on the co-crystallised sotorasib, Vina scored sotorasib −8.14, divarasib −8.06, adagrasib −7.58, CHEMBL4855521 −6.03 and CHEMBL4856277 −5.51 kcal/mol. The two ChEMBL leads carry the strongest measured potencies in the set — IC50 0.51 and 0.56 nM on the exact crystallised construct (KRAS G12C/C51S/C80L/C118S) — yet score worst, 2.11–2.63 kcal/mol behind sotorasib, a margin above Vina's ±1–2 kcal/mol noise. As a control, sotorasib scored −7.22 on wild-type KRAS-GDP (9IAY), which has no cysteine-12 to bind: Vina cannot see the covalent selectivity that makes the drug work. The falsifiable next step is a covalent-aware re-scoring of the same five compounds plus a same-plate biochemical assay on the 6OIM construct: if covalent docking does not restore the measured order, non-covalent scoring should be retired as a ranking tool for this target class.

---

## 1. Introduction

KRAS is the most frequently mutated oncogene in human cancer, and its glycine-12-to-cysteine mutant (G12C) occurs in approximately 12–15% of non-small cell lung cancers (NSCLC) and about 3% of colorectal cancers. For three decades KRAS was considered undruggable: the protein has no deep pocket in its active, GTP-bound state, and its affinity for GTP is picomolar. The breakthrough was the discovery of an inducible pocket in and around switch-II that exists only in the inactive, GDP-bound state, adjacent to the mutant cysteine-12. Covalent inhibitors that reach into that pocket and bond to Cys12 lock KRAS G12C in its inactive form. Two such drugs are now FDA-approved — sotorasib (Lumakras, accelerated approval 28 May 2021; CodeBreaK 100: objective response rate 37.1%, median overall survival 12.5 months in previously treated NSCLC) and adagrasib (Krazati, accelerated approval 12 December 2022; KRYSTAL-1: objective response rate 43%, median duration of response 8.5 months) — and a third, divarasib (GDC-6036), showed single-agent activity in its Phase I trial.

The benefit is real and time-limited. Acquired resistance is near-universal, and the on-target fraction clusters in the switch-II pocket itself: secondary mutations at R68, H95, Y96 and Q99. The Y96D substitution is the most frequently observed switch-II pocket mutation in post-progression cohorts (14% of patients in a 143-patient cohort carried a switch-II pocket mutation, Y96D the commonest), and in vitro Y96D/S confers resistance to both approved drugs, while G13D and R68M remain sensitive to adagrasib but not sotorasib, and Q99L is resistant to adagrasib but sensitive to sotorasib. The next generation of inhibitors must therefore be selected against this resistance landscape — and selection is exactly where the field's cheapest tool, docking, is least trustworthy. A 2026 benchmark (Pyrite, arXiv:2611.14511) showed that even expert chemists rank docking poses near chance, and a 2026 sequence-to-hits pipeline (ANTIOCH-VS, arXiv:2611.14287) shows how easily a screening campaign can now be launched from sequence alone — which makes the ranking step, not the generation step, the bottleneck. This paper tests that ranking step on the target where it matters most.

**Hypothesis (falsifiable):** under one standardised non-covalent Vina protocol on the verified KRAS G12C structure 6OIM, docking scores rank covalent KRAS G12C inhibitors in the same order as their measured potencies. The test is the within-protocol ranking of five inhibitors whose measured potencies span 0.51 nM to 11 nM, including two leads measured on the exact crystallised construct.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-12 (web search; PubMed; RCSB; ChEMBL and PubChem APIs). The daily literature digest of 2026-11-12 screened 840 candidates and contributed the two methods papers framing this study (ANTIOCH-VS and Pyrite, above). Key sources: Lanman et al. 2020 for sotorasib (J Med Chem 63:52–65); Canon et al. 2019 for the 6OIM structure (Nature 575:217–223); Skoulidis et al. 2021 for CodeBreaK 100 (N Engl J Med 384:2371–2381); Hallin et al. 2020 for adagrasib (Cancer Discov 10:54–71); Sacher et al. 2023 for divarasib (N Engl J Med 389:710–721); a 2025 molecular-dynamics and biochemical study for divarasib's nucleotide-exchange potency and its Y96D sensitivity (Sci Rep 15:24843); Tanaka et al. 2021, Koga et al. 2021 and Awad et al. 2021 for acquired resistance; Whitley et al. 2026 (Nat Commun) for the structural mechanisms of switch-II pocket resistance; and Broker et al. 2025 for the 9IAY wild-type control structure (J Med Chem 68:15649–15668). Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 The pipeline run — and its two disclosed failures

The LeadForge pipeline was run twice on 2026-11-12 (UniProtKB P01116, human GTPase KRas, 189 residues; query compound sotorasib, verified in PubChem as CID 137278711, C30H30F2N6O3). Both runs failed at the same step, in two different ways, and both failures are disclosed because they determine what this paper can and cannot claim.

**Failure 1 (first run):** target resolution by UniProt accession returned the correct ChEMBL target (CHEMBL2189121) but the bioactivity query returned zero ligands. A direct re-query of the same endpoint minutes later returned HTTP 200 with 4,666 activities — the failure was transient ChEMBL unreliability, not absence.

**Failure 2 (second run):** the by-accession endpoint returned HTTP 500, so the pipeline fell back to ChEMBL text search for "KRAS", which returned maltase-glucoamylase (CHEMBL2074) as its first hit — the same wrong target that corrupted the 2026-11-11 dengue paper's automatic run. The pipeline then retrieved 55 maltase-glucoamylase inhibitors (iminosugars; Tanimoto similarity to sotorasib ≈ 0.1) and docked five of them on the automatically picked structure. Those scores (best −9.12 kcal/mol) are meaningless for KRAS and are discarded; they do not appear in the results. The lesson, repeated from the 2026-11-11 centre audit: an automatic target or structure pick must be verified before any score is trusted.

### 2.3 The corrected benchmark

The lead set was rebuilt by direct, verified queries. ChEMBL target CHEMBL2189121 was queried for activities with pChEMBL ≥ 5 (HTTP 200; 4,666 activities). Most top hits are G12D/G12V assays, which are the wrong allele for this structure, so the set was restricted to the G12C-construct assays: the three most potent leads measured on KRAS G12C/C51S/C80L/C118S — the exact engineered construct of the 6OIM crystal structure (C51S/C80L/C118S are the structure's engineered mutations). Two could be resolved to structures: CHEMBL4855521 (IC50 0.51 nM, pChEMBL 9.29; a deuterated quinazolinone acrylamide) and CHEMBL4856277 (IC50 0.56 nM, pChEMBL 9.25). The third, CHEMBL4852458 (IC50 0.51 nM, same assay), could not be resolved: the ChEMBL molecule endpoint returned HTTP 500 on three attempts, so no SMILES is available for it. It is reported as missing, not invented. The three clinical drugs were verified in PubChem by name and CID — sotorasib CID 137278711, adagrasib CID 138611145 (C32H35ClFN7O2, MW 604.1), divarasib CID 146624881 (C29H32ClF4N7O2, MW 622.1) — and their isomeric SMILES were used for docking.

Docking used the verified structure **6OIM** (KRAS G12C covalently bound to sotorasib/AMG 510, 1.65 Å; Canon et al. 2019), not the pipeline's automatic pick. The automatic pick was **9IAY** (0.95 Å, "structure of 10 in complex with GDP-KRAS", Broker et al. 2025): its SEQADV records show no G12C mutation — it is wild-type KRAS-GDP in complex with a non-covalent pan-KRAS inhibitor (ligand WYU). Docking a G12C-selective covalent inhibitor into a wild-type structure is not a G12C benchmark, so 9IAY was demoted to a control: sotorasib was docked there once (score −7.22 kcal/mol, from the pipeline run) to test whether Vina can detect the drug's covalent selectivity.

On 6OIM, the grid centre was set exactly on the co-crystallised sotorasib (residue MOV, chain A, 41 atoms): centroid [1.87, −8.26, −1.36], computed with the pipeline's audited `dock._ligand_center`, which excludes the GDP cofactor (centroid [−6.13, 3.59, 7.31]) and waters. The audited centre was recomputed inside the docking script and matched the used centre to 0.0024 Å. Protocol, identical for all five compounds: AutoDock Vina 1.2.7, box 22.5 Å, exhaustiveness 8, best of three poses reported.

### 2.4 ADMET and PAINS screen

RDKit descriptors (molecular weight, logP, hydrogen-bond donors/acceptors, TPSA, rotatable bonds, Lipinski violations) and the PAINS filter were computed for all five compounds with the pipeline's chemistry module — the same code that scored the query compound in the pipeline run.

### 2.5 Honesty limits

Docking is not activity, and for this target the gap is structural, not statistical: **Vina is a non-covalent scorer, and all five compounds are covalent inhibitors whose potency depends on bond formation with Cys12, a term Vina cannot compute.** A Vina score here measures only non-covalent shape complementarity to the switch-II pocket. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds. One rigid structure (GDP-bound, inactive) cannot represent the GTP-bound state, the switch-II ensemble, or the resistance mutants. The measured potencies in Table 1 come from different assay types (binding Ki, nucleotide exchange, cellular signalling, ChEMBL IC50), so cross-assay ranking is indicative, not exact — except for the two ChEMBL leads, which share one assay on the exact crystallised construct. No molecular dynamics, covalent docking, or free-energy refinement was run. No experimental data were generated.

## 3. Results

### 3.1 The docking table

| Compound | Vina best (kcal/mol) | Poses (kcal/mol) | Measured potency (published / ChEMBL) | MW | logP | HBD / HBA | TPSA (Å²) | Rot. bonds | Lipinski viol. | PAINS |
|---|---|---|---|---|---|---|---|---|---|---|
| Sotorasib (re-dock) | −8.14 | −8.14, −8.06, −7.45 | Ki 11 nM (GDP-KRAS G12C); pERK IC50 68 nM; H358 IC50 0.03 μM | 560.61 | 4.48 | 1 / 7 | 104.45 | 5 | 1 | none |
| Divarasib | −8.06 | −8.06, −7.60, −7.34 | Nucleotide-exchange IC50 2.4 ± 0.2 nM; HCC1171 EC50 2 nM | 622.07 | 5.09 | 1 / 8 | 100.71 | 6 | 2 | none |
| Adagrasib | −7.58 | −7.58, −7.56, −7.55 | Cellular signalling IC50 ~5 nM; viability 10–973 nM | 604.13 | 4.73 | 0 / 8 | 88.83 | 7 | 1 | none |
| CHEMBL4855521 | −6.03 | −6.03, −5.99, −5.65 | ChEMBL IC50 0.51 nM vs KRAS G12C/C51S/C80L/C118S | 641.11 | 5.28 | 0 / 8 | 102.68 | 3 | 2 | none |
| CHEMBL4856277 | −5.51 | −5.51, −5.46, −5.40 | ChEMBL IC50 0.56 nM vs KRAS G12C/C51S/C80L/C118S | 653.11 | 5.94 | 0 / 7 | 93.45 | 3 | 2 | none |

All five compounds are PAINS-clean. All five breach Lipinski's molecular-weight or logP limits at least once — expected for switch-II pocket binders, which need size and lipophilicity to fill the pocket — so the ADMET panel does not separate them; the docking rank is the whole story.

### 3.2 The ranking is inverted for the most potent binders

The hypothesis fails. The two strongest measured binders in the set — CHEMBL4855521 and CHEMBL4856277, both sub-nanomolar on the exact crystallised construct — score worst by Vina (−6.03 and −5.51 kcal/mol), 2.11 and 2.63 kcal/mol behind sotorasib. That margin exceeds Vina's ±1–2 kcal/mol noise, so the inversion cannot be dismissed as scoring noise. Both ChEMBL leads are larger (MW 641–653 vs 561 for sotorasib) and more lipophilic (logP 5.28–5.94), with only three rotatable bonds each: their potency likely comes from a precise, rigid fit plus the covalent bond — exactly the contributions a rigid-receptor, non-covalent scorer undervalues. Within the three clinical drugs, Vina cannot separate anything: sotorasib and divarasib differ by 0.08 kcal/mol (noise), and adagrasib trails sotorasib by 0.56 kcal/mol (also noise), although divarasib's measured nucleotide-exchange potency (2.4 nM) is roughly five-fold better than sotorasib's binding Ki (11 nM) and its cellular potency is an order of magnitude better. The sotorasib re-dock (−8.14) confirms the protocol reproduces the crystal pose's pocket well; the protocol is sound — the scoring function is the problem.

### 3.3 The wild-type control: Vina cannot see covalent selectivity

Sotorasib scored −7.22 kcal/mol on wild-type KRAS-GDP (9IAY), which has no cysteine-12 for it to bond to — only 0.92 kcal/mol worse than its score on the G12C structure it was designed for, inside Vina's noise. A scorer that cannot distinguish the drug's true target from a protein it cannot covalently bind cannot rank candidates for this target class. The same blind spot explains Section 3.2: Vina rewards non-covalent complementarity and is silent on the covalent step that dominates measured potency.

## 4. Discussion

### 4.1 What this means for LeadForge and for the field

Every LeadForge paper to date has used the same Vina protocol as a ranking tool, and for non-covalent targets (FLT3, PPARγ, AmpC, the dengue protease) its failures were matters of noise or wrong structures — correctable by auditing. KRAS G12C is the first target in this series where the failure is in the physics: the scoring function lacks the term that matters most. Two practical consequences follow. First, any LeadForge run on a covalent target must pair Vina with a covalent-aware scorer (covalent docking, or a two-term score: non-covalent complementarity plus a warhead-reactivity term) before any ranking is reported; a Vina-only ranking for a covalent series is not a result, it is a shape contest. Second, the ChEMBL lane needs the same audit discipline as the structure lane: the pipeline's automatic target resolution failed twice in one day (a transient zero, then a wrong-target fallback to maltase-glucoamylase), and the wrong-target run produced confident-looking scores for the wrong enzyme. The fix applied here — direct verification of the ChEMBL target ID against the UniProt accession, and an allele check on the assays — should be a pipeline gate, not a manual rescue.

### 4.2 The literature context: ranking is the bottleneck, not generation

Today's digest makes the point from both sides. ANTIOCH-VS (Hasdemir et al. 2026) shows a complete screening campaign can now start from a protein sequence alone — generation is solved and cheap. Pyrite (Srivastava et al. 2026) shows the other side: on a 1,500-pair benchmark, even expert chemists rank docking poses near chance, and only purpose-built agents beat that bar. This paper is the same finding from inside a real campaign: the poses are easy to generate and the scores are easy to compute, and the ranking they produce is wrong for the compounds that matter most. The field's next gain is not more poses; it is scoring that knows what kind of chemistry it is scoring.

### 4.3 Resistance sets the bar for the next lead

The two ChEMBL leads are potent against the wild-type-pocket construct, but potency against today's pocket is not the selection criterion — survival against tomorrow's pocket is. Divarasib's nucleotide-exchange IC50 rises from 2.4 nM on G12C to 229 nM on G12C/Y96D, a ~100-fold loss from a single switch-II mutation, and Y96D is the commonest clinical resistance substitution. Whitley et al. (2026) classify the resistance mechanisms as Type I (loss of inhibitor contacts) and Type II (stabilisation of pocket-occluding switch-II conformations), with Y96D exhibiting both. A next-generation lead therefore needs either a Y96-independent contact network or a mechanism outside the switch-II pocket (the RAS(ON) tricomplex inhibitors are the live example). Neither ChEMBL lead has published resistance data; that is the first experiment to run on them, before any potency claim is repeated.

### 4.4 The falsifiable test

Two experiments decide whether this paper's conclusion holds. **(1) Covalent-aware re-scoring:** re-score the same five compounds with a covalent docking protocol (covalent bond to Cys12 modelled explicitly) on the same 6OIM structure. Prediction: the covalent-aware order restores the measured order — CHEMBL4855521 and CHEMBL4856277 at or near the top, ahead of sotorasib — while the non-covalent order reported here does not reproduce. If covalent scoring also fails to restore the order, the problem is the pocket model itself, not the covalent term. **(2) Same-plate biochemical assay:** measure all five compounds in one nucleotide-exchange assay on the 6OIM construct (KRAS G12C/C51S/C80L/C118S), plus the G12C/Y96D double mutant. Prediction: the two ChEMBL leads remain sub-nanomolar on G12C and lose potency on Y96D by at least an order of magnitude; sotorasib's Ki of 11 nM reproduces within two-fold. If the ChEMBL leads do not reproduce as sub-nanomolar on a shared plate, their ChEMBL numbers are assay artefacts and this paper's inversion claim falls with them.

## 5. Limitations

(1) Five compounds, one structure, one rigid-receptor protocol — a benchmark, not a screen. (2) Measured potencies mix assay types (Ki, nucleotide exchange, cellular signalling, ChEMBL IC50); only the two ChEMBL leads share an assay, so the cross-assay ranking is indicative. (3) The ChEMBL leads are unnamed, uncharacterised compounds from a single assay series; their structures were verified in ChEMBL but their provenance (patent vs paper) was not traced, and one sibling lead (CHEMBL4852458) could not be resolved at all because the ChEMBL molecule endpoint returned HTTP 500 three times. (4) No re-dock RMSD was computed for sotorasib against its crystal pose, so the −8.14 re-dock score is a pocket-fit check, not a pose-accuracy claim. (5) No molecular dynamics, no covalent docking, no free-energy calculation, no experiment. (6) ChEMBL was intermittently unavailable during this run (HTTP 500 on two endpoints); a re-query on another day could return additional G12C-construct leads.

## 6. Conclusion

On the verified KRAS G12C structure 6OIM, standardised non-covalent Vina docking ranks the two most potent measured binders last: CHEMBL4855521 and CHEMBL4856277 (ChEMBL IC50 0.51 and 0.56 nM on the crystallised construct) score −6.03 and −5.51 kcal/mol, 2.11–2.63 kcal/mol behind sotorasib (−8.14), whose measured Ki is 11 nM. Sotorasib scores nearly as well on wild-type KRAS (−7.22), which it cannot covalently bind. The hypothesis is rejected: for covalent KRAS G12C inhibitors, non-covalent Vina scores do not rank compounds by measured potency, and they should not be used as a ranking tool for this target class without a covalent-aware term. The two ChEMBL leads are genuine sub-nanomolar leads on the construct — and the next experiment is not more docking, it is a covalent re-score and a same-plate assay including the Y96D resistance mutant.

---

## References

1. Canon J, Rex K, Saiki AY, et al. The clinical KRAS(G12C) inhibitor AMG 510 drives anti-tumour immunity. *Nature*. 2019;575:217–223. doi:10.1038/s41586-019-1694-1. PMID 31666701. (6OIM structure; sotorasib discovery.)
2. Lanman BA, Allen JR, Allen JG, et al. Discovery of a covalent inhibitor of KRASG12C (AMG 510) for the treatment of solid tumors. *J Med Chem*. 2020;63:52–65. doi:10.1021/acs.jmedchem.9b01180. PMID 31820981. (Sotorasib Ki 11 nM; pERK IC50 68 nM.)
3. Skoulidis F, Li BT, Dy GK, et al. Sotorasib for lung cancers with *KRAS* p.G12C mutation. *N Engl J Med*. 2021;384:2371–2381. doi:10.1056/NEJMoa2103695. PMID 34096690. (CodeBreaK 100: ORR 37.1%, median OS 12.5 months.)
4. Hallin J, Engstrom LD, Hargis L, et al. The KRAS(G12C) inhibitor MRTX849 provides insight toward therapeutic susceptibility of KRAS-mutant cancers in mouse models and patients. *Cancer Discov*. 2020;10:54–71. doi:10.1158/2159-8290.CD-19-1167. PMID 31658955. (Adagrasib cellular IC50 ~5 nM; viability 10–973 nM.)
5. Fell JB, Fischer JP, Baer BR, et al. Identification of the clinical development candidate MRTX849, a covalent KRAS G12C inhibitor for the treatment of cancer. *J Med Chem*. 2020;63:6679–6693. doi:10.1021/acs.jmedchem.9b02052.
6. Sacher A, et al. Single-agent divarasib (GDC-6036) in solid tumors with a KRAS G12C mutation. *N Engl J Med*. 2023;389:710–721. (Divarasib Phase I.)
7. Binding modes of the KRAS(G12C) inhibitors GDC-6036 and LY3537982 revealed by all atom molecular dynamics simulations. *Sci Rep*. 2025;15:24843. doi:10.1038/s41598-025-07532-2. (Divarasib nucleotide-exchange IC50 2.4 ± 0.2 nM on G12C, 229 ± 59 nM on G12C/Y96D.)
8. Tanaka N, Lin JJ, Li C, et al. Clinical acquired resistance to KRAS(G12C) inhibition through a novel KRAS switch-II pocket mutation and polyclonal alterations converging on RAS-MAPK reactivation. *Cancer Discov*. 2021;11:1913–1922. doi:10.1158/2159-8290.CD-21-0365. PMID 33824136. (Y96D resistance mutation.)
9. Koga T, Suda K, Fujino T, et al. KRAS secondary mutations that confer acquired resistance to KRAS G12C inhibitors, sotorasib and adagrasib, and overcoming strategies: insights from in vitro experiments. *J Thorac Oncol*. 2021;16:1321–1332. (Cross-resistance profiles: Y96D/S both drugs; G13D/R68M adagrasib-sensitive; Q99L sotorasib-sensitive.)
10. Awad MM, Liu S, Rybkin II, et al. Acquired resistance to KRAS(G12C) inhibition in cancer. *N Engl J Med*. 2021;384:2382–2393. doi:10.1056/NEJMoa2105281.
11. Whitley MJ, Denson JP, Messing SA, et al. Structural mechanisms underlying resistance to Switch-II pocket inhibitors in KRAS. *Nat Commun*. 2026. doi:10.1038/s41467-026-78133-4. (R68S, H95Q, Y96C, Y96D, Q99L; Type I/II mechanisms; 143-patient cohort, 14% switch-II pocket mutations.)
12. Broker J, Waterson AG, Hodges TR, et al. Discovery of BI-2493, a pan-KRAS inhibitor showing in vivo efficacy. *J Med Chem*. 2025;68:15649–15668. doi:10.1021/acs.jmedchem.5c00576. PMID 40709733. (9IAY wild-type KRAS-GDP structure.)
13. Hasdemir HS, Adury VSS, Tiwary P. ANTIOCH-VS: From sequence to hits with modular, open-source ensemble virtual screening. arXiv:2611.14287 (2026).
14. Srivastava M, Lim MH, Keys AM, Murugan P, Gruver N, et al. Pyrite: Building and benchmarking protein-ligand pose ranking agents. arXiv:2611.14511 (2026).
15. U.S. Food and Drug Administration. FDA grants accelerated approval to adagrasib for KRAS G12C-mutated NSCLC. 12 December 2022. (KRYSTAL-1: ORR 43%, median duration of response 8.5 months.)
16. Sotorasib, a KRASG12C inhibitor for non-small cell lung cancer. *Trends Pharmacol Sci*. 2022;43:536–537. doi:10.1016/j.tips.2022.03.011. PMID 35461718. (G12C in 12–15% of NSCLC, 3% of colorectal cancer; FDA approval 28 May 2021.)

---

## Data availability

All numbers in this paper trace to the files below (goal workspace `hidden_files/`, retained with the manuscript) or to the cited literature. No new experimental data were generated.

- LeadForge pipeline runs (both attempts, including the two disclosed failures): `run_kras_g12c_2026-11-12_raw.json` (run 1: correct target CHEMBL2189121, zero ligands; run 2: wrong target CHEMBL2074, 55 maltase-glucoamylase ligands — discarded) and `dock_kras_g12c_2026-11-12_raw.json` (automatic 9IAY docks — discarded except the sotorasib wild-type control, −7.22 kcal/mol).
- Centre-audited 6OIM benchmark (5 compounds, descriptors, PAINS): `dock_kras_6oim_2026-11-12.json`; script: `dock_kras_6oim_2026-11-12.py`; pipeline run script: `run_kras_g12c_2026-11-12.py`.
- ChEMBL target CHEMBL2189121, queried live 2026-11-12 (pChEMBL ≥ 5; 4,666 activities); PubChem CIDs 137278711 (sotorasib), 138611145 (adagrasib), 146624881 (divarasib), queried live 2026-11-12. Structures: RCSB PDB 6OIM (1.65 Å) and 9IAY (0.95 Å), downloaded 2026-11-12.
- Daily literature digest: `~/workspace/research-team/digests/2026-11-12.md`.
- Research-agent status: Mimosa's litellm patch is verified working but its smoke run stalled in 2026-11-02 and was never completed; Co-Scientist, Denario and EvoScientist remain blocked on API-key authorisation (see `~/workspace/research-agents/INSTALL-LOG-2026-11-01.md`). No agent was used for this paper; the literature sweep and computation were done directly. No API key was requested, invented, or used.
