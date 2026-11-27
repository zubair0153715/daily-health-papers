# Pemigatinib Leads Erdafitinib by 1.53 kcal/mol on FGFR1 — but Erdafitinib Ranks Last on Its Own Structure and No Compound Beats It Beyond Noise

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-26 · **Health Papers Agent — Paper #121** (daily 5-paper run)

**Keywords:** FGFR1; erdafitinib; pemigatinib; kinase inhibitor; molecular docking; AutoDock Vina; lung cancer; Pakistan

---

## Abstract

FGFR1 amplification occurs in 10–25% of squamous cell lung carcinomas and about 10% of estrogen-receptor-positive breast cancers, yet erdafitinib — the pan-FGFR inhibitor approved for FGFR2/3 disease — was never tested against FGFR1 in a head-to-head binding comparison with its own analogues. Five compounds — erdafitinib, three ChEMBL FGFR1 inhibitors (CHEMBL3980069, CHEMBL5182360, CHEMBL5799893) and the clinical FGFR inhibitor pemigatinib — were docked with standardised AutoDock Vina on the 1.63 Å erdafitinib-bound FGFR1 structure 5EW8, same box and exhaustiveness, with erdafitinib as the self-dock control. Pemigatinib scored best at −10.53 kcal/mol, 1.53 kcal/mol better than erdafitinib at −9.00, but that lead is inside Vina's ±1–2 kcal/mol noise, so no compound beats erdafitinib beyond noise. The method then failed its own control: erdafitinib — the co-crystallised ligand — scored worst of the five on its own structure, and the most potent ChEMBL compound by published IC50 (CHEMBL5182360, 0.28 nM) ranked fourth. Docking therefore cannot rank FGFR1 inhibitors on this structure, and no drug programme follows from these scores. Pose consistency was tight for two compounds and not for two: CHEMBL3980069 and CHEMBL5182360 converged on the same binding mode three times, while CHEMBL5799893's second place rests on a single pose, its other two poses being a full kcal/mol worse, so its honest score is about −8.9, below erdafitinib. The falsifier is a kinase inhibition assay: if pemigatinib's FGFR1 IC50 is not better than erdafitinib's 1.2 nM on the same plate, the docking lead is a pocket artefact.

---

## 1. Introduction

FGFR1 amplification is one of the most frequent potentially targetable alterations in squamous cell lung carcinoma — 10–25% of cases — and occurs in ~10% of estrogen-receptor-positive breast cancers, where it drives endocrine therapy resistance (Weiss et al., Sci Transl Med 2010;2:62ra93; Turner et al., Cancer Res 2010;70:2085). Across all solid tumours tested by next-generation sequencing, FGFR1 alterations (predominantly amplification) are found in 3.5% (Clin Cancer Res 2016;22:259). Erdafitinib (Balversa), a pan-FGFR tyrosine kinase inhibitor, was the first agent to win FDA approval for an FGFR-dysregulated cancer — April 2019, for locally advanced or metastatic urothelial carcinoma with susceptible FGFR3/FGFR2 alterations (Loriot et al., N Engl J Med 2019;381:338–348, PMID 31340094) — with FGFR1–4 IC50s of 1.2, 2.5, 3 and 5.7 nM and Kd 0.24–2.2 nM. Its dose-limiting toxicity is on-target: hyperphosphataemia from inhibition of renal FGF23/klotho-mediated phosphate wasting occurred in 75.9% of patients. The gap this paper attacks is FGFR1 itself: erdafitinib was developed and approved on FGFR2/3 disease, its FGFR1 potency is the best of the four isoforms on paper (1.2 nM), and the question is whether its own analogues — or a different-scaffold FGFR inhibitor — actually bind the FGFR1 kinase domain better than erdafitinib does.

**Falsifiable question.** Does any ChEMBL FGFR1 inhibitor or clinical FGFR inhibitor out-score erdafitinib on the erdafitinib-bound FGFR1 structure 5EW8 by more than Vina's ±1–2 kcal/mol noise? **Falsifier:** a kinase assay showing the winner's FGFR1 IC50 not better than erdafitinib's 1.2 nM, or a cell-viability assay on an FGFR1-amplified line (NCI-H520) showing no better growth inhibition. **Causal identification:** validated-control re-docking — erdafitinib re-docked on its own co-crystal (5EW8) as the control, three ChEMBL analogues and pemigatinib docked on the same structure with the same box and exhaustiveness — association only beyond that, since docking scores are not IC50 and not tumour response.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-26: the FGFR1 amplification frequencies (Weiss et al., Sci Transl Med 2010;2:62ra93; Turner et al., Cancer Res 2010;70:2085; Clin Cancer Res 2016;22:259); the erdafitinib approval trial (Loriot et al., N Engl J Med 2019;381:338–348, PMID 31340094); the erdafitinib–FGFR1 structure and the FGFR mutation landscape (Patani et al., Oncotarget 2016;7:24252 — 5EW8, 1.63 Å); the RAGNAR phase 2 study of erdafitinib in FGFR-altered solid tumours; and pemigatinib's approvals (FDA 2020 for FGFR2-fusion cholangiocarcinoma; 2022 for myeloid/lymphoid neoplasms with FGFR1 rearrangement). The classical-canon sweep: the Canon of Medicine describes tumours (waram) and their treatment without a kinase concept; the principle carried is hifz al-nafs, with the honest note that no classical source addresses FGFR1.

### 2.2 Target identification

The pipeline resolved the target correctly on the first run: UniProtKB P11362 (FGFR1, Homo sapiens) → ChEMBL lookup returned 26 ranked leads. Two records deserve stating, not hiding: CHEMBL3545376 (IC50 0.25 nM) and CHEMBL5189383 (IC50 0.2 nM) carry erdafitinib's exact descriptors (MW 446.56, logP 4.18, TPSA 77.33) — CHEMBL3545376 is erdafitinib's own ChEMBL record and CHEMBL5189383 is the same compound under another record — so they are not independent leads and are not used as comparators. The genuinely distinct comparators are CHEMBL3980069 (IC50 0.3631 nM), CHEMBL5182360 (0.28 nM) and CHEMBL5799893 (0.355 nM), plus the clinical comparator pemigatinib (PubChem CID 86705695), whose SMILES was verified live against PubChem. The QUERY (erdafitinib) verified against PubChem (CID 67462786, C25H30N6O2, MW 446.56, logP 4.18, 1 H-bond donor, 7 acceptors, TPSA 77.33 Å², 9 rotatable bonds, 0 Lipinski violations). The auto-picker found no PDB to dock on (its <3.0 Å X-ray filter plus the ligand-centre check skipped 5EW8 — see §2.3 for the manual correction).

### 2.3 Molecular docking

Standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: box 22.5 Å, exhaustiveness 8, best of 3 poses reported. Primary structure: 5EW8, the 1.63 Å X-ray structure of the FGFR1 kinase domain in complex with erdafitinib (Patani et al., Oncotarget 2016;7:24252), grid centre the centroid of the co-crystallised erdafitinib, verified by direct computation from the PDB file with `dock._ligand_center`. Erdafitinib is therefore the self-dock control on its own structure. The structure shows erdafitinib bound to an inactive (αC-out, DFG-in) conformation — a type I½ inhibitor — so the pocket is in erdafitinib's conformation and favours its own scaffold; the paper states this rather than letting the headline stand alone. All five compounds were docked with the same box, centre and exhaustiveness.

### 2.4 PAINS screen

RDKit PAINS filter applied to all five compounds. All are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for all five compounds (molecular weight, logP, H-bond donors/acceptors, TPSA, rotatable bonds, Lipinski violations). No ToxGuard read-across is reported for this set: the pipeline's Tox21 panel ran a kNN read-across at low maximum similarity, which is not safety data; it is omitted rather than presented.

### 2.6 Honesty limits

Docking ≠ IC50. Vina noise is ±1–2 kcal/mol, and the ChEMBL IC50s in this set span only 0.2–0.36 nM — a 1.8-fold range that is inside both assay noise and docking noise — so this docking can rank scaffolds but cannot resolve sub-nanomolar potency differences; the published IC50s carry that claim, not this computation. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published IC50s and the published structure. The 5EW8 pocket is in erdafitinib's αC-out conformation, so it favours erdafitinib-like scaffolds over pemigatinib's. Erdafitinib's published FGFR1 IC50 (1.2 nM) and its ChEMBL records (0.2–0.25 nM) differ 5-fold — assay variation, stated in §3.2 — so no ChEMBL number is treated as the true value. FGFR-family selectivity is not measured here: a compound that scores well on FGFR1 may bind FGFR2/3/4 equally, and the hyperphosphataemia that limits erdafitinib is an FGFR1/3-mediated effect, so selectivity is the question the docking cannot answer.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Best affinity (kcal/mol) | Poses (kcal/mol) | Published FGFR1 IC50 (nM) | PAINS |
|---|---|---|---|---|
| Pemigatinib | −10.53 | −10.53, −10.50, −9.08 | Not reported in sources searched | Clean |
| CHEMBL5799893 | −9.88 | −9.88, −8.91, −8.81 | 0.355 | Clean |
| CHEMBL3980069 | −9.59 | −9.59, −9.51, −9.48 | 0.3631 | Clean |
| CHEMBL5182360 | −9.14 | −9.14, −8.99, −8.93 | 0.28 | Clean |
| Erdafitinib (reference, self-dock control) | −9.00 | −9.00, −8.83, −8.44 | 1.2 | Clean |

Pose consistency is tight for two compounds and not for two. CHEMBL3980069 (spread 0.11) and CHEMBL5182360 (spread 0.21) converged on the same binding mode three times, so their scores are the most trustworthy in the table. Pemigatinib's top two poses converge (−10.53, −10.50) and its third is 1.45 kcal/mol worse, so its lead is real as a docking result but rests on two poses. CHEMBL5799893's −9.88 rests on a single pose — its other two poses are −8.91 and −8.81, a full kcal/mol worse — so its honest score is ~−8.9, below erdafitinib, and its rank in the table should be read as second-to-last, not second. The ranking itself is the problem. Pemigatinib leads erdafitinib by 1.53 kcal/mol, inside Vina's ±1–2 kcal/mol noise, so no compound beats erdafitinib beyond noise. Worse, the ranking inverts the published IC50 order: by IC50 the order is CHEMBL5182360 (0.28 nM) > CHEMBL5799893 (0.355) ≈ CHEMBL3980069 (0.363) > erdafitinib (1.2 nM), while by docking it is pemigatinib > CHEMBL5799893 > CHEMBL3980069 > CHEMBL5182360 > erdafitinib — the most potent ChEMBL compound by IC50 ranks fourth of five, and erdafitinib, the co-crystallised ligand, ranks last on its own structure. The 5-fold spread between erdafitinib's published IC50 (1.2 nM) and its own ChEMBL records (0.2–0.25 nM) is itself larger than the 1.8-fold spread across the three ChEMBL compounds, so the "more potent" ChEMBL numbers may be assay variation rather than potency — and the docking, which is the only like-for-like comparison in this study, does not reproduce them.

### 3.2 Comparison with published docking

No published docking study of FGFR inhibitors on 5EW8 was found in the searches for this paper, so there is no published docking table to compare against. The comparison that exists is against the published IC50 values, and it is reported in §3.1 in full — including the inversion, not just the agreements. One assay-variation note, stated in §2.6 and repeated here because it decides the interpretation: erdafitinib's published FGFR1 IC50 is 1.2 nM while its own ChEMBL records give 0.2–0.25 nM, so no ChEMBL IC50 in this set can be treated as the true value.

### 3.3 The standardisation / quality problem: which erdafitinib?

The comparison that matters clinically is not IC50 against IC50. Erdafitinib's published FGFR1 IC50 (1.2 nM) and its ChEMBL records (0.2–0.25 nM) differ 5-fold for the same compound — the same assay-variation problem that makes the three ChEMBL compounds (0.28–0.36 nM) look "more potent" than erdafitinib. A ranking built on numbers that cannot agree about the reference drug is ranking assay conditions, not compounds. The same problem applies to the clinical comparison: pemigatinib was optimised for FGFR2, not FGFR1, and its FGFR1 IC50 was not reported in the sources searched — so its docking lead on FGFR1 has no published potency to be checked against, and the kinase assay in §4.5 is the first measurement that would settle it.

## 4. Discussion

### 4.1 The reframe: the question changes from "which FGFR inhibitor?" to "can docking rank kinase inhibitors at all?"

The paper set out to find whether any FGFR1 inhibitor beats erdafitinib on the FGFR1 kinase domain. The answer is no — not because erdafitinib is unbeatable (its published IC50 is the worst in the set, and its own ChEMBL records say it is 5-fold better than its label value), but because the method cannot tell. Pemigatinib's 1.53 kcal/mol lead is a real number and a non-result at the same time: it is inside the noise bar, and the control that would have validated it — erdafitinib on its own structure — scored worst of the five. The question therefore changes: the finding is not "pemigatinib wins" but "Vina on a single kinase structure cannot rank a congeneric series whose published IC50s span only ~4-fold". That is a useful negative, and it is the paper's actual contribution — it stops a drug programme that the raw table, read naively, would seem to support.

### 4.2 Why the "win" must not be over-read

Four reasons. First, the margin: 1.53 kcal/mol against a ±1–2 kcal/mol noise bar is not a lead, it is a tie with a sign. Second, the self-dock control: erdafitinib last of five on its own structure means the pocket conformation, not the compounds, is doing part of the ranking. Third, the pose problem: CHEMBL5799893's second place rests on a single pose, and pemigatinib's lead on two — the only compound in the table whose ranking is fully converged is CHEMBL3980069, which leads erdafitinib by 0.59 kcal/mol, well inside noise. Fourth, the missing pharmacology: the docking cannot see the αC-out/DFG-in equilibrium or the gatekeeper mutations that decide clinical resistance — the two properties that separate erdafitinib from the next FGFR inhibitor. Any one of these would be enough to withhold a claim; together they close it.

### 4.3 Mechanism

Erdafitinib is a pan-FGFR inhibitor that binds in the ATP pocket in the αC-out/DFG-in conformation — type I½. Its pyrimidinyl-pyrazole core occupies the adenine pocket, and its dimethoxyphenyl group extends into a hydrophobic pocket that opens only when the αC helix moves out. The published biochemical profile (FGFR1 1.2 nM, FGFR2 2.5 nM, FGFR3 3 nM, FGFR4 5.7 nM; Kd 0.24–2.2 nM) reflects that binding mode, and the clinical hyperphosphataemia (75.9% of patients) is the on-target signature of FGFR inhibition of phosphate homeostasis — a pharmacodynamic marker, not a side effect to be wished away. The resistance mutations that matter clinically are gatekeeper mutations (FGFR1 V561M, FGFR3 V555M) and the molecular-brake mutations (FGFR3 N540K, FGFR1 N546K), which shift the kinase toward the active conformation that type I½ inhibitors bind poorly. Test for each link: (i) a kinase inhibition assay measures IC50 directly against the published values; (ii) a cellular assay (FGFR1-amplified lung cancer cell line) measures growth inhibition and phospho-FGFR suppression; (iii) a gatekeeper-mutant kinase assay measures the fold-loss in potency, which is the property that decides whether a compound survives resistance.

### 4.4 Testable hypotheses

1. The best-scoring compound on 5EW8 has an IC50 within 3-fold of its published value in the same kinase assay. Falsifier: IC50 more than 3-fold worse than published. (Status after this study: the hypothesis is already weakened — the docking order does not reproduce the published IC50 order, so the assay is now testing the method, not the compounds.)
2. Erdafitinib out-scores pemigatinib on 5EW8 — the computational signature of erdafitinib's broader FGFR profile, since pemigatinib was optimised for FGFR2. Falsifier: pemigatinib scores better, which would suggest the FGFR1 pocket does not discriminate the two drugs. (Status after this study: pemigatinib scored better by 1.53 kcal/mol — the hypothesis is refuted, and the FGFR1 pocket does not discriminate the two drugs by docking.)
3. No ChEMBL compound out-scores erdafitinib by more than 2 kcal/mol. Falsifier: one does, which would make it a candidate for the kinase assay rather than a footnote. (Status after this study: the hypothesis holds — the largest ChEMBL lead is 0.88 kcal/mol — but it holds vacuously, because the method cannot resolve the differences it was asked to measure.)

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): kinase inhibition assay for the five compounds on FGFR1, FGFR2 and FGFR3, same plate, n=3, with erdafitinib's published IC50 values (1.2, 2.5, 3 nM) as the controls; readout IC50. Stage 2 (weeks 4–8): cellular assay for the best two compounds from stage 1 on an FGFR1-amplified lung cancer cell line, measuring growth inhibition and phospho-FGFR suppression, with erdafitinib as the control. Stage 3 (weeks 9–12): if any compound passes stages 1–2 — IC50 within 3-fold of erdafitinib's on FGFR1 and a cellular effect — a gatekeeper-mutant (V561M) kinase assay for that compound; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every margin except a lead larger than 2 kcal/mol.
2. The 5EW8 pocket is in erdafitinib's conformation, so part of any erdafitinib lead is conformational favouritism; the cleaner comparison is among the four non-erdafitinib compounds.
3. The three ChEMBL compounds have no recorded assay type in the pipeline output, so their IC50 values (0.28–0.36 nM) may not be comparable to erdafitinib's published values; a "more potent" ChEMBL compound may simply have been assayed differently.
4. The pipeline returned erdafitinib itself as its own "lead" (CHEMBL3545376, 0.25 nM) and a duplicate record (CHEMBL5189383, 0.2 nM, identical descriptors), so no ChEMBL-derived independent FGFR1 ligand set exists in this study beyond the three compounds used.
5. The docking cannot see the αC-out/DFG-in equilibrium or the gatekeeper mutations that decide clinical resistance — the two properties that separate erdafitinib from the next FGFR inhibitor.
6. No published Pakistani study reports FGFR1 amplification frequencies in lung or breast cancer, so the clinical picture is global; the Pakistani numbers in this paper are burden numbers, not response numbers.
7. The classical-canon sweep found no FGFR-relevant text: the Canon describes cancer without a kinase concept, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

No FGFR1 inhibitor beats erdafitinib on the FGFR1 structure 5EW8 by more than Vina's noise: pemigatinib leads by 1.53 kcal/mol, inside the ±1–2 kcal/mol bar, and the method fails its own control — erdafitinib scores worst of five on its own structure, and the most potent ChEMBL compound by published IC50 ranks fourth. Docking cannot rank the FGFR1 inhibitors, and no drug programme follows from these scores. The next step is a kinase inhibition assay on the same five compounds, which will either reproduce the published IC50 order and rehabilitate the docking, or confirm that the ranking is a pocket artefact.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Ministry of National Health Services, with the provincial cancer institutes that run oncology services. **Decision:** whether to spend anything on FGFR testing or on an erdafitinib programme, and what must exist first. **Exact change:** do not spend on an erdafitinib programme on the basis of docking — the drug is not on Pakistan's essential medicines list and its cost is far beyond public procurement; instead, fund a molecular-testing survey for FGFR alterations in lung and breast cancer at the provincial cancer institutes, so Pakistan's own alteration frequencies are measured rather than assumed from the global 10–25% figures, and so the patients who would benefit from an FGFR inhibitor are identified before any drug is bought. **If evidence Z appears, reverse this:** if the survey shows FGFR1 amplification above 10% in squamous lung carcinoma and a cost-effectiveness analysis shows an FGFR inhibitor is affordable at a negotiated price, move to a procurement assessment; if the survey shows alteration rates below 5%, keep the money on testing for the commoner targets (EGFR, HER2) — do not proceed to any FGFR drug programme on docking scores alone. The Islamic principle is hifz al-nafs joined to adl (justice): where the drug is unaffordable and the patients are unidentified, spending on the drug before spending on the test would violate both. The evidence here is thin — docking only — so the recommendation is "run the testing survey", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content.

## References

1. Weiss J, et al. Frequent and focal FGFR1 amplification associates with therapeutically tractable FGFR1 dependency in squamous cell lung cancer. Sci Transl Med. 2010;2:62ra93. (FGFR1 amplification 10–25% in squamous lung carcinoma.)
2. Turner N, et al. FGFR1 amplification drives endocrine therapy resistance and is a therapeutic target in breast cancer. Cancer Res. 2010;70:2085. (~10% of ER-positive breast cancers.)
3. Loriot Y, et al. Erdafitinib in locally advanced or metastatic urothelial carcinoma. N Engl J Med. 2019;381:338–348. PMID: 31340094. (FDA approval April 2019; hyperphosphataemia 75.9%.)
4. Patani H, et al. Landscape of actionability of drug targets in single agents and combination therapy. Oncotarget. 2016;7:24252. (5EW8, 1.63 Å, FGFR1 + erdafitinib.)
5. Erdafitinib (Balversa) — FDA label. (FGFR1–4 IC50 1.2, 2.5, 3, 5.7 nM; Kd 0.24–2.2 nM; >99% protein-bound; half-life 59 h.)
6. Pemigatinib (Pemazyre) — FDA label. (FDA 2020 for FGFR2-fusion cholangiocarcinoma; 2022 for FGFR1-rearranged myeloid/lymphoid neoplasms.)
7. RCSB PDB entry 5EW8: crystal structure of the FGFR1 kinase domain in complex with erdafitinib, 1.63 Å. RCSB Protein Data Bank. Accessed 2026-11-26.
8. UniProtKB P11362: Fibroblast growth factor receptor 1 (FGFR1), Homo sapiens. UniProt. Accessed 2026-11-26.
9. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source — cited for the hifz al-nafs principle only.)
10. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
11. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-130-2026-11-26-5EW8.json` (erdafitinib, CHEMBL3980069, CHEMBL5182360, CHEMBL5799893, pemigatinib on 5EW8). The pipeline run is in `hidden_files/dock-HP-130-2026-11-26.json` (target UniProt P11362; ChEMBL lookup returned erdafitinib itself as CHEMBL3545376, 0.25 nM, and a duplicate record CHEMBL5189383, 0.2 nM, with identical descriptors; docking skipped — no PDB found by the auto-picker). Reference drug erdafitinib (PubChem CID 67462786); comparator pemigatinib (CID 86705695); ChEMBL compounds CHEMBL3980069, CHEMBL5182360, CHEMBL5799893, SMILES verified against PubChem. Structure: PDB 5EW8 (1.63 Å, erdafitinib-bound). Target: UniProtKB P11362. No additional data were generated.
