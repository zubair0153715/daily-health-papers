# Midostaurin Out-Docks Gilteritinib by 2.59 kcal/mol and Loses by 8-Fold in Measured Affinity: A Centre-Audited Vina Benchmark of FLT3 Inhibitors on 6JQR

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-11 · **Health Papers Agent — Paper #43** (daily 5-paper run)

**Keywords:** FLT3; gilteritinib; acute myeloid leukaemia; FLT3-ITD; molecular docking; AutoDock Vina; F691L; drug resistance

---

## Abstract

FLT3 internal tandem duplication (FLT3-ITD) occurs in about 25% of acute myeloid leukaemia (AML) and confers poor prognosis with high relapse rates, yet gilteritinib, the FLT3 inhibitor with a proven survival benefit in relapsed or refractory disease, extends median overall survival to only 9.3 months, and gatekeeper (F691L) and activation-loop (D835) mutations erode even that benefit. The gap this paper attacks is whether a standardised docking screen can rank FLT3 inhibitors against gilteritinib at all. We docked gilteritinib, four established FLT3 inhibitors and seven PubChem analogues on the 2.20 Å gilteritinib-bound FLT3 kinase-domain structure 6JQR (AutoDock Vina 1.2.7, grid centred on the co-crystallised ligand centroid), after the ChEMBL activity endpoint returned HTTP 500 and the pipeline retrieved no ligands. Midostaurin scored best (−10.42 kcal/mol) and crenolanib second (−9.55), ahead of gilteritinib (−7.83) and quizartinib (−7.70), but against single-assay measured Kd values the ranking is uncorrelated (Spearman ρ = −0.3, p = 0.62, n = 5): midostaurin, the best by Vina, is the weakest measured binder (Kd 7.9 nM), while crenolanib, the strongest measured binder (Kd 0.28 nM), ranks second. Among the three type I inhibitors the reversal is exact (ρ = −1.0), so the failure is not a type I versus type II artefact. One PAINS-clean analogue (PubChem CID 150967523, −8.91 kcal/mol) out-scored gilteritinib by 1.08 kcal/mol, inside the ±1–2 kcal/mol Vina noise, and gilteritinib itself carries a PAINS alert, so neither is a lead claim. The falsifiable next step is a single-assay FLT3 kinase panel of the five inhibitors plus the three best analogues, with F691L and D835Y mutant arms: if the measured order follows the published Kd order rather than the Vina order, rigid docking must not be used to prioritise FLT3 leads on this structure.

---

## 1. Introduction

Leukaemia accounted for an estimated 487,294 new cases and 305,405 deaths worldwide in 2022 (GLOBOCAN 2022). Acute myeloid leukaemia (AML) is the most common acute leukaemia in adults — roughly 80% of acute leukaemia cases, with a median age at diagnosis of 68 years — and remains the deadliest. FLT3 (FMS-like tyrosine kinase 3), a class III receptor tyrosine kinase, is one of the most commonly mutated genes in AML: activating mutations occur in about 30% of cases, as internal tandem duplications (ITD) in the juxtamembrane domain in approximately 25% and as point mutations in the tyrosine kinase domain (TKD), chiefly at D835, in about 5%. FLT3-ITD disrupts the autoinhibitory juxtamembrane domain, leaving the kinase constitutively active and driving proliferation and survival through STAT5, PI3K/AKT and RAS/MAPK signalling. Patients with FLT3-ITD have higher relapse rates and inferior overall survival, and even allogeneic transplantation in first remission leaves a 30–59% relapse risk.

Gilteritinib (ASP2215) changed the relapsed/refractory setting: a type I inhibitor that binds the active (DFG-in) conformation, it inhibits FLT3 with an IC50 of 0.29 nM and AXL with 0.73 nM, about 800-fold more potent against FLT3 than against c-KIT (230 nM). In the phase 3 ADMIRAL trial (371 patients with relapsed/refractory FLT3-mutated AML), gilteritinib 120 mg daily improved median overall survival to 9.3 months versus 5.6 months with salvage chemotherapy (hazard ratio 0.64) and doubled the complete remission rate (CR/CRh 34.0% versus 15.3%), leading to FDA approval in November 2018. Quizartinib, a type II inhibitor that binds the inactive (DFG-out) conformation, improved survival in newly diagnosed FLT3-ITD AML in the QuANTUM-First trial (median overall survival 31.9 versus 15.1 months, hazard ratio 0.78) and was approved in 2023. Midostaurin, the first-generation multi-kinase inhibitor, remains the frontline FLT3 inhibitor in combination with chemotherapy, and crenolanib, a type I inhibitor, retains activity against the D835 and F691L mutants that defeat type II drugs.

The benefit is short-lived. Acquired resistance emerges through secondary kinase-domain mutations — the gatekeeper F691L, which alters the inhibitor-binding pocket and confers resistance to type I and type II inhibitors alike, and activation-loop mutations at D835, which stabilise the DFG-in conformation and defeat type II inhibitors — and through off-target mechanisms including AXL and RAS pathway activation. New scaffolds that retain activity against F691L are urgently needed, and the 2024 imidazo[1,2-a]pyridine compound 24 showed that balanced potency against FLT3-ITD, FLT3-ITD/D835Y and FLT3-ITD/F691L is achievable. The question this paper asks is narrower and prior to any of that: can a standardised docking screen rank FLT3 inhibitors against gilteritinib at all?

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen of established FLT3 inhibitors against gilteritinib on the gilteritinib-bound structure 6JQR will rank compounds in the same order as their measured binding affinities from a single-assay panel. The test is the rank correlation, not the best score.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-11 (web search; PubMed via targeted queries). The daily literature digest of 2026-11-11 screened 589 candidates and selected 8 papers, none on FLT3, so the FLT3 literature was gathered by targeted searches. Key sources: GLOBOCAN 2022 global leukaemia statistics; the 2026 ACS review of FLT3 structural biology and resistance; the ADMIRAL and QuANTUM-First phase 3 trials; the preclinical characterisation of gilteritinib; a 2020 single-assay Kd panel of five FLT3 inhibitors; the quizartinib and crenolanib primary papers; the quizartinib-bound FLT3 structure 4RT7; and a 2024 Vina study of the same four inhibitors on both DFG conformations. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P36888 (human FLT3, 993 residues); ChEMBL target CHEMBL1974 (Receptor-type tyrosine-protein kinase FLT3, single protein). Structure: PDB 6JQR, the FLT3 kinase domain in complex with gilteritinib itself, resolution 2.20 Å, deposited 2019. Grid centre [−28.04, −10.36, −28.99] — the centroid of the co-crystallised gilteritinib (ligand C6F) computed from the deposited coordinates by the pipeline's `dock._ligand_center`, which excludes cofactors, glycans, lipids and modified residues. The domain matches the drug's binding site: 6JQR is the FLT3 kinase domain with gilteritinib bound in the ATP site, not another kinase and not another domain. Box 22.5 Å, exhaustiveness 8, best of three poses reported per compound. The same grid, box and exhaustiveness were used for every compound.

A note on the run: the ChEMBL activity endpoint was down on 2026-11-11. Three pipeline runs (10:26, 10:33 and 10:34 PKT) all retrieved zero ligands — the first two because the target-components endpoint failed, the third because the activity endpoint returned HTTP 500. The outage was verified by direct query: the target endpoint returns CHEMBL1974 for UniProt P36888, while the activity endpoint returned HTTP 500 on three separate direct curls (simple and ordered queries alike). The raw JSONs of the failed runs are kept (`dock-HP-030-2026-11-11-RUN1-QUERY-ONLY.json`, `-RUN2-QUERY-ONLY.log`); no result in this paper comes from them except the gilteritinib re-dock. The fallback follows the documented 2026-11-02 FLT3 precedent: PubChem `fastsimilarity_2d` analogues of gilteritinib (85% threshold) plus four known FLT3 inhibitors as comparators, all docked with the identical protocol. Seven analogues were docked (one salt record excluded as multi-component); no measured potency is attached to any analogue. Gilteritinib was docked twice independently (pipeline run 1: −8.01 kcal/mol; fallback run: −7.83 kcal/mol), a run-to-run difference of 0.18 kcal/mol.

### 2.3 PAINS screen

RDKit PAINS filter (FilterCatalog, PAINS A/B/C) applied to every docked compound. Gilteritinib itself carries a PAINS alert, `anil_di_alk_A(478)`, on its anilino-pyrazine core; the same alert appears on the five analogues that share that core. The alert is reported, never hidden; it changes the validation design (redox and aggregation controls).

### 2.4 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds. A single rigid DFG-in structure cannot represent the conformational ensemble of the kinase, and it structurally disadvantages type II inhibitors, which bind the DFG-out conformation. No molecular dynamics or free-energy refinement was run. No experimental data were generated. Docking was performed on wild-type FLT3 only; no F691L or D835Y mutant structure was docked.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Vina best (kcal/mol) | Poses (kcal/mol) | Measured Kd, single-assay panel (nM) | PAINS |
|---|---|---|---|---|
| Midostaurin | −10.42 | −10.42, −8.73, −8.33 | 7.9 | none |
| Crenolanib | −9.55 | −9.55, −9.45, −9.31 | 0.28 | none |
| PubChem CID 150967523 | −8.91 | −8.91, −8.74, −8.16 | none (similarity analogue) | none |
| Sorafenib | −8.28 | −8.28, −8.06, −8.01 | 5.9 | none |
| PubChem CID 138319679 | −8.12 | −8.12, −7.97, −7.91 | none (similarity analogue) | anil_di_alk_A(478) |
| PubChem CID 66642725 | −8.05 | −8.05, −7.94, −7.50 | none (similarity analogue) | none |
| Gilteritinib (reference) | −7.83 | −7.83, −7.60, −7.50 | 1.0 | anil_di_alk_A(478) |
| PubChem CID 124086185 | −7.83 | −7.83, −7.65, −7.63 | none (similarity analogue) | anil_di_alk_A(478) |
| PubChem CID 66642864 | −7.76 | −7.76, −7.64, −7.63 | none (similarity analogue) | anil_di_alk_A(478) |
| PubChem CID 166626288 | −7.75 | −7.75, −7.68, −7.59 | none (similarity analogue) | anil_di_alk_A(478) |
| Quizartinib | −7.70 | −7.70, −7.07, −6.85 | 3.3 | none |
| PubChem CID 155533199 | −7.48 | −7.48, −7.44, −7.26 | none (similarity analogue) | anil_di_alk_A(478) |

All twelve docks are on 6JQR (2.20 Å), grid centre on the co-crystallised gilteritinib centroid. Measured Kd values are from a single 2020 panel in which all five inhibitors were assayed under the same conditions against 404 kinases (duplicate 11-point dose–response curves); they are the only measured values used for the rank test, so assay heterogeneity cannot explain a ranking failure. Gilteritinib's independent re-dock in pipeline run 1 gave −8.01 kcal/mol, 0.18 kcal/mol from the fallback value reported here.

Midostaurin out-scores gilteritinib by 2.59 kcal/mol — a margin larger than the ±1–2 kcal/mol noise band, so this is not a noise artefact. Crenolanib out-scores gilteritinib by 1.72 kcal/mol. The best analogue, CID 150967523, out-scores gilteritinib by 1.08 kcal/mol, inside the noise band. The other two analogues that out-score gilteritinib do so by 0.29 kcal/mol (CID 138319679) and 0.22 kcal/mol (CID 66642725), both inside noise. Pose consistency is good for most compounds (top-three poses within ~1 kcal/mol) except midostaurin, whose poses span 2.09 kcal/mol (−10.42 to −8.33), the least consistent set in the table. All four known comparators except gilteritinib are PAINS-clean; gilteritinib and five of its seven analogues carry the same `anil_di_alk_A(478)` alert.

Drug-likeness of the docked set: crenolanib is the most drug-like known inhibitor (MW 443.55, logP 3.92, zero Lipinski violations, TPSA 78.43 Å²). Gilteritinib (MW 552.72, logP 2.70, TPSA 121.11 Å²), midostaurin (MW 570.65, logP 5.91), quizartinib (MW 560.68, logP 5.86) and sorafenib (MW 464.83, logP 5.55) each carry one Lipinski violation. The best analogue CID 150967523 (MW 542.68, logP 5.49, TPSA 82.20 Å²) also carries one violation and contains an acrylamide group, a potential Michael acceptor that the PAINS filter did not flag.

### 3.2 Comparison with published docking

The only published Vina study of the same four inhibitors (Carranza-Aranda et al. 2024, Vina 1.1.2) docked sorafenib, midostaurin, gilteritinib and quizartinib on homology models of wild-type and ITD-mutated FLT3 in both DFG-out and DFG-in conformations, and reported higher affinities for the second-generation inhibitors (gilteritinib, quizartinib) than for the first-generation ones (sorafenib, midostaurin) on both conformations, with in vitro data supporting the predictions. Our single-structure DFG-in run gives the opposite generation order — a first-generation drug first. The difference is the structure: they sampled both conformations; we used one DFG-in structure. No published Vina scores on 6JQR itself were found for these inhibitors, so no absolute-score comparison is possible; as with VEGFR2, absolute Vina scores are protocol- and structure-dependent and cannot be compared across studies.

### 3.3 The standardisation problem: the ranking is uncorrelated, and exactly reversed among type I inhibitors

For the five known inhibitors, the Vina order (best first) is midostaurin > crenolanib > sorafenib > gilteritinib > quizartinib. The measured-Kd order (best first) is crenolanib (0.28 nM) > gilteritinib (1.0 nM) > quizartinib (3.3 nM) > sorafenib (5.9 nM) > midostaurin (7.9 nM). Spearman rank correlation ρ = −0.3 (p = 0.62, n = 5): no positive correlation. The compound Vina ranks first is the weakest by measured affinity, by a factor of 7.9 against gilteritinib and 28 against crenolanib.

The obvious confounder is conformation: 6JQR is a DFG-in structure, and the two type II inhibitors (quizartinib, sorafenib) bind the DFG-out conformation, so they are penalised by construction. But the failure survives removing that confounder. Among the three type I inhibitors alone — midostaurin, crenolanib and gilteritinib, all of which bind the DFG-in conformation this structure represents — the reversal is exact: Vina ranks midostaurin > crenolanib > gilteritinib, while measurement ranks crenolanib > gilteritinib > midostaurin (ρ = −1.0, n = 3). The scoring function does not recover the experimental order even where the conformation is right.

A secondary observation: the seven analogues are all gilteritinib-like pyrazine-carboxamides, not new chemotypes — except CID 150967523, which replaces the pyrazine core with an acrylamide-bearing scaffold. None of the seven beats gilteritinib beyond noise, and the best-scoring one carries the acrylamide caveat. The screen therefore produced no lead claim, only a shortlist for assay.

## 4. Discussion

### 4.1 The reframe

The question was whether docking can rank FLT3 inhibitors against gilteritinib. The answer on this structure is no — not because the setup was wrong (the grid is on the co-crystallised ligand, the structure is the drug's own complex, the reference reproduces to 0.18 kcal/mol across independent runs) but because the scoring function does not recover the experimental order, and the largest error (midostaurin, 2.59 kcal/mol) exceeds the noise band. The honest headline is therefore a negative result about the method, not a lead claim. A paper that reported "midostaurin beats gilteritinib" from the raw scores would have been wrong in exactly the way the field keeps being wrong — and midostaurin is a drug already in the clinic, so the error is checkable in a way a novel-scaffold error would not be.

### 4.2 Why the "win" must not be over-read

Four reasons. First, the only margin that exceeds noise is the one that is wrong: midostaurin's 2.59 kcal/mol lead over gilteritinib corresponds to the weakest measured binder. Second, midostaurin has the least consistent poses in the set (2.09 kcal/mol spread), so even its own best score is the least trustworthy. Third, the ranking is uncorrelated with measurement overall (ρ = −0.3) and exactly reversed among the type I inhibitors (ρ = −1.0), so no subset of the ranking survives. Fourth, all five known inhibitors are single-digit nanomolar binders by measurement (Kd 0.28–7.9 nM); the practical difference between them is selectivity, mutant coverage and pharmacokinetics, none of which a single-structure docking score measures. The 2024 Carranza-Aranda study is the right contrast: it paired docking on both conformations with measured cell viability, and the assay was the verdict.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

Gilteritinib itself — an approved drug — carries the `anil_di_alk_A(478)` PAINS alert, as do five of its seven analogues. A filter that flags the reference drug cannot be used to discard the scaffold; it is a prompt for controls. The validation assay therefore needs detergent to expose aggregators, a counter-screen against an unrelated kinase, and a redox control, for every analogue including the PAINS-clean ones. The two PAINS-clean analogues (CID 150967523 and CID 66642725) are the only ones that could advance without the PAINS caveat — but CID 150967523 carries an acrylamide, so it additionally needs a glutathione-reactivity check before any potency claim, since a covalent warhead would make a reversible-binding assay misleading.

### 4.4 Testable hypotheses

1. In a single-assay FLT3 kinase panel (ADP-Glo or TR-FRET, gilteritinib control on the same plate), the Kd/IC50 order of the five known inhibitors will follow the published Kd order (crenolanib > gilteritinib > quizartinib > sorafenib > midostaurin), not the Vina order. Refuted if the Vina order reproduces.
2. Re-docking the same five inhibitors on the quizartinib-bound structure 4RT7 (DFG-out, 3.1 Å) will change the Vina order — quizartinib and sorafenib will improve relative to the type I drugs — showing the ranking is structure-dependent. Refuted if the order is identical.
3. The best analogue CID 150967523 will inhibit FLT3-ITD MV4-11 proliferation with an IC50 within 10× of gilteritinib's 0.92 nM (i.e. ≤ ~10 nM) and retain activity against FLT3-ITD/F691L within 10× of its FLT3-ITD value. Refuted if its IC50 exceeds 100 nM or the F691L shift exceeds 10×.
4. The `anil_di_alk_A(478)` alert on the gilteritinib scaffold is a filter artefact for this chemotype, not a redox or aggregation artefact: the analogues' kinase inhibition will survive detergent and redox controls. Refuted if activity collapses under those controls.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): FLT3 kinase assay for the five known inhibitors plus the three best analogues (CID 150967523, CID 138319679, CID 66642725), 10-point dose–response in triplicate, gilteritinib control on the same plate, with detergent, aggregation and redox controls; wild-type, F691L and D835Y enzymes in the same panel to test hypotheses 1 and 4. Stage 2 (weeks 4–6): MV4-11 and MOLM-14 viability for the analogues that survive stage 1, plus Ba/F3 cells expressing FLT3-ITD, FLT3-ITD/F691L and FLT3-ITD/D835Y, to test hypothesis 3. Stage 3 (weeks 7–12): re-docking on 4RT7 and a 100 ns molecular-dynamics plus MM-GBSA rescoring to test hypothesis 2, and a glutathione-reactivity assay for CID 150967523. Stop rule: if stage 1 reproduces the published Kd order, the Vina ranking is discarded and the project proceeds on measured potency only; if an analogue fails the detergent or redox controls, it is dropped regardless of its score.

## 5. Limitations

1. Docking only — no experimental data; no compound here is shown to inhibit FLT3 in any assay.
2. The ChEMBL activity endpoint was down (HTTP 500, verified three times), so no ChEMBL-derived leads were screened; the analogues come from PubChem similarity only and carry no measured potency.
3. Single rigid DFG-in structure (6JQR); type II inhibitors are penalised by construction, and no MD or free-energy refinement was run.
4. Wild-type FLT3 only — no F691L or D835Y mutant structure was docked, so nothing here addresses the resistance mutations that motivate the work.
5. Rank correlation computed on n = 5 known inhibitors (n = 3 for the type I trio) — a perfect ρ = −1.0 on three points is striking but fragile.
6. Measured Kd values come from one 2020 panel; other assays give different absolute values (crenolanib 0.28 nM here versus 0.74 nM in Galanis et al.), though the rank order is the same.
7. Gilteritinib's re-dock varied by 0.18 kcal/mol between independent runs (conformer sampling); all margins below ~0.2 kcal/mol are therefore meaningless.
8. No local (Pakistan) market, pricing or access data were collected; gilteritinib and quizartinib availability and cost in Pakistan were not assessed.

## 6. Conclusion

Five established FLT3 inhibitors docked on the gilteritinib-bound structure 6JQR do not rank in their measured potency order (Spearman ρ = −0.3, n = 5), and among the three type I inhibitors the reversal is exact (ρ = −1.0): midostaurin, the weakest measured binder, scores best by 2.59 kcal/mol. No PubChem analogue beats gilteritinib beyond Vina noise, and the reference drug itself carries a PAINS alert. The benchmark's value is the negative result: rigid docking on this structure cannot prioritise FLT3 inhibitors, and any lead claim built on these scores alone would be unjustified. The next step is a head-to-head FLT3 kinase assay of the five inhibitors and the three best analogues, with F691L and D835Y mutant arms, which will settle whether the published Kd order or the Vina order is real.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all tools and data sources used are free and public (UniProtKB, ChEMBL, PubChem, RCSB PDB, AutoDock Vina).

## References

1. Bray F, Laversanne M, Sung H, et al. Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. CA Cancer J Clin. 2024;74(3):229–263. doi:10.3322/caac.21834
2. Yan YF, et al. Epidemiological characteristics of leukemia in China and worldwide. Zhonghua Zhong Liu Za Zhi. 2025. PMID 41443736. (GLOBOCAN 2022: 487,294 new leukaemia cases, 305,405 deaths.)
3. Rodrigues da Silva M, Lima LM, Barbosa MLC. Targeting FLT3 in acute myeloid leukemia: structural insights and key challenges. ACS Bio Med Chem Au. 2026;6(4):305–322.
4. Perl AE, Martinelli G, Cortes JE, et al. Gilteritinib or chemotherapy for relapsed or refractory FLT3-mutated AML. N Engl J Med. 2019;381(18):1728–1740. doi:10.1056/NEJMoa1902688. PMID 31665578.
5. Erba HP, Montesinos P, Kim HJ, et al. Quizartinib plus chemotherapy in newly diagnosed patients with FLT3-internal-tandem-duplication-positive acute myeloid leukaemia (QuANTUM-First): a randomised, double-blind, placebo-controlled, phase 3 trial. Lancet. 2023;401(10388):1571–1583. doi:10.1016/S0140-6736(23)00464-6. PMID 37116523.
6. Lee LY, Hernandez D, Rajkhowa T, et al. Preclinical studies of gilteritinib, a next-generation FLT3 inhibitor. Blood. 2017;129(2):257–260. doi:10.1182/blood-2016-10-745133. PMID 27908881.
7. Mori M, Kaneko N, Ueno Y, et al. Gilteritinib, a FLT3/AXL inhibitor, shows antileukemic activity in mouse models of FLT3 mutated acute myeloid leukemia. Invest New Drugs. 2017;35(5):556–565. doi:10.1007/s10637-017-0470-z. PMID 28516360.
8. Aikawa T, Togashi N, Iwanaga K, et al. Quizartinib, a selective FLT3 inhibitor, maintains antileukemic activity in preclinical models of RAS-mediated midostaurin-resistant acute myeloid leukemia cells. Oncotarget. 2020;11:943. PMID 32215183. PMCID PMC7082118.
9. Zarrinkar PP, Gunawardane RN, Cramer MD, et al. AC220 is a uniquely potent and selective inhibitor of FLT3 for the treatment of acute myeloid leukemia. Blood. 2009;114(14):2984–2992. doi:10.1182/blood-2009-05-222034.
10. Galanis A, Ma H, Rajkhowa T, et al. Crenolanib is a potent inhibitor of FLT3 with activity against resistance-conferring point mutants. Blood. 2014;123(1):94–100. doi:10.1182/blood-2013-10-529313.
11. Wilhelm SM, Carter C, Tang L, et al. BAY 43-9006 exhibits broad spectrum oral antitumor activity and targets the RAF/MEK/ERK pathway and receptor tyrosine kinases involved in tumor progression and angiogenesis. Cancer Res. 2004;64(19):7099–7109. doi:10.1158/0008-5472.CAN-04-1443.
12. Smith CC, Zhang C, Lin KC, et al. Characterizing and overriding the structural mechanism of the quizartinib-resistant FLT3 gatekeeper mutation. Cancer Discov. 2015;5(6):668–679. doi:10.1158/2159-8290.CD-15-0060. PMID 25847190.
13. Wang X, DeFilippis RA, Weldemichael T, et al. An imidazo[1,2-a]pyridine-pyridine derivative potently inhibits FLT3-ITD and FLT3-ITD secondary mutants, including gilteritinib-resistant FLT3-ITD/F691L. Eur J Med Chem. 2024;264:115977. doi:10.1016/j.ejmech.2023.115977. PMID 38056299.
14. Carranza-Aranda AS, Jave-Suárez LF, Flores-Hernández FY, et al. In silico and in vitro study of FLT3 inhibitors and their application in acute myeloid leukemia. Mol Med Rep. 2024;30(6):229. doi:10.3892/mmr.2024.13353. PMID 39392050.
15. Protein Data Bank. Crystal structure of FLT3 in complex with gilteritinib. PDB ID 6JQR, resolution 2.20 Å. https://www.rcsb.org/structure/6JQR
16. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J Chem Inf Model. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-030-2026-11-11.json` (fallback run: 5 known inhibitors + 7 PubChem analogues on 6JQR); the gilteritinib re-dock from pipeline run 1 (−8.01 kcal/mol) is in `hidden_files/dock-HP-030-2026-11-11-RUN1-QUERY-ONLY.json`; the fallback docking script is `hidden_files/dock_fallback_HP030.py`. Target: UniProt P36888; ChEMBL target CHEMBL1974 (activity endpoint returned HTTP 500 on 2026-11-11, verified by direct query); structure PDB 6JQR; compounds: gilteritinib (PubChem CID 49803313), quizartinib (CID 24889392), midostaurin (CID 9829523), crenolanib (CID 10366136), sorafenib (CID 216239), analogues CID 66642864, 124086185, 166626288, 138319679, 155533199, 66642725, 150967523. No additional data were generated.
