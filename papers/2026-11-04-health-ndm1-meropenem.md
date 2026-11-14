# Five Triazole-Thioether NDM-1 Inhibitors Docked With the Catalytic Zinc Retained: The Best Compound Is Found, the Ranking Is Not

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-04 · **Health Papers Agent — Paper #8** (daily 5-paper run)

**Keywords:** NDM-1; metallo-beta-lactamase; carbapenem resistance; meropenem; molecular docking; AutoDock Vina; zinc; Klebsiella pneumoniae

---

## Abstract

New Delhi metallo-beta-lactamase 1 (NDM-1) hydrolyses nearly all beta-lactams including carbapenems, and there is still no FDA-approved inhibitor that targets metallo-beta-lactamases. In Karachi, blaNDM was found in 63.5% of carbapenem-resistant isolates from catheter-associated urinary infections, and NDM-5/NDM-1 dominate carbapenem-resistant Klebsiella pneumoniae. We asked whether standardised docking could rank five known NDM-1 inhibitors against meropenem, the failing substrate, and whether retaining the catalytic zinc ions changes the answer. Compounds came from ChEMBL bioactivities against NDM-1 (CHEMBL1667695), were screened with RDKit (Lipinski/Veber/PAINS) and a Tox21 kNN panel, and were docked with AutoDock Vina 1.2.7 into NDM-1 (PDB 5XP6, 0.95 Å) under an identical protocol, twice: once with the standard metal-free receptor preparation, and once with the two catalytic Zn2+ ions retained (charge +2.00). The pipeline's first automated grid centre was wrong — it centred on succinic acid, a crystallisation additive, rather than the di-zinc active site. With zinc retained, the best measured inhibitor, CHEMBL3809719 (IC50 160 nM), scored best (−8.13 kcal/mol) versus meropenem's −7.59 kcal/mol, a 0.54 kcal/mol margin inside Vina's ±1–2 kcal/mol noise; but the rest of the ranking did not track measurement — CHEMBL3808541 docked second (−7.65 kcal/mol) while measuring worst (980 nM), and meropenem, a substrate the enzyme destroys, docked mid-pack, which docking alone cannot distinguish from inhibition. The boronate positive control, taniborbactam, could not be docked at all: the toolchain rejects the boron atom type. The falsifiable next step is a nitrocefin-hydrolysis NDM-1 inhibition assay for CHEMBL3809719 and CHEMBL3808541 under identical conditions: if the docking order held, CHEMBL3808541 would be near-equipotent to CHEMBL3809719; the measured ChEMBL values predict a 6-fold gap, and the assay would settle which signal to trust.

---

## 1. Introduction

Carbapenem-resistant Enterobacterales are a critical-priority threat, and the New Delhi metallo-beta-lactamase is the carbapenemase that dominates in Pakistan. NDM-1, first identified in 2008 in Klebsiella pneumoniae from a Swedish patient returning from India, is a class B1 metallo-beta-lactamase whose activity depends on one or two bound zinc ions; it hydrolyses penicillins, cephalosporins and carbapenems, sparing only aztreonam among beta-lactams. A 2024–2025 Karachi study of 308 Gram-negative isolates from catheter-associated urinary tract infections found blaNDM in 66 of 104 carbapenem-resistant isolates (63.5%), concentrated in K. pneumoniae (31 of 48 carbapenem-resistant isolates, 64.6%). A genomic survey of 507 K. pneumoniae isolates from Karachi found 42% carbapenem-resistant, with blaNDM-5 in 45.8% and blaNDM-1 in 12.5% of the sequenced resistant isolates. The clinical consequence is stark: colistin was the only antibiotic showing consistent activity in that survey, and even the newest agent, cefiderocol — initially reported as resistant to metallo-beta-lactamase hydrolysis — is efficiently inactivated by NDM-1 and NDM-5.

No beta-lactamase inhibitor approved by the FDA targets metallo-beta-lactamases. The nearest are the bicyclic boronates: taniborbactam, which in the phase III CERTAIN-1 trial (cefepime-taniborbactam vs meropenem for complicated urinary tract infection) showed superiority on the composite of clinical and microbiological success, and xeruborbactam, which retains activity against the taniborbactam-resistant NDM-9 variant (E152K). Aztreonam-avibactam, approved by the FDA in February 2025, works against NDM producers by a different route — aztreonam is not hydrolysed by NDM, and avibactam covers the co-produced serine enzymes. The older metal chelator aspergillomarasmine A inhibits NDM-1 with an IC50 of 4.1 ± 1.0 µM. The field therefore needs new NDM-1 inhibitor chemotypes, and it needs computational screens that can rank them — which is what this paper tests.

The hypothesis is that a standardised Vina protocol, with the catalytic zinc ions retained in the receptor, can rank five known NDM-1 inhibitors against meropenem. The paper reports that the protocol finds the best compound but fails the ranking, and that docking cannot tell a substrate from an inhibitor.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 4 November 2026: the daily literature digest (2026-11-04), PubMed E-utilities (verified PMIDs/DOIs below), and ChEMBL (EBI). Key sources: Kashif et al. for the Karachi blaNDM prevalence; the Karachi CR-KP genomic survey; Warecki et al. for cefiderocol inactivation by NDM-1/NDM-5; Lomovskaya et al. for taniborbactam, xeruborbactam and NDM-9; Wang et al. for the 5XP6 structure's context.

### 2.2 Compound selection (LeadForge pipeline)

The LeadForge pipeline was run live on 4 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target identification used the query "New Delhi metallo-beta-lactamase 1" (UniProt C7C422, metallo-beta-lactamase type 2, Klebsiella pneumoniae); the ChEMBL target was CHEMBL1667695 (single-protein, K. pneumoniae). Bioactivities (pChEMBL ≥ 5) were retrieved; meropenem was verified in PubChem (CID 441130). Compounds passing the similarity screen were ranked by composite score. The top five distinct leads were taken forward. All five are a congeneric series of 1,3,4-triazole thioethers — N-(aryl)-2-[(5-aryl-1H-1,2,4-triazol-3-yl)thio]acetamides — with measured NDM-1 IC50 values of 160–990 nM; none has a preferred name, an approval, or a development phase in ChEMBL. Meropenem is the reference as the failing substrate: it binds the active site and is hydrolysed, which is the gap the inhibitors must close.

### 2.3 Molecular docking

Docking was performed 4 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was NDM-1, PDB 5XP6 (0.95 Å, "native structure of NDM-1 crystallized at pH 5.5"), with the grid centred on the midpoint of the two catalytic zinc ions: [−5.17, −5.37, −16.38]. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

Two corrections to the pipeline's automated handling are documented here. First, the pipeline's automatic grid centre was the centroid of SIN (succinic acid, 8 atoms), a crystallisation additive in 5XP6, at [−5.64, −0.91, −15.44]; the active site is the di-zinc centre, and the grid was re-centred on the Zn–Zn midpoint. The 22.5 Å box meant the first run still covered the active site, but the centre was not the site. Second, the standard receptor preparation drops all HETATM records, which deletes the two catalytic Zn2+ ions — the dominant interaction for NDM-1 inhibitors. All six ligands were therefore docked twice: once metal-free (the pipeline default) and once with both Zn2+ ions retained in the receptor PDBQT (charge +2.00, AutoDock type Zn). The bridging hydroxide (OH 303) was removed on the standard assumption that a ligand displaces it. Only the zinc-retained numbers are reported as the result; the metal-free run is retained for comparison. The boronate positive control taniborbactam (PubChem CID 76902493) could not be docked: meeko writes boron as atom type "B", which Vina rejects ("Atom type B is not a valid AutoDock type"). The toolchain therefore cannot evaluate the most advanced NDM inhibitor chemotype at all — a limitation of the pipeline, stated plainly.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all five leads and meropenem were PAINS-clean. A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead; the highest read-across probabilities were 0.21–0.33 across the five leads, and meropenem's measured panel maximum was 0. No lead carries a toxicity flag that distinguishes it from the reference.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; a single apo crystal structure (5XP6, pH 5.5) was used; the zinc charges (+2.00 each) are a fixed-charge approximation and the bridging hydroxide was assumed displaced, neither of which was validated; the five "leads" are already-known NDM-1 inhibitors, so no novelty of chemistry is claimed; docking cannot distinguish a substrate (meropenem) from an inhibitor; boronate inhibitors cannot be evaluated with this toolchain at all.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Zn-retained (kcal/mol) | Metal-free (kcal/mol) | Poses, Zn-retained | ChEMBL NDM-1 IC50 (nM) | PAINS |
|---|---|---|---|---|---|
| CHEMBL3809719 | **−8.13** | −7.31 | −8.13, −7.99, −7.87 | 160 | clean |
| CHEMBL3808541 | −7.65 | −7.53 | −7.65, −7.43, −7.38 | 980 | clean |
| CHEMBL3810122 | −7.64 | −7.42 | −7.64, −7.63, −7.44 | 450 | clean |
| Meropenem (reference) | −7.59 | −7.24 | −7.59, −7.38, −6.79 | substrate | clean |
| CHEMBL3808678 | −7.42 | −7.36 | −7.42, −7.40, −7.00 | 190 | clean |
| CHEMBL3809445 | −7.23 | −7.15 | −7.23, −7.15, −7.15 | 990 | clean |

All docking on PDB 5XP6 (NDM-1, 0.95 Å), Zn–Zn midpoint [−5.17, −5.37, −16.38], box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 4 November 2026. Meropenem's drug-likeness: MW 383.47, logP −0.31, Lipinski pass. The five leads: MW 324.41–353.45, logP 3.09–3.76, all Lipinski pass, all PAINS-clean. The series differs by single substituents: CHEMBL3809719 carries an ortho-hydroxyphenyl ring; CHEMBL3808541 a para-hydroxyphenyl; CHEMBL3810122 an ortho-aminophenyl; CHEMBL3809445 an ethyl-substituted anilide.

### 3.2 Zinc changes the answer for one compound only

Retaining zinc improved every score, but unevenly: CHEMBL3809719 gained 0.82 kcal/mol (from −7.31 to −8.13) and moved from fourth to first, while the others gained 0.06–0.22 kcal/mol. The thioether sulfur of CHEMBL3809719 presumably coordinates a zinc ion, which the metal-free run could not reward. The zinc-retained ranking puts the best measured inhibitor first — but the rest of the ranking does not track measurement: CHEMBL3808541 docks second (−7.65) while measuring worst (980 nM), and CHEMBL3808678 docks fifth (−7.42) while measuring second-best (190 nM). The measured range (160–990 nM, ~6-fold) is itself narrow, so part of the failure is that there is little ranking to resolve — but a screen that inverts second and worst cannot be trusted to prioritise analogues.

### 3.3 Meropenem docks like an inhibitor

Meropenem scores −7.59 kcal/mol with zinc retained — better than two of the five actual inhibitors. Docking measures binding, not turnover: a substrate that binds well and is hydrolysed looks identical to an inhibitor that binds well and is not. Any NDM-1 docking screen that does not follow up with a hydrolysis assay will therefore promote substrates alongside inhibitors, and the "reference drug" in this paper is a demonstration of that failure mode, not a baseline to beat.

### 3.4 Comparison with published docking

Published NDM-1 inhibitor work is dominated by boronates and chelators, neither of which this toolchain can dock (boron is rejected; chelators' metal binding is not modelled by a fixed-charge Vina run). The triazole-thioether series itself was reported with measured IC50 values in ChEMBL; no published Vina score for these compounds on 5XP6 was found to benchmark against. The zinc-retained Vina value for meropenem on 5XP6 (−7.59 kcal/mol) and for CHEMBL3809719 (−8.13 kcal/mol) are now on record for others to reproduce — with the caveat that the zinc treatment is a fixed-charge approximation.

## 4. Discussion

### 4.1 The reframe

The paper's value is twofold and both parts are negative. First, zinc-retained docking finds the best compound in the set but cannot rank the rest, and cannot distinguish substrate from inhibitor — so it is a filter for "binds the di-zinc site", not a ranking tool. Second, the toolchain cannot dock boronates at all, which excludes taniborbactam and xeruborbactam, the two most advanced NDM inhibitors in existence. A pipeline that cannot evaluate the state of the art cannot be the screen that finds the next one.

### 4.2 Why the "win" must not be over-read

CHEMBL3809719 beats meropenem by 0.54 kcal/mol — inside Vina's noise — and beats the second lead by 0.48 kcal/mol, also inside noise. Its pose consistency is good (−8.13/−7.99/−7.87), which is the strongest point in its favour, and its measured IC50 (160 nM) is the best in the set, which is the second. But the same protocol ranks a 980 nM compound second, so the docking evidence alone would not have selected CHEMBL3809719 with confidence; the measured data do the selecting, and docking merely fails to contradict them for this one compound.

### 4.3 The zinc question is the experiment's design constraint

Fixed +2.00 charges on zinc are a crude model: real zinc coordination involves charge transfer and polarisation that a fixed-charge force field cannot capture, and the bridging hydroxide's displacement was assumed, not shown. The honest reading is that the zinc-retained numbers are better than the metal-free numbers (the metal-free run cannot reward metal coordination at all) but still not quantitative. The validation assay must therefore be enzymatic (nitrocefin hydrolysis), not a better docking run.

### 4.4 Testable hypotheses

1. CHEMBL3809719 inhibits recombinant NDM-1 (nitrocefin assay) with an IC50 within 2-fold of 160 nM, and CHEMBL3808541 with an IC50 within 2-fold of 980 nM — a 6-fold gap that docking predicted as near-equipotent.
2. Meropenem shows no inhibition in the same assay at any concentration (it is a substrate), confirming that its −7.59 kcal/mol docking score is a false positive for inhibition.
3. CHEMBL3809719 restores meropenem susceptibility (MIC reduction ≥4-fold) in an NDM-1-producing K. pneumoniae clinical isolate, with no effect on an isogenic NDM-1-negative strain.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant NDM-1 nitrocefin-hydrolysis inhibition assay for all five leads plus meropenem, same plates, n = 3, with pre-registered IC50 decision rules. Stage 2 (weeks 3–6): checkerboard synergy (meropenem + lead) against NDM-1-producing K. pneumoniae and E. coli clinical isolates, reporting fractional inhibitory concentration indices. Stage 3 (weeks 7–12): the best compound from Stage 2 against a panel of NDM variants (NDM-1, NDM-5, NDM-9) and a human metallo-enzyme counter-screen (e.g. human glyoxalase II or ACE) to test selectivity — a metal chelator that hits human enzymes is not a drug. All compounds are research chemicals, not approved drugs; taniborbactam and xeruborbactam are the clinical benchmarks for any future comparison.

## 5. Limitations

1. Docking only; no experimental data. 2. The best-pose margin (0.54 kcal/mol) is inside Vina's ±1–2 kcal/mol noise. 3. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation was performed. 4. A single apo crystal structure (5XP6, pH 5.5) was used; the enzyme's conformation with a bound inhibitor may differ. 5. Zinc was modelled with fixed +2.00 charges and the bridging hydroxide was assumed displaced — neither validated. 6. Docking cannot distinguish substrate from inhibitor. 7. Boronate inhibitors (taniborbactam, xeruborbactam) cannot be docked with this toolchain. 8. All five leads are already-known NDM-1 inhibitors; no new chemical matter is proposed. 9. No Pakistani-market or clinical data are presented; the Pakistan burden figures are contextual, not part of the result.

## 6. Conclusion

With the catalytic zinc retained, the best measured NDM-1 inhibitor in the set, CHEMBL3809719 (160 nM), docks best (−8.13 kcal/mol), but the ranking below it does not track measurement, meropenem docks like an inhibitor, and the toolchain cannot dock boronates at all. Zinc-retained Vina docking on NDM-1 is a binding filter, not a ranking tool and not a substitute for a hydrolysis assay. The next experiment is a nitrocefin inhibition assay, not more docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Kashif S, Sohail M, Uddin F, Ansari A, Alorabi M, Khan RN, Husain S. Molecular detection and risk factors of carbapenemase-encoding gene among the Gram-negative uropathogens associated with catheter-associated urinary tract infection. *BMC Infect Dis.* 2026. doi:10.1186/s12879-026-14568-w.
2. The microbiological characteristics and genomic surveillance of carbapenem-resistant Klebsiella pneumoniae isolated from clinical samples. *Microorganisms.* 2025;13(7):1577.
3. Warecki BA, Tomatis PE, Mojica MF, et al. Cefiderocol "under siege"? Understanding the rise of NDM-mediated resistance to novel agents. *Chem Sci.* 2025. (PMCID: PMC12152739.)
4. Lomovskaya O, Tsivkovski R, Totrov M, Dressel D, Castanheira M, Dudley M. New boronate drugs and evolving NDM-mediated beta-lactam resistance. *Antimicrob Agents Chemother.* 2023. doi:10.1128/aac.00579-23.
5. Wang R, Lai H, Gao C, et al. Bismuth antimicrobial drugs serve as broad-spectrum metallo-beta-lactamase inhibitors. *Nat Commun.* 2018;9. doi:10.1038/s41467-018-02828-6.
6. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
7. RCSB Protein Data Bank. Native structure of NDM-1 crystallized at pH 5.5. PDB ID 5XP6, 0.95 Å. https://www.rcsb.org/structure/5XP6 (accessed 4 November 2026).
8. ChEMBL database, European Bioinformatics Institute. Target: metallo-beta-lactamase type 2 (CHEMBL1667695); bioactivities accessed 4 November 2026. https://www.ebi.ac.uk/chembl/.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-011-2026-11-04.json` (pipeline run: UniProt C7C422, ChEMBL CHEMBL1667695, 26 ranked leads; metal-free dock on PDB 5XP6 centred on succinic acid) and `hidden_files/dock-HP-011c-2026-11-04.json` (authoritative re-dock: PDB 5XP6, 0.95 Å, Zn–Zn midpoint [−5.17, −5.37, −16.38], two Zn2+ retained at +2.00, Vina 1.2.7; taniborbactam failure recorded with the Vina boron error). ChEMBL IDs: meropenem (query), CHEMBL3808678, CHEMBL3808541, CHEMBL3809719, CHEMBL3810122, CHEMBL3809445. PDB ID 5XP6. No additional data were generated.
