# No Structure to Dock On: A ChEMBL Potency Analysis of HIV-1 Integrase Inhibitors Against Dolutegravir, and Why Wild-Type Potency Is Solved but Mutant Coverage Is Not

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-10 · **Health Papers Agent — Paper #40** (daily 5-paper run)

**Keywords:** HIV-1 integrase; dolutegravir; INSTI; drug resistance; ChEMBL; strand transfer; cabotegravir; BMS-707035

---

## Abstract

HIV-1 infects 40.8 million people worldwide, with 1.3 million new infections and 630,000 AIDS-related deaths in 2024; in Pakistan an estimated 350,000 people live with HIV, new infections rose 200% between 2010 and 2024, and only 21% of those infected know their status. Dolutegravir, a second-generation integrase strand transfer inhibitor (INSTI), is the backbone of first-line antiretroviral therapy because of its potency (strand-transfer IC50 2.7 nM) and high genetic barrier — but resistance through G140S/Q148H, G118R, N155H and R263K is now documented, including in 4.8% of people failing dolutegravir-based therapy in a 2026 Taiwan cohort. The gap this paper attacks is whether the next INSTI should be chosen on wild-type potency at all. We ran the LeadForge pipeline (UniProtKB P04585 → corrected ChEMBL target CHEMBL3471, 48 bioactivities → PubChem verification → RDKit ADMET/PAINS) and analysed the top leads against dolutegravir — with docking deliberately SKIPPED, because no X-ray structure of HIV-1 integrase with a strand-transfer inhibitor exists and the pipeline's default structure pick was the wrong enzyme (HIV-1 protease, PDB 6DV4). All ten top leads are sub-3 nM by their best ChEMBL record: cabotegravir is the most potent (IC50 0.22 nM, pChEMBL 9.66), dolutegravir's own record is 0.5 nM, and seven BMS-707035-series analogues share EC50 2.0 nM in the same assay — yet the pipeline's composite score still ranks by similarity to dolutegravir, not by potency, so a different chemotype with equal potency scores far lower. Wild-type potency is solved; the falsifiable next step is a strand-transfer assay of the top leads on wild-type versus G140S/Q148H intasomes, with the investigational compound 4d as comparator: a lead only matters if it keeps potency where dolutegravir loses it.

---

## 1. Introduction

UNAIDS estimates 40.8 million people were living with HIV in 2024, with 1.3 million new infections and 630,000 AIDS-related deaths that year, and 9.2 million people still not accessing antiretroviral therapy. Pakistan is one of the fastest-growing epidemics in the WHO Eastern Mediterranean Region: an estimated 350,000 people live with HIV, new infections rose from about 16,000 in 2010 to 48,000 in 2024 (a 200% increase), only ~21% know their status, ~16% are on treatment and ~7% have achieved viral suppression. The 2019 Larkana outbreak — in the author's own city — showed how fast the virus moves where testing and prevention fail.

HIV-1 integrase is the enzyme that inserts the viral DNA copy into host chromatin. INSTIs block the strand-transfer step by binding the integrase–viral DNA complex (the intasome) and coordinating the two catalytic Mg²⁺ ions at the D64/D116/E152 active site. First-generation INSTIs (raltegravir, elvitegravir) fell to single mutations; second-generation INSTIs — dolutegravir, bictegravir, cabotegravir — use a tricyclic scaffold with a di-keto motif and a halogenated benzyl group that binds the mutated active site more favourably, giving a higher genetic barrier. Dolutegravir (GSK1349572) inhibits HIV-1 integrase-catalysed strand transfer with an IC50 of 2.7 nM and viral replication in peripheral blood mononuclear cells with an EC50 of 0.51 nM, and it retains activity against raltegravir-resistant signature mutants Y143R, Q148K, N155H and G140S/Q148H in vitro — but only partially: the G140S/Q148H double mutant still reduces its potency about 5- to 6-fold. Resistance pathways are now defined along at least four routes (G118R, G140A/S/Q148H/K/R, N155H, R263K), and a 2026 multicentre Taiwan study found second-generation INSTI resistance-associated mutations in 4.8% of people failing dolutegravir-based therapy (6/127) and 5.5% failing bictegravir (4/73), most commonly Q148H/K/R (3.5%), G140A/C/R/S (3.0%) and R263K (1.5%).

Structural biology has explained why. Cryo-EM intasome structures (HIV-1 strand transfer complex, PDB 5U1C; SIVrcm intasome with dolutegravir and bictegravir) and eleven drug-resistant intasome structures published in 2023 show that G140S/Q148H perturb optimal magnesium coordination in the active site — and that the investigational compound 4d inhibits those mutants more effectively than dolutegravir, retaining antiviral potency against a panel of quadruple mutants where all three approved second-generation INSTIs lose potency.

**Hypothesis (falsifiable):** among ChEMBL HIV-1 integrase actives, wild-type potency no longer separates the leads — all top compounds are sub-3 nM — so the ranking that matters is potency on resistant intasomes, not potency on wild-type enzyme. The test is a strand-transfer assay on wild-type versus G140S/Q148H intasomes.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-10 (web search; PubMed/bioRxiv via the daily digest of 2026-11-10). Key sources: UNAIDS global HIV statistics 2024 and WHO/UNAIDS Pakistan figures; Kobayashi et al. 2011 and Hare et al. 2011 for dolutegravir's in vitro profile; Passos et al. 2017 (5U1C) and Cook et al. 2020 for intasome structures; Li et al. 2023 for the eleven drug-resistant intasome structures and compound 4d; the 2025 quadruple-mutant comparison of 4d against dolutegravir, bictegravir and cabotegravir; the 2026 Taiwan resistance cohort; and Naidu et al. 2018 for the BMS-707035 series. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 ChEMBL potency analysis (docking SKIPPED — see 2.3)

Standardised LeadForge pipeline, exactly as Papers #1/#3, except for the corrected target and the skipped docking step: UniProtKB P04585 → ChEMBL CHEMBL3471 (see correction below), 48 bioactivities retrieved (pChEMBL ≥ 5) → PubChem verification of dolutegravir → RDKit Morgan-fingerprint similarity screen vs dolutegravir → RDKit ADMET/PAINS + ToxGuard Tox21 kNN → composite lead ranking (similarity × 40 + Lipinski × 20 + Veber × 10 + PAINS × 10 + tox × 20). The top 10 leads by composite score are reported with their best ChEMBL record (pChEMBL and activity).

**Target correction (verified live, 2026-11-10):** the pipeline's default path is wrong for this target. UniProt text search for "HIV-1 integrase" returns the Gag-Pol polyprotein P04585 (integrase is a cleavage product; UniProtKB has no standalone HIV-1 integrase entry for HXB2). The pipeline's ChEMBL lookup on that accession returns a single target, CHEMBL3638360 ("Gag-Pol polyprotein"), whose top bioactivities are HIV-1 protease assays (e.g. CHEMBL3887078, WT HIV-1 protease with a peptide substrate) and whole-virus T-cell assays (CHEMBL3887045) — not integrase assays. A paper built on those would be a protease paper mislabelled as integrase. The run was therefore corrected to the true HIV-1 integrase ChEMBL target CHEMBL3471 ("Human immunodeficiency virus type 1 integrase", SINGLE PROTEIN), using the pipeline's own bioactivity, similarity, ADMET and scoring functions with only the target lookup overridden (driver script `run_docking_integrase.py`, kept in the pipeline directory).

### 2.3 Why docking was skipped

Two independent reasons, both verified. First, the pipeline's structure picker, given the polyprotein accession P04585, selects PDB 6DV4 — HIV-1 wild-type protease with the inhibitor GRL-04315A, 1.14 Å — because it sorts the accession's PDB cross-references by resolution and takes the best ligand-bound X-ray structure, regardless of which Pol domain it is. A run_docking.py attempt on that structure was started, identified as the wrong enzyme, and killed mid-Vina; no result from it is used. Second, there is no correct structure for the pipeline to pick instead: no X-ray structure of HIV-1 integrase with a strand-transfer inhibitor at the strand-transfer site exists. The dolutegravir-bound structures are cryo-EM intasomes — e.g. 8FNG, the G140A HIV-1 intasome with dolutegravir bound (2.5 Å, Li et al. 2023) — whose active site is a protein–DNA–Mg²⁺ interface: rigid AutoDock Vina docking cannot model metal coordination, the DNA interface, or a megadalton nucleoprotein complex, and the pipeline's X-ray-only picker excludes cryo-EM entries by design. The X-ray integrase structures that do carry inhibitors are allosteric-site (LEDGIN) complexes such as 8CBT (MUT872, 2.14 Å) — a different pocket from the strand-transfer site. Docking dolutegravir on 6DV4, on 8CBT, or on a cryo-EM intasome would produce numbers that look like results and are not. The paper is therefore a potency and resistance-landscape analysis, and says so in its title.

### 2.4 PAINS screen

RDKit PAINS filter applied to every lead. No compound in the top 10 carries a PAINS alert.

### 2.5 Honesty limits

No docking was performed, so there are no docking scores in this paper at all — nothing is inferred about binding modes. "Measured" potencies are single-assay ChEMBL maxima from heterogeneous assays (enzyme strand-transfer IC50 vs cell-based antiviral EC50, different laboratories and years); they are not head-to-head values, and the EC50 and IC50 figures in the table are not directly comparable with each other. The pipeline's composite score is dominated by similarity to dolutegravir (40 of 100 points), so it ranks analogues above equally potent different chemotypes by construction. No experimental data were generated.

## 3. Results

### 3.1 Potency: the comparison table

| Rank (composite score) | Compound | Similarity to dolutegravir | Composite score | Best ChEMBL record (pChEMBL) | PAINS |
|---|---|---|---|---|---|
| 1 | Dolutegravir (query) | 1.000 | 98.5 | Literature: strand-transfer IC50 2.7 nM; PBMC EC50 0.51 nM | none |
| 2 | Dolutegravir (CHEMBL1229211) | 1.000 | 98.5 | IC50 0.5 nM (9.30) | none |
| 3 | Cabotegravir (CHEMBL2403238) | 0.846 | 92.4 | IC50 0.22 nM (9.66) | none |
| 4 | CHEMBL4130252 | 0.337 | 72.8 | EC50 2.0 nM (8.70) | none |
| 5 | CHEMBL4126686 | 0.330 | 72.5 | IC50 2.0 nM (8.70) | none |
| 6 | CHEMBL4127923 | 0.312 | 71.6 | EC50 2.0 nM (8.70) | none |
| 7 | CHEMBL4128240 | 0.304 | 71.4 | EC50 1.0 nM (9.00) | none |
| 8 | CHEMBL4130102 | 0.293 | 71.1 | EC50 2.0 nM (8.70) | none |
| 9 | CHEMBL4127873 | 0.278 | 70.4 | EC50 2.0 nM (8.70) | none |
| 10 | CHEMBL492465 | 0.278 | 69.8 | IC50 2.0 nM (8.70) | none |

All ten leads are sub-3 nM by their best record; the measured-potency spread is under one log unit (pChEMBL 8.70–9.66). CHEMBL1229211 is dolutegravir's own ChEMBL record (identical MW 419.38, logP 1.35, similarity 1.0) — the duplicate is an internal consistency check, not a second compound. Cabotegravir (CHEMBL2403238) is the most potent by its best record (IC50 0.22 nM), ahead of dolutegravir's own record (0.5 nM) and ahead of the literature head-to-head values for dolutegravir (2.7 nM strand transfer). Ranks 4–10 are seven analogues from the BMS-707035 series (Naidu et al. 2018, Bioorg Med Chem Lett; document CHEMBL4118197), all reported at EC50/IC50 2.0 nM in the same strand-transfer antiviral assay — a single-assay cluster, not seven independent measurements.

### 3.2 Comparison with published potency data

The literature head-to-head values are less extreme than the ChEMBL maxima: dolutegravir strand-transfer IC50 2.7 nM (Kobayashi et al. 2011) against the ChEMBL top record of 0.5 nM for the same compound — a five-fold gap between a single-assay maximum and the standard reference value. The same caution applies to cabotegravir's 0.22 nM: it is a top record, not a head-to-head win over dolutegravir. The 2025 quadruple-mutant study is the relevant comparison instead: against G140S/Q148H-centred quadruple mutants, all three approved second-generation INSTIs lose potency while the investigational compound 4d retains it — a difference invisible in the wild-type table above, where everything is sub-3 nM.

### 3.3 The standardisation problem: similarity is not potency

The composite score's 40-point similarity component makes the ranking a similarity contest: the BMS-707035 series (similarity 0.28–0.34 to dolutegravir) scores 70–73 while dolutegravir and cabotegravir score 92–99, although the measured potencies are within one log unit of each other and the BMS compounds are, on their best records, as potent as dolutegravir itself. A reader who took the composite score at face value would conclude the BMS series is far worse; the data say it is not. Two further cautions: the EC50 figures (cell-based antiviral activity) and IC50 figures (enzyme strand transfer) in the table measure different things and cannot be ranked against each other; and the seven BMS records at exactly 2.0 nM are one assay's output, so the apparent depth of that chemotype is a single data point repeated seven times.

Drug-likeness is clean across the top 10: MW 361–505, logP 0.64–2.55, zero Lipinski violations except CHEMBL4127873 (MW 504.58, one violation). No Tox21 flags were predicted for any compound by kNN read-across — a prediction, not a measurement. Dolutegravir's long-acting sibling cabotegravir is already the clinical answer to adherence (injectable, every 2 months); a new oral INSTI must therefore beat dolutegravir on resistance, not on wild-type potency or convenience.

## 4. Discussion

### 4.1 The reframe

The question was whether a standardised screen can rank new integrase leads against dolutegravir. The answer is that the question is obsolete for wild-type enzyme: every compound in the top tier is sub-3 nM, and the ranking that the pipeline produces is driven by structural similarity to the reference, not by potency. The paper's contribution is therefore the reframe, plus a documented pipeline failure: for polyprotein targets, the standard UniProt→ChEMBL→PDB chain silently substitutes a different enzyme (protease for integrase) at all three steps, and the correction — not the docking — is the methodological result. Any future run on a viral polyprotein target must check the ChEMBL target's assay descriptions and the PDB entry's molecule name before trusting a score.

### 4.2 Why the "win" must not be over-read

Cabotegravir's 0.22 nM is a single-assay ChEMBL maximum, not a head-to-head win; the literature value for dolutegravir in the same type of assay is 2.7 nM, and the two were not measured on the same plate. The BMS series' seven identical 2.0 nM records are one assay, not seven confirmations. And no docking exists to suggest a binding-mode advantage for any compound here — the structural claims in this paper come from the published cryo-EM intasome literature, not from this run.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

No PAINS alerts were found. The validation assay still needs standard controls (detergent to expose aggregators; a counter-screen against an unrelated enzyme) and, critically, a resistant-intasome arm — wild-type potency alone cannot distinguish the leads.

### 4.4 Testable hypotheses

1. In a strand-transfer assay on wild-type intasomes, the IC50 order of cabotegravir, dolutegravir and the BMS-707035 series will be within 3-fold of each other — i.e. no meaningful wild-type difference. Refuted if any lead is >10-fold better than dolutegravir.
2. On G140S/Q148H intasomes, dolutegravir will lose 5- to 6-fold potency (as published) while at least one BMS-series compound retains wild-type potency. Refuted if all leads lose potency together.
3. The investigational compound 4d will outperform all top-10 leads on the quadruple-mutant panel (G140S/Q148H + L74/E92/T97 + E138A/K), reproducing the published result. Refuted if it does not.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): strand-transfer enzyme assay for cabotegravir, dolutegravir, BMS-707035 and the two most potent BMS analogues, wild-type integrase, 10-point dose–response in triplicate, same plate — the deliverable is a head-to-head table, replacing the ChEMBL maxima. Stage 2 (weeks 4–6): the same assay on G140S/Q148H and G118R mutant integrases, with compound 4d as comparator — the deliverable is the fold-change in IC50, which is the only number that matters for this target. Stage 3 (weeks 7–12): for the lead that survives stage 2, a cell-based antiviral assay (single-round infection) on wild-type and quadruple-mutant virus, plus a comparison of the published cryo-EM intasome structures (8FNG and the 2023 series) to rationalise the mutant result structurally. Stop rule: a lead that is potent on wild-type but loses potency on G140S/Q148H exactly like dolutegravir is a failure, not a publication — wild-type potency is not the endpoint.

## 5. Limitations

1. No docking was performed — this paper contains no binding-mode or docking-score claims at all, by design (see 2.3).
2. "Measured" potencies are single-assay ChEMBL maxima from heterogeneous assays (enzyme IC50 vs cell-based EC50); they are not head-to-head values, and dolutegravir's own record (0.5 nM) differs five-fold from the literature reference value (2.7 nM).
3. The pipeline's composite score is similarity-dominated; the ranking in Table 3.1 must not be read as a potency ranking.
4. The seven BMS-series records at 2.0 nM come from a single assay and a single publication; they are not independent confirmations.
5. The resistance discussion rests on published cryo-EM and virology, not on any measurement in this run.
6. No data are presented on pharmacokinetics, long-acting formulation, or cost — cabotegravir's clinical advantage is adherence, which this analysis does not address.
7. No local (Pakistan) epidemiological or access data beyond the national estimates in Section 1 were collected.

## 6. Conclusion

Against dolutegravir, the ChEMBL HIV-1 integrase top tier is uniformly sub-3 nM: cabotegravir leads on its best record (IC50 0.22 nM), dolutegravir's own record is 0.5 nM, and seven BMS-707035-series analogues share 2.0 nM in one assay — but the pipeline's similarity-dominated ranking obscures that equality, and none of it separates the leads where it matters, on resistant intasomes. Docking was skipped because no X-ray structure of HIV-1 integrase with a strand-transfer inhibitor exists and the pipeline's default pick was the wrong enzyme. The next step is a strand-transfer assay on wild-type versus G140S/Q148H intasomes, with compound 4d as comparator: a lead only matters if it keeps potency where dolutegravir loses it.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all tools and data sources used are free and public (UniProtKB, ChEMBL, PubChem, RCSB PDB).

## References

1. Kobayashi M, Yoshinaga T, Seki T, et al. In vitro antiretroviral properties of S/GSK1349572, a next-generation HIV integrase inhibitor. Antimicrob Agents Chemother. 2011;55(2):813–821.
2. Hare SA, Smith SJ, Métifiot M, et al. Structural and functional analyses of the second-generation integrase strand transfer inhibitor dolutegravir (S/GSK1349572). Mol Pharmacol. 2011;80(4):565–572. doi:10.1124/mol.111.073189
3. Passos DO, Li M, Yang R, et al. Cryo-EM structures and atomic model of the HIV-1 strand transfer complex intasome. Science. 2017;355(6320):89–92. PMID 28059769. doi:10.1126/science.aah5163
4. Cook NJ, Li W, Berta D, et al. Structural basis of second-generation HIV integrase inhibitor action and viral resistance. Science. 2020;367(6479):806–810. PMID 32001525. doi:10.1126/science.aay4919
5. Li M, Oliveira Passos D, Shan Z, et al. Mechanisms of HIV-1 integrase resistance to dolutegravir and potent inhibition of drug-resistant variants. Sci Adv. 2023;9(29):eadg5953. PMID 37478179. doi:10.1126/sciadv.adg5953
6. Comparative analyses of antiviral potencies of second-generation integrase strand transfer inhibitors (INSTIs) and the developmental compound 4d against a panel of integrase quadruple mutants. Viruses. 2025;17(1):121.
7. Resistance to second-generation integrase inhibitors in people with HIV following treatment failure on dolutegravir- or bictegravir-based ART in Taiwan. J Antimicrob Chemother. 2026;81(2):dkaf488. PMID 41574657. doi:10.1093/jac/dkaf488
8. Naidu BN, Walker MA, Sorenson ME, et al. The discovery and preclinical evaluation of BMS-707035, a potent HIV-1 integrase strand transfer inhibitor. Bioorg Med Chem Lett. 2018;28(12):2124–2130. PMID 29779976. doi:10.1016/j.bmcl.2018.05.027
9. Protein Data Bank. Structure of G140A HIV-1 intasome with dolutegravir bound. PDB ID 8FNG. https://www.rcsb.org/structure/8FNG
10. Protein Data Bank. HIV-1 wild type protease with GRL-04315A. PDB ID 6DV4. https://www.rcsb.org/structure/6DV4 (cited as the structure the pipeline wrongly selected for this target; not used for any result in this paper)

## Data availability

All potency values reported here are in `hidden_files/dock-HP-039-2026-11-10.json` (pipeline steps 1–6 on corrected target CHEMBL3471; docking skipped with reason recorded). Target: UniProt P04585 (Gag-Pol polyprotein; see correction note); ChEMBL target CHEMBL3471; compounds: dolutegravir (CHEMBL1229211), cabotegravir (CHEMBL2403238), CHEMBL4130252, CHEMBL4126686, CHEMBL4127923, CHEMBL4128240, CHEMBL4130102, CHEMBL4127873, CHEMBL492465. The discarded protease-structure attempt (PDB 6DV4) produced no saved output. No additional data were generated.
