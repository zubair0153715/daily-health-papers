# The Best Docking Score Is the Weakest Measured Binder: A Centre-Audited PPAR-gamma Screen Against Pioglitazone on 9F7W, with a Corrected ChEMBL Target

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-11 · **Health Papers Agent — Paper #45** (daily 5-paper run)

**Keywords:** PPAR-gamma; pioglitazone; partial agonist; molecular docking; AutoDock Vina; type 2 diabetes; thymoquinone; SPPARM

---

## Abstract

Type 2 diabetes affects 589 million adults worldwide, and Pakistan carries the world's highest age-standardised prevalence at 31.4%, yet the most effective insulin sensitiser, pioglitazone, is limited by PPAR-gamma-driven weight gain of about 3.5 kg over six months and oedema in about 5% of patients. The gap this paper attacks is whether a standardised docking screen can rank partial-agonist candidates against pioglitazone at all, and whether thymoquinone, a natural product with reported PPAR-gamma activity, binds the receptor at all. We ran the LeadForge pipeline (UniProtKB P37231 → ChEMBL → PubChem → RDKit ADMET/PAINS → AutoDock Vina 1.2.7) and docked four ChEMBL PPAR-gamma actives, pioglitazone and thymoquinone into the 1.25 Å PPAR-gamma ligand-binding-domain structure 9F7W, with the grid centre audited to 0.01 Å from the co-crystallised ligand. The first pipeline run silently retrieved maltase-glucoamylase actives instead of PPAR-gamma actives; the audit caught it, and the run was repeated against the verified target CHEMBL235. One lead out-scored pioglitazone — CHEMBL6145236 at −10.24 versus −9.00 kcal/mol — but the margin (1.24 kcal/mol) sits at the edge of the ±1–2 kcal/mol Vina noise, and the ranking is reversed against measured potency: Spearman ρ = −0.8 (n = 4), with the strongest measured binder (CHEMBL1813011, EC50 0.018 nM) ranking third by Vina. Thymoquinone docked weakly (−6.25 kcal/mol) and carries a PAINS quinone alert. The falsifiable next step is a PPAR-gamma transactivation assay of the four leads against pioglitazone: if the measured EC50 order matches the ChEMBL record rather than the Vina order, docking alone must not be used to prioritise PPAR-gamma leads on this structure.

---

## 1. Introduction

Diabetes affected an estimated 589 million adults aged 20–79 worldwide in 2024, about one in nine people, and the International Diabetes Federation projects 853 million by 2050. Pakistan carries the world's highest age-standardised diabetes prevalence at 31.4%, with an estimated 34.5 million adults affected in 2024, about 226,752 diabetes-related deaths that year, and a projected 70.2 million cases by 2050. In a country where the disease burden is this large, an insulin sensitiser that works without adding weight or fluid is not a refinement — it is the difference between a drug patients can stay on and one they cannot.

Pioglitazone is the most effective insulin sensitiser in routine use. It is a thiazolidinedione and a full agonist of peroxisome proliferator-activated receptor gamma (PPAR-gamma, UniProt P37231), a ligand-activated nuclear receptor that is the master regulator of adipocyte differentiation and a key controller of glucose and lipid metabolism. Full PPAR-gamma activation improves insulin sensitivity in muscle, fat and liver — but it also drives the drug's two dose-limiting effects: weight gain of about 5%, roughly 3.5 kg over six months, and water retention with leg oedema in about 5% of patients, with peripheral oedema reported in 2–5% on monotherapy and 5–15% when combined with insulin. The fluid retention is mechanistically tied to PPAR-gamma itself: the receptor is expressed in the renal collecting duct, where activation increases sodium reabsorption, and collecting-duct-specific deletion of PPAR-gamma abolishes thiazolidinedione-induced fluid retention in mice. Intravascular volume rises by about 6–7% on glitazones, which is why the class carries a boxed warning for heart failure.

The field's answer has been to separate insulin sensitisation from full agonism. Two lines of evidence show it can be done. First, obesity-linked phosphorylation of PPAR-gamma at Ser273 by cyclin-dependent kinase 5 (Cdk5) dysregulates a specific gene set — including the insulin-sensitising adipokine adiponectin — without changing the receptor's adipogenic capacity, and anti-diabetic PPAR-gamma ligands block this phosphorylation independently of classical transcriptional agonism. Second, ligands built on that insight work in animals: SR1664, a non-agonist PPAR-gamma ligand that blocks Ser273 phosphorylation, has anti-diabetic activity roughly equivalent to rosiglitazone in obese mice while causing no fluid retention or weight gain; and GQ-16, a thiazolidinedione-derived partial agonist, retains rosiglitazone-like anti-diabetic efficacy in mice with no weight gain or oedema, while blocking Cdk5-mediated phosphorylation. These compounds are selective PPAR-gamma modulators (SPPARMs) — ligands whose dose–response relationships for different activities are uncoupled, so that insulin sensitisation is kept and adipogenesis is not.

Thymoquinone, the active constituent of black seed (*Nigella sativa*), is a candidate from the natural-product side: in high-fat-diet plus streptozotocin diabetic rats it lowered glucose, improved HOMA-IR and raised PPAR-gamma levels, and an earlier docking study on the pioglitazone-bound structure 2XKW reported pioglitazone at −9.4 and thymoquinone at −7.0 kcal/mol. But thymoquinone is a 1,4-benzoquinone — a redox-active chemotype that the PAINS filter flags — so any PPAR-gamma signal from it must survive artefact controls before it is believed.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen of ChEMBL PPAR-gamma actives against pioglitazone on a high-resolution PPAR-gamma ligand-binding-domain structure will rank compounds in the same order as their measured potencies, and thymoquinone will bind the same pocket measurably worse than pioglitazone. The test is the rank correlation, not the best score.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-11 (web search; PubMed/bioRxiv via the daily digest of 2026-11-11, which screened 589 candidates and selected 8, none on PPAR-gamma — the digest's relevance is methodological, not topical, for this paper). Key sources: the IDF Diabetes Atlas 11th edition (2025) for the burden numbers; Choi et al. 2010 and 2011 for the Cdk5–Ser273 mechanism and SR1664; Amato et al. 2012 for GQ-16; Yang and Soodvilai 2008 for the collecting-duct mechanism of fluid retention; Megantara et al. 2017 for the earlier thymoquinone–pioglitazone docking comparison; and Alshahrani et al. 2021 for thymoquinone's in vivo PPAR-gamma data. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P37231 (human PPAR-gamma, PPARG, 505 aa); ChEMBL target CHEMBL235 (verified: "Peroxisome proliferator-activated receptor gamma"); 44 bioactivities retrieved with pChEMBL ≥ 5, 26 leads after RDKit filtering and ranking; the top 4 leads docked plus the reference query (pioglitazone, PubChem CID 4829, verified live) and, separately, thymoquinone (PubChem CID 10281, verified live). Structure: PDB 9F7W, the human PPAR-gamma ligand-binding domain in complex with a coactivator-1-alpha peptide and bisphenol A, resolution 1.25 Å. Grid centre [47.10, 6.91, 1.39] — audited against the co-crystallised ligand bisphenol A (residue 501) centroid computed from the deposited coordinates: distance 0.01 Å, i.e. the grid is exactly on the ligand-binding pocket. (A second bisphenol A copy, residue 502, sits 12.24 Å from the centre at a surface site and was not used.) Best of three poses reported per compound. The same grid, box (22.5 Å) and exhaustiveness were used for every compound including pioglitazone. Pioglitazone was docked twice, once in each pipeline run, and reproduced to 0.04 kcal/mol (−9.04 and −9.00), a reproducibility control for the setup.

A note on the run, and the reason Section 3.3 exists: the first pipeline run resolved the ChEMBL target incorrectly. The UniProt-accession lookup returned CHEMBL2074, "Maltase-glucoamylase", and the pipeline pulled 55 bioactivities for that target. The error was caught by checking the retrieved target name against the UniProt protein before writing the paper: the docked "leads" were polyhydroxylated iminosugar-like molecules, the classic alpha-glucosidase-inhibitor chemotype, not PPAR-gamma ligands. The first ChEMBL call in the corrected re-run also failed (EBI API error, a known same-day flakiness), and succeeded on the single permitted retry with the plain environment. No result in the comparison table comes from the wrong-target run; its numbers are reported separately, in Section 3.3, as the audit finding.

### 2.3 PAINS screen

RDKit PAINS filter (the pipeline's own filter, classes A–C) applied to every docked compound. The four ChEMBL leads and pioglitazone are clean. Thymoquinone carries one PAINS alert — its 1,4-benzoquinone core — reported in the table, not hidden; it changes the validation design (redox controls, Section 4.3).

### 2.4 Honesty limits

Docking is not activity, and for a nuclear receptor it is doubly not efficacy: a docking score cannot distinguish a full agonist from a partial agonist or a non-agonist binder, which is the entire question this paper asks. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds. A single rigid structure (9F7W, coactivator-bound, bisphenol A in the pocket) cannot represent the conformational ensemble of the ligand-binding domain, and bisphenol A is a weak partial agonist, not a thiazolidinedione, so the pocket conformation is not the pioglitazone-bound one. No molecular dynamics or free-energy refinement was run. No experimental data were generated. Measured potencies come from heterogeneous ChEMBL assays (EC50 vs Ki, different assay conditions); pChEMBL values are not head-to-head measurements. No measured PPAR-gamma potency for pioglitazone itself was retrieved in this run, so the reference enters the rank test by docking score only.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Vina best (kcal/mol) | Poses (kcal/mol) | Measured potency (ChEMBL235) | pChEMBL | PAINS |
|---|---|---|---|---|---|
| CHEMBL6145236 | −10.24 | −10.24, −9.38, −9.38 | EC50 0.49 nM | 9.31 | none |
| Pioglitazone (query) | −9.00 | −9.00, −8.48, −8.39 | — (not retrieved) | — | none |
| CHEMBL65805 | −8.60 | −8.60, −8.32, −8.09 | Ki 0.4 nM | 9.40 | none |
| CHEMBL1813011 | −8.57 | −8.57, −7.67, −7.64 | EC50 0.018 nM | 10.74 | none |
| CHEMBL1813008 | −8.52 | −8.52, −7.55, −7.36 | EC50 0.05 nM | 10.30 | none |
| Thymoquinone (extra) | −6.25 | −6.25, −6.21, −6.16 | — (no ChEMBL PPAR-gamma potency) | — | alert (quinone) |

All six docks are on 9F7W (1.25 Å), grid centre exactly on the co-crystallised ligand centroid (0.01 Å). Pioglitazone reproduced to 0.04 kcal/mol across the two runs (−9.04, −9.00).

One lead out-scores pioglitazone: CHEMBL6145236, by 1.24 kcal/mol. That margin sits at the edge of Vina's ±1–2 kcal/mol noise — it is the only margin in the table that even approaches significance, and it does not exceed the noise band. The other three leads score 0.40–0.48 kcal/mol *worse* than pioglitazone, deep inside noise. Pose consistency is good for the top two (top-three poses within ~0.9 kcal/mol) and weaker for CHEMBL1813011 and CHEMBL1813008 (spread ~0.9–1.2 kcal/mol), which is itself a small warning about those two poses.

The four leads are all sub-nanomolar by measurement (EC50/Ki 0.018–0.49 nM), spanning only 1.43 log units of pChEMBL (9.31–10.74). CHEMBL6145236 is the most drug-like of the set by the pipeline's own descriptors: lowest logP (2.14), fewest rotatable bonds (2), zero Lipinski violations, TPSA 103.68 Å² — and its scaffold is the most distinct from pioglitazone (a quinolinone–carbonitrile–sulfone, similarity 0.163, versus the oxazole-acid pair CHEMBL1813008/CHEMBL1813011, similarity 0.26–0.27). The two oxazole acids are close analogues of each other and carry the highest logP in the set (4.37–4.67). None of the four is a proven partial agonist: all four are recorded in ChEMBL as PPAR-gamma actives with sub-nanomolar potency, which is what full agonists look like too. Binding strength says nothing about efficacy.

Thymoquinone docked at −6.25 kcal/mol, 2.75 kcal/mol worse than pioglitazone, with tight poses (−6.25, −6.21, −6.16) — a consistent but weak fit — and it carries the PAINS quinone alert. It was not in the pipeline's ChEMBL top 26 (its similarity to pioglitazone is low), so it was docked separately on the identical protocol; its score is directly comparable to the table.

Pioglitazone's own Tox21 measured flags (from the pipeline's safety panel) are worth recording without over-reading: NR-PPAR-gamma active (expected — it is a PPAR-gamma agonist), SR-ARE active and SR-MMP active. These are assay-activity flags from Tox21, not clinical toxicity findings, and the four leads carry only low kNN read-across probabilities on the same panel (highest single value: SR-MMP 0.397 for CHEMBL6145236) — predictions, not measurements, and not a safety claim.

### 3.2 Comparison with published docking

The only directly comparable published docking is Megantara et al. 2017, who docked thymoquinone and pioglitazone on 2XKW, the pioglitazone-bound PPAR-gamma structure, with AutoDock Vina 1.1: pioglitazone −9.4, thymoquinone −7.0 kcal/mol. Our numbers on 9F7W are pioglitazone −9.00 and thymoquinone −6.25. The direction is the same — pioglitazone binds the pocket about 2.7–2.8 kcal/mol more strongly than thymoquinone in both studies — while the absolute values differ, as expected across structures and Vina versions. That agreement in direction, across two structures and two Vina versions, is the most robust docking result in this paper, and it is also the least surprising: a small quinone is not a thiazolidinedione.

### 3.3 The standardisation problem: the first run docked the wrong target's ligands

The first pipeline run is reported here because the failure mode matters more than the numbers. It resolved UniProt P37231 to ChEMBL CHEMBL2074, "Maltase-glucoamylase", pulled 55 bioactivities for that target, and docked the top leads into the (correct) PPAR-gamma structure 9F7W:

| Compound (wrong-target run) | Vina best (kcal/mol) | Quoted potency — against MGAM, not PPAR-gamma |
|---|---|---|
| CHEMBL5558505 | −9.10 | IC50 420 nM (pChEMBL 6.38) |
| Pioglitazone (query) | −9.04 | — |
| CHEMBL3349446 | −7.27 | IC50 330 nM (pChEMBL 6.48) |
| CHEMBL332802 | −7.03 | Ki 28 nM (pChEMBL 7.55) |
| CHEMBL3349435 | −6.98 | IC50 230 nM (pChEMBL 6.64) |

Nothing in that table is a PPAR-gamma result. The quoted potencies are maltase-glucoamylase potencies, the docked molecules are alpha-glucosidase-class iminosugars (three of the four are polyhydroxylated aminocyclitol-like scaffolds), and the one apparently interesting number — CHEMBL5558505 "beating" pioglitazone by 0.06 kcal/mol — is a cross-target accident. The pipeline reported every step as "ok": the failure was silent, and only the name check (CHEMBL2074 ≠ PPAR-gamma) caught it. The corrected run (Section 3.1) re-pulled against CHEMBL235 and is the only run the paper's conclusions rest on. The fix, for the pipeline, is a one-line assertion: the resolved ChEMBL target's preferred name must contain the UniProt gene or protein name before any ligand is retrieved. Until that assertion exists, every LeadForge run needs this manual check — which is why this section is in the paper rather than in a log file.

### 3.4 The ranking is reversed

For the four distinct ChEMBL leads, the Vina order (best first) is CHEMBL6145236 > CHEMBL65805 > CHEMBL1813011 > CHEMBL1813008. The measured-potency order (pChEMBL, best first) is the exact reverse for the top and bottom: CHEMBL1813011 (10.74) > CHEMBL1813008 (10.30) > CHEMBL65805 (9.40) > CHEMBL6145236 (9.31). Spearman rank correlation ρ = −0.8 (n = 4). The compound Vina ranks first is the weakest by measured potency; the strongest measured binder ranks third by Vina. As in the VEGFR2 benchmark in this same series, the reversal is a ranking failure among near-equal compounds — all four are sub-nanomolar, spanning 1.43 log units — not a failure to detect a weak binder. But it is a complete ranking failure all the same, and it is the paper's main result: on 9F7W, under this protocol, Vina cannot order PPAR-gamma ligands, and the single "win" over pioglitazone is the least trustworthy number in the table.

## 4. Discussion

### 4.1 The reframe

The question was whether docking can rank PPAR-gamma leads against pioglitazone, and whether thymoquinone belongs in the pocket at all. The answer to the first half is no — not because the setup was wrong (the grid is exactly on the ligand, the reference reproduces to 0.04 kcal/mol across runs, poses are consistent) but because the scoring function does not recover the experimental order even among four sub-nanomolar binders. The answer to the second half is that thymoquinone does dock, weakly and consistently, 2.75 kcal/mol worse than pioglitazone — the same direction as the published 2XKW comparison — but its PAINS alert means the binding itself is not yet evidence of PPAR-gamma activity. The honest headline is therefore a double negative result about the method and about thymoquinone, plus one genuine lead for the assay queue: CHEMBL6145236, the only compound in the set that is simultaneously the best Vina scorer, the most drug-like by descriptors, and the most structurally distinct from pioglitazone — which is exactly the profile a partial-agonist search wants, and exactly the profile docking cannot validate.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 1.24 kcal/mol margin sits at the edge of the ±1–2 kcal/mol noise and does not exceed it. Second, the ranking is anti-correlated with measurement (ρ = −0.8), and the "winner" is the weakest measured binder of the four. Third, and specific to this target, a docking score cannot measure what matters: efficacy. A partial agonist and a full agonist can have identical binding affinities and opposite clinical profiles — GQ-16 and rosiglitazone differ in efficacy, not in whether they occupy the pocket. The property that would make CHEMBL6145236 valuable (partial agonism, Ser273-phosphorylation blockade without full transactivation) is invisible to Vina by construction. The compound's value is as a test case for the assay, not as a claim.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

Thymoquinone's 1,4-benzoquinone core is redox-active: quinones cycle redox, generate reactive oxygen species and can produce assay signals that look like target activity. That does not prove its PPAR-gamma signal is an artefact — the in vivo rat data (raised PPAR-gamma levels, improved HOMA-IR) and two independent docking studies pointing the same way are real, if weak, evidence — but it does fix the design of the validation: every thymoquinone assay needs a reducing-agent control (e.g. dithiothreitol), a catalase control, and a counter-screen against an unrelated nuclear receptor, so that a redox artefact has somewhere to show itself. The same controls apply, in milder form, to the four leads: all four are hydrophobic (logP 2.14–4.67) and hydrophobic aggregators are the other classic source of false inhibition.

### 4.4 Testable hypotheses

1. In a PPAR-gamma transactivation assay (reporter gene, pioglitazone and rosiglitazone controls on the same plate), the EC50 order of the four leads will follow the ChEMBL pChEMBL order, not the Vina order — i.e. CHEMBL1813011 will be the most potent and CHEMBL6145236 the least. Refuted if the Vina order reproduces.
2. Re-docking the same five compounds on 2XKW (the pioglitazone-bound structure) will change the Vina order, showing the ranking is structure-dependent. Refuted if the order is identical.
3. CHEMBL6145236 will show lower maximal transactivation efficacy than pioglitazone (partial agonism) while blocking Cdk5-mediated Ser273 phosphorylation in adipocytes — the profile that would make it a SPPARM candidate rather than just another full agonist. Refuted if it is a full agonist with efficacy equal to pioglitazone.
4. Thymoquinone's apparent PPAR-gamma activity in the transactivation assay will disappear under reducing-agent (dithiothreitol) and catalase controls, consistent with a redox artefact from its quinone core. Refuted if the signal survives the controls.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): PPAR-gamma transactivation assay (luciferase reporter, HEK293 or similar) for the four leads + pioglitazone + rosiglitazone, 10-point dose–response in triplicate, same plate, reporting both EC50 and maximal efficacy as a percentage of rosiglitazone — efficacy, not just potency, is the readout that matters for partial agonism. Thymoquinone runs in the same assay with dithiothreitol and catalase arms. Detergent and aggregation controls throughout. Stage 2 (weeks 4–6): Cdk5 Ser273-phosphorylation assay in cultured adipocytes for the best lead only (western blot for phospho-Ser273 PPAR-gamma, rosiglitazone and SR1664-style controls), plus 3T3-L1 adipogenesis with aP2/FABP4 readout as the adipogenicity proxy for the weight-gain question. Stage 3 (weeks 7–12): re-docking on 2XKW and a short molecular-dynamics rescoring to test hypothesis 2, and, if stage 1 supports it, a focused analogue series around CHEMBL6145236's quinolinone core. Stop rule: if stage 1 reproduces the ChEMBL order, the Vina ranking is discarded and the project proceeds on measured potency and efficacy only; if thymoquinone's signal collapses under redox controls, it leaves the PPAR-gamma queue and stays a general antioxidant candidate only.

## 5. Limitations

1. Docking only — no experimental data; no compound here is shown to activate, partially activate, or block phosphorylation of PPAR-gamma in any assay.
2. All Vina margins are at or inside the ±1–2 kcal/mol noise; the single "win" over pioglitazone does not exceed it.
3. The ranking is anti-correlated with measured potency (ρ = −0.8, n = 4) — a perfect or near-perfect reversal on four points is striking but fragile; one more compound could change it.
4. Single rigid structure (9F7W, coactivator-bound, bisphenol A in the pocket — not the pioglitazone-bound conformation); no MD, no free-energy refinement, no induced-fit treatment.
5. Docking cannot measure efficacy, so nothing here can distinguish a partial agonist from a full agonist — the paper's central question is unanswerable by its own method and needs the assay.
6. Measured potencies come from heterogeneous ChEMBL assays (EC50 vs Ki, different assay conditions); pChEMBL values are not head-to-head measurements, and no measured PPAR-gamma potency for pioglitazone was retrieved.
7. Thymoquinone carries a PAINS quinone alert; any activity claim for it needs redox controls that were not run.
8. The pipeline's ChEMBL target resolution failed silently once in this run (Section 3.3); the corrected run was verified by hand, but the underlying bug is unfixed and the same failure could recur on other targets.
9. No local (Pakistan) market, pricing or access data were collected.

## 6. Conclusion

One ChEMBL PPAR-gamma active out-scored pioglitazone by Vina on 9F7W, but the margin sits at the edge of scoring noise, the ranking is reversed against measured potency (ρ = −0.8, n = 4), and docking cannot measure the efficacy that separates a useful partial agonist from another full agonist. Thymoquinone binds the pocket weakly and carries a PAINS quinone alert. The paper's durable findings are methodological: a centre-audited docking setup that reproduces its reference to 0.04 kcal/mol, a rank test that fails, and a silent ChEMBL target mix-up caught only by a name check. The next step is a head-to-head PPAR-gamma transactivation assay of the four leads against pioglitazone, reporting efficacy as well as potency, which will settle whether the ChEMBL order or the Vina order is real — and whether CHEMBL6145236 is a partial agonist or just another strong binder.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all tools and data sources used are free and public (UniProtKB, ChEMBL, PubChem, RCSB PDB, AutoDock Vina).

## References

1. International Diabetes Federation. IDF Diabetes Atlas, 11th edition. Brussels, Belgium: International Diabetes Federation; 2025. https://diabetesatlas.org
2. Choi JH, Banks AS, Estall JL, et al. Anti-diabetic drugs inhibit obesity-linked phosphorylation of PPARgamma by Cdk5. Nature. 2010;466(7305):451–456. PMID 20651683. doi:10.1038/nature09291
3. Choi JH, Banks AS, Kamenecka TM, et al. Antidiabetic actions of a non-agonist PPARγ ligand blocking Cdk5-mediated phosphorylation. Nature. 2011;477(7365):477–481. PMID 21892191. doi:10.1038/nature10383
4. Amato AA, Rajagopalan S, Lin JZ, et al. GQ-16, a novel peroxisome proliferator-activated receptor γ (PPARγ) ligand, promotes insulin sensitization without weight gain. J Biol Chem. 2012;287(33):28169–28179. PMID 22584573. doi:10.1074/jbc.M111.332106
5. Yang T, Soodvilai S. Renal and vascular mechanisms of thiazolidinedione-induced fluid retention. PPAR Res. 2008;2008:943614. PMID 18784848. doi:10.1155/2008/943614
6. Megantara S, et al. In silico study of thymoquinone as peroxisome proliferator activated receptor gamma agonist in the treatment of type 2 diabetes mellitus. J Pharm Sci Res. 2017;9(9):1478–1482.
7. Alshahrani S, Anwer T, Alam MF, et al. Effect of thymoquinone on high fat diet and STZ-induced experimental type 2 diabetes: a mechanistic insight by in vivo and in silico studies. J Food Biochem. 2021;45.
8. Coelho MS, de Lima CL, Royer C, et al. GQ-16, a TZD-derived partial PPARγ agonist, induces the expression of thermogenesis-related genes in brown fat and visceral white fat and decreases visceral adiposity in obese and hyperglycemic mice. PLoS One. 2016;11(5):e0154310. doi:10.1371/journal.pone.0154310
9. Scheen AJ. Combined thiazolidinedione-insulin therapy: should we be concerned about safety? Drug Saf. 2004;27(12):841–856. PMID 15366973. doi:10.2165/00002018-200427120-00002
10. Nesto RW, Bell D, Bonow RO, et al. Thiazolidinedione use, fluid retention, and congestive heart failure: a consensus statement from the American Heart Association and American Diabetes Association. Diabetes Care. 2004;27(1):256–263.
11. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J Chem Inf Model. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203
12. Protein Data Bank. Human PPARgamma ligand binding domain in complex with coactivator 1alpha peptide and bisphenol A (BPA). PDB ID 9F7W, resolution 1.25 Å. https://www.rcsb.org/structure/9F7W
13. ChEMBL. Target: Peroxisome proliferator-activated receptor gamma (CHEMBL235). https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL235/

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-002-2026-11-11-CORRECTED.json` (ChEMBL235 run) and `hidden_files/dock-HP-002-2026-11-11-TQ.json` (thymoquinone extra dock); the discarded wrong-target run is kept as `hidden_files/dock-HP-002-2026-11-11.json` (ChEMBL2074, maltase-glucoamylase). Target: UniProt P37231; ChEMBL target CHEMBL235; structure PDB 9F7W; compounds: pioglitazone (PubChem CID 4829), CHEMBL6145236, CHEMBL65805, CHEMBL1813011, CHEMBL1813008, thymoquinone (PubChem CID 10281). No additional data were generated.
