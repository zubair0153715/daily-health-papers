# Four Known Neprilysin Inhibitors Dock at −7.1 to −9.9 kcal/mol on the Omapatrilat Site: A Vina Benchmark, a 37.9 Å Grid Error, and the Zinc That Vina Cannot See

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-05 · **Health Papers Agent — Paper #4** (daily 5-paper run)

**Keywords:** neprilysin; sacubitril; sacubitrilat; molecular docking; AutoDock Vina; heart failure; zinc metallopeptidase; ChEMBL

---

## Abstract

Sacubitril/valsartan, the first angiotensin receptor–neprilysin inhibitor, cut cardiovascular death or heart-failure hospitalisation by 20% versus enalapril in the 8,442-patient PARADIGM-HF trial, yet no standardised Vina benchmark for neprilysin inhibitors existed. We asked whether a standardised, fully automated docking pipeline could rank known neprilysin inhibitors against the active metabolite sacubitrilat on the neprilysin catalytic site. The LeadForge pipeline was run live on 5 November 2026 (UniProtKB P08473 → ChEMBL CHEMBL1944, 53 bioactivities → 26 ranked leads) and docked the top leads with AutoDock Vina 1.2.7 into neprilysin (PDB 6SUK, 1.75 Å). The pipeline's first grid centre was a surface glycan, 37.9 Å from the inhibitor site, and its scores (−5.0 to −6.0 kcal/mol) were discarded; all ligands were re-docked at the centroid of the co-crystallised inhibitor omapatrilat. At the corrected centre the four known inhibitors scored −7.07 to −9.92 kcal/mol: CHEMBL3677663 best at −9.92 kcal/mol (ChEMBL IC50 1.0 nM), against −8.54 kcal/mol for sacubitrilat (LBQ657, the active metabolite) and −8.76 kcal/mol for the sacubitril prodrug. The 1.38 kcal/mol margin over sacubitrilat is inside Vina's ±1–2 kcal/mol noise, and the ranking is again inverted against potency — the most potent compound (CHEMBL3703484, IC50 0.3 nM) scores third at −8.72 kcal/mol. Neprilysin is a zinc metallopeptidase and its inhibitors chelate the catalytic Zn²⁺, which Vina's scoring function cannot model, so every score here is a shape-and-hydrogen-bond estimate that omits the dominant metal interaction. The falsifiable next step is a direct neprilysin enzyme inhibition assay of CHEMBL3677663 against sacubitrilat under identical conditions, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable potency advantage.

---

## 1. Introduction

Heart failure affects an estimated 64 million people worldwide (Global Burden of Disease), and it remains one of the leading causes of hospitalisation and death. The landmark PARADIGM-HF trial (2014) randomised 8,442 patients with heart failure with reduced ejection fraction (EF ≤ 40%) to sacubitril/valsartan or enalapril 10 mg twice daily, on top of optimal medical therapy, and stopped early for benefit: a 20% reduction in the primary endpoint of cardiovascular death or heart-failure hospitalisation, a 20% reduction in cardiovascular mortality, a 21% reduction in heart-failure hospitalisation, and a 16% reduction in all-cause mortality — the first therapy to beat a full-dose ACE inhibitor head-to-head in HFrEF, with an absolute mortality reduction of about 2.8% over ~27 months (number needed to treat ≈ 36 to prevent one death). Sacubitril/valsartan is now first-line therapy for HFrEF in the 2021 ESC and 2022 AHA/ACC guidelines.

The mechanism is twofold. Valsartan blocks the angiotensin-II receptor; sacubitril inhibits neprilysin (NEP, neutral endopeptidase, EC 3.4.24.11), a zinc-dependent membrane-bound metallopeptidase that degrades natriuretic peptides (ANP, BNP, CNP), bradykinin and adrenomedullin. Sacubitril itself is a prodrug: it is de-ethylated in vivo to the active metabolite sacubitrilat (LBQ657), which inhibits neprilysin and prolongs the vasodilatory, natriuretic and anti-fibrotic actions of the natriuretic peptides. Neprilysin's catalytic site holds a zinc ion coordinated by the HEXXH motif histidines, and its inhibitors — including omapatrilat, the dual ACE/NEP inhibitor whose thiol group coordinates the zinc directly — bind by chelating that metal. That metal interaction is the central problem for docking: AutoDock Vina's scoring function has no term for metal coordination, so a Vina score for a neprilysin inhibitor is, by construction, an underestimate that omits the dominant interaction.

The question this paper asks is methodological: can a standardised, automated docking pipeline benchmark known neprilysin inhibitors against sacubitrilat on the catalytic site, and what does it miss? The falsifiable hypothesis is that four known sub-nanomolar neprilysin inhibitors, docked under an identical protocol, will score within Vina's noise of sacubitrilat — and that any apparent "win" smaller than 2 kcal/mol is not a discovery, because the zinc term is missing from every score.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 5 November 2026: the daily literature digest (2026-11-05), PubMed E-utilities and web search (verified references below), ChEMBL (EBI) and RCSB PDB. Key sources: the PARADIGM-HF results and guideline position for the clinical case; Sharma et al. for the 6SUK omapatrilat structure and the zinc-coordination mechanism; and a 2024 Frontiers in Pharmacology review for neprilysin's structure and inhibitor design.

### 2.2 Compound selection (LeadForge pipeline)

The LeadForge pipeline was run live on 5 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target identification used the query "Neprilysin (NEP)": UniProt P08473, neprilysin (membrane metallo-endopeptidase, MME), Homo sapiens. The ChEMBL target was CHEMBL1944 (single-protein, human). Fifty-three bioactivities (pChEMBL ≥ 5) were retrieved; sacubitril was verified in PubChem (CID 11720835; SMILES CCOC(=O)C(C)CC(CC1=CC=C(C=C1)C2=CC=CC=C2)NC(=O)CCC(=O)O; MW 411.50). Twenty-five compounds passed the Morgan-fingerprint similarity screen and 26 were ranked by composite score (similarity ×40 + Lipinski ×20 + Veber ×10 + PAINS ×10 + tox ×20). The top four ranked leads were taken forward to docking, plus sacubitril itself. All four leads are known neprilysin inhibitors with published ChEMBL potencies: CHEMBL3677663 (IC50 1.0 nM, pChEMBL 9.00), CHEMBL4443138 (IC50 0.8 nM, pChEMBL 9.10), CHEMBL3703484 (IC50 0.3 nM, pChEMBL 9.52) and CHEMBL3676144 (IC50 0.38 nM, pChEMBL 9.42). None has a preferred name, an approval, or a development phase in ChEMBL. Two of the leads, CHEMBL3703484 and CHEMBL4443138, are stereoisomers of the same scaffold (identical MW 417.89 and logP 4.01, differing in defined stereochemistry at one centre) with recorded IC50s of 0.3 and 0.8 nM; they are treated as distinct ChEMBL entries, not duplicates.

### 2.3 Molecular docking

Docking was performed 5 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was human neprilysin, PDB 6SUK (1.75 Å, "Crystal structure of neprilysin in complex with omapatrilat", Sharma et al. 2020), with the grid centred on the centroid of its co-crystallised ligand FT8 — omapatrilat: [21.80, −46.58, 16.97]. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Two reference forms were docked: sacubitril (the ethyl-ester prodrug, as verified by PubChem) and sacubitrilat (LBQ657, the active metabolite, PubChem CID 10430040, C22H25NO5, isomeric SMILES C[C@H](C[C@@H](CC1=CC=C(C=C1)C2=CC=CC=C2)NC(=O)CCC(=O)O)C(=O)O), because the prodrug is not the species that inhibits the enzyme. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

One automated-pipeline error was caught and corrected before reporting, and it is documented here because it is the largest such error in this series. The pipeline's automatic grid-centre picker takes the centroid of the first drug-like HETATM group in the PDB file. In 6SUK the first HETATM group is the catalytic zinc ion (residue 801, 1 atom, skipped as too small) and the next is NAG 802 — a 2-acetamido-2-deoxy-beta-D-glucopyranose glycan, 27 atoms, attached to the protein surface — whose centroid [33.33, −14.69, 33.89] the pipeline used as the grid centre. The co-crystallised inhibitor omapatrilat (FT8, residue 806, 50 atoms) sits 37.9 Å away at [21.80, −46.58, 16.97], next to the zinc at [21.61, −49.01, 11.24]. The first docking run therefore docked all five ligands into a surface sugar, 38 Å from the catalytic site, and its scores (−5.00 to −5.96 kcal/mol) are discarded in full. All six ligands (four leads, sacubitril, sacubitrilat) were re-docked at the FT8 centroid with the same protocol, and only the corrected numbers are reported — they are 2.07–3.96 kcal/mol better than the glycan-centre numbers, which is the size of the error the default introduced. The raw JSON of every run is preserved (see Data availability), so the correction is auditable.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all four leads, sacubitril and sacubitrilat were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probabilities were NR-ER 0.171 for CHEMBL3677663 and 0.072 or lower for the others. These are similarity-based predictions, not measurements, and no lead carries a strong flag.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; a single crystal structure (6SUK, one neprilysin conformation) was used; Vina cannot model the catalytic Zn²⁺ coordination that dominates neprilysin inhibitor binding, so all scores systematically omit the metal term; the receptor was prepared without the zinc ion as a scored interaction; and the four leads are already-known neprilysin inhibitors, so no novelty of chemistry is claimed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | NEP potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL3677663 | IC50 1.0 nM | **−9.92** | −9.92, −9.79, −9.38 | clean |
| CHEMBL4443138 | IC50 0.8 nM | −9.09 | −9.09, −7.76, −7.63 | clean |
| Sacubitril (prodrug) | — (prodrug) | −8.76 | −8.76, −8.67, −8.52 | clean |
| CHEMBL3703484 | IC50 0.3 nM | −8.72 | −8.72, −8.62, −8.04 | clean |
| Sacubitrilat (active, LBQ657) | — (active metabolite) | −8.54 | −8.54, −8.47, −8.34 | clean |
| CHEMBL3676144 | IC50 0.38 nM | −7.07 | −7.07, −6.86, −6.54 | clean |

All docking on PDB 6SUK (human neprilysin, 1.75 Å), grid centre [21.80, −46.58, 16.97] (FT8/omapatrilat centroid), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 5 November 2026. CHEMBL3677663: MW 433.46, logP 3.29, Lipinski-clean. CHEMBL4443138 / CHEMBL3703484: MW 417.89, logP 4.01, Lipinski-clean. CHEMBL3676144: MW 419.86, logP 3.38, Lipinski-clean. Sacubitril: MW 411.50, logP 3.84. Sacubitrilat: MW 383.44 (C22H25NO5).

The headline number needs its qualifier in the same breath: CHEMBL3677663 beats sacubitrilat by 1.38 kcal/mol, inside Vina's noise — and the ranking is inverted against potency, since the most potent compound (CHEMBL3703484, IC50 0.3 nM) scores third at −8.72 kcal/mol, behind both the prodrug (−8.76) and CHEMBL4443138 (−9.09, IC50 0.8 nM). The stereoisomer pair splits by 0.37 kcal/mol in the same direction as their potencies (0.8 nM scores better than 0.3 nM) — again, the wrong direction, and inside noise. Pose consistency is good for the top compound (within 0.54 kcal/mol across poses) and for sacubitrilat (within 0.20 kcal/mol), but poor for CHEMBL4443138, whose second pose falls 1.33 kcal/mol to −7.76. The honest reading: Vina on 6SUK reproduces the sub-nanomolar band — every compound lands between −7.07 and −9.92 kcal/mol — but it cannot rank within it, and it cannot rank the prodrug against the active metabolite meaningfully either, since the prodrug out-scores its own active form by 0.22 kcal/mol. The discarded glycan-centre run is the more important number in one sense: it shows the pipeline's default can understate every score by 2–4 kcal/mol while producing a clean, plausible-looking table.

### 3.2 Comparison with published docking

The co-crystallised ligand omapatrilat is itself a dual ACE/NEP inhibitor whose thiol coordinates the catalytic zinc, and Sharma et al. reported the structural basis of its binding in the same 2020 paper that deposited 6SUK. No published Vina score for sacubitrilat or any of these leads on 6SUK was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for sacubitrilat (−8.54 kcal/mol, poses −8.54/−8.47/−8.34) and four known NEP inhibitors on 6SUK are now on record for others to reproduce. A re-dock of omapatrilat itself into 6SUK (protocol self-validation, RMSD against the crystal pose, including the zinc coordination geometry) was not run and is listed as a hypothesis below; Vina cannot reproduce a metal-coordination pose, so that validation would be expected to fail, which is itself informative.

### 3.3 The standardisation problem

The grid-centre audit in §2.3 is the durable methodological finding, and it is the worst instance in this series: 37.9 Å, a surface glycan mistaken for the binding site. The pipeline's centre picker — first non-junk HETATM group — cannot distinguish a co-crystallised inhibitor from a glycan, a cofactor, or a buffer component, and in this series it has now picked a cofactor (1.82 Å off), a cofactor (18.33 Å off), an ATP analogue (10.14 Å off) and a glycan (37.9 Å off). Only one of the four was harmless. The fix is cheap — verify the co-crystallised ligand's identity and centroid before docking — but it is not optional, and it must be applied per structure, because the distance between the first HETATM group and the true inhibitor site is not predictable from the file alone. For metalloproteases there is a second, unfixable-within-Vina problem: the scoring function has no metal term, so even a correctly centred run omits the dominant interaction.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a benchmark plus two cautions. First, a benchmark: four known neprilysin inhibitors and sacubitrilat dock at −7.07 to −9.92 kcal/mol on the omapatrilat site under a standardised protocol, with pose consistency good enough to reproduce. Second, a caution about the pipeline: a 37.9 Å centre error produced a plausible table that understated every score by 2–4 kcal/mol, and only a manual HETATM audit caught it. Third, a caution about the method: Vina cannot score the zinc coordination that defines neprilysin inhibition, so the numbers are shape-and-hydrogen-bond estimates for a metal-binding problem. None of the four leads is a better neprilysin inhibitor than sacubitrilat on this evidence; CHEMBL3677663 is a candidate for an enzyme assay, not a drug.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 1.38 kcal/mol margin over sacubitrilat is inside Vina's ±1–2 kcal/mol noise. Second, potency and docking score disagree within the lead set: the most potent compound scores third, and the prodrug out-scores its own active metabolite. Third, the zinc term is missing from every score — the ranking could change entirely under a metal-aware method, and no Vina ranking of metalloprotease inhibitors should be trusted without one.

### 4.3 The PAINS/tox picture is clean but thin

No PAINS alerts is good, but PAINS-clean is a low bar, and the Tox21 read-across flags (NR-ER 0.171 at most) are predictions from neighbours, not data. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either.

### 4.4 Testable hypotheses

1. CHEMBL3677663 inhibits recombinant neprilysin with an IC50 within 2-fold of its ChEMBL value (1.0 nM) under identical assay conditions, and inhibits it more potently than sacubitrilat — the docking predicts no measurable advantage; a >5-fold advantage would refute the noise interpretation.
2. A metal-aware re-scoring (e.g. a zinc-coordination-aware docking or MM-GBSA with the Zn²⁺ retained) re-ranks the four leads in potency order, where Vina does not.
3. A Vina re-dock of the co-crystallised omapatrilat into 6SUK fails to reproduce its crystallographic pose within 2 Å RMSD, specifically at the zinc-coordinating thiol — the expected failure that would quantify Vina's metal blind spot (protocol self-validation; not yet run).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant neprilysin enzyme inhibition assay (fluorogenic substrate, e.g. Mca-based) for CHEMBL3677663, CHEMBL3703484 and sacubitrilat, same plate, n = 3, with a pre-registered 2-fold decision rule. Stage 2 (weeks 3–6): selectivity panel against ACE and endothelin-converting enzyme for any compound that clears Stage 1, since dual ACE/NEP inhibition carries the angioedema risk that ended omapatrilat. Stage 3 (weeks 7–12): plasma stability and protein binding for any compound that clears Stage 2, since a neprilysin inhibitor must survive circulation to reach its target. Total compound cost is the binding constraint; all four leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. Vina cannot model Zn²⁺ coordination — the dominant interaction is missing from every score. 3. The 1.38 kcal/mol margin over sacubitrilat is inside Vina's ±1–2 kcal/mol noise. 4. No molecular-dynamics refinement, binding-free-energy calculation, metal-aware re-scoring, or re-docking validation of omapatrilat was performed. 5. A single crystal structure (6SUK, one neprilysin conformation) was used. 6. All four leads are already-known neprilysin inhibitors; no new chemical matter is proposed. 7. No clinical, selectivity, or Pakistani-market data are presented; the PARADIGM-HF figures are contextual, not part of the result. 8. The pipeline's automated grid-centre selection failed by 37.9 Å and required manual correction — other silent defaults in the same pipeline are not yet audited.

## 6. Conclusion

Four known neprilysin inhibitors dock at −7.07 to −9.92 kcal/mol on the omapatrilat site (PDB 6SUK), with the best lead beating sacubitrilat by 1.38 kcal/mol — inside Vina's noise, and ranked in the wrong potency order. The durable findings are the benchmark values themselves, the 37.9 Å grid error that understated every score by 2–4 kcal/mol before correction, and the zinc blind spot: Vina cannot score the metal coordination that defines this target. The next experiment is a head-to-head neprilysin enzyme assay with metal-aware re-scoring — not more Vina docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. McMurray JJV, Packer M, Desai AS, et al. Angiotensin–neprilysin inhibition versus enalapril in heart failure. *N Engl J Med.* 2014;371:993–1004. doi:10.1056/NEJMoa1409077.
2. Sharma U, Cozier GE, Sturrock ED, Acharya KR. Molecular basis for omapatrilat and sampatrilat binding to neprilysin — implications for dual inhibitor design with angiotensin-converting enzyme. *J Med Chem.* 2020. doi:10.1021/acs.jmedchem.0c00441.
3. Comprehensive review on neprilysin (NEP) inhibitors: design, structure-activity relationships, and clinical applications. *Front Pharmacol.* 2024. doi:10.3389/fphar.2024.1501407.
4. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
5. RCSB Protein Data Bank. Crystal structure of neprilysin in complex with omapatrilat. PDB ID 6SUK, 1.75 Å. https://www.rcsb.org/structure/6SUK (accessed 5 November 2026).
6. ChEMBL database, European Bioinformatics Institute. Target: neprilysin (CHEMBL1944); bioactivities accessed 5 November 2026. https://www.ebi.ac.uk/chembl/.
7. PubChem, National Library of Medicine. Sacubitrilat (LBQ657), CID 10430040 (accessed 5 November 2026).

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-043-2026-11-05.json` (pipeline run: UniProt P08473, ChEMBL CHEMBL1944, 26 ranked leads; first docking run at the NAG-glycan centre retained for audit) and `hidden_files/dock-HP-043c-2026-11-05.json` (authoritative re-dock: PDB 6SUK, 1.75 Å, FT8/omapatrilat centroid [21.80, −46.58, 16.97], Vina 1.2.7; includes sacubitrilat, PubChem CID 10430040). ChEMBL IDs: sacubitril (query), CHEMBL3677663, CHEMBL4443138, CHEMBL3703484, CHEMBL3676144. PDB ID 6SUK. No additional data were generated.
