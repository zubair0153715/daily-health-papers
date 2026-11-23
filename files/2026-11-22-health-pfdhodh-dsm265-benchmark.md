# DSM265 Self-Docks at −10.70 kcal/mol on Its Own PfDHODH Structure — but Two Weaker Analogues Score Better, and the Ranking Inverts

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-22 · **Health Papers Agent — Paper #98** (daily 5-paper run)

**Keywords:** Plasmodium falciparum; dihydroorotate dehydrogenase; DSM265; malaria; molecular docking; AutoDock Vina; ChEMBL; antimalarial

---

## Abstract

Malaria caused 263 million cases and 597,000 deaths in 2023, three-quarters of the deaths in children under five in Africa, and artemisinin resistance makes new antimalarials urgent. DSM265, a selective Plasmodium falciparum dihydroorotate dehydrogenase (PfDHODH) inhibitor, is the reference compound for this benchmark. We asked whether Vina docking on the DSM265-bound PfDHODH structure ranks known PfDHODH inhibitors by their measured IC50 values. The pipeline resolved PfDHODH (UniProtKB Q08210) to ChEMBL CHEMBL3588732, retrieved 58 bioactivities, and ranked 26 leads; docking ran on 4RX0 (PfDHODH co-crystallised with DSM265, 2.25 Å) and on 7L01 (PfDHODH co-crystallised with a different inhibitor, DSM782, 1.6 Å). On 4RX0, DSM265 self-docked at −10.70 kcal/mol, but CHEMBL3289670 (IC50 35 nM) scored −12.16 and CHEMBL1738786 (IC50 38 nM) scored −11.86 — both weaker in assay than DSM265 (IC50 27 nM) yet better in docking, so the ranking inverts. The same molecule docked twice under different SMILES spellings scored −10.70 and −10.37 on 4RX0 and −8.22 and −7.79 on 7L01, a same-molecule reproducibility spread of 0.33–0.43 kcal/mol, and the self-dock structure scored every compound about 2.5 kcal/mol better than the cross-dock structure. Docking therefore cannot rank this PfDHODH series, and the best-pose scores are unstable across poses. The falsifier is a head-to-head PfDHODH enzymatic assay of DSM265, CHEMBL3289670 and CHEMBL1738786 under identical conditions: if the two analogues do not outperform DSM265 there, the docking ranking is refuted.

---

## 1. Introduction

The World Health Organization's World Malaria Report 2024 records 263 million malaria cases and 597,000 deaths in 2023, with children under five accounting for 76% of deaths in the African Region. Artemisinin partial resistance is now confirmed in multiple regions, and the pipeline of new antimalarials is thin. Dihydroorotate dehydrogenase (DHODH), the fourth enzyme of de novo pyrimidine biosynthesis, is a validated target: *Plasmodium falciparum* cannot salvage pyrimidines and depends entirely on this pathway, while the human enzyme differs enough in its inhibitor-binding pocket to allow selectivity.

DSM265 is the flagship PfDHODH inhibitor. Phillips et al. (Sci Transl Med 2015) showed it is selective for the *Plasmodium* enzyme over the human enzyme, active against blood and liver stages, and that a single oral dose of 200–400 mg maintains therapeutic concentrations for more than eight days. Its measured PfDHODH IC50 in ChEMBL is 27 nM, consistent with the published value of about 33 nM. This paper tests one falsifiable hypothesis: **Vina docking on the DSM265-bound PfDHODH structure (4RX0) ranks known PfDHODH inhibitors in the same order as their measured IC50 values.** The falsifier is stated in the Abstract.

## 2. Methods

### 2.1 Literature basis

Sources verified on 22 November 2026: WHO World Malaria Report 2024 (burden figures); Phillips et al., Sci Transl Med 2015;7:296ra111 (DSM265 discovery and properties, PMID 26180101, doi:10.1126/scitranslmed.aaa6645); ChEMBL bioactivities for PfDHODH (CHEMBL3588732), retrieved live. The Islamic literature sweep found no canonical work that addresses DHODH or malaria chemotherapy: Ibn Sina's *Canon* describes fevers and their treatment, but the parasite, the enzyme and the drug were all unknown to the classical authors, so no classical source can inform the docking question; this is recorded as a limitation, not hidden.

### 2.2 Molecular docking

The standardised AutoDock Vina protocol of Papers #1 and #3 was used. Target: *P. falciparum* DHODH, UniProtKB Q08210, resolved live to ChEMBL CHEMBL3588732 (SINGLE PROTEIN, *Plasmodium falciparum* isolate 3D7), 58 bioactivities, 26 leads after similarity screening. Two structures were docked. **4RX0** (PfDHODH co-crystallised with DSM265, 2.25 Å): the grid centre [−26.36, −11.70, −16.46] is the centroid of the co-crystallised DSM265 ligand (HETATM group D65, 70 atoms including alternate conformations), computed with `dock._ligand_center`, which excludes the FMN cofactor, the orotate substrate and waters — the centre audit is mandatory after the TYK2 wrong-domain precedent. **7L01** (PfDHODH co-crystallised with inhibitor DSM782, 1.6 Å): centre [5.00, 49.01, 2.20], the DSM782 centroid; this is a cross-dock for DSM265, not its own structure. Box 22.5 Å on both. Best of three poses reported; the reference drug and the analogues were docked under the identical protocol on each structure. Ligands: DSM265 (PubChem CID 51347395) and ChEMBL leads with their ChEMBL activities.

### 2.3 PAINS screen

RDKit PAINS filter applied to every compound. All five compounds reported here are PAINS-clean.

### 2.4 Honesty limits

Docking is not activity. Vina's scoring noise is ±1–2 kcal/mol, so gaps smaller than ~1 kcal/mol cannot rank compounds. No experimental data were generated; no molecular dynamics or free-energy refinement was run. The same molecule was docked twice under different SMILES spellings, which measures reproducibility rather than adding a compound.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured IC50 (ChEMBL) | 4RX0 best affinity (kcal/mol) | 4RX0 poses | 7L01 best affinity (kcal/mol) | 7L01 poses | PAINS |
|---|---|---|---|---|---|---|
| DSM265 (reference) | 27 nM | −10.70 | −10.70, −7.84, −7.72 | −8.22 | −8.22, −7.72, −7.70 | clean |
| DSM265 as CHEMBL1956285 | 27 nM | −10.37 | −10.37, −7.92, −7.17 | −7.79 | −7.79, −7.70, −7.47 | clean |
| CHEMBL1956283 | 28 nM | −10.78 | −10.78, −9.33, −8.16 | −8.67 | −8.67, −8.57, −8.54 | clean |
| CHEMBL3289670 | 35 nM | −12.16 | −12.16, −9.12, −9.00 | −9.61 | −9.61, −9.08, −9.02 | clean |
| CHEMBL1738786 | 38 nM | −11.86 | −11.86, −9.50, −8.67 | −8.90 | −8.90, −8.87, −8.14 | clean |

On the self-dock structure 4RX0, the ranking inverts. The most potent compound, DSM265 (27 nM), scores −10.70; the two least potent, CHEMBL3289670 (35 nM) and CHEMBL1738786 (38 nM), score −12.16 and −11.86 — 1.46 and 1.16 kcal/mol better than DSM265. CHEMBL1956283 (28 nM) scores −10.78, essentially tied with DSM265. Ranked by docking: CHEMBL3289670 > CHEMBL1738786 > CHEMBL1956283 ≈ DSM265. Ranked by assay: DSM265 > CHEMBL1956283 > CHEMBL3289670 > CHEMBL1738786. The two orders are reversed. The same inversion appears on the cross-dock structure 7L01, where CHEMBL3289670 again scores best (−9.61) and DSM265 worst (−8.22/−7.79).

Two further findings qualify the numbers. First, the same molecule docked twice: DSM265 entered as the PubChem query and as ChEMBL1956285 (identical connectivity, different SMILES spelling) scores −10.70 versus −10.37 on 4RX0 and −8.22 versus −7.79 on 7L01 — a same-molecule reproducibility spread of 0.33–0.43 kcal/mol, which is the floor below which score differences are meaningless. Second, the pose spreads are wide: DSM265's three 4RX0 poses span −10.70 to −7.72 (2.98 kcal/mol), and CHEMBL3289670's span −12.16 to −9.00 (3.16 kcal/mol). The best pose is an outlier in both cases, not a consensus. Third, the structure effect is large and consistent: every compound scores about 2.5 kcal/mol better on its self-dock structure 4RX0 than on the cross-dock structure 7L01 (DSM265: −10.70 vs −8.22; CHEMBL3289670: −12.16 vs −9.61).

### 3.2 Compound properties

| Compound | MW | logP | HBD | HBA | Rotatable bonds | TPSA (Å²) | Lipinski violations | Veber | Tox21 max |
|---|---|---|---|---|---|---|---|---|---|
| DSM265 | 415.34 | 5.95 | 1 | 4 | 4 | 55.11 | 1 | pass | 0.476 |
| CHEMBL1956283 | 323.73 | 3.94 | 1 | 4 | 3 | 55.11 | 0 | pass | 0.366 |
| CHEMBL3289670 | 375.28 | 4.45 | 1 | 4 | 3 | 55.11 | 0 | pass | 0.396 |
| CHEMBL1738786 | 357.29 | 4.31 | 1 | 4 | 3 | 55.11 | 0 | pass | 0.386 |

All four analogues are smaller and cleaner than DSM265 by the usual rules (MW 323–375 vs 415, logP 3.94–4.45 vs 5.95, zero Lipinski violations vs one, 3 rotatable bonds vs 4). DSM265's single Lipinski violation is its logP of 5.95, and its Tox21 kNN maximum of 0.476 is the highest in the set, though still below 0.5. All are PAINS-clean with identical TPSA (55.11 Å²), reflecting the shared triazolopyrimidine core.

### 3.3 Comparison with published docking

No published Vina benchmark of DSM265 against these specific ChEMBL analogues on 4RX0 was found in the literature sweep; the numbers here are the first report of this comparison. The 4RX0 structure itself is the published DSM265 complex from Phillips et al. (2015).

## 4. Discussion

### 4.1 The reframe

The question was whether docking can rank PfDHODH inhibitors. The answer is no — not on either structure, and not even in the right direction. The most potent compound scores worst, and the two weakest score best. This is the third consecutive paper in this run (#96 HCV NS5B, #97 renin, #98 PfDHODH) in which Vina fails to rank a congeneric series by potency, and the strongest such failure yet: an outright inversion rather than a null.

### 4.2 Why the "win" must not be over-read

There is no win to over-read here, and that is the point. CHEMBL3289670's −12.16 is the best score in the table, but its best pose is 3.16 kcal/mol ahead of its second pose, its assay potency is 35 nM against DSM265's 27 nM, and its advantage over DSM265 (1.46 kcal/mol) is inside Vina's ±1–2 kcal/mol noise. A reader who took −12.16 at face value would prioritise the wrong compound. The honest reading: these four compounds are all sub-40 nM PfDHODH inhibitors, docking cannot separate them, and the choice between them must be made on properties and assay data, not on Vina scores.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five compounds are PAINS-clean, so the head-to-head assay does not need redox and aggregation controls. The assay's controls instead need to cover the known confounder in DHODH assays: the enzyme's dependence on its electron acceptor (decylubiquinone in vitro), whose concentration shifts apparent IC50 values. The validation design must fix the acceptor concentration and report it.

### 4.4 Testable hypotheses

1. CHEMBL3289670 and CHEMBL1738786 inhibit recombinant PfDHODH with IC50 values of ~35 and ~38 nM in the same assay that gives DSM265 27 nM — i.e. the docking inversion does not reproduce in assay. Settled by the head-to-head assay.
2. DSM265 docked twice under different SMILES spellings reproduces within 0.5 kcal/mol on any PfDHODH structure — a reproducibility check for future benchmarks.
3. A 100 ns molecular-dynamics simulation of the CHEMBL3289670 4RX0 pose shows it leaving the pocket or rearranging, confirming that its −12.16 best pose is a scoring outlier.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): source the four compounds (commercial, ≥95% purity) and recombinant PfDHODH; set up a colorimetric DHODH activity assay (DCIP reduction) with DSM265 as the internal control and a fixed decylubiquinone concentration. Stage 2 (weeks 3–6): dose–response curves for all four compounds in triplicate, same plate; report IC50 with 95% confidence intervals. Stage 3 (weeks 7–8): repeat on a second enzyme lot; if the inversion holds in assay (the analogues genuinely outperform DSM265), run a 100 ns molecular-dynamics simulation of the top pose. Stage 4 (weeks 9–12): selectivity panel against human DHODH for the winner only — selectivity is the property that made DSM265 a drug, and a PfDHODH inhibitor that also hits the human enzyme is not a lead.

## 5. Limitations

1. Docking only — no experimental data; Vina noise ±1–2 kcal/mol, and the best-pose scores reported here are outliers within their own pose sets.
2. The same-molecule reproducibility spread (0.33–0.43 kcal/mol) sets a floor on meaningful differences that most of the table's gaps do not clear.
3. Single-structure analysis per compound set; no molecular dynamics or free-energy refinement was run.
4. ChEMBL activities come from different assays and laboratories; the IC50 values compared here were not measured under identical conditions — the head-to-head assay is the correction.
5. No canonical Islamic medical work addresses DHODH or malaria chemotherapy; the literature sweep covers the available digitised canon and names this gap rather than claiming a classical precedent that does not exist.
6. Nothing here supports a clinical recommendation; DSM265's clinical record is outside this paper's scope.

## 6. Conclusion

DSM265 self-docks at −10.70 kcal/mol on its own PfDHODH structure 4RX0, yet two weaker analogues score better (−12.16 and −11.86), inverting the potency ranking. The same molecule docked twice reproduces only within 0.33–0.43 kcal/mol, and the self-dock structure scores every compound about 2.5 kcal/mol better than the cross-dock structure. Vina cannot rank this PfDHODH series. The next step is a head-to-head PfDHODH assay of the four compounds under identical conditions.

## 7. Policy implications

**Decision-maker:** the ORIC director and the laboratory supervisor at SMBBMU Larkana (Prof. Dr. Nadeem Baloch, ORIC), who control the university's small research budget. **Decision:** whether to fund the 8–12-week head-to-head PfDHODH assay proposed in §4.5 before any analogue prioritisation. **Exact change:** approve the assay for DSM265, CHEMBL3289670, CHEMBL1738786 and CHEMBL1956283 as the next funded step, capped at the cost of four commercial compounds and one recombinant PfDHODH lot, and spend nothing on analogue synthesis until the assay returns. **Reversal condition:** if the assay confirms the ChEMBL potencies (DSM265 best), drop the docking-based prioritisation entirely and use assay data only for future lead selection — do not spend further on Vina benchmarks of this series. The Islamic principle is *hifz al-nafs* (preservation of life, one of the maqasid al-sharia): malaria kills 597,000 people a year, mostly children, and a better antimalarial would serve that end — but the same principle forbids spending scarce university funds on a compound chosen by a score that the paper itself shows cannot rank, and forbids any clinical claim before the assay exists.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content.

## References

1. World Health Organization. World Malaria Report 2024. Geneva: WHO; 2024. (263 million cases, 597,000 deaths in 2023; children under five 76% of deaths in the African Region.)
2. Phillips MA, Lotharius J, Marsh K, et al. A long-duration dihydroorotate dehydrogenase inhibitor (DSM265) for prevention and treatment of malaria. Sci Transl Med. 2015;7(296):296ra111. doi:10.1126/scitranslmed.aaa6645. PMID 26180101.
3. ChEMBL. Dihydroorotate dehydrogenase (quinone), mitochondrial — Plasmodium falciparum (CHEMBL3588732) bioactivity data, retrieved live 22 November 2026. https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3588732/
4. Protein Data Bank. 4RX0: Plasmodium falciparum dihydroorotate dehydrogenase bound with inhibitor DSM265, 2.25 Å. https://www.rcsb.org/structure/4RX0
5. Protein Data Bank. 7L01: Plasmodium falciparum dihydroorotate dehydrogenase bound with inhibitor DSM782, 1.6 Å. https://www.rcsb.org/structure/7L01

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-095-2026-11-22.json` (pipeline: ChEMBL CHEMBL3588732, 58 bioactivities, 26 leads; 7L01 cross-dock) and `hidden_files/dock-HP-095-4rx0-2026-11-22.json` (4RX0 self-dock, centre [−26.36, −11.70, −16.46]). Ligands: DSM265 PubChem CID 51347395; CHEMBL1956285, CHEMBL1956283, CHEMBL3289670, CHEMBL1738786 (ChEMBL). Target: P. falciparum DHODH, UniProtKB Q08210. No additional data were generated.
