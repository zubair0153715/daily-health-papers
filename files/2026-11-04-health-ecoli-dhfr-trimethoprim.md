# Five Trimethoprim Analogues Dock Within Noise of Trimethoprim on E. coli DHFR — and None Addresses the dfrA Resistance Route

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-04 · **Health Papers Agent — Paper #7** (daily 5-paper run)

**Keywords:** dihydrofolate reductase; trimethoprim; Escherichia coli; antimicrobial resistance; dfrA; molecular docking; AutoDock Vina; urinary tract infection

---

## Abstract

Trimethoprim has treated urinary tract infection since ~1962 by competitively inhibiting bacterial dihydrofolate reductase (DHFR), but resistance is now common: 30–40% of urinary E. coli isolates worldwide, 64.2% in a 2025 Islamabad study and 72% for trimethoprim-sulfamethoxazole in Dera Ismail Khan, Pakistan. The dominant route is not mutation of the chromosomal folA enzyme but acquisition of a trimethoprim-insensitive DHFR encoded by dfrA (47 alleles). We asked whether standardised docking could rank five known potent E. coli DHFR inhibitors against trimethoprim, and whether any of them plausibly addresses the dfrA route. Compounds came from ChEMBL bioactivities against E. coli DHFR (CHEMBL1809), were screened with RDKit (Lipinski/Veber/PAINS) and a Tox21 kNN panel, and were docked with AutoDock Vina 1.2.7 into E. coli DHFR (PDB 9PWM, 0.89 Å) at the co-crystallised folate centroid, under an identical protocol. The pipeline's first automated grid centre was wrong — it centred on an oxidised-cysteine residue record 12 Å from the folate site, returning meaningless scores of −5.6 to −5.8 kcal/mol; re-centring on folate gave −7.69 to −8.10 kcal/mol. Trimethoprim scored −7.87 kcal/mol; the best lead, CHEMBL278345, scored −8.10 kcal/mol, a 0.23 kcal/mol margin inside Vina's ±1–2 kcal/mol noise, and all five leads are close trimethoprim analogues (measured Ki 0.4–1.0 nM vs trimethoprim IC50 10 nM) that bind the same folA pocket. None was tested against any DfrA enzyme, and dfrA variants share only 38–70% similarity with folA DHFR, so nothing here addresses the clinically dominant resistance route. The falsifiable next step is a paired enzyme assay of CHEMBL278345 against folA DHFR and a representative DfrA enzyme (dfrA1 or dfrA17): activity against folA with no activity against DfrA would confirm that this chemotype cannot solve trimethoprim resistance as it exists in clinics.

---

## 1. Introduction

Urinary tract infection (UTI) is among the most common bacterial infections, and uropathogenic Escherichia coli causes more than 80% of uncomplicated community-acquired cases. Trimethoprim, a 2,4-diaminopyrimidine, competitively inhibits bacterial dihydrofolate reductase (DHFR), blocking the conversion of dihydrofolate to tetrahydrofolate and hence thymidine and DNA synthesis. It has been a UTI mainstay since ~1962, usually combined with sulfamethoxazole as co-trimoxazole. Resistance now limits it severely: a 2025 assessment found trimethoprim resistance in 30–40% of UTI-associated E. coli isolates, with geography and local usage setting the level. In Pakistan the figures are worse — a 2025 study of 150 UTI patients at the Pakistan Institute of Medical Sciences, Islamabad, found trimethoprim resistance of 64.2% among E. coli isolates (co-trimoxazole 47.3%), and a 2022–2024 study from Dera Ismail Khan reported trimethoprim-sulfamethoxazole resistance of 72% (112 of 155 E. coli isolates).

The mechanism matters for drug design. Resistance can arise by folA overexpression or by binding-pocket mutation, but the most common route is horizontal acquisition of dfrA, a plasmid- or integron-encoded trimethoprim-insensitive DHFR. A 2025 study of 278 clinical isolates from the AnTIC and ALTAR trials found 104 isolates (37%) carrying 112 dfrA genes, with eight isolates carrying two copies; allelic replacement showed growth behaviour was allele-specific (dfrA1, dfrA5, dfrA7, dfrA8, dfrA14, dfrA17 tested). The DfrA family now comprises 47 alleles (dfrA1–dfrA48, dfrA2 unused), sharing only 38–70% similarity with each other — a different enzyme family from the chromosomal folA DHFR, not a point mutant of it. Any new DHFR inhibitor that only beats trimethoprim on the folA enzyme therefore answers the wrong question.

The hypothesis of this paper is that five ChEMBL-reported sub-nanomolar E. coli DHFR inhibitors, docked under an identical protocol, will out-score trimethoprim on the folA enzyme — and that the margin, if any, must then be tested against the dfrA route rather than assumed to matter. The paper reports the first half and states the second half as an untested requirement.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 4 November 2026: the daily literature digest (2026-11-04), PubMed E-utilities (verified PMIDs below), and ChEMBL (EBI). Key sources: Spencer et al. for the dfrA allele data and the AnTIC/ALTAR isolate survey; the PIMS Islamabad and Dera Ismail Khan studies for the Pakistan resistance figures; Sawaya and Kraut for the E. coli DHFR structure and mechanism.

### 2.2 Compound selection (LeadForge pipeline)

The LeadForge pipeline was run live on 4 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target identification used the query "folA Escherichia coli" (UniProt P0ABQ4, dihydrofolate reductase, E. coli strain K12, 159 aa); the ChEMBL target was CHEMBL1809 (single-protein, E. coli). Thirty-seven bioactivities (pChEMBL ≥ 5) were retrieved; trimethoprim was verified in PubChem (CID 5578; SMILES COC1=CC(=CC(=C1OC)OC)CC2=CN=C(N=C2N)N). Twenty-five compounds passed the similarity screen and 26 were ranked by composite score. The top five distinct leads were taken forward; the rank-2 entry, CHEMBL22, is trimethoprim itself and is reported as the reference only. All five leads are close trimethoprim analogues (2,4-diaminopyrimidine + substituted benzyl) with measured Ki 0.4–1.0 nM against E. coli DHFR; none has a preferred name, an approval, or a development phase in ChEMBL.

### 2.3 Molecular docking

Docking was performed 4 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was E. coli DHFR, PDB 9PWM (0.89 Å, "Dihydrofolate Reductase Complexed with Folate and Nicotinamide Adenine Dinucleotide Phosphate (Oxidized Form)"), with the grid centred on the centroid of co-crystallised folate (FOL): [−1.29, 3.27, −7.86]. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

The pipeline's automated grid centre was wrong and is documented here because it is part of the result. The auto-picker takes the first drug-like HETATM residue in file order; in 9PWM that is OCS, an oxidised-cysteine residue record (9 atoms) at [−3.89, 15.51, −18.56], roughly 12 Å from the folate site. The first docking run therefore scored all six ligands at −5.60 to −5.81 kcal/mol in the wrong pocket. All six ligands were re-docked at the folate centroid with the same protocol; only the re-dock numbers are reported. The raw JSON of both runs is preserved (see Data availability). No mutant DHFR structure was docked: the topic's mutant angle could not be executed because no trimethoprim-resistant folA mutant structure with a bound ligand was selected under the protocol, and inventing one was not an option. The mutant question is therefore addressed only in the Discussion, as a limitation.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all five leads and trimethoprim were PAINS-clean. A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead; the highest read-across probabilities were 0.12–0.23 across the five leads, and trimethoprim's measured panel maximum was 0. No lead carries a toxicity flag that distinguishes it from the reference drug.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; a single crystal structure (9PWM, closed Met20-loop conformation) was used; the five "leads" are already-known DHFR inhibitors, so no novelty of chemistry is claimed; nothing was tested against any DfrA enzyme, so no claim about clinical trimethoprim resistance is made; the cofactor NADP+ was present in the crystal structure but the docking grid covered the folate site only.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Best affinity (kcal/mol) | Poses (kcal/mol) | ChEMBL Ki (nM) | ChEMBL IC50 (nM) | PAINS |
|---|---|---|---|---|---|
| CHEMBL278345 | **−8.10** | −8.10, −7.76, −7.72 | 0.4 | 3.7 | clean |
| CHEMBL23609 | −8.03 | −8.03, −7.68, −7.01 | 0.5 | 4.0 | clean |
| CHEMBL60069 | −8.03 | −8.03, −7.55, −7.08 | 1.0 | 4.5 | clean |
| CHEMBL23338 | −8.01 | −8.01, −7.50, −7.40 | 0.9 | 3.2 | clean |
| Trimethoprim (reference) | −7.87 | −7.87, −7.83, −6.83 | — | 10.0 | clean |
| CHEMBL31891 | −7.69 | −7.69, −7.62, −6.97 | 0.60 | 2.95 | clean |

All docking on PDB 9PWM (E. coli DHFR, 0.89 Å), folate centroid [−1.29, 3.27, −7.86], box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 4 November 2026. Trimethoprim's drug-likeness: MW 290.32, logP 1.26, Lipinski pass. The five leads: MW 300.36–339.19, logP 1.65–2.28, all Lipinski pass, all PAINS-clean. The structural changes are minimal: CHEMBL23609 replaces one methoxy with ethoxy; CHEMBL60069 with propoxy; CHEMBL278345 with propyl; CHEMBL31891 adds a bromine; CHEMBL23338 adds a propenyl group.

### 3.2 The ranking tracks the measurement — within noise

The docking order (278345 > 23609 = 60069 > 23338 > trimethoprim > 31891) roughly follows the measured Ki order (0.4, 0.5, 1.0, 0.9, —, 0.60 nM) with one inversion: CHEMBL31891 has the second-best measured Ki (0.60 nM) but the worst docking score (−7.69 kcal/mol), consistent with its bromine substituent clashing in the rigid crystal structure. The best margin over trimethoprim is 0.23 kcal/mol — inside Vina's noise. The measured potency differences are equally small: the leads' IC50 values (2.95–4.5 nM) are 2–3-fold better than trimethoprim's 10 nM, a difference no docking protocol can resolve and no clinician would notice.

### 3.3 The standardisation problem, third instance

This is the third paper in this run in which the pipeline's automated structure handling failed silently: Paper #5 picked the wrong protein (EGFR for HER2) and the wrong domain (extracellular for kinase); Paper #6's PDB lookup crashed and its auto-centre would have hit a detergent; here the auto-centre hit a modified-residue record 12 Å from the active site. The pattern is now a finding, not an anecdote: every automated choice in this pipeline — target resolution, PDB selection, grid centring — requires manual verification against the structure's title and ligand records before any number is trusted.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a lead-discovery claim into a resistance-strategy warning. Five close analogues of trimethoprim bind the folA pocket about as well as trimethoprim does, and two to three times more potently by measurement. That is a real but clinically irrelevant improvement if the resistance in the clinic is dfrA-mediated — and in Pakistan, where trimethoprim resistance exceeds 60%, the dfrA route is the one that matters. A better folA binder is a better drug for the 1962 problem, not the 2026 problem.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 0.23 kcal/mol margin is inside Vina's noise. Second, the leads differ from trimethoprim by a single substituent each; they are the same chemotype in the same pocket, so folA binding-pocket mutations would be expected to cross-resist them, and nothing in this study tests that. Third, the DfrA enzymes that actually cause clinical failure were not docked at all — no DfrA structure was in the protocol, and the 38–70% sequence similarity to folA DHFR means folA scores do not transfer.

### 4.3 What would actually address trimethoprim resistance

Two routes, neither taken here. One: a DHFR inhibitor that binds DfrA enzymes — which requires DfrA structures (several are deposited) and a selectivity screen against human DHFR, since the whole point of trimethoprim is bacterial selectivity. Two: a non-DHFR mechanism, such as a folate-pathway combination that bypasses DHFR or a drug that blocks dfrA horizontal transfer. Both are beyond docking against one folA structure, and the paper says so rather than implying otherwise.

### 4.4 Testable hypotheses

1. CHEMBL278345 inhibits recombinant folA DHFR with an IC50 within 2-fold of 3.7 nM under identical assay conditions to trimethoprim's 10 nM (the docking predicts no measurable advantage beyond the known 2–3-fold).
2. CHEMBL278345 shows no measurable inhibition of recombinant DfrA1 or DfrA17 at 10 µM — the concentration at which a clinically useful compound would need to act.
3. A folA binding-pocket mutant (e.g. a Met20-loop or active-site mutant) raises the IC50 of CHEMBL278345 and trimethoprim by a similar factor, confirming cross-resistance within the chemotype.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant folA DHFR inhibition assay (spectrophotometric NADPH oxidation) for CHEMBL278345, CHEMBL23609 and trimethoprim, same plates, n = 3, with a pre-registered 2-fold decision rule. Stage 2 (weeks 3–6): the same assay against recombinant DfrA1 and DfrA17, plus human DHFR as a selectivity control — the stage that decides whether the chemotype is worth pursuing. Stage 3 (weeks 7–12): MIC testing against a panel of clinical UTI E. coli isolates with known dfrA carriage (sensitive, single-dfrA, dual-dfrA) for any compound that clears Stage 2; a compound that fails Stage 2 stops there, and that negative result is itself publishable. All compounds are research chemicals, not approved drugs.

## 5. Limitations

1. Docking only; no experimental data. 2. The best-pose margin (0.23 kcal/mol) is inside Vina's ±1–2 kcal/mol noise. 3. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of folate was performed. 4. A single crystal structure (9PWM, closed Met20-loop conformation) was used; DHFR's loop movements during catalysis are not modelled. 5. No trimethoprim-resistant folA mutant structure was docked. 6. No DfrA enzyme was docked or assayed — the clinically dominant resistance route is entirely untested. 7. All five leads are already-known DHFR inhibitors and close trimethoprim analogues; no new chemical matter is proposed. 8. The pipeline's automated grid centring failed and required manual correction; other silent defaults in the same pipeline are not yet audited.

## 6. Conclusion

Five trimethoprim analogues dock within noise of trimethoprim on E. coli DHFR (best margin 0.23 kcal/mol), and all five are already-known sub-nanomolar inhibitors of the same folA pocket. The durable findings are methodological — automated grid centring failed a third time in this run and must be verified by hand — and strategic: beating trimethoprim on folA does not address dfrA-mediated resistance, which causes most clinical failure. The next experiment is a paired folA/DfrA enzyme assay, not more docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Spencer A, Wong Q, Lawson ST, et al. Trimethoprim resistance in Escherichia coli exhibits an allele-specific growth advantage. *J Med Microbiol.* 2025;74. (PMCID: PMC12452031.)
2. Sawaya MR, Kraut J. Loop and subdomain movements in the mechanism of Escherichia coli dihydrofolate reductase: crystallographic evidence. *Biochemistry.* 1997;36:586–603. PMID: 9012674. doi:10.1021/bi962337c.
3. Wajid U, Wajid A, Waheed U. Antibiotic resistance trends in UTI-causing E. coli. *Int J Nat Med Health Sci.* 2025;4(1):30–37.
4. Bacterial profiling and antibiotic resistance patterns in urinary tract infections: a microbiological analysis from Dera Ismail Khan, Pakistan. *BMC Infect Dis.* 2025. doi:10.1186/s12879-025-11588-w.
5. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
6. RCSB Protein Data Bank. Dihydrofolate reductase complexed with folate and nicotinamide adenine dinucleotide phosphate (oxidized form). PDB ID 9PWM, 0.89 Å. https://www.rcsb.org/structure/9PWM (accessed 4 November 2026).
7. ChEMBL database, European Bioinformatics Institute. Target: dihydrofolate reductase, Escherichia coli (CHEMBL1809); bioactivities accessed 4 November 2026. https://www.ebi.ac.uk/chembl/.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-014-2026-11-04.json` (pipeline run: UniProt P0ABQ4, ChEMBL CHEMBL1809, 26 ranked leads; auto-centred OCS run retained for audit) and `hidden_files/dock-HP-014c-2026-11-04.json` (authoritative re-dock: PDB 9PWM, 0.89 Å, folate centroid [−1.29, 3.27, −7.86], Vina 1.2.7). ChEMBL IDs: trimethoprim (CHEMBL22, query), CHEMBL23609, CHEMBL60069, CHEMBL278345, CHEMBL31891, CHEMBL23338. PDB ID 9PWM. No additional data were generated.
