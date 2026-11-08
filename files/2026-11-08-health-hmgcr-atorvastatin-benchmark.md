# No Statin Beats Atorvastatin Beyond Noise: A Vina Benchmark of Four HMG-CoA Reductase Inhibitors on 2R4F, and the Non-Statin Scaffold the Screen Did Not Find

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-08 · **Health Papers Agent — Paper #3** (daily 5-paper run)

**Keywords:** atorvastatin; HMG-CoA reductase; statin intolerance; molecular docking; AutoDock Vina; LDL cholesterol; cardiovascular disease; fluvastatin

---

## Abstract

Cardiovascular disease killed about 19.8 million people in 2022, a third of all deaths, and high LDL cholesterol is one of its main modifiable drivers. Atorvastatin blocks HMG-CoA reductase, the rate-limiting enzyme of cholesterol synthesis, and each 1 mmol/L of LDL lowering cuts major vascular events by about a fifth — but muscle symptoms make some patients stop statins, and the SAMSON trial showed about 90% of those symptoms are also felt on placebo, so true statin intolerance is uncommon (about 3–5%) yet real, and non-statin alternatives are still needed. We ran the LeadForge pipeline live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina docking) against the human HMG-CoA reductase structure in complex with a pyrazole inhibitor (PDB 2R4F), with the grid centred on the co-crystallised inhibitor, and docked atorvastatin plus four known HMG-CoA reductase inhibitors with measured IC50 values of 0.23–1.8 nM, all under an identical AutoDock Vina 1.2.7 protocol. No compound beat atorvastatin beyond noise: atorvastatin scored best at −9.00 kcal/mol, the closest lead (atorvastatin itself in ChEMBL, IC50 0.23 nM) trailed by 0.40 kcal/mol, and the most potent measured inhibitor in the set is atorvastatin itself — every margin inside Vina's ±1–2 kcal/mol noise, and the docking order disagrees with measured potency. The screen also failed its stated purpose: all four leads are statins or statin analogues carrying the same 3,5-dihydroxyheptanoate pharmacophore, so no non-statin scaffold was tested at all. The falsifiable next step is a deliberately dissimilarity-based screen for non-statin HMG-CoA reductase binders plus an LDL-lowering assay of the best-docking lead against atorvastatin, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable advantage; a non-statin lead that lowers LDL in a statin-intolerant model would refute the claim that this target has nothing left to offer beyond statins.

---

## 1. Introduction

Cardiovascular disease (CVD) is the leading cause of death worldwide: the Global Burden of Disease study records about 19.8 million CVD deaths in 2022, 32% of all deaths, 85% of them from heart attack and stroke. In Pakistan, heart disease is reported to cause about 16–18% of all deaths (University of Karachi, 2023). High LDL cholesterol is one of the main modifiable drivers of that burden, and lowering it is one of the best-proven interventions in medicine: the Cholesterol Treatment Trialists' Collaboration meta-analysis of 26 randomised trials showed that each 1 mmol/L reduction in LDL cholesterol cuts major vascular events by about a fifth.

Statins lower LDL by blocking HMG-CoA reductase (HMGCR, 888 amino acids), the rate-limiting enzyme of cholesterol synthesis. Atorvastatin (Lipitor) is the most prescribed statin: it lowers LDL by about 50% at 40–80 mg daily, and its benefit is proportional to the LDL reduction, not to any property of the molecule beyond its potency. The problem is not efficacy but tolerability. Muscle symptoms are the commonest reason patients stop statins, and the SAMSON trial — 60 patients who had stopped atorvastatin because of side effects, cycled through four months each of atorvastatin 20 mg, identical placebo and no tablet — found mean symptom scores of 16.3 on atorvastatin, 15.4 on placebo and 8.0 on no tablet: a nocebo ratio of 0.90, meaning about 90% of the symptoms felt on the drug were also felt on placebo, and 30 of the 60 patients successfully restarted statins afterwards. The International Lipid Expert Panel estimates complete statin intolerance affects only 3–5% of treated patients. But 3–5% of a drug taken by hundreds of millions of people is still millions of people, and for them the alternatives are ezetimibe (about 18–25% LDL reduction), bempedoic acid (which cut major adverse cardiovascular events by 13% in the CLEAR Outcomes trial in statin-intolerant patients) and PCSK9 inhibitors (expensive, injectable). A cheap oral non-statin HMGCR inhibitor would still be valuable.

The question this paper asks is narrower and methodological: can a standardised, automated docking pipeline rank known HMG-CoA reductase inhibitors against atorvastatin on the true human structure, and does the screen actually return the non-statin scaffolds it was asked for? The falsifiable hypothesis is that any lead beating atorvastatin by less than 2 kcal/mol on Vina docking has no measurable potency advantage, and that the docking ranking will disagree with measured HMGCR IC50 values on this target.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 8 November 2026: the daily literature digest at `~/workspace/research-team/digests/2026-11-08.md` (no statin item that day), PubMed and web search, ChEMBL (EBI), RCSB PDB and UniProtKB. Key sources: the Global Burden of Disease 2023 almanac (Mensah et al., J Am Coll Cardiol 2023) for CVD burden; the Cholesterol Treatment Trialists' Collaboration meta-analysis for the LDL benefit; the SAMSON trial (Howard et al., J Am Coll Cardiol 2021) for the nocebo result; the CLEAR Outcomes trial (Nissen et al., N Engl J Med 2023) for bempedoic acid; and the 2R4F structure paper (Pfefferkorn et al., J Med Chem 2008) for the target structure. All ChEMBL potency values quoted were re-checked live against the ChEMBL API on 8 November 2026 for the target "3-hydroxy-3-methylglutaryl-coenzyme A reductase" (CHEMBL402).

### 2.2 Molecular docking

The LeadForge pipeline was run live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target resolution was verified by hand: UniProt **P04035** (HMDH_HUMAN, HMG-CoA reductase, 888 aa) and ChEMBL target **CHEMBL402** ("3-hydroxy-3-methylglutaryl-coenzyme A reductase", SINGLE PROTEIN, Homo sapiens) — both correct, no correction needed.

Docking was performed with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure is PDB **2R4F**, human HMG-CoA reductase in complex with the pyrazole inhibitor PF-3052334 (ligand code RIE), deposited 2007 (Pfefferkorn et al., J Med Chem 2008). The grid was centred on the centroid of the co-crystallised RIE copy on chain A: **[78.03, 9.09, −4.92]**. The centre was verified against the PDB file: it is exactly the RIE centroid, and the structure holds no cofactor, so the grid-centre fault that has corrupted earlier runs (centring on a cofactor or glycan) did not occur here. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types, HETATM ligands stripped); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

Five ligands were docked: atorvastatin itself (QUERY, PubChem CID 60823) and the top four pipeline-ranked leads that could be prepared, all known HMG-CoA reductase inhibitors with ChEMBL IC50 values of 0.23–1.8 nM. Two of the top five leads failed ligand preparation on the first attempt — "RDKit molecule has 2 fragments" — because their ChEMBL SMILES are sodium salts; both were desalted (largest fragment kept, the parent drug) and re-docked at the same centre, and the correction is recorded in the data file. One of the five (CHEMBL1487) is atorvastatin itself as recorded in ChEMBL (IC50 0.23 nM), docked independently as a same-molecule control; it is reported as such, not as a new lead.

### 2.3 PAINS screen

Every test compound was screened with the RDKit PAINS filter: atorvastatin and all four leads were PAINS-clean (no alerts). A ToxGuard Tox21 panel was run for each lead. Atorvastatin's panel is measured data, not read-across: NR-Aromatase 1.0. Fluvastatin's panel is also measured: NR-AhR 1.0 and NR-Aromatase 1.0. These are Tox21 assay readouts, not clinical claims, and are reported here so they are not misread as toxicity findings. The desalted leads' highest read-across probabilities were NR-Aromatase 0.62–0.69, NR-ER up to 0.39 and SR-MMP up to 0.33. These are similarity-based predictions, not measurements.

### 2.4 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of the co-crystallised RIE pose (RMSD) was performed; a single X-ray structure (2R4F, one HMGCR conformation) was used; the receptor was held rigid; the leads are already-known HMG-CoA reductase inhibitors, so no novelty of chemistry is claimed. LDL lowering — the outcome that matters — was not measured for any lead, so a docking win says nothing about clinical benefit. Muscle safety, the problem that motivates the search, was not modelled for any lead.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | HMGCR IC50, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | MW | logP | Lipinski violations | PAINS | Top tox |
|---|---|---|---|---|---|---|---|---|
| Atorvastatin (reference, query) | — | **−9.00** | −9.00, −8.82, −8.11 | 558.6 | 6.31 | 2 | clean | NR-Aromatase 1.0 (measured) |
| CHEMBL1487 (atorvastatin, ChEMBL record) | IC50 0.23 nM | −8.60 | −8.60, −8.28, −7.75 | 558.6 | 6.31 | 2 | clean | NR-Aromatase 1.0 (measured) |
| CHEMBL394937 (statin analogue, desalted) | IC50 1.8 nM | −8.15 | −8.15, −7.63, −7.19 | 580.6 | 1.98 | 1 | clean | NR-Aromatase 0.688 |
| CHEMBL2220442 (fluvastatin) | IC50 0.35 nM | −8.05 | −8.05, −7.67, −7.58 | 411.5 | 4.63 | 0 | clean | NR-AhR 1.0 (measured) |
| CHEMBL161829 (statin analogue, desalted) | IC50 0.57 nM | −7.88 | −7.88, −7.48, −7.26 | 447.5 | 0.09 | 0 | clean | NR-Aromatase 0.617 |

All docking on PDB 2R4F (human HMG-CoA reductase + PF-3052334, chain-A RIE site), grid centre [78.03, 9.09, −4.92] (RIE centroid), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 8 November 2026. All four leads are statins or statin analogues (all carry the 3,5-dihydroxyheptanoate pharmacophore); potencies are ChEMBL on-target values, re-checked live on 8 November 2026.

The headline, stated honestly: **no statin beats atorvastatin beyond noise**. Atorvastatin scores best at −9.00 kcal/mol, the closest lead (atorvastatin itself in ChEMBL) trails by 0.40 kcal/mol, and the furthest by 1.12 kcal/mol — every margin inside Vina's ±1–2 kcal/mol noise. The same molecule docked twice (atorvastatin as QUERY and as its ChEMBL record CHEMBL1487) scores −9.00 and −8.60, a 0.40 kcal/mol spread for an identical compound — which calibrates the protocol's run-to-run jitter on this site, and it is exactly the size of the "win" over the closest lead. The docking order also disagrees with measured potency: by IC50 the order is 0.23, 0.35, 0.57 and 1.8 nM, but by docking it is atorvastatin, then the 0.23 nM record, then the 1.8 nM analogue, then fluvastatin (0.35 nM), then the 0.57 nM analogue. The least potent measured inhibitor in the set (CHEMBL394937, 1.8 nM) scores third at −8.15 kcal/mol, ahead of two more potent compounds. The docking scores span only 1.12 kcal/mol while the measured potencies span 8-fold — Vina compresses the potency range on this site and ranks within it unreliably. Pose consistency does not rescue the ranking: every compound's three poses sit within 0.96 kcal/mol of its best score, so the scores are stable — stably wrong in potency order.

### 3.2 Comparison with published docking

No published Vina score for atorvastatin or any of these leads on 2R4F was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for atorvastatin, fluvastatin and two statin analogues on the human structure are now on record for others to reproduce, together with the centre audit trail and the desalt correction. The ordering is not comparable to published potency: the four leads span measured HMGCR IC50 values of 0.23–1.8 nM, an 8-fold spread, while their docking scores span 1.12 kcal/mol in an order that disagrees with potency — the 1.8 nM compound third, fluvastatin fourth. Vina ranks poses, not IC50s, and on this site it ranks them unreliably.

### 3.3 The standardisation / quality problem

Two things that could silently corrupt this result did not, and one did. The grid centre was verified against the PDB file to 0.01 Å and sits on the co-crystallised RIE inhibitor — the structure holds no cofactor, so the cofactor-centring fault is absent here. The pipeline's target resolution was also correct (P04035 HMGCR; CHEMBL402). What did fail was the screen's stated purpose: the topic asked for non-statin scaffolds for statin-intolerant patients, but the pipeline ranks by similarity to atorvastatin, and the most similar compounds to a statin are other statins. All four leads carry the 3,5-dihydroxyheptanoate pharmacophore — fluvastatin is a marketed statin, and the other three are statin analogues. A similarity screen cannot find a non-statin scaffold, because similarity to the query is the score. The second fault was minor and corrected: two leads' ChEMBL SMILES are sodium salts, which the ligand preparation rejects as two fragments; both were desalted to the parent drug and re-docked, and the salt forms are recorded in the data file so the fix is auditable.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a negative benchmark with a useful control — and a failed screen. There is no lead here: atorvastatin beats every statin in the set on its own site, the closest by 0.40 kcal/mol — inside noise, and the same size as the jitter between two dockings of the identical molecule. The durable findings are the benchmark values for atorvastatin on 2R4F (−9.00 kcal/mol, with full pose lists), the demonstration that Vina compresses an 8-fold potency range into 1.12 kcal/mol and orders it wrong, and the same-molecule control (−9.00 and −8.60 for atorvastatin twice), which calibrates the protocol's own reproducibility on this site at ±0.40 kcal/mol. The more important finding is the screen failure: a similarity-ranked pipeline cannot return non-statin scaffolds, so the clinical question — what to give a statin-intolerant patient — cannot be answered by this pipeline as configured. The next screen must rank by dissimilarity to statins, not similarity to atorvastatin.

### 4.2 Why the "win" must not be over-read

Three reasons. First, any margin under 2 kcal/mol is inside Vina's ±1–2 kcal/mol noise, and the best margin here is 0.40. Second, the ranking must be checked against measured HMGCR IC50 values — the four leads span 0.23–1.8 nM, and a docking order that disagrees with that order is a measurement of the scoring function, not of the molecules. Third, the same-molecule control sets the floor: two dockings of atorvastatin differ by 0.40 kcal/mol, so a 0.40 kcal/mol "win" is indistinguishable from re-docking the reference. A docking "win" against atorvastatin on this site is not a discovery; it is a benchmark value awaiting an assay.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All leads are PAINS-clean, which removes one artefact class from the validation design — but PAINS-clean is a low bar, and the Tox21 flags (NR-Aromatase 1.0 measured for atorvastatin and fluvastatin) are assay readouts, not clinical findings, and must not be reported as toxicity. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either. The validation assay must still include redox controls and a counter-screen, because a clean PAINS filter does not rule out assay interference. The larger safety question — muscle toxicity, the problem that motivates the search — is not addressed by PAINS at all and needs a dedicated muscle-cell model for any lead that advances.

### 4.4 Testable hypotheses

1. The best-docking lead inhibits recombinant human HMG-CoA reductase with an IC50 within 2-fold of its ChEMBL value under identical assay conditions; a measured IC50 worse than atorvastatin's would confirm the noise interpretation, while a better one would refute it.
2. A dissimilarity-ranked screen (Tanimoto < 0.3 to any statin) returns at least one non-statin HMGCR binder with a measured IC50 under 100 nM; failure to find one would show the target's known chemical space is statin-only.
3. A Vina re-dock of the co-crystallised RIE inhibitor into 2R4F reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).
4. Docking the same five ligands on the earlier HMGCR structure 1HWK (atorvastatin complex) gives the same ranking as on 2R4F; a different ranking would show the result is structure-dependent, not molecule-dependent.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): HMG-CoA reductase inhibition assay for the best-docking lead, fluvastatin and atorvastatin, same plate, n = 3, with a pre-registered 2-fold decision rule and the rule that a docking margin under 2 kcal/mol predicts no measurable advantage. Stage 2 (weeks 3–6): a dissimilarity screen of the ChEMBL HMGCR bioactivities for non-statin scaffolds (Tanimoto < 0.3 to atorvastatin, no dihydroxyheptanoate), with the best three docked on 2R4F and assayed as in Stage 1. Stage 3 (weeks 7–12): LDL-uptake assay in HepG2 cells for any compound that clears Stage 2, with atorvastatin as control, plus a muscle-cell toxicity screen, since muscle symptoms are the clinical problem a docking score cannot see. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. Any margin under 2 kcal/mol is inside Vina's ±1–2 kcal/mol noise and cannot be interpreted as a real advantage — the best margin here is 0.40 kcal/mol. 3. Only one HMGCR structure (2R4F, one conformation) was docked; the earlier 1HWK atorvastatin complex was not scored. 4. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking RMSD validation of the co-crystallised RIE pose was performed. 5. A single rigid receptor was used; the HMG-CoA binding pocket's flexibility is not modelled. 6. All leads are already-known HMG-CoA reductase inhibitors, and all are statins — no non-statin scaffold was tested, so the paper cannot speak to the statin-intolerance question it was built around. 7. The same-molecule control (atorvastatin docked twice, −9.00 and −8.60) calibrates run-to-run jitter but was not repeated across days or Vina versions. 8. Muscle safety was not modelled for any lead. 9. LDL lowering was not measured for any lead.

## 6. Conclusion

No statin in this set beats atorvastatin on its own binding site: atorvastatin scores −9.00 kcal/mol on the human HMG-CoA reductase structure 2R4F, every lead trails it by 0.40–1.12 kcal/mol — inside Vina's noise — and the docking order disagrees with measured potency, with the 1.8 nM analogue third and fluvastatin fourth. The honest reading is that on this site, non-covalent docking cannot rank known inhibitors against atorvastatin — and the screen itself failed its purpose, returning only statins, so the next experiment is a dissimilarity-ranked search for a non-statin scaffold plus a head-to-head HMGCR assay with a pre-registered 2 kcal/mol rule, not more similarity docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Mensah GA, Fuster V, Roth GA, et al. A heart-healthy and stroke-free world: using data to inform global action. *J Am Coll Cardiol.* 2023;82(25):2343–2349. DOI: 10.1016/j.jacc.2023.11.003. (Global Burden of Disease: about 19.8 million CVD deaths in 2022, 32% of all deaths, 85% from heart attack and stroke.)
2. Baigent C, Blackwell L, Emberson J, et al. Efficacy and safety of more intensive lowering of LDL cholesterol: a meta-analysis of data from 170,000 participants in 26 randomised trials. *Lancet.* 2010;376(9753):1670–1681. DOI: 10.1016/S0140-6736(10)61350-5. (Each 1 mmol/L LDL reduction cuts major vascular events by about a fifth.)
3. Howard JP, Wood FA, Finegold JA, et al. Side effect patterns in a crossover trial of statin, placebo, and no treatment. *J Am Coll Cardiol.* 2021;78(12):1210–1222. (SAMSON: 60 patients; mean symptom score 16.3 atorvastatin, 15.4 placebo, 8.0 no tablet; nocebo ratio 0.90; 30 of 60 restarted statins.)
4. Nissen SE, Lincoff AM, Brennan D, et al. Bempedoic acid and cardiovascular outcomes in statin-intolerant patients. *N Engl J Med.* 2023;388(15):1358–1369. DOI: 10.1056/NEJMoa2215028. (CLEAR Outcomes: 13% reduction in major adverse cardiovascular events in statin-intolerant patients.)
5. Pfefferkorn JA, Choi C, Larsen SD, et al. Substituted pyrazoles as hepatoselective HMG-CoA reductase inhibitors: discovery of (3R,5R)-7-[2-(4-fluoro-phenyl)-4-isopropyl-5-(4-methyl-benzylcarbamoyl)-2H-pyrazol-3-yl]-3,5-dihydroxyheptanoic acid (PF-3052334) as a candidate for the treatment of hypercholesterolemia. *J Med Chem.* 2008;51(1):31–45. PMID: 18072721. DOI: 10.1021/jm070849r. (Structure 2R4F.)
6. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
7. RCSB Protein Data Bank. Human HMG-CoA reductase in complex with PF-3052334. PDB ID 2R4F. https://www.rcsb.org/structure/2R4F (accessed 8 November 2026).
8. UniProtKB. 3-hydroxy-3-methylglutaryl-coenzyme A reductase, Homo sapiens: P04035 (HMGCR, 888 aa). https://www.uniprot.org/uniprotkb/P04035/entry (accessed 8 November 2026).
9. ChEMBL database, European Bioinformatics Institute. Target: 3-hydroxy-3-methylglutaryl-coenzyme A reductase, Homo sapiens (CHEMBL402, single protein); bioactivities and compound potencies accessed 8 November 2026. https://www.ebi.ac.uk/chembl/ (Atorvastatin: CHEMBL1487, IC50 0.23 nM; fluvastatin: CHEMBL2220442, IC50 0.35 nM.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-010c-2026-11-08.json` (desalted re-dock of CHEMBL161829 and CHEMBL394937 included; original run `hidden_files/dock-HP-010-2026-11-08.json` kept for audit). ChEMBL IDs: atorvastatin (query, PubChem CID 60823; ChEMBL record CHEMBL1487, IC50 0.23 nM), CHEMBL2220442 (fluvastatin, IC50 0.35 nM), CHEMBL161829 (IC50 0.57 nM), CHEMBL394937 (IC50 1.8 nM). Target: UniProt P04035 (HMGCR), ChEMBL CHEMBL402. PDB ID 2R4F. No additional data were generated.
