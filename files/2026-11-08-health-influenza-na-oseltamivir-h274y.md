# Oseltamivir Scores Worst on Its Own Wildtype Site — and Better on the Resistant Mutant: A Vina Benchmark on 3TI6 and 3CL0 That Fails to Reproduce H274Y Resistance

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-08 · **Health Papers Agent — Paper #5** (daily 5-paper run)

**Keywords:** influenza; neuraminidase; oseltamivir; H274Y; drug resistance; molecular docking; AutoDock Vina; antiviral

---

## Abstract

Seasonal influenza infects about a billion people a year and causes 290,000–650,000 respiratory deaths, and oseltamivir is the first-line antiviral — yet the H274Y neuraminidase mutation, which swept to more than 90% of seasonal H1N1 in 2008–09, makes the virus resistant to it by shifting the Glu276 side chain into the drug's hydrophobic pocket. We ran the LeadForge pipeline live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina docking) against the 2009 pandemic H1N1 neuraminidase (PDB 3TI6) and its H274Y mutant (PDB 3CL0), docking oseltamivir plus five oseltamivir-scaffold analogues with measured IC50 values of 0.3–1.8 nM, each centred on the co-crystallised oseltamivir, under an identical AutoDock Vina 1.2.7 protocol. The protocol fails the test it was built for: oseltamivir scores worst of all six ligands on the wildtype site (−4.83 kcal/mol), every ligand scores better on the resistant mutant than on the wildtype (oseltamivir −6.48 vs −4.83 kcal/mol), and the docking order disagrees with measured potency on both structures. The falsifiable next step is a neuraminidase inhibition assay of the best-docking analogue against oseltamivir on wildtype and H274Y enzymes, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable advantage; an analogue that inhibits the H274Y enzyme at its ChEMBL IC50 would refute the claim that rigid docking on a drug-bound mutant structure cannot reproduce resistance.

---

## 1. Introduction

Seasonal influenza infects about a billion people every year, including 3–5 million cases of severe illness, and causes 290,000–650,000 respiratory deaths annually, two-thirds of them in people aged 65 and over. Neuraminidase (NA) cleaves sialic acid from host glycans, releasing new virions from infected cells, and it is the target of oseltamivir (Tamiflu), zanamivir and peramivir — the only antivirals that work after infection is established. Oseltamivir phosphate is a prodrug of oseltamivir carboxylate, the active metabolite, which binds the NA active site with sub-nanomolar potency.

Resistance to oseltamivir is dominated by a single mutation, H274Y (histidine to tyrosine at residue 274, N2 numbering; H275Y in N1 numbering). It sits near but not in the drug-binding site, and it works by shifting the carboxylate side chain of Glu276 into the binding pocket, shrinking the hydrophobic pocket that accommodates oseltamivir's pentyloxy group and disrupting the hydrogen-bond network around it — a mechanism established by the crystal structures of Collins et al. (Nature, 2008) and confirmed by molecular-dynamics simulations showing the Glu276 carboxylate rotated by about 115° and the oseltamivir pentyloxy group by about 125°, with water infiltrating the pocket. The mutation first emerged in seasonal H1N1 in 2007–08 and within a year was present in more than 90% of seasonal H1N1 in the USA, Canada, the UK and Australia; the 2009 pandemic H1N1 strain has stayed largely susceptible (under 1.5% resistance), but H274Y remains the resistance mutation that matters most for pandemic preparedness.

The question this paper asks is deliberately narrow and methodological: can a standardised, automated docking pipeline reproduce H274Y resistance — that is, score oseltamivir worse on the mutant than on the wildtype — when both structures are docked with the same protocol? The falsifiable hypothesis is that it cannot, because the mutant structure was crystallised with oseltamivir bound, so its pocket is pre-formed around the drug, and rigid docking will score the mutant as if it were a better binder.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 8 November 2026: the daily literature digest at `~/workspace/research-team/digests/2026-11-08.md` (no influenza item that day), the WHO seasonal-influenza fact sheet, a 2020 review of influenza antiviral resistance (Eur J Clin Microbiol Infect Dis 2020;39:1201–1208), ChEMBL (EBI), RCSB PDB and UniProtKB. Key sources: the WHO fact sheet for burden; the resistance review for the H274Y epidemiology; Collins et al., Nature 2008 for the structural mechanism and the 3CL0 structure; and the 3TI6 structure paper (PLoS Pathog 2011) for the wildtype structure. All ChEMBL potency values quoted were re-checked live against the ChEMBL API on 8 November 2026 for the target "Neuraminidase" (CHEMBL2051, influenza A/Puerto Rico/8/1934 H1N1).

### 2.2 Molecular docking

The LeadForge pipeline was run live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target resolution was verified by hand: UniProt **P03468** (NRAM_I34A1, neuraminidase, influenza A/Puerto Rico/8/1934 H1N1, 454 aa) and ChEMBL target **CHEMBL2051** ("Neuraminidase", SINGLE PROTEIN, influenza A virus A/Puerto Rico/8/1934 H1N1) — both correct, no correction needed.

Docking was performed with AutoDock Vina 1.2.7, using the LeadForge protocol: the same grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand on each structure; best of three poses reported. Two structures were docked. The wildtype is PDB **3TI6**, the 2009 pandemic H1N1 neuraminidase in complex with oseltamivir (ligand code G39), and the grid was centred on the centroid of the co-crystallised G39 copy: **[−48.44, 14.42, 10.08]**. The mutant is PDB **3CL0**, the H274Y neuraminidase in complex with oseltamivir (G39), from Collins et al. (Nature 2008), and the grid was centred on its co-crystallised G39 centroid: **[−31.62, −56.44, 7.78]**. Both centres were verified against the PDB files to 0.01 Å: they are exactly the G39 centroids, and no cofactor or glycan was involved, so the grid-centre fault that has corrupted earlier runs did not occur here. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types, HETATM ligands stripped); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

Six ligands were docked on both structures: oseltamivir itself (QUERY, the ethyl-ester prodrug, PubChem CID 65028) and the top five pipeline-ranked leads, all oseltamivir-scaffold analogues with ChEMBL IC50 values of 0.3–1.8 nM. One of the five (CHEMBL674) is oseltamivir carboxylate — the active metabolite — docked independently as a same-scaffold control; it is reported as such, not as a new lead. The remaining four are a phenethyl analogue (CHEMBL81286), a cyclohexylethyl analogue (CHEMBL315261), a sulfonate analogue in which the carboxylate is replaced by a sulfonate (CHEMBL4440605), and an allyl analogue (CHEMBL311288).

**Correction (fault, found and fixed during this run).** The first docking run was discarded in full: the pipeline's human-preferring target ranking picked ChEMBL CHEMBL1862, the human ABL1 kinase, so all leads were ABL1 inhibitors, and the structure it picked, PDB 1NMB (N9 neuraminidase in complex with a Fab antibody fragment), holds no drug-like ligand, so the `_ligand_center` fallback landed on a Fab glycan (NAG residue 1, chain A). Those scores (oseltamivir −4.88 kcal/mol at a glycan, ABL1 inhibitors ranked above it) are meaningless and are not reported as results; the discarded file is kept for audit. The corrected run forced UniProt P03468 and ChEMBL CHEMBL2051, verified live on 8 November 2026, and docked manually on 3TI6 and 3CL0 as described above.

### 2.3 PAINS screen

Every test compound was screened with the RDKit PAINS filter: oseltamivir and all five leads were PAINS-clean (no alerts). A ToxGuard Tox21 panel was run for each lead; the highest read-across probabilities were 0.10–0.20 (NR-AhR, NR-ER, NR-Aromatase), and no Tox21 panel was returned for oseltamivir itself. These are similarity-based predictions, not measurements, and no lead carries a tox flag that would end it.

### 2.4 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of the co-crystallised G39 pose (RMSD) was performed; the receptor was held rigid, so the Glu276 rotation that causes H274Y resistance is invisible to this protocol by design; only two NA structures (one wildtype, one mutant, both drug-bound) were docked; the leads are already-known NA inhibitors, so no novelty of chemistry is claimed. Antiviral activity in cell culture was not measured for any lead, so a docking win says nothing about clinical benefit. The H274Y numbering used here is N2 numbering, as in Collins et al.; in N1 numbering the same mutation is H275Y.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | NA IC50, ChEMBL | Wildtype 3TI6 (kcal/mol) | Poses, WT | H274Y 3CL0 (kcal/mol) | Poses, H274Y | MW | logP | Lipinski violations | PAINS |
|---|---|---|---|---|---|---|---|---|---|
| CHEMBL81286 (phenethyl analogue) | IC50 0.3 nM | **−6.61** | −6.61, −6.15, −3.81 | **−7.36** | −7.36, −7.09, −7.03 | 360.4 | 2.03 | 0 | clean |
| CHEMBL315261 (cyclohexylethyl analogue) | IC50 1.0 nM | −6.07 | −6.07, −5.68, −5.59 | −6.99 | −6.99, −6.72, −6.61 | 366.5 | 2.76 | 0 | clean |
| CHEMBL4440605 (sulfonate analogue) | IC50 1.8 nM | −5.69 | −5.69, −5.00, −4.96 | −6.96 | −6.96, −6.74, −6.47 | 320.4 | 0.57 | 0 | clean |
| CHEMBL311288 (allyl analogue) | IC50 1.0 nM | −5.67 | −5.67, −5.43, −5.39 | −6.58 | −6.58, −6.54, −6.35 | 296.4 | 0.97 | 0 | clean |
| CHEMBL674 (oseltamivir carboxylate) | IC50 0.65 nM | −5.36 | −5.36, −5.23, −5.04 | −6.77 | −6.77, −6.67, −6.50 | 284.4 | 0.81 | 0 | clean |
| Oseltamivir (reference, prodrug) | — | −4.83 | −4.83, −4.79, −4.54 | −6.48 | −6.48, −6.42, −5.93 | 312.4 | 1.29 | 0 | clean |

All docking on PDB 3TI6 (2009 pandemic H1N1 NA + oseltamivir) and 3CL0 (H274Y NA + oseltamivir), each grid centred on its co-crystallised oseltamivir (G39) centroid, box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 8 November 2026. Potencies are ChEMBL on-target values, re-checked live on 8 November 2026. H274Y is N2 numbering (H275Y in N1 numbering).

The headline, stated honestly: **the protocol fails the test it was built for**. Oseltamivir scores worst of all six ligands on its own wildtype site (−4.83 kcal/mol), trailing the best lead by 1.78 kcal/mol, and every ligand scores better on the resistant mutant than on the wildtype — oseltamivir itself by 1.65 kcal/mol (−6.48 vs −4.83), the phenethyl analogue by 0.75, the cyclohexylethyl analogue by 0.92, the sulfonate analogue by 1.27, the allyl analogue by 0.91 and oseltamivir carboxylate by 1.41 kcal/mol. The ranking is identical on both structures, which is itself suspicious: a resistance mutation that changes the pocket should change the ranking, and it does not. The docking order also disagrees with measured potency on both structures: by IC50 the order is 0.3, 0.65, 1.0, 1.0 and 1.8 nM, but by docking it is 0.3, 1.0, 1.8, 1.0 and 0.65 nM — oseltamivir carboxylate, the second most potent compound in the set, scores fifth on both structures. One internal consistency check does pass: the active carboxylate (CHEMBL674) out-docks the prodrug ester (QUERY) on both structures (−5.36 vs −4.83 wildtype; −6.77 vs −6.48 mutant), as it should, since the carboxylate is the form that binds. Pose consistency does not rescue the ranking: the best lead's wildtype poses span 2.80 kcal/mol (−6.61 to −3.81), the largest pose spread in the set, so its best score is the least stable of the six.

### 3.2 Comparison with published docking

No published Vina score for oseltamivir or any of these analogues on 3TI6 or 3CL0 was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for oseltamivir, its active carboxylate and four analogues on both the wildtype and the H274Y mutant structure are now on record for others to reproduce, together with the centre audit trail and the correction. The ordering is not comparable to published potency: the five leads span measured NA IC50 values of 0.3–1.8 nM, a 6-fold spread, while their docking scores span 1.25 kcal/mol on the wildtype and 0.78 kcal/mol on the mutant, in an order that disagrees with potency on both structures. Vina ranks poses, not IC50s, and on this site it ranks them unreliably — and, uniquely in this series, it ranks the resistant mutant as the better binder for every ligand.

### 3.3 The standardisation / quality problem

Two faults were found and fixed, and one was not a fault but a design limitation. The first fault was the target resolution: the pipeline's human-preferring ranking picked the human ABL1 kinase as the ChEMBL target for a viral neuraminidase query, so the first run's leads were ABL1 inhibitors and its structure (1NMB, an N9 neuraminidase–Fab complex) held no drug-like ligand, so the centre fell on a Fab glycan. That run was discarded in full. The second fault is the same `_ligand_center` fallback that bit the TGR paper: a structure with no drug-like ligand gets an automatic centre on whatever HETATM group survives the exclusions, and here it was a glycan. The fix is a hard rule that a structure with no drug-like ligand gets no automatic centre at all. The design limitation is the interesting one: the mutant structure 3CL0 was crystallised with oseltamivir bound, so its pocket is already in the drug-bound conformation — the Glu276 shift that causes resistance is accommodated in the crystal, and the pocket Vina sees is pre-organised around the drug. Rigid docking on a drug-bound mutant structure cannot reproduce resistance, because the structure has already paid the conformational cost that resistance imposes. The wildtype structure 3TI6 is also drug-bound, but its pocket is the one oseltamivir evolved to fit; the mutant's pocket is the one oseltamivir was forced into. Vina, scoring a rigid pocket, rewards the forced fit.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a negative benchmark with a useful control — and a warning about what docking can and cannot test. There is no lead here: the best-docking analogue (CHEMBL81286, IC50 0.3 nM) is already the most potent measured inhibitor in the set, so its docking "win" adds nothing, and the drug the paper is about scores worst on its own site. The durable findings are the benchmark values for oseltamivir and five analogues on both the wildtype and the H274Y structure (with full pose lists), the demonstration that rigid Vina docking scores every ligand better on the resistant mutant than on the wildtype — the exact opposite of the resistance phenotype — and the same-scaffold control (carboxylate out-docks prodrug on both structures), which shows the protocol is not random, just blind to the mechanism that matters. The more important finding is the design limitation: a resistance mutation whose mechanism is a conformational change cannot be tested by rigid docking on a drug-bound mutant structure, because the crystal has already absorbed the change.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the margins that matter are inside noise: the best lead beats oseltamivir by 1.78 kcal/mol on the wildtype — inside Vina's ±1–2 kcal/mol noise — and the wildtype–mutant differences (0.75–1.65 kcal/mol) are also inside it. Second, the ranking must be checked against measured NA IC50 values — the five leads span 0.3–1.8 nM, and a docking order that puts the second most potent compound fifth on both structures is a measurement of the scoring function, not of the molecules. Third, the resistance test is void by construction: the mutant structure is drug-bound, so the pocket Vina scores is the drug-accommodating conformation, not the apo conformation that resists binding. A docking "win" against oseltamivir on 3TI6 is not a discovery; it is a benchmark value awaiting an assay, and a docking "win" on 3CL0 is not a resistance-breaking lead; it is an artefact of the crystal.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All leads are PAINS-clean, which removes one artefact class from the validation design — but PAINS-clean is a low bar, and the Tox21 panel is thin (highest read-across 0.10–0.20, no panel returned for oseltamivir). The honest reading: nothing in the panel kills any lead, and nothing in it advances one either. The validation assay must still include redox controls and a counter-screen, because a clean PAINS filter does not rule out assay interference, and the NA enzyme assay itself is prone to fluorescence artefacts. The larger safety question — whether an analogue that binds the mutant also inhibits the human sialidases, which share the active-site architecture — is not addressed by PAINS at all and needs a dedicated human-enzyme counter-screen for any lead that advances.

### 4.4 Testable hypotheses

1. The best-docking analogue (CHEMBL81286) inhibits recombinant wildtype N1 neuraminidase with an IC50 within 2-fold of its ChEMBL value (0.3 nM) under identical assay conditions; a measured IC50 worse than oseltamivir carboxylate's would confirm the noise interpretation, while a better one would refute it.
2. A Vina re-dock of the co-crystallised oseltamivir (G39) into 3TI6 reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run) — and the same re-dock into 3CL0 reproduces the mutant pose, showing the protocol can recover a pose it cannot score.
3. A molecular-dynamics simulation of oseltamivir bound to the H274Y apo structure shows the Glu276 shift and water infiltration reported by Collins et al. and by Malaisree et al., while the same simulation on the drug-bound 3CL0 structure does not — directly testing the claim that the crystal has absorbed the resistance mechanism.
4. Docking the same six ligands on the zanamivir-bound N1 structure 3B7E (1918 H1N1 NA) gives a different ranking from 3TI6; a different ranking would show the result is structure-dependent, not molecule-dependent.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): neuraminidase inhibition assay (MUNANA fluorescence) for the best-docking analogue, oseltamivir carboxylate and oseltamivir, on recombinant wildtype N1 and H274Y enzymes, same plate, n = 3, with a pre-registered 2-fold decision rule and the rule that a docking margin under 2 kcal/mol predicts no measurable advantage. Stage 2 (weeks 3–6): the same assay on the H274Y enzyme for any compound that clears Stage 1, plus a human sialidase counter-screen at 10× the NA IC50. Stage 3 (weeks 7–12): cell-culture antiviral assay (MDCK, plaque reduction) for the best compound against wildtype and H274Y virus, with oseltamivir as control, before any claim about resistance-breaking activity. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. Any margin under 2 kcal/mol is inside Vina's ±1–2 kcal/mol noise and cannot be interpreted as a real advantage — the best margin here is 1.78 kcal/mol. 3. The docking order disagrees with measured potency on both structures. 4. Rigid docking on a drug-bound mutant structure cannot reproduce a conformational resistance mechanism — the central test of this paper is void by construction. 5. Only two NA structures (3TI6, 3CL0, both drug-bound) were docked; the apo structures were not scored. 6. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking RMSD validation of the co-crystallised G39 pose was performed. 7. A single rigid receptor was used per structure; the NA active site's flexibility, including the 150-loop, is not modelled. 8. All leads are already-known NA inhibitors, and all are oseltamivir analogues — no new chemotype was tested. 9. The first docking run was discarded in full (wrong target, glycan centre); the correction is documented, but the pipeline faults that caused it are not yet fixed in code. 10. Antiviral activity in cell culture was not measured for any lead.

## 6. Conclusion

Oseltamivir scores worst of all six ligands on its own wildtype neuraminidase site (−4.83 kcal/mol on 3TI6), and every ligand scores better on the resistant H274Y mutant than on the wildtype (oseltamivir −6.48 vs −4.83 kcal/mol on 3CL0) — the exact opposite of the resistance phenotype, because the mutant structure was crystallised with the drug bound and its pocket is pre-organised around it. The honest reading is that on this target, rigid docking cannot test resistance at all — and the next experiment is a head-to-head enzyme assay on wildtype and H274Y neuraminidase with a pre-registered 2 kcal/mol rule, plus a molecular-dynamics simulation of the apo mutant, not more docking on drug-bound crystals.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. World Health Organization. Influenza (seasonal) (fact sheet). Geneva: WHO; updated 28 February 2025. https://www.who.int/news-room/fact-sheets/detail/influenza-(seasonal) (accessed 8 November 2026). (Around a billion cases of seasonal influenza annually, including 3–5 million cases of severe illness; 290,000–650,000 respiratory deaths annually.)
2. Collins PJ, Haire LF, Lin YP, et al. Crystal structures of oseltamivir-resistant influenza virus neuraminidase mutants. *Nature.* 2008;453(7199):1258–1261. PMID: 18480754. DOI: 10.1038/nature06956. (Structure 3CL0; H274Y shifts the Glu276 side chain into the oseltamivir binding pocket.)
3. Vavricka CJ, Li Q, Wu Y, et al. Structural and functional analysis of laninamivir and its octanoate prodrug reveals group-specific mechanisms for influenza neuraminidase inhibition. *PLoS Pathog.* 2011;7(10):e1002249. PMID: 22028647. DOI: 10.1371/journal.ppat.1002249. (Structure 3TI6.)
4. Lampejo T. Influenza and antiviral resistance: an overview. *Eur J Clin Microbiol Infect Dis.* 2020;39(7):1201–1208. DOI: 10.1007/s10096-020-03840-9. (H274Y emerged 2007–08; more than 90% of seasonal H1N1 in 2008–09; pandemic H1N1 under 1.5% resistance.)
5. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
6. RCSB Protein Data Bank. Neuraminidase of 2009 pandemic H1N1 influenza virus in complex with oseltamivir. PDB ID 3TI6. https://www.rcsb.org/structure/3TI6 (accessed 8 November 2026).
7. RCSB Protein Data Bank. H274Y mutant neuraminidase in complex with oseltamivir. PDB ID 3CL0. https://www.rcsb.org/structure/3CL0 (accessed 8 November 2026).
8. UniProtKB. Neuraminidase, influenza A virus (strain A/Puerto Rico/8/1934 H1N1): P03468 (NRAM_I34A1, 454 aa). https://www.uniprot.org/uniprotkb/P03468/entry (accessed 8 November 2026).
9. ChEMBL database, European Bioinformatics Institute. Target: Neuraminidase, influenza A virus (A/Puerto Rico/8/1934(H1N1)) (CHEMBL2051, single protein); bioactivities and compound potencies accessed 8 November 2026. https://www.ebi.ac.uk/chembl/ (Oseltamivir carboxylate: CHEMBL674, IC50 0.65 nM; CHEMBL81286, IC50 0.3 nM; CHEMBL315261, IC50 1.0 nM; CHEMBL311288, IC50 1.0 nM; CHEMBL4440605, IC50 1.8 nM.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-038c-2026-11-08.json` (wildtype 3TI6 and H274Y 3CL0, each centred on its co-crystallised oseltamivir; the first ABL1/glycan-centred run's file `hidden_files/dock-HP-038-2026-11-08.json` is discarded and kept for audit). ChEMBL IDs: CHEMBL81286 (IC50 0.3 nM), CHEMBL674 (oseltamivir carboxylate, IC50 0.65 nM), CHEMBL315261 (IC50 1.0 nM), CHEMBL311288 (IC50 1.0 nM), CHEMBL4440605 (IC50 1.8 nM); oseltamivir (query, PubChem CID 65028). Target: UniProt P03468 (N1 neuraminidase), ChEMBL CHEMBL2051. PDB IDs 3TI6, 3CL0. No additional data were generated.
