# Four Sub-Nanomolar Androgen Receptor Ligands Dock in Exact Measured-Potency Order on 8E1A — While Enzalutamide Itself Fails to Dock

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-12 · **Health Papers Agent — Paper #51** (daily 5-paper run)

**Keywords:** androgen receptor; enzalutamide; F876L; molecular docking; AutoDock Vina; prostate cancer; castration-resistant; drug resistance

---

## Abstract

Prostate cancer accounted for about 7.5% of all new cancers worldwide in 2024, roughly 1.5 million cases, and enzalutamide — an androgen receptor (AR) antagonist that extended median overall survival from 13.6 to 18.4 months in the AFFIRM trial — eventually fails in most men with metastatic castration-resistant disease, in part because the F876L ligand-binding-domain mutation converts the drug from antagonist to agonist. The gap this paper attacks is whether a standardised docking screen can rank AR ligands at all when the reference drug itself is the hard case. We ran the LeadForge pipeline (UniProtKB P10275 → ChEMBL target CHEMBL1871, 38 bioactivities → PubChem → RDKit ADMET/PAINS → AutoDock Vina 1.2.7) and docked four ChEMBL AR actives plus enzalutamide into the 1.2 Å AR ligand-binding-domain structure 8E1A, with the grid centre audited to 0.005 Å from the co-crystallised ligand. The four leads docked in exact measured-potency order — CHEMBL391548 −9.88 kcal/mol (IC50 0.02 nM), CHEMBL3818706 −8.47 (EC50 0.032 nM), CHEMBL3819048 −8.07 (EC50 0.16 nM), CHEMBL3819648 −6.96 (EC50 0.20 nM), Spearman ρ = 1.0 — but enzalutamide itself failed to dock, scoring +0.71 kcal/mol across all three poses, and a re-dock at exhaustiveness 32 returned the same failure (+0.69 kcal/mol), ruling out search depth as the cause; a fifth lead produced no docking result at all. No "beats enzalutamide" claim can therefore be made from this screen, and no F876L-mutant structure was docked, so the resistance question the topic posed remains untested. The falsifiable next step is an AR transactivation assay of the four leads against enzalutamide in wild-type and F876L AR: if the measured antagonist order matches the ChEMBL record rather than the Vina order, docking alone must not be used to prioritise AR leads on this structure.

---

## 1. Introduction

Prostate cancer is the second most diagnosed cancer in men and the fifth leading cause of cancer-related mortality worldwide. The 2024 GLOBOCAN estimates put prostate cancer at 7.5% of all new cancers — roughly 1.5 million cases in a year in which 20.6 million cancers were diagnosed. Localised disease is nearly always survivable, with a five-year survival rate close to 100%, but metastatic disease drops that figure to about 30%. The androgen receptor, a ligand-activated nuclear transcription factor, is the primary driver of prostate cancer growth and progression, and it remains the central therapeutic target even after the disease stops responding to androgen deprivation.

Enzalutamide was the drug that proved the receptor stays druggable in castration-resistant disease. In the AFFIRM trial — 1,199 men with metastatic castration-resistant prostate cancer after chemotherapy, randomised 2:1 to enzalutamide 160 mg daily or placebo — median overall survival was 18.4 months on enzalutamide versus 13.6 months on placebo (hazard ratio for death 0.63, 95% CI 0.53–0.75), and the trial was stopped early at a planned interim analysis. Enzalutamide inhibits AR nuclear translocation, DNA binding and coactivator recruitment, three steps beyond simple ligand competition.

Resistance follows in most patients. The mechanisms are AR-dependent in the majority of cases: AR gene amplification, ligand-binding-domain point mutations, and splice variants such as AR-V7 that activate signalling without a ligand-binding domain at all. The best-characterised point mutation is F876L. In a reporter-based mutagenesis screen, F876L converted enzalutamide from an antagonist into an agonist, and ectopic expression of AR F876L rescued prostate cancer cells from enzalutamide growth inhibition; molecular dynamics suggested the substitution repositions helix 12, the coactivator-recruiting helix, so that the drug-bound receptor adopts an active conformation. The same mutation confers resistance to apalutamide (ARN-509). A compound that antagonises F876L AR — the screen that found F876L also found three such compounds — is therefore the precise therapeutic need, and a docking screen that cannot even place enzalutamide in the wild-type pocket cannot be trusted to find one.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen of ChEMBL androgen-receptor actives against enzalutamide on a high-resolution AR ligand-binding-domain structure will rank compounds in the same order as their measured potencies. The test is the rank correlation, not the best score — and the reference drug must itself dock, or the comparison is void.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-12 (web search; PubMed/bioRxiv via the daily digest of 2026-11-12, which screened 840 candidates and selected 8, none on the androgen receptor — the digest's relevance is methodological, not topical, for this paper). Key sources: Sung et al. 2026 for the 2024 global cancer burden; Scher et al. 2012 for the AFFIRM trial; Balbas et al. 2013 for the F876L mutation and its agonist conversion; Quistini et al. 2025 for AR resistance mechanisms. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P10275 (human androgen receptor, AR, 920 aa); ChEMBL target CHEMBL1871 (verified: "Androgen receptor", SINGLE PROTEIN, Homo sapiens); 38 bioactivities retrieved, 25 leads after RDKit similarity screening and ranking, 26 including the reference query; the top 5 leads docked plus the reference query (enzalutamide, PubChem CID 15951529, verified live). Structure: PDB 8E1A, the human AR ligand-binding domain (residues 664–919), resolution 1.2 Å, deposited from a structure-based study of novel AR inhibitors. Grid centre [26.97, 2.59, 4.23] — audited against the co-crystallised ligand 3E0 (chain A, residue 1001) centroid computed from the deposited coordinates with the pipeline's own `_ligand_center` function: distance 0.005 Å, i.e. the grid is exactly on the ligand-binding pocket. Best of three poses reported per compound. The same grid, box (22.5 Å) and exhaustiveness (8) were used for every compound including enzalutamide.

Two pipeline faults are disclosed here, not hidden. First, the fifth lead, CHEMBL3818497 (EC50 0.20 nM, pChEMBL 9.70), produced no docking result: no affinity, no poses, and no error was logged by the docking run. It is reported as missing in the table, not silently dropped. Second, a live ChEMBL activity-endpoint lookup at drafting time (to cross-check the per-lead potencies against the ChEMBL API directly) returned HTTP 500 on both network variants — the known EBI flakiness also seen on 2026-11-11. The potencies in the table therefore come from the pipeline's own ChEMBL retrieval during the run, which succeeded, and were not independently re-fetched.

No F876L-mutant structure was docked. The topic as posed asked for docking against the AR ligand-binding domain including the F876L mutant; the pipeline's structure picker returned the wild-type structure 8E1A only, and no mutant structure was substituted. The resistance question is therefore untested in this paper and is carried forward as the first validation step.

### 2.3 PAINS screen

RDKit PAINS filter (the pipeline's own filter, classes A–C) applied to every docked compound. All four leads and enzalutamide are PAINS-clean. The ToxGuard Tox21 kNN read-across panel flagged several nuclear-receptor and stress-response assays for every compound including enzalutamide (Section 3.1); these are similarity-based flags, not measurements, and they are reported as a screen result, not as toxicity findings.

### 2.4 Honesty limits

Docking is not activity, and for a nuclear receptor it is doubly not efficacy: a docking score cannot distinguish an antagonist from an agonist, which is the entire question this paper asks — F876L is precisely a mutation that changes what a bound ligand does, not whether it binds. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds; the 1.41 kcal/mol gap between the first and second leads sits inside that noise. A single rigid structure (8E1A, co-crystallised with the inhibitor 3E0) cannot represent the conformational ensemble of the ligand-binding domain, and the pocket conformation is the 3E0-bound one, not the enzalutamide-bound one — no enzalutamide-bound AR structure was used. No molecular dynamics or free-energy refinement was run. No experimental data were generated. Measured potencies come from heterogeneous ChEMBL assays (one IC50, three EC50, different assay conditions); pChEMBL values are not head-to-head measurements, and the rank test mixes assay types. No measured AR potency for enzalutamide itself was retrieved in this run, so the reference enters the rank test by docking score only — and it failed to dock.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Vina best (kcal/mol) | Poses (kcal/mol) | Measured potency (CHEMBL1871) | pChEMBL | PAINS |
|---|---|---|---|---|---|
| CHEMBL391548 | −9.88 | −9.88, −9.63, −8.88 | IC50 0.02 nM | 10.70 | none |
| CHEMBL3818706 | −8.47 | −8.47 | EC50 0.03162 nM | 10.50 | none |
| CHEMBL3819048 | −8.07 | −8.07, −8.06, −6.48 | EC50 0.1585 nM | 9.80 | none |
| CHEMBL3819648 | −6.96 | −6.96 | EC50 0.1995 nM | 9.70 | none |
| CHEMBL3818497 | no result | — | EC50 0.1995 nM | 9.70 | none |
| Enzalutamide (query) | +0.71 | +0.71, +2.56, +7.05 | — (not retrieved) | — | none |

All four leads are small (MW 263–337), lipophilic (logP 3.74–4.44), Lipinski-clean (0 violations), with 1 hydrogen-bond donor, 2 acceptors and 1–2 rotatable bonds. Enzalutamide is larger (MW 464.44, logP 3.99) with 3 rotatable bonds. The ToxGuard read-across panel flagged NR-AR, NR-AR-LBD, NR-AhR, NR-PPAR-gamma, SR-ARE and SR-MMP for all five compounds, with additional ER/ER-LBD, aromatase, HSE and p53 flags varying by compound; no compound was flagged clean, and no compound was singled out — the panel does not discriminate between the leads and the reference, so it contributes nothing to ranking and is reported only for completeness.

The rank test the hypothesis posed: the Vina order of the four leads (391548 > 3818706 > 3819048 > 3819648) is exactly the measured-potency order (pChEMBL 10.70 > 10.50 > 9.80 > 9.70), Spearman ρ = 1.0 (n = 4). That is a clean pass on four compounds — and it is also a result that must not be over-read, for three reasons. First, n = 4. Second, the potency values mix one IC50 with three EC50 measurements from different assays. Third, the gap between the first and second leads (1.41 kcal/mol) is inside Vina's ±1–2 kcal/mol noise, so the only ordering the data actually support is "391548 first, 3819648 last"; the middle two are within noise of each other.

### 3.2 Comparison with published docking

No published Vina benchmark of these four ChEMBL compounds on 8E1A was found at drafting time, so there is no published docking comparison to make. The depositing study for 8E1A is a structure-based study of novel AR inhibitors, but its own docking scores for its compounds were not retrieved in this run and are not compared here. The absence of a published comparator is stated, not filled in.

### 3.3 The reference drug failed to dock

Enzalutamide scored +0.71 kcal/mol as its best pose, with the other two poses worse (+2.56, +7.05). A positive Vina score means no favourable binding pose was found in the box: the ligand was placed, but every placement clashed or failed to make productive contacts. Three explanations are possible, and this run tested the first. (a) Exhaustiveness: Vina's default exhaustiveness of 8 may be too low for a ligand of this size and flexibility, and the search may simply have missed the pocket. A re-dock at exhaustiveness 32 returned +0.69 kcal/mol (poses +0.69, +2.49, +7.04) — essentially identical to the exhaustiveness-8 result (+0.71, +2.56, +7.05). The failure is therefore not a search-depth artefact. (b) Pocket conformation: 8E1A is bound to 3E0, a smaller inhibitor (20 heavy atoms in the deposited ligand), and the pocket may be in a conformation that does not accommodate enzalutamide's thiohydantoin core without rearrangement. (c) Ligand preparation: the 3D conformer generated from the PubChem SMILES may be a poor starting point. The re-dock eliminates (a) and leaves (b) or (c) standing. Whichever explanation holds, the consequence is the same: the reference comparator is absent from this benchmark, and any claim of the form "lead X beats enzalutamide" would be comparing a number against a failure, not against a drug.

## 4. Discussion

### 4.1 The reframe

The paper's question changed while running it. It started as "which ChEMBL AR ligands beat enzalutamide?" and became "can this screen rank AR ligands at all?" The answer to the second question is a qualified yes on four compounds and a no on the reference: the rank correlation is perfect, but the comparator failed. A benchmark that ranks the test set correctly and cannot place its own reference is a screen with a hole in the middle, and the honest report is the hole, not just the correlation.

### 4.2 Why the "win" must not be over-read

Four compounds, mixed assay types, and a 1.41 kcal/mol top gap inside the noise margin. The Spearman ρ = 1.0 is a property of four points, not a validation of Vina on AR. The leads are also extremely potent by their ChEMBL records (0.02–0.20 nM) — sub-nanomolar across the board — which means the screen selected from the extreme tail of the activity distribution, where rank order is easiest to get right and least informative about the middle of the distribution where real prioritisation happens. None of the four is identified by name in this run (ChEMBL IDs only); their chemotypes, selectivity against other nuclear receptors, and agonist-versus-antagonist character are all unknown from this data.

### 4.3 The PAINS problem does not apply here — the reference problem does

All compounds are PAINS-clean, so no artefact controls are needed on that front. The design constraint this experiment imposes is different: any validation assay must include enzalutamide as a measured comparator in the same assay, on the same plate, because the docking comparison against it failed. A validation that compares the leads only against each other would repeat the screen's error — it would rank compounds without anchoring them to the drug they are supposed to improve on.

### 4.4 Testable hypotheses

1. **Rank hypothesis.** In an AR transactivation assay, the antagonist potency order of the four leads matches their ChEMBL record order (391548 > 3818706 > 3819048 > 3819648). Falsified if the measured order differs — in which case the perfect Spearman correlation was a four-point coincidence.
2. **Reference hypothesis.** Enzalutamide's failure to dock is a search-depth artefact: a re-dock at higher exhaustiveness recovers a favourable score (≤ −7 kcal/mol). Falsified — the exhaustiveness-32 re-dock returned +0.69 kcal/mol, essentially identical to the standard run. The remaining explanations are pocket conformation or ligand preparation, and the hypothesis is now: docking enzalutamide into an enzalutamide-accommodating AR conformation recovers a favourable score. Falsified if no standard protocol places it favourably — in which case Vina at this setting cannot be used for AR antagonist ranking at all.
3. **Resistance hypothesis.** At least one of the four leads antagonises AR F876L in a transactivation assay where enzalutamide acts as an agonist. Falsified if all four behave as agonists or are inactive on F876L — in which case the leads are wild-type binders only, and the resistance question needs a different chemotype.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain or synthesise the four leads; confirm identity and purity by LC-MS and NMR; confirm enzalutamide as the in-assay reference. Stage 2 (weeks 3–6): AR transactivation (reporter-gene) assay in wild-type AR and F876L AR, dose–response for all four leads plus enzalutamide on the same plates, with an AR antagonist control and a vehicle control; read out antagonist IC50 and any agonist activity (the F876L test). Stage 3 (weeks 7–10): counter-screen the best lead against glucocorticoid and progesterone receptors for selectivity, and repeat the top two leads in a second AR assay format (e.g. binding). Stage 4 (weeks 11–12): if a lead antagonises F876L, dock it into an F876L model and compare the pose with the wild-type pose; if none does, report the negative result and stop. Sample-size logic: three independent biological replicates per dose–response curve, eight concentrations, is the minimum for a defensible IC50; the F876L agonism test needs the same, because a false "antagonist" call on the mutant is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. Vina noise is ±1–2 kcal/mol; the 1.41 kcal/mol gap between the top two leads cannot rank them.
3. The rank test is n = 4 and mixes one IC50 with three EC50 values from heterogeneous ChEMBL assays.
4. The reference drug enzalutamide failed to dock (+0.71 kcal/mol); no comparison against it is possible from this screen.
5. The fifth lead, CHEMBL3818497, produced no docking result and no error; its absence is unexplained.
6. No F876L-mutant structure was docked, although the topic posed the resistance question; the wild-type result says nothing about the mutant.
7. A single rigid structure (8E1A, 3E0-bound) cannot represent the AR ligand-binding-domain ensemble; docking cannot distinguish antagonist from agonist.
8. No molecular dynamics or free-energy refinement was run.
9. A live ChEMBL cross-check at drafting time returned HTTP 500; potencies rest on the pipeline's in-run retrieval alone.
10. The four leads are identified by ChEMBL ID only; chemotype, selectivity and agonist/antagonist character are unknown from this data.

## 6. Conclusion

Four sub-nanomolar ChEMBL androgen-receptor ligands dock in exact measured-potency order on the 1.2 Å structure 8E1A (Spearman ρ = 1.0, n = 4), with CHEMBL391548 first at −9.88 kcal/mol against a measured IC50 of 0.02 nM. The benchmark's reference drug, enzalutamide, failed to dock at all, and the F876L resistance question was not tested. The screen is therefore a rank-order signal on four compounds with a missing comparator, not a lead claim. The next step is the assay in Section 4.5, with enzalutamide measured on the same plates.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Sung H, Ferlay J, Siegel RL, et al. Global cancer statistics 2024: GLOBOCAN estimates of incidence and mortality worldwide for 34 cancers in 186 countries. CA Cancer J Clin. 2026. doi:10.3322/caac.70090.
2. Scher HI, Fizazi K, Saad F, et al. Increased survival with enzalutamide in prostate cancer after chemotherapy. N Engl J Med. 2012;367(13):1187–1197. PMID: 22894553. doi:10.1056/NEJMoa1207506.
3. Balbas MD, et al. Overcoming mutation-based resistance to antiandrogens with rational drug design. eLife. 2013;2:e00499. doi:10.7554/eLife.00499.
4. Quistini et al. Androgen receptor signalling in prostate cancer: mechanisms of resistance to endocrine therapies. Res Rep Urol. 2025;17:211–223.
5. ChEMBL database, European Bioinformatics Institute. Androgen receptor, target CHEMBL1871. Accessed 2026-11-12. https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1871/
6. UniProtKB. Androgen receptor, human, P10275. Accessed 2026-11-12. https://www.uniprot.org/uniprotkb/P10275/entry
7. RCSB Protein Data Bank. Structure 8E1A, androgen receptor ligand-binding domain. Accessed 2026-11-12. https://www.rcsb.org/structure/8E1A
8. PubChem. Enzalutamide, CID 15951529. Accessed 2026-11-12. https://pubchem.ncbi.nlm.nih.gov/compound/15951529

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-036-2026-11-12.json`; the enzalutamide re-dock at exhaustiveness 32 is in `hidden_files/redock-HP-036-enzalutamide-2026-11-12.json`. ChEMBL IDs, UniProt accession P10275, ChEMBL target CHEMBL1871, PDB ID 8E1A and PubChem CID 15951529 are given in the text. No additional data were generated.
