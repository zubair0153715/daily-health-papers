# Direct InhA Inhibitors Dock 3.5–4.4 kcal/mol Better Than Free Isoniazid on Mycobacterium tuberculosis InhA: A Standardised Vina Benchmark at the INH–NAD Adduct Site

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-05 · **Health Papers Agent — Paper #1** (daily 5-paper run)

**Keywords:** InhA; isoniazid; KatG; molecular docking; AutoDock Vina; tuberculosis; drug resistance; ChEMBL

---

## Abstract

Tuberculosis killed an estimated 1.23 million people in 2024, and Pakistan — fifth among high-burden countries, with about 669,000 cases and 51,000 deaths — carries 6.3% of the global burden. Isoniazid, the cornerstone of TB chemotherapy, is a prodrug: it must be activated by the mycobacterial catalase-peroxidase KatG into the INH–NAD adduct that inhibits the enoyl-ACP reductase InhA, and the KatG S315T mutation alone is found in 94% of isoniazid-resistant clinical isolates. Direct InhA inhibitors that need no KatG activation are therefore the rational bypass, but no standardised Vina benchmark for them on the adduct-bound structure existed. We ran the LeadForge pipeline live on 5 November 2026 (UniProtKB P9WGR1 → ChEMBL CHEMBL1849, 52 bioactivities → 26 ranked leads) and docked the top leads plus isoniazid with AutoDock Vina 1.2.7 into InhA (PDB 4TRO, 1.40 Å) at the centroid of the co-crystallised INH–NAD adduct (ZID). The pipeline's first grid centre was the NAD cofactor centroid, 1.82 Å from the adduct centroid; all ligands were re-docked at the corrected centre and only the corrected numbers are reported. Two known direct inhibitors beat free isoniazid by 3.5–4.4 kcal/mol: CHEMBL3125235 scored −10.27 kcal/mol (ChEMBL IC50 2.0 nM) and CHEMBL3125270 −9.37 kcal/mol (IC50 4.0 nM), against −5.83 kcal/mol for isoniazid; a third, CHEMBL259138, scored −7.50 kcal/mol (Ki 1.0 nM). All three leads are PAINS-clean and already-published InhA actives, so this is a benchmark, not a discovery — and the margin over isoniazid is expected, because the free prodrug is not the active species; the adduct, not isoniazid, is the true comparator. The falsifiable next step is a direct InhA enzyme inhibition assay of CHEMBL3125235 against the INH–NAD adduct under identical conditions, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable advantage.

---

## 1. Introduction

Tuberculosis remains the world's deadliest infectious disease. The World Health Organization's Global Tuberculosis Report 2025 records an estimated 10.7 million people falling ill with TB in 2024 and 1.23 million deaths; eight countries account for two-thirds of cases, and Pakistan ranks fifth, with an estimated 669,000 cases (6.3% of the global burden, incidence 266 per 100,000 population) and about 51,000 deaths. Roughly 75% of estimated cases were notified and treated, and Pakistan is listed among the high-burden countries for multidrug-resistant and rifampicin-resistant TB. Treatment success is reported at 95%, but the gap between estimated and notified cases — and the resistance burden — keeps new drugs a priority.

Isoniazid (INH) has been the cornerstone of TB chemotherapy for over seventy years. It is a prodrug: the mycobacterial catalase-peroxidase KatG (encoded by Rv1908c) activates it to a reactive isonicotinoyl species that reacts with NAD+ to form the INH–NAD adduct, which binds the active site of InhA, the NADH-dependent enoyl-ACP reductase of the FAS-II system, blocking mycolic-acid biosynthesis and killing the bacillus. The dominant resistance mechanism is loss of the activator: mutations in katG, above all S315T, are found in 94% of isoniazid-resistant clinical isolates, preventing prodrug activation. A second mechanism is mutation or overexpression of inhA itself (promoter c-15t), which titrates the drug. Because the activator, not the target, fails in most resistant isolates, the target itself remains druggable — a direct InhA inhibitor (DII) that binds InhA in its native state, without KatG activation, should retain activity against KatG-mutant strains. Recent work has pursued exactly this: triazolopyrimidine direct InhA inhibitors reported in 2026 bind with computed energies of −13.9 kcal/mol and outperform triclosan (−8.67 kcal/mol) in silico, with the explicit rationale of evading KatG-mediated resistance.

The question this paper asks is narrower and methodological: can a standardised, fully automated docking pipeline benchmark known direct InhA inhibitors against isoniazid on the adduct-bound InhA structure, and can its automated grid-centre choice be trusted? The falsifiable hypothesis is that known potent direct InhA inhibitors, docked under an identical protocol, will score substantially better than free isoniazid on InhA (PDB 4TRO) — and that the margin must be read as a prodrug artefact, not as a discovery, unless it also beats the INH–NAD adduct itself.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 5 November 2026: the daily literature digest (2026-11-05), PubMed E-utilities and web search (verified references below), ChEMBL (EBI) and RCSB PDB. Key sources: the WHO Global Tuberculosis Report 2025 for burden figures; the Microbiology Spectrum review of isoniazid and ethionamide resistance for the KatG S315T 94% figure and the adduct mechanism; Miesel et al. for the early genetic evidence; and a 2026 Research Square preprint on direct InhA inhibitors for the current DII rationale.

### 2.2 Compound selection (LeadForge pipeline)

The LeadForge pipeline was run live on 5 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target identification used the query "M. tuberculosis enoyl-ACP reductase (InhA)": UniProt P9WGR1, enoyl-[acyl-carrier-protein] reductase [NADH], gene inhA, Mycobacterium tuberculosis H37Rv, 269 aa. The ChEMBL target was CHEMBL1849 (single-protein). Fifty-two bioactivities (pChEMBL ≥ 5) were retrieved; isoniazid was verified in PubChem and appears in the lead set as CHEMBL64 (SMILES NNC(=O)c1ccncc1, MW 137.14, logP −0.31). Twenty-five compounds passed the Morgan-fingerprint similarity screen and 26 were ranked by composite score (similarity ×40 + Lipinski ×20 + Veber ×10 + PAINS ×10 + tox ×20). The top five ranked leads were taken forward to docking. All five are known InhA actives with published ChEMBL potencies: isoniazid itself (Ki 0.75 nM, pChEMBL 9.12, as recorded in ChEMBL), CHEMBL3125235 (IC50 2.0 nM, pChEMBL 8.70), CHEMBL3125270 (IC50 4.0 nM, pChEMBL 8.40) and CHEMBL259138 (Ki 1.0 nM, pChEMBL 9.00). None of the three leads has a preferred name, an approval, or a development phase in ChEMBL; they are unnamed research compounds.

### 2.3 Molecular docking

Docking was performed 5 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was M. tuberculosis InhA, PDB 4TRO (1.40 Å, "Structure of the enoyl-ACP reductase of Mycobacterium tuberculosis InhA, inhibited with the active metabolite of isoniazid"), with the grid centred on the centroid of its co-crystallised ligand ZID — isonicotinic-acetyl-nicotinamide-adenine dinucleotide, i.e. the INH–NAD adduct itself: [3.82, −33.34, 13.56]. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

One automated-pipeline error was caught and corrected before reporting, and is documented here because it is part of the result. The pipeline's automatic grid-centre picker takes the centroid of the first drug-like HETATM group in the PDB file. In 4TRO that group is the NAD cofactor (residue 301, 44 atoms), not the inhibitor; the centre it produced was [2.22, −32.75, 14.19]. The co-crystallised inhibitor ZID (residue 302, 52 atoms) sits 1.82 Å away at [3.82, −33.34, 13.56]. Because the INH–NAD adduct occupies the NAD-binding pocket, the two centroids nearly coincide, and the re-dock shifted scores by only 0.01–0.39 kcal/mol — but the correction matters in principle: on other structures the same default has landed 13–45 Å from the inhibitor site. All five ligands were re-docked at the ZID centroid with the same protocol, and only the corrected numbers are reported. The raw JSON of both runs is preserved (see Data availability), so the correction is auditable.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all three leads and isoniazid were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probabilities were SR-MMP 0.564 for CHEMBL259138, SR-MMP 0.165 for CHEMBL3125270 and NR-AhR 0.135 for CHEMBL3125235. These are similarity-based predictions, not measurements — and isoniazid itself carries a measured NR-AhR flag of 1.0 in the same panel, so a flag in this panel does not distinguish a lead from the reference drug.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; a single crystal structure (4TRO, one conformation) was used; free isoniazid was docked, not the INH–NAD adduct, so the isoniazid number is a prodrug baseline, not a potency estimate; and the three leads are already-known InhA inhibitors, so no novelty of chemistry is claimed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | InhA potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL3125235 | IC50 2.0 nM | **−10.27** | −10.27, −9.83, −9.51 | clean |
| CHEMBL3125270 | IC50 4.0 nM | **−9.37** | −9.37, −9.35, −9.01 | clean |
| CHEMBL259138 | Ki 1.0 nM | −7.50 | −7.50, −7.37, −7.25 | clean |
| Isoniazid (reference, free prodrug) | Ki 0.75 nM (as recorded) | −5.83 | −5.83, −5.67, −5.58 | clean |
| CHEMBL64 (= isoniazid, duplicate entry) | Ki 0.75 nM | −5.82 | −5.82, −5.80, −5.36 | clean |

All docking on PDB 4TRO (M. tuberculosis InhA, 1.40 Å), grid centre [3.82, −33.34, 13.56] (ZID adduct centroid), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 5 November 2026. CHEMBL3125235: MW 514.59, logP 2.94, 1 Lipinski violation (MW > 500). CHEMBL3125270: MW 423.47, logP 1.71, Lipinski-clean. CHEMBL259138: MW 271.36, logP 4.70, Lipinski-clean.

The headline number needs its qualifier in the same breath: CHEMBL3125235 beats free isoniazid by 4.44 kcal/mol and CHEMBL3125270 by 3.54 kcal/mol, both far outside Vina's noise — but free isoniazid is not the active species, and its −5.83 kcal/mol is the score of a small prodrug that was never meant to bind InhA on its own. The meaningful comparison in this table is among the three direct inhibitors themselves: CHEMBL3125235 leads CHEMBL3125270 by 0.90 kcal/mol (inside noise) and CHEMBL259138 by 2.77 kcal/mol. Pose consistency is good across the set: the top two leads hold within 0.76 and 0.36 kcal/mol across all three poses, while isoniazid holds within 0.25 kcal/mol — consistency is not what separates them; the binding pocket's shape is. Note also that CHEMBL64 and the query isoniazid are the same molecule entered twice by the pipeline (similarity 1.0); their near-identical scores (−5.82 vs −5.83) are an accidental reproducibility check, not two independent measurements.

### 3.2 Comparison with published docking

Published direct-InhA docking exists for comparison: a 2026 study of triazolopyrimidine direct InhA inhibitors reported binding energies of −13.93 and −13.14 kcal/mol for its best compounds, against triclosan at −8.67 kcal/mol and ethambutol at −7.15 kcal/mol, using a different docking setup and a different InhA structure. Our Vina numbers are not directly comparable to those energies, and no published Vina score for any of our three leads on 4TRO was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for three known InhA actives on 4TRO (−10.27, −9.37, −7.50 kcal/mol, with full pose lists) are now on record for others to reproduce. The ordering is also consistent with the published potencies in direction but not in magnitude: CHEMBL259138 has the best recorded potency (Ki 1.0 nM) yet the worst docking score of the three (−7.50), a reminder that Vina ranks poses, not IC50s.

### 3.3 The standardisation problem

The grid-centre audit in §2.3 is the durable methodological finding. The pipeline's centre picker — first non-junk HETATM group — silently centred on the NAD cofactor in 4TRO. Here the error was only 1.82 Å, because the adduct occupies the cofactor pocket, and the re-dock moved scores by at most 0.39 kcal/mol. But the same default has previously centred grids on a cofactor 13.26 Å from the inhibitor site and on a glycan 45.24 Å away, in both cases producing publishable-looking numbers for the wrong pocket. The fix is cheap — verify the co-crystallised ligand's identity and centroid before docking — but it is not optional, and it must be applied per structure, because the distance between the first HETATM group and the true inhibitor site is not predictable from the file alone.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into two narrower contributions. First, a benchmark: three known direct InhA inhibitors dock at −7.50 to −10.27 kcal/mol on the adduct-bound structure under a standardised protocol, with pose consistency good enough to reproduce. Second, a caution: the 3.5–4.4 kcal/mol "win" over isoniazid is real as a docking number and meaningless as a drug comparison, because the comparator is a prodrug. The clinically relevant question is not whether a direct inhibitor out-docks free isoniazid — any molecule that actually binds the pocket will — but whether it out-binds the INH–NAD adduct in KatG-mutant strains, and whether it kills whole bacilli. Neither is answered by docking.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the comparator is wrong: the active species is the adduct, and docking the adduct itself (or a KatG-independent reference such as triclosan, published at −8.67 kcal/mol in another setup) is the honest baseline. Second, potency and docking score disagree within the lead set: CHEMBL259138, the most potent by recorded Ki (1.0 nM), scores worst (−7.50), while CHEMBL3125235, the best docker (−10.27), is the least potent by recorded IC50 (2.0 nM) — a 2-fold potency spread against a 2.77 kcal/mol score spread, in the wrong direction. Third, all three leads are already-known InhA actives; there is no new chemistry here, only a new comparison.

### 4.3 The PAINS/tox picture is clean but thin

No PAINS alerts is good, but PAINS-clean is a low bar, and the Tox21 read-across flags (SR-MMP 0.564 for CHEMBL259138) are predictions from neighbours, not data. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either — least of all because the reference drug flags the same assay at 1.0.

### 4.4 Testable hypotheses

1. CHEMBL3125235 inhibits recombinant InhA with an IC50 within 2-fold of its ChEMBL value (2.0 nM) under identical assay conditions, and inhibits the KatG-independent enzyme directly, without activation.
2. CHEMBL3125235 and CHEMBL3125270 retain whole-cell activity (MIC) against a KatG S315T mutant M. tuberculosis strain where isoniazid loses ≥32-fold potency — the direct-inhibitor prediction that docking alone cannot test.
3. A Vina re-dock of the co-crystallised ZID adduct into 4TRO reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant InhA enzyme inhibition assay (NADH oxidation readout) for CHEMBL3125235, CHEMBL3125270 and the INH–NAD adduct as control, same plate, n = 3, with a pre-registered 2-fold decision rule. Stage 2 (weeks 3–6): whole-cell MIC against H37Rv and a KatG S315T mutant strain, isoniazid as control, with the pre-registered prediction that the leads lose <4-fold potency where isoniazid loses ≥32-fold. Stage 3 (weeks 7–12): cytotoxicity (Vero/THP-1) for any compound that clears Stage 2, with a selectivity index (CC50/MIC) > 10 required to proceed. Total compound cost is the binding constraint; all three leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. The isoniazid comparator is the free prodrug, not the INH–NAD adduct — the 3.5–4.4 kcal/mol margin is a prodrug artefact, not a potency claim. 3. Vina noise is ±1–2 kcal/mol; the 0.90 kcal/mol gap between the top two leads is not significant. 4. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of ZID was performed. 5. A single crystal structure (4TRO, one InhA conformation) was used; InhA's substrate-binding loop is flexible and induced-fit effects are not modelled. 6. All three leads are already-known InhA inhibitors; no new chemical matter is proposed. 7. No whole-cell, resistance-strain, or Pakistani-market data are presented; the Pakistan burden figures are contextual, not part of the result. 8. The pipeline's automated grid-centre selection failed silently and required manual correction — other silent defaults in the same pipeline are not yet audited.

## 6. Conclusion

Three known direct InhA inhibitors dock at −7.50 to −10.27 kcal/mol on the adduct-bound InhA structure (PDB 4TRO), beating free isoniazid (−5.83 kcal/mol) by 1.7–4.4 kcal/mol — a margin that is real as docking and meaningless as a drug comparison, because isoniazid is a prodrug and the adduct is the true comparator. The durable findings are the benchmark values themselves and the grid-centre audit: the pipeline centred on the NAD cofactor, 1.82 Å from the adduct site, and only a manual check caught it. The next experiment is a head-to-head InhA enzyme assay against the adduct, then MIC testing on a KatG S315T strain — not more docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. World Health Organization. Global tuberculosis report 2025. Geneva: WHO; 2025. https://www.who.int/publications/i/item/9789240116924 (accessed 5 November 2026).
2. Vilchèze C, Jacobs WR Jr. Resistance to isoniazid and ethionamide in Mycobacterium tuberculosis: genes, mutations, and causalities. *Microbiol Spectr.* 2014;2(4). doi:10.1128/microbiolspec.MGM2-0014-2013.
3. Miesel L, Rozwarski DA, Sacchettini JC, Jacobs WR Jr. Mechanisms for isoniazid action and resistance. *Novartis Found Symp.* 1998;217:209–221.
4. Synthesis and discovery of direct Enoyl-ACP Reductase (InhA) inhibitors via in-silico studies and ADMET prediction for potent anti-tubercular activity. *Research Square* preprint, posted 14 August 2026. doi:10.21203/rs.3.rs-10317124/v1.
5. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
6. RCSB Protein Data Bank. Structure of the enoyl-ACP reductase of Mycobacterium tuberculosis InhA, inhibited with the active metabolite of isoniazid. PDB ID 4TRO, 1.40 Å. https://www.rcsb.org/structure/4TRO (accessed 5 November 2026).
7. ChEMBL database, European Bioinformatics Institute. Target: enoyl-[acyl-carrier-protein] reductase [NADH] (CHEMBL1849); bioactivities accessed 5 November 2026. https://www.ebi.ac.uk/chembl/.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-018-2026-11-05.json` (pipeline run: UniProt P9WGR1, ChEMBL CHEMBL1849, 26 ranked leads; first docking run at the NAD-cofactor centre retained for audit) and `hidden_files/dock-HP-018c-2026-11-05.json` (authoritative re-dock: PDB 4TRO, 1.40 Å, ZID adduct centroid [3.82, −33.34, 13.56], Vina 1.2.7). ChEMBL IDs: isoniazid (CHEMBL64, query), CHEMBL3125235, CHEMBL3125270, CHEMBL259138. PDB ID 4TRO. No additional data were generated.
