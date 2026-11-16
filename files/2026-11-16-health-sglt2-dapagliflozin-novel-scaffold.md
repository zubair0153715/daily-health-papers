# Dapagliflozin Re-Docks at −11.00 kcal/mol on Its Own Cryo-EM Structure — but the Screen Ranks the Most Potent Lead Last

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-16 · **Health Papers Agent — Paper #68** (daily 5-paper run)

**Keywords:** SGLT2; dapagliflozin; empagliflozin; diabetic kidney disease; cryo-EM; molecular docking; AutoDock Vina; polyol pathway

---

## Abstract

Dapagliflozin blocks the kidney's sodium-glucose cotransporter 2 (SGLT2) and has transformed diabetic kidney disease and heart failure, but finding a better SGLT2 inhibitor still relies on screens that must first prove they can rank the drugs we already have. We asked whether a standard automated docking pipeline ranks SGLT2 inhibitors by their measured potency. The pipeline (UniProtKB → ChEMBL → PubChem → RDKit → Vina 1.2.7) found no X-ray structure for SGLT2 and skipped docking entirely, so we docked dapagliflozin, four ChEMBL leads and empagliflozin on 8HEZ, the 2.8 angstrom cryo-EM structure of human SGLT2 bound to dapagliflozin itself, with the grid centre verified as the bound dapagliflozin's centroid. Dapagliflozin re-docks at −11.00 kcal/mol; its duplicate ChEMBL record scores −11.61, a 0.61 kcal/mol gap between identical molecules that sets the run's noise floor. The lead CHEMBL3703792 leads at −12.34, empagliflozin scores −12.03, and the LeadForge star lead CHEMBL5288495 scores −11.48 — but the docking rank against the measured potencies is exactly inverted (Spearman rho −1.0, n = 4): the most potent lead (IC50 0.308 nM) scores worst (−9.76) and the least potent (0.551 nM) scores best. The measured band is only 1.8-fold wide, so the inversion is a property of a band too narrow to rank, not a real anti-correlation — and empagliflozin, six times less potent than dapagliflozin (3.1 versus 0.49 nM), still out-scores it by 1.03 kcal/mol. The screen cannot rank SGLT2 inhibitors within this potency band, and the star lead is indistinguishable from dapagliflozin itself (0.48 kcal/mol behind its duplicate record, inside the 0.61 noise floor). The falsifiable next step is a glucose-uptake assay: if the measured IC50 rank does not match the docking rank, docking is not a ranking tool for this target. And the polyol-escape caveat from Paper #3 stands: an SGLT2-only inhibitor, however potent, does not address the sorbitol pathway that damages retina, kidney and nerve.

---

## 1. Introduction

SGLT2 reabsorbs most of the glucose filtered by the kidney, and blocking it spills glucose into the urine, lowers blood glucose, and — through mechanisms that go beyond glucose lowering — protects the kidney and the heart. In Pakistan, where 34.5 million adults live with diabetes at the highest age-standardised prevalence in the world (IDF Diabetes Atlas, 11th edition, 2025), that protection matters: diabetic kidney disease is the leading cause of kidney failure, and the SGLT2 inhibitors are the first drug class in decades to change its course. Dapagliflozin's evidence is the strongest in the class. In DAPA-CKD (4,304 patients with CKD, with or without diabetes), it cut the primary composite — a sustained 50% fall in eGFR, end-stage kidney disease, or death from renal or cardiovascular causes — from 14.5% to 9.2% over a median 2.4 years (hazard ratio 0.61, 95% CI 0.51–0.72; number needed to treat 19), with the kidney composite at HR 0.56 and death at HR 0.69 (Heerspink et al., N Engl J Med 2020;383:1436–1446, doi:10.1056/NEJMoa2024816). In DAPA-HF (4,744 patients with heart failure and reduced ejection fraction), it cut worsening heart failure or cardiovascular death from 21.2% to 16.3% (HR 0.74, 0.65–0.85) (McMurray et al., N Engl J Med 2019;381:1995–2008, doi:10.1056/NEJMoa1911303). The benefit is independent of diabetes status in both trials.

The structural basis arrived only recently. There is no X-ray structure of human SGLT2; the structures are cryo-EM. Niu et al. resolved the human SGLT2–MAP17 complex bound to empagliflozin at 2.95 angstrom (7VSI, Nature 2022;601:280–284) and showed empagliflozin occupying both the sugar-binding site and the external vestibule, locking the transporter in an outward-open conformation. Hiraizumi et al. then resolved the complex with five inhibitors, including dapagliflozin (8HEZ, 2.8 angstrom, Nat Struct Mol Biol 2024;31:159–169), and showed the four synthetic inhibitors binding the outward-facing conformation while phlorizin binds inward-facing. That history creates a precise, testable problem for docking. A pipeline that only accepts X-ray structures finds no structure at all for SGLT2 and skips docking — the correct behaviour for its own rules, and a failure of the rules. And a screen that docks on the cryo-EM structure must first prove it can rank dapagliflozin against empagliflozin and against leads whose measured potencies span less than two-fold.

This paper is SGLT2-only by design (topic HP-006), and it carries the polyol-escape caveat stated in Paper #3 of this series. Blocking SGLT2 lowers blood glucose, but glucose that enters insulin-independent tissues — retina, kidney, nerve — still feeds the polyol pathway: aldose reductase reduces it to sorbitol, consuming NADPH and depleting the glutathione those cells need against oxidative stress, while sorbitol itself cannot cross membranes and draws water in. Paper #3's rationale for a dual aldose-reductase + SGLT2 inhibitor was exactly this escape: an SGLT2-only drug, however potent, does not address polyol-mediated damage. The screen below ranks SGLT2 fit; it says nothing about the polyol pathway, and the paper does not pretend otherwise.

**Hypothesis (falsifiable):** under one standardised Vina protocol on the dapagliflozin-bound cryo-EM structure (8HEZ), the docking rank of the SGLT2 inhibitors will track their measured potencies, and the LeadForge star lead CHEMBL5288495 (IC50 0.35 nM) will out-score dapagliflozin. Falsified if the rank correlation is below 0.5, or if the star lead does not out-score dapagliflozin by more than the duplicate-molecule noise floor.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-16 (web search; PubMed; the daily digest of 2026-11-15, which contained no SGLT2 item). Key sources: Heerspink et al. 2020 (doi:10.1056/NEJMoa2024816) for DAPA-CKD; McMurray et al. 2019 (doi:10.1056/NEJMoa1911303) for DAPA-HF; Niu et al. 2022 (Nature 601:280–284) for 7VSI; Hiraizumi et al. 2024 (Nat Struct Mol Biol 31:159–169, doi:10.1038/s41594-023-01134-0) for 8HEZ; Michel et al. 2015 (Naunyn Schmiedebergs Arch Pharmacol 388:801–816, doi:10.1007/s00210-015-1134-1) for empagliflozin's IC50 of 3.1 nM and its selectivity; and the IDF Diabetes Atlas, 11th edition (2025), for the Pakistan diabetes burden. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Computation

The standard LeadForge pipeline was run with target "Sodium-glucose cotransporter 2" and reference drug dapagliflozin (run_docking.py, RDKit venv). UniProtKB resolved SGLT2 to P31639 (human SLC5A2, 672 amino acids), ChEMBL to target CHEMBL3884 (Sodium/glucose cotransporter 2, single protein, human), which returned 22 bioactivities; the similarity screen kept 22 and the ranking produced 23 leads. The pipeline's structure picker found no experimental structure meeting its criteria (X-ray only, under 3.0 angstrom) and docking was SKIPPED — error `no_pdb_found` — which the task protocol requires the paper to state honestly rather than to work around silently. The pipeline output is `hidden_files/dock-HP-006-2026-11-16.json`.

Because no X-ray structure exists, a control docking was run on 8HEZ, the 2.8 angstrom cryo-EM structure of the human SGLT2–MAP17 complex bound to dapagliflozin (hidden_files/dock_hp006_8hez.py, same Vina defaults: AutoDock Vina 1.2.7, one box of 22.5 angstrom, exhaustiveness 8, best of three poses reported). The centre [66.86, 66.86, 76.15] is from `D._ligand_center` and was verified by computing the HETATM group centroids directly from the PDB file: it is exactly the centroid of the bound dapagliflozin (ligand code LE6, chain A, residue 802, 28 atoms). The other HETATM groups are water molecules, a sodium ion (centroid [76.29, 61.39, 69.96]) and an N-acetylglucosamine (NAG, chain A, residue 801, centroid [60.43, 63.11, 114.25]) — the glycosylation site, far from the inhibitor pocket, and not the centre. Six compounds were docked: the query plus the top four leads, and empagliflozin (SMILES fetched live from PubChem PUG REST by name) as an approved-drug comparison. The query (dapagliflozin, MW 408.88, logP 1.84, TPSA 99.38, zero Lipinski violations, PAINS-clean, highest Tox21 read-across 0.076) carries no ChEMBL activity value in the pipeline output; its ChEMBL record CHEMBL429910 carries IC50 0.49 nM, and other ChEMBL assays for the same target report EC50 1.1 nM and IC50 6.7 nM — the paper quotes the stored value and names the spread. The leads' potencies are the ChEMBL bioactivity values for target CHEMBL3884, quoted as stored (IC50 values; the pipeline output does not record assay conditions, and the paper does not invent them).

### 2.3 PAINS and safety panel

RDKit PAINS filter and the ToxGuard Tox21 kNN read-across panel (12 assays) were applied to every compound, exactly as in Papers #1/#3 and the 2026-11-15 run.

### 2.4 Analysis plan (stated before results)

The analysis plan was fixed before docking: (i) report the 8HEZ docking table with measured SGLT2 potencies from the ChEMBL record and the literature; (ii) treat CHEMBL429910, the ChEMBL record of dapagliflozin itself, as a duplicate-reproducibility check against the query, exactly as Paper #64 did for olaparib; (iii) compute Spearman rank correlation of docking score against measured potency; (iv) declare the screen unable to rank within the band if the correlation is below 0.5 or the duplicate gap exceeds the gaps between distinct compounds. No post-hoc re-ranking was performed; any exploratory observation is labelled as such.

### 2.5 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol. The structure is cryo-EM at 2.8 angstrom, not X-ray, and the docking is rigid: SGLT2 is a transporter that cycles through outward-open, occluded and inward-open states, and a single rigid conformation cannot model that cycle or the sodium-coupled transport step. No compound was assayed. The polyol pathway, the paper's stated caveat, is not modelled here. No cure claims are made.

## 3. Results

### 3.1 The pipeline found no structure — docking was skipped

The pipeline's structure picker accepts X-ray structures under 3.0 angstrom only. Human SGLT2 has no X-ray structure; its experimental structures are cryo-EM (7VSI at 2.95 angstrom, 8HEZ at 2.8 angstrom). The pipeline therefore returned `no_pdb_found` and skipped docking. That is the correct behaviour under its own rules, and it is also a failure of the rules: a pipeline that cannot use cryo-EM structures cannot dock the target that defines the class, and a user who did not read the log would receive a lead ranking with no docking at all. The docking below is the manual control that the pipeline's rules excluded.

### 3.2 Docking on the dapagliflozin-bound cryo-EM structure (8HEZ, 2.8 angstrom)

| Compound | Measured SGLT2 potency | Vina on 8HEZ (kcal/mol) | PAINS |
|---|---|---|---|
| CHEMBL3703792 | IC50 0.551 nM (ChEMBL) | **−12.34** (−12.34, −9.34, −8.78) | clean |
| Empagliflozin | IC50 3.1 nM (literature) | −12.03 (−12.03, −9.74, −9.38) | clean |
| CHEMBL429910 (= dapagliflozin) | IC50 0.49 nM (ChEMBL) | −11.61 (−11.61, −10.07, −8.40) | clean |
| CHEMBL5288495 (star lead) | IC50 0.35 nM (ChEMBL) | −11.48 (−11.48, −9.45, −8.46) | clean |
| Dapagliflozin (QUERY) | IC50 0.49 nM (ChEMBL record); other assays EC50 1.1 nM, IC50 6.7 nM | −11.00 (−11.00, −10.09, −8.42) | clean |
| CHEMBL3703868 | IC50 0.308 nM (ChEMBL) | −9.76 (−9.76, −8.81, −8.49) | clean |

Scores in kcal/mol, best of three poses (all poses in parentheses). All six compounds are PAINS-clean, carry zero Lipinski violations each (MW 408–461, logP 1.13–3.28), and show no decisive Tox21 signal (highest single read-across 0.362 for the star lead, 0.076 for dapagliflozin). Pose spreads are 1.27–3.56 kcal/mol — wider than the converged 6L88 control in Paper #67, tighter than the unconverged 4PF3 run, and moderate enough that the best-pose numbers are usable but not precise.

Three findings matter. First, the duplicate check: dapagliflozin docked twice — once as the query, once as its ChEMBL record CHEMBL429910 — scores −11.00 and −11.61, a 0.61 kcal/mol gap between identical molecules. That is the run's noise floor, and it is larger than the 0.37 gap Paper #64 found for the olaparib duplicate. Any gap smaller than 0.61 between two compounds in this table is indistinguishable from re-docking the same molecule.

Second, the rank is exactly inverted against the measured potencies. The four ChEMBL leads' measured order is CHEMBL3703868 (0.308 nM) > CHEMBL5288495 (0.35) > CHEMBL429910 (0.49) > CHEMBL3703792 (0.551); the docking order is the precise reverse, Spearman rho −1.0 (n = 4). The most potent lead scores worst (−9.76) and the least potent scores best (−12.34), a 2.58 kcal/mol gap across a 1.8-fold potency band. The paper reports the −1.0 and declines to treat it as a real anti-correlation: a 1.8-fold band is narrower than any assay can resolve, and the inversion is what noise looks like when the signal is smaller than the noise. The honest statement is that the screen cannot rank within this band — not that it ranks backwards.

Third, the approved-drug comparison fails the same way Paper #67's did. Empagliflozin (IC50 3.1 nM) is about six times less potent than dapagliflozin (0.49 nM by the stored ChEMBL value), yet it out-scores dapagliflozin by 1.03 kcal/mol (−12.03 versus −11.00). And the star lead CHEMBL5288495 (IC50 0.35 nM) scores −11.48 — 0.48 kcal/mol behind dapagliflozin's duplicate record, inside the 0.61 noise floor, and 0.86 behind the leader. The star lead is indistinguishable from dapagliflozin itself by this screen. The hypothesis is falsified on both counts: the rank correlation is −1.0, not above 0.5, and the star lead does not out-score dapagliflozin by more than the duplicate noise floor.

### 3.3 Comparison with published docking

No published Vina docking score for dapagliflozin on 8HEZ was found to compare against, and the paper does not invent one. The reference point is the structural literature: Niu et al. 2022 showed empagliflozin occupying both the sugar-binding site and the external vestibule of the outward-open transporter (7VSI), and Hiraizumi et al. 2024 showed the four synthetic inhibitors, including dapagliflozin, binding the outward-facing conformation (8HEZ). Our re-dock places dapagliflozin at −11.00 kcal/mol in its own co-crystal pocket with poses of −11.00, −10.09 and −8.42, consistent with re-docking into its own cryo-EM structure. The earlier LeadForge figure for the star lead (−7.03 kcal/mol against dapagliflozin's −4.84) is NOT reproduced here: it came from a different structure and protocol whose grid centre was never verified after the centre-pick bug, and the two numbers are not comparable. The honest comparator is the clinical one: dapagliflozin's kidney and heart-failure benefits (DAPA-CKD HR 0.61; DAPA-HF HR 0.74) and its selectivity (about 1,200-fold over SGLT1; empagliflozin over 2,500-fold) are properties of the drugs in patients and in cells, and no docking score on 8HEZ predicts them.

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say that dapagliflozin re-docks in its own pocket at −11.00 kcal/mol, that the duplicate-molecule noise floor is 0.61 kcal/mol, and that the lead CHEMBL3703792 tops the table at −12.34 — a candidate worth the glucose-uptake assay, not a verdict. It can say that the pipeline's X-ray-only rule excludes the only structures that exist for this target, and that a cryo-EM structure at 2.8 angstrom docks fine once the centre is verified against the bound ligand. It cannot rank SGLT2 inhibitors within a 1.8-fold potency band: the rank is inverted, the star lead is indistinguishable from dapagliflozin, and the weaker approved drug out-scores the stronger one. It cannot say anything about the polyol pathway, which is the paper's stated caveat and the reason Paper #3 proposed a dual inhibitor.

### 4.2 The cryo-EM lesson

The pipeline's structure picker is the finding, not a footnote. It accepts X-ray structures under 3.0 angstrom and nothing else, so for SGLT2 — a target whose structures are all cryo-EM — it silently returns no docking and a lead ranking built on similarity and ADMET alone. Paper #65 found the same pattern for GLP-1R, where the picker chose a 1.80 angstrom extracellular-domain crystal over the 3.1 angstrom cryo-EM structure of the full receptor with the drug bound, and the drug re-docked 3.14 kcal/mol stronger on the cryo-EM structure. The lesson generalises: the picker's resolution filter is a proxy for quality, and for membrane proteins — transporters, GPCRs — the best structure is often the cryo-EM one the filter excludes. The fix is to let the picker accept cryo-EM structures and to verify the centre against the bound ligand, as this paper did; the fix is stated here as a pipeline change, not implemented in this run.

### 4.3 The polyol-escape caveat, restated

An SGLT2-only inhibitor lowers blood glucose by spilling it into the urine, but the glucose that reaches insulin-independent tissues still enters the polyol pathway, where aldose reductase reduces it to sorbitol at the cost of NADPH, depleting glutathione and drawing water into cells that cannot export sorbitol. That is the damage mechanism in retina, kidney and nerve, and it is not addressed by a better SGLT2 score. Paper #3's dual aldose-reductase + SGLT2 rationale stands: the next screen in this series should dock against both targets and require a lead to score on both, or the programme should say plainly that it is optimising glucose lowering and kidney protection, not the polyol damage. This paper optimises the former and states the limit.

### 4.4 Testable hypotheses

1. **Potency hypothesis.** In a glucose-uptake assay in SGLT2-expressing cells, the measured IC50 rank of the docked set reproduces the 8HEZ docking rank. Falsified if the rank correlation is below 0.5 — in which case docking is not a ranking tool for this target, and the programme should screen by uptake assay directly.
2. **Selectivity hypothesis.** The best lead CHEMBL3703792 is at least 1,000-fold selective for SGLT2 over SGLT1 in the same assay, matching dapagliflozin's profile. Falsified if selectivity is below 100-fold — in which case the lead risks the gastrointestinal effects of SGLT1 blockade, whatever its SGLT2 score.
3. **Polyol hypothesis.** In a diabetic rat model, the best lead plus an aldose-reductase inhibitor reduces retinal sorbitol more than the lead alone, at the same glucose lowering. Falsified if the combination adds nothing — in which case Paper #3's dual rationale does not hold in vivo, and the SGLT2-only path is sufficient for that endpoint.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): glucose-uptake (AMG) assay in SGLT2- and SGLT1-expressing cells for the docked set plus dapagliflozin and empagliflozin as controls; report IC50 with 95% CI and the SGLT2/SGLT1 selectivity ratio. Stage 2 (weeks 4–6): aldose-reductase inhibition assay for the best lead, to test the dual-inhibition rationale directly. Stage 3 (weeks 7–10): urinary glucose excretion and kidney sorbitol in a diabetic rat model for the best lead versus dapagliflozin, with and without an aldose-reductase inhibitor. Stage 4 (weeks 11–12): hERG and CYP inhibition screen for the lead. Success criterion: the lead matches dapagliflozin's glucose lowering with at least 1,000-fold SGLT2 selectivity — not merely a better docking score.

## 5. Limitations

1. Docking only; no experimental data in this paper. Vina noise (±1–2 kcal/mol) is larger than several of the gaps reported, and the duplicate-molecule gap (0.61 kcal/mol) is the measured noise floor for this run.
2. A single rigid cryo-EM conformation: SGLT2 cycles through outward-open, occluded and inward-open states, and rigid docking cannot model that cycle or the sodium-coupled transport step; no MD or free-energy refinement was run.
3. The measured potency band is 1.8-fold wide (0.308–0.551 nM), narrower than any assay can resolve; the −1.0 rank correlation is a property of that band, not evidence of anti-correlation.
4. Measured potencies mix ChEMBL bioactivities and literature IC50 values from different assays; dapagliflozin itself is reported as 0.49 nM (stored ChEMBL IC50), 1.1 nM (EC50) and 6.7 nM (IC50) in different assays.
5. The polyol pathway is stated as a caveat, not modelled; no aldose-reductase docking or assay is in this paper.
6. The Islamic canon sweep covers the available digitised canon relevant to the question (Ibn Sina, *Al-Qanun fi al-Tibb*, c. 1025; Al-Razi, *Kitab al-Hawi*, c. 900); the full 23 volumes of *Kitab al-Hawi* exist in English only in selections, and many classical Arabic manuscripts remain undigitised — the sweep names this gap rather than claiming completeness.
7. No Pakistan-specific data on SGLT2 inhibitor prices, availability, or kidney-monitoring capacity are reported here; the burden numbers are national diabetes estimates (IDF Diabetes Atlas 2025).

## 6. Conclusion

Dapagliflozin re-docks at −11.00 kcal/mol in its own cryo-EM pocket (8HEZ), but the screen cannot rank SGLT2 inhibitors: the docking rank against measured potency is exactly inverted (rho −1.0, n = 4) across a 1.8-fold band too narrow to rank, the star lead CHEMBL5288495 (−11.48) is indistinguishable from dapagliflozin itself (0.48 kcal/mol behind its duplicate record, inside the 0.61 noise floor), and empagliflozin — six times less potent — out-scores dapagliflozin by 1.03 kcal/mol. The pipeline's X-ray-only rule skipped docking entirely for this target, because the only SGLT2 structures are cryo-EM; the manual control on 8HEZ, with its centre verified against the bound dapagliflozin, is what produced the numbers. And the polyol-escape caveat from Paper #3 stands: an SGLT2-only inhibitor, however potent, does not address the sorbitol pathway that damages retina, kidney and nerve.

## 7. Policy implications

**Decision-maker:** the Drug Regulatory Authority of Pakistan (DRAP) and the provincial health departments, with the Pakistan Society of Nephrology and the Pakistan Endocrine Society as clinical advisers. **Decision:** whether to add an SGLT2 inhibitor to the public formulary for diabetic kidney disease and heart failure, and at what price. **Recommendation:** add dapagliflozin (or a generic equivalent when available) to the formulary for patients with diabetic kidney disease or heart failure with reduced ejection fraction, on the DAPA-CKD and DAPA-HF evidence — the kidney composite fell by 39% and the heart-failure composite by 26%, with benefits independent of diabetes status — and pair the listing with urine albumin-to-creatinine testing in diabetes clinics, since the indication cannot be applied where albuminuria is never measured. **Falsifier / reversal:** if the negotiated price exceeds the per-patient cost of the current standard pathway without a measured kidney- or heart-failure-outcome gain, or if albuminuria testing coverage cannot be demonstrated in the prescribing facilities, reverse the formulary recommendation and keep the drug in the private market only. The principle is *hifz al-nafs* (preservation of life) with *maslaha* (public benefit) as the weighing rule, in the tradition of Ibn Sina's *Al-Qanun fi al-Tibb* (c. 1025): a health system preserves life by buying the drug whose benefit is proven in the patients who need it, and by building the testing that finds those patients — treatment and diagnosis together, not one without the other.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Heerspink HJL, Stefansson BV, Correa-Rotter R, et al. Dapagliflozin in patients with chronic kidney disease. N Engl J Med. 2020;383(15):1436–1446. doi:10.1056/NEJMoa2024816.
2. McMurray JJV, Solomon SD, Inzucchi SE, et al. Dapagliflozin in patients with heart failure and reduced ejection fraction. N Engl J Med. 2019;381(21):1995–2008. doi:10.1056/NEJMoa1911303.
3. Niu Y, Liu R, Guan C, et al. Structural basis of inhibition of the human SGLT2-MAP17 glucose transporter. Nature. 2022;601:280–284. doi:10.1038/s41586-021-04212-9. (PDB 7VSI.)
4. Hiraizumi M, Akashi T, Murasaki K, et al. Transport and inhibition mechanism of the human SGLT2-MAP17 glucose transporter. Nat Struct Mol Biol. 2024;31:159–169. PMID 38057552. doi:10.1038/s41594-023-01134-0. (PDB 8HEZ.)
5. Grempler R, Thomas L, Eckhardt M, et al. Empagliflozin, a novel selective sodium glucose cotransporter-2 (SGLT-2) inhibitor: characterisation and comparison with other SGLT-2 inhibitors. Diabetes Obes Metab. 2012;14(1):83–90. (Empagliflozin SGLT2 IC50 3.1 nM; selectivity over SGLT1.)
6. Michel MC, Mayoux E, Vallon V. A comprehensive review of the pharmacodynamics of the SGLT2 inhibitor empagliflozin in animals and humans. Naunyn Schmiedebergs Arch Pharmacol. 2015;388(8):801–816. PMID 26108304. doi:10.1007/s00210-015-1134-1. (Empagliflozin SGLT2 IC50 3.1 nM, from Grempler et al. 2012, ref. 5.)
7. International Diabetes Federation. IDF Diabetes Atlas. 11th edition. 2025. Pakistan: 34.5 million adults (20–79) with diabetes in 2024; age-standardised prevalence 31.4%.
8. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. Book I (preservation of health). Cited as the classical source for the policy principle; the full Arabic text was not read in this run — see Limitations.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-006-8hez-2026-11-16.json` (8HEZ control docking; the pipeline run that skipped docking is `hidden_files/dock-HP-006-2026-11-16.json`); the control script is `hidden_files/dock_hp006_8hez.py`. No additional data were generated. ChEMBL target CHEMBL3884 (SGLT2); UniProt P31639; PDB 8HEZ (2.8 angstrom cryo-EM, dapagliflozin-bound, ligand LE6); grid centre [66.86, 66.86, 76.15], verified as the bound dapagliflozin centroid. The manuscript source is `files/2026-11-16-health-sglt2-dapagliflozin-novel-scaffold.md`.
