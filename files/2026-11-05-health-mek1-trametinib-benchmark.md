# Trametinib Beats Itself by 1.75 kcal/mol: A Vina Benchmark of MEK1 Inhibitors on 7B7R and the Conformer-Sampling Error Hiding Inside Every Docking Score

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-05 · **Health Papers Agent — Paper #3** (daily 5-paper run)

**Keywords:** MEK1; trametinib; molecular docking; AutoDock Vina; melanoma; BRAF; allosteric inhibitor; ChEMBL

---

## Abstract

BRAF/MEK inhibitor combinations produce response rates of 60–70% in BRAF V600-mutant melanoma, but resistance typically develops within 12–18 months, and the search for better MEK inhibitors continues. We asked whether a standardised, fully automated docking pipeline could rank known MEK1 inhibitors against trametinib on the MEK1 allosteric pocket. The LeadForge pipeline was run live on 5 November 2026; its first target query resolved to the wrong protein entirely (KSR1, not MEK1) and was discarded, and its first grid centre was the ATP-site analogue, 10.14 Å from the allosteric inhibitor pocket. On the corrected target (UniProt Q02750, ChEMBL CHEMBL3587, 38 bioactivities) and the corrected centre — the centroid of the co-crystallised allosteric inhibitor T1K in PDB 7B7R (1.70 Å) — five ligands were docked with AutoDock Vina 1.2.7. The best-scoring "lead", CHEMBL2103875 at −9.52 kcal/mol, is trametinib itself, entered twice by the pipeline under two SMILES orderings; the duplicate trametinib entry scored −7.77 kcal/mol. The same molecule therefore beats itself by 1.75 kcal/mol, an error larger than Vina's nominal ±1–2 kcal/mol scoring noise and larger than every real difference in the set. The remaining known inhibitors — CHEMBL5433950 −8.02 kcal/mol (IC50 0.7 nM), CHEMBL1615025 −7.94 kcal/mol (IC50 1.79 nM), CHEMBL507361 −7.13 kcal/mol (IC50 0.33 nM) — are statistically tied with trametinib and ranked in the wrong potency order. No lead beats trametinib once the duplicate is recognised. The falsifiable next step is a head-to-head MEK1 enzyme inhibition assay of CHEMBL507361 against trametinib under identical conditions, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable potency advantage.

---

## 1. Introduction

Melanoma of the skin caused approximately 332,000 new cases and 59,000 deaths worldwide in 2022 (IARC GLOBOCAN 2022). About half of cutaneous melanomas carry a BRAF V600 mutation, which drives the RAS–RAF–MEK–ERK (MAPK) pathway, and the combination of a BRAF inhibitor with a MEK inhibitor is now standard: BRAF/MEK combinations produce response rates of 60–70% in BRAF V600-mutant melanoma, among the highest in solid-tumour targeted therapy, with responses often beginning within days. The central limitation is resistance, which typically develops within 12–18 months, driven largely by MAPK pathway reactivation. Trametinib, an allosteric MEK1/2 inhibitor approved in combination with dabrafenib, is the benchmark: in the COMBI-d trial the combination gave median overall survival of 25.1 months versus 18.7 months for dabrafenib alone (hazard ratio 0.71), and in COMBI-v 25.6 months versus 18.0 months for vemurafenib alone. In a long-term Chinese cohort the combination gave an objective response rate of 71.7% and a 3-year overall survival rate of 28.8%. The clinical question is whether a better MEK inhibitor exists — one that binds the same allosteric pocket more tightly, or that retains activity against resistance mutations.

The question this paper asks is narrower and methodological: can a standardised, automated docking pipeline rank known MEK1 inhibitors against trametinib on the allosteric pocket, and how large is the pipeline's own error? The falsifiable hypothesis is that five known sub-nanomolar MEK1 inhibitors, docked under an identical protocol, will score within Vina's noise of trametinib — and that any apparent "win" smaller than 2 kcal/mol is not a discovery.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 5 November 2026: the daily literature digest (2026-11-05), PubMed E-utilities and web search (verified references below), ChEMBL (EBI) and RCSB PDB. Key sources: IARC GLOBOCAN 2022 for melanoma burden; the National Institute for Health and Care Excellence appraisal TA396 for the COMBI-d and COMBI-v survival figures; a 2021 Frontiers in Oncology long-term follow-up for the combination's response and survival in a Chinese cohort; and the RCSB entry for PDB 7B7R.

### 2.2 Compound selection (LeadForge pipeline) — and a wrong-target fault caught

The LeadForge pipeline was run live on 5 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). One fault was caught before any number was reported, and it is documented here because it is part of the result. The first target query, "MEK1/2 (MAP2K1/2)", resolved in UniProtKB to Q8IVT5 — KSR1, kinase suppressor of Ras 1, a scaffold protein, not MEK — and the ChEMBL target attached to it (CHEMBL1938215, KSR1) returned a single bioactivity. That run was discarded in full; its raw JSON is preserved for audit. The run was repeated with the precise gene query "MAP2K1": UniProt Q02750 (dual specificity mitogen-activated protein kinase kinase 1, MEK1, Homo sapiens), ChEMBL CHEMBL3587 (single-protein, human), 38 bioactivities retrieved. Trametinib was verified in PubChem (MW 615.39). Twenty-five compounds passed the Morgan-fingerprint similarity screen and 26 were ranked by composite score (similarity ×40 + Lipinski ×20 + Veber ×10 + PAINS ×10 + tox ×20). The top five ranked leads were taken forward to docking. All five are known MEK1 inhibitors with published ChEMBL potencies: trametinib itself (IC50 0.48 nM, pChEMBL 9.32, as CHEMBL2103875), CHEMBL5433950 (IC50 0.7 nM, pChEMBL 9.15), CHEMBL1615025 (IC50 1.79 nM, pChEMBL 8.75) and CHEMBL507361 (IC50 0.33 nM, pChEMBL 9.48). None of the three non-trametinib leads has a preferred name, an approval, or a development phase in ChEMBL.

### 2.3 Molecular docking

Docking was performed 5 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was human MEK1, PDB 7B7R (1.70 Å, "MEK1 in complex with compound 4"), with the grid centred on the centroid of its co-crystallised ligand T1K — 2-[5-[ethyl(methyl)amino]imidazo[1,2-a]pyrimidin-7-yl]phenol, an allosteric MEK inhibitor (compound 4): [−28.04, −12.97, 13.32]. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

One automated-pipeline error was caught and corrected before reporting, and is documented here because it is part of the result. The pipeline's automatic grid-centre picker takes the centroid of the first drug-like HETATM group in the PDB file. In 7B7R that group is ANP (phosphoaminophosphonic acid-adenylate ester, the ATP analogue, residue 401, 31 atoms), not the inhibitor; the centre it produced was [−31.01, −3.89, 16.73], in the ATP site. The co-crystallised allosteric inhibitor T1K (residue 403, 20 atoms) sits 10.14 Å away. MEK allosteric inhibitors bind a pocket adjacent to the ATP site, so the 22.5 Å box still covered the allosteric pocket — and the first docking run's scores shifted by only 0.14–0.96 kcal/mol on re-docking — but the centre was wrong in principle, and on other structures the same default has landed 13–45 Å from the inhibitor site. All five ligands were re-docked at the T1K centroid with the same protocol, and only the corrected numbers are reported. The raw JSON of every run is preserved (see Data availability), so the correction is auditable.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all four leads and trametinib were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probabilities were NR-ER 0.351 for CHEMBL5433950 and 0.338 for trametinib, and SR-MMP 0.087 for CHEMBL1615025. These are similarity-based predictions, not measurements — and trametinib itself carries the highest flags in the panel, so a flag here does not distinguish a lead from the approved reference drug. CHEMBL507361's panel is measured data (not read-across) with no flags.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; a single crystal structure (7B7R, one MEK1 conformation) was used; MEK2 was not docked (trametinib inhibits both MEK1 and MEK2); and the four leads are already-known MEK1 inhibitors, so no novelty of chemistry is claimed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | MEK1 potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL2103875 (= trametinib) | IC50 0.48 nM | **−9.52** | −9.52, −8.90, −8.25 | clean |
| CHEMBL5433950 | IC50 0.7 nM | −8.02 | −8.02, −7.82, −7.60 | clean |
| CHEMBL1615025 | IC50 1.79 nM | −7.94 | −7.94, −7.69, −7.43 | clean |
| Trametinib (reference, duplicate entry) | IC50 0.48 nM (same molecule) | −7.77 | −7.77, −7.71, −7.42 | clean |
| CHEMBL507361 | IC50 0.33 nM | −7.13 | −7.13, −7.13, −6.32 | clean |

All docking on PDB 7B7R (human MEK1, 1.70 Å), grid centre [−28.04, −12.97, 13.32] (T1K allosteric-inhibitor centroid), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 5 November 2026. CHEMBL2103875/trametinib: MW 615.40, logP 3.94, 1 Lipinski violation. CHEMBL5433950: MW 617.42, logP 4.12, 1 violation. CHEMBL1615025: MW 504.23, logP 1.07, 1 violation. CHEMBL507361: MW 482.20, logP 2.47, Lipinski-clean.

The headline number is a self-contradiction, stated plainly: the pipeline entered trametinib twice — once as the query (SMILES written in one atom order) and once as the top ChEMBL hit CHEMBL2103875 (the same molecule, SMILES written in another order) — and the two entries scored −7.77 and −9.52 kcal/mol. The same molecule beats itself by 1.75 kcal/mol. The difference comes from conformer generation: the ligand-preparation step builds a 3D conformer from the SMILES string, and the starting conformer depends on atom ordering, so the same molecule enters Vina from different starting geometries and lands in different local minima. Every real difference in this table is smaller than that artefact: the gap between trametinib-as-QUERY and the best genuine lead (CHEMBL5433950, −8.02) is 0.25 kcal/mol, and the total spread across the four distinct molecules is 0.89 kcal/mol — all inside Vina's noise, and all smaller than the 1.75 kcal/mol the pipeline generates from one molecule against itself. Pose consistency does not rescue the ranking: trametinib-as-QUERY holds within 0.35 kcal/mol across poses, CHEMBL507361 holds its best score across two poses, and the most potent compound by measured IC50 (CHEMBL507361, 0.33 nM) has the worst docking score (−7.13) — the ranking is inverted against potency at the bottom of the table as well as the top.

### 3.2 Comparison with published docking

No published Vina score for trametinib or any of these leads on 7B7R was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for trametinib and three known MEK1 inhibitors on 7B7R are now on record for others to reproduce, together with the duplicate-entry control that quantifies the pipeline's own error. The ordering is not comparable to published potency: all four distinct molecules are sub-nanomolar to low-nanomolar MEK1 inhibitors (IC50 0.33–1.79 nM, a 5-fold spread), while their docking scores span 0.89 kcal/mol in the wrong order — Vina ranks poses, not IC50s, and here it cannot even rank a molecule against itself.

### 3.3 The standardisation problem

Two automated steps that could silently corrupt this result did corrupt it, and a third corrupted it in a way no structure check can catch. The UniProtKB free-text search for "MEK1/2 (MAP2K1/2)" returns KSR1 first; the PDB picker centres on the ATP analogue 10.14 Å from the allosteric pocket; and the lead list contains the reference drug itself under a different SMILES ordering, which the pipeline treats as a new compound. The first two are fixed by verification — check the accession, check the co-crystallised ligand. The third is fixed only by canonicalising SMILES before ranking: two entries with identical canonical SMILES are one molecule, and any pipeline that does not canonicalise will periodically "discover" its own reference drug and report it as a lead beating the reference. The fix is cheap — canonicalise, deduplicate, and include a duplicate-entry control in every run — but it is not optional.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a measurement of the pipeline's own error. There is no lead here: the best "lead" is trametinib, the second-best is 0.25 kcal/mol from trametinib's duplicate score, and the most potent compound scores worst. The durable finding is the 1.75 kcal/mol self-difference — a direct, controlled measurement of conformer-sampling variance in this exact pipeline, on this exact structure, with the reference drug as its own control. Any future paper from this pipeline that reports a margin under ~2 kcal/mol without a duplicate-entry control is reporting noise. The benchmark values for trametinib on 7B7R (−7.77 and −9.52 kcal/mol for the two entries, with full pose lists) are now on record, and the honest way to read them is as a range, not a point: trametinib on 7B7R scores somewhere in a ~2 kcal/mol band depending on input ordering.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the winner is the reference drug. Second, the 1.75 kcal/mol margin is generated by the pipeline itself, not by chemistry — the same molecule, two SMILES orderings. Third, potency and docking score disagree within the lead set: CHEMBL507361, the most potent by recorded IC50 (0.33 nM), scores worst (−7.13), while CHEMBL5433950 (0.7 nM) scores best among genuine leads (−8.02) — a 0.89 kcal/mol spread against a 5-fold potency spread, in no consistent direction.

### 4.3 The PAINS/tox picture is clean but thin

No PAINS alerts is good, but PAINS-clean is a low bar for kinase inhibitors, and the Tox21 read-across flags (NR-ER 0.351 for CHEMBL5433950) are predictions from neighbours, not data. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either — least of all because the reference drug flags the same assays.

### 4.4 Testable hypotheses

1. CHEMBL507361 inhibits recombinant MEK1 with an IC50 within 2-fold of its ChEMBL value (0.33 nM) under identical assay conditions, and inhibits it more potently than trametinib (0.48 nM) — the docking predicts no measurable advantage; a >5-fold advantage would refute the noise interpretation.
2. A Vina re-dock of the co-crystallised ligand T1K (compound 4) into 7B7R reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).
3. Canonicalising the SMILES of all 26 ranked leads and re-running the pipeline removes the trametinib duplicate and changes no other lead's rank — a pipeline fix to be verified, not assumed.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant MEK1 kinase inhibition assay (ADP-Glo or equivalent) for CHEMBL507361, CHEMBL5433950 and trametinib, same plate, n = 3, with a pre-registered 2-fold decision rule. Stage 2 (weeks 3–6): BRAF V600E melanoma cell-line viability (A375, SK-MEL-28) for any compound that clears Stage 1, with trametinib as control and a BRAF wild-type line as selectivity check. Stage 3 (weeks 7–12): MEK2 inhibition assay for any compound that clears Stage 2, since trametinib's clinical value rests on dual MEK1/2 inhibition and a MEK1-only compound is a weaker candidate. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. The 1.75 kcal/mol self-difference for trametinib means no margin under ~2 kcal/mol in this paper is interpretable. 3. Vina noise is ±1–2 kcal/mol on top of the conformer-sampling variance measured here. 4. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of T1K was performed. 5. A single crystal structure (7B7R, one MEK1 conformation) was used; MEK's allosteric pocket is flexible and induced-fit effects are not modelled. 6. MEK2 was not docked. 7. All leads are already-known MEK1 inhibitors; no new chemical matter is proposed. 8. The pipeline's automated target resolution, grid-centre selection and lead deduplication all failed silently and required manual correction — other silent defaults in the same pipeline are not yet audited.

## 6. Conclusion

No MEK1 inhibitor in this set beats trametinib: the best-scoring "lead" is trametinib itself, and the same molecule scored −7.77 and −9.52 kcal/mol under two SMILES orderings — a 1.75 kcal/mol self-difference that exceeds every real difference in the table and sets the floor for what this pipeline can claim. The durable findings are the benchmark values for trametinib on 7B7R and the duplicate-entry control that quantifies conformer-sampling error. The next experiment is a head-to-head MEK1 IC50 assay, not more docking — and the next pipeline change is SMILES canonicalisation before ranking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. International Agency for Research on Cancer. Global Cancer Observatory: melanoma of skin, 2022 estimates (approximately 332,000 new cases, 59,000 deaths).
2. National Institute for Health and Care Excellence. Trametinib in combination with dabrafenib for treating unresectable or metastatic melanoma. Technology appraisal guidance TA396. 2016. https://prep.medthority.com/nice/conditions-and-diseases/cancer/metastases/ta396/ (accessed 5 November 2026).
3. Overall survival of patients with unresectable or metastatic BRAF V600-mutant acral/cutaneous melanoma administered dabrafenib plus trametinib: long-term follow-up of a multicenter, single-arm phase IIa trial. *Front Oncol.* 2021;11:720044. doi:10.3389/fonc.2021.720044.
4. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
5. RCSB Protein Data Bank. MEK1 in complex with compound 4. PDB ID 7B7R, 1.70 Å. https://www.rcsb.org/structure/7B7R (accessed 5 November 2026).
6. ChEMBL database, European Bioinformatics Institute. Target: dual specificity mitogen-activated protein kinase kinase 1 (CHEMBL3587); bioactivities accessed 5 November 2026. https://www.ebi.ac.uk/chembl/.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-057-2026-11-05.json` (discarded first run: UniProt Q8IVT5 KSR1, ChEMBL CHEMBL1938215, single bioactivity) and `hidden_files/dock-HP-057b-2026-11-05.json` (pipeline run: UniProt Q02750, ChEMBL CHEMBL3587, 26 ranked leads; first docking run at the ANP/ATP-site centre retained for audit) and `hidden_files/dock-HP-057c-2026-11-05.json` (authoritative re-dock: PDB 7B7R, 1.70 Å, T1K allosteric-inhibitor centroid [−28.04, −12.97, 13.32], Vina 1.2.7). ChEMBL IDs: trametinib (CHEMBL2103875, query), CHEMBL5433950, CHEMBL1615025, CHEMBL507361. PDB ID 7B7R. No additional data were generated.
