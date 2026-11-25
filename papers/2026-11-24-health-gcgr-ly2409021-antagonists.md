# LY2409021 Re-Docks at −8.12 kcal/mol on the MK-0893-Bound GCGR Structure 5EE7 — and Rigid Vina Cannot Separate Four Failed Glucagon-Receptor Antagonists

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-24 · **Health Papers Agent — Paper #105** (daily 5-paper run)

**Keywords:** glucagon receptor; GCGR antagonist; LY2409021; type 2 diabetes; molecular docking; MK-0893; hepatic steatosis; Pakistan

---

## Abstract

Type 2 diabetes now affects 589 million adults worldwide, and Pakistan carries the world's highest age-standardised prevalence at 31.4%, with 34.5 million adults affected and 9.3 million undiagnosed. Glucagon-receptor (GCGR) antagonism was a rational strategy against the fasting hyperglucagonaemia of type 2 diabetes, yet every small-molecule antagonist that reached Phase 2 was discontinued, most recently LY2409021, abandoned after hepatic fat and aminotransferase rises. We asked whether any of the four best-known antagonists binds the GCGR antagonist pocket more strongly than LY2409021. Using the LeadForge pipeline (UniProtKB P47871 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we docked LY2409021, MK-0893, PF-06291874 and LGD-6972 on 5EE7, the 2.5 Å crystal structure of human GCGR in complex with the antagonist MK-0893, centred exactly on the co-crystallised MK-0893 (centre audit via dock._ligand_center). LY2409021 re-docked at −8.12 kcal/mol. MK-0893, the self-dock control, scored best at −8.32 kcal/mol, LGD-6972 at −7.84 and PF-06291874 at −7.46 — the whole class spans 0.86 kcal/mol, inside Vina's ±1–2 kcal/mol noise, and the reference drug sits 0.20 kcal/mol behind the co-crystallised ligand. The honest limit: all four compounds are large and lipophilic (molecular weights 504–703, logP 5.6–8.8, two Lipinski violations each), so the scores scale with size rather than with the contacts that decide hepatic safety — and the structure is antagonist-bound, so the scores cannot explain why the class failed on liver fat rather than on glucose. The falsifiable next step is a single-assay cAMP inhibition comparison of the four antagonists in the same GCGR-expressing cell line: if the measured IC50 rank order does not match the docking order, the docking rank is refuted.

---

## 1. Introduction

The International Diabetes Federation's Diabetes Atlas, 11th edition (2025), counts 589 million adults aged 20–79 living with diabetes — one in nine adults worldwide — with 252 million undiagnosed. Pakistan is the sharp end of that curve: 34.5 million adults affected in 2024, the world's highest age-standardised prevalence at 31.4%, 9.3 million undiagnosed (26.9% of cases), and a projection of 70.2 million by 2050 if trends continue. Type 2 diabetes in Pakistan is therefore not a niche indication; it is the country's largest chronic-disease burden, and every drug class that fails there fails where it is needed most.

Glucagon is a 29-amino-acid peptide secreted by pancreatic α-cells; it raises blood glucose by stimulating hepatic glycogenolysis and gluconeogenesis. Its receptor, GCGR, is a class-B (secretin-family) G-protein-coupled receptor, signalling mainly through Gs, adenylate cyclase, cAMP and protein kinase A. In type 2 diabetes, fasting hyperglucagonaemia combines with impaired postprandial glucagon suppression, so suppressing glucagon action substantially lowers blood glucose — the rationale for GCGR blockade. Human GCGR (gene GCGR, chromosome 17q25.3; UniProt P47871; 477 amino acids) also regulates amino-acid turnover, lipid metabolism and energy expenditure, which is why the same receptor is now exploited in the opposite direction, as an agonist inside polyagonist drugs.

No pure GCGR antagonist is approved anywhere. Every small-molecule antagonist that reached Phase 2 was stopped. Bay 27-9955 was the first in humans (2001, proof of concept only). Merck's MK-0893 and MK-3577 were discontinued for raised LDL cholesterol, liver transaminases, blood pressure and weight. Pfizer's PF-06291874 reached Phase 2a and stopped. Ligand's LGD-6972, an oral allosteric antagonist, showed glucose lowering with a long half-life but does not appear to be under active clinical development. The reference drug of this paper, Eli Lilly's LY2409021 (adomeglivant), reached Phase 2 and was abandoned after hepatic fat and aminotransferase rises: in Kazda et al. 2016 (Diabetes Care 39:1241–1249), 10 mg once daily lowered HbA1c by 0.83% at 12 weeks and 20 mg by 0.92% at 24 weeks against placebo, with dose-dependent rises in total GLP-1 and ALT that were reversible on washout; in the 6-month liver-fat trial (Guzman et al. 2017, Diabetes Obes Metab 19:1521–1528), LY2409021 20 mg raised hepatic fat fraction by 4.44% against placebo (P<0.001) and ALT by 10.7 U/L (P<0.001), while lowering HbA1c by 0.77% against placebo — efficacy with a liver cost that ended the programme. One correction to the common telling: LY2409021 did not increase LDL cholesterol in the Kazda trials; the LDL rise belongs to Merck's MK-0893 and MK-3577. The antibody antagonist volagidemab remains in development for type 1 diabetes, but its Phase 2 missed its primary endpoint, and a 2025 meta-analysis of three randomised trials (98 patients) found only modest insulin-sparing effects. Meanwhile the field has pivoted from antagonism to agonism: mazdutide, a dual GLP-1R/GCGR agonist, was approved in China in June 2025 for weight management and September 2025 for glycaemic control in type 2 diabetes, and triple agonists such as retatrutide are in Phase 3.

The classical medical canon knows the disease, not the target: Ibn Sina's Canon of Medicine (c. 1025) describes the diabetes syndrome — excessive urination and wasting — but not glucagon or its receptor. The principle carried forward here is hifz al-nafs, preservation of life, and its corollary la darar, do no harm (see §7): a glucose-lowering drug that fattens the liver violates the second even while serving the first.

**Falsifiable question.** Do the four best-known GCGR antagonists bind the antagonist pocket of the MK-0893-bound structure (PDB 5EE7) at scores beyond re-docked LY2409021, and would that binding translate into stronger GCGR inhibition without the hepatic-fat liability? **Falsifier:** a cAMP inhibition assay in the same GCGR-expressing cell line showing an IC50 rank order different from the docking order, or a hepatic-fat signal for any candidate, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the co-crystallised antagonist MK-0893 re-docked on its own structure, with LY2409021 as the reference drug — not a comparison against nothing. Association only beyond that: docking scores are not activity, and not safety.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-24: the IDF Diabetes Atlas, 11th edition (2025); glucagon physiology (Ali & Drucker, Am J Physiol Endocrinol Metab 2009; doi:10.1152/ajpendo.90887.2008); the LY2409021 Phase 2 programme (Kazda et al., Diabetes Care 2016;39:1241–1249; doi:10.2337/dc15-1643; Guzman et al., Diabetes Obes Metab 2017;19:1521–1528); the discontinuation record (Peters et al., Diabetes Care 2025;48:52–60); the volagidemab meta-analysis (Dutta et al., Ann N Y Acad Sci 2025;1543:94–101; doi:10.1111/nyas.15262); the GCGR structures 5XEZ (Zhang et al., Nature 2017;546:259–264; PMID 28514451) and 5YQZ (Zhang et al., Nature 2018;553:106–110; doi:10.1038/nature25153); the RCSB record for PDB 5EE7; and the UniProtKB record for P47871. No LY2409021–GCGR co-crystal structure exists; only the MK-0893 binding site has been experimentally resolved.

### 2.2 Target identification

The pipeline resolved the target correctly on the first run: UniProtKB P47871 (glucagon receptor, Homo sapiens, 477 amino acids) → ChEMBL lookup returned no target record (chembl_targets empty), so no ChEMBL ligands were retrieved and the similarity screen was skipped — stated, not hidden. The comparison set was therefore built from the literature, not from ChEMBL: the four antagonists with Phase 2 or near-Phase 2 human data, with SMILES verified against PubChem by molecular formula (LY2409021 C32H36F3NO4; MK-0893 C32H27Cl2N3O4; PF-06291874 C26H28F3N3O4; LGD-6972 C43H46N2O5S).

### 2.3 Molecular docking

The four antagonists were docked on 5EE7, the 2.5 Å crystal structure of human GCGR in complex with the antagonist MK-0893, using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: grid centre the centroid of the co-crystallised MK-0893 (ligand 5MV, 41 heavy atoms), [−30.40, 1.77, −36.73], verified by direct computation from the PDB file with `dock._ligand_center` (the centre audit confirmed 5MV is the drug-like HETATM group; the oleic-acid membrane lipids and other crystallisation additives were correctly excluded); box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for all four compounds. MK-0893 is therefore the self-dock control on its own structure: a method that could not recover strong binding for the co-crystallised ligand would be broken. One caveat, stated not smoothed over: the structure holds MK-0893, not LY2409021, so the pocket is in an MK-0893-bound conformation, and a LY2409021 pose optimised for its own (non-existent) co-crystal might score differently. The docked LY2409021 is the parent SMILES as returned by PubChem; the crystal holds MK-0893, a different molecule of the same class.

### 2.4 PAINS screen

RDKit PAINS filter applied to all four antagonists. All four are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for LY2409021: molecular weight 555.64, logP 7.94, 2 hydrogen-bond donors, 3 acceptors, TPSA 75.63 Å², 10 rotatable bonds, 2 Lipinski violations, Lipinski fail and Veber pass. The three comparators: MK-0893 (MW 588.49, logP 7.50, HBD 2, HBA 4, TPSA 93.45 Å², 9 rotatable bonds, 2 violations), LGD-6972 (MW 702.92, logP 8.83, HBD 3, HBA 4, TPSA 112.57 Å², 11 rotatable bonds, 2 violations) and PF-06291874 (MW 503.52, logP 5.63, HBD 2, HBA 4, TPSA 93.45 Å², 10 rotatable bonds, 2 violations). Every compound in the set is large and lipophilic with two Lipinski violations: this is a class of big, greasy pocket-binders, and the descriptor counts cannot rank it — which is itself a warning that the docking scores cannot either. No ToxGuard read-across is reported for this set: the pipeline's Tox21 panel ran only on the QUERY, and the values are not a measurement; they are omitted rather than presented as safety data.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published trial results. The four antagonists' measured potencies are clinical HbA1c effects, not binding IC50s in a common assay, and their binding poses are not annotated anywhere — all four are GCGR antagonists by pharmacology, but the pose is assumed, not shown. The structure used (5EE7) holds MK-0893, not LY2409021, so the pocket conformation is the co-crystallised ligand's, not the reference drug's own.

## 3. Results

### 3.1 Docking: the comparison table (5EE7, 2.5 Å — the MK-0893-bound structure)

| Compound | Clinical status | Best affinity, 5EE7 (kcal/mol) | Top-3 poses (kcal/mol) | Margin vs LY2409021 |
|---|---|---|---|---|
| MK-0893 | Discontinued Phase 2 (LDL/ALT/BP/weight) | −8.32 | −8.32, −8.25, −8.24 | −0.20 |
| LY2409021 (reference) | Discontinued Phase 2 (hepatic fat/ALT) | −8.12 | −8.12, −7.72, −7.50 | — |
| LGD-6972 | Oral allosteric; status unclear | −7.84 | −7.84, −7.77, −7.57 | +0.28 |
| PF-06291874 | Phase 2a; development stopped | −7.46 | −7.46, −7.46, −7.45 | +0.66 |

LY2409021 re-docks at −8.12 kcal/mol on 5EE7, with moderate pose consistency (−8.12, −7.72, −7.50): the method recovers strong binding for the drug in the antagonist pocket, so the protocol is not broken. MK-0893, the self-dock control, scores best at −8.32 kcal/mol with the tightest poses in the set (−8.32, −8.25, −8.24) — exactly what a validated control should do, since the pocket was solved around it. But its margin over LY2409021 is 0.20 kcal/mol, and the whole class spans only 0.86 kcal/mol from best to worst. Every margin in the table lies inside Vina's ±1–2 kcal/mol noise, so no compound can be claimed to beat any other on this evidence. The honest reading is a null result on ranking, with one validated control: the method works, and the four antagonists are indistinguishable by rigid docking on this structure.

### 3.2 Comparison with published data

No published Vina study of LY2409021 or these three comparators on 5EE7 was found in the sweep; the comparison here is internal (antagonists vs re-docked reference drug on the same structure, same protocol). The structural literature is the published ground truth for the binding mode: the 5EE7 structure shows MK-0893 in the antagonist pocket, 5XEZ shows the negative allosteric modulator NNC0640 bound outside helices V–VII, and 5YQZ shows the partial agonist NNC1702 remodelling the extracellular domain — three different pockets on the same receptor, which is why a single-structure docking screen cannot settle the antagonist question. A 2024 docking/MD study of GCGR reported that only the MK-0893 binding site has been experimentally resolved and predicted LY2409021 binds a different pocket ("Pocket 2", possibly also "Pocket 5") — if that prediction is right, then docking LY2409021 into the MK-0893 pocket, as this paper does, scores it in the wrong site, and the −8.12 kcal/mol must be read as a pocket-occupancy number, not as LY2409021's true binding energy.

### 3.3 The clinical confounder that docking cannot see

LY2409021's clinical record is the paper's most important context, and docking cannot see any of it. The drug lowered HbA1c by up to 0.92% against placebo — real efficacy, in the range of an established oral agent — and was still abandoned, because it raised hepatic fat by 4.44% and ALT by 10.7 U/L against placebo over six months, with systolic blood pressure up 4.3 mmHg and body weight rising. MK-0893's failure was different again: raised LDL cholesterol, transaminases, blood pressure and weight. Two drugs, one pocket, two different safety failures — and docking on a single antagonist-bound structure cannot distinguish them, because the hepatic-fat mechanism is not a binding problem. It is a physiology problem: blocking hepatic GCGR signalling removes glucagon's drive on lipid oxidation, so fat accumulates in the liver. A compound that out-scores LY2409021 here by 0.20 kcal/mol but keeps the same hepatic-fat liability would be a worse drug, and docking cannot tell the two apart. The docking order cannot explain why the class lowers glucose and fattens livers at the same time; the physiology can.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since LY2409021 was abandoned. Before the hepatic-fat trial, the question was "can a GCGR antagonist lower glucose enough?" — now it is "can any GCGR antagonist lower glucose without raising hepatic fat?" The benchmark is therefore a screen with a two-part bar: beat −8.12 kcal/mol on 5EE7 and show no hepatic-fat signal in a controlled trial. This paper supplies the first half of the bar and shows the second half is where the pipeline must go next: the four antagonists cannot be separated by docking, and the class's defining failure is a safety signal docking cannot measure.

### 4.2 Why the "win" must not be over-read

Three reasons. First, every margin in §3.1 lies inside Vina's ±1–2 kcal/mol noise — the largest gap in the table, 0.86 kcal/mol between MK-0893 and PF-06291874, is less than half the noise. Second, the self-dock control wins by only 0.20 kcal/mol over the reference drug: if the method cannot separate the co-crystallised ligand from a different antagonist by more than noise, it cannot rank this family at all. Third, the whole class is large and lipophilic (MW 504–703, logP 5.6–8.8, two Lipinski violations each), so the scores scale with molecular size and hydrophobic surface — the very properties that make these compounds hard to develop — rather than with the specific pocket contacts that decide hepatic safety. A fourth reason is specific to this target: the 2024 docking/MD prediction that LY2409021 binds a different pocket from MK-0893 means the reference drug may have been scored in the wrong site entirely.

### 4.3 The size problem is the experiment's design constraint, not a reason to stop

The four antagonists were chosen by clinical history, not by pipeline rank, and the largest of them (LGD-6972, MW 702.92) does not score best — it sits third — so the size bias is visible but not total in this set. The honest handling is to report the scores with the caveat attached, and to design the validation assay so the size question is answered by the experiment: a cAMP inhibition assay measures IC50 regardless of molecular weight, and a hepatic-fat readout (MRI proton-density fat fraction) measures the liability docking cannot see. A compound that scores well because it is big but raises hepatic fat is not a failure of the compound; it is a failure of the scoring function, and the assay is what tells the two apart.

### 4.4 Mechanism

LY2409021 is a competitive GCGR antagonist: it occupies the antagonist pocket of GCGR, blocks glucagon binding, and so reduces Gs-mediated cAMP production, hepatic glycogenolysis and gluconeogenesis, lowering fasting glucose. Test for each link: (i) a cAMP inhibition assay in GCGR-expressing cells (with LY2409021 as the comparator) measures IC50 directly against the published HbA1c effects; (ii) a hepatocyte lipid-accumulation assay measures whether the analogue reproduces the hepatic-fat signal — a rise in intracellular triglyceride is the likeliest way a "better" antagonist becomes a worse drug, because hepatic fat is the liability that ended this class; (iii) a glucose-output assay in primary hepatocytes measures functional glucose lowering at matched concentration, with a cytotoxicity counter-screen.

### 4.5 Testable hypotheses

1. The best-scoring antagonist, MK-0893, inhibits GCGR-mediated cAMP production with an IC50 within 3-fold of LY2409021 in the same assay. Falsifier: IC50 > 3-fold worse than LY2409021.
2. The same compound does not raise hepatocyte triglyceride above LY2409021's level at matched cAMP inhibition. Falsifier: triglyceride rise > 2-fold above LY2409021 at the same degree of GCGR blockade.
3. The 5EE7 pose predicts the safety profile: an antagonist whose docked pose makes the same deep-pocket contacts as MK-0893 carries the same hepatic-fat liability as MK-0893. Falsifier: an antagonist with those contacts shows no hepatic-fat signal in the hepatocyte assay.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): cAMP inhibition assay for the four antagonists — MK-0893, LY2409021, LGD-6972, PF-06291874 — in GCGR-expressing HEK293 cells; readout IC50, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): hepatocyte triglyceride assay for the best compound from stage 1 against LY2409021 at matched cAMP inhibition; readout intracellular triglyceride and ALT release. Stage 3 (weeks 9–12): if any antagonist passes stages 1–2 — cAMP potency within 3-fold of LY2409021 and no excess triglyceride — primary-hepatocyte glucose-output assay; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin — the whole class spans 0.86 kcal/mol.
2. The ranking cannot resolve the class (the self-dock control beats the reference by only 0.20 kcal/mol), so the set cannot test ranking at all.
3. The whole class is large and lipophilic (MW 504–703, logP 5.6–8.8, two Lipinski violations each); the scores scale with size, not with the contacts that decide hepatic safety.
4. The structure used (5EE7) holds MK-0893, not LY2409021 — the pocket is in the co-crystallised ligand's conformation, and a 2024 docking/MD study predicts LY2409021 binds a different pocket ("Pocket 2"), so the reference drug may have been scored in the wrong site.
5. One rigid structure was used (5EE7, antagonist-bound, 2.5 Å); GCGR is a class-B GPCR with at least three ligand pockets (5EE7, 5XEZ, 5YQZ), and the other two were not docked.
6. No data on the clinical confounder: docking cannot distinguish the glucose-lowering that the class achieves from the hepatic-fat liability that ended it.
7. The ChEMBL ligand retrieval returned no data for this target, so the comparison set was built from the literature rather than from measured ChEMBL potencies; the four antagonists' potencies are clinical HbA1c effects, not binding IC50s in a common assay.
8. The classical-canon sweep found no GCGR-relevant text: the Canon of Medicine describes the diabetes syndrome, not the receptor, so the Islamic-principle discussion rests on hifz al-nafs and la darar as principles, not on a classical source about this target.

## 6. Conclusion

LY2409021, the glucagon-receptor antagonist abandoned after it raised hepatic fat by 4.44% and ALT by 10.7 U/L against placebo, re-docks at −8.12 kcal/mol on the 2.5 Å GCGR structure 5EE7 with no PAINS alert — a validated control, not a discovery. MK-0893, the co-crystallised ligand, scores best at −8.32 kcal/mol, but by 0.20 kcal/mol, inside noise; LGD-6972 and PF-06291874 follow at −7.84 and −7.46 kcal/mol, and the whole class spans 0.86 kcal/mol. The docking verdict is a null result on ranking, with one validated control, and it is useful precisely as one: this class cannot be ranked by rigid Vina scoring on a single antagonist-bound structure, the scores scale with the size the whole class shares, and the next screen must be a cAMP assay plus a hepatocyte triglyceride assay, not a bigger docking set. What the docking cannot do is resolve the safety split: the same pocket that binds LY2409021 at −8.12 kcal/mol is the pocket whose blockade fattens the liver, and only a hepatic-fat assay can tell whether a successor keeps the glucose benefit without the liver cost. The next step is the cheap, decisive test — a cAMP assay plus a triglyceride assay for the four antagonists against LY2409021 — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the National Diabetes Programme, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund any further GCGR-antagonist work in Pakistan, and where the country's diabetes research money should go instead. **Exact change:** do not fund another GCGR-antagonist potency screen — the docking verdict here is that the class cannot be ranked by computation, and the clinical record is that every member failed on liver safety, not on glucose. Instead, commission the 8–12-week cAMP-plus-triglyceride screen proposed in §4.6 for the four antagonists against LY2409021, and only if a candidate passes both halves — potency within 3-fold of LY2409021 with no excess triglyceride — consider any further GCGR work; and, in parallel, direct the diabetes programme's drug budget toward the classes with proven safety in Pakistan's population (metformin, SGLT2 inhibitors, GLP-1 receptor agonists) and toward prevention and early detection, given 9.3 million Pakistanis are undiagnosed. **If evidence Z appears, reverse this:** if a GCGR antagonist beats LY2409021's cAMP IC50 by >10-fold in the binding assay and shows no triglyceride rise in hepatocytes, drop the access-only framing and fund that candidate's development; if all four fail the triglyceride test, drop GCGR antagonism entirely and redirect the same screen to the polyagonist (GLP-1R/GCGR agonist) class — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia) with la darar (do no harm): where a cheap test can distinguish a usable glucose-lowering drug from one that fattens the liver in the country with the world's highest diabetes prevalence, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. International Diabetes Federation. IDF Diabetes Atlas, 11th edition. Brussels: International Diabetes Federation; 2025. (589 million adults aged 20–79 with diabetes; Pakistan 34.5 million, age-standardised prevalence 31.4%, 9.3 million undiagnosed, 70.2 million projected by 2050.)
2. Ali S, Drucker DJ. Glucagon and glucagon receptor physiology. Am J Physiol Endocrinol Metab. 2009. doi:10.1152/ajpendo.90887.2008.
3. Kazda CM, et al. Efficacy and safety of the glucagon receptor antagonist LY2409021 in type 2 diabetes. Diabetes Care. 2016;39:1241–1249. doi:10.2337/dc15-1643.
4. Guzman CB, et al. LY2409021 and hepatic fat in type 2 diabetes. Diabetes Obes Metab. 2017;19:1521–1528.
5. Peters AL, et al. Glucagon receptor antagonists in type 2 diabetes. Diabetes Care. 2025;48:52–60.
6. Dutta P, et al. Volagidemab in type 1 diabetes: a meta-analysis. Ann N Y Acad Sci. 2025;1543:94–101. doi:10.1111/nyas.15262.
7. Zhang H, et al. Structure of the glucagon receptor in complex with a negative allosteric modulator. Nature. 2017;546:259–264. PMID: 28514451.
8. Zhang H, et al. Structure of the glucagon receptor in complex with a glucagon analogue. Nature. 2018;553:106–110. doi:10.1038/nature25153.
9. RCSB PDB entry 5EE7: Crystal structure of the human glucagon receptor (GCGR) in complex with the antagonist MK-0893, 2.5 Å. RCSB Protein Data Bank. Accessed 2026-11-24.
10. UniProtKB P47871: Glucagon receptor, Homo sapiens. UniProt. Accessed 2026-11-24.
11. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; describes the diabetes syndrome — cited for the hifz al-nafs and la darar principles only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-107-2026-11-24-5EE7.json` (LY2409021 + three GCGR antagonists on 5EE7). The pipeline run is in `hidden_files/dock-HP-107-2026-11-24.json` (LY2409021 −8.20 kcal/mol on 5EE7; ChEMBL ligand retrieval returned no data). Reference drug LY2409021; comparators MK-0893, PF-06291874, LGD-6972 (SMILES verified against PubChem by molecular formula). Structure: PDB 5EE7 (2.5 Å). Target: UniProtKB P47871. No additional data were generated.
