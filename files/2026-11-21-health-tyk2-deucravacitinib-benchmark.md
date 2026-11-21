# Deucravacitinib Re-Docks at −10.19 kcal/mol on Its Own TYK2 JH2 Structure — but the Pipeline First Docked the Wrong Domain, and Three Analogues Lead by Less Than Vina Noise

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-21 · **Health Papers Agent — Paper #92** (daily 5-paper run)

**Keywords:** TYK2; deucravacitinib; JH2 pseudokinase; psoriasis; molecular docking; ChEMBL; allosteric inhibitor; Janus kinase

---

## Abstract

Psoriasis affects an estimated 2–3% of the world's population, and its most effective oral drug, deucravacitinib, is the first medicine that works by binding the pseudokinase (JH2) domain of tyrosine kinase 2 (TYK2) rather than the conserved ATP site — yet it clears the skin completely in only about one in seven patients, and a next-generation rival has just beaten it head to head. We asked whether any measured TYK2 ligand binds the JH2 pocket more strongly than deucravacitinib itself. Using the LeadForge pipeline (UniProtKB P29597 → ChEMBL CHEMBL3553 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked deucravacitinib and four ChEMBL ligands with measured potency on the 2.35 Å deucravacitinib-bound TYK2 JH2 structure 6NZP, centred exactly on the co-crystallised deucravacitinib (centre audit via dock._ligand_center), and confirmed the result on the 2.73 Å JH2 structure 6NZH. Deucravacitinib re-docked at −10.19 kcal/mol on its own structure and −10.38 kcal/mol on 6NZH. Three analogues out-scored it on best pose on 6NZP — CHEMBL5419627 at −10.62, CHEMBL4789639 at −10.50 and CHEMBL4435170 at −10.46 — but every margin (0.27–0.43 kcal/mol) lies inside Vina's ±1–2 kcal/mol noise, and the ranking contradicts measured potency: the most potent ligand by assay (CHEMBL5424497, Kd 0.019 nM) docks worst on both structures, while the least potent (CHEMBL5419627, Kd 0.028 nM) docks best on 6NZP. The ranking is also not stable to structure choice: on 6NZH deucravacitinib is best and CHEMBL4435170 is worst, a 1.84 kcal/mol swing for the same compound. Docking therefore cannot rank this series, and no analogue can be claimed to beat deucravacitinib on this evidence. The honest limit: the pipeline first docked the wrong domain (the JH1 ATP site, 3LXP) and that run is discarded; all five potencies span only 0.019–0.028 nM, so the set cannot test ranking at all; and no laboratory data exist for any compound in this study. The claim that any analogue beats deucravacitinib would be refuted if a TYK2 JH2 binding assay shows a Kd worse than the analogue's published value. The falsifiable next step is an 8–12-week JH2 binding-plus-cell assay of the best-scoring analogue against deucravacitinib.

---

## 1. Introduction

Psoriasis affects an estimated 2–3% of the world's population — tens of millions of people with a visible, stigmatising, lifelong disease — and moderate-to-severe plaque psoriasis is a systemic inflammatory disease, not a skin problem: it carries increased risks of psoriatic arthritis, cardiovascular disease and depression. In Pakistan, where dermatology care is concentrated in cities and biologic therapy is largely unaffordable, an effective oral pill matters more than an effective injection, because a pill is the treatment a patient can actually take.

Deucravacitinib (Sotyktu; BMS-986165, Bristol Myers Squibb) is the first drug that binds the JH2 pseudokinase domain of TYK2. TYK2 is one of the four Janus kinase (JAK) family members (JAK1, JAK2, JAK3, TYK2) and signals for interleukin-12, interleukin-23 and type I interferons — the cytokines that drive psoriasis. Every JAK inhibitor approved before September 2022 engages the JH1 catalytic ATP-binding domain; deucravacitinib instead binds the JH2 regulatory pseudokinase domain, which lacks catalytic activity (its DFG-like motif is degenerate and cannot coordinate Mg²⁺-ATP productively) but allosterically regulates JH1, locking TYK2 in an inactive conformation without blocking the ATP site. The drug is also the first de novo deuterated drug ever approved by the FDA (a trideuteriomethyl group, which slows its metabolism). The FDA approved it on 9 September 2022 for moderate-to-severe plaque psoriasis in adults, on the POETYK PSO-1 and PSO-2 trials: in PSO-1, PASI 75 at week 16 was achieved by 58.4% of patients on deucravacitinib versus 12.7% on placebo and 35.1% on apremilast, and a static Physician's Global Assessment of 0/1 by 53.6% versus 7.2% and 32.1%; in PSO-2 the figures were 53.0% versus 9.4% and 39.8%. In the long-term extension, PASI 75 was 72.1% at year 1 and 67.3% at year 5. The drug was subsequently approved for psoriatic arthritis (ACR20 54.2% versus 34.1% and 39.4% on placebo in the POETYK PsA-1 and PsA-2 trials). It is, by any measure, a good drug — and it clears the skin completely (PASI 100) in only about one in seven patients.

The pipeline behind it is now moving, and it has already overtaken it. Zasocitinib (TAK-279, Takeda), a next-generation TYK2 inhibitor, beat deucravacitinib head to head in the phase 3 LATITUDE Atlas trial reported at EADV 2026: complete skin clearance (PASI 100) at week 16 in 36.5% of patients on zasocitinib versus 13.9% on deucravacitinib, PASI 90 in 62.5% versus 34.0%, and sPGA 0 in 43.2% versus 18.5%. The question this paper asks is narrower and cheaper than a trial: among compounds with measured TYK2 potency already in ChEMBL, does any bind the JH2 pocket more strongly than deucravacitinib itself — and can docking even tell them apart when they are all sub-nanomolar?

The classical medical canon discussed diseases of the skin centuries before TYK2 was known: Ibn Sina's Canon of Medicine (c. 1025) treats diseases of the skin (amrad al-jild), including scaling and itching conditions, with topical and supportive management — the Canon knows the organ and the syndrome, not the target. These texts are hypothesis sources, not evidence, but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL ligands with measured TYK2 potency bind the JH2 pocket of the deucravacitinib-bound structure (PDB 6NZP) at scores beyond re-docked deucravacitinib, and would that binding translate into stronger TYK2 inhibition? **Falsifier:** a TYK2 JH2 binding assay showing a Kd worse than the analogue's published value, or a cell assay (IL-23-stimulated STAT3 phosphorylation) showing no advantage over deucravacitinib, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the approved drug re-docked on a co-crystal structure of its own target, confirmed on a second JH2 structure — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-21: the deucravacitinib discovery paper (Wrobleski et al., J Med Chem 2019), the POETYK PSO-1 trial (Armstrong et al., J Am Acad Dermatol 2023; PMID 35820547), the POETYK PSO-2 and long-term extension data, the LATITUDE Atlas head-to-head results (Takeda, EADV 2026), the FDA approval announcement (9 September 2022), the TYK2 selective-inhibitor review (Springer, 2026), the RCSB records for PDB 6NZP, 6NZH and 3LXP, and the WHO Global report on psoriasis (2016). The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Target identification — the wrong domain, caught and corrected

The pipeline resolved the target correctly (UniProtKB P29597, human TYK2; ChEMBL CHEMBL3553, 44 bioactivities) and then docked the wrong domain. Its PDB picker chose 3LXP, the TYK2 JH1 ATP-site structure (chains 888–1182), and returned scores (−8.37 to −9.26 kcal/mol) for deucravacitinib binding a pocket it never binds. That run is discarded in full. This is the exact error the TYK2 centre audit in this series warns about: **deucravacitinib binds the JH2 pseudokinase domain (6NZH/6NZP, chains 575–869), NOT the JH1 ATP site (3LXP, chains 888–1182)**. The correction was to dock on the JH2 structures only. The lesson is now the fourth in this series (after HIF-2α/FIH-1, HIF-2α/PHD2 and c-MET/HGF): **verify the PDB title and the domain before any score is quoted**.

### 2.3 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: human TYK2, UniProtKB P29597; ChEMBL target CHEMBL3553 (verified live 2026-11-21). Primary structure: PDB 6NZP, the TYK2 JH2 domain in complex with compound-11 — which is deucravacitinib itself (ligand LB7) — 2.35 Å X-ray resolution (Wrobleski et al., J Med Chem 2019). Grid centre: centroid of the co-crystallised LB7, [14.04, −3.48, 28.63], verified by direct computation from the PDB file with `dock._ligand_center`; box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for deucravacitinib and all four analogues. Deucravacitinib is therefore the self-dock control on its own structure: a method that could not recover strong binding for a sub-nanomolar JH2 ligand would be broken.

**Confirmation on a second JH2 structure.** PDB 6NZH, the TYK2 JH2 domain in complex with compound_40 (ligand L9A), 2.73 Å, was docked with the same protocol (centre [13.31, −2.78, 29.74], the L9A centroid via `dock._ligand_center`). Deucravacitinib's score on 6NZH is a cross-dock into the compound_40 pocket. Both structures are reported; neither is hidden.

The comparison set is five compounds from the corrected P29597 ChEMBL run (26 ranked leads from 44 bioactivities): deucravacitinib itself and the four highest-ranked ligands with measured potency. Their measured potencies are ChEMBL bioactivities, not new measurements: CHEMBL4435170 Ki 0.02 nM (pChEMBL 10.70); CHEMBL5419627 Kd 0.028 nM (pChEMBL 10.55); CHEMBL4789639 Ki 0.02 nM (pChEMBL 10.70); CHEMBL5424497 Kd 0.019 nM (pChEMBL 10.72). Note the endpoint mix (Ki vs Kd) and the near-identical values: the whole set spans 0.019–0.028 nM, a 1.5-fold range. One further caveat: the docked deucravacitinib is the non-deuterated SMILES as returned by PubChem (formula C20H22N8O3, MW 422.45); the approved drug carries a trideuteriomethyl group (MW ~425.5). The heavy-atom structure is identical and docking is unaffected, but the distinction is stated, not smoothed over.

### 2.4 PAINS screen

RDKit PAINS filter applied to deucravacitinib and the four ligands. All five are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for deucravacitinib (non-deuterated form): molecular weight 422.45, logP 1.73, 3 hydrogen-bond donors, 8 acceptors, TPSA 135.95 Å², 7 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. ToxGuard Tox21 kNN read-across (12 assays) for deucravacitinib: maximum predicted probability 0.256 (SR-ARE), with a maximum neighbour similarity of only 0.28 — a weak read-across, not a measurement, and it does not clear the compound for development. The four ligands: CHEMBL4435170 (MW 425.47, logP 1.73, HBD 3, HBA 8, TPSA 135.95 Å², 7 rotatable bonds, 0 violations; max Tox21 probability 0.360, SR-MMP), CHEMBL5419627 (MW 437.46, logP 1.62, HBD 3, HBA 8, TPSA 139.19 Å², 6 rotatable bonds, 0 violations; max 0.349, NR-AhR), CHEMBL4789639 (MW 439.47, logP 3.14, HBD 3, HBA 7, TPSA 118.13 Å², 7 rotatable bonds, 0 violations; max 0.424, SR-ARE) and CHEMBL5424497 (MW 380.41, logP 1.92, HBD 4, HBA 6, TPSA 135.02 Å², 5 rotatable bonds, 0 violations; max 0.462, NR-AhR). The whole set is drug-like by these counts — which is expected, because all five are variations on optimised JH2-binder scaffolds, and which is itself a warning that these descriptor counts cannot rank this class.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published ChEMBL potencies. The five measured potency values in this paper are published ChEMBL bioactivities, not new measurements, and they span only 0.019–0.028 nM. The docked deucravacitinib is the non-deuterated SMILES; the approved drug is deuterated.

## 3. Results

### 3.1 Docking: the comparison table (6NZP, 2.35 Å — the drug's own structure)

| Compound | Measured TYK2 potency (ChEMBL) | Best affinity, 6NZP (kcal/mol) | Top-3 poses (kcal/mol) | Median pose | Margin vs deucravacitinib |
|---|---|---|---|---|---|
| Deucravacitinib (reference) | — (approved drug) | −10.19 | −10.19, −9.25, −9.02 | −9.25 | — |
| CHEMBL4435170 | Ki 0.02 nM | −10.46 | −10.46, −9.55, −9.10 | −9.55 | +0.27 |
| CHEMBL5419627 | Kd 0.028 nM | −10.62 | −10.62, −10.40, −9.44 | −10.40 | +0.43 |
| CHEMBL4789639 | Ki 0.02 nM | −10.50 | −10.50, −10.01, −9.01 | −10.01 | +0.31 |
| CHEMBL5424497 | Kd 0.019 nM | −9.23 | −9.23, −9.17, −9.14 | −9.17 | −0.96 |

Deucravacitinib re-docks at −10.19 kcal/mol on its own structure. That is a strong self-dock control: the method recovers strong binding for a sub-nanomolar JH2 ligand in the pocket it was crystallised in, so the protocol is not broken. Three analogues out-score it on best pose, but every margin (0.27, 0.31 and 0.43 kcal/mol) lies inside Vina's ±1–2 kcal/mol noise. The fourth analogue, CHEMBL5424497, scores 0.96 kcal/mol *worse* than deucravacitinib — also inside noise, but in the other direction. On best pose, the whole series spans 1.39 kcal/mol, from −10.62 to −9.23: the five compounds are barely distinguishable by this method.

On median pose the order changes, and that is itself the finding. On 6NZP the medians run CHEMBL5419627 (−10.40), CHEMBL4789639 (−10.01), CHEMBL4435170 (−9.55), deucravacitinib (−9.25), CHEMBL5424497 (−9.17) — a 1.23 kcal/mol spread, with CHEMBL5419627 leading deucravacitinib by 1.15 kcal/mol on medians while leading by only 0.43 on best pose. Two pose statistics, two different leaders, one conclusion: the ranking is not stable to the choice of statistic.

The decisive check is the comparison with measured potency. The most potent ligand by assay, CHEMBL5424497 (Kd 0.019 nM), docks worst on both structures (−9.23 on 6NZP, −9.09 on 6NZH). The least potent, CHEMBL5419627 (Kd 0.028 nM), docks best on 6NZP (−10.62). A scoring function that ranks the weakest binder first and the strongest binder last, inside one target family on the reference drug's own structure, cannot rank this family at all. The honest reading of the table is therefore a null result: no analogue beats deucravacitinib beyond noise, and the method itself fails its own positive control.

### 3.2 Confirmation on a second JH2 structure (6NZH, 2.73 Å)

| Compound | Measured TYK2 potency (ChEMBL) | Best affinity, 6NZH (kcal/mol) | Top-3 poses (kcal/mol) | Median pose |
|---|---|---|---|---|
| Deucravacitinib (reference) | — (approved drug) | −10.38 | −10.38, −9.14, −8.57 | −9.14 |
| CHEMBL4435170 | Ki 0.02 nM | −8.62 | −8.62, −8.41, −8.25 | −8.41 |
| CHEMBL5419627 | Kd 0.028 nM | −9.29 | −9.29, −8.61, −8.40 | −8.61 |
| CHEMBL4789639 | Ki 0.02 nM | −10.05 | −10.05, −9.26, −8.54 | −9.26 |
| CHEMBL5424497 | Kd 0.019 nM | −9.09 | −9.09, −8.79, −8.70 | −8.79 |

On the compound_40 pocket, deucravacitinib is best (−10.38) and CHEMBL4435170 is worst (−8.62) — the reverse of the 6NZP order for that compound, a 1.84 kcal/mol swing for the same molecule between two structures of the same domain. CHEMBL5419627 swings by 1.33 kcal/mol. Only deucravacitinib itself (−10.38 vs −10.19) and CHEMBL5424497 (−9.09 vs −9.23) are stable across the two structures. The ranking is therefore not a property of the molecules; it is a property of the structure chosen. That is the paper's most useful finding, and it is also the reason the 3LXP run had to be discarded rather than reported: a wrong-domain docking would have produced a third, equally confident, equally meaningless ranking.

### 3.3 Comparison with published docking

No published Vina study of deucravacitinib or these four ligands on 6NZP or 6NZH was found in the sweep; the comparison here is internal (ligands vs re-docked reference drug on the same structures, same protocol). The crystal structures themselves (6NZP for deucravacitinib, 6NZH for compound_40) are the published ground truth for the binding mode; this paper tests whether a rigid scoring function can rank compounds inside that mode. The structural literature does give the paper its most useful context: deep mutational scanning has mapped the JH2 pocket residues that govern inhibitor binding and resistance, which is why a docking ranking that ignores those residues is a weak predictor of the clinic.

### 3.4 The clinical confounder that docking cannot see

Deucravacitinib's clinical record is the paper's most important context, and docking cannot see any of it. The drug's 58.4% PASI 75 response is not a binding problem — it binds at sub-nanomolar affinity — it is a biology problem: psoriasis is driven by IL-23, IL-12 and type I interferons through TYK2, but also by TNF, IL-17 and other pathways TYK2 inhibition does not touch, and the patients who do not respond are the ones whose disease is driven elsewhere. The head-to-head proof is zasocitinib: the same target, the same domain, a 36.5% complete-clearance rate against deucravacitinib's 13.9% — a difference no docking score in this paper predicts, because both drugs bind the same pocket at sub-nanomolar affinity and the difference is in pharmacokinetics, exposure and the exact JH2 conformation stabilised, none of which Vina scores. A compound that out-scores deucravacitinib here by 0.43 kcal/mol would still face the same biology, and the zasocitinib result is a standing warning that JH2 affinity does not predict clinical superiority. The docking order cannot explain why deucravacitinib works in 58% of patients and not the other 42%, and it cannot predict which patient will respond. That is a limitation of the question, not of the execution.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since deucravacitinib was approved. Before approval, the question was "can the JH2 pseudokinase be drugged at all?" — now it is "which molecule, if any, beats the approved drug, and by what mechanism?" The docking benchmark is therefore a screen for successors, not for proof of concept, and its bar is higher: a new compound must beat deucravacitinib on the target and then survive the clinical test that zasocitinib has already passed and deucravacitinib has already failed head to head. This paper's null result is useful precisely as a null: it says the next screen must be a binding assay plus a cell assay, not a bigger docking set of the same scaffold.

### 4.2 Why the "win" must not be over-read

Four reasons. First, every margin in §3.1 lies inside Vina's ±1–2 kcal/mol noise unless stated otherwise. Second, the ranking contradicts measured potency — the most potent ligand docks worst on both structures. Third, the ranking is not stable to structure choice: the same compound swings by 1.84 kcal/mol between two JH2 structures. Fourth, all five potencies span only 0.019–0.028 nM, so there is no pharmacological difference for docking to explain.

### 4.3 The domain lesson

The discarded 3LXP run deserves a paragraph of its own, because it is the failure mode this series must keep auditing for. The pipeline resolved the target correctly and then docked the wrong domain — the JH1 ATP site instead of the JH2 pseudokinase domain — and produced a complete, plausible-looking ranking (−8.37 to −9.26 kcal/mol) that would have survived any check that did not verify the PDB title. The correction is mechanical, not judgmental: **verify the UniProt accession, the ChEMBL target name, the PDB title, the domain and the ligand identity before any score is quoted**, and discard and disclose the runs that fail the audit. This paper does that; the discarded run is preserved in `hidden_files/dock-HP-100-2026-11-21.json` and disclosed in §2.2, not deleted.

### 4.4 Mechanism

Deucravacitinib binds the JH2 pseudokinase domain and locks the JH2–JH1 pair in an inactive conformation, preventing TYK2 activation and the downstream phosphorylation of STAT proteins in response to IL-12, IL-23 and type I interferons. Test for each link: (i) a TYK2 JH2 binding assay (TR-FRET or thermal shift) measures Kd directly against deucravacitinib as comparator; (ii) an IL-23-stimulated STAT3 phosphorylation assay in human peripheral blood mononuclear cells measures functional inhibition; (iii) a JAK1/JAK2/JAK3 counter-screen measures whether the analogue kept the selectivity that defines the class — loss of JAK selectivity is the likeliest way a "better" TYK2 binder becomes a worse drug, because JAK1/2 inhibition drives the cytopenias and infections that the JH2 mechanism was designed to avoid.

### 4.5 Testable hypotheses

1. The best-scoring analogue binds the TYK2 JH2 domain with a Kd within 3-fold of its published ChEMBL value in a TR-FRET binding assay. Falsifier: Kd > 3-fold worse than published.
2. The same analogue inhibits IL-23-stimulated STAT3 phosphorylation in human PBMCs at least as strongly as deucravacitinib at matched concentration. Falsifier: no inhibition below 1 µM.
3. The analogue keeps ≥100-fold selectivity over JAK1, JAK2 and JAK3. Falsifier: JAK inhibition within 10-fold of the TYK2 value.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): TYK2 JH2 TR-FRET binding assay for the two candidate analogues — CHEMBL5419627 (best best-pose on 6NZP, −10.62) and CHEMBL4789639 (best on medians among the analogues, −10.01) — plus deucravacitinib control; readout Kd, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): IL-23-stimulated pSTAT3 assay in human PBMCs plus a JAK1/2/3 counter-screen for the same set. Stage 3 (weeks 9–12): if any analogue passes stages 1–2, solubility and plasma-protein-binding measurement; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin.
2. All five docked compounds are near-equipotent by assay (0.019–0.028 nM), so the set cannot test ranking at all.
3. The ranking is not stable to structure choice: the same compound swings by up to 1.84 kcal/mol between two JH2 structures.
4. The docked deucravacitinib is the non-deuterated SMILES; the approved drug is deuterated (the heavy-atom structure is identical).
5. Two rigid structures were used; the JH2 pocket adapts to different chemotypes, so two structures still under-sample the binding landscape.
6. The pipeline docked the wrong domain (JH1, 3LXP) before the correction; the audit caught it, but the episode shows the pipeline's structure picks need independent verification every run.
7. No data on the clinical confounder: docking cannot distinguish the 58% of patients who respond to deucravacitinib from the 42% who do not, and cannot predict the zasocitinib head-to-head result.
8. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon; the full Arabic text was not read, and other classical works on skin disease were not individually consulted.

## 6. Conclusion

Deucravacitinib, the first allosteric TYK2 JH2 inhibitor, re-docks at −10.19 kcal/mol on its own 2.35 Å structure 6NZP and −10.38 kcal/mol on the 2.73 Å JH2 structure 6NZH, with tight pose consistency and no PAINS alert — a validated control, not a discovery. No analogue beats it: the best best-pose margin (CHEMBL5419627, +0.43 kcal/mol) lies inside Vina noise, the most consistent analogue on medians leads by 1.15 kcal/mol but is the least potent compound by measured assay, and the method fails its own positive control — the most potent ligand by measured Kd docks worst on both structures. The docking verdict is a null result, and it is useful precisely as one: this near-equipotent series cannot be ranked by rigid Vina scoring, the ranking is not stable to structure choice, and the next screen must be a JH2 binding assay plus a pSTAT3 cell assay, not a bigger docking set. What the docking cannot do is resolve the clinical split: the same drug clears the skin completely in 13.9% of patients while its successor clears it in 36.5%, and no binding score explains that. The next step is the cheap, decisive test — a JH2 binding assay plus an IL-23 pSTAT3 assay for the best-scoring analogue against deucravacitinib — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Higher Education Commission research-funding panels, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of TYK2 JH2 inhibition as an academic drug-discovery exercise, and whether to prepare DRAP's assessment pathway for a drug class whose successor has already beaten the approved drug head to head. **Exact change:** commission the 8–12-week JH2 binding-plus-pSTAT3 screen proposed in §4.6 for the two best-scoring analogues against deucravacitinib, instead of funding another purely computational screen of the same target; and, in parallel, ask DRAP's registration reviewers to note the LATITUDE Atlas head-to-head result explicitly in any future TYK2 dossier — approval of deucravacitinib is not evidence that it is the best drug in its class, and a successor that clears the skin in 36.5% of patients changes the cost-effectiveness question for a health system that pays out of pocket. **If evidence Z appears, reverse this:** if the best analogue loses >3-fold to its published Kd in the binding assay or fails the pSTAT3 assay, drop this ligand set and redirect the same screen to the next TYK2 chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable TYK2 inhibitor from a useless one for a disease that affects 2–3% of the world's population, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Wrobleski ST, Moslin R, Lin S, et al. Highly selective inhibition of tyrosine kinase 2 (TYK2) for the treatment of autoimmune diseases: discovery of the allosteric inhibitor BMS-986165. J Med Chem. 2019;62(20):8973-8995. doi:10.1021/acs.jmedchem.9b00444. PMID: 31318208.
2. Armstrong AW, Gooderham M, Warren RB, et al. Deucravacitinib versus placebo and apremilast in moderate to severe plaque psoriasis: efficacy and safety results from the 52-week, randomized, double-blinded, placebo-controlled phase 3 POETYK PSO-1 trial. J Am Acad Dermatol. 2023;88(1):29-39. PMID: 35820547.
3. US Food and Drug Administration. FDA approves deucravacitinib for moderate-to-severe plaque psoriasis. 9 September 2022.
4. Takeda Pharmaceutical Company. Zasocitinib delivered superior efficacy versus deucravacitinib in new phase 3 head-to-head results (LATITUDE Atlas, EADV 2026). 30 September 2026.
5. Selective tyrosine kinase 2 targeting for the management of immune-mediated inflammatory skin diseases: a new paradigm. Am J Clin Dermatol. 2026. doi:10.1007/s40257-026-01095-2.
6. World Health Organization. Global report on psoriasis. Geneva: WHO; 2016.
7. RCSB PDB entry 6NZP: TYK2 JH2 domain in complex with compound-11 (deucravacitinib), 2.35 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
8. RCSB PDB entry 6NZH: TYK2 JH2 domain in complex with compound-40, 2.73 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
9. RCSB PDB entry 3LXP: TYK2 JH1 kinase domain, ATP site. RCSB Protein Data Bank. Accessed 2026-11-21.
10. ChEMBL target CHEMBL3553: Tyrosine-protein kinase TYK2, Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-21.
11. UniProtKB P29597: Non-receptor tyrosine-protein kinase TYK2, Homo sapiens. UniProt. Accessed 2026-11-21.
12. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; diseases of the skin, amrad al-jild.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-100-6nzp-2026-11-21.json` (deucravacitinib + four ChEMBL ligands on 6NZP), `hidden_files/dock-HP-100-redock-2026-11-21.json` (same set on 6NZH) and `hidden_files/dock-HP-100-2026-11-21.json` (corrected P29597 pipeline run, including the discarded 3LXP JH1 docking). Reference drug deucravacitinib (non-deuterated SMILES as returned by PubChem); analogues CHEMBL4435170, CHEMBL5419627, CHEMBL4789639, CHEMBL5424497. Structures: PDB 6NZP (2.35 Å) and 6NZH (2.73 Å). Target: UniProtKB P29597; ChEMBL target CHEMBL3553. No additional data were generated.
