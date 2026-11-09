# Three Diazabicyclooctanes "Beat" Avibactam by Docking and Lose by Less Than 1 kcal/mol of Noise: A Vina Benchmark of KPC-2 Inhibitors on 6TD0 — and the Boronate Blind Spot

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-08 · **Daily research paper — Health track (HP-012)**

**Keywords:** KPC-2; carbapenemase; avibactam; nacubactam; relebactam; diazabicyclooctane; molecular docking; AutoDock Vina; antimicrobial resistance; Klebsiella pneumoniae

---

## Abstract

Klebsiella pneumoniae carbapenemase (KPC-2) is the most commonly encountered class A beta-lactamase variant worldwide, and it confers high-level resistance to most available antibiotics; ceftazidime-avibactam is the standard inhibitor combination against it, but omega-loop variants such as D179N already escape it. We ran the LeadForge pipeline live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina docking): target KPC-2 (UniProt Q9F663, ChEMBL CHEMBL6132, 4 bioactivities retrieved), structure PDB 6TD0 at 0.99 angstrom, grid centred exactly on the co-crystallised vaborbactam (centroid [15.45, 8.23, 21.26]), and six ligands docked with AutoDock Vina 1.2.7 under an identical protocol. Nacubactam scored −7.65 kcal/mol, a 2-sulfamoyl diazabicyclooctane −7.50 and relebactam −7.35, against avibactam at −6.73 (re-dock −7.15) and tazobactam at −6.42 — margins of 0.62–0.92 kcal/mol, all inside Vina's ±1–2 kcal/mol noise, so no compound can be called better than avibactam on these scores. Two clinically important boronates, vaborbactam and taniborbactam, could not be docked at all: the pipeline writes boron as PDBQT atom type "B", which this Vina build rejects, and their covalent boron–Ser70 mechanism is outside non-covalent docking in any case. The falsifiable next step is a head-to-head KPC-2 inhibition assay (nitrocefin hydrolysis, purified enzyme, same plate) of nacubactam and relebactam against avibactam, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable Ki advantage; a measured Ki for nacubactam tighter than avibactam's would refute the noise interpretation, and re-running the same benchmark on the D179N variant structure (PDB 8G2R) would test whether the ranking survives the resistance mutation.

---

## 1. Introduction

The antimicrobial resistance (AMR) literature of the last 48 hours is a catalogue of the problem this paper works on. R-pyocins used as an evolutionary trap restored aminoglycoside sensitivity in a pan-drug-resistant clinical Pseudomonas aeruginosa isolate (Estrada et al., bioRxiv, updated 7 November 2026); vanA-positive vancomycin-resistant enterococci are highly prevalent in clinical isolates from central Iran, with linked biofilm and virulence profiles (Mezher et al., 2026); a pan-genome random-forest analysis of 465 pork-associated Salmonella Derby genomes separates isolates by country and finds Chinese isolates carrying the most AMR determinants, 15.3 per isolate (Chen & Cui, 2026); and a new review traces how biofilm tolerance becomes heritable resistance — the phenotype layer that gene-presence screens miss (Guchhait et al., 2026). The field is moving from detecting resistance to reversing it, and the tools for the detection side are still being built: SCCmecExtractor, a lightweight toolkit that extracts staphylococcal cassette chromosome elements from whole genomes, was benchmarked on 7,297 genomes across 70 species this month (MacFadyen, 2026). Against that background, the beta-lactamase inhibitor — the molecule that protects the antibiotic rather than killing the bacterium — remains the most clinically proven resistance-reversal strategy in routine use.

KPC-2 is the target that justifies that claim. It is, in the words of a 2021 mechanistic study, "the most commonly encountered class A beta-lactamase variant worldwide, which confer high-level resistance to most available antibiotics" (Lizana et al., 2021). It hydrolyses penicillins, cephalosporins, monobactams and carbapenems. The inhibitor that changed its clinical management is avibactam, a diazabicyclooctane (DBO) that inhibits KPC-2 by reversible covalent acylation of the catalytic Ser70: acylation and deacylation both proceed through a tetrahedral intermediate, with activation barriers of 19.5 and 23.0 kcal/mol and an estimated inhibition constant of 3.3 × 10⁻³, reported as in good agreement with the experimental value (Lizana et al., 2021). Avibactam is given with ceftazidime, and it is the reference drug for this benchmark.

Three other DBOs matter for the comparison. Relebactam is an approved DBO inhibitor given with imipenem–cilastatin. Nacubactam (OP0595) is an investigational DBO in development with meropenem; it differs from avibactam by an aminoethoxy side chain that was designed to add direct antibacterial activity against Pseudomonas aeruginosa through penicillin-binding-protein inhibition. A fourth DBO, a 2-sulfamoyl analogue with no preferred name in ChEMBL (CHEMBL5483057; PubChem CID 172433364), is a close structural cousin of avibactam. Tazobactam, a penam sulfone, is the negative control: a beta-lactamase inhibitor with no useful KPC-2 activity. And two cyclic boronates, vaborbactam (approved, with meropenem) and taniborbactam (investigational), are the inhibitors this pipeline cannot dock — a failure that is itself a result, reported below.

The falsifiable hypothesis of this paper is that one or more of these DBOs binds KPC-2 more favourably than avibactam by a margin large enough to predict a measurable potency advantage, and that the docking margin predicts the measured ranking. The paper then tests that hypothesis against Vina's own noise floor and against the covalent mechanism that non-covalent docking cannot see.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 8 November 2026: the daily literature digest at `~/workspace/research-team/digests/2026-11-08.md` (465 candidates screened, 8 selected), PubMed E-utilities, ChEMBL (EBI), UniProtKB and RCSB PDB. Key sources: Lizana et al. (2021) for the KPC-2 burden statement and the avibactam acylation/deacylation mechanism; Estrada et al. (2026, bioRxiv) for R-pyocin resistance reversal; Mezher et al. (2026) for vanA VRE prevalence; Chen & Cui (2026) for the Salmonella Derby AMR landscape; Guchhait et al. (2026) for the biofilm tolerance-to-resistance review; MacFadyen (2026) for SCCmecExtractor; Mastropietro & Bajorath (2026) and Singh et al. (2026) for the current state of agentic and computational lead optimisation, the context in which this pipeline operates. No measured Ki or IC50 values for the ranked DBOs against KPC-2 are reported in this paper, because none were retrievable from ChEMBL for this target (see §2.4) — that absence is a finding, not an omission, and the proposed assay is designed to fill it.

### 2.2 LeadForge pipeline

The LeadForge pipeline was run live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target: Klebsiella pneumoniae carbapenemase KPC-2, UniProt Q9F663; ChEMBL CHEMBL6132 ("Carbapenem-hydrolyzing beta-lactamase KPC", single protein, Klebsiella pneumoniae). ChEMBL returned 4 bioactivities for this target, and the pipeline ranked five leads by composite score (similarity × 40 + Lipinski × 20 + Veber × 10 + PAINS × 10 + tox × 20): the avibactam query (99.8), its ChEMBL record CHEMBL1689063 (99.8), the 2-sulfamoyl DBO CHEMBL5483057 (75.9), nacubactam CHEMBL3989959 (74.6) and tazobactam CHEMBL404 (64.9). Three named clinical comparators — relebactam, vaborbactam and taniborbactam — were added by PubChem name lookup (CIDs 44129647, 56649692, 76902493) and docked at the same centre under the identical protocol.

### 2.3 Molecular docking

Docking was performed with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 angstrom cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was KPC-2, PDB 6TD0 (0.99 angstrom, "Crystal structure of vaborbactam bound to KPC-2"), with the grid centred exactly on the centroid of the co-crystallised vaborbactam, residue 4D6 chain A 301: [15.45, 8.23, 21.26]. The centre was verified against the PDB file: the two alternate-location conformers of vaborbactam have centroids [15.45, 8.22, 21.34] (altloc A) and [15.45, 8.24, 21.18] (altloc B), both within 0.08 angstrom of the grid centre, and the only other non-water hetero groups in the file are glycerol and sulfate, which the centre picker excludes — the grid-centre fault that has corrupted earlier runs (centring on a cofactor, glycan or lipid) did not occur here. The avibactam-bound wild-type structure 4ZBE (1.8 angstrom) was checked as the alternative and not used, because 6TD0 is the higher-resolution structure and its co-crystallised ligand is also a KPC-2 inhibitor. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

Avibactam was docked twice — once by the pipeline (−6.73 kcal/mol) and once as an independent re-dock at the identical centre, box and exhaustiveness (−7.15 kcal/mol) — as a reproducibility check on the protocol. The 0.42 kcal/mol spread between the two runs is the protocol's own run-to-run variation and is carried into every comparison below.

### 2.4 The boronate failure

Vaborbactam and taniborbactam could not be docked. Ligand preparation (meeko) writes the boron atom as PDBQT atom type "B", and Vina 1.2.7 rejects it: "PDBQT parsing error: Atom type B is not a valid AutoDock type (atom types are case-sensitive)." Both compounds failed identically, at the same step, with no poses produced. Two consequences follow. First, the co-crystallised ligand of 6TD0 could not be re-docked, so no self-docking validation of the protocol against the crystal pose is available for this structure — the avibactam re-dock above is the only reproducibility check. Second, the two boronates are exactly the compounds whose mechanism Vina could not model even if the atom type were accepted: cyclic boronates inhibit KPC-2 by forming a covalent bond between boron and the Ser70 oxygen, a tetrahedral boronate adduct, and non-covalent docking has no term for it. Mapping boron onto carbon to force a score would produce a number that misrepresents the chemistry, so no such score is reported. The boronate gap is a limitation of this pipeline, stated here so that a later run with boron-capable docking (or a covalent-docking protocol) can close it.

### 2.5 PAINS and ToxGuard screens

Every compound was screened with the RDKit PAINS filter (A/B/C catalogues) and a ToxGuard Tox21 kNN read-across panel (12 assays). All six docked compounds are PAINS-clean. Read-across probabilities are low throughout (highest single assay probability 0.148, avibactam NR-AR; nacubactam's highest is SR-ARE 0.105; relebactam's highest is NR-ER 0.081; tazobactam's highest is NR-AR 0.054), but the nearest-neighbour similarities are also low (maximum 0.22–0.34), so these are weak read-acrosses, not safety findings. The named boronates are likewise PAINS-clean, with vaborbactam's highest read-across SR-ARE 0.319 and taniborbactam's NR-AhR 0.154 — again weak read-acrosses, and both are approved or late-stage compounds, so the panel adds no liability signal.

### 2.6 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement, binding-free-energy calculation, covalent docking, or re-docking validation of the co-crystallised ligand was performed (the boronate failure, §2.4); a single crystal structure (6TD0, one KPC-2 conformation) was used; and, most importantly, every DBO in this benchmark inhibits KPC-2 by reversible covalent acylation of Ser70 — a mechanism Vina cannot model — so every score reported here is missing the dominant binding term, exactly as the NDM-1 paper's zinc and the CYP51 paper's haem coordination were missing from theirs. ChEMBL holds no pChEMBL values for KPC-2 (all 50 recorded activities for CHEMBL6132 lack pChEMBL, and the retrieved bioactivities are substrate-hydrolysis and MIC records, not inhibitor potencies), so no measured ranking exists to check the docking ranking against. The leads are already-known inhibitors, so no novelty of chemistry is claimed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Class | Best affinity (kcal/mol) | Poses (kcal/mol) | MW | logP | Lipinski violations | Veber | PAINS | Top tox read-across |
|---|---|---|---|---|---|---|---|---|---|
| Nacubactam (CHEMBL3989959) | DBO | **−7.65** | −7.65, −7.38, −6.82 | 324.31 | −2.00 | 0 | fail (TPSA 151.5) | clean | SR-ARE 0.105 |
| 2-sulfamoyl-DBO (CHEMBL5483057) | DBO | −7.50 | −7.50, −7.00, −6.81 | 301.30 | −1.76 | 0 | fail (TPSA 147.3) | clean | SR-MMP 0.104 |
| Relebactam (CID 44129647) | DBO | −7.35 | −7.35, −7.11, −6.80 | 348.38 | −1.14 | 0 | pass | clean | NR-ER 0.081 |
| Avibactam, pipeline (QUERY) | DBO | −6.73 | −6.73, −6.60, −6.32 | 265.25 | −1.53 | 0 | pass | clean | NR-AR 0.148 |
| Avibactam, re-dock | DBO | −7.15 | −7.15, −6.42, −6.21 | 265.25 | −1.53 | 0 | pass | clean | NR-AR 0.148 |
| Avibactam, ChEMBL record (CHEMBL1689063) | DBO | −6.62 | −6.62, −6.58, −6.55 | 265.25 | −1.53 | 0 | pass | clean | NR-AR 0.148 |
| Tazobactam (CHEMBL404) | penam sulfone | −6.42 | −6.42, −5.69, −5.37 | 300.30 | −1.52 | 0 | pass | clean | NR-AR 0.054 |
| Vaborbactam (CID 56649692) | cyclic boronate | **not docked** | — | 297.14 | 0.45 | 0 | pass | clean | SR-ARE 0.319 |
| Taniborbactam (CID 76902493) | cyclic boronate | **not docked** | — | 389.26 | 0.32 | 0 | pass | clean | NR-AhR 0.154 |

Tanimoto similarity (Morgan fingerprints) to avibactam: relebactam 0.612, 2-sulfamoyl-DBO 0.659, nacubactam 0.646, tazobactam 0.127, vaborbactam 0.099, taniborbactam 0.098.

### 3.2 The margins are noise

Against the pipeline's avibactam score (−6.73), nacubactam leads by 0.92 kcal/mol, the 2-sulfamoyl DBO by 0.77 and relebactam by 0.62. Against the avibactam re-dock (−7.15), the same margins shrink to 0.50, 0.35 and 0.20. Every margin is inside Vina's ±1–2 kcal/mol noise, and the choice of which avibactam run to compare against moves the "win" by almost half. The ranking is also fragile at the level of individual poses: relebactam's second pose (−7.11) is already worse than nacubactam's best, and tazobactam's best pose (−6.42) is only 0.20–0.31 kcal/mol behind avibactam's — a molecule with no useful KPC-2 activity scores within noise of the reference drug. That is the control working as intended: it shows the protocol cannot separate an active DBO from an inactive penam sulfone on scores alone.

### 3.3 The boronate blind spot

The two compounds the pipeline could not dock are not marginal. Vaborbactam is the co-crystallised ligand of the very structure used here, and it is an approved KPC-2 inhibitor; taniborbactam is the broadest-spectrum boronate in development, active against both serine- and metallo-beta-lactamases. Their absence from the table is a property of the tooling, not of the molecules, and it biases the benchmark in a specific direction: the only inhibitors that survive the pipeline are the ones whose chemistry Vina can represent, which is exactly the set whose covalent mechanism Vina cannot score. A benchmark that cannot dock its own structure's ligand is a benchmark that should be read as a pose screen of DBOs, not as a ranking of KPC-2 inhibitors.

### 3.4 The resistance-variant angle

Structures of KPC-2 variants in complex with avibactam are already deposited: the D179N variant (PDB 8G2R, 1.28 angstrom) and the G89D mutant (PDB 8RWP, 1.19 angstrom), alongside the wild-type avibactam complex 4ZBE (1.8 angstrom). The D179N structure is the direct structural counterpart of the ceftazidime-avibactam escape route: the omega loop that positions the catalytic machinery. No docking was run on 8G2R in this paper; it is named here as the immediate follow-up, because a DBO that only beats avibactam on wild-type KPC-2 is of limited use if the ranking collapses on the variant that actually circulates under ceftazidime-avibactam pressure.

## 4. Discussion

### 4.1 The reframe

The honest reading of Table 3.1 is not "three DBOs beat avibactam" but "four DBOs and one inactive control all score within about 1.2 kcal/mol of each other on wild-type KPC-2, and the two boronates cannot be scored at all." That is a negative result about the method, and it is consistent with the three previous benchmarks in this series: flavonoids "beat" acarbose on alpha-amylase by ~1 kcal/mol of noise; five HER2 inhibitors docked within noise of lapatinib; five COX-2 inhibitors showed docking selectivity that did not track measured selectivity. The pattern is now four for four: on a single-structure, single-protocol Vina benchmark, the reference drug is never beaten by a margin the method can defend.

### 4.2 Why the "win" must not be over-read

Three separate reasons, each sufficient. First, the noise floor: Vina's ±1–2 kcal/mol error is larger than every margin in the table, and the avibactam re-dock alone moves the reference by 0.42 kcal/mol. Second, the missing mechanism: avibactam, nacubactam, relebactam and the sulfamoyl DBO all inhibit KPC-2 by reversible covalent acylation through a tetrahedral intermediate (Lizana et al., 2021), and Vina scores only the non-covalent pose — the same missing term that made the CYP51 benchmark blind to haem coordination and the NDM-1 benchmark blind to zinc. A DBO with a better non-covalent pose can still be the worse covalent inhibitor, and the assay that matters measures the acylation rate, not the pose. Third, the missing comparator: the boronates, which include the approved vaborbactam and the broad-spectrum taniborbactam, are absent, so the table cannot even claim to rank the clinically relevant set.

### 4.3 What the DBOs do offer

The result is not that the DBOs are interchangeable. Nacubactam's aminoethoxy side chain gives it direct antibacterial activity that avibactam lacks, and its development rationale is the combination with meropenem, not a better KPC-2 Ki. Relebactam's value is its approved combination with imipenem–cilastatin and its activity against KPC-producing isolates in that combination. The sulfamoyl DBO is a reminder that the DBO scaffold tolerates substitution at the 2-position — the same position that carries avibactam's carboxamide — and that ChEMBL's KPC-2 record, thin as it is, already contains analogues worth assaying. The docking table does not rank these properties; it only says that pose energy will not be the property that separates them.

### 4.4 Testable hypotheses

**H1 (noise):** In a head-to-head KPC-2 inhibition assay (nitrocefin hydrolysis, purified recombinant KPC-2, same plate, n = 3), nacubactam and relebactam show no measurable Ki advantage over avibactam (pre-registered rule: a docking margin under 2 kcal/mol predicts a Ki ratio within 2-fold). A measured Ki for nacubactam more than 2-fold tighter than avibactam's refutes H1 and would be the first evidence in this series that a sub-noise docking margin predicted a real advantage.

**H2 (variant):** The same four DBOs docked on the D179N variant structure (PDB 8G2R) at the avibactam centroid keep the wild-type ranking (nacubactam ≥ sulfamoyl-DBO ≥ relebactam ≥ avibactam). A re-ordering on 8G2R — in particular avibactam falling behind — would show the wild-type benchmark does not generalise to the resistance variant and would redirect the assay in H1 to the D179N enzyme.

**H3 (boronate):** With a boron-capable docking protocol (covalent docking or a Vina build that accepts boron), vaborbactam re-docked into 6TD0 reproduces the crystal pose within 2 angstrom RMSD and scores within 1 kcal/mol of the best DBO. Failure would show the boronate mechanism needs a different method entirely, not a patched atom type.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): nitrocefin-hydrolysis KPC-2 inhibition assay for nacubactam, relebactam, the 2-sulfamoyl DBO and avibactam, purified enzyme, same plate, n = 3, with the pre-registered 2-fold decision rule from H1; tazobactam as the negative control (expected: no measurable inhibition at the tested range). Stage 2 (weeks 3–6): if Stage 1 shows any genuine advantage, repeat on purified D179N KPC-2 (H2) and add a whole-cell assay against a KPC-2-producing Klebsiella pneumoniae isolate with the partner beta-lactam (ceftazidime for avibactam, meropenem for nacubactam, imipenem for relebactam) to test whether an enzyme-level advantage survives the outer membrane and efflux. Stage 3 (weeks 7–12): if Stage 1 shows none, the project stops at the benchmark and the paper stands as a negative result; the boronate arm (H3) is pursued only if a boron-capable protocol is available, otherwise it is recorded as a pipeline gap for a future run. Total compound cost is the binding constraint; avibactam, relebactam and tazobactam are approved drugs, nacubactam and the sulfamoyl DBO are research chemicals, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. Every "winning" margin (0.62–0.92 kcal/mol against the pipeline avibactam run; 0.20–0.50 against the re-dock) is inside Vina's ±1–2 kcal/mol noise and cannot be interpreted as a real advantage. 3. Vina cannot model the reversible covalent acylation of Ser70 that defines DBO inhibition, so every score is missing the dominant binding term. 4. The two boronates (vaborbactam, taniborbactam) could not be docked at all — boron is not a valid atom type in this Vina build — so the benchmark cannot rank the clinically relevant inhibitor set and no self-docking validation against the crystal pose was possible. 5. A single crystal structure (6TD0, one KPC-2 conformation) was used; no molecular-dynamics refinement, binding-free-energy calculation, or covalent docking was performed. 6. ChEMBL holds no pChEMBL values for KPC-2, so no measured ranking exists to check the docking ranking against; the four retrieved bioactivities are the entire ChEMBL ligand record for this target, which is thin for a target of this importance. 7. The D179N variant benchmark (H2) was not run. 8. The Tox21 read-across probabilities are similarity-based predictions with low nearest-neighbour similarity (0.22–0.34), not measurements. 9. The 2-sulfamoyl DBO has no preferred name in ChEMBL and is identified here by its ChEMBL ID and PubChem CID only.

## 6. Conclusion

Nacubactam, a 2-sulfamoyl diazabicyclooctane and relebactam dock to wild-type KPC-2 at −7.65, −7.50 and −7.35 kcal/mol, ahead of avibactam at −6.73 (re-dock −7.15) — but the margins are 0.62–0.92 kcal/mol against one avibactam run and 0.20–0.50 against the other, all inside Vina's noise; tazobactam, which has no useful KPC-2 activity, scores within 0.31 kcal/mol of avibactam; and the two boronates, including the structure's own co-crystallised ligand, cannot be docked at all. The honest reading is that on a covalent target with a thin ChEMBL record, non-covalent docking measures the method, not the molecule — and the next experiment is a nitrocefin KPC-2 assay with a pre-registered 2-fold rule, plus the same benchmark on the D179N variant, not more Vina docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Lizana I, Uribe EA, Delgado EJ. A theoretical approach for the acylation/deacylation mechanisms of avibactam in the reversible inhibition of KPC-2. *J Comput Aided Mol Des.* 2021;35(9):943–952. DOI: 10.1007/s10822-021-00408-3. PMID: 34236545.
2. Estrada I, Campbell D, Welch G, Smith P, Goldberg J, Rumbaugh K, Diggle S. R-pyocin-mediated selection reverses pan-drug resistance in Pseudomonas aeruginosa. *bioRxiv.* Updated 7 November 2026. DOI: 10.64898/2026.08.04.742823.
3. Mezher RT, Abbas RR, Jabbar HA, Akbari M, Kashi M, Chegini Z, Shariati A. High prevalence of vanA-positive vancomycin-resistant Enterococcus faecalis and Enterococcus faecium: antibiotic resistance, biofilm formation, and virulence profiles. *Health Sci Rep.* 2026. DOI: 10.1002/hsr2.73468. PMID: 42985573.
4. Chen Z, Cui M. Comparative genomics and machine learning reveal antimicrobial resistance landscapes, population structures, and geographic signatures of pork-associated Salmonella Derby across major producing countries. *World J Microbiol Biotechnol.* 2026. DOI: 10.1007/s11274-026-05385-z. PMID: 42986490.
5. Guchhait KC, Dey S, Pradhan SR, Panda AK, Ghosh C. From biofilm tolerance to antimicrobial resistance: molecular adaptation strategies and emerging therapeutic vulnerabilities. *Front Microbiol.* 2026. DOI: 10.3389/fmicb.2026.1988464. PMID: 42991282.
6. MacFadyen AC. SCCmecExtractor: a tool for extracting staphylococcal cassette chromosome elements from whole-genome sequences. *Microb Genom.* 2026. DOI: 10.1099/mgen.0.001809. PMID: 42986781.
7. Tran VN, Lahane TS, Qaderi I, Harvey H, Burrows LL. Identification and characterization of new P. aeruginosa phages using a surface receptor platform. *bioRxiv.* 7 November 2026. DOI: 10.64898/2026.11.06.764861.
8. Mastropietro A, Bajorath J. From generative molecular design to agentic artificial intelligence in drug discovery. *ChemMedChem.* 2026. DOI: 10.1002/cmdc.70564. PMID: 42984375.
9. Singh R, Kumar R, Khatoon R, Chaudhary S, Verma P, Kumar R. Lead optimization in drug discovery: integrating advanced computational approaches for enhanced drug design. *Curr Comput Aided Drug Des.* 2026 (online ahead of print). DOI: 10.2174/0115734099506020261022104618. PMID: 42983246.
10. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
11. RCSB Protein Data Bank. Crystal structure of vaborbactam bound to KPC-2. PDB ID 6TD0, 0.99 angstrom. https://www.rcsb.org/structure/6TD0 (accessed 8 November 2026).
12. RCSB Protein Data Bank. Crystal structure of KPC-2 beta-lactamase complexed with avibactam. PDB ID 4ZBE, 1.8 angstrom. https://www.rcsb.org/structure/4ZBE (accessed 8 November 2026).
13. RCSB Protein Data Bank. Crystal structure of the KPC-2 D179N variant in complex with avibactam. PDB ID 8G2R, 1.28 angstrom. https://www.rcsb.org/structure/8G2R (accessed 8 November 2026).
14. RCSB Protein Data Bank. KPC-2 G89D mutant in complex with avibactam. PDB ID 8RWP, 1.19 angstrom. https://www.rcsb.org/structure/8RWP (accessed 8 November 2026).
15. ChEMBL database, European Bioinformatics Institute. Target: carbapenem-hydrolyzing beta-lactamase KPC (CHEMBL6132); compounds avibactam (CHEMBL1689063), nacubactam (CHEMBL3989959), tazobactam (CHEMBL404), CHEMBL5483057; bioactivities accessed 8 November 2026. https://www.ebi.ac.uk/chembl/.
16. UniProtKB. Beta-lactamase KPC-2, Klebsiella pneumoniae (Q9F663). https://www.uniprot.org/uniprotkb/Q9F663/entry (accessed 8 November 2026).
17. PubChem, National Center for Biotechnology Information. Vaborbactam (CID 56649692), relebactam (CID 44129647), taniborbactam (CID 76902493), [(5R)-7-oxo-2-sulfamoyl-1,6-diazabicyclo[3.2.1]octan-6-yl] hydrogen sulfate (CID 172433364). https://pubchem.ncbi.nlm.nih.gov/ (accessed 8 November 2026).

## Data availability

All docking scores reported here are in `hidden_files/pipeline-HP-012-2026-11-08.json` (pipeline run, including the five-lead docking on 6TD0) and `hidden_files/dock-HP-012-named-2026-11-08.json` (named comparators and the avibactam re-dock), with PAINS and ToxGuard panels in `hidden_files/pains-tox-HP-012-named-2026-11-08.json` and `hidden_files/tox-HP-012-named-2026-11-08.json`. Target: UniProt Q9F663, ChEMBL CHEMBL6132. PDB ID 6TD0. No additional data were generated.
