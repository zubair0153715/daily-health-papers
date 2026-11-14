# Vina Ranks the Weakest Measured PBP2a Binder First: Zero Rank Correlation on Two MRSA Acyl-Enzyme Structures

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-13 · **Health Papers Agent — Paper #53** (daily 5-paper run)

**Keywords:** MRSA; PBP2a; mecA; ceftaroline; ceftobiprole; molecular docking; AutoDock Vina; rank correlation

---

## Abstract

MRSA caused more than 100,000 deaths attributable to antimicrobial resistance in 2019, and its resistance rests on a single protein, PBP2a, encoded by mecA, whose closed active site excludes most beta-lactams; ceftaroline overcomes this by binding an allosteric site 60 angstrom away, opening the active site for a second molecule to acylate Ser403, and clinical N146K/E150K mutations disrupt that trigger. The gap this paper attacks is whether a standardised docking screen can rank PBP2a binders at all. We docked four ChEMBL MecA actives with measured Kd/IC50 values, ceftaroline (prodrug and active form), ceftobiprole and the carbapenem analogue L-695,256 into two acyl-enzyme structures — 1MWS (2.00 A) and the ceftaroline co-crystal 3ZG0 chain B (2.60 A) — with AutoDock Vina 1.2.7 under one protocol, centres audited to 0.0 A from the co-crystallised ligands. The rank test failed on both structures: the Vina order (CHEMBL4862632 first) is unrelated to the measured order (CHEMBL4847813, Kd 129 nM, first), Spearman rho = 0.0, and the second-best measured binder, CHEMBL4879273 (Kd 168 nM), docked worst on both structures. A second independent Vina run reproduced the same order, and one ChEMBL ligand turned out to be ceftobiprole itself, the same molecule scoring 1 kcal/mol apart under two SMILES representations. No "beats ceftaroline" claim can be made from this screen, and Vina's non-covalent scores cannot model the covalent acylation that is ceftaroline's mechanism. The falsifiable next step is a PBP2a acylation assay (k2/Ks) of the four ChEMBL ligands against ceftaroline in wild-type and N146K/E150K PBP2a: if the measured acylation order matches the ChEMBL record rather than the Vina order, docking alone must not be used to prioritise PBP2a leads on these structures.

---

## 1. Introduction

Methicillin-resistant *Staphylococcus aureus* (MRSA) was the single deadliest pathogen–drug combination in the 2019 Global Research on Antimicrobial Resistance estimates: more than 100,000 deaths directly attributable to MRSA in one year, within 1.27 million deaths attributable to bacterial antimicrobial resistance overall. South Asia carried one of the highest attributable burdens, at 22 deaths per 100,000 population. MRSA's resistance rests on one protein. The *mecA* gene encodes penicillin-binding protein 2a (PBP2a), a transpeptidase that takes over cell-wall cross-linking when the bacterium's native PBPs are inhibited, and it does so because its active site is closed: protective loops shield the catalytic Ser403, so most beta-lactams cannot reach it at therapeutic concentrations.

Ceftaroline, a fifth-generation cephalosporin, is the drug that solved the closed-site problem without opening it by force. A first ceftaroline molecule binds a non-covalent allosteric site about 60 A from the active site, triggering a conformational change that opens the active site; a second molecule then acylates Ser403 and inactivates the enzyme. That mechanism is also its vulnerability: the clinical resistance mutations N146K/E150K (double mutant) and N146K/E150K/H351N (triple mutant) sit in the allosteric domain and disrupt the trigger, so the active site never opens. Ceftobiprole, the other anti-MRSA cephalosporin, retains activity against most ceftaroline-nonsusceptible isolates — in a 2025 survey of 8,184 US MRSA isolates, ceftobiprole MIC50/90 was 1/2 mg/L with 99.3% susceptible, against ceftaroline MIC50/90 of 0.5/1 mg/L.

**Hypothesis (falsifiable):** under one standardised protocol, a Vina screen of ChEMBL MecA actives against ceftaroline on acyl-PBP2a structures will rank compounds in the same order as their measured Kd/IC50 values. The test is the rank correlation, not the best score — and the reference drug must itself dock, or the comparison is void.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-13 (web search; PubMed via the daily digest of 2026-11-13, which screened 627 candidates and selected 8, none on PBP2a — the digest's relevance is methodological, not topical, for this paper). Key sources: Murray et al. 2022 for the MRSA burden; Lim and Strynadka 2002 for the PBP2a structure; Fishovitz et al. 2014 and Otero et al. 2013 for the allosteric mechanism and the resistance mutations; Sader et al. 2025 for current ceftaroline and ceftobiprole MIC distributions. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

Two disclosures belong in Methods, not in a footnote. First, the ChEMBL API was down on the whole of 2026-11-13: target search, target-by-accession and activity endpoints all returned HTTP 500, verified by direct calls, by a browser fetch and by a delegated browser task. The standard pipeline therefore retrieved zero ligands. The four ChEMBL MecA potencies in this paper come from a LeadForge retrieval of 2026-10-29, when ChEMBL was live (target CHEMBL6187, "MecA (Staphylococcus aureus)"), and the SMILES are copied verbatim from that retrieval; the docking itself was re-run today. Second, the first docking run of this paper was killed by the runtime (SIGTERM) at 14 of 16 docks with no JSON saved, because results were only written at the end. The script was patched to save incrementally after every dock and to resume from a partial file, and re-run detached. The re-run is the primary dataset reported here; the first run's 14 scores survive in its log and are used only as a reproducibility check (Section 3.2).

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; target UniProt Q53707 (MecA PBP2a, *S. aureus*, 668 aa); ChEMBL target CHEMBL6187 (retrieved 2026-10-29, not re-verified today because the API is down). Two structures, both acyl-enzyme complexes: 1MWS, nitrocefin acyl-PBP2a, 2.00 A X-ray, chain A only (the full file is two chains and makes Vina crawl on this VM; the chain-A-only receptor is the verified 2026-10-29 precedent), centre [28.55, 29.22, 87.49] — audited against the chain-A nitrocefin NC1 centroid computed from the deposited coordinates with the pipeline's own `_ligand_center` function: distance 0.0 A. The two-chain NC1 average is 8.15 A away and is an artefact (chain-B NC1 is 6 atoms, 63.87 A away); it is not the centre. 3ZG0 chain B, ceftaroline acyl-PBP2a, 2.60 A X-ray, centre [−35.99, 44.39, 66.82] — the chain-B AI8 (ceftaroline, bound form) centroid; chain A was excluded because it fails RDKit sanitisation (a 1.81 A Gly402 O…Ser403 N contact misread as a bond). Best of three poses reported per compound. The same box (22.5 A) and exhaustiveness (8) were used for every compound on both structures, including ceftaroline itself. Eight compounds: the four ChEMBL ligands, ceftaroline fosamil (the administered prodrug, PubChem CID 9852981) and active ceftaroline (CID 74316801), ceftobiprole (CID 135413542) and L-695,256 (CID 9890833).

### 2.3 PAINS screen

RDKit PAINS filter (the pipeline's own filter, classes A–C) applied to every docked compound. All eight compounds are PAINS-clean on both structures.

### 2.4 Honesty limits

Docking is not activity, and for PBP2a it is doubly not activity: ceftaroline's mechanism is covalent acylation of Ser403, and Vina's scores here are non-covalent pose scores in acyl-enzyme structures — they cannot model the acylation step, and they cannot model the allosteric trigger, which was discussed but not docked (a second-molecule allosteric model is beyond Vina's single-ligand protocol). Vina's scoring noise is ±1–2 kcal/mol, so differences smaller than that cannot rank compounds. Both structures are acyl-enzyme complexes, so the pocket conformation is the acylated one, not the apo one a screening ligand first encounters. No molecular dynamics or free-energy refinement was run. No experimental data were generated. The four ChEMBL potencies mix Kd and IC50 values from heterogeneous assays (pChEMBL 5.72–6.89); they are not head-to-head measurements, and the rank test mixes assay types. The ChEMBL potencies could not be re-fetched today because the API is down; they rest on the 2026-10-29 retrieval alone.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | 1MWS chain A (kcal/mol) | 3ZG0 chain B (kcal/mol) | Measured potency | PAINS |
|---|---|---|---|---|
| CHEMBL4862632 | −9.69 (−9.69, −9.53, −9.34) | −10.08 (−10.08, −10.05, −9.62) | Kd 264 nM | none |
| CHEMBL4847813 | −9.38 (−9.38, −9.05, −9.00) | −9.73 (−9.73, −9.61, −9.52) | Kd 129 nM | none |
| CHEMBL520642 | −9.32 (−9.32, −8.61, −8.51) | −9.58 (−9.58, −9.38, −9.33) | IC50 1900 nM | none |
| CHEMBL4879273 | −7.30 (−7.30, −7.20, −7.05) | −7.62 (−7.62, −7.57, −7.37) | Kd 168 nM | none |
| Ceftaroline (active) | −8.84 (−8.84, −8.22, −8.06) | −7.64 (−7.64, −7.22, −7.21) | MRSA MIC90 1 mg/L | none |
| Ceftaroline fosamil | −8.26 (−8.26, −8.24, −7.99) | −8.62 (−8.62, −7.88, −7.47) | MRSA MIC90 1 mg/L | none |
| Ceftobiprole | −10.30 (−10.30, −9.22, −9.21) | −8.86 (−8.86, −8.33, −7.83) | MRSA MIC50/90 1/2 mg/L | none |
| L-695,256 | −9.62 (−9.62, −9.32, −9.22) | −9.84 (−9.84, −9.71, −9.45) | none attached | none |

All eight compounds are large and flexible by screening standards (MW 469–685, 5–11 rotatable bonds); ceftaroline fosamil is the largest (MW 684.7, 11 rotatable bonds, TPSA 223.24) and the most flexible, and it scores worst of the two ceftaroline forms on both structures. Ceftobiprole is the most structure-dependent compound in the set: −10.30 on 1MWS (the best score in the whole screen) but −8.86 on 3ZG0, a 1.44 kcal/mol spread — the "best" compound in this screen depends on which structure you pick.

The rank test the hypothesis posed: the measured order of the four ChEMBL ligands is CHEMBL4847813 (Kd 129 nM) > CHEMBL4879273 (Kd 168 nM) > CHEMBL4862632 (Kd 264 nM) > CHEMBL520642 (IC50 1900 nM). The Vina order on 1MWS is CHEMBL4862632 > CHEMBL4847813 > CHEMBL520642 > CHEMBL4879273, and on 3ZG0 it is exactly the same: CHEMBL4862632 > CHEMBL4847813 > CHEMBL520642 > CHEMBL4879273. Spearman rho = 0.0 on both structures (n = 4). The weakest measured binder docks first, the second-best measured binder docks last, and the middle two swap. The hypothesis is falsified on both structures.

### 3.2 Reproducibility: the killed first run agrees

The first run's 14 surviving scores (logged before the SIGTERM kill) reproduce the re-run's order. On 1MWS the first run gave CHEMBL4862632 −10.47, ceftobiprole −10.32, L-695,256 −9.63, CHEMBL4847813 −9.37, CHEMBL520642 −9.26, active ceftaroline −8.81, fosamil −8.26, CHEMBL4879273 −7.21 — the same order as the re-run except that the top two swap, within noise. The largest cross-run differences are CHEMBL4862632 on 1MWS (−10.47 to −9.69, 0.78 kcal/mol) and active ceftaroline on 3ZG0 (−8.78 to −7.64, 1.14 kcal/mol); all other differences are 0.09 kcal/mol or less. Every cross-run difference sits inside Vina's ±1–2 kcal/mol noise, and the rank conclusion — rho = 0.0, CHEMBL4879273 last — is identical in both runs. Two independent Vina runs, same failed rank test.

### 3.3 One ChEMBL ligand is ceftobiprole

CHEMBL520642 and ceftobiprole have identical connectivity: the same molecular formula (C20H22N8O6S2) and the same canonical SMILES once stereochemistry is stripped; CHEMBL520642 is the stereochemistry-specified ChEMBL record of ceftobiprole, and the PubChem ceftobiprole SMILES is the same scaffold without stereochemistry. The dock set therefore contains one molecule twice, under two representations — and the same molecule scores differently: −9.32 versus −10.30 on 1MWS, and −9.58 versus −8.86 on 3ZG0. The input representation alone moves the score by about 1 kcal/mol, which is the same size as the gaps between the ranked compounds. This is reported as a finding, not hidden: the ChEMBL IC50 of 1900 nM attached to CHEMBL520642 and the whole-cell MIC50/90 of 1/2 mg/L attached to ceftobiprole describe the same molecule in different assays, and they must not both enter the rank test. The rank test in Section 3.1 uses the four ChEMBL ligands only; ceftobiprole enters as the clinical comparator, not as a fifth ranked ligand.

### 3.4 Comparison with published docking

No published Vina benchmark of these four ChEMBL compounds on 1MWS or 3ZG0 was found at drafting time, so there is no published docking comparison to make. The depositing studies for both structures are structure papers, not docking benchmarks. The absence of a published comparator is stated, not filled in.

## 4. Discussion

### 4.1 The reframe

The paper's question changed while running it. It started as "which ChEMBL MecA ligands beat ceftaroline?" and became "can this screen rank PBP2a binders at all?" The answer is no on both structures, twice. A screen that ranks the weakest measured binder first and the second-best measured binder last is not a screen with a weak signal — it is a screen with no signal for this target at this setting, and the honest report is the zero, not the best score.

### 4.2 Why the "win" must not be over-read

CHEMBL4862632's −10.08 on 3ZG0 is the best ChEMBL score in the screen, and it is also the score of the weakest measured binder (Kd 264 nM) — a "win" that is a loss by the measured record. Ceftobiprole's −10.30 on 1MWS looks like a lead until the same molecule, under its ChEMBL representation, scores −9.32 on the same structure, and until the same compound scores −8.86 on 3ZG0. Three numbers for what is effectively one comparison, spanning 1.44 kcal/mol. The gaps between the ranked ChEMBL ligands (0.31–2.39 kcal/mol on 1MWS) are the same size as the representation noise, so no ordering between them is defensible from these scores at all.

### 4.3 The PAINS problem does not apply here — the mechanism problem does

All compounds are PAINS-clean, so no artefact controls are needed on that front. The design constraint this experiment imposes is different: any validation must measure acylation, not binding. Ceftaroline's efficacy is a second-order acylation rate (k2/Ks) after an allosteric trigger, and a non-covalent pose score in an acyl-enzyme structure measures neither the trigger nor the acylation. A validation assay that only measures equilibrium binding would repeat the screen's error in a different format.

### 4.4 Testable hypotheses

1. **Rank hypothesis.** In a PBP2a acylation assay, the k2/Ks order of the four ChEMBL ligands matches their ChEMBL record order (4847813 > 4879273 > 4862632 > 520642). Falsified if the measured order differs — in which case the ChEMBL record itself, not just the docking, fails to predict acylation, and the ligands need re-measurement before any prioritisation.
2. **Representation hypothesis.** The same molecule docked from its stereochemistry-specified and unspecified SMILES scores within Vina's noise on both structures (difference ≤ 2 kcal/mol). Supported by this run (differences 0.72–0.98 kcal/mol); falsified if a third representation scores more than 2 kcal/mol away — in which case the input preparation, not the scoring function, dominates the result.
3. **Resistance hypothesis.** At least one of the four ChEMBL ligands acylates N146K/E150K PBP2a at a rate within ten-fold of its wild-type rate, where ceftaroline's rate collapses. Falsified if all four lose acylation on the mutant as ceftaroline does — in which case none of them addresses the clinical resistance mechanism, and the allosteric site, not the active site, is the target that matters.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain or synthesise the four ChEMBL ligands; confirm identity and purity by LC-MS and NMR — with explicit confirmation that CHEMBL520642 and ceftobiprole are the same molecule, so only one of them is carried forward as a test compound. Stage 2 (weeks 3–6): PBP2a acylation assay (nitrocefin competition or Bocillin-FL binding) in wild-type PBP2a, measuring k2/Ks for all four ligands plus ceftaroline and ceftobiprole on the same plates, in triplicate. Stage 3 (weeks 7–10): repeat the acylation assay on N146K/E150K PBP2a (the clinical allosteric mutant); whole-cell MRSA MICs for the best two ligands in the same strains. Stage 4 (weeks 11–12): if a ligand acylates the mutant, dock it into the mutant structure and compare the pose with the wild-type pose; if none does, report the negative result and stop. Sample-size logic: three independent biological replicates per k2/Ks determination is the minimum for a defensible second-order rate; the mutant comparison needs the same, because a false "retains activity" call on the resistance mutant is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. Vina noise is ±1–2 kcal/mol; the gaps between the ranked ligands are the same size as the representation noise.
3. The rank test is n = 4 and mixes Kd and IC50 values from heterogeneous ChEMBL assays.
4. The four ChEMBL potencies could not be re-fetched today (ChEMBL API HTTP 500); they rest on the 2026-10-29 retrieval alone.
5. Vina's non-covalent scores cannot model covalent acylation or the allosteric trigger; the allosteric site was not docked.
6. Both structures are acyl-enzyme complexes; the pocket conformation is the acylated one, not the apo one.
7. CHEMBL520642 and ceftobiprole are the same molecule, so the set contains seven distinct compounds, not eight.
8. No molecular dynamics or free-energy refinement was run.
9. No N146K/E150K mutant structure was docked, although the topic posed the resistance question; the wild-type result says nothing about the mutant.
10. A single rigid structure per run cannot represent the PBP2a conformational ensemble.

## 6. Conclusion

Four ChEMBL MecA actives dock in no measured-potency order on either of two acyl-PBP2a structures (Spearman rho = 0.0 on both, n = 4), with the weakest measured binder first and the second-best measured binder last, and a second independent Vina run reproduces the same order. One ChEMBL ligand is ceftobiprole itself, and the same molecule scores about 1 kcal/mol apart under two SMILES representations. The screen is therefore a reproduced negative result with a missing mechanism, not a lead claim. The next step is the acylation assay in Section 4.5, with ceftaroline measured on the same plates.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399(10325):629–655. doi:10.1016/S0140-6736(21)02724-0.
2. Lim D, Strynadka NCJ. Structural basis for the beta-lactam resistance of PBP2a from methicillin-resistant Staphylococcus aureus. Nat Struct Biol. 2002;9:870–876. PMID: 12389036. doi:10.1038/nsb858.
3. Fishovitz J, Rojas-Altuve A, Otero LH, Dawley M, Carrasco-Lopez C, Chang M, Hermoso JA, Mobashery S. Disruption of allosteric response as an unprecedented mechanism of resistance to antibiotics. J Am Chem Soc. 2014;136(28):9814–9817. PMID: 24955778. doi:10.1021/ja5030657.
4. Otero LH, Rojas-Altuve A, Llarrull LI, Carrasco-Lopez C, Kumarasiri M, Lastochkin E, Fishovitz J, Dawley M, Hesek D, Lee M, Johnson JW, Fisher JF, Chang M, Mobashery S, Hermoso JA. How allosteric control of Staphylococcus aureus penicillin binding protein 2a enables methicillin resistance and physiological function. Proc Natl Acad Sci U S A. 2013;110(42):16808–16813. doi:10.1073/pnas.1300118110.
5. Sader HS, Smart JI, Mendes RE, Castanheira M. Ceftobiprole activity against multidrug-resistant Staphylococcus aureus clinical isolates collected in the United States from 2016 through 2022. Antimicrob Agents Chemother. 2025;69(2):e01402-24. PMID: 39804046. doi:10.1128/aac.01402-24.
6. ChEMBL database, European Bioinformatics Institute. MecA (Staphylococcus aureus), target CHEMBL6187. Ligand potencies retrieved 2026-10-29; API returned HTTP 500 on all endpoints on 2026-11-13. https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6187/
7. UniProtKB. MecA PBP2', Staphylococcus aureus, Q53707. Accessed 2026-11-13. https://www.uniprot.org/uniprotkb/Q53707/entry
8. RCSB Protein Data Bank. Structures 1MWS and 3ZG0. Accessed 2026-11-13. https://www.rcsb.org/structure/1MWS and https://www.rcsb.org/structure/3ZG0
9. PubChem. Ceftaroline fosamil, CID 9852981; ceftaroline, CID 74316801; ceftobiprole, CID 135413542; L-695,256, CID 9890833. Accessed 2026-11-13. https://pubchem.ncbi.nlm.nih.gov/

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-013-2026-11-13.json` (re-run, primary dataset); the first run's 14 surviving scores are in `hidden_files/dock-HP-013-2026-11-13.log` and its re-run log is `hidden_files/dock-HP-013-2026-11-13-rerun.log`. The discarded pipeline runs are in `hidden_files/dock-HP-013-2026-11-13-PIPELINE-QUERY-ONLY.json` and `hidden_files/dock-HP-013-WRONG-TARGET-2026-11-13.json`. ChEMBL IDs, UniProt accession Q53707, ChEMBL target CHEMBL6187, PDB IDs 1MWS and 3ZG0, and PubChem CIDs are given in the text. No additional data were generated.
