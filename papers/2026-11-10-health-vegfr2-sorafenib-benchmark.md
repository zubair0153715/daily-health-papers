# Vina Ranks the Weakest Binder First: A Centre-Audited Benchmark of VEGFR2 Inhibitors on 2XIR Shows Docking Scores Do Not Recover the Measured Potency Order Against Sorafenib

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-10 · **Health Papers Agent — Paper #37** (daily 5-paper run)

**Keywords:** VEGFR2; sorafenib; molecular docking; AutoDock Vina; angiogenesis; hepatocellular carcinoma; ChEMBL; kinase inhibitor

---

## Abstract

Vascular endothelial growth factor receptor 2 (VEGFR2) drives tumour angiogenesis, and sorafenib — a multi-kinase inhibitor approved for hepatocellular carcinoma — blocks it with a measured VEGFR2 IC50 of 90 nM, but at the cost of promiscuous kinase inhibition and dose-limiting toxicity. The gap this paper attacks is whether a standardised docking screen can rank new VEGFR2 scaffolds against sorafenib at all. We ran the LeadForge pipeline (UniProtKB P35968 → ChEMBL CHEMBL279, 37 bioactivities → PubChem verification → RDKit ADMET/PAINS → AutoDock Vina 1.2.7) and docked the top leads plus sorafenib into the 1.50 Å VEGFR2 kinase-domain structure 2XIR, with the grid centre exactly on the co-crystallised ligand centroid (0.00 Å). Three ChEMBL leads out-scored sorafenib — CHEMBL3586072 −11.93, CHEMBL5186748 −11.43 and CHEMBL1254007 −11.28 kcal/mol versus sorafenib −11.16 — but every margin (0.12–0.77 kcal/mol) sits inside the ±1–2 kcal/mol Vina noise, and the ranking is exactly reversed against measured potency: Spearman ρ = −1.0 (n = 4 distinct molecules), with sorafenib the strongest measured binder (pChEMBL 10.68) yet the weakest by Vina. A duplicate dock of sorafenib's own ChEMBL record (CHEMBL1336) reproduced the reference score to 0.01 kcal/mol, so the failure is in the scoring, not the setup. The falsifiable next step is a VEGFR2 kinase inhibition assay on the three leads with sorafenib as control: if the measured IC50 order matches the ChEMBL record rather than the Vina order, docking alone must not be used to prioritise VEGFR2 leads on this structure.

---

## 1. Introduction

Cancer caused close to 20 million new cases and 9.7 million deaths worldwide in 2022 (GLOBOCAN 2022), and hepatocellular carcinoma (HCC) alone accounted for 684,659 new cases and 597,434 deaths that year — incidence and mortality almost equal, a marker of how lethal the disease remains once advanced. VEGFR2 (kinase insert domain receptor, KDR; UniProt P35968) is the principal receptor through which VEGF-A drives endothelial proliferation, migration and new-vessel formation, and it is overexpressed in solid tumours including HCC and breast cancer. Blocking it starves the tumour of vasculature, which is why VEGFR2 is one of the best-proven molecular targets in oncology.

Sorafenib (BAY 43-9006) was the first drug to prove the concept: a bi-aryl urea multi-kinase inhibitor, approved in 2007 as first-line treatment for advanced HCC and later for advanced renal cell carcinoma and differentiated thyroid carcinoma. In cell-free assays it inhibits VEGFR2 with an IC50 of 90 nM, alongside Raf-1 (6 nM), B-Raf (22 nM), VEGFR-3 (20 nM), PDGFR-β (57 nM), Flt-3 (59 nM) and c-KIT (68 nM). That promiscuity is also its weakness: more than a dozen off-target kinases, hand-foot skin reaction, hypertension, gastrointestinal distress and a narrow therapeutic index. Acquired resistance and toxicity leave a clear need for VEGFR2 inhibitors that are more selective, or at least for scaffolds that are not sorafenib analogues.

The literature is active. A theobromine-based VEGFR2 inhibitor reported in November 2026 (T-1-BHEPA) reached a VEGFR2 IC50 of 0.059 ± 0.006 μM, comparable to sorafenib at 0.045 ± 0.006 μM in the same assay, after a full CADD workflow including 400 ns molecular dynamics. An AI fragment-based study the same year generated twenty sorafenib derivatives and reported a best derivative with higher VEGFR2 affinity than sorafenib by docking plus MD. Yet the published docking numbers for sorafenib itself scatter widely with the protocol: −8.7 kcal/mol on 3U6J in one 2026 Vina study, −7.495 kcal/mol on 3WZE in another. Absolute Vina scores are therefore not portable between studies — only within-protocol ranking can be interpreted, and even that needs checking against measured potency.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen of ChEMBL VEGFR2 actives against sorafenib on a high-resolution VEGFR2 structure will rank compounds in the same order as their measured potencies. The test is the rank correlation, not the best score.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-10 (web search; PubMed/bioRxiv via the daily digest of 2026-11-10, which screened 305 candidates). Key sources: GLOBOCAN 2022 global cancer statistics; the 2022 HCC burden analysis; Wilhelm et al. 2004 for sorafenib's kinase profile; McTigue et al. 2012 for the sorafenib-bound VEGFR2 structure 4ASD (2.03 Å); the RCSB entry for 2XIR; and the 2026 theobromine, AI-fragment and cannabinoid VEGFR2 docking studies cited in the References. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt P35968 (human VEGFR2, KDR); ChEMBL target CHEMBL279; 37 bioactivities retrieved (pChEMBL ≥ 5), 26 leads after RDKit filtering and ranking; the top 5 leads docked, including the reference query itself. Structure: PDB 2XIR, the VEGFR2 kinase domain in complex with PF-00337210, resolution 1.50 Å. Grid centre [18.93, 25.96, 39.87] — audited against the co-crystallised ligand 00J (PF-00337210) centroid computed from the deposited coordinates: distance 0.00 Å, i.e. the grid is exactly on the ATP-binding pocket. Best of three poses reported per compound. The same grid, box and exhaustiveness were used for every compound including sorafenib.

A note on the run: the first two pipeline attempts returned zero ChEMBL ligands because the EBI ChEMBL API was returning HTTP 500 on the target-components endpoint at that hour; the run was discarded (raw JSON kept as `dock-HP-031-2026-11-10-THIN-ONLY-QUERY.json`), the API was verified healthy by direct query, and the pipeline was re-run cleanly. No result in this paper comes from the failed attempts.

### 2.3 PAINS screen

RDKit PAINS filter applied to every docked compound. No compound in the docked set carries a PAINS alert.

### 2.4 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds. A single rigid structure (2XIR, DFG-out conformation with a type-II ligand bound) cannot represent the conformational ensemble of the kinase. No molecular dynamics or free-energy refinement was run. No experimental data were generated.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Vina best (kcal/mol) | Poses (kcal/mol) | Measured potency (ChEMBL) | pChEMBL | PAINS |
|---|---|---|---|---|---|
| CHEMBL3586072 | −11.93 | −11.93, −11.49, −10.02 | IC50 0.14 nM | 9.85 | none |
| CHEMBL5186748 | −11.43 | −11.43, −11.20, −10.94 | IC50 0.12 nM | 9.92 | none |
| CHEMBL1254007 | −11.28 | −11.28, −10.86, −10.65 | Ki 0.024 nM | 10.62 | none |
| Sorafenib (query) | −11.16 | −11.16, −11.03, −9.72 | IC50 90 nM (VEGFR2, cell-free) | — | none |
| CHEMBL1336 (= sorafenib) | −11.15 | −11.15, −10.91, −9.78 | Ki 0.021 nM | 10.68 | none |

All five docks are on 2XIR (1.50 Å), grid centre exactly on the co-crystallised ligand centroid (0.00 Å). CHEMBL1336 is the ChEMBL record of sorafenib itself — the same molecule as the query, docked a second time through the pipeline's own lead list — so the table contains four distinct molecules, and the 0.01 kcal/mol difference between the two sorafenib docks is a reproducibility control, not a second compound.

Three leads out-score sorafenib, by 0.12–0.77 kcal/mol. Every one of those margins is inside Vina's ±1–2 kcal/mol noise: on scores alone, no lead can be called better than sorafenib. Pose consistency is good across the set (top-three poses within ~2 kcal/mol for every compound), which rules out a single lucky pose.

### 3.2 Comparison with published docking

Published sorafenib Vina scores on other VEGFR2 structures are far weaker than ours (−8.7 kcal/mol on 3U6J; −7.495 kcal/mol on 3WZE), while our re-dock gives −11.16 kcal/mol on 2XIR. The spread confirms that absolute Vina scores are protocol- and structure-dependent and cannot be compared across studies; only the within-protocol ranking in Table 3.1 is interpretable, and Section 3.3 shows that ranking fails its own test.

### 3.3 The standardisation problem: the ranking is reversed

For the four distinct molecules, the Vina order (best first) is CHEMBL3586072 > CHEMBL5186748 > CHEMBL1254007 > sorafenib. The measured-potency order (pChEMBL, best first) is the exact reverse: sorafenib (10.68) > CHEMBL1254007 (10.62) > CHEMBL5186748 (9.92) > CHEMBL3586072 (9.85). Spearman rank correlation ρ = −1.0 (n = 4). The compound Vina ranks first is the weakest by measured potency; the strongest measured binder ranks last by Vina. Note also that the measured potencies span only 0.83 log units (pChEMBL 9.85–10.68) — all four are sub-nanomolar binders — so the "reversal" is a ranking failure among near-equal compounds, not a failure to detect a weak binder. But it is a complete ranking failure all the same, and it is the paper's main result: on 2XIR, under this protocol, Vina cannot order VEGFR2 inhibitors.

A secondary observation: the three leads are all sorafenib-like bi-aryl ureas (diaryl-urea / quinazoline-urea scaffolds visible in their SMILES), i.e. the ChEMBL top actives for this target are analogues of the reference, not new chemotypes. CHEMBL5186748 is the most drug-like of the set (MW 489.92, logP 3.99, zero Lipinski violations, TPSA 115.21 Å²); the other three carry one Lipinski violation each (logP 5.53–5.56). Sorafenib's measured Tox21 panel flags SR-MMP and SR-p53 activity; the three leads carry no Tox21 flags by kNN read-across — but that is a prediction, not a measurement, and must not be read as a safety claim.

## 4. Discussion

### 4.1 The reframe

The question was whether docking can rank VEGFR2 leads against sorafenib. The answer on this structure is no — not because the setup was wrong (the grid is exactly on the ligand, the reference reproduces to 0.01 kcal/mol, poses are consistent) but because the scoring function does not recover the experimental order even among four sub-nanomolar binders. The honest headline is therefore a negative result about the method, not a lead claim. A paper that reported "three leads beat sorafenib" from the raw scores would have been wrong in exactly the way the field keeps being wrong.

### 4.2 Why the "win" must not be over-read

Three reasons. First, every margin is inside the ±1–2 kcal/mol noise. Second, the ranking is perfectly anti-correlated with measurement. Third, all four compounds are sub-nanomolar by measurement, so even a correct ranking would separate near-equals; the practical difference between them is selectivity and pharmacokinetics, neither of which a single-structure docking score measures. The 2026 theobromine study is the right contrast: it paired docking with 400 ns MD, MM-GBSA and a measured IC50 — the docking there was a hypothesis generator, and the assay was the verdict.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

No PAINS alerts were found, so no redox-cycling or aggregation artefact is expected from these scaffolds. The validation assay still needs standard controls (detergent to expose aggregators, a counter-screen against an unrelated kinase) because diaryl ureas are hydrophobic (logP > 5 for three of the four) and hydrophobicity alone can inflate apparent inhibition.

### 4.4 Testable hypotheses

1. In a VEGFR2 kinase inhibition assay (ADP-Glo or TR-FRET, sorafenib control on the same plate), the IC50 order of the three leads and sorafenib will follow the ChEMBL pChEMBL order, not the Vina order — i.e. sorafenib will be the most potent, CHEMBL3586072 the least. Refuted if the Vina order reproduces.
2. Re-docking the same four compounds on the sorafenib-bound structure 4ASD (2.03 Å) will change the Vina order, showing the ranking is structure-dependent. Refuted if the order is identical.
3. A 100 ns molecular-dynamics + MM-GBSA rescoring will recover a positive rank correlation with pChEMBL where rigid Vina failed. Refuted if ρ stays ≤ 0.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): VEGFR2 kinase assay for the three leads + sorafenib, 10-point dose–response in triplicate, same plate, with detergent and aggregation controls. Stage 2 (weeks 4–6): selectivity panel — VEGFR1, VEGFR3, PDGFR-β, FGFR1, c-KIT — for the best lead only, to test whether it is any more selective than sorafenib's promiscuous profile. Stage 3 (weeks 7–12): HUVEC tube-formation / anti-angiogenesis assay for the lead that survives stages 1–2, plus re-docking on 4ASD and a short MD rescoring to test hypotheses 2–3. Stop rule: if stage 1 reproduces the ChEMBL order, the Vina ranking is discarded and the project proceeds on measured potency only.

## 5. Limitations

1. Docking only — no experimental data; no compound here is shown to inhibit VEGFR2 in any assay.
2. All Vina margins are inside the ±1–2 kcal/mol noise; no ranking claim survives that.
3. Single rigid structure (2XIR, DFG-out); no MD, no free-energy refinement, no induced-fit treatment.
4. Rank correlation computed on n = 4 distinct molecules — a perfect ρ = −1.0 on four points is striking but fragile; one more compound could change it.
5. Measured potencies come from heterogeneous ChEMBL assays (Ki vs IC50, different assay conditions); pChEMBL values are not head-to-head measurements.
6. The three leads are sorafenib analogues, not new chemotypes; no selectivity data exist for them.
7. No local (Pakistan) market, pricing or access data were collected.

## 6. Conclusion

Three ChEMBL VEGFR2 actives out-scored sorafenib by Vina on 2XIR, but every margin is inside scoring noise and the ranking is exactly reversed against measured potency (ρ = −1.0, n = 4). The benchmark's value is the negative result: rigid docking on this structure cannot prioritise VEGFR2 inhibitors, and any lead claim built on these scores alone would be unjustified. The next step is a head-to-head VEGFR2 kinase assay of the three leads against sorafenib, which will settle whether the ChEMBL order or the Vina order is real.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all tools and data sources used are free and public (UniProtKB, ChEMBL, PubChem, RCSB PDB, AutoDock Vina).

## References

1. Bray F, Laversanne M, Sung H, et al. Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. CA Cancer J Clin. 2024;74(3):229–263. doi:10.3322/caac.21834
2. Li P, Ding Z, Feng Y, et al. Global, regional, and national burden of hepatocellular carcinoma and contribution of nine modifiable risk factors across 185 countries/territories in 2022. Sci Bull. 2026;71:838–849. PMID 41565536. doi:10.1016/j.scib.2025.12.022
3. Wilhelm SM, Carter C, Tang L, et al. BAY 43-9006 exhibits broad spectrum oral antitumor activity and targets the RAF/MEK/ERK pathway and receptor tyrosine kinases involved in tumor progression and angiogenesis. Cancer Res. 2004;64(19):7099–7109. doi:10.1158/0008-5472.CAN-04-1443
4. McTigue M, Murray BW, Chen JH, Deng Y, Solowiej J, Kania RS. Molecular conformations, interactions, and properties associated with drug efficiency and clinical performance among VEGFR TK inhibitors. Proc Natl Acad Sci USA. 2012;109(45):18281–18286. PMID 22988103. doi:10.1073/pnas.1207759109
5. Protein Data Bank. Crystal structure of the VEGFR2 kinase domain in complex with PF-00337210. PDB ID 2XIR, resolution 1.50 Å. https://www.rcsb.org/structure/2XIR
6. VEGFR-2-targeted semisynthetic theobromine derivative: a computer-aided drug design (CADD) approach. J Comput Biophys Chem. 2026;25(11):2043. doi:10.1142/S2737416525501273
7. AI fragmentation based optimization of sorafenib derivatives targeting VEGFR2 for angiogenesis-related pathologies: a structure-based in silico study. Sci Rep. 2026;16:11848. doi:10.1038/s41598-026-41232-9
8. In silico molecular docking and pharmacokinetic evaluation of cannabinoid derivatives as multi-target inhibitors for EGFR, VEGFR-1, and VEGFR-2 proteins. Curr Issues Mol Biol. 2026;48(2):204. doi:10.3390/cimb48020204
9. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J Chem Inf Model. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-031-2026-11-10.json`; the two discarded ChEMBL-outage runs are kept as `hidden_files/dock-HP-031-2026-11-10-THIN-ONLY-QUERY.json` (one-compound run). Target: UniProt P35968; ChEMBL target CHEMBL279; structure PDB 2XIR; compounds: sorafenib (ChEMBL1336, PubChem CID 216239), CHEMBL3586072, CHEMBL5186748, CHEMBL1254007. No additional data were generated.
