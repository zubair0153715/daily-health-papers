# One Molecule, Two Bottlenecks: A Predicted Dual Aldose-Reductase / SGLT2 Inhibitor and the Case for Closing the Polyol Escape Route in Diabetes

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2 November 2026 · **Paper #3 — Health track, extra** (Daily Research Papers)

**Keywords:** dual inhibitor; aldose reductase; SGLT2; polyol pathway; diabetic complications; thymoquinone; CHEMBL5288495; molecular docking

---

## Abstract

SGLT2 inhibitors are the most successful modern therapy for diabetic kidney and cardiovascular disease, yet residual risk remains: complications still progress in many treated patients. Aldose reductase (AR) inhibitors, the drugs that block the polyol pathway driving diabetic neuropathy, retinopathy and cataract, failed clinically — but a 2023 mechanistic review reports a fact that reframes both classes: when renal SGLT2 is inhibited, downstream SGLT1 transports glucose at a higher frequency and **activates the aldose reductase gene**, producing sorbitol and fructose that damage the tubule. SGLT2 inhibition may therefore open a polyol escape route even as it lowers glucose. We tested, by standardised AutoDock Vina docking, whether either of two known leads already hits both targets. The SGLT2 lead CHEMBL5288495 (measured SGLT2 IC50 0.35 nM; docked −7.03 kcal/mol on 7VSI) docked to aldose reductase (PDB 1US0) at **−9.56 kcal/mol** — 3.09 kcal/mol better than the AR reference drug epalrestat (−6.47), consistent across all three top poses, and PAINS-clean. Thymoquinone docked to both targets as well (AR −7.28; SGLT2 −6.98, outscoring dapagliflozin −4.79 in-run), but carries a PAINS alert. No published paper has reported dual AR/SGLT2 activity for any molecule, and no head-to-head AR-inhibitor versus SGLT2-inhibitor trial exists. We propose two falsifiable steps: (1) an in-vitro AR inhibition assay of CHEMBL5288495 and its novel analogs, and (2) a combination trial design (SGLT2 inhibitor + AR inhibitor) in patients with residual albuminuria or neuropathy despite SGLT2 therapy. The honest counterpoint is stated in full: in the ARISE-HF trial of the AR inhibitor AT-001, the benefit signal appeared in the subgroup **not** receiving SGLT2 inhibitors — so the combination is a hypothesis to test, not a conclusion.

---

## 1. Introduction

Type 2 diabetes now affects roughly 1 in 3 adults in Pakistan and over 500 million people worldwide, and its complications — kidney failure, heart failure, neuropathy, retinopathy, cataract — are the main source of its morbidity. Two drug classes attack two different bottlenecks. SGLT2 inhibitors block renal glucose reabsorption and have transformed cardiorenal outcomes. Aldose reductase (AR) inhibitors block the first, rate-limiting enzyme of the polyol pathway, which converts excess glucose to sorbitol and drives osmotic and oxidative injury in nerve, retina, lens and kidney. The first class succeeded; the second largely failed in the clinic, with the most recent large trial (ARISE-HF, AT-001, 2024) missing its primary endpoint.

These two stories are usually told separately. A 2023 mechanistic review of SGLT1, SGLT2 and dual inhibitors (Azizogli et al.) contains a sentence that connects them: when renal SGLT2 is inhibited, downstream renal SGLT1 "facilitates the transport of glucose at a higher frequency and activates the aldose reductase gene, making sorbitol and fructose. Fructose gets metabolized through fructokinase and leads to uric acid synthesis, oxidative stress, and cytokine inflammation, damaging the tubule." If that mechanism operates in patients, then SGLT2 inhibition — the standard of care — may itself upregulate the very enzyme AR inhibitors are meant to block, leaving a polyol escape route open behind the drug's benefit. That is a testable claim, and it reframes the AR inhibitor not as a failed monotherapy but as the missing second half of SGLT2 therapy.

This paper asks the narrowest version of that question: does any molecule already known as an SGLT2 inhibitor also inhibit aldose reductase? We cross-docked two leads against both targets under one protocol — the SGLT2 lead CHEMBL5288495 from our own LeadForge pipeline (measured IC50 0.35 nM) and thymoquinone, the black-seed quinone that outscored epalrestat on AR in our companion paper — and report the first dual AR/SGLT2 docking evidence for either molecule.

## 2. Methods

### 2.1 Literature basis and novelty check

We searched for prior dual AR/SGLT2 work (web and PubMed, 2 November 2026): "dual aldose reductase SGLT2 inhibitor", "thymoquinone SGLT2", and related terms. The nearest items found were (i) a 2023 comparison review of SGLT1/SGLT2/dual inhibitors (Azizogli et al.), (ii) a 2026 technical comparison of AR inhibitors versus SGLT2 inhibitors noting that **no head-to-head clinical trial of the two classes exists**, and (iii) a dual PTP1B + aldose-reductase flavonoid study — a different target pair. No paper reporting a dual AR/SGLT2 inhibitor, and no AR-inhibitor + SGLT2-inhibitor combination trial, was found.

### 2.2 Molecular docking

Docking used AutoDock Vina 1.2.7 with the LeadForge protocol, identical for every ligand in a run (same structure, same grid, same exhaustiveness 8, box 22.5 Å). Aldose reductase: PDB 1US0 (0.66 Å), centre [21.26, −6.13, 27.39]. SGLT2: PDB 7VSI (human SGLT2–MAP17 + empagliflozin, cryo-EM 2.95 Å), centre [46.73, 36.59, 40.54] — the SGLT2 pipeline uses direct Vina calls for 7VSI because the standard UniProt lookup admits X-ray structures only and all SGLT2 structures are cryo-EM. Vina's scoring noise is approximately ±1–2 kcal/mol; differences below this are not treated as significant. Affinities are the best of three poses; all three poses are reported.

### 2.3 Controls and a control failure, honestly reported

An initial SGLT2 run used flat connectivity SMILES (no stereochemistry) for dapagliflozin and produced an absurd control score (−2.76 for a nanomolar drug) and dropped epalrestat entirely from the AR run. Both controls were re-run with proper isomeric SMILES from PubChem, which restored them to their known values (dapagliflozin −4.79, matching the −4.84 of the earlier diabetes run; epalrestat −6.47, matching the −6.48 of the companion paper). Only the corrected, control-verified numbers are used in this paper. Thymoquinone's SGLT2 score was replicated in both runs (−6.95, then −6.98).

### 2.4 Honesty limits

Docking affinity is not enzyme inhibition and not efficacy. A docking "win" is triage: it tells the laboratory which assay to run first. No wet-lab data are presented. No clinical claim is made.

## 3. Results

### 3.1 The SGLT2 lead is a predicted aldose-reductase inhibitor — stronger than the AR reference drug

| Ligand | Aldose reductase, 1US0 (kcal/mol) | Poses | Verdict |
|---|---|---|---|
| **CHEMBL5288495 (SGLT2 lead)** | **−9.56** | −9.56 / −9.13 / −7.58 | **3.09 better than epalrestat** |
| Thymoquinone | −7.28 | −7.28 / −7.24 / −7.13 | Beats epalrestat (see companion paper) |
| Epalrestat (ref) | −6.47 | −6.47 / −6.35 / −6.11 | Reference |

CHEMBL5288495 — a fluorinated dapagliflozin analog with measured SGLT2 IC50 0.35 nM and prior SGLT2 docking −7.03 — docked to aldose reductase at −9.56 kcal/mol. The margin over epalrestat (3.09 kcal/mol) exceeds Vina's ±1–2 kcal/mol noise, and all three top poses beat epalrestat's best pose. The molecule is PAINS-clean (per the LeadForge ADMET screen) and Lipinski-compliant. A structural rationale, not yet proof: AR's natural substrate is glucose, and CHEMBL5288495 carries a C-glycoside sugar moiety that plausibly occupies the sugar-binding pocket — the same pocket epalrestat binds. Pose-level interaction analysis and molecular dynamics are the required next step, not an assumption made here.

### 3.2 Thymoquinone hits both targets — moderately, and with a caveat

| Ligand | SGLT2, 7VSI (kcal/mol) | Poses | Verdict |
|---|---|---|---|
| Thymoquinone | −6.98 | −6.98 / −6.85 / −5.87 | Outscores dapagliflozin in-run |
| Dapagliflozin (ref) | −4.79 | −4.79 / −2.64 / −2.63 | Reference (replicates −4.84) |
| CHEMBL5288495 (prior run) | −7.03 | — | Prior SGLT2 docking |

Thymoquinone docked to SGLT2 at −6.98 kcal/mol, 2.19 kcal/mol better than dapagliflozin in the same run — at the edge of Vina's noise, but consistent across poses (even its worst pose, −5.87, beats dapagliflozin's best). Combined with its AR score (−7.28), TQ is a predicted dual inhibitor of both targets, though weaker than CHEMBL5288495 on AR and carrying a PAINS alert (quinone redox cycler) that the SGLT2 lead does not. TQ's dual activity is therefore a secondary lead; CHEMBL5288495 is the primary one.

### 3.3 The novelty statement, precisely bounded

To our knowledge, no published paper reports dual aldose-reductase/SGLT2 activity for any molecule, and no trial has combined the two classes. The nearest precedents are dual inhibitors of *other* pairs (e.g. PTP1B + AR flavonoids) and a comparison review that explicitly notes the absence of head-to-head AR-versus-SGLT2 trials. This paper's claim is correspondingly narrow: a computational dual-activity signal for one specific molecule, plus a mechanistic rationale and a falsifiable assay plan — not a drug, and not a clinical recommendation.

## 4. Discussion

### 4.1 The polyol escape-route hypothesis

The mechanism reported by Azizogli et al. — SGLT2 inhibition → increased downstream SGLT1 glucose transport → aldose-reductase gene activation → sorbitol/fructose → uric acid, oxidative stress, cytokine inflammation, tubular damage — predicts a specific, measurable consequence: markers of polyol flux (erythrocyte sorbitol, urinary fructose, AR expression) should rise, not fall, in some patients after SGLT2 inhibitor initiation, and that rise should track residual renal risk. If confirmed, it explains part of the residual risk on SGLT2 therapy and identifies the patients in whom adding AR inhibition should help most. If refuted — if polyol markers fall on SGLT2 therapy — the hypothesis dies cleanly and cheaply.

### 4.2 The counterpoint that must not be hidden

The ARISE-HF trial (AT-001, n = 691, 15 months, JACC 2024) missed its primary endpoint (peak VO2). The only benefit signal appeared in a prespecified subgroup: patients **not** receiving SGLT2 inhibitors or GLP-1 RAs at baseline (+0.62 mL/kg/min peak VO2, p = .04; interaction p = .10). Read plainly, that subgroup result cuts *against* the combination: AR inhibition seemed to help precisely where SGLT2 inhibition was absent. Three readings are possible — (i) the subgroup is noise (interaction not significant), (ii) SGLT2 therapy already captures the benefit AR inhibition would add, or (iii) the combination was never actually tested (no patient received both drugs by design, and the subgroup is an absence, not a comparison). Only a trial that randomises the combination can distinguish them. This paper proposes that trial; it does not assume its outcome.

### 4.3 Two falsifiable steps

**Step 1 — enzyme confirmation (8–12 weeks, university lab).** In-vitro AR inhibition (IC50) of CHEMBL5288495 and its five novel analogs (best: A:Me/CH2/Cl, docked −8.19 on SGLT2), with epalrestat as control, plus SGLT2 inhibition (IC50) of thymoquinone. Confirmation = AR IC50 in a plausible range for CHEMBL5288495 with the effect surviving redox controls; refutation = no AR inhibition at ≤10 µM, or an effect that vanishes under redox/detergent controls. **Step 2 — combination trial design.** A randomised trial of SGLT2 inhibitor + AR inhibitor versus SGLT2 inhibitor alone in type 2 diabetes with residual albuminuria or neuropathy despite SGLT2 therapy, with polyol-flux markers (erythrocyte sorbitol, urinary fructose) as the mechanistic readout and albuminuria/neuropathy scores as clinical endpoints. The falsifiable prediction: the combination lowers polyol markers more than SGLT2 alone; if it does not, the escape-route hypothesis is wrong.

### 4.4 Why this matters in Pakistan specifically

Pakistan carries ~34.5 million adults with diabetes (~30.8% prevalence), and SGLT2 inhibitors are increasingly prescribed while AR inhibitors are essentially absent from practice. If the escape-route mechanism holds, the cheapest second step is not a new patented drug but the pairing of an existing SGLT2 inhibitor with a low-cost AR inhibitor — and the dual-activity signal for CHEMBL5288495 suggests the field should also look for single molecules that do both jobs, starting with the analogs already designed in our pipeline.

## 5. Limitations

1. Docking only; no experimental data. 2. The AR margin for CHEMBL5288495 exceeds Vina noise, but a large ligand can score highly from contact count alone — pose inspection and dynamics are required. 3. TQ's SGLT2 margin (2.19 kcal/mol) sits at the noise edge. 4. Dapagliflozin scored −7.23 in the analogs run versus −4.84/−4.79 in two other runs — Vina run-to-run variability is real; only within-run comparisons are used here. 5. The SGLT2→AR activation mechanism rests on a single review's report; it needs direct experimental confirmation. 6. No Pakistani-market or population-specific data are presented.

## 6. Conclusion

One molecule built to block SGLT2 is predicted to block aldose reductase even more strongly than the AR reference drug — and the literature supplies a mechanism (SGLT2 inhibition activating the AR gene via SGLT1) that makes that dual activity therapeutically interesting rather than merely curious. The claim is narrow, the assay that settles it is cheap, and the trial that tests the combination is the obvious next step. If the assay refutes the docking, the field learns that a −9.56 Vina score can mislead; if it confirms it, the cheapest path to closing residual diabetic risk may already be sitting in the SGLT2 pipeline.

---

## Acknowledgments

**AI assistance:** This manuscript was drafted with the assistance of an AI research assistant (Lapis, Meta Muse Spark), which also performed the literature searches and docking computations. The author takes responsibility for the content.

## References

1. Azizogli AR, Vitti MR, Mishra R, Osorno L, Heffernan C, Kumar VA. Comparison of SGLT1, SGLT2, and Dual Inhibitor biological activity in treating Type 2 Diabetes Mellitus. *Adv Ther (Weinh).* 2023;6(12):2300143. doi:10.1002/adtp.202300143. PMID: 38223846; PMCID: PMC10783160. (SGLT2 inhibition → SGLT1 → aldose-reductase gene activation.)
2. Januzzi JL, Butler J, del Prato S, Ezekowitz J, Ibrahim N, et al. Randomized Trial of a Selective Aldose Reductase Inhibitor in Patients With Diabetic Cardiomyopathy (ARISE-HF). *J Am Coll Cardiol.* 2024;84(2):137–148. doi:10.1016/j.jacc.2024.03.380. (AT-001 missed primary endpoint; subgroup not on SGLT2i/GLP-1RA +0.62 mL/kg/min, p = .04.)
3. A Tale of Two Targets: Aldose Reductase Inhibitors vs. SGLT2 Inhibitors in Diabetic Complications. BenchChem Technical Support Team, April 2026. (Technical comparison; notes no head-to-head AR-vs-SGLT2 trials exist.)
4. Sarkar C, Jamaddar S, Islam T, Mondal M, Islam MT, Mubarak MS. Therapeutic perspectives of the black cumin component thymoquinone: A review. *Food Funct.* 2021;12(14):6167–6213. (Thymoquinone background.)
5. Potential of Flavonoids from *Orthosiphon stamineus* as Antidiabetic Candidates through Inhibition of PTP1B and Aldose Reductase. *J Farmasi dan Ilmu Kefarmasian Indonesia.* doi:10.35451/jfm.v7i2.2654. (Nearest precedent: dual inhibition of a different pair, PTP1B + AR.)
6. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0. *J Chem Inf Model.* 2021;61(8):3891–3898.
7. Baell JB, Holloway GA. New substructure filters for removal of pan assay interference compounds (PAINS) from screening libraries. *J Med Chem.* 2010;53(7):2719–2740.
8. RCSB Protein Data Bank entries 1US0 (aldose reductase) and 7VSI (human SGLT2–MAP17 + empagliflozin). https://www.rcsb.org/
9. Ali Z, et al. Thymoquinone as a Putative Aldose Reductase Inhibitor for Diabetic Complications (Paper #1, Daily Research Papers, 2 November 2026). Internal manuscript. (TQ docking table; PAINS analysis; market variance.)
10. LeadForge AI. SGLT2 novel analogs — design, docking and ADMET (7 October 2026). Internal report. (CHEMBL5288495: SGLT2 IC50 0.35 nM, docking −7.03 on 7VSI; 5 novel analogs, best A:Me/CH2/Cl −8.19; dapagliflozin run-to-run variability noted.)

## Data availability

Cross-docking inputs, scripts and raw results: `~/workspace/research-agents/runs/dual-ar-sglt2-2026-11-02/` (cross_dock.py, sglt2_direct.py, controls_rerun.py; cross_dock_results.json, sglt2_direct_results.json, controls_rerun_results.json). AutoDock Vina 1.2.7, LeadForge protocol, 2 November 2026. SMILES: thymoquinone, CHEMBL5288495, dapagliflozin and epalrestat (isomeric, PubChem). No new experimental data are presented in this draft.
