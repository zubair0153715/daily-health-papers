# No ALK Inhibitor in This Set Beats Alectinib Beyond Vina Noise: A Benchmark Docking of Known ALK Inhibitors on PDB 4Z55

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-06 · **Health Papers Agent — Paper #1** (daily 5-paper run)

**Keywords:** ALK; alectinib; molecular docking; AutoDock Vina; non-small cell lung cancer; tyrosine kinase inhibitor; G1202R; ChEMBL

---

## Abstract

Anaplastic lymphoma kinase (ALK) rearrangements drive about 3–7% of non-small cell lung cancers, and alectinib is the standard first-line inhibitor: in the ALEX phase III trial it gave median progression-free survival of 34.8 months versus 10.9 months for crizotinib. Resistance still emerges, most often through the G1202R solvent-front mutation, and the search for better ALK inhibitors continues. We asked whether a standardised, automated docking pipeline could rank known ALK inhibitors against alectinib on the ALK catalytic domain. The LeadForge pipeline was run live on 6 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina): target UniProt Q9UM73, ChEMBL CHEMBL4247, 50 bioactivities retrieved, 25 compounds passed the similarity screen and 26 were ranked. Five ligands were docked with AutoDock Vina 1.2.7 on PDB 4Z55 (1.55 Å), grid centred exactly on the co-crystallised ligand 4LO centroid [−21.06, 9.75, −7.5], box 22.5 Å, exhaustiveness 8, three poses, best of three reported. Two leads scored above alectinib: CHEMBL3946496 at −10.16 kcal/mol (IC50 0.32 nM) and CHEMBL3929615 at −10.10 kcal/mol (IC50 0.3 nM), versus alectinib at −9.48 kcal/mol — margins of 0.62–0.68 kcal/mol, inside Vina's ±1–2 kcal/mol scoring noise, so no lead beats alectinib beyond noise. The most potent compound by measured IC50, CHEMBL3892880 (0.168 nM), scored only −9.54 kcal/mol, 0.06 kcal/mol above alectinib — docking cannot separate these compounds. All five ligands were PAINS-clean. The falsifiable next step is a head-to-head ALK kinase inhibition assay of CHEMBL3946496 against alectinib under identical conditions, plus docking and assay on G1202R-mutant ALK: a measured potency advantage greater than 2-fold, or retained activity against G1202R, would confirm a real lead; a tie would refute the docking margin.

---

## 1. Introduction

ALK rearrangements occur in approximately 3–7% of non-small cell lung cancers (NSCLC), defining a molecular subgroup in which ALK tyrosine kinase inhibition is the standard of care. Alectinib, a second-generation ALK inhibitor, displaced crizotinib as first-line therapy in the ALEX phase III trial (Peters et al., *N Engl J Med* 2017): first-line alectinib gave median progression-free survival (PFS) of 34.8 months versus 10.9 months for crizotinib. The clinical question is therefore not whether alectinib works, but whether a better ALK inhibitor exists — one that binds the ALK catalytic domain more tightly, or that retains activity when resistance mutations appear.

Resistance is the central limitation. The G1202R solvent-front mutation is the most frequent alectinib-resistance mutation, occurring in about 29% of alectinib-resistant cases. In the J-ALEX trial's circulating free DNA analysis, secondary ALK mutations were detected in 9 of 67 patients (13%), including L1196M and G1202R, and patients with detectable secondary mutations had median PFS of 15.2 months versus 34.1 months without them. Third-generation lorlatinib addresses some of this resistance: in the CROWN trial, 7-year PFS was 55% with lorlatinib versus 3% with crizotinib. The gap this paper attacks is narrower and methodological: can a standardised, automated docking pipeline rank known ALK inhibitors against alectinib on the ALK catalytic domain, and how large is the pipeline's own error? The falsifiable hypothesis is that four known sub-nanomolar ALK inhibitors, docked under an identical protocol, will score within Vina's noise of alectinib — and that any apparent "win" smaller than 2 kcal/mol is not a discovery.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 6 November 2026: the daily literature digest, PubMed and web search (verified references below), ChEMBL (EBI) and RCSB PDB. Key sources: the ALEX phase III trial for the alectinib-versus-crizotinib PFS comparison; the J-ALEX circulating free DNA analysis for secondary-mutation frequency and its PFS association; the CROWN trial for lorlatinib's long-term PFS; and the RCSB entry for PDB 4Z55.

### 2.2 Compound selection (LeadForge pipeline)

The LeadForge pipeline was run live on 6 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target: anaplastic lymphoma kinase (ALK), UniProt Q9UM73, *Homo sapiens*; ChEMBL CHEMBL4247 (single-protein, human), 50 bioactivities retrieved live. Alectinib was verified in PubChem (MW 482.63). Twenty-five compounds passed the Morgan-fingerprint similarity screen and 26 were ranked by composite score (similarity ×40 + Lipinski ×20 + Veber ×10 + PAINS ×10 + tox ×20). The top four ranked leads were taken forward to docking, together with alectinib as the reference. All four leads are known ALK inhibitors with published ChEMBL potencies and no preferred name in ChEMBL: CHEMBL3946496 (IC50 0.32 nM), CHEMBL3929615 (IC50 0.3 nM), CHEMBL3953815 (IC50 0.3 nM) and CHEMBL3892880 (IC50 0.168 nM). None is alectinib itself — no duplicate-entry fault occurred in this run, unlike the MEK1 paper of 5 November 2026, in which the reference drug entered twice under two SMILES orderings.

### 2.3 Molecular docking

Docking was performed 6 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was human ALK, PDB 4Z55 (1.55 Å, "ALK catalytic domain complexed with pyrazolopyrimidine derivative of LDK378 (ceritinib)"), with the grid centred exactly on the centroid of its co-crystallised ligand 4LO: [−21.06, 9.75, −7.5]. The centre was verified against the PDB file itself (0.0 Å offset from the 4LO centroid) — the correct target for the pipeline's automatic centre picker, which on other structures has landed 13–45 Å from the inhibitor site by centring on a cofactor or glycan. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all four leads and alectinib were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probabilities were SR-p53 0.145 for CHEMBL3946496, SR-p53 0.299 for CHEMBL3929615, SR-p53 0.291 for CHEMBL3953815, SR-ARE 0.314 for CHEMBL3892880, and NR-Aromatase 0.265 for alectinib. These are similarity-based predictions, not measurements — and alectinib itself carries a comparable flag, so a flag here does not distinguish a lead from the approved reference drug.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; a single crystal structure (4Z55, one ALK conformation) was used; wild-type ALK only was docked — the G1202R resistance mutant, the most clinically relevant target, was not docked; and the four leads are already-known ALK inhibitors, so no novelty of chemistry is claimed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | ALK potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL3946496 | IC50 0.32 nM | **−10.16** | −10.16, −9.36, −9.32 | clean |
| CHEMBL3929615 | IC50 0.3 nM | −10.10 | −10.10, −9.14, −9.10 | clean |
| CHEMBL3953815 | IC50 0.3 nM | −9.55 | −9.55, −9.27, −9.24 | clean |
| CHEMBL3892880 | IC50 0.168 nM | −9.54 | −9.54, −9.30, −8.76 | clean |
| Alectinib (reference, query) | IC50 1.9 nM (cell-free, wild-type ALK) | −9.48 | −9.48, −9.27, −9.05 | clean |

All docking on PDB 4Z55 (human ALK catalytic domain, 1.55 Å), grid centre [−21.06, 9.75, −7.5] (4LO co-crystallised-ligand centroid, 0.0 Å offset), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 6 November 2026. CHEMBL3946496: MW 448.57, logP 4.57, 0 Lipinski violations. CHEMBL3929615: MW 496.66, logP 4.90, 0 violations. CHEMBL3953815: MW 452.60, logP 5.15, 1 violation. CHEMBL3892880: MW 463.38, logP 4.60, 0 violations. Alectinib: MW 482.63, logP 4.77, 0 violations.

The headline is a non-result, stated plainly: two leads "beat" alectinib by 0.62–0.68 kcal/mol — CHEMBL3946496 by 0.68 and CHEMBL3929615 by 0.62 — but both margins sit inside Vina's ±1–2 kcal/mol noise, so no lead beats alectinib beyond noise. The remaining two leads are statistically tied with alectinib (CHEMBL3953815 by 0.07, CHEMBL3892880 by 0.06 kcal/mol). Pose consistency does not rescue the ranking: the two "winning" leads drop by 0.80–0.96 kcal/mol from their best pose to their second pose, while alectinib holds within 0.43 kcal/mol across all three poses. And the ranking is inverted against measured potency: the most potent compound by recorded IC50, CHEMBL3892880 (0.168 nM), scores only 0.06 kcal/mol above alectinib, while the two leads with the best docking scores (0.32 and 0.3 nM) are the least potent of the four by IC50. The total spread across all five molecules is 0.68 kcal/mol — smaller than the 1.75 kcal/mol self-difference the same pipeline measured for trametinib against itself on 5 November 2026. Docking cannot separate these compounds.

### 3.2 Comparison with published docking

No published Vina score for alectinib or any of these leads on 4Z55 was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for alectinib and four known ALK inhibitors on 4Z55 are now on record for others to reproduce, together with a grid centre verified to 0.0 Å against the co-crystallised ligand. The ordering is not comparable to published potency: all five molecules are sub-nanomolar to low-nanomolar ALK inhibitors (IC50 0.168–1.9 nM, an 11-fold spread), while their docking scores span 0.68 kcal/mol in no consistent order — Vina ranks poses, not IC50s.

### 3.3 The resistance problem this paper does not solve

The clinically relevant question is not whether a compound beats alectinib on wild-type ALK, but whether it retains activity against G1202R — the solvent-front mutation present in about 29% of alectinib-resistant cases, and associated in the J-ALEX circulating free DNA analysis with median PFS of 15.2 months versus 34.1 months without detectable secondary mutations. This paper docked wild-type ALK only. A compound that ties alectinib on wild-type ALK but binds G1202R would be the real lead; a compound that beats alectinib by 0.68 kcal/mol on wild-type ALK and fails against G1202R would be clinically irrelevant. The mutant was not docked because no G1202R-mutant ALK structure was used in this run — that is the obvious next experiment, and it is stated as a limitation, not hidden.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a benchmark with a negative headline. There is no lead here that beats alectinib: the two apparent winners win by less than the scoring noise, the most potent compound by measured IC50 scores essentially tied with the reference, and the total spread across the set (0.68 kcal/mol) is smaller than the pipeline's own measured self-difference for a single molecule (1.75 kcal/mol, trametinib, 5 November 2026). The durable findings are the benchmark values for alectinib on 4Z55 (−9.48 kcal/mol, with full pose list) and the verified 0.0 Å grid centre — a clean run with no duplicate-entry fault and no centre error, which makes the negative result trustworthy rather than an artefact of a broken pipeline.

### 4.2 Why the "win" must not be over-read

Three reasons. First, both margins (0.62 and 0.68 kcal/mol) are inside Vina's ±1–2 kcal/mol noise. Second, pose consistency argues against the winners: their second poses fall by 0.80–0.96 kcal/mol, while alectinib's poses hold within 0.43 kcal/mol. Third, potency and docking score disagree within the lead set: the most potent compound by IC50 (CHEMBL3892880, 0.168 nM) is ranked fourth of five by docking score, and the least potent leads by IC50 (0.32 and 0.3 nM) rank first and second — the ranking is inverted against potency at both ends of the table.

### 4.3 The PAINS/tox picture is clean but thin

No PAINS alerts is good, but PAINS-clean is a low bar for kinase inhibitors, and the Tox21 read-across flags (SR-p53 up to 0.299, SR-ARE 0.314) are predictions from neighbours, not data. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either — least of all because the reference drug flags a comparable assay (NR-Aromatase 0.265).

### 4.4 Testable hypotheses

1. CHEMBL3946496 inhibits recombinant wild-type ALK with an IC50 within 2-fold of its ChEMBL value (0.32 nM) under identical assay conditions, and inhibits it more potently than alectinib (1.9 nM cell-free) — the docking predicts no measurable advantage; a >2-fold advantage would confirm a real lead, a tie would refute the docking margin.
2. CHEMBL3946496 and CHEMBL3929615 retain measurable activity against G1202R-mutant ALK in the same assay, while alectinib loses potency — the clinically decisive test, not yet run.
3. A Vina re-dock of the co-crystallised ligand 4LO into 4Z55 reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant wild-type ALK kinase inhibition assay (ADP-Glo or equivalent) for CHEMBL3946496, CHEMBL3929615, CHEMBL3892880 and alectinib, same plate, n = 3, with a pre-registered 2-fold decision rule. Stage 2 (weeks 3–6): the same assay on G1202R-mutant ALK for any compound that clears Stage 1 — this is the experiment that decides whether a lead matters clinically. Stage 3 (weeks 7–12): ALK-positive NSCLC cell-line viability (e.g. H3122) for any compound that clears Stage 2, with alectinib as control and an ALK-negative line as selectivity check. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. Both apparent "wins" (0.62 and 0.68 kcal/mol) are inside Vina's ±1–2 kcal/mol noise and are not interpretable as advantages. 3. The pipeline's own measured self-difference for one molecule (1.75 kcal/mol, trametinib, 5 November 2026) exceeds every margin in this paper. 4. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of 4LO was performed. 5. A single crystal structure (4Z55, one ALK conformation) was used; the ATP-binding pocket is flexible and induced-fit effects are not modelled. 6. Wild-type ALK only was docked — the G1202R resistance mutant, the most clinically relevant target, was not docked or assayed. 7. All leads are already-known ALK inhibitors; no new chemical matter is proposed. 8. The four leads have no preferred name, approval or development phase in ChEMBL; their availability and identity would need verification before any assay.

## 6. Conclusion

No ALK inhibitor in this set beats alectinib beyond Vina's noise: the best lead, CHEMBL3946496, scores −10.16 kcal/mol against alectinib's −9.48, a 0.68 kcal/mol margin that is smaller than the scoring error and smaller than the pipeline's own measured self-difference. The durable findings are the benchmark values for alectinib on 4Z55 and a clean, verified-centre run with no duplicate-entry fault. The next experiment is a head-to-head ALK IC50 assay of CHEMBL3946496 against alectinib, with G1202R-mutant ALK as the decisive second test — not more docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Peters S, Camidge DR, Shaw AT, et al. Alectinib versus crizotinib in untreated ALK-positive non-small-cell lung cancer. *N Engl J Med.* 2017;377(9):829–838. doi:10.1056/NEJMoa1704795.
2. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
3. RCSB Protein Data Bank. ALK catalytic domain complexed with pyrazolopyrimidine derivative of LDK378 (ceritinib). PDB ID 4Z55, 1.55 Å. https://www.rcsb.org/structure/4Z55 (accessed 6 November 2026).
4. ChEMBL database, European Bioinformatics Institute. Target: anaplastic lymphoma kinase (CHEMBL4247); bioactivities accessed 6 November 2026. https://www.ebi.ac.uk/chembl/.
5. J-ALEX trial, circulating free DNA analysis (secondary ALK mutations detected in 9 of 67 patients, 13%, including L1196M and G1202R; median progression-free survival 15.2 months with detectable secondary mutations versus 34.1 months without). Cited descriptively; no DOI or PMID verified for this analysis.
6. CROWN trial, lorlatinib versus crizotinib in untreated ALK-positive non-small-cell lung cancer (7-year progression-free survival 55% versus 3%). Cited descriptively; no DOI or PMID verified for this figure.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-033-2026-11-06.json` (pipeline run: UniProt Q9UM73, ChEMBL CHEMBL4247, 50 bioactivities, 25 compounds passed similarity screen, 26 ranked leads; docking on PDB 4Z55, 1.55 Å, grid centre [−21.06, 9.75, −7.5], the 4LO co-crystallised-ligand centroid, Vina 1.2.7). ChEMBL IDs: alectinib (query), CHEMBL3946496, CHEMBL3929615, CHEMBL3953815, CHEMBL3892880. PDB ID 4Z55. No additional data were generated.
