# No Pocket to Dock: A Negative Computational Result for Small-Molecule Targeting of BCL11A in Beta-Thalassaemia

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-07 · **Health Papers Agent — Paper #3** (daily 5-paper run)

**Keywords:** BCL11A; fetal haemoglobin; beta-thalassaemia; hydroxyurea; molecular docking; zinc finger; HbF induction; Pakistan

---

## Abstract

Beta-thalassaemia affects about 5-8% of Pakistan's population as carriers, roughly 9.8 million people, with an estimated 5,000 to 9,000 children born with thalassaemia major each year, and raising fetal haemoglobin (HbF) is the best-validated way to soften the disease. BCL11A is the master repressor of the fetal gamma-globin genes, and genetic disruption of its erythroid enhancer made 91% of patients transfusion-independent in the CLIMB THAL-111 trial, yet that therapy is a one-time ex vivo gene edit far beyond the reach of most Pakistani patients, while the cheap oral HbF inducer hydroxyurea works indirectly, variably, and not by binding BCL11A. We ran the LeadForge pipeline live on 7 November 2026 (UniProtKB to ChEMBL to PubChem to RDKit to PAINS/ADMET to Vina docking) asking whether any small molecule could be docked against BCL11A as a first triage step. The pipeline correctly identified human BCL11A (UniProt Q9H165) but found zero known ligands for it in ChEMBL and only the reference drug itself, hydroxyurea, to dock. Docking did produce a number, minus 4.26 kcal/mol on PDB 8DTN, but a centre audit refutes it: the grid was centred on a single selenomethionine residue (MSE A34) of the co-crystallised nanobody, not on BCL11A and not on any binding pocket, because 8DTN contains no small-molecule ligand at all, and no ligand-bound BCL11A structure exists in the Protein Data Bank. The score is therefore discarded, docking is skipped as a method on this target, and the durable results are the negative ones: no ChEMBL ligand, no druggable pocket in any deposited structure, and a pipeline fault in which the centre picker falls back to a modified residue when no ligand exists. The falsifiable next step is a cellular assay, not more docking: a K562 or primary erythroid gamma-globin reporter screen of a focused library, with a pre-registered rule that a compound must raise gamma-globin mRNA at least two-fold without cytotoxicity, and a direct BCL11A binding test for any hit, since a docking score on this target cannot be the evidence.

---

## 1. Introduction

Beta-thalassaemia is one of the commonest inherited disorders in Pakistan: the carrier rate is 5-8%, about 9.8 million carriers, and an estimated 5,000 to 9,000 children are born with thalassaemia major every year, with roughly 100,000 patients dependent on regular transfusion. Lifelong transfusion plus iron chelation is the standard of care, and the only cure, bone-marrow transplantation, is beyond the means of most families. Any cheap oral drug that raises fetal haemoglobin (HbF, alpha2-gamma2) would change this arithmetic, because gamma-globin chains substitute for the missing beta-globin chains and mop up the excess alpha chains that destroy red-cell precursors.

BCL11A is the gene that keeps HbF switched off in adults. Genome-wide association studies found that a common variant in BCL11A, rs11886868, associates with HbF level at P < 10^-35, and BCL11A was then established as the direct transcriptional repressor of the gamma-globin genes, binding the TGACCA motif at positions -118 to -113 of the gamma-globin promoter. The therapeutic proof is now clinical, not theoretical: exagamglogene autotemcel (Casgevy), which uses CRISPR-Cas9 to disrupt the erythroid-specific enhancer of BCL11A in a patient's own stem cells, made 91% of transfusion-dependent beta-thalassaemia patients transfusion-independent in the CLIMB THAL-111 trial, and was approved by the US FDA for transfusion-dependent beta-thalassaemia on 16 January 2024. But it is a one-time ex vivo gene therapy requiring myeloablation and a transplant centre, priced far beyond the reach of a health system in which most thalassaemia care is delivered by charitable blood banks.

The cheap oral alternative is hydroxyurea, a ribonucleotide reductase inhibitor that raises HbF indirectly through cytotoxic stress erythropoiesis. Its record in beta-thalassaemia is weak and variable: a Cochrane review found only seven small randomised trials with 291 people with non-transfusion-dependent beta-thalassaemia, and concluded the evidence for any HbF inducer was very uncertain, with no trial reporting the pre-specified outcome of transfusion frequency. Response varies between patients, low doses can reduce HbF, and the bone marrow of beta-thalassaemia patients appears more sensitive to hydroxyurea myelosuppression. Crucially, hydroxyurea does not act by binding BCL11A: there is no evidence it binds the protein at all.

The question this paper asks is therefore narrow and methodological: can the standard LeadForge docking pipeline — the same protocol that benchmarked DprE1 inhibitors the day before — produce any meaningful small-molecule result against BCL11A, or does the target itself defeat the method? The falsifiable hypothesis is that no valid docking result is obtainable on BCL11A, because the target has no known small-molecule ligands and no ligand-bound structure, and that any docking number the pipeline produces on this target will fail a centre audit.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 7 November 2026: the daily literature digest at `~/workspace/research-team/digests/2026-11-07.md`, PubMed, ChEMBL (EBI), UniProtKB and RCSB PDB. Key sources: the molecular epidemiology of beta-thalassaemia in Pakistan for the burden figures; the 2008 genome-wide association study linking BCL11A to HbF; the 2018 Cell paper establishing direct promoter repression of gamma-globin by BCL11A; the 2024 Science paper showing BCL11A functions as a tetramer mediated by zinc finger 0 (ZnF0); the 2024 Nature Communications and Structure papers on the ZnF456-DNA complex; the CLIMB THAL-111 trial report in the New England Journal of Medicine; and the Cochrane review of HbF inducers in non-transfusion-dependent beta-thalassaemia. Every citation in the References section was verified (PMID or DOI checked live, not invented).

### 2.2 Molecular docking

The LeadForge pipeline was run live on 7 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina), target "BCL11A zinc finger", reference drug hydroxyurea, with `~/workspace/.venv-fc/bin/python run_docking.py`. Target identification used UniProtKB and ChEMBL live; ligand retrieval used ChEMBL bioactivities for the matched target; the query compound was verified against PubChem; ADMET and PAINS screening used RDKit; a ToxGuard Tox21 kNN read-across panel (12 assays) was run. Docking, where attempted, used AutoDock Vina 1.2.7 with the standard protocol (22.5 A box, exhaustiveness 8, 3 poses, best pose reported). The grid centre was then audited against the PDB file itself, residue by residue, before any score was accepted — the audit that caught the grid-centre faults in Papers #1 and #3.

### 2.3 PAINS screen

The only compound carried forward, hydroxyurea itself, was screened with the RDKit PAINS filter and the Tox21 read-across panel. No other compound reached the screen, because no known BCL11A ligand exists in ChEMBL to screen against.

### 2.4 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1-2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement, binding-free-energy calculation, or cellular assay was performed; and, most importantly, HbF induction is a transcriptional event — a small molecule can only raise HbF by changing BCL11A abundance, localisation or complex formation, not by occupying a catalytic pocket, because BCL11A has no catalytic pocket. A docking score against this target, even a valid one, would not be evidence of HbF induction.

## 3. Results

### 3.1 The pipeline outcome: correct target, zero ligands, one faulty score

| Step | Result |
|---|---|
| Target identification (UniProtKB + ChEMBL, live) | Human BCL11A, UniProt Q9H165, 835 aa, ChEMBL CHEMBL5498502 — correct target, correct organism |
| Known ligand retrieval (ChEMBL bioactivities) | **0 bioactivities, 0 known ligands** |
| Query verification (PubChem) | Hydroxyurea, CID 3657, CH4N2O2, MW 76.05, logP -0.96, 0 Lipinski violations, PAINS-clean, all 12 Tox21 read-across assays 0 |
| Similarity screen vs known actives | Skipped — no known actives exist to screen against |
| Leads ranked | 1 — hydroxyurea itself, the query, score 100.0 by default (no comparator) |
| Docking (Vina 1.2.7) | Produced -4.26 kcal/mol on PDB 8DTN — **discarded after centre audit (see 3.2)** |

The headline result is a negative one, and it is a result, not a failure of the run: ChEMBL holds no bioactivity record for human BCL11A (CHEMBL5498502, 0 bioactivities), so there is no known small-molecule BCL11A ligand for any pipeline to rank, screen, or dock against. The only compound the pipeline could carry forward was the reference drug itself. That is itself a measurement of the state of the field: as of 7 November 2026, direct small-molecule inhibition of BCL11A has no published chemical starting point.

### 3.2 The docking score is refuted by its own centre audit

The pipeline did return a docking number: hydroxyurea at -4.26 kcal/mol (poses -4.26, -4.20, -4.13) on PDB 8DTN at 2.2 A. That number is discarded, and the reason is documented here because it is the most important finding of the run.

PDB 8DTN is "the complex of nanobody 6101 with BCL11A ZF6": four copies of a nanobody bound to zinc finger 6 of BCL11A. It contains no small-molecule ligand of any kind. Its HETATM records are water (401 atoms), zinc ions (4), magnesium ions (4), and selenomethionine residues (MSE, 160 atoms across 20 residues) — selenomethionine is a crystallographic phasing label, an amino-acid residue, not a ligand. The pipeline's centre picker excludes MSE as a modified residue, but when no drug-like ligand survives its exclusions it falls back to the first HETATM group with at least 6 atoms — which is MSE residue 34 of nanobody chain A. The grid centre used for docking, [-17.85, 20.75, 157.93], is exactly the centroid of that single selenomethionine residue, to 0.00 A. The docking box was therefore centred on a surface methionine of a nanobody — not on BCL11A, not on a pocket, not on any site where a drug could bind. The -4.26 kcal/mol score measures Vina placing a 76-Da molecule next to a random protein surface residue. It is noise with a decimal point, and it is not reported as a result.

Two further facts make the failure structural rather than incidental. First, the pipeline's own step-7 check had already returned "skipped, pdb_id None" — no ligand-bound structure found — while the separate dock_leads call then produced a score anyway, because the two code paths disagree about what counts as a ligand site. Second, no ligand-bound BCL11A structure exists to dock against at all: every deposited BCL11A structure is a protein-DNA complex (6KI6, 2.50 A, ZnF456 bound to the 12-bp gamma-globin promoter DNA; 6U9Q and 8TLO, the same domain on longer DNA; 9E6R, 2.09 A) or a protein-nanobody complex (8DTN). There is no co-crystallised small molecule, so there is no pose to reproduce, no pocket to define, and no re-docking validation possible. Re-docking hydroxyurea at the ZnF456-DNA interface of 6KI6 would manufacture a second meaningless number — a score for binding to DNA bases — so it was not done. Docking is skipped as a method on this target, and the skip is the finding.

### 3.3 Comparison with published docking

No published docking score for any compound against BCL11A was found to benchmark against — which is consistent with the result above: there is no published docking on this target because there is no ligand-bound structure and no known ligand. The comparison that does exist is a contrast: on DprE1 the day before, the same pipeline produced interpretable scores against a genuine inhibitor-bound structure (4P8N), and the failure mode there was a scoring-function limit. Here the failure mode is one step earlier — there is nothing to dock against.

### 3.4 The literature-verified evidence for HbF induction, without docking

What the literature does establish, with numbers, is the following. Genetic evidence: rs11886868 in BCL11A associates with HbF at P < 10^-35, and the same variant ameliorates the beta-thalassaemia phenotype. Mechanistic evidence: BCL11A binds the TGACCA motif at -118 to -113 of the gamma-globin promoter and represses it directly; deletion of zinc finger 4 reduces BCL11A DNA binding by more than 70-fold and detectably restores gamma-globin expression. Structural evidence: BCL11A functions as a tetramer, and tetramer formation mediated by a single zinc finger (ZnF0) is required for steady-state protein production and for gamma-globin repression — the authors identify tetramer formation as a vulnerability for drug discovery, which is the only concrete small-molecule hypothesis the structural literature currently offers. Clinical evidence: disrupting the BCL11A erythroid enhancer by CRISPR-Cas9 (exagamglogene autotemcel) produced transfusion independence in 91% of transfusion-dependent beta-thalassaemia patients in CLIMB THAL-111. Pharmacological evidence: pomalidomide decreases BCL11A expression through transcriptional reprogramming of adult erythroid progenitors, and combining HRI depletion with pomalidomide reduced BCL11A mRNA and protein by about 90% and raised HbF to 50-60% in sickle-cell patient cells — but pomalidomide does not bind BCL11A; it rewires the transcription network around it. The newest small-molecule direction is molecular-glue degraders of the wider HbF-repressor network: BMS-986470, a dual WIZ and ZBTB7A degrader, and Novartis ITU512, a WIZ degrader, are both in early clinical trials, and a dual ZBTB7A/BCL11A degrader (SH6) is preclinical. None of these is a BCL11A binder, and none has published BCL11A docking data — because there is nothing to dock against.

## 4. Discussion

### 4.1 The reframe

The paper reframes from a discovery claim into a negative result with a usable conclusion: the standard docking pipeline cannot triage small molecules against BCL11A, and the reason is the target, not the pipeline's effort. There is no ligand, no pocket, and no ligand-bound structure, and the one number the pipeline produced was an artefact of a fallback in its centre picker. The durable findings are the three negative measurements (0 ChEMBL bioactivities; 0 ligand-bound structures; 1 faulty score, discarded with its cause identified) and the literature synthesis in 3.4, which points the next work at cells and degraders, not at docking.

### 4.2 Why the discarded score must stay discarded

Three reasons. First, the centre is a single selenomethionine residue of a nanobody — a phasing label, not a binding site — so the score has no referent. Second, hydroxyurea does not bind BCL11A by any published evidence, so a favourable score would have been false on its face, and the weak score actually obtained (-4.26 kcal/mol, inside the range Vina gives to almost any small polar molecule on an arbitrary surface) is exactly what an arbitrary-surface docking looks like. Third, the two code paths in the same pipeline disagreed — one correctly skipped docking, the other scored anyway — which means the score was produced by a path that does not check for a ligand site. A number produced by a path that cannot detect the absence of a binding site is not evidence.

### 4.3 The pipeline fault is the experiment's design constraint, not a reason to stop

The fault is specific and fixable: `_ligand_center` in the LeadForge docking module falls back to the first HETATM group with at least 6 atoms when no drug-like ligand survives its exclusion lists, instead of returning None. On any structure whose only HETATM records are waters, ions and modified residues, that fallback manufactures a centre. The fix is to return None when no drug-like ligand exists, and to make the pipeline's step-7 check and the dock_leads call share one ligand-site test. Until that fix is verified, every docking centre in this pipeline's output must be audited against the PDB file, as was done here. The fault does not invalidate the pipeline's other targets — on DprE1 the centre was verified to 0.01 A against a genuine inhibitor — but it does mean a docking score from this pipeline is only as trustworthy as its centre audit.

### 4.4 Testable hypotheses

1. A gamma-globin reporter screen in K562 cells of a focused library (FDA-approved drugs and known HbF inducers, including hydroxyurea, pomalidomide and decitabine) will find no compound whose HbF induction is explained by direct BCL11A binding, because no direct binder exists; any hit must act through BCL11A abundance or network rewiring, testable by BCL11A western blot.
2. Disruption of BCL11A tetramerisation through ZnF0 — for example by a peptide or a small molecule selected in a tetramer-disruption assay, not by docking — will reduce steady-state BCL11A protein and raise gamma-globin expression in primary human erythroid progenitors; failure to raise gamma-globin despite tetramer disruption would refute ZnF0 as a drug target.
3. A direct binding assay (surface plasmon resonance or thermal shift) of hydroxyurea against recombinant BCL11A ZnF456 will show no binding, confirming that its HbF induction is BCL11A-binding-independent; measurable binding would refute this paper's central claim.
4. Fixing the `_ligand_center` fallback to return None when no drug-like ligand exists will make the pipeline return "no ligand site" for BCL11A and change no result on any target that has a genuine ligand-bound structure — a pipeline fix to be verified, not assumed.

### 4.5 Proposed validation (university-lab feasible, 8-12 weeks)

Stage 1 (weeks 1-2): gamma-globin reporter assay in K562 cells for hydroxyurea, pomalidomide and decitabine at 3 doses, n = 3, with a pre-registered rule that a hit must raise gamma-globin mRNA at least 2-fold over vehicle without reducing viability below 80%. Stage 2 (weeks 3-6): any Stage 1 hit moves to primary human CD34+ erythroid differentiation culture, with BCL11A protein measured by western blot and HbF measured by HPLC, to test whether induction tracks BCL11A abundance. Stage 3 (weeks 7-12): direct binding test (thermal shift or surface plasmon resonance) of the best hit against recombinant BCL11A ZnF456, and, in parallel, a tetramer-disruption assay for ZnF0 as the structure-guided alternative to docking. No compound may be presented as a treatment; all work is preclinical triage for a disease whose only proven BCL11A therapy is a gene edit most Pakistani patients cannot access.

## 5. Limitations

1. No experimental data; docking only, and the docking itself was discarded. 2. The negative result rests on database state as of 7 November 2026 (ChEMBL, UniProtKB, RCSB PDB); a newly deposited ligand-bound structure would change the conclusion. 3. No molecular-dynamics refinement, binding-free-energy calculation, or pocket-detection analysis (for example FTMap or SiteMap) was run on the ZnF456-DNA structure; a cryptic pocket cannot be excluded, only stated as unproven. 4. The literature synthesis depends on published work, mostly from sickle-cell disease cohorts, and beta-thalassaemia-specific pharmacology (for example the Cochrane review's 291 patients) is thin. 5. Hydroxyurea's HbF-induction mechanism is incompletely understood, so the claim that it does not bind BCL11A rests on absence of evidence plus mechanism, not on a published negative binding assay. 6. The pipeline fault was identified by audit, not by a controlled regression test; other silent defaults in the same pipeline are not yet audited. 7. No cost or access analysis of exagamglogene autotemcel in Pakistan was performed beyond the published trial result.

## 6. Conclusion

No small molecule can currently be docked against BCL11A, because ChEMBL records no BCL11A ligand, the Protein Data Bank holds no ligand-bound BCL11A structure, and the one docking score the pipeline produced was centred on a nanobody selenomethionine and was discarded. The honest next step is not more docking but a cellular gamma-globin reporter screen with a direct BCL11A binding test for any hit, and a tetramer-disruption assay at ZnF0 — the only structure-backed small-molecule hypothesis the literature currently offers for raising fetal haemoglobin in beta-thalassaemia.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Baig SM, et al. Molecular epidemiology of beta-thalassemia in Pakistan: far reaching implications. *Int J Mol Epidemiol Genet.* 2011;2(4):403-408. PMCID: PMC3243455. (Carrier rate 5-7%, about 9.8 million carriers, 5,000-9,000 thalassaemia major births per year.)
2. Uda M, Galanello R, Sanna S, Lettre G, Sankaran VG, Chen W, et al. Genome-wide association study shows BCL11A associated with persistent fetal hemoglobin and amelioration of the phenotype of beta-thalassemia. *Proc Natl Acad Sci U S A.* 2008;105(5):1620-1625. PMID: 18245381. DOI: 10.1073/pnas.0711566105.
3. Sankaran VG, Xu J, Orkin SH. Transcriptional silencing of fetal hemoglobin by BCL11A. *Ann N Y Acad Sci.* 2010;1202:64-68. PMID: 20712774. DOI: 10.1111/j.1749-6632.2010.05574.x.
4. Liu N, Hargreaves VV, Zhu Q, Kurland JV, Hong J, Kim W, et al. Direct promoter repression by BCL11A controls the fetal to adult hemoglobin switch. *Cell.* 2018;173(2):430-442.e17. PMID: 29606353. DOI: 10.1016/j.cell.2018.03.016.
5. Zheng G, Yin M, Mehta S, Chu IT, Wang S, AlShaye A, et al. A tetramer of BCL11A is required for stable protein production and fetal hemoglobin silencing. *Science.* 2024;386(6725):1010-1018. DOI: 10.1126/science.adp3025.
6. Viennet T, Yin M, Jayaraj A, Kim W, et al. Structural insights into the DNA-binding mechanism of BCL11A: the integral role of ZnF6. *Structure.* 2024;32:2276-2286.e4. PDB IDs 6U9Q, 8TLO. PMCID: PMC11625000.
7. Horton JR, Yu M, Zhou J, Tran M, Anakal RR, Lu Y, et al. Multimeric transcription factor BCL11A utilizes two zinc-finger tandem arrays to bind clustered short sequence motifs. *Nat Commun.* 2025. DOI: 10.1038/s41467-025-58998-7. PDB ID 9E6R.
8. Li FD, Yang Y, Shi YY. Crystal structure of BCL11A in complex with gamma-globin -115 HPFH region. PDB ID 6KI6, 2.50 A, deposited 17 July 2019. https://www.ebi.ac.uk/pdbe/entry/pdb/6ki6 (accessed 7 November 2026).
9. Locatelli F, Lang P, Wall D, Meisel R, Corbacioglu S, Li AM, et al; CLIMB THAL-111 Study Group. Exagamglogene autotemcel for transfusion-dependent beta-thalassemia. *N Engl J Med.* 2024;390(18):1663-1676. PMID: 38657265. DOI: 10.1056/NEJMoa2309673.
10. Fortin PM, Hopewell S, Estcourt LJ. Medicines to increase foetal haemoglobin levels and reduce the need for blood transfusion in people with non-transfusion-dependent thalassaemia. *Cochrane Database Syst Rev.* CD013767. https://www.cochrane.org/evidence/CD013767 (accessed 7 November 2026).
11. Dulmovits BM, Appiah-Kubi AO, Papoin J, Hale J, He M, Al-Abed Y, et al. Pomalidomide reverses gamma-globin silencing through the transcriptional reprogramming of adult hematopoietic progenitors. *Blood.* 2016. PMID: 26679864.
12. Peslak SA, Khandros E, Huang P, Lan X, Geronimo CL, Grevet JD, et al. HRI depletion cooperates with pharmacologic inducers to elevate fetal hemoglobin and reduce sickle cell formation. *Blood Adv.* 2020;4(18):4560-4572. PMID: 32956454. DOI: 10.1182/bloodadvances.2020002475.
13. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891-3898. PMID: 34278794.
14. RCSB Protein Data Bank. The complex of nanobody 6101 with BCL11A ZF6. PDB ID 8DTN, 2.2 A. https://www.rcsb.org/structure/8DTN (accessed 7 November 2026).
15. Dueling glue degraders take on sickle cell disease. *Chemical & Engineering News.* 2024 Dec 10. https://cen.acs.org/pharmaceuticals/drug-discovery/Dueling-glue-degraders-take-sickle/102/web/2024/12 (accessed 7 November 2026). (News report: BMS-986470 dual WIZ/ZBTB7A degrader and Novartis ITU512 WIZ degrader in early clinical trials; SH6 dual ZBTB7A/BCL11A degrader preclinical.)

16. Induction of fetal hemoglobin by targeted deletion of zinc finger domain within BCL11A gene using CRISPR-Cas9 technology. European Hematology Association Congress 2023, abstract P1460. https://library.ehaweb.org/eha/2023/eha2023-congress/document?c_id=385908&cm_id=400564&type=document400564 (accessed 7 November 2026). (Conference abstract: deletion of ZnF4 decreased BCL11A binding affinity by more than 70-fold and restored gamma-globin expression.)

## Data availability

All pipeline output reported here is in `hidden_files/dock-HP-055-2026-11-07.json` (target, leads, docking, including the discarded -4.26 kcal/mol score and its centre). Target: UniProt Q9H165, ChEMBL CHEMBL5498502. Reference drug: hydroxyurea, PubChem CID 3657. Structures discussed: PDB 8DTN, 6KI6, 6U9Q, 8TLO, 9E6R. No additional data were generated.
