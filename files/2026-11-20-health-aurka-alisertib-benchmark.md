# The 8-Chloro Isomer of Alisertib Out-Docks Alisertib on the 1.96 Å Aurora A Structure — but the 0.33 kcal/mol Margin Is Inside Vina Noise and the Most Potent Measured Inhibitor Docks Ninth

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-20 · **Health Papers Agent — Paper #87** (daily 5-paper run)

**Keywords:** Aurora kinase A; AURKA; alisertib; MLN8237; molecular docking; LY3295668; solid tumours; ChEMBL

---

## Abstract

Aurora kinase A (AURKA) is amplified or overexpressed in many solid tumours, yet no Aurora kinase inhibitor is approved anywhere: alisertib, the most advanced, failed its Phase 3 LUMIERE trial in peripheral T-cell lymphoma (response rate 33% versus 45% for the comparators). We asked whether alisertib analogues or other clinical-stage AURKA inhibitors bind the true ATP pocket more strongly than re-docked alisertib. ChEMBL's bioactivity endpoint was down on the day of the run (HTTP 500 for every target), so the comparison set was built from PubChem 2D-similar analogues of alisertib plus four literature inhibitors with published potencies, and docked with AutoDock Vina 1.2.7 on the 1.96 Å AURKA structure 6C2R at the co-crystallised LY3295668 centroid. The best score came from PubChem CID 92044531, the 8-chloro positional isomer of alisertib, at −9.20 kcal/mol versus −8.87 for alisertib and −8.95 for the co-crystallised LY3295668; two further analogues scored −8.77 and −8.74, and the two top-similarity hits turned out to be sodium-salt forms of alisertib itself. The honest limit: the 0.33 kcal/mol margin is inside Vina's ±1–2 kcal/mol noise, the most potent measured inhibitor (MK-5108, IC50 0.064 nM) docked ninth of ten at −8.19, the docking–potency correlation across the five literature compounds is weak (Spearman rho 0.40, p = 0.51), and no analogue carries a measured potency. The claim that the 8-chloro isomer is a better AURKA inhibitor would be refuted if a biochemical kinase assay shows its IC50 more than 10-fold worse than alisertib's 1.2 nM, or if cellular phospho-Thr288 inhibition shows no advantage. The falsifiable next step is an 8–12-week kinase-plus-cellular test of the isomer against alisertib and LY3295668.

---

## 1. Introduction

Cancer caused an estimated 20 million new cases and 9.7 million deaths worldwide in 2022, and in Pakistan 185,748 new cases and 118,631 deaths in the same year (IARC GLOBOCAN 2022). Most of those deaths are in solid tumours, where the drugs that work do so for a while and then stop working — resistance, not the absence of targets, is the usual failure. Aurora kinase A (AURKA) is one of the targets that keeps being re-tried: a mitotic serine/threonine kinase, encoded on chromosome 20q13, that matures centrosomes, builds the bipolar spindle and guards chromosome segregation. When it is amplified or overexpressed — in breast, ovarian, colorectal, lung, gastric, prostate, cervical and pancreatic cancers — it drives proliferation, epithelial–mesenchymal transition, metastasis, cancer-stem-cell self-renewal and resistance to chemotherapy and radiotherapy. In epithelial ovarian cancer, 82.8% of tumours overexpress Aurora A, and the most strongly overexpressing tumours cut median survival from 2.81 to 1.44 years.

The most advanced AURKA inhibitor, alisertib (MLN8237), is a selective ATP-competitive inhibitor with a cell-free IC50 of 1.2 nM and more than 200-fold selectivity over Aurora B. It reached Phase 3: the LUMIERE trial (NCT01482962) randomised 271 patients with relapsed or refractory peripheral T-cell lymphoma to alisertib 50 mg twice daily (days 1–7 of a 21-day cycle) or investigator's choice of pralatrexate, romidepsin or gemcitabine. It was stopped early for futility — overall response rate 33% versus 45% for the comparators, median progression-free survival 115 versus 104 days, median overall survival 415 versus 367 days — and the most common adverse events were anaemia (53%) and neutropenia (47%). No Aurora kinase inhibitor is approved anywhere. The class did not fail because the target is wrong; it failed because a single molecule, dosed intermittently at the edge of myelosuppression, could not beat the comparators. That leaves the precise question this paper attacks: do other molecules — either analogues of alisertib itself or other clinical-stage AURKA inhibitors — bind the true ATP pocket of AURKA more strongly than re-docked alisertib, and do the measured potencies track the docking order?

The classical medical canon knew this disease class long before the gene was: Ibn Sina's Canon of Medicine (c. 1025) discusses sartan (cancer) as a hard, spreading swelling with a poor prognosis, and Al-Razi's Kitab al-Hawi records clinical observation of tumours. These texts are hypothesis sources, not evidence — they knew the syndrome, not the target — but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do alisertib analogues and clinical-stage AURKA inhibitors bind the true ATP pocket of AURKA (PDB 6C2R) at scores beyond re-docked alisertib, and does the docking order track measured biochemical potency? **Falsifier:** if a fluorescence-based kinase assay shows a candidate's AURKA IC50 more than 10-fold worse than alisertib's 1.2 nM, or if cellular phospho-Thr288 Aurora A inhibition shows no advantage, the claim for that compound is refuted. **Causal identification:** validated-control re-docking — the reference drug and the co-crystallised ligand both re-docked on a co-crystal structure of the same target — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-20: the alisertib development record (Manfredi et al. 2011 characterisation; LUMIERE Phase 3 outcome, O'Connor et al. 2019), the LY3295668 RB1 synthetic-lethality study (Gong et al. 2019), AURKA reviews (Du et al. 2021; nuclear-function review 2024), the ovarian-cancer prognosis study (Landen et al. 2007), the latest literature digest (2026-11-14, no AURKA item — the sweep was therefore targeted, not digest-led), and the RCSB records for PDB 6VPM and 6C2R. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025); Al-Razi, Kitab al-Hawi (c. 900) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 The ChEMBL outage and the comparison set

The standard LeadForge pipeline was run first (UniProtKB → ChEMBL → PubChem → RDKit → Vina). It resolved the target correctly — UniProtKB O14965, human Aurora kinase A, 403 amino acids — but the ChEMBL bioactivity endpoint returned HTTP 500 for every target on 2026-11-20 (an EBI-side outage, verified the same day against other targets), so step 2 returned zero ligands and no ChEMBL-measured potencies were retrievable. The pipeline was run once; per the standing rule it was not re-run in the hope the outage would clear. The comparison set was therefore built the way the 2026-11-11 FLT3 run built its set under the same outage: PubChem `fastsimilarity_2d` (2D fingerprint similarity ≥80%) against alisertib, which returned 50 candidate CIDs, of which 49 yielded usable structures; and four literature-known AURKA inhibitors with published potencies — LY3295668 (Ki 0.8 nM, >1,000-fold selective over Aurora B), MK-5108 (IC50 0.064 nM), ENMD-2076 (IC50 14 nM) and danusertib (IC50 13 nM Aurora A, 79 nM Aurora B, 61 nM Aurora C). **No measured potency is attached to any PubChem analogue in this paper** — their PubChem similarity is a structural fact, not an activity claim, and any analogue that "wins" here is a candidate for the assay, not a better drug.

### 2.3 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: human AURKA, UniProtKB O14965. Structure: PDB 6C2R, the AURKA kinase domain (residues 125–391) in complex with LY3295668, 1.96 Å. Grid centre: centroid of the co-crystallised ligand EG7 (LY3295668), [110.14, −17.65, 5.80], computed with `dock._ligand_center`; box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for alisertib and every comparator.

**A wrong-site audit, stated plainly.** The pipeline's first run for this topic picked PDB 6VPM (1.58 Å) — the highest-resolution AURKA structure — and docked alisertib there at −8.36 kcal/mol. That run is DISCARDED, not reported as a result. The audit showed the grid centre [−4.65, −7.62, −29.10] is exactly the centroid of R74, a covalent fragment disulfide-bonded to Cys290 in the activation loop — an allosteric redox site, not the ATP pocket — while the ATP-site nucleotide in the same structure sits ~34 Å away. Alisertib is an ATP-competitive inhibitor; a score at the R74 site says nothing about its ATP-pocket binding. The failure mode is the same class as the TYK2 JH1/JH2 domain audit (2026-11-11), the gyrase 3M4I audit (Paper #75) and the MDM2/PLK1 wrong-target audit (Paper #80): the auto-picked structure must be checked for the right *site*, not just the right protein. The corrected run uses 6C2R, whose co-crystallised ligand LY3295668 sits in the ATP pocket — verified directly: its centroid is 7.9 Å from the hinge Ala213 Cα and its closest atom is 1.88 Å from a hinge residue (210–216). All scores in §3 are from the corrected run (`hidden_files/dock-HP-102-2026-11-20.json`); the discarded 6VPM run is preserved in `hidden_files/dock-HP-102-2026-11-20-WRONG-SITE.json` for audit.

### 2.4 PAINS screen

The RDKit PAINS filter (PAINS-A/B/C) was applied to alisertib and every docked comparator. Results are in the table in §3.1. A PAINS alert is reported, never hidden; it changes the validation design (redox controls).

### 2.5 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for every compound; ToxGuard Tox21 kNN read-across (12 assays) run for alisertib in the pipeline run. Alisertib itself (PubChem CID 24771867, C27H20ClFN4O4, MW 518.93) has 2 Lipinski violations (logP 5.75, MW >500) and a maximum Tox21 read-across probability of 0.385 (SR-MMP).

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for the PubChem analogues against AURKA in this study, and none is claimed. Measured IC50 values below are published records, not new measurements, and they come from different assay formats (cell-free IC50, Ki, cellular autophosphorylation IC50) — they are not directly interchangeable, and the paper says so wherever they are compared.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured potency vs AURKA* | Best affinity, 6C2R (kcal/mol) | Top-3 poses (kcal/mol) | PAINS | MW / logP |
|---|---|---|---|---|---|
| PubChem CID 92044531 (8-chloro isomer of alisertib)† | none (analogue) | **−9.20** | −9.20, −8.64, −8.57 | none | 518.9 / 5.75 |
| LY3295668 (co-crystallised ligand, re-docked) | Ki 0.8 nM | **−8.95** | −8.95, −8.91, −8.49 | none | 489.95 / 5.09 |
| Alisertib (reference, re-docked) | IC50 1.2 nM | −8.87 | −8.87, −8.30, −8.18 | none | 518.93 / 5.75 |
| PubChem CID 11712649 (difluoro analogue)† | none (analogue) | −8.77 | −8.77, −8.64, −8.22 | none | 476.87 / 5.87 |
| PubChem CID 11526006 (des-methoxy analogue)† | none (analogue) | −8.74 | −8.74, −8.35, −8.29 | none | 488.91 / 5.74 |
| Danusertib | IC50 13 nM | −8.51 | −8.51, −7.81, −7.73 | none | 474.57 / 2.64 |
| PubChem CID 66819785 (alisertib sodium salt, desalted)‡ | none (salt form) | −8.30 | −8.30, −8.12, −8.09 | none | 517.92 / 4.41 |
| PubChem CID 56843791 (alisertib sodium salt hydrate, desalted)‡ | none (salt form) | −8.28 | −8.28, −8.09, −8.04 | none | 517.92 / 4.41 |
| MK-5108 | IC50 0.064 nM | −8.19 | −8.19, −7.93, −7.68 | none | 461.95 / 5.71 |
| ENMD-2076 | IC50 14 nM | −7.79 | −7.79, −7.69, −7.60 | none | 375.48 / 3.17 |

\* Published potencies are from different assay formats (cell-free IC50, Ki) and are not directly interchangeable; see §2.6. † PubChem analogues: RDKit Morgan Tanimoto similarity to alisertib 0.811 (92044531), 0.699 (11712649), 0.833 (11526006); no measured potency is attached to any of them. ‡ The two top-similarity PubChem hits (Tanimoto 0.863 and 0.851) are sodium-salt forms of alisertib's carboxylate, not independent analogues: their PubChem SMILES contain 2–3 fragments, Vina's ligand preparation rejects multi-fragment molecules, and they were docked as the desalted carboxylate (MW 517.92, logP 4.41). Their scores therefore test the protonation state of alisertib, not a new scaffold.

The best score in the set belongs to the 8-chloro positional isomer of alisertib (CID 92044531): the same molecular formula as alisertib (C27H20ClFN4O4), the chlorine moved one position on the phenyl ring (8-chloro instead of 9-chloro), 0.33 kcal/mol better than alisertib itself. Two further genuine analogues — the 2,6-difluoro variant (CID 11712649) and the des-methoxy variant (CID 11526006, alisertib without the 2-methoxy group on the benzoic-acid ring) — score within 0.13 kcal/mol of alisertib. The co-crystallised ligand LY3295668 re-docks at −8.95 with tight poses (top-3 spread 0.46 kcal/mol), which validates the method: the protocol recovers strong binding for the ligand this structure was solved with. Every compound in the set is PAINS-clean.

### 3.2 The docking–activity relationship

The docking order does not track the measured potency order. Across the five compounds with published potencies, Spearman rho between measured potency (nM) and docking score is 0.40 (p = 0.51, n = 5) — weak and not statistically significant, and the five potencies mix IC50 and Ki formats, so even that number is an exploratory check rather than a measurement. The single most important discordance: MK-5108, the most potent measured inhibitor in the set by a factor of 12 (IC50 0.064 nM, 220-fold selective over Aurora B), docks ninth of ten at −8.19 kcal/mol — 0.76 kcal/mol worse than LY3295668, whose Ki is 0.8 nM. Conversely ENMD-2076, the weakest measured inhibitor (14 nM), docks last at −7.79, which is the one ranking the docking gets right. Rigid Vina scoring on this pocket cannot resolve a 12-fold potency difference, and it actively mis-ranks the most potent compound — the same failure Paper #80 found on MDM2, where the most potent measured compound also docked worst. This is the paper's most important negative result: **the docking ranking is not a potency ranking**, and any claim built on the −9.20 versus −8.87 gap alone would be over-reading noise.

### 3.3 Comparison with published docking

No published Vina study of these PubChem analogues on 6C2R was found in the sweep; the comparison here is internal (analogues and literature inhibitors versus re-docked alisertib on the same structure, same protocol). A molecular-dynamics study of AURKA selectivity did dock LY3295668, MK-5108 and alisertib on Aurora A (and Aurora B) and reported MM/PBSA binding free energies, but it did not publish Vina scores comparable to these, so no numeric cross-check is possible. The re-docked LY3295668 score is the validated control that anchors the comparison: it is the co-crystallised ligand of this exact structure, so a method that could not recover strong binding for it would be broken. It did.

### 3.4 The developability problem the table does not solve

Every compound in the set except ENMD-2076 and danusertib is highly lipophilic (logP 5.09–5.87), and alisertib, its 8-chloro isomer, MK-5108 and LY3295668 all carry Lipinski violations driven by logP >5 (alisertib also by MW >500). The 8-chloro isomer inherits alisertib's exact developability profile — same formula, same logP — so even if its 0.33 kcal/mol edge were real, it would face the same solubility and protein-binding problems, and the same on-target myelosuppression that comes from inhibiting a mitotic kinase in normal proliferating tissue. The two analogues with the cleanest profiles are the des-methoxy variant (CID 11526006, MW 488.91, 1 violation) and the difluoro variant (CID 11712649, MW 476.87, 1 violation), but both are still logP >5.7. A better docking score does not fix a lipophilicity problem, and this paper does not pretend otherwise.

## 4. Discussion

### 4.1 The reframe

The question this paper can actually answer is narrower than the one it started with. It cannot say "the 8-chloro isomer beats alisertib" — the 0.33 kcal/mol margin is inside noise, the docking order contradicts the measured potency order, and the isomer inherits alisertib's exact lipophilicity problem. What it can say is: (a) a positional isomer of alisertib, differing by one chlorine position, binds the true ATP pocket with a tight, reproducible pose and the best score in a ten-compound set; (b) two further genuine analogues bind within 0.13 kcal/mol of alisertib; (c) the two top-similarity PubChem hits are not new molecules at all but alisertib's own sodium salt, caught and reported rather than counted as discoveries; (d) the pipeline's first, wrong-site run was caught and corrected before publication, and the correction is documented; (e) the decisive experiment is now sharply defined — a biochemical kinase assay plus cellular phospho-Thr288 engagement for the 8-chloro isomer against alisertib and LY3295668 — and it is cheap and feasible in a university lab.

### 4.2 Why the "win" must not be over-read

Three reasons, whatever the table shows. First, any margin under ~1–2 kcal/mol is inside Vina's noise. Second, rigid docking on one structure cannot rank compounds whose measured potencies span three orders of magnitude (0.064 nM to 14 nM) — if the docking order contradicts the measured order, the docking is wrong, not the measurements. Third, the PubChem analogues carry no measured potency at all: a good docking score for an analogue is a hypothesis for the assay, worth exactly one binding experiment, and nothing more.

### 4.3 Mechanism

AURKA is activated at the centrosome by TPX2 binding and by autophosphorylation of Thr288 in the activation loop; it then phosphorylates substrates that build the bipolar spindle (including TACC3/ch-TOG) and it stabilises N-Myc and MYC in the nucleus, where kinase-independent scaffolding functions also sustain oncogenic transcription. That nuclear, kinase-independent role is the reason kinase inhibitors can fail even when they occupy the ATP pocket perfectly — the protein keeps scaffolding. Test for each link: (i) a biochemical kinase assay measures whether the compound inhibits AURKA catalytic activity (IC50/Ki); (ii) phospho-Thr288 immunoblotting in mitotic cells measures whether the compound engages AURKA in cells; (iii) monopolar-spindle formation and G2/M arrest measure whether the mitotic phenotype follows; (iv) an RB1-deficient line (e.g. NCI-H446) versus an RB1-wild-type line measures whether the LY3295668 synthetic-lethality logic extends to the new compound.

### 4.4 Testable hypotheses

1. The best-docking PubChem analogue inhibits recombinant AURKA with an IC50 within 10-fold of alisertib's 1.2 nM in a biochemical kinase assay. Falsifier: IC50 >12 nM.
2. At least one analogue reduces phospho-Thr288 Aurora A in mitotic HCT116 cells at ≤1 µM, with monopolar spindles as the phenotypic readout. Falsifier: no phospho-Thr288 reduction below 10 µM.
3. Re-docking with molecular-dynamics refinement preserves any analogue's advantage over alisertib within 1 kcal/mol. Falsifier: the advantage disappears after minimisation.
4. The best analogue shows a selectivity window over Aurora B (phospho-HisH3 Ser10 readout) of at least 10-fold. Falsifier: Aurora B inhibition within 3-fold of Aurora A inhibition — the compound is a pan-Aurora inhibitor, not an AURKA inhibitor, and its development case collapses into the danusertib class.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): biochemical AURKA kinase assay for the best two analogues + alisertib and LY3295668 controls; readout IC50, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): cellular target engagement — phospho-Thr288 Aurora A and phospho-HisH3 Ser10 (Aurora B counter-screen) in HCT116, plus monopolar-spindle counts; RB1-deficient NCI-H446 versus RB1-wild-type as the synthetic-lethality check. Stage 3 (weeks 9–12): if any analogue passes stages 1–2, solubility and plasma-protein-binding measurement plus a first cytotoxicity screen (HepG2); if none passes, publish the negative result with the docking data as the reason the hypothesis failed.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin.
2. The PubChem analogues have no measured potency against AURKA — or against anything — and similarity to alisertib is not evidence of activity.
3. The ChEMBL bioactivity endpoint was down on the day of the run (HTTP 500), so no ChEMBL-measured AURKA ligands could be retrieved; the comparison set is smaller and less systematic than the pipeline's design intends. A re-run when the endpoint recovers may change the set.
4. Published potencies compared here come from different assay formats (cell-free IC50, Ki, cellular autophosphorylation IC50) and are not directly interchangeable; the Spearman analysis in §3.2 treats them as one scale only as an exploratory check.
5. A single structure (6C2R) was used; the ATP pocket is flexible and the DFG-in/DFG-out state and the TPX2-bound conformation change the pocket, so one rigid structure under-samples the binding landscape.
6. AURKA's kinase-independent nuclear scaffolding functions (MYC/N-Myc stabilisation) are not addressed by ATP-pocket docking at all; an ATP-competitive inhibitor can score perfectly here and still fail against the scaffolding function.
7. No Aurora B counter-screen was computed: selectivity over AURKB is the property that separates a usable AURKA drug from a pan-Aurora drug, and docking on AURKA alone cannot show it.
8. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon and Al-Razi's Kitab al-Hawi; the full Arabic texts were not read, and other classical works on tumours were not individually consulted.

## 6. Conclusion

The 8-chloro positional isomer of alisertib (PubChem CID 92044531) binds the true ATP pocket of Aurora A (6C2R) with the best score in a ten-compound set, −9.20 kcal/mol against −8.87 kcal/mol for re-docked alisertib and −8.95 for the co-crystallised LY3295668, with tight pose consistency and no PAINS alerts. The 0.33 kcal/mol margin is inside Vina noise, the docking order contradicts the measured potency order, and the isomer shares alisertib's lipophilicity problem — so this is not evidence that the isomer beats alisertib, it is evidence that the isomer is worth the cheap, decisive test: a biochemical kinase assay and cellular phospho-Thr288 engagement with alisertib and LY3295668 as comparators. That test, not another docking run, is the next step.

## 7. Policy implications

**Decision-maker:** Pakistan's Higher Education Commission research-funding panels and the SMBBMU ORIC office, with DRAP as the eventual regulator. **Decision:** whether to fund a small, targeted validation of alisertib analogues and existing AURKA inhibitors as an academic drug-discovery exercise. **Exact change:** commission the 8–12-week biochemical-plus-cellular screen proposed in §4.5 for the best two PubChem analogues against alisertib and LY3295668, instead of funding another purely computational screen of the same target. **If evidence Z appears, reverse this:** if both analogues lose >10-fold to alisertib in the kinase assay or show no phospho-Thr288 reduction in cells, drop this analogue set and redirect the same screen to the next AURKA chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable drug from a useless one for a disease that kills 9.7 million people a year, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only, and for the analogues not even measured potency — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Manfredi MG, Ecsedy JA, Chakravarty A, et al. Characterization of alisertib (MLN8237), an investigational small-molecule inhibitor of Aurora A kinase using novel in vivo pharmacodynamic assays. Clin Cancer Res. 2011;17(24):7614-7624. doi:10.1158/1078-0432.CCR-11-1536. PMID: 22016509.
2. O'Connor OA, Ozcan M, Jacobsen ED, et al. Randomized phase III study of alisertib or investigator's choice (selected single agent) in patients with relapsed or refractory peripheral T-cell lymphoma. J Clin Oncol. 2019;37(8):613-623. doi:10.1200/JCO.18.00899. PMID: 30707661.
3. Gong X, Du J, Parsons SH, et al. Aurora A kinase inhibition is synthetic lethal with loss of the RB1 tumor suppressor gene. Cancer Discov. 2019;9(2):248-263. doi:10.1158/2159-8290.CD-18-0469. PMID: 30373917.
4. Du R, Huang C, Liu K, Li X, Dong Z. Targeting AURKA in cancer: molecular mechanisms and opportunities for cancer therapy. Mol Cancer. 2021;20:15. doi:10.1186/s12943-020-01305-3.
5. Landen CN Jr, Lin YG, Immaneni A, et al. Overexpression of the centrosomal protein Aurora-A kinase is associated with poor prognosis in epithelial ovarian cancer patients. Clin Cancer Res. 2007;13(14):4098-4104. doi:10.1158/1078-0432.CCR-07-0431. PMID: 17634535.
6. Lim DC, Joukov V, Rettenmaier TJ, et al. Redox priming promotes Aurora A activation during mitosis. Sci Signal. 2020;13(642):eabb6707. doi:10.1126/scisignal.abb6707. PMID: 32694171.
7. RCSB PDB entry 6C2R: Aurora A kinase domain (residues 125–391) in complex with LY3295668, 1.96 Å. RCSB Protein Data Bank. Accessed 2026-11-20.
8. RCSB PDB entry 6VPM: TPX2–Aurora A fusion with C290 disulfide-bonded compound 8-34, 1.58 Å. RCSB Protein Data Bank. Accessed 2026-11-20.
9. ClinicalTrials.gov NCT01482962: A phase 3, randomized, two-arm, open-label trial of alisertib or investigator's choice in relapsed/refractory peripheral T-cell lymphoma (LUMIERE).
10. ClinicalTrials.gov NCT03092934: A phase I/II study of AK-01 (LY3295668) in solid tumours.
11. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; sartan, cancer as a hard spreading swelling.)
12. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; clinical observation of tumours.)
13. IARC Global Cancer Observatory. GLOBOCAN 2022: Pakistan fact sheet — 185,748 new cases, 118,631 deaths; worldwide 20 million new cases, 9.7 million deaths. Accessed 2026-11-20.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-102-2026-11-20.json` (corrected 6C2R run) and `hidden_files/dock-HP-102-2026-11-20-WRONG-SITE.json` (discarded 6VPM run, preserved for audit). PubChem analogues are listed by CID in `hidden_files/analogues-HP-102-2026-11-20.json`. Reference drug alisertib, PubChem CID 24771867. Structure: PDB 6C2R (1.96 Å). Target: UniProtKB O14965. No additional data were generated.
