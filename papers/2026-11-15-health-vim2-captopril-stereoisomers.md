# Four Captopril Stereoisomers Dock Within 0.07 kcal/mol on VIM-2 While Their Measured Potencies Span 76-Fold: Rigid Docking Is Blind to the Stereochemistry That Defines MBL Inhibition

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-15 · **Health Papers Agent — Paper #61** (daily 5-paper run)

**Keywords:** VIM-2; metallo-beta-lactamase; captopril; stereoisomers; taniborbactam; molecular docking; AutoDock Vina; carbapenem resistance

---

## Abstract

VIM-2 is a B1 metallo-beta-lactamase that hydrolyses almost all beta-lactams including carbapenems, and no clinically useful inhibitor exists for it. The best measured inhibitor in the reference set, taniborbactam (Ki 0.02 µM), cannot be docked by AutoDock Vina at all because it contains boron, which Vina's PDBQT parser rejects — a tool limit the standard pipeline run for this paper hit and could not pass. The testable question that remains is whether rigid docking can resolve the potency gap between stereoisomers of the same molecule: D-captopril inhibits VIM-2 at 0.072 µM, L-captopril at 4.4 µM, and the two epi-isomers at 5.5 µM each, a 76-fold range from a single stereocentre flip, with crystal structures showing different binding modes. We docked all four stereoisomers with AutoDock Vina 1.2.7 on 4C1E, the 1.40 angstrom VIM-2 structure co-crystallised with D-captopril. The scores are minus 6.16, minus 6.19, minus 6.12 and minus 6.19 kcal/mol — a total span of 0.07 kcal/mol, thirty times smaller than Vina noise, with rank correlation against measured potency of 0.15. The screen cannot see the stereochemistry that defines this inhibition. The falsifiable next step is a single-assay IC50 comparison of the four stereoisomers on VIM-2 with a metal-aware rescoring of the same poses: if the measured 76-fold gap reproduces while every rescoring still ties them, the failure is confirmed as a scoring-function limit, not a pose-sampling error.

---

## 1. Introduction

Metallo-beta-lactamases (MBLs) are zinc-dependent enzymes that hydrolyse almost all beta-lactam antibiotics, including the latest cephalosporins and carbapenems, and no clinically useful MBL inhibitor exists. The B1 subclass — NDM, VIM and IMP types — is the most clinically relevant, and VIM-2, first described in Pseudomonas aeruginosa, is among the most widely disseminated: VIM-type enzymes are prevalent in India and across Asia, and NDM- and VIM-producing Enterobacterales are a documented and growing problem in Pakistan, where carbapenem resistance limits therapeutic options. A November 2026 review in ACS Infectious Diseases (PMID 43023851) audited exactly why computational prediction keeps failing on B1 MBL inhibitor discovery — the pitfalls this paper tests one by one. The clinical stakes are set by the newest boronate inhibitors: taniborbactam inhibits VIM-2 with a Ki of 0.02 µM and NDM-1 with 0.08 µM (Le Terrier et al. 2024), and cefepime-taniborbactam has shown efficacy in complicated urinary tract infection, but taniborbactam does not inhibit IMP-type enzymes, where xeruborbactam is the current hope — and IMP variants resistant even to xeruborbactam are already reported (Antimicrob Agents Chemother 2025;69:e00297-25).

Captopril, the antihypertensive ACE inhibitor, is the cleanest test case in this field. Its thiol chelates the two active-site zinc ions, and its four stereoisomers inhibit VIM-2 across a 76-fold range in a single assay (Brem et al. 2016): D-captopril 0.072 µM, L-captopril 4.4 µM, epi-D- and epi-L-captopril 5.5 µM each. The crystal structures show why: D-captopril's carboxylate forms an electrostatic interaction with the conserved Arg228 at 2.9 angstrom, while L-captopril's carboxylate points away from Arg228 and interacts with Asn233 instead, and the L3 loop closes differently around the two. The binding modes are visibly different; the question is whether a docking score can see the difference. A screen that cannot distinguish stereoisomers cannot rank MBL inhibitors at all, because stereochemistry is where the potency lives in this chemotype.

**Hypothesis (falsifiable):** under one standardised protocol on the D-captopril co-crystal structure, docking rank will track the measured VIM-2 ranking (D first, the epi-isomers last), with D-captopril separated from L-captopril by more than Vina noise. Falsified if all four stereoisomers score within 0.1 kcal/mol of each other, in which case rigid docking is confirmed blind to the stereochemistry that defines MBL inhibition.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-15 (web search; PubMed; the daily digest of 2026-11-14, which screened 722 candidates and selected 8 — item 3, the ACS Infectious Diseases audit of computational prediction on B1 MBLs (PMID 43023851), is directly on this topic). Key sources: Brem et al. 2016 (Antimicrob Agents Chemother 60:142–150, PMID 26482303, PMCID PMC4704194) for all measured IC50s, the MIC data and structures 4C1E/4C1D; Le Terrier et al. 2024 (Antimicrob Agents Chemother 68:e00991-23, doi:10.1128/aac.00991-23) for the taniborbactam Ki values; Silwal et al. 2025 (J Inorg Biochem 271:112975, PMID 40513263) for the VIM-20/VIM-31/VIM-15 structures and the D-captopril potency pattern; the 2026 Bioorganic Chemistry review of zinc-binding MBL inhibitors (doi:10.1016/j.bioorg.2026.110576); and Thomas et al. 2020 (J Inorg Biochem 210:111123, PMID 32622213) for the inhibition mechanisms of thiol MBL inhibitors including ANT431. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Pipeline failure and correction

The standard LeadForge pipeline was run with target "Verona integron-encoded metallo-beta-lactamase 2 (VIM-2)" and reference drug taniborbactam (run_docking.py, RDKit venv, NO_PROXY prefix). It failed, and its numbers are DISCARDED (kept in `hidden_files/dock-HP-064-2026-11-15.json` for audit only). The ChEMBL target CHEMBL1255147 returned zero bioactivities, so the only "lead" was the query itself; and the single docking attempt failed because taniborbactam contains boron and Vina's PDBQT parser rejects it ("Atom type B is not a valid AutoDock type"). Boronates cannot be docked by this protocol at all. The pipeline's structure pick, 9CV3, is also wrong for the question: it is VIM-20 (a VIM-2-like variant from Enterobacter cloacae) with L-captopril, not VIM-2 itself.

The correction (documented fallback, HP-027 precedent; script `health-papers-agent/dock_vim2_4c1e_correction.py`) uses structure 4C1E — VIM-2 from Pseudomonas aeruginosa in complex with D-captopril, 1.40 angstrom (Brem et al. 2016) — with the centre from `D._ligand_center`, the centroid of the co-crystallised D-captopril. The centre [75.98, 6.89, 58.12] was audited: the two catalytic zinc ions sit 5.41 and 4.28 angstrom from the centre, with a Zn–Zn distance of 3.71 angstrom, matching the 3.7 angstrom reported on inhibitor binding. The four stereoisomers' SMILES were built by stereocentre inversion from the PubChem-verified L-captopril structure and checked by RDKit CIP assignment — D = (2S,2R), L = (2S,2S), epi-D = (2R,2R), epi-L = (2R,2S) — and each was confirmed against PubChem by isomeric-SMILES lookup (D: CID 447055; L: CID 44093; epi-D: CID 446549; epi-L: CID 688267, "Epicaptopril"). All four share the formula C9H15NO3S.

### 2.3 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; one box (22.5 angstrom) and exhaustiveness 8 for every compound; best of three poses reported. Four compounds on 4C1E: D-captopril (re-dock control on its own structure), L-captopril, epi-D-captopril and epi-L-captopril. Taniborbactam was NOT docked (boron — see Section 2.2) and is carried as the measured reference only: Ki 0.02 µM against VIM-2 (Le Terrier et al. 2024). Measured potencies are all VIM-2 IC50s from Brem et al. 2016 Table 1 (same assay, same paper): D 0.072 µM; L 4.4 µM; epi-D 5.5 µM; epi-L 5.5 µM. A metal-aware caveat applies to every score here: Vina treats the two zinc ions as static point charges and cannot price thiol–zinc coordination, which is the dominant interaction for this chemotype.

### 2.4 PAINS screen

RDKit PAINS filter applied to every compound. All four are PAINS-clean. All four pass Lipinski and Veber outright (MW 217.29, logP 0.92, TPSA 83.90 for each — the stereoisomers share all descriptors except the stereochemistry).

### 2.5 Rank correlation

Spearman rank correlation was computed between the Vina scores and the measured VIM-2 IC50 values for the four stereoisomers (n = 4). The two tied measured values (5.5 µM, twice) and the two tied docking values (−6.19, twice) were assigned average ranks. A correlation on four points is reported as a descriptive check, not as a validated ranking — the paper's real test is the size of the docking span against the size of the potency span.

### 2.6 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol; the entire docking span in this study (0.07 kcal/mol) is thirty times smaller than that. Vina cannot price thiol–zinc coordination or the carboxylate–Arg228 interaction that the crystal structures show distinguishing D- from L-captopril. D-captopril's score is a re-dock on its own co-crystal structure (4C1E). No molecular dynamics, covalent or metal-aware docking, or free-energy refinement was run. No compound was assayed. The MIC data quoted are from Brem et al. 2016 and were not reproduced here.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured VIM-2 IC50 | Vina on 4C1E (kcal/mol) | PAINS |
|---|---|---|---|
| D-captopril (reference) | 0.072 µM | −6.16 (−6.16, −6.06, −5.95) | clean |
| L-captopril | 4.4 µM | −6.19 (−6.19, −6.03, −5.94) | clean |
| epi-D-captopril | 5.5 µM | −6.12 (−6.12, −6.05, −5.95) | clean |
| epi-L-captopril | 5.5 µM | −6.19 (−6.19, −6.06, −5.88) | clean |
| Taniborbactam (measured reference, not docked) | Ki 0.02 µM | — (boron; Vina rejects atom type B) | clean |

Scores in kcal/mol, best of three poses (all three poses in parentheses). Measured IC50s are VIM-2 values from Brem et al. 2016 Table 1; taniborbactam Ki from Le Terrier et al. 2024. "—" means not docked.

The four stereoisomers span 0.07 kcal/mol in docking — D −6.16, L −6.19, epi-D −6.12, epi-L −6.19 — against a 76-fold span in measured potency (0.072 to 5.5 µM). The most potent compound measured (D-captopril) does not even rank first by docking; it ranks third, behind two compounds 61- and 76-fold weaker. The docking span is not merely inside Vina noise: it is thirty times smaller than Vina noise. The screen is not noisy on this question. It is silent.

### 3.2 Rank correlation: none

Against the measured VIM-2 IC50s, Spearman rho is 0.15 (n = 4) — no correlation. The value is meaningless at this sample size, but its direction is not the point; the point is the span. A screening tool that returns the same number for four compounds whose potencies differ 76-fold has no discriminating power on this chemotype, whatever the correlation coefficient.

### 3.3 The crystal structures say what the scores cannot

The difference between D- and L-captopril is visible in the structures and invisible in the scores. In 4C1E (D-captopril, 1.40 angstrom) the carboxylate sits 2.9 angstrom from the conserved Arg228, the residue that binds the beta-lactam substrate carboxylate; in 4C1D (L-captopril, 1.20 angstrom) the carboxylate points away from Arg228 and interacts with Asn233 instead, and the L3 loop closes differently around the hydrophobic face. The thiol bridges both zinc ions in both structures. Vina's scoring function prices none of this: the zinc ions are static charges, the thiol–zinc bond is not a term, and the carboxylate–arginine salt bridge is worth the same in either orientation at this resolution of scoring. The structures are the ground truth here, and they contradict the scores — which is why the paper reports the structures as the finding and the scores as the failure.

### 3.4 The boronate gap

Taniborbactam, the most potent measured inhibitor in the reference set (Ki 0.02 µM, 3.6-fold more potent than D-captopril), cannot be docked by this protocol at all: Vina rejects the boron atom type. The same applies to xeruborbactam and every other boronate in the MBL pipeline. A screening programme built on Vina therefore cannot rank the single most important chemotype in current MBL inhibitor development. That is a tooling limit, not a scientific result, and it is stated here so that no future run silently drops the boronates and reports a ranking of everything else as if it were complete.

### 3.5 ADMET and safety panel

All four stereoisomers share identical descriptors (MW 217.29, logP 0.92, TPSA 83.90) and are PAINS-clean; they differ only in stereochemistry, which is the point. The safety story that matters is not in any panel: captopril is a clinically used antihypertensive, and the concentrations needed for MBL inhibition in vitro exceed the maximum used in treatment — a 2026 repurposing study (FEMS Microbiol Lett 2026;373:fnag064) concluded the repurposing objective could not be achieved for L-captopril on pharmacological grounds, while still reporting that imipenem and meropenem activity was restored for more than 80% and 60% of Enterobacterales strains respectively at 400 mg/L. The stereoisomers are research tools for the binding-mode question, not drug candidates.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say nothing about the relative potency of captopril stereoisomers on VIM-2. It cannot say that D-captopril is the best of the four — the measured record says that, and the screen ranks it third. It cannot say that the epi-isomers are equivalent to L-captopril — the measured record says they are (5.5 vs 4.4 µM), and the screen agrees by accident, returning the same number for all four. A paper that reported "all four stereoisomers dock at −6.1 to −6.2 and are therefore equivalent leads" would be reporting the screen's blindness as a finding. The honest conclusion is narrower and more useful: rigid docking with a static-zinc model has no discriminating power for thiol MBL inhibitors, and any ranking it produces on this chemotype should be discarded.

### 4.2 The metal-aware correction

The correct computational test for this chemotype prices the metal: a metal-aware docking protocol (with zinc coordination restraints or a metal-specific scoring term), or a free-energy comparison that includes the thiol–zinc interaction, or a QM/MM refinement of the docked poses. The crystal structures already exist for D- and L-captopril on VIM-2 (4C1E/4C1D), so the correction can be validated against known binding modes rather than against scores. The assay is the decisive step, because it also answers the question the docking cannot ask: whether the 76-fold gap is driven by the Arg228 interaction, the L3-loop closure, or the zinc geometry — the structures suggest all three, and only a designed experiment separates them.

### 4.3 Why this matters beyond VIM-2

The failure generalises. Any target whose binding is dominated by a metal interaction — MBLs, histone deacetylases, carbonic anhydrases, matrix metalloproteinases — will show the same pattern: a standard rigid-docking screen returning near-identical scores for compounds whose measured potencies differ by orders of magnitude, because the scorer cannot see the interaction that matters. The VIM-2 stereoisomer set is the cleanest demonstration available, because the four compounds are identical in every descriptor except stereochemistry, so there is no confounder to blame. Any screening programme that ranks metal-binding compounds on one Vina scale should first run this control: four stereoisomers, one target, known potencies. If the screen ties them, the screen is not measuring what it claims to measure.

### 4.4 Testable hypotheses

1. **Metal-aware hypothesis.** Re-scoring the same four docked poses with a metal-aware protocol (zinc coordination restraints) restores the measured ranking (D first, epi-isomers last, with D separated from L by more than 1 kcal/mol). Falsified if the metal-aware scores still tie all four within 0.1 kcal/mol — in which case the failure is in pose sampling, not scoring.
2. **Arg228 hypothesis.** A VIM-2 Arg228Ala mutant weakens D-captopril's IC50 by more than 10-fold while weakening L-captopril's by less than 3-fold. Falsified if both weaken equally — in which case the Arg228 interaction is not the driver of the 76-fold gap.
3. **Boronate hypothesis.** A boron-capable docking protocol (e.g. a covalent or boron-parameterised scorer) docks taniborbactam on 4C1E with a score better than D-captopril's −6.16, matching its measured Ki advantage (0.02 vs 0.072 µM). Falsified if taniborbactam still scores worse — in which case the boronate's potency, like the thiol's, is invisible to docking.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain the four captopril stereoisomers and taniborbactam; confirm identity, stereochemistry and purity by LC-MS, NMR and chiral HPLC. Stage 2 (weeks 3–6): IC50 assay on recombinant VIM-2 (nitrocefin hydrolysis), all five compounds on the same plates, in triplicate — the single-assay comparison this paper could not make, and the direct test of the 76-fold gap. Stage 3 (weeks 7–10): metal-aware re-scoring of the docked poses for hypothesis 1, plus the Arg228Ala mutant assay for hypothesis 2. Stage 4 (weeks 11–12): if the metal-aware rescoring restores the ranking, apply it to a small library of thiol MBL inhibitors and synthesise the best two; if it does not, report the negative result and stop. Sample-size logic: three independent biological replicates per IC50 determination is the minimum for a defensible potency claim; the D-versus-L comparison needs the same, because a false "equivalent" call on a 61-fold gap is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. Vina cannot price thiol–zinc coordination or the carboxylate–Arg228 salt bridge; the 0.07 kcal/mol span is the finding, not a defect to be averaged away.
3. D-captopril's score is a re-dock on its own co-crystal structure (4C1E); the other three are cross-docked into a pocket shaped for D-captopril.
4. The measured IC50s come from one paper (Brem et al. 2016) and were not re-measured on one plate here; the 0.072 µM value is at the sensitive end of the nitrocefin assay.
5. Spearman rho is computed on four points with two ties; it is a descriptive check, not a validated ranking.
6. Taniborbactam was not docked (boron); its Ki is quoted from Le Terrier et al. 2024, a different assay from Brem et al. 2016, so the 3.6-fold advantage over D-captopril is cross-assay.
7. No molecular dynamics, metal-aware docking, or free-energy refinement was run — the methods that could actually price the zinc interaction.
8. The 9CV3 (VIM-20) structure was not used; VIM-20 differs from VIM-2 by an active-site-adjacent residue, and the paper does not claim its results transfer to VIM-20.
9. The captopril stereoisomers are research tools, not drug candidates; the concentrations needed for MBL inhibition exceed clinical use.
10. No Pakistan-specific VIM-2 prevalence numbers are cited; the paper's relevance to Pakistan is the resistance context (NDM/VIM-producing Enterobacterales) and the methodological warning for local screening programmes.

## 6. Conclusion

On 4C1E, four captopril stereoisomers dock at −6.16, −6.19, −6.12 and −6.19 kcal/mol — a span of 0.07 kcal/mol, thirty times smaller than Vina noise — while their measured VIM-2 IC50s span 76-fold (0.072 to 5.5 µM), and the most potent measured inhibitor in the reference set, taniborbactam (Ki 0.02 µM), cannot be docked at all because Vina rejects boron. The screen is blind to the stereochemistry that defines MBL inhibition and to the chemotype that defines its future. The next step is the single-assay IC50 comparison in Section 4.5, with metal-aware rescoring of the same poses — and, as a standing rule, no docking screen on a metalloenzyme is trusted until it has passed the stereoisomer control: four stereoisomers, one target, known potencies, and a spread in the scores that matches the spread in the measurements.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Brem J, van Berkel SS, Zollman D, et al. Structural basis of metallo-beta-lactamase inhibition by captopril stereoisomers. Antimicrob Agents Chemother. 2016;60(1):142–150. PMID: 26482303. doi:10.1128/AAC.01335-15.
2. Le Terrier C, Viguier C, Nordmann P, Vila AJ, Poirel L. Relative inhibitory activities of the broad-spectrum beta-lactamase inhibitor taniborbactam against metallo-beta-lactamases. Antimicrob Agents Chemother. 2024;68(2):e00991-23. doi:10.1128/aac.00991-23.
3. Silwal SB, Wamsley B, Wang Z, et al. Mutation of an active site-adjacent residue in VIM indirectly dictates interactions with and blunts inhibition by D-captopril. J Inorg Biochem. 2025;271:112975. PMID: 40513263. doi:10.1016/j.jinorgbio.2025.112975.
4. Why computational predictions fall short in subclass B1 metallo-beta-lactamase inhibitor discovery: progress, pitfalls, and translational opportunities. ACS Infect Dis. 2026 (published 13 November 2026). PMID: 43023851. doi:10.1021/acsinfecdis.6c00608.
5. Structural and mechanistic insights into zinc-binding inhibitors of metallo-beta-lactamases: from boronic acids to peptide mimics for combating carbapenem resistance. Bioorg Chem. 2026 (in press). doi:10.1016/j.bioorg.2026.110576.
6. Thomas CA, et al. Probing the mechanisms of inhibition for various inhibitors of metallo-beta-lactamases VIM-2 and NDM-1. J Inorg Biochem. 2020;210:111123. PMID: 32622213. doi:10.1016/j.jinorgbio.2020.111123.
7. Le Terrier C, et al. The emerging concern of IMP variants being resistant to the only IMP-type metallo-beta-lactamase inhibitor, xeruborbactam. Antimicrob Agents Chemother. 2025;69:e00297-25. doi:10.1128/aac.00297-25.
8. Rodriguez-Avial I, et al. Repurposing insights: experimental and pharmacological approach on L-captopril and dimercaprol as metallo-beta-lactamase inhibitors. FEMS Microbiol Lett. 2026;373:fnag064. doi:10.1093/femsle/fnag064.
9. UniProtKB. Metallo-beta-lactamase VIM-2, Q5U7L7. Accessed 2026-11-15. https://www.uniprot.org/uniprotkb/Q5U7L7/entry
10. RCSB Protein Data Bank. Structures 4C1E (VIM-2 with D-captopril, 1.40 A), 4C1D (VIM-2 with L-captopril, 1.20 A), 9CV3 (VIM-20 with L-captopril, 1.51 A). Accessed 2026-11-15. https://www.rcsb.org/structure/4C1E
11. ChEMBL. Target CHEMBL1255147 (metallo-beta-lactamase) — returned zero bioactivities in the pipeline run; the VIM-2 potencies in this paper are from Brem et al. 2016, not from ChEMBL. Accessed 2026-11-15. https://www.ebi.ac.uk/chembl/
12. PubChem. Captopril, CID 44093; D-captopril, CID 447055; epi-D-captopril, CID 446549; epi-L-captopril (Epicaptopril), CID 688267. Accessed 2026-11-15. https://pubchem.ncbi.nlm.nih.gov/compound/44093

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-064-2026-11-15-4C1E.json` (corrected docking on 4C1E); the discarded pipeline run is in `hidden_files/dock-HP-064-2026-11-15.json` (0 ChEMBL ligands; taniborbactam boron rejected by Vina; structure 9CV3 is VIM-20 — do not use its numbers). The correction script is `health-papers-agent/dock_vim2_4c1e_correction.py`. UniProt accession Q5U7L7, PDB IDs 4C1E/4C1D/9CV3, and the PubChem CIDs for the four stereoisomers are given in the text. No additional data were generated.
