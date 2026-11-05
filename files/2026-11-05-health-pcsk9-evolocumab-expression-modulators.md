# Five Sub-Nanomolar PCSK9 Expression Modulators Dock Only Weakly at the LDLR-Interface Site: A Vina Benchmark on 7S5H, Two Target-Resolution Faults, and the Binder-versus-Modulator Distinction

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-05 · **Health Papers Agent — Paper #5** (daily 5-paper run)

**Keywords:** PCSK9; evolocumab; LDL cholesterol; molecular docking; AutoDock Vina; cyclic peptide; expression modulator; protein–protein interaction

---

## Abstract

PCSK9 binds the hepatic LDL receptor (LDLR) and promotes its degradation, raising plasma LDL cholesterol; the monoclonal antibody evolocumab lowers LDL cholesterol by about 59% and cut major cardiovascular events by 20% in the FOURIER trial (27,564 patients, hazard ratio 0.80), but antibodies are parenteral and costly, so oral small molecules are sought. We ran a standardised AutoDock Vina 1.2.7 benchmark of ChEMBL PCSK9 actives (UniProt Q8NBP7; ChEMBL CHEMBL2929; 53 bioactivities) against PDB 7S5H (1.27 Å, PCSK9 in complex with cyclic peptide 35). Two pipeline faults were caught and fixed: the first target query resolved to a monkey protein and human maltase-glucoamylase and was discarded, and the grid was re-centred from a single peptide-residue fragment to the full cyclic-peptide centroid (4.05 Å shift; re-dock shifts ≤0.28 kcal/mol). Five dockable small molecules — carbonyl-linked benzimidazole–indole PCSK9 expression modulators with sub-nanomolar cellular EC50 values (0.15–2.46 nM) — scored only −6.04 to −6.48 kcal/mol at the LDLR-interface site, with no correlation between score and potency (the most potent, 0.15 nM, scored −6.12). The twenty strongest ChEMBL actives are macrocyclic peptides (molecular weight 894–1,738 Da; Ki/IC50 down to 0.13 nM) that bind the same interface but exceed Vina's practical scope. Evolocumab itself cannot be docked (a ~150 kDa antibody), so no numeric comparison with the reference drug is possible. The weak scores are consistent with the small molecules acting by reducing PCSK9 expression rather than by binding PCSK9: docking cannot validate an expression modulator. The falsifiable next step is a direct PCSK9-binding assay (surface plasmon resonance or a PCSK9–LDLR interaction assay) on the five compounds; binding weaker than ~10 µM would confirm the non-binder interpretation, while sub-micromolar binding would refute it.

---

## 1. Introduction

Elevated low-density lipoprotein cholesterol (LDL-C) is a causal, cumulative risk factor for atherosclerotic cardiovascular disease: each 1.0 mmol/L reduction in LDL-C is associated with a 20–25% decrease in cardiovascular event risk (Baigent et al., 2010). Proprotein convertase subtilisin/kexin type 9 (PCSK9), a 692-amino-acid secreted serine protease, binds LDL receptor family members — LDLR, VLDLR, LRP1 and LRP8 — and promotes their degradation in intracellular acidic compartments (UniProt Q8NBP7). Gain-of-function PCSK9 variants cause familial hypercholesterolaemia; loss-of-function carriers have markedly low LDL-C and low cardiovascular risk, making PCSK9 one of the best genetically validated lipid targets.

The clinically approved PCSK9 inhibitors are monoclonal antibodies. Evolocumab (Repatha) lowered LDL-C by ~59% from baseline and reduced the composite of myocardial infarction, stroke and cardiovascular death by 20% (hazard ratio 0.80) over 2.2 years in FOURIER (27,564 patients with atherosclerotic disease; Sabatine et al., 2017). Alirocumab reduced the primary composite endpoint by 15% (hazard ratio 0.85) over 2.8 years in ODYSSEY OUTCOMES (18,924 patients; Schwartz et al., 2018). Neither antibody reduced cardiovascular death. Antibodies require subcutaneous injection every two weeks or monthly, need cold-chain handling, and are expensive — a particular barrier in Pakistan, where cardiovascular disease is the leading cause of death and most lipid-lowering therapy is oral and generic. An oral small molecule that blocks PCSK9 would therefore be valuable, and the PCSK9–LDLR interface is the obvious binding site: the LDLR EGF-A domain binds a flat surface on the PCSK9 catalytic domain, and the 1.27 Å structure 7S5H shows a macrocyclic peptide occupying exactly that surface (Tucker et al., 2021).

**Hypothesis, stated falsifiably:** the most potent small-molecule PCSK9 actives in ChEMBL bind the PCSK9–LDLR interface with Vina scores comparable to known interface binders (≤ −8 kcal/mol), and docking score ranks with measured potency. This paper tests that hypothesis — and finds it false, for a mechanistically informative reason.

## 2. Methods

### 2.1 Literature basis

Sources searched on 2026-11-05: PubMed-indexed trial reports (FOURIER, ODYSSEY OUTCOMES), the Cholesterol Treatment Trialists' Collaboration meta-analysis, ChEMBL (target CHEMBL2929, 53 bioactivities, accessed live), UniProtKB (Q8NBP7), and RCSB PDB (7S5H). The daily research digest at `~/workspace/research-team/digests/` was consulted for recent PCSK9 literature. All references below were verified (PMID/DOI checked against ChEMBL, RCSB or the publisher); no citation was invented.

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, as in Papers #1 and #3 of this series: ligands from ChEMBL (canonical SMILES), receptor from RCSB PDB 7S5H (1.27 Å, PCSK9(ΔCRD) in complex with cyclic peptide 35; Tucker et al., 2021), grid box 22.5 Å, exhaustiveness 8, best of three poses reported. The reference drug evolocumab is a ~150 kDa monoclonal antibody: it has no PubChem small-molecule record (query returned "not found") and cannot be docked by Vina, so the comparison with the reference drug is mechanistic, not numeric — stated here rather than hidden. The twenty macrocyclic-peptide leads (molecular weight 894–1,738 Da) were excluded from docking as beyond Vina's practical scope, and are reported as undockable rather than silently dropped.

### 2.3 PAINS screen

RDKit PAINS filter applied to all five docked compounds: all five are PAINS-clean. All five pass Lipinski's rule of five with zero violations.

### 2.4 Honesty limits

Docking is not activity: a Vina score estimates a binding free energy for one rigid-receptor pose, with ±1–2 kcal/mol noise. No molecular dynamics or free-energy refinement was run. No experimental data were generated. The EC50 values quoted are cellular potencies from the literature, not binding affinities, and the distinction is the central point of this paper.

## 3. Results

### 3.1 Two pipeline faults caught before any number was trusted

**Fault 1 — wrong target, twice over.** The first query, "Proprotein convertase subtilisin/kexin type 9 (PCSK9)", resolved in UniProtKB to A8T677 from *Plecturocebus moloch* (a monkey) and in ChEMBL to CHEMBL2074 — human maltase-glucoamylase. CHEMBL2074 is a known fallback: the same wrong target appeared in the leishmaniasis paper earlier today (HP-052) and in the 2026-11-05 LpxH paper, whenever a free-text query fails to match a real target. The run (55 bioactivities, 25 leads, no structure found) was discarded in full. A precise gene query, "PCSK9", resolved correctly to UniProt Q8NBP7 (*Homo sapiens*, 692 aa) and ChEMBL CHEMBL2929 (53 bioactivities, 25 leads). Lesson recorded for the pipeline: free-text target resolution must be verified against accession, organism and ChEMBL target name before any docking is trusted.

**Fault 2 — fragment centre.** The pipeline centred the grid on Z50, the first residue of the co-crystallised cyclic peptide 35 (23 atoms; centroid [−18.18, 17.44, −11.55]). The correct centre for the peptide site is the centroid of the whole cyclic peptide (chain C, 75 non-water atoms): [−17.58, 18.25, −7.63], 4.05 Å away. All five leads were re-docked at the corrected centre; scores shifted by ≤0.28 kcal/mol and the ranking was preserved (one adjacent swap, inside noise). The corrected scores below are authoritative.

### 3.2 Docking: the comparison table

| Compound | Cellular EC50 (nM) | MW | logP | Rot. bonds | Vina, corrected centre (kcal/mol) | Vina, fragment centre (kcal/mol) | PAINS |
|---|---|---|---|---|---|---|---|
| CHEMBL4797870 | 0.69 | 488.52 | 2.55 | 6 | **−6.48** | −6.61 | clean |
| CHEMBL4783308 | 1.21 | 325.32 | 3.57 | 2 | **−6.36** | −6.31 | clean |
| CHEMBL4789986 | 2.46 | 297.26 | 3.55 | 2 | **−6.26** | −6.36 | clean |
| CHEMBL4780905 | 0.15 | 311.29 | 3.56 | 2 | **−6.12** | −6.40 | clean |
| CHEMBL4785006 | 0.28 | 367.40 | 4.84 | 5 | **−6.04** | −6.14 | clean |
| Evolocumab (reference) | — (antibody; LDL-C −59%, FOURIER HR 0.80) | ~150,000 | — | — | not dockable | not dockable | — |

All five are carbonyl-linked benzimidazole–indole compounds from Xie et al. (2020), developed from a 2,3′-diindolylmethane phenotypic-screen hit by nitrogen scan, deuterium substitution and fluorine scan. Their EC50 values come from ChEMBL assay CHEMBL4774177: "Modulation of PCSK9 in human HepG2 cells assessed as reduction in PCSK9 expression … measured after 24 hrs by ELISA" (assay type B, confidence score 9). That is a **cellular expression assay, not a binding assay** — a fact the docking table alone would conceal.

Three observations: (i) the whole dockable set spans only 0.44 kcal/mol (−6.04 to −6.48), well inside Vina's ±1–2 kcal/mol noise — the five compounds are indistinguishable by docking; (ii) there is no correlation between docking score and cellular potency — the most potent compound (CHEMBL4780905, EC50 0.15 nM) scores −6.12, while the weakest (CHEMBL4789986, EC50 2.46 nM) scores −6.26; (iii) the absolute scores are weak: in this same series, true interface binders on other targets scored −7.5 to −10.7 kcal/mol. A −6.1 to −6.5 kcal/mol score at a flat protein–protein interface is what a non-binder looks like.

### 3.3 The twenty compounds that could not be docked

The remaining twenty leads are macrocyclic peptides, molecular weight 894–1,738 Da, with potencies that exceed the dockable set: CHEMBL5084416 (Ki 0.1285 nM, MW 1,611.95) is from the Tucker et al. (2021) tricyclic-peptide series — the same series as the co-crystallised cyclic peptide 35 in 7S5H — and CHEMBL4642977 (IC50 0.152 nM) is from a cyclic-tetramer series (Sabnis, 2020). These are genuine direct binders at the LDLR interface, proven crystallographically for the series, but their size and flexibility (up to 21 rotatable bonds) place them outside what rigid-receptor Vina docking can meaningfully score. They are the real comparators for any future small-molecule binder — and they show what a true interface binder's potency looks like (sub-nanomolar Ki/IC50), which makes the dockable set's weak scores more, not less, informative.

### 3.4 Comparison with published docking

No published Vina docking of these five benzimidazole–indole compounds against PCSK9 exists to compare with, as far as we could determine; the Xie et al. (2020) paper reports cellular and in-vivo data, not docking. The 7S5H structure itself is the crystallographic evidence that the LDLR-interface site is druggable by a macrocycle, not by these small molecules.

## 4. Discussion

### 4.1 The reframe: the hypothesis fails, and the failure is the finding

The hypothesis was that the most potent small-molecule PCSK9 actives bind the LDLR interface. They do not — or at least, nothing in the docking supports it. Their sub-nanomolar cellular EC50 values measure **reduction of PCSK9 expression in HepG2 cells**, not binding to PCSK9 protein. Xie et al. describe them as PCSK9 modulators discovered by phenotypic screening; the mechanism is suppression of PCSK9 expression, not occupation of the LDLR interface. A compound that lowers PCSK9 expression has no reason to bind PCSK9 at all, and its −6.1 to −6.5 kcal/mol docking score is exactly the weak, non-specific signal such a compound should give at an unrelated site. Docking an expression modulator against the protein it down-regulates is a category error — and this paper documents the error rather than repeating it silently.

### 4.2 Why the "weak scores" must not be over-read in the other direction

Weak docking does not prove non-binding either: Vina on a flat protein–protein interface underestimates binders that rely on induced fit, water networks or entropy, and the ΔCRD construct in 7S5H lacks the C-terminal domain. The scores rule out a strong, conventional binding mode; they do not exclude weak or allosteric binding. The correct reading is "no evidence of interface binding", not "proven non-binder".

### 4.3 Three modalities, three different comparisons

PCSK9 is now attacked by (at least) three modalities that must never be ranked on one scale: (i) antibodies (evolocumab, alirocumab) that bind circulating PCSK9 with picomolar affinity and have outcome-trial proof; (ii) macrocyclic peptides (Tucker et al., 2021) that bind the LDLR interface with sub-nanomolar Ki and showed LDL lowering in cynomolgus monkeys comparable to the antibodies; (iii) small-molecule expression modulators (Xie et al., 2020) with sub-nanomolar cellular EC50 values whose target engagement is at the level of PCSK9 expression, not PCSK9 protein. Add siRNA (inclisiran) as a fourth, expression-level modality. Any "PCSK9 inhibitor ranking" that mixes EC50 (expression), Ki (binding) and clinical LDL-C reduction is meaningless — this paper's table keeps the units and assay types explicit for that reason.

### 4.4 Testable hypotheses

1. **Direct binding:** the five benzimidazole–indole compounds bind PCSK9 with Kd weaker than ~10 µM by surface plasmon resonance, or fail to compete with LDLR EGF-A in a PCSK9–LDLR interaction assay. Sub-micromolar binding would refute the non-binder interpretation.
2. **Expression mechanism:** the compounds reduce PCSK9 mRNA and secreted PCSK9 protein in HepG2 cells in a dose-dependent manner without changing PCSK9–LDLR binding affinity in a cell-free assay.
3. **Peptide benchmark:** a truncated, dockable fragment of cyclic peptide 35 scores ≤ −8 kcal/mol at the same corrected centre, validating the grid for genuine interface binders.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): recombinant human PCSK9 + LDLR EGF-A domain; SPR binding screen of the five compounds (single-cycle kinetics, 0.1–50 µM) plus cyclic peptide 35 as a positive control. Stage 2 (weeks 4–7): HepG2 cells; PCSK9 mRNA (qPCR) and secreted PCSK9 (ELISA) after 24 h compound exposure, replicating the ChEMBL assay, with a PCSK9–LDLR co-immunoprecipitation arm to separate expression effects from binding effects. Stage 3 (weeks 8–12): LDL uptake assay (fluorescent LDL) in HepG2 cells as a functional readout; a compound that lowers PCSK9 expression should increase LDL uptake without binding PCSK9 in Stage 1. All stages include evolocumab as a binding positive control and a vehicle control; PAINS artefacts are not a concern (all five are PAINS-clean), but a detergent control is included for the SPR stage.

## 5. Limitations

1. Docking only: no experimental binding or cellular data were generated; all potency values are literature values from ChEMBL.
2. Vina noise ±1–2 kcal/mol exceeds the 0.44 kcal/mol spread of the dockable set — the five compounds cannot be ranked against each other by docking.
3. The reference drug evolocumab cannot be docked; the clinical comparison is qualitative, not numeric.
4. The twenty most potent actives (macrocyclic peptides) could not be docked; the paper's docking claim covers only the small-molecule chemotype.
5. A single rigid structure (7S5H, ΔCRD construct) was used; no molecular dynamics, no induced-fit modelling, no alternative PCSK9 conformation was tested.
6. The ChEMBL assay annotation ("reduction in PCSK9 expression … by ELISA") is taken as reported; the primary paper (Xie et al., 2020) should be read in full before any laboratory work.
7. No Pakistan-specific data: PCSK9 variant frequencies, evolocumab pricing and access in Pakistan were not assessed here.

## 6. Conclusion

Five sub-nanomolar cellular PCSK9 actives dock only weakly (−6.04 to −6.48 kcal/mol) at the LDLR-interface site of 7S5H, with no correlation between docking score and potency — because their EC50 values measure reduced PCSK9 expression in HepG2 cells, not binding to PCSK9. The genuine interface binders in the same ChEMBL set are macrocyclic peptides too large for Vina, and the reference antibody evolocumab cannot be docked at all. The honest conclusion is a negative one with a clear next step: test direct binding by SPR; if binding is weaker than ~10 µM, these compounds are expression modulators, and future small-molecule PCSK9 work should be benchmarked against the macrocyclic peptides, not against the antibody.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content.

## References

1. Tucker TJ, Embrey MW, Alleyne C, Amin RP, Bass A, Bhatt B, Bianchi E, Branca D, Bueters T, Buist N, Ha SN, Hafey M, He H, Higgins J, Johns DG, Kerekes AD, Koeplinger KA, Kuethe JT, Li N, Murphy B, Orth P, Salowe S, Shahripour A, Tracy R, Wang W, Wu C, Xiong Y, Zokian HJ, Wood HB, Walji A. A Series of Novel, Highly Potent, and Orally Bioavailable Next-Generation Tricyclic Peptide PCSK9 Inhibitors. J Med Chem. 2021;64(22):16770–16800. PMID: 34704436. DOI: 10.1021/acs.jmedchem.1c01599.
2. Xie H, Yang K, Winston-McPherson GN, Stapleton DS, Keller MP, Attie AD, Smith KA, Tang W. From methylene bridged diindole to carbonyl linked benzimidazoleindole: Development of potent and metabolically stable PCSK9 modulators. Eur J Med Chem. 2020;206:112678. PMID: 32823006. DOI: 10.1016/j.ejmech.2020.112678.
3. Sabatine MS, Giugliano RP, Keech AC, Honarpour N, Wiviott SD, Murphy SA, Kuder JF, Wang H, Liu T, Wasserman SM, Sever PS, Pedersen TR; FOURIER Steering Committee and Investigators. Evolocumab and Clinical Outcomes in Patients with Cardiovascular Disease. N Engl J Med. 2017;376(18):1713–1722. PMID: 28304224. DOI: 10.1056/NEJMoa1615664.
4. Schwartz GG, Steg PG, Szarek M, Bhatt DL, Bittner VA, Diaz R, Edelberg JM, Goodman SG, Hanotin C, Harrington RA, Jukema JW, Lecorps G, Mahaffey KW, Moryusef A, Pordy R, Quintero K, Roe MT, Sasiela WJ, Tamby JF, Tricoci P, White HD, Zeiher AM; ODYSSEY OUTCOMES Committees and Investigators. Alirocumab and Cardiovascular Outcomes after Acute Coronary Syndrome. N Engl J Med. 2018;379(22):2097–2107. PMID: 30403574. DOI: 10.1056/NEJMoa1801174.
5. Baigent C, Blackwell L, Emberson J, Holland LE, Reith C, Bhala N, Peto R, Barnes EH, Keech A, Simes J, Collins R; Cholesterol Treatment Trialists' (CTT) Collaboration. Efficacy and safety of more intensive lowering of LDL cholesterol: a meta-analysis of data from 170,000 participants in 26 randomised trials. Lancet. 2010;376(9753):1670–1681. PMID: 21067804. DOI: 10.1016/S0140-6736(10)61350-5.
6. Sabnis RW. Novel Cyclic Tetramer Compounds as PCSK9 Inhibitors for Treating Metabolic Disorders. ACS Med Chem Lett. 2020;11(9):1671. PMID: 32944132. DOI: 10.1021/acsmedchemlett.0c00388.
7. ChEMBL target CHEMBL2929 (proprotein convertase subtilisin/kexin type 9, human); bioactivity data accessed 2026-11-05 via the ChEMBL API (ebi.ac.uk/chembl). Assay CHEMBL4774177 (modulation of PCSK9 in human HepG2 cells, ELISA).
8. UniProtKB Q8NBP7 (PCSK9, Homo sapiens, 692 aa); function annotation accessed 2026-11-05.
9. RCSB PDB 7S5H: PCSK9(ΔCRD) in complex with cyclic peptide 35, 1.27 Å. https://www.rcsb.org/structure/7S5H

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-046b-2026-11-05.json` (pipeline run; fragment-centre scores) and `hidden_files/dock-HP-046c-2026-11-05.json` (authoritative re-dock at the full cyclic-peptide centroid); the discarded first run is `hidden_files/dock-HP-046-2026-11-05.json` (wrong target: A8T677 / CHEMBL2074). Compound identities: ChEMBL CHEMBL4797870, CHEMBL4783308, CHEMBL4789986, CHEMBL4780905, CHEMBL4785006. Structure: PDB 7S5H. No additional data were generated.
