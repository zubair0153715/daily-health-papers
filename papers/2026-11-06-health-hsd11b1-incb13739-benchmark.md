# INCB13739 Still Leads by 1.05 kcal/mol — Inside the Noise: A Vina Benchmark of 11β-HSD1 Inhibitors on 4C7K and the Wrong-Target Run That Had to Be Discarded

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-06 · **Health Papers Agent — Paper #4** (daily 5-paper run)

**Keywords:** 11beta-HSD1; INCB13739; molecular docking; AutoDock Vina; type 2 diabetes; glucocorticoid; metabolic syndrome; ChEMBL

---

## Abstract

Type 2 diabetes affected about 537 million adults worldwide in 2021, including about 33 million in Pakistan, and intracellular glucocorticoid excess is one of the metabolic drivers that existing therapies do not directly target. The enzyme 11-beta-hydroxysteroid dehydrogenase type 1 (11beta-HSD1) converts inactive cortisone into active cortisol inside liver and adipose tissue, amplifying intracellular glucocorticoid action; its activity is elevated in the adipose tissue of obese rodents and humans and is linked to metabolic syndrome and type 2 diabetes. INCB13739, a selective 11beta-HSD1 inhibitor, showed a positive phase 2 result — 200 mg daily for 12 weeks lowered A1C by 0.6 percent, fasting glucose by 24 mg per decilitre and HOMA-IR by 24 percent versus placebo in 302 patients inadequately controlled on metformin — yet it was never approved, and no 11beta-HSD1 inhibitor has reached approval. We asked whether a standardised automated docking pipeline could rank known sub-nanomolar 11beta-HSD1 inhibitors against INCB13739. The LeadForge pipeline was run live on 6 November 2026; its first target query resolved to the wrong enzyme entirely (AKR1C3, not 11beta-HSD1) and was discarded, and its first structures failed receptor preparation or centred on a detergent molecule. On the corrected target (UniProt P28845, ChEMBL CHEMBL4235, 58 bioactivities) and the corrected centre — the centroid of the co-crystallised inhibitor DZL in PDB 4C7K (1.91 angstrom) — five ligands were docked with AutoDock Vina 1.2.7. INCB13739 scored minus 11.32 kcal per mol; the best lead, CHEMBL3664636 (IC50 0.31 nM), scored minus 10.27 kcal per mol, with the remaining leads at minus 9.69, minus 9.36 and minus 8.55 kcal per mol. INCB13739 still leads on docking by 1.05 kcal per mol, inside Vina's plus-minus 1 to 2 kcal per mol noise, and all four leads are sub-nanomolar by measured IC50, so docking cannot separate them from the reference and the ranking is not a discovery. The falsifiable next step is a head-to-head 11beta-HSD1 enzyme inhibition assay of CHEMBL3664636 versus INCB13739 under identical conditions, with a pre-registered rule that a docking margin under 2 kcal per mol predicts no measurable potency advantage; a measured potency difference larger than two-fold would refute that prediction.

---

## 1. Introduction

Diabetes affected approximately 537 million adults worldwide in 2021, including about 33 million in Pakistan (IDF Diabetes Atlas 2021). Most of that burden is type 2 diabetes, driven by insulin resistance in liver, muscle and adipose tissue. One amplifier of insulin resistance that standard glucose-lowering drugs do not directly target is intracellular glucocorticoid action: the enzyme 11β-hydroxysteroid dehydrogenase type 1 (11β-HSD1) converts inactive cortisone into active cortisol inside liver and adipose tissue, raising local glucocorticoid levels without raising circulating cortisol. Its activity is elevated in the adipose tissue of obese rodents and humans and is linked to metabolic syndrome and type 2 diabetes, which makes selective 11β-HSD1 inhibition a mechanistically attractive target — lower cortisol where it does harm, without adrenal suppression.

INCB13739 is the most clinically advanced selective 11β-HSD1 inhibitor. In its phase 2 trial (Rosenstock et al., Diabetes Care 2010; 302 patients with type 2 diabetes inadequately controlled on metformin, 12 weeks, five doses versus placebo; ClinicalTrials.gov NCT00698230), the 200 mg dose lowered A1C by 0.6%, fasting plasma glucose by 24 mg/dL and HOMA-IR by 24% versus placebo; total cholesterol, LDL cholesterol and triglycerides decreased significantly in hyperlipidaemic patients, and body weight fell by about 1 kg at the highest dose. The drug was well tolerated at all doses. Despite that positive result, INCB13739 was never approved, and to this day there is still no approved 11β-HSD1 inhibitor — a class-wide gap that makes the question of whether any known inhibitor is measurably better than INCB13739 worth asking properly.

The question this paper asks is narrower and methodological: can a standardised, automated docking pipeline rank known 11β-HSD1 inhibitors against INCB13739 on the inhibitor-bound structure, and how large is the pipeline's own error? The falsifiable hypothesis is that four known sub-nanomolar 11β-HSD1 inhibitors, docked under an identical protocol, will score within Vina's noise of INCB13739 — and that any apparent "win" smaller than 2 kcal/mol is not a discovery.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 6 November 2026: the daily literature digest, PubMed and web search (verified references below), ChEMBL (EBI) and RCSB PDB. Key sources: the IDF Diabetes Atlas 2021 for diabetes burden; the Rosenstock et al. phase 2 trial report for INCB13739's clinical effects; and the RCSB entry for PDB 4C7K.

### 2.2 Compound selection (LeadForge pipeline) — and a wrong-target fault caught

The LeadForge pipeline was run live on 6 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Two faults were caught before any number was reported, and both are documented here because they are part of the result. The first target query, "11beta-hydroxysteroid dehydrogenase type 1", resolved in UniProtKB to P42330 — AKR1C3 (aldo-keto reductase family 1 member C3), a different enzyme — and the pipeline docked on PDB 1S1P, the AKR1C3 structure. That whole run was discarded in full; its raw JSON is preserved for audit, and none of its scores is reported here as an 11β-HSD1 result. The run was repeated with the precise gene query "HSD11B1": UniProt P28845 (11-beta-hydroxysteroid dehydrogenase 1, Homo sapiens), ChEMBL CHEMBL4235 (single-protein, human), 58 bioactivities retrieved. INCB13739 was verified in PubChem (MW 467.53). Twenty-five compounds passed the Morgan-fingerprint similarity screen and 26 were ranked by composite score (similarity ×40 + Lipinski ×20 + Veber ×10 + PAINS ×10 + tox ×20). The top four ranked leads were taken forward to docking. All four are known 11β-HSD1 inhibitors with published ChEMBL potencies: CHEMBL3664636 (IC50 0.31 nM), CHEMBL4075869 (IC50 0.5 nM), CHEMBL4101787 (IC50 0.4 nM) and CHEMBL557417 (IC50 0.5 nM). None of the four has a preferred name, an approval, or a development phase in ChEMBL.

### 2.3 Molecular docking

Docking was performed 6 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was human 11β-HSD1, PDB 4C7K (1.91 Å, "11β-hydroxysteroid dehydrogenase type 1 in complex with inhibitor (DZL)"), with the grid centred exactly on the centroid of its co-crystallised ligand DZL, chain A: [−21.30, −6.46, 34.49]. The centre was verified directly against the PDB file: the distance from the grid centre to the DZL chain-A centroid is 0.01 Å. The NADP+ cofactor centroid sits 11.12 Å away, so the centre is not on the cofactor. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

Two further automated-pipeline errors were caught and corrected before reporting, and are documented here because they are part of the result. The pipeline's auto-picked structure 1XU9 (1.55 Å) fails RDKit receptor preparation — "pdb parse failed" — for all five ligands, so no docking on 1XU9 was possible at all. The next candidate, 1XU7, was rejected for the opposite reason: its grid centre lands on a CHAPS detergent molecule (CPS), not on an inhibitor, so a docking run there would have scored the detergent site. Only the third structure, 4C7K, passed both checks — a parseable receptor and a grid centre on a genuine co-crystallised inhibitor — and only the 4C7K numbers are reported. The raw JSON of every run is preserved (see Data availability), so the correction is auditable.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: INCB13739 and all four leads were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probabilities were SR-ARE 0.515 for INCB13739, NR-ER 0.307 for CHEMBL3664636, SR-MMP 0.279 for CHEMBL4075869, NR-Aromatase 0.253 for CHEMBL4101787 and SR-MMP 0.207 for CHEMBL557417. These are similarity-based predictions, not measurements — and the reference drug itself carries the highest flag in the panel, so a flag here does not distinguish a lead from the reference. No lead carries a PAINS alert that would require redox controls in validation.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; a single crystal structure (4C7K, one 11β-HSD1 conformation) was used; the four leads are already-known 11β-HSD1 inhibitors, so no novelty of chemistry is claimed; and no clinical inference can be drawn from docking scores — the phase 2 evidence for INCB13739 comes from the Rosenstock trial, not from this computation.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | 11β-HSD1 potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| INCB13739 (reference) | phase 2, 200 mg: A1C −0.6% | **−11.32** | −11.32, −11.29, −10.83 | clean |
| CHEMBL3664636 | IC50 0.31 nM | −10.27 | −10.27, −9.93, −9.82 | clean |
| CHEMBL4075869 | IC50 0.5 nM | −9.69 | −9.69, −9.68, −8.75 | clean |
| CHEMBL4101787 | IC50 0.4 nM | −9.36 | −9.36, −8.77, −8.65 | clean |
| CHEMBL557417 | IC50 0.5 nM | −8.55 | −8.55, −8.44, −8.33 | clean |

All docking on PDB 4C7K (human 11β-HSD1, 1.91 Å), grid centre [−21.30, −6.46, 34.49] (DZL chain-A centroid, 0.01 Å), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 6 November 2026. INCB13739: MW 467.53, logP 3.44, 0 Lipinski violations. CHEMBL3664636: MW 446.55, logP 5.00, 1 violation. CHEMBL4075869: MW 434.51, logP 5.46, 1 violation. CHEMBL4101787: MW 416.52, logP 5.32, 1 violation. CHEMBL557417: MW 283.42, logP 3.90, 0 violations.

The headline is stated plainly: INCB13739 still leads on docking, by 1.05 kcal/mol over the best lead — and that margin is inside Vina's ±1–2 kcal/mol noise, so it is not a significant lead. The ranking is also not a discovery in the other direction: all four leads are sub-nanomolar by measured IC50 (0.31–0.5 nM, a 1.6-fold spread), while their docking scores span 1.72 kcal/mol in the same order as potency only at the top — CHEMBL3664636 is both the most potent by IC50 and the best-scoring lead, but the remaining three are ranked by docking in the order −9.69, −9.36, −8.55 against IC50s of 0.5, 0.4 and 0.5 nM, which is no ordering at all. Pose consistency does not rescue the ranking either: INCB13739 holds within 0.49 kcal/mol across its three poses and CHEMBL557417 within 0.22, so the poses are stable — the problem is that the scoring function itself cannot separate compounds whose measured potencies differ by less than two-fold. No lead beats INCB13739, and INCB13739 does not beat any lead by a margin this method can defend.

### 3.2 Comparison with published docking

No published Vina score for INCB13739 or any of these leads on 4C7K was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for INCB13739 and four known 11β-HSD1 inhibitors on 4C7K are now on record for others to reproduce, together with the verified grid centre and the documented pipeline faults. The ordering is not comparable to published potency: all four leads are sub-nanomolar inhibitors, yet their docking scores span 1.72 kcal/mol — Vina ranks poses, not IC50s, and here it cannot separate a 0.31 nM inhibitor from a 0.5 nM one.

### 3.3 The standardisation / quality problem

Three automated steps that could silently corrupt this result did corrupt it. The UniProtKB free-text search for "11beta-hydroxysteroid dehydrogenase type 1" returns AKR1C3 first — a different enzyme that also acts on steroids, so the error is easy to miss and the discarded run's scores would have looked plausible. The PDB picker then chose a structure (1XU9) that cannot be prepared at all, and a second structure (1XU7) whose centre is a detergent molecule. The first two are fixed by verification — check the accession, check that the receptor parses, check the co-crystallised ligand is an inhibitor and not a detergent or cofactor. The lesson generalises: a docking pipeline that reports a score without reporting its target accession, its structure's parse status, and the identity of the molecule its grid is centred on is not reporting a result, it is reporting a guess.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a negative benchmark with a useful control. There is no lead here: the reference drug leads by a margin the method cannot defend, and the most potent lead by measured IC50 (CHEMBL3664636, 0.31 nM) is the best-scoring lead by only 1.05 kcal/mol behind the reference. The durable findings are the benchmark values for INCB13739 on 4C7K (−11.32 kcal/mol, with full pose list) and the documented chain of three pipeline faults — wrong target, unparseable structure, detergent-centred grid — each caught by a verification step that any automated run should include. The class context sharpens the point: INCB13739 itself, despite a positive phase 2, was never approved, and no 11β-HSD1 inhibitor has been approved — so the field does not need a compound that docks 1 kcal/mol better than INCB13739; it needs a compound that is measurably more potent, more selective, or better tolerated in the laboratory and the clinic.

### 4.2 Why the "win" must not be over-read

Two reasons. First, the 1.05 kcal/mol margin is smaller than Vina's ±1–2 kcal/mol noise — the same protocol re-run from a different starting conformer could erase it or reverse it. Second, potency and docking score barely agree within the lead set: the measured IC50s span only 1.6-fold (0.31–0.5 nM) while the docking scores span 1.72 kcal/mol, and the three leads at 0.4–0.5 nM are ranked in no potency order. A docking "win" of this size, on compounds this close in measured potency, is noise wearing a ranking's clothes.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five compounds are PAINS-clean, so no redox or aggregation controls are forced by the screen — but PAINS-clean is a low bar, and the Tox21 read-across flags (SR-ARE 0.515 for INCB13739 itself) are predictions from neighbours, not data. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either — least of all because the reference drug flags the same assays. The validation assay should still include a detergent control and a counter-screen against a related dehydrogenase (for example 11β-HSD2, which inactivates cortisol and must not be inhibited), because selectivity, not potency, is where an 11β-HSD1 programme most often fails.

### 4.4 Testable hypotheses

1. CHEMBL3664636 inhibits recombinant human 11β-HSD1 with an IC50 within 2-fold of its ChEMBL value (0.31 nM) under identical assay conditions, and is not more potent than INCB13739 by more than 2-fold — the docking predicts no measurable advantage; a >5-fold advantage would refute the noise interpretation.
2. A Vina re-dock of the co-crystallised ligand DZL into 4C7K reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).
3. Re-running the pipeline with the precise gene query "HSD11B1" and the verified-centre check reproduces the 4C7K scores within 0.5 kcal/mol — a pipeline reproducibility check to be verified, not assumed.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant human 11β-HSD1 enzyme inhibition assay (cortisone-to-cortisol conversion, LC-MS or scintillation readout) for CHEMBL3664636, CHEMBL4075869 and INCB13739, same plate, n = 3, with a pre-registered 2-fold decision rule and a carbenoxolone positive control. Stage 2 (weeks 3–6): selectivity counter-screen against 11β-HSD2 and AKR1C3 for any compound that clears Stage 1 — AKR1C3 is the enzyme the pipeline first mistook for the target, and cross-activity there would be a genuine liability. Stage 3 (weeks 7–12): adipocyte cell-based assay (differentiated 3T3-L1 or human primary adipocytes) measuring intracellular cortisol generation for any compound that clears Stage 2, with INCB13739 as control. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. The 1.05 kcal/mol margin between INCB13739 and the best lead is inside Vina's ±1–2 kcal/mol noise and is not interpretable as a potency difference. 3. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of DZL was performed. 4. A single crystal structure (4C7K, one 11β-HSD1 conformation) was used; the enzyme's active site is flexible and induced-fit effects are not modelled. 5. The NADP+ cofactor was present in the structure but its 11.12 Å distance from the grid centre means cofactor interactions were not part of the scored pose. 6. All leads are already-known 11β-HSD1 inhibitors; no new chemical matter is proposed. 7. No clinical inference can be drawn: the phase 2 evidence cited for INCB13739 comes from the Rosenstock trial, and docking scores say nothing about A1C, weight, or tolerability. 8. The pipeline's automated target resolution, structure selection and grid-centre selection all failed silently and required manual correction — other silent defaults in the same pipeline are not yet audited.

## 6. Conclusion

No 11β-HSD1 inhibitor in this set beats INCB13739: the reference leads by 1.05 kcal/mol on 4C7K, a margin inside Vina's noise, and all four leads are sub-nanomolar by measured IC50, so docking cannot separate them from the reference. The durable findings are the benchmark values for INCB13739 on 4C7K and the documented chain of pipeline faults — a wrong target, an unparseable structure, and a detergent-centred grid — each caught by verification. The next experiment is a head-to-head 11β-HSD1 IC50 assay of CHEMBL3664636 against INCB13739, not more docking — and the next pipeline change is to verify the accession, the parse, and the centred ligand before any score is reported.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Rosenstock J, Banarer S, Fonseca VA, Inzucchi SE, Sun W, Yao W, Hollis G, Flores R, Levy R, Williams WV, Seckl JR, Huber R; INCB13739-202 Study Group. The 11-beta-hydroxysteroid dehydrogenase type 1 inhibitor INCB13739 improves hyperglycemia in patients with type 2 diabetes inadequately controlled by metformin. *Diabetes Care.* 2010;33(7):1516–1522. doi:10.2337/dc09-2315. ClinicalTrials.gov NCT00698230.
2. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
3. RCSB Protein Data Bank. 11β-hydroxysteroid dehydrogenase type 1 in complex with inhibitor (DZL). PDB ID 4C7K, 1.91 Å. https://www.rcsb.org/structure/4C7K (accessed 6 November 2026).
4. ChEMBL database, European Bioinformatics Institute. Target: 11-beta-hydroxysteroid dehydrogenase 1 (CHEMBL4235); bioactivities accessed 6 November 2026. https://www.ebi.ac.uk/chembl/.
5. International Diabetes Federation. IDF Diabetes Atlas, 10th edition. 2021. Diabetes burden figures: approximately 537 million adults worldwide, including about 33 million in Pakistan.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-008c-2026-11-06.json` (authoritative re-dock: PDB 4C7K, 1.91 Å, DZL chain-A centroid [−21.30, −6.46, 34.49], Vina 1.2.7). Discarded runs are preserved for audit: `hidden_files/dock-HP-008-2026-11-06.json` (wrong target: UniProt P42330 AKR1C3, PDB 1S1P — not 11β-HSD1, scores not reported) and `hidden_files/dock-HP-008b-2026-11-06.json` (correct target P28845 / CHEMBL4235, but PDB 1XU9 receptor parse failure and PDB 1XU7 CHAPS-detergent grid centre — no usable scores). ChEMBL IDs: INCB13739 (query), CHEMBL3664636, CHEMBL4075869, CHEMBL4101787, CHEMBL557417. PDB ID 4C7K. No additional data were generated.
