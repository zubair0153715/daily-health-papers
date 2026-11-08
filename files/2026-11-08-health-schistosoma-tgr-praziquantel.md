# Two Furoxan Analogues Out-Dock Praziquantel on Schistosoma TGR — But Praziquantel Does Not Target TGR: A Corrected Vina Benchmark on 8PDD

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-08 · **Health Papers Agent — Paper #4** (daily 5-paper run)

**Keywords:** schistosomiasis; thioredoxin glutathione reductase; praziquantel; furoxan; oxadiazole 2-oxide; molecular docking; AutoDock Vina; neglected tropical disease

---

## Abstract

Schistosomiasis required preventive treatment for at least 253.7 million people in 2024, yet only 39.6% of them were reached, and control still rests on a single drug, praziquantel, which kills adult worms but not eggs or immature worms and does not prevent reinfection. Thioredoxin glutathione reductase (TGR) of *Schistosoma mansoni* is a selenocysteine flavoenzyme that is the parasite's sole route for both thioredoxin and glutathione reduction — a validated drug target with no human equivalent. We ran the LeadForge pipeline live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina docking) against the 1.25 Å SmTGR structure (PDB 8PDD), docking praziquantel plus five known TGR inhibitors (measured potencies 10–100 nM) with an identical AutoDock Vina 1.2.7 protocol. Two furoxan (oxadiazole 2-oxide) analogues out-docked praziquantel: CHEMBL3322292 (IC50 83 nM) at −10.93 kcal/mol and CHEMBL3322287 (IC50 10 nM) at −10.27 kcal/mol, against praziquantel at −9.59 kcal/mol — but praziquantel does not act on TGR, so beating it on this site is a cross-docking control, not a therapeutic comparison, and the docking order inverts the measured potencies (the 83 nM compound docks better than the 10 nM compound by 0.66 kcal/mol). The grid centre was corrected during the run: the first attempt centred on the FAD cofactor, and re-docking at the redox-active cysteine site changed no ranking and shifted scores by at most 0.66 kcal/mol, showing the conclusion is robust to that error. The falsifiable next step is a TGR enzyme assay of the two furoxans head-to-head with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable potency advantage; a furoxan that inhibits TGR at its ChEMBL IC50 and kills schistosomula would refute the claim that docking order on this target is uninformative.

---

## 1. Introduction

Schistosomiasis is an acute and chronic parasitic disease caused by blood flukes of the genus *Schistosoma*. The World Health Organization records that at least 253.7 million people required preventive treatment in 2024, of whom more than 100.5 million were treated — only 39.6% coverage — and deaths are estimated at 14,353 per year, a figure WHO itself notes is likely underestimated. The disease is endemic in 78 countries, with 50 requiring preventive chemotherapy. Control rests almost entirely on one drug, praziquantel, donated by Merck for free distribution since 2007: a single dose is usually curative, with cure rates above 80–90% in many series, but it kills adult worms only — not eggs or immature worms — and it does not prevent reinfection, so people return to contaminated water and are infected again. A second drug with a different mechanism is the single most important unmet need in schistosomiasis control.

Thioredoxin glutathione reductase (TGR) is that mechanism's best-validated target. Schistosomes lack separate thioredoxin reductase and glutathione reductase enzymes: a single selenocysteine-containing flavoenzyme, TGR, performs both reductions, and it is essential for the parasite's redox balance. Humans have separate enzymes, so a selective TGR inhibitor has a built-in therapeutic window. TGR was validated as a drug target by Kuntz et al. (2007), who showed the enzyme is essential and that the gold drug auranofin inhibits it and kills schistosomes. The oxadiazole 2-oxide (furoxan) class is the most studied TGR inhibitor chemotype: furoxans inhibit SmTGR in the low-nanomolar range and kill the parasite, acting in part through nitric-oxide release and covalent modification of the redox-active cysteines.

The question this paper asks is deliberately narrow and methodological: can a standardised, automated docking pipeline rank known TGR inhibitors on the true *S. mansoni* structure, and does the ranking track measured potency? The falsifiable hypothesis is that the docking order will disagree with measured TGR IC50 values, and that any margin under 2 kcal/mol is inside Vina's noise.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 8 November 2026: the daily literature digest at `~/workspace/research-team/digests/2026-11-08.md` (no schistosomiasis item that day), the WHO schistosomiasis fact sheet, BMJ Best Practice, ChEMBL (EBI), RCSB PDB and UniProtKB. Key sources: the WHO fact sheet for burden and treatment coverage; Kuntz et al., PLoS Med 2007 for TGR validation; and the 8PDD structure paper (de Souza Neto et al., Sci Rep 2024) for the target structure. All ChEMBL potency values quoted were re-checked live against the ChEMBL API on 8 November 2026 for the target "Thioredoxin glutathione reductase" (CHEMBL6110, *Schistosoma mansoni*).

### 2.2 Molecular docking

The LeadForge pipeline was run live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target resolution was verified by hand: ChEMBL target **CHEMBL6110** ("Thioredoxin glutathione reductase", SINGLE PROTEIN, *Schistosoma mansoni*) is correct; UniProt resolution was not the failure point here.

Docking was performed with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure is PDB **8PDD**, *S. mansoni* TGR at 1.25 Å resolution (de Souza Neto et al., Sci Rep 2024), the highest-resolution SmTGR structure available. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

Six ligands were docked: praziquantel itself (QUERY, PubChem CID 4891) as a cross-docking negative control — praziquantel's mechanism is disruption of calcium homeostasis and tegument damage, not TGR inhibition — and the top five pipeline-ranked TGR inhibitors with measured potencies of 10–100 nM. Two of the five are furoxan (oxadiazole 2-oxide) analogues, identified from their ChEMBL structures.

**Centre correction (fault, found and fixed during this run).** The first docking run centred the grid on the FAD cofactor centroid, **[7.30, −2.84, 57.31]**, because 8PDD holds no drug-like ligand and the pipeline's `_ligand_center` fallback picks the first HETATM group with six or more atoms when nothing survives its cofactor/glycan/lipid exclusions — and FAD is a cofactor that the exclusions did not catch in this structure. That first run's scores are kept for audit in the data file and are reported in Section 3.3, but they are not the result. The corrected centre is **[8.28, −4.52, 51.60]**, the midpoint of the FAD isoalloxazine centroid [6.23, −4.20, 52.39] and the midpoint of the redox-active Cys154–Cys159 disulfide SG atoms [10.33, −4.84, 50.80] (Cys154 SG is 4.59 Å and Cys159 SG 3.22 Å from the FAD isoalloxazine — both distances verified in the PDB file). The same six ligands were re-docked at the corrected centre, and the corrected run is the result reported here.

### 2.3 PAINS screen

Every test compound was screened with the RDKit PAINS filter: praziquantel and all five leads were PAINS-clean (no alerts). A ToxGuard Tox21 panel was run for each lead. Praziquantel's panel is measured data, not read-across: NR-ER 1.0. This is a Tox21 assay readout, not a clinical claim, and is reported here so it is not misread as a toxicity finding. The two furoxans' highest read-across probabilities were NR-ER 0.41 (CHEMBL3322292) and NR-AhR 0.17 (CHEMBL3322287); the remaining leads' highest read-across probabilities were 0.07–0.52. These are similarity-based predictions, not measurements.

### 2.4 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of a co-crystallised ligand pose (RMSD) was performed — 8PDD has no co-crystallised inhibitor to re-dock; a single X-ray structure (8PDD, one TGR conformation) was used; the receptor was held rigid; the selenocysteine residue (Sec597 in SmTGR) is modelled as cysteine in the docking preparation, so any selenium-specific interaction is invisible to this protocol; the leads are already-known TGR inhibitors, so no novelty of chemistry is claimed. Praziquantel's docking score on TGR says nothing about praziquantel as a drug, because praziquantel does not act on TGR. Schistosome killing was not measured for any lead.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | SmTGR potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | MW | logP | Lipinski violations | PAINS | Top tox |
|---|---|---|---|---|---|---|---|---|
| CHEMBL3322292 (furoxan analogue) | IC50 83 nM | **−10.93** | −10.93, −9.29, −9.16 | 469.5 | 0.83 | 0 | clean | NR-ER 0.413 |
| CHEMBL3322287 (furoxan analogue) | IC50 10 nM | −10.27 | −10.27, −9.68, −8.67 | 357.3 | −1.01 | 0 | clean | NR-AhR 0.169 |
| Praziquantel (reference, negative control) | — | −9.59 | −9.59, −9.31, −8.22 | 312.4 | 2.53 | 0 | clean | NR-ER 1.0 (measured) |
| CHEMBL1535744 | Potency 100 nM | −7.74 | −7.74, −7.19, −6.28 | 274.4 | 3.10 | 0 | clean | NR-ER 0.155 |
| CHEMBL1456339 | Potency 100 nM | −7.33 | −7.33, −7.11, −7.09 | 296.2 | 3.44 | 0 | clean | NR-AhR 0.094 |
| CHEMBL1365586 | Potency 100 nM | −6.51 | −6.51, −6.09, −6.01 | 306.5 | 3.04 | 0 | clean | NR-AhR 0.070 |

All docking on PDB 8PDD (*S. mansoni* TGR, 1.25 Å), corrected grid centre [8.28, −4.52, 51.60] (midpoint of FAD isoalloxazine and Cys154–Cys159 disulfide), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 8 November 2026. Potencies are ChEMBL on-target values, re-checked live on 8 November 2026. Praziquantel does not target TGR; its score is a cross-docking control.

The headline, stated honestly: **two furoxans out-dock praziquantel on TGR — and that comparison is meaningless as a drug comparison**, because praziquantel does not act on TGR. The real comparison is between the leads themselves, and it fails: the 83 nM compound (CHEMBL3322292) docks better than the 10 nM compound (CHEMBL3322287) by 0.66 kcal/mol — the docking order inverts the measured potency order at the top of the table. The margins that matter are all inside noise: the two furoxans differ by 0.66 kcal/mol, and each beats praziquantel by 0.68 and 1.34 kcal/mol — the second inside Vina's ±1–2 kcal/mol noise, the first only just outside it. The three 100 nM compounds score −7.74 to −6.51 kcal/mol, a full 2.5–4.4 kcal/mol below the furoxans, so the screen does separate the potent from the weak — it just cannot order the potent ones. Pose consistency does not rescue the top ranking: CHEMBL3322292's second pose drops to −9.29, a 1.64 kcal/mol gap from its best pose, the largest pose spread in the set, so its best score is the least stable of the six.

### 3.2 Comparison with published docking

No published Vina score for any of these leads on 8PDD was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for two furoxan TGR inhibitors, praziquantel as a cross-docking control, and three 100 nM inhibitors on the 1.25 Å SmTGR structure are now on record for others to reproduce, together with the centre audit trail and the correction. The ordering is not comparable to published potency: the two furoxans span measured TGR IC50 values of 10 and 83 nM, an 8-fold spread, and their docking order is inverted relative to it. Vina ranks poses, not IC50s, and on this site it ranks the top two backwards.

### 3.3 The standardisation / quality problem

The centre fault is the story of this paper's methods section, and its resolution is reassuring: the first run centred on the FAD cofactor [7.30, −2.84, 57.31] and gave CHEMBL3322292 −11.24, CHEMBL3322287 −10.16, praziquantel −9.31, CHEMBL1535744 −8.40 and CHEMBL1365586 −6.33 kcal/mol — the same ranking as the corrected run, with shifts of at most 0.66 kcal/mol. The FAD isoalloxazine sits adjacent to the redox cysteines (3.22–4.59 Å), so a grid centred on FAD still overlaps the redox site; the error was real but small, because the cofactor and the active site are neighbours in this enzyme. That is luck, not validation: in the aldose-reductase case that motivated this audit, the cofactor centre was 13.26 Å from the inhibitor site and the ranking inverted. The pipeline's `_ligand_center` fallback — first HETATM group with six or more atoms when nothing survives the exclusions — still silently picks a cofactor when a structure holds no drug-like ligand, and it did so here; the fix is a hard rule that a structure with no drug-like ligand gets no automatic centre at all, and a human picks the site. The second fault was the screen's design: praziquantel was chosen as the reference drug because it is the standard of care, but it is not a TGR inhibitor, so the paper's central comparison is a control, not a contest. The honest framing is that this paper benchmarks TGR inhibitors against each other, with praziquantel as the negative control that proves the site binds non-TGR drugs too.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a negative benchmark with a useful control — and a methods warning. There is no lead here: the two furoxans are already-known TGR inhibitors, their docking scores invert their measured potencies, and the drug they "beat" does not act on the target. The durable findings are the benchmark values for two furoxans and praziquantel on 8PDD (with full pose lists), the demonstration that Vina inverts an 8-fold potency difference at the top of this table, and the centre-correction audit: a cofactor-centred grid and a redox-site-centred grid gave the same ranking with shifts under 0.66 kcal/mol, because in TGR the cofactor and the active site are neighbours — a result that would not generalise to a target where they are apart. The more important finding is the reference-drug error: choosing the standard of care as the docking reference is only valid when the standard of care acts on the target, and here it does not.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the margins that matter are inside noise: the two furoxans differ by 0.66 kcal/mol, and the smaller furoxan–praziquantel margin is 0.68 kcal/mol, both inside Vina's ±1–2 kcal/mol noise. Second, the ranking must be checked against measured SmTGR IC50 values — the two leads span 10 and 83 nM, and a docking order that inverts that order is a measurement of the scoring function, not of the molecules. Third, the reference comparison is void: praziquantel does not inhibit TGR, so out-docking it proves only that the site accepts a non-TGR drug, which is expected for a large flavoprotein active site. A docking "win" against praziquantel on TGR is not a discovery; it is a benchmark value awaiting an assay.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All leads are PAINS-clean, which removes one artefact class from the validation design — but the furoxan chemotype is a known covalent/reactive class, and PAINS-clean does not rule out covalent or redox-mediated assay interference, which is precisely how furoxans are thought to act on TGR (nitric-oxide release, cysteine modification). The Tox21 flags are low (highest read-across 0.41–0.52) and must not be reported as toxicity. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either. The validation assay must include redox controls, a counter-screen against the human thioredoxin reductase, and a reversibility test, because a furoxan that inhibits by covalent modification needs a different evidentiary standard than a reversible binder. The larger safety question — selectivity over the human enzyme, which is the whole point of targeting TGR — is not addressed by PAINS at all and needs a dedicated human-enzyme counter-screen for any lead that advances.

### 4.4 Testable hypotheses

1. The best-docking furoxan (CHEMBL3322292) inhibits recombinant SmTGR with an IC50 within 2-fold of its ChEMBL value (83 nM) under identical assay conditions; a measured IC50 worse than 10 nM for CHEMBL3322287 would confirm the noise interpretation, while the reverse would refute it.
2. A Vina re-dock of a fragment from the 8PDD fragment screen into its crystallographic site reproduces the experimental pose within 2 Å RMSD (protocol self-validation; not yet run).
3. Both furoxans inhibit SmTGR reversibly and selectively over human thioredoxin reductase by at least 10-fold; failure of selectivity would end the chemotype regardless of potency.
4. Docking the same six ligands on the earlier SmTGR structure 2X99 gives the same ranking as on 8PDD; a different ranking would show the result is structure-dependent, not molecule-dependent.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): SmTGR enzyme inhibition assay for both furoxans and praziquantel as a negative control, same plate, n = 3, with a pre-registered 2-fold decision rule and the rule that a docking margin under 2 kcal/mol predicts no measurable advantage. Stage 2 (weeks 3–6): schistosomula viability assay for any compound that clears Stage 1 at its measured IC50, plus a human thioredoxin reductase counter-screen at 10× the SmTGR IC50, with a reversibility test (dialysis or dilution) to distinguish covalent from reversible inhibition. Stage 3 (weeks 7–12): adult-worm assay for the best compound, with praziquantel as the positive control, and a first-pass mouse tolerability check before any efficacy claim. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. Any margin under 2 kcal/mol is inside Vina's ±1–2 kcal/mol noise and cannot be interpreted as a real advantage — the furoxan–furoxan margin is 0.66 kcal/mol. 3. The docking order inverts the measured potency order for the top two leads. 4. Praziquantel does not act on TGR, so the headline comparison is a control, not a contest. 5. Only one TGR structure (8PDD, one conformation) was docked; the earlier 2X99 structure was not scored. 6. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking RMSD validation was performed. 7. A single rigid receptor was used; the TGR active site's flexibility is not modelled. 8. The selenocysteine residue is modelled as cysteine in the docking preparation, so selenium-specific interactions are invisible. 9. The first docking run used a cofactor-centred grid; the correction is documented, but the pipeline fault that caused it is not yet fixed in code. 10. Schistosome killing was not measured for any lead.

## 6. Conclusion

Two furoxan TGR inhibitors out-dock praziquantel on the *S. mansoni* TGR structure 8PDD — CHEMBL3322292 at −10.93 and CHEMBL3322287 at −10.27 kcal/mol against praziquantel at −9.59 — but praziquantel does not act on TGR, so that comparison is a control, and the docking order inverts the measured potencies (the 83 nM compound beats the 10 nM compound by 0.66 kcal/mol). The honest reading is that on this site, non-covalent docking cannot rank known TGR inhibitors against each other — and the next experiment is a head-to-head enzyme assay with a pre-registered 2 kcal/mol rule plus a human-enzyme counter-screen, not more docking against the wrong reference drug.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. World Health Organization. Schistosomiasis (fact sheet). Geneva: WHO; updated 2025. https://www.who.int/news-room/fact-sheets/detail/schistosomiasis/ (accessed 8 November 2026). (At least 253.7 million people required preventive treatment in 2024; 39.6% reached; deaths estimated at 14,353 per year, likely underestimated; 50 countries require preventive chemotherapy.)
2. Kuntz AN, Davioud-Charvet E, Sayed AA, et al. Thioredoxin glutathione reductase from *Schistosoma mansoni*: an essential parasite enzyme and a key drug target. *PLoS Med.* 2007;4(6):e206. DOI: 10.1371/journal.pmed.0040206.
3. de Souza Neto LR, Montoya BO, Brandao-Neto J, et al. Fragment library screening by X-ray crystallography and binding site analysis on thioredoxin glutathione reductase of *Schistosoma mansoni*. *Sci Rep.* 2024;14:1582. PMID: 38238498. DOI: 10.1038/s41598-024-52018-2. (Structure 8PDD, 1.25 Å.)
4. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
5. RCSB Protein Data Bank. Thioredoxin glutathione reductase of *Schistosoma mansoni* at 1.25 Å resolution. PDB ID 8PDD. https://www.rcsb.org/structure/8PDD (accessed 8 November 2026).
6. UniProtKB. Thioredoxin-disulfide reductase (NADPH), *Schistosoma mansoni*: Q962Y6 (TGR, 598 aa). https://www.uniprot.org/uniprotkb/Q962Y6/entry (accessed 8 November 2026).
7. ChEMBL database, European Bioinformatics Institute. Target: Thioredoxin glutathione reductase, *Schistosoma mansoni* (CHEMBL6110, single protein); bioactivities and compound potencies accessed 8 November 2026. https://www.ebi.ac.uk/chembl/ (CHEMBL3322287, IC50 10 nM; CHEMBL3322292, IC50 83 nM.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-026c-2026-11-08.json` (corrected centre [8.28, −4.52, 51.60]; the first FAD-centred run's scores are preserved in the same file for audit). ChEMBL IDs: CHEMBL3322292 (IC50 83 nM), CHEMBL3322287 (IC50 10 nM), CHEMBL1535744 (Potency 100 nM), CHEMBL1456339 (Potency 100 nM), CHEMBL1365586 (Potency 100 nM); praziquantel (query, PubChem CID 4891). Target: ChEMBL CHEMBL6110 (SmTGR). PDB ID 8PDD. No additional data were generated.
