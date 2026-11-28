# A 0.2 nM Diaminopyrimidine Out-Docks Iclaprim on Staphylococcus aureus DHFR by 1.39 kcal/mol — but the Measured Ki Favours Iclaprim

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-28 · **Health Papers Agent — Paper #126** (daily 5-paper run)

**Keywords:** Staphylococcus aureus; MRSA; dihydrofolate reductase; iclaprim; diaminopyrimidine; antimicrobial resistance; molecular docking; ChEMBL; Pakistan

---

## Abstract

Methicillin-resistant Staphylococcus aureus (MRSA) remains a leading drug-resistant pathogen: bacterial antimicrobial resistance caused an estimated 1.27 million deaths directly in 2019, with S. aureus the leading pathogen, and a 2026 meta-analysis of 68 studies put pooled MRSA prevalence among clinical S. aureus isolates in Pakistan at 50% (95% CI 45–54%). Dihydrofolate reductase (DHFR) is a validated antibacterial target, but its most advanced inhibitor, iclaprim, was refused approval by the FDA twice (2009 and 2019) and its development has since been discontinued — leaving no approved DHFR antibiotic for MRSA. We re-screened the target with the standardised LeadForge protocol (UniProtKB P0A017 → ChEMBL target CHEMBL1681620, 48 bioactivities → PubChem → RDKit → PAINS/ADMET → AutoDock Vina 1.2.7 against PDB 2W9H, wild-type S. aureus DHFR in complex with trimethoprim, 1.48 Å) and docked the top five leads plus iclaprim in the same grid. The headline result is a contradiction: CHEMBL1235617, an unnamed ChEMBL diaminopyrimidine with a measured Ki of 0.2 nM against S. aureus DHFR, out-docked iclaprim by 1.39 kcal/mol (−9.38 vs −7.99 kcal/mol, three poses within 0.02 kcal/mol), yet the measured Ki ranks iclaprim first (0.08 nM vs 0.2 nM). Docking and experiment therefore disagree on which molecule is better, and the docking "win" must not be read as a potency claim. The falsifiable next step is a direct enzyme assay: CHEMBL1235617 must show an IC50 against wild-type and F98Y-mutant S. aureus DHFR at or below iclaprim's, with at least 100-fold selectivity over human DHFR, or the docking rank is refuted. Until that assay exists, this paper is a triage signal only — no efficacy, safety or clinical claim follows.

---

## 1. Introduction

Bacterial antimicrobial resistance (AMR) killed an estimated 1.27 million people directly in 2019 and was associated with 4.95 million deaths, with *Staphylococcus aureus* the single leading pathogen (Antimicrobial Resistance Collaborators, *Lancet* 2022). In Pakistan the burden is concentrated: a 2026 systematic review and meta-analysis of 68 studies estimated pooled MRSA prevalence at 50% (95% CI 45–54%) among clinical *S. aureus* isolates, and a South Asia meta-analysis the same year put Pakistan at 37.8% — the lowest in the region, yet still more than one in three isolates. Vancomycin retains ~98% pooled susceptibility in the region, but vancomycin-intermediate and vancomycin-resistant *S. aureus* exist, and vancomycin's nephrotoxicity and slow bactericidal action leave a real gap for a new oral or intravenous anti-MRSA agent.

Dihydrofolate reductase sits at the bottleneck of bacterial folate metabolism: it reduces dihydrofolate to tetrahydrofolate, the one-carbon donor for thymidylate and purine synthesis. Trimethoprim proved the target druggable half a century ago, but trimethoprim resistance — most famously the F98Y active-site mutation — is widespread. Iclaprim, an optimised diaminopyrimidine analogue of trimethoprim discovered at Roche, was the field's best answer: potent against MSSA, MRSA, vancomycin-intermediate and vancomycin-resistant strains, including trimethoprim-resistant isolates, and non-inferior to vancomycin in the two Phase III REVIVE trials of acute bacterial skin and skin-structure infections (pooled analysis, Huang et al. 2018). Yet iclaprim never reached patients: the FDA issued a complete response letter in 2009 (efficacy within the non-inferiority margin and QT-prolongation concerns), a second application was refused in 2019 (additional data on hepatic toxicity requested), and a 2026 review of antibacterial development records its development as discontinued. The target is validated; the molecule is dead. The gap this paper attacks is narrow and concrete: is there a ChEMBL-registered diaminopyrimidine that binds *S. aureus* DHFR at least as tightly as iclaprim, with measured potency already on record, and can docking rank it honestly?

**Falsifiable hypothesis (one sentence):** CHEMBL1235617 inhibits wild-type *S. aureus* DHFR with an IC50 at or below iclaprim's and at least 100-fold selectivity over human DHFR.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-28: PubMed (iclaprim, 93 results; REVIVE trials; iclaprim anti-virulence 2024), RCSB PDB (2W9H, 3FY8), ChEMBL (target CHEMBL1681620, live) and a 2026 review of antibacterial clinical development (*Antibiotics* 2026;15:993). Burden figures are from the Global Burden of Disease AMR analysis (*Lancet* 2022) and the Pakistan MRSA meta-analysis (2026). The Islamic canon sweep (per the programme's standing rule) checked Ibn Sina's *Canon of Medicine* (Book II, materia medica) and Al-Razi's *Kitab al-Judari wa al-Hasba* (On Smallpox and Measles, c. 910) as hypothesis sources for anti-infective leads; neither text contains a DHFR-directed lead, and no Canon-listed plant was docked in this run — the classical literature is cited here for the policy principle (hifz al-nafs, preservation of life), not as evidence for the molecule.

### 2.2 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7, PDB 2W9H (wild-type *S. aureus* DHFR in complex with trimethoprim, 1.48 Å resolution), grid centred on the co-crystallised trimethoprim ligand at [8.96, −5.92, 16.43], 22.5 Å cubic box, exhaustiveness 8, best of three poses reported. The same grid, box and exhaustiveness were used for every compound, including the reference. Ligands came from ChEMBL (CHEMBL1681620 bioactivities, 48 records) and PubChem (iclaprim as QUERY). No structure was invented: 2W9H is an experimental crystal structure, and the F98Y mutant structure (PDB 3FY8, DHFR–NADPH–AR-101 ternary complex) is cited for the resistance discussion but was not docked in this run.

### 2.3 PAINS screen

RDKit PAINS filter applied to every test compound. All five docked compounds are PAINS-clean (zero alerts). A PAINS alert, had one appeared, would have changed the validation design (redox controls); none did.

### 2.4 Honesty limits

Docking is not activity. Vina's scoring error is ±1–2 kcal/mol, which is larger than the 1.39 kcal/mol gap reported here — the "win" sits inside the noise band. No molecular dynamics or free-energy refinement was run. No enzyme assay, MIC, cytotoxicity or animal data exist for CHEMBL1235617 in this paper. Human-DHFR selectivity was not computed and not measured. The measured Ki values quoted are ChEMBL records for the same target (CHEMBL1681620), not new measurements.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Best affinity (kcal/mol) | Top-3 poses (kcal/mol) | Measured Ki vs *S. aureus* DHFR (ChEMBL) | MW | logP | PAINS |
|---|---|---|---|---|---|---|
| CHEMBL1235617 | **−9.38** | −9.38, −9.37, −9.36 | 0.2 nM (pChEMBL 9.70) | 486.58 | 3.98 | none |
| CHEMBL3681399 | −8.55 | −8.55, −8.54, −8.48 | 0.66 nM (pChEMBL 9.18) | 310.36 | 2.27 | none |
| CHEMBL3681411 | −8.11 | −8.11, −8.10, −7.99 | 0.4 nM (pChEMBL 9.40) | 312.33 | 1.06 | none |
| Iclaprim (QUERY, PubChem) | −7.99 | −7.99, −7.89, −7.75 | — | 354.41 | 2.43 | none |
| Iclaprim (CHEMBL134561) | −7.90 | −7.90, −7.86, −7.82 | 0.08 nM (pChEMBL 10.10) | 354.41 | 2.43 | none |

All five compounds pass Lipinski's rule with zero violations. CHEMBL1235617's Tox21 kNN read-across shows low predicted activity across all 12 assays (maximum 0.316, SR-ARE). Its SMILES carries the classic 2,4-diaminopyrimidine warhead shared with trimethoprim and iclaprim, on a distinct scaffold (Tanimoto similarity to iclaprim 0.326).

### 3.2 Comparison with published docking

No published Vina docking of CHEMBL1235617 against *S. aureus* DHFR was found; the compound is unnamed in ChEMBL (no preferred name, no development phase). The reference re-dock is internally consistent: iclaprim docked at −7.99 (PubChem structure) and −7.90 (ChEMBL structure), a 0.09 kcal/mol spread that validates the protocol's reproducibility for this pocket. The 3FY8 structure paper established that iclaprim, AR-101 and AR-102 are competitive inhibitors with respect to dihydrofolate and are significantly more potent than trimethoprim against both wild-type and F98Y-mutant DHFR.

### 3.3 The standardisation problem: thymidine rescue

DHFR inhibitors carry a known in-vivo confounder that has nothing to do with binding: exogenous thymidine rescues bacteria from folate blockade. In a mouse protection model, iclaprim's PD50 was <0.5–1.8 mg/kg against thymidine-kinase-deficient *S. aureus* but 2.2–10.8 mg/kg against wild-type (thymidine-kinase-competent) strains — thymidine in infected tissue antagonises the drug. Any validation assay for CHEMBL1235617 must therefore run in thymidine-free medium and, for animal work, against a thymidine-kinase-deficient strain, or a genuine inhibitor will read as weak. Separately, sub-inhibitory iclaprim suppresses *S. aureus* exotoxin production and improves survival in a *Galleria mellonella* infection model (Hao et al. 2024), an anti-virulence effect that a follow-on molecule should also be tested for — it is a second, cheaper falsifier before any animal work.

## 4. Discussion

### 4.1 The reframe: the docking "win" is a disagreement, not a discovery

The honest reading of the table is that docking and experiment point in opposite directions. Vina ranks CHEMBL1235617 first by 1.39 kcal/mol; the measured Ki ranks iclaprim first by 2.5-fold (0.08 vs 0.2 nM). Both orderings are within their own error bars — Vina's ±1–2 kcal/mol swallows the docking gap, and a 2.5-fold Ki difference is within inter-assay variation. The paper's contribution is therefore not "a better iclaprim" but a precisely stated, cheaply testable question: does the molecule that docks best also inhibit best? The answer costs one enzyme assay, not one drug-development programme.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 1.39 kcal/mol margin is inside Vina noise. Second, CHEMBL1235617 is the largest molecule in the table (MW 486.58, 8 rotatable bonds, TPSA 128.95) — larger ligands systematically score better in Vina because they make more contacts, and its logP of 3.98 is the highest in the set. Third, all four ChEMBL compounds are already sub-nanomolar measured binders; the screen found no molecule that is both novel and dramatically better, only one that docks better. A paper that reported only the −9.38 number would be misleading; the Ki column is the correction.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five compounds are PAINS-clean, so no redox-cycling or aggregation artefact is expected from the structures themselves. The design constraint that does apply is thymidine rescue (§3.3): the validation assay must control thymidine, and the human-DHFR selectivity gate must be measured, not assumed — iclaprim's value rested on bacterial selectivity, and a 486 Da molecule with a diaminopyrimidine warhead has no right to inherit it.

### 4.4 Testable hypotheses

1. CHEMBL1235617 inhibits wild-type *S. aureus* DHFR with IC50 ≤ iclaprim's in the same assay (falsifier: IC50 > 2× iclaprim's).
2. CHEMBL1235617 retains activity against F98Y-mutant DHFR within 10-fold of wild-type (falsifier: >10-fold loss, the trimethoprim pattern).
3. CHEMBL1235617 is ≥100-fold selective for bacterial over human DHFR (falsifier: selectivity <10-fold).
4. CHEMBL1235617 shows an MIC ≤ 1 µg/mL against MRSA ATCC 43300 in thymidine-free medium (falsifier: MIC > 4 µg/mL).
5. At sub-MIC, CHEMBL1235617 suppresses *S. aureus* exotoxin production as iclaprim does (falsifier: no suppression at 0.5× MIC).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): recombinant wild-type and F98Y *S. aureus* DHFR plus human DHFR; spectrophotometric NADPH-oxidation assay; IC50 for CHEMBL1235617, CHEMBL3681399, CHEMBL3681411 and iclaprim in one plate, triplicate, thymidine-free buffer. Stage 2 (weeks 4–6): broth microdilution MICs against MSSA ATCC 29213, MRSA ATCC 43300 and a local clinical MRSA isolate, in standard and thymidine-free medium, with a thymidine-kinase-deficient control strain. Stage 3 (weeks 7–9): exotoxin suppression at sub-MIC (haemolysin/protease readouts) and HepG2 cytotoxicity. Stage 4 (weeks 10–12): *Galleria mellonella* survival at two doses, if stages 1–3 pass. Total compound need is milligrams; the enzyme assay is the only gate that matters for this paper's claim.

## 5. Limitations

1. Docking only: no enzyme, MIC or animal data were generated; the 1.39 kcal/mol margin is inside Vina's ±1–2 kcal/mol noise.
2. Single structure: docking used one wild-type structure (2W9H); the F98Y mutant (3FY8) was not docked, and no MD or free-energy refinement was run.
3. Selectivity unknown: human-DHFR binding was neither computed nor measured — the first safety gate is untested.
4. Measured Ki values are ChEMBL records from different source assays, not head-to-head measurements in one laboratory.
5. The Pakistan burden figure (50% pooled MRSA prevalence) carries very high heterogeneity (I² = 98.9%) and is a meta-analytic summary, not a rate for any single hospital.
6. Islamic-canon sweep: the full 23 volumes of Al-Razi's *Kitab al-Hawi* exist in English only in selections, and Ibn al-Nafis's commentary survives as an Arabic manuscript with only partial English translation; those texts were not read in full. No classical work was used as evidence for the molecule — only for the policy principle.
7. No local-market data: availability and price of the test compounds in Pakistan were not checked.

## 6. Conclusion

CHEMBL1235617 out-docks iclaprim on *S. aureus* DHFR by 1.39 kcal/mol, but the measured Ki favours iclaprim — the two methods disagree, and only a head-to-head enzyme assay can settle which is right. The molecule is a legitimate, cheap, falsifiable next step for a target whose best drug died in regulation, not in the laboratory. Until the assay runs, nothing here is a treatment claim.

## 7. Policy implications

**Decision-maker:** the Drug Regulatory Authority of Pakistan (DRAP) and the National Institute of Health (NIH) AMR surveillance programme, with the provincial health departments. **Decision:** whether to fund a university-lab DHFR inhibitor validation pipeline for MRSA, and whether to add DHFR-inhibitor susceptibility to the national AMR surveillance panel. **Exact change:** DRAP/NIH should commission, within the existing AMR surveillance budget, a 12-week head-to-head enzyme-and-MIC validation of the three ChEMBL leads in this paper against local MRSA isolates, run in thymidine-free conditions, and publish the IC50/MIC table whether positive or negative — instead of waiting for a foreign sponsor to revive a discontinued molecule. **If the evidence reverses this:** if all three leads fail the human-DHFR selectivity gate (selectivity <10-fold), the pipeline should stop and the funds should move to surveillance and stewardship, not to more docking. **Islamic principle:** hifz al-nafs (preservation of life), the first of the five necessities defined by Al-Ghazali in *Al-Mustasfa min 'Ilm al-Usul* (c. 1109) and systematised by Al-Shatibi in *Al-Muwafaqat* — a drug-resistance policy that lets a treatable infection become untreatable fails the preservation of life, and maslaha (public interest) requires the cheap assay to be run before the expensive drug is bought. Al-Razi's *Kitab al-Judari wa al-Hasba* (c. 910), the first clinical distinction of two contagious diseases, is the classical precedent for the method: observe, distinguish, and test — the same discipline this paper asks of DRAP.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the open-data providers — UniProtKB, ChEMBL, PubChem and the RCSB Protein Data Bank — without which this work would not exist.

## References

1. Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399(10325):629–655. doi:10.1016/S0140-6736(21)02724-0. PMID: 35065702.
2. Ali S, Shafiq M, Aziz A, Rahman N, Hasan MA. The prevalence of methicillin-resistant Staphylococcus aureus in clinical settings of Pakistan: a systematic review and meta-analysis. J Epidemiol Glob Health. 2026. doi:10.1007/s44197-026-00587-y.
3. Huang DB, Corey GR, Holland TL, Lodise T, O'Riordan W, Wilcox MH, File TM Jr, Dryden M, Balser B, Desplats E, Torres A. Pooled analysis of the phase 3 REVIVE trials: randomised, double-blind studies to evaluate the safety and efficacy of intravenous iclaprim versus vancomycin for treatment of acute bacterial skin and skin structure infections. Int J Antimicrob Agents. 2018;52(2):233–240. doi:10.1016/j.ijantimicag.2018.05.012. PMID: 29783024.
4. Hao L, Zhou J, Yang H, He C, Shu W, Song H, Liu Q. Anti-virulence potential of iclaprim, a novel folic acid synthesis inhibitor, against Staphylococcus aureus. Appl Microbiol Biotechnol. 2024;108(1):432. doi:10.1007/s00253-024-13268-2. PMID: 39102054.
5. Clinical development of antibacterial drugs: recent progress and future outlook. Antibiotics. 2026;15(10):993. doi:10.3390/antibiotics15100993. (Records iclaprim's development as discontinued after the 2009 and 2019 FDA complete response letters.)
6. RCSB PDB entry 2W9H: wild-type Staphylococcus aureus DHFR in complex with trimethoprim, 1.48 Å. RCSB Protein Data Bank. Accessed 2026-11-28.
7. RCSB PDB entry 3FY8: crystal structure of Staphylococcus aureus DHFR complexed with NADPH and AR-101 (iclaprim enantiomer). RCSB Protein Data Bank. Accessed 2026-11-28.
8. UniProtKB P0A017: dihydrofolate reductase (DfrA), Staphylococcus aureus. UniProt. Accessed 2026-11-28.
9. ChEMBL target CHEMBL1681620: dihydrofolate reductase, Staphylococcus aureus (SINGLE PROTEIN); 48 bioactivities retrieved live 2026-11-28, including Ki values for CHEMBL134561 (iclaprim, 0.08 nM), CHEMBL1235617 (0.2 nM), CHEMBL3681411 (0.4 nM) and CHEMBL3681399 (0.66 nM). ChEMBL, EMBL-EBI.
10. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
11. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)
12. Al-Razi. Kitab al-Judari wa al-Hasba (On Smallpox and Measles). c. 910. (First clinical distinction of two contagious diseases; cited for method precedent only.)
13. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Book II, materia medica, checked as a hypothesis source; no DHFR lead taken from it.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-112-2026-11-28.json` (LeadForge pipeline raw output: UniProtKB P0A017, ChEMBL target CHEMBL1681620, 26 ranked leads, Vina 1.2.7 docking vs PDB 2W9H). Compound identifiers: iclaprim (ChEMBL CHEMBL134561), CHEMBL1235617, CHEMBL3681399, CHEMBL3681411. No additional data were generated.
