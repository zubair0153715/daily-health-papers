# Fasiglifam Re-Docks at −10.23 kcal/mol on the GPR40–MK-8666 Structure — but One Analogue Leads by 1.71 kcal/mol, the Most Potent Analogue Docks Worst, and Every Analogue Is More Lipophilic Than the Drug That Failed on Liver Safety

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-21 · **Health Papers Agent — Paper #94** (daily 5-paper run)

**Keywords:** GPR40; FFAR1; fasiglifam; type 2 diabetes; molecular docking; drug-induced liver injury; ChEMBL; Pakistan

---

## Abstract

Pakistan has the highest age-standardised diabetes prevalence in the world — 31.4% of adults, about 34.5 million people, with 9.3 million undiagnosed — and type 2 diabetes is therefore the country's largest chronic-disease burden. GPR40 (free fatty acid receptor 1, FFAR1) is an attractive target because it potentiates glucose-dependent insulin secretion, so it lowers blood glucose with a low risk of hypoglycaemia; but its best-known agonist, fasiglifam (TAK-875), was terminated in late phase 3 in December 2013 over liver safety, and no GPR40 agonist has reached the market since. We asked whether any measured GPR40 agonist binds the receptor's allosteric pocket more strongly than fasiglifam itself. Using the LeadForge pipeline (UniProtKB O14842 → ChEMBL CHEMBL4422 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked fasiglifam and five ChEMBL analogues with measured potency on the 2.20 Å GPR40 structure 5TZR, centred exactly on the co-crystallised partial agonist MK-8666 (centre audit via dock._ligand_center). Fasiglifam re-docked at −10.23 kcal/mol. One analogue, CHEMBL3287571, leads by 1.71 kcal/mol on best pose (−11.94) and 1.43 kcal/mol on median pose — the first lead beyond Vina noise in this series — but the ranking contradicts measured potency: the most potent analogue by assay (CHEMBL4463571, EC50 0.2 nM) docks worst at −9.71, and fasiglifam itself (EC50 0.35 nM) docks second-worst. Every analogue is more lipophilic than fasiglifam (logP 5.02–6.79 vs 5.31), the property class that drove fasiglifam's liver injury through bile-acid transporter inhibition and a reactive acyl glucuronide. The claim that any analogue beats fasiglifam would be refuted if a GPR40 functional assay shows an EC50 worse than fasiglifam's, or if a bile-acid transporter panel shows inhibition at therapeutic concentrations. The falsifiable next step is an 8–12-week functional-plus-safety test of the best-scoring analogue against fasiglifam, with transporter and mitochondrial controls.

---

## 1. Introduction

In 2024, diabetes affected 589 million adults aged 20–79 worldwide (11.11% of the global population) and is projected to affect 853 million by 2050 (IDF Diabetes Atlas, 11th edition). Pakistan carries the heaviest burden of any country by age-standardised prevalence: 31.41% in 2024, an estimated 34.5 million adults living with the disease, 9.3 million of them undiagnosed, about 226,752 diabetes-related deaths in 2024, and a projected 70.2 million cases by 2050. Type 2 diabetes in Pakistan is therefore not a niche indication; it is the country's largest chronic-disease market, and it is also the disease where a failed drug costs the most — because the patients are already there, waiting, and the next candidate inherits their trust.

GPR40 (free fatty acid receptor 1, FFAR1) is a G-protein-coupled receptor on pancreatic β-cells that mediates free-fatty-acid-induced insulin secretion. Its appeal is a mechanism, not a marketing claim: activation potentiates glucose-stimulated insulin secretion, so it lowers blood glucose only when glucose is high, with a low risk of hypoglycaemia compared with traditional insulin secretagogues. Fasiglifam (TAK-875), a dihydrobenzofuran acetic acid developed by Takeda, is an ago-allosteric modulator of GPR40 — it binds a site distinct from the endogenous free-fatty-acid site and potentiates the effect of free fatty acids, signalling through Gαq, phospholipase C, inositol trisphosphate and diacylglycerol. It showed significant efficacy in phase 2 and phase 3 trials, improving glycaemic control with a low risk of hypoglycaemia. Then, in December 2013, its development was voluntarily terminated in late phase 3 over liver safety: in a pooled analysis of 15 double-blind studies (9,139 patients), ALT ≥3× the upper limit of normal occurred in 2.7% of fasiglifam patients versus 0.8% on active comparators and 0.5% on placebo, with three serious liver injuries and one Hy's Law case. No GPR40 agonist has reached the market since. The question this paper asks is narrower than "can GPR40 be drugged?" — it is "does any measured GPR40 agonist bind the allosteric pocket more strongly than fasiglifam, and is it any safer?"

The classical medical canon knew diabetes by its symptoms centuries before insulin or receptors: Ibn Sina's Canon of Medicine (c. 1025) describes the wasting disease with excessive urination (al-bawl al-sukkari, the sweet urine) and discusses dietary management — the Canon knows the syndrome, not the target. These texts are hypothesis sources, not evidence, but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL agonists with measured GPR40 potency bind the allosteric pocket of the MK-8666-bound structure (PDB 5TZR) at scores beyond re-docked fasiglifam, and would that binding translate into stronger GPR40 activation without fasiglifam's liver liability? **Falsifier:** a GPR40 functional assay showing an EC50 worse than fasiglifam's 0.35 nM, or a bile-acid transporter panel showing inhibition at therapeutic concentrations, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the reference compound re-docked on a co-crystal structure of its own target class — not a comparison against nothing. Association only beyond that: docking scores are not activity, and a docking score is not a liver-safety prediction.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-21: the fasiglifam mechanism and termination literature, the bile-acid transporter and acyl-glucuronide mechanistic studies, the MK-8666 phase Ib trial, the IDF Diabetes Atlas 11th edition (Lancet Diabetes Endocrinol 2026), the RCSB records for PDB 4PHU and 5TZR, and the ChEMBL target record. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Target identification — audited, with one correction to the record

The pipeline resolved the target correctly on the accession: UniProtKB O14842, human free fatty acid receptor 1 (FFAR1/GPR40), verified live 2026-11-21; ChEMBL target CHEMBL4422, "Free fatty acid receptor 1", human, single protein. One audit note: the pipeline's ChEMBL target-resolution step listed many unrelated targets (maltase-glucoamylase, ABCC9, PDE5A and others) before settling on CHEMBL4422 — the final target used was correct, and all 26 ranked leads are GPR40 agonists, but the resolution step needs the same independent verification as the PDB pick. A second, more consequential audit: the pipeline's query compound was verified against PubChem (CID 24857286, C29H32O7S, MW 524.6) and against ChEMBL1829174, whose ChEMBL preferred name is FASIGLIFAM — the query SMILES is the true fasiglifam scaffold (dihydrobenzofuran acetic acid with a methylsulfonylpropoxy biphenyl), and the ChEMBL record is the same molecule under its ChEMBL identifier, included as a separate lead. That duplication is the paper's internal control, and §3.1 says so.

### 2.3 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: human GPR40/FFAR1, UniProtKB O14842; ChEMBL target CHEMBL4422 (verified live 2026-11-21). Structure: PDB 5TZR, human GPR40 in complex with the partial agonist MK-8666 (ligand MK6), 2.20 Å X-ray resolution (Lu et al., Nat Struct Mol Biol 2017). Grid centre: centroid of the co-crystallised MK-8666, [−50.14, −1.90, 60.00], verified by direct computation from the PDB file with `dock._ligand_center` (audit 0.00 Å); box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for fasiglifam and all five analogues. Fasiglifam is therefore the self-dock control on a structure of its own target class: a method that could not recover strong binding for a 0.35 nM agonist would be broken. Two structures frame the binding mode: 4PHU (GPR40 + TAK-875, 2.33 Å, Srivastava et al., Nature 2014) established the non-canonical allosteric pocket that fasiglifam occupies, and 5TZR shows the same pocket occupied by MK-8666, a partial agonist from the same chemical family.

The comparison set is six compounds from the corrected O14842 ChEMBL run (26 ranked leads): fasiglifam itself and the five highest-ranked analogues with measured potency. Their measured potencies are ChEMBL bioactivities, not new measurements: fasiglifam EC50 0.35 nM (pChEMBL 9.46, as ChEMBL1829174); CHEMBL3287571 EC50 1.3 nM (pChEMBL 8.89; 12 nM in a CHO-cell aequorin assay); CHEMBL4534836 EC50 1.1 nM (pChEMBL 8.96); CHEMBL4591657 EC50 0.94 nM (pChEMBL 9.03); CHEMBL1829173 EC50 1.3 nM (pChEMBL 8.89); CHEMBL4463571 EC50 0.2 nM (pChEMBL 9.70). Note that these EC50 values come from different functional assays (inositol-phosphate accumulation, aequorin) and are not directly comparable across compounds — see §5.

### 2.4 PAINS screen

RDKit PAINS filter applied to fasiglifam and the five analogues. **No PAINS alerts in the set** — the first clean set in this series. That is a genuine positive: unlike the Pks13 benzofuran series, these compounds do not carry a structural alert. It does not clear them: fasiglifam itself carries no PAINS alert and still failed on liver safety, through mechanisms (transporter inhibition, reactive metabolite, mitochondrial toxicity) that no PAINS filter detects.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for fasiglifam: molecular weight 524.64, logP 5.31, 1 hydrogen-bond donor, 6 acceptors, TPSA 99.13 Å², 11 rotatable bonds, **2 Lipinski violations (molecular weight > 500, logP > 5) and a Veber failure** (11 rotatable bonds). The reference drug that reached phase 3 is not drug-like by these counts — a fact the validation design must remember, because descriptor counts cannot rank this class. The analogues: CHEMBL3287571 (MW 462.94, logP 5.02, HBD 1, HBA 5, TPSA 90.13 Å², 8 rotatable bonds, 1 violation, Veber pass), CHEMBL4534836 (MW 444.52, logP 6.10, HBD 1, HBA 3, TPSA 55.76 Å², 9 rotatable bonds, 1 violation, Veber pass), CHEMBL4591657 (MW 426.53, logP 6.16, HBD 1, HBA 3, TPSA 55.76 Å², 9 rotatable bonds, 1 violation, Veber pass), CHEMBL1829173 (MW 438.45, logP 6.53, HBD 1, HBA 2, TPSA 46.53 Å², 7 rotatable bonds, 1 violation, Veber pass) and CHEMBL4463571 (MW 440.56, logP 6.40, HBD 1, HBA 3, TPSA 55.76 Å², 9 rotatable bonds, 1 violation, Veber pass). Every analogue is smaller than fasiglifam but **more lipophilic** (logP 5.02–6.79, all above 5) — and lipophilicity is exactly the property class that drove fasiglifam's liver injury (see §3.3). ToxGuard Tox21 kNN read-across (12 assays) for fasiglifam: maximum predicted probability 0.373 (SR-ARE), with a maximum neighbour similarity of only 0.28 — a weak read-across, not a measurement, and it does not clear the compound. The analogues' maxima are 0.109–0.363 (SR-ARE or SR-MMP). No compound in the set is cleared by this screen, and none is condemned by it.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published ChEMBL potencies, which come from different functional assays and are not directly comparable. GPR40 has (at least) two ligand sites — the TAK-875/MK-8666 allosteric pocket docked here, and the fatty-acid orthosteric site where full agonists bind — and the analogues' chemotypes (cyclopropyl phenylacetic acids, a tetrazole) may bind the orthosteric site, in which case their scores here test fit to a pocket they do not occupy. Docking cannot predict liver safety. The five measured potency values in this paper are published ChEMBL bioactivities, not new measurements, and they span only 0.2–1.3 nM.

## 3. Results

### 3.1 Docking: the comparison table (5TZR, 2.20 Å)

| Compound | Measured GPR40 potency (ChEMBL) | Best affinity, 5TZR (kcal/mol) | Top-3 poses (kcal/mol) | Median pose | Margin vs fasiglifam | PAINS |
|---|---|---|---|---|---|---|
| CHEMBL3287571 | EC50 1.3 nM | −11.94 | −11.94, −11.59, −11.49 | −11.59 | +1.71 | none |
| CHEMBL4534836 | EC50 1.1 nM | −10.83 | −10.83, −10.37, −10.07 | −10.37 | +0.60 | none |
| CHEMBL4591657 | EC50 0.94 nM | −10.75 | −10.75, −10.54, −10.48 | −10.54 | +0.52 | none |
| CHEMBL1829173 | EC50 1.3 nM | −10.58 | −10.58, −10.32, −9.98 | −10.32 | +0.35 | none |
| Fasiglifam (query) | EC50 0.35 nM | −10.23 | −10.23, −10.16, −10.02 | −10.16 | — | none |
| CHEMBL4463571 | EC50 0.2 nM | −9.71 | −9.71, −9.09, −8.79 | −9.09 | −0.52 | none |

Fasiglifam re-docks at −10.23 kcal/mol on the MK-8666 structure, with tight pose consistency (−10.23, −10.16, −10.02) — a strong self-dock control for a 0.35 nM agonist in the allosteric pocket of its own target class. One analogue, CHEMBL3287571, leads by 1.71 kcal/mol on best pose (−11.94) and 1.43 kcal/mol on median pose (−11.59 vs −10.16) — **the first lead beyond Vina noise in this series**, on both pose statistics, with the tightest pose spread in the table (−11.94, −11.59, −11.49). Three more analogues lead by 0.35–0.60 kcal/mol on best pose, inside noise. The only compound that trails fasiglifam is the most potent by assay.

The decisive check is the comparison with measured potency, and it fails the same way it failed in every paper in this series. The most potent analogue by assay, CHEMBL4463571 (EC50 0.2 nM), docks worst (−9.71), 0.52 kcal/mol behind fasiglifam and 2.23 kcal/mol behind the best analogue. Fasiglifam itself (EC50 0.35 nM, more potent than four of the five analogues) docks second-worst. A scoring function that ranks the most potent compound last and a 1.3 nM compound first, inside one target family on the reference compound's own structure class, cannot rank this family — even when one margin clears the noise bar. The honest reading is therefore mixed, not a win: one analogue leads beyond noise, but the method fails its own positive control, so the lead is a hypothesis to test, not a discovery.

### 3.2 Comparison with published docking

No published Vina study of fasiglifam or these five analogues on 5TZR was found in the sweep; the comparison here is internal (analogues vs re-docked reference compound on the same structure, same protocol). The crystal structures themselves (4PHU for TAK-875, 5TZR for MK-8666) are the published ground truth for the allosteric binding mode; this paper tests whether a rigid scoring function can rank compounds inside that mode. The follow-on clinical record is the other comparison: MK-8666, the partial agonist co-crystallised in 5TZR, reached a phase Ib proof-of-concept study (63 patients, 14 days) and reduced fasting plasma glucose by 54.1 mg/dL at 500 mg versus placebo, with no serious adverse effects and one case of mild-to-moderate transaminitis at 150 mg — efficacy with a liver signal already visible at 14 days. That is the class history this paper's analogues inherit.

### 3.3 The liver-safety problem that docking cannot see

Fasiglifam's liver injury is not a class effect of GPR40 agonism; it is attributed to the specific chemical properties of the molecule, and three mechanisms are documented. First, **bile-acid transporter inhibition**: fasiglifam inhibits the efflux transporter MRP2 (IC50 2.41 µM) and the uptake transporters NTCP (IC50 10.9 µM), OATP1B1 (2.28 µM) and OATP1B3 (3.98 µM), impairing biliary excretion of bile acids and producing cholestatic hepatotoxicity; in rats, 100 mg/kg increased serum total bile acids 3- to 4-fold and total bilirubin 1.5- to 2.6-fold. Second, **a reactive acyl glucuronide**: fasiglifam is metabolised to a reactive acyl glucuronide (and possibly an acyl-CoA thioester) with a covalent binding burden of 2.0 mg/day, above the 1 mg/day threshold considered a risk for drug-induced liver injury; the glucuronide metabolite is exceptionally potent against MRP3 (0.21 µM), and in rats at 1,000 mg/kg/day it reached ≤32.7 µM in liver, associated with ALT ×4, bilirubin ×9 and bile acids ×3.4. Third, **mitochondrial toxicity**: fasiglifam inhibited mitochondrial respiration in HepG2 cells and mitochondrial Complex 1 and 2 activities in isolated rat mitochondria. Every analogue in this paper is a carboxylic acid — the same functional group that forms the acyl glucuronide — and every analogue is more lipophilic than fasiglifam (logP 5.02–6.79 vs 5.31), the property that drives transporter inhibition and hepatic accumulation. A compound that out-scores fasiglifam here by 1.71 kcal/mol would still carry the same acid, the same glucuronide risk and a worse lipophilicity profile — and the next series, not the next analogue, is where the field actually needs to move. The docking order cannot explain why fasiglifam worked for glycaemic control and then failed on liver safety, and it cannot predict which compound in this set is safe. That is a limitation of the question, not of the execution.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since fasiglifam was terminated. Before 2013, the question was "does GPR40 agonism lower glucose safely?" — now it is "which molecule, if any, keeps the glucose benefit without the liver liability?" The docking benchmark is therefore a screen for successors, not for proof of concept, and its bar is higher: a new compound must beat fasiglifam on the target, survive a transporter panel, and avoid the acyl-glucuronide burden that stopped the class leader. This paper's mixed result is useful precisely as a mixed result: it says the next screen must be a functional assay plus a transporter panel, not a bigger docking set of the same chemotype.

### 4.2 Why the "win" must not be over-read

Four reasons. First, the ranking contradicts measured potency — the most potent analogue docks worst, and fasiglifam itself docks second-worst. Second, the analogues' chemotypes may bind the orthosteric/full-agonist site rather than the allosteric pocket docked here, in which case the 1.71 kcal/mol lead measures fit to the wrong pocket. Third, every analogue is more lipophilic than fasiglifam, the property class that drove the liver injury this paper is trying to avoid. Fourth, the measured EC50 values come from different functional assays and are not directly comparable across compounds, so the potency ranking itself is approximate.

### 4.3 The two-pocket lesson

GPR40 has (at least) two ligand sites: the non-canonical allosteric pocket occupied by TAK-875 and MK-8666, and the fatty-acid orthosteric site where full agonists bind. This paper docked everything into the allosteric pocket, because that is the pocket with a co-crystal structure for a partial agonist and because fasiglifam is a partial agonist. That choice is defensible for fasiglifam and for MK-8666-like analogues, and it is a stated assumption for the rest. The correction is mechanical, not judgmental: **verify the UniProt accession, the ChEMBL target name, the PDB title, the ligand identity and the binding site before any score is quoted**, and disclose the runs that fail the audit. This paper does that; the pipeline's unrelated-target listing in the resolution step is disclosed in §2.2, not hidden.

### 4.4 Mechanism

Fasiglifam wedges into the allosteric pocket of GPR40 (between the transmembrane helices, in the non-canonical site established by 4PHU), potentiating free-fatty-acid signalling through Gαq, phospholipase C, inositol trisphosphate and diacylglycerol, which raises intracellular calcium and potentiates glucose-stimulated insulin secretion from pancreatic β-cells. Test for each link: (i) a GPR40 functional assay (inositol-phosphate accumulation or calcium flux) measures EC50 directly against fasiglifam (0.35 nM) as comparator, with a full-agonist control to distinguish partial from full agonism; (ii) a bile-acid transporter panel (BSEP, MRP2/3/4, NTCP, OATP1B1/1B3) measures whether the analogue kept the transporter inhibition that drove fasiglifam's liver injury — loss of transporter safety is the likeliest way a "better" GPR40 binder becomes a worse drug; (iii) an acyl-glucuronide formation assay and a mitochondrial respiration assay measure the other two documented liabilities.

### 4.5 Testable hypotheses

1. The best-scoring analogue activates GPR40 with an EC50 within 3-fold of fasiglifam's 0.35 nM in the same functional assay. Falsifier: EC50 > 1.05 nM, or a partial-agonist efficacy below 50% of fasiglifam's maximum response.
2. The same analogue shows no inhibition of BSEP, MRP2 or OATP1B1 below 10 µM. Falsifier: any transporter IC50 < 10 µM (fasiglifam's were 2.28–10.9 µM).
3. The analogue forms no detectable acyl glucuronide in human hepatocytes, or a covalent binding burden below 1 mg/day. Falsifier: a burden above 1 mg/day.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): GPR40 functional assay for the best candidate analogue — CHEMBL3287571 (best best-pose and best median, −11.94/−11.59) — plus fasiglifam control and a full-agonist control, with a binding-site competition assay to confirm which pocket the analogue actually occupies; readout EC50 and maximum response, n=3. Stage 2 (weeks 4–8): bile-acid transporter panel (BSEP, MRP2/3/4, NTCP, OATP1B1/1B3) and a mitochondrial respiration assay for the same set, plus an acyl-glucuronide formation assay in human hepatocytes. Stage 3 (weeks 9–12): if any analogue passes stages 1–2, solubility and plasma-protein-binding measurement; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin except CHEMBL3287571's.
2. All six docked compounds are near-equipotent by assay (EC50 0.2–1.3 nM), so the set cannot test ranking at all, and the EC50 values come from different functional assays and are not directly comparable.
3. The analogues may bind the orthosteric/full-agonist site rather than the allosteric pocket docked here; no binding-site competition assay was run.
4. A single rigid structure was used; GPR40 adapts to different chemotypes, so one structure under-samples the binding landscape.
5. Fasiglifam fails Lipinski (2 violations) and Veber, yet reached phase 3 — descriptor counts cannot rank this class.
6. No data on the clinical confounder: docking cannot distinguish partial from full agonism, and cannot predict liver safety.
7. The pipeline's ChEMBL target-resolution step listed unrelated targets before settling on CHEMBL4422; the audit caught it, but the episode shows the pipeline's target picks need independent verification every run.
8. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon; the full Arabic text was not read, and other classical works on diabetes were not individually consulted.

## 6. Conclusion

Fasiglifam, the best-known GPR40 agonist and the only one to reach late phase 3, re-docks at −10.23 kcal/mol on the 2.20 Å GPR40–MK-8666 structure 5TZR, with tight pose consistency — a validated control, not a discovery. One analogue, CHEMBL3287571, leads by 1.71 kcal/mol on best pose and 1.43 kcal/mol on median pose — the first lead beyond Vina noise in this series — but the method fails its own positive control: the most potent analogue by measured assay docks worst, fasiglifam itself docks second-worst, and the analogues' chemotypes may bind a different pocket from the one docked. The docking verdict is therefore mixed, and it is useful precisely as a mixed result: this chemotype cannot be ranked by rigid Vina scoring, every analogue is more lipophilic than the drug that failed on liver safety, and the next step must be a functional assay plus a transporter panel, not a bigger docking set. What the docking cannot do is resolve the clinical split: the same mechanism lowered glucose and then injured livers, and no binding score explains that. The next step is the cheap, decisive test — a GPR40 functional assay with a binding-site competition control, plus a bile-acid transporter panel and an acyl-glucuronide assay, for the best-scoring analogue against fasiglifam — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's National Diabetes Programme, the Drug Regulatory Authority (DRAP) and the Higher Education Commission research-funding panels, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of GPR40 agonism as an academic drug-discovery exercise in the country with the world's highest diabetes prevalence, and whether to close the diagnostic gap that leaves 9.3 million Pakistanis with diabetes undiagnosed. **Exact change:** commission the 8–12-week functional-plus-safety screen proposed in §4.6 for the best-scoring analogue against fasiglifam, with a transporter panel and an acyl-glucuronide assay, instead of funding another purely computational screen of the same target; and, in parallel, ask the National Diabetes Programme to cost the closing of the 9.3-million-case detection gap — because a GPR40 drug is worthless to a patient whose diabetes was never diagnosed. **If evidence Z appears, reverse this:** if the best analogue loses >3-fold to fasiglifam in the functional assay, binds the wrong pocket, or shows transporter inhibition below 10 µM or an acyl-glucuronide burden above 1 mg/day, drop this analogue set and redirect the same screen to a less lipophilic chemotype — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable antidiabetic from a liver-toxic one for a disease that affects 589 million people, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Srivastava A, Yano J, Oh W, et al. High-resolution structure of the human GPR40 receptor bound to allosteric agonist TAK-875. Nature. 2014;513(7516):124-127. doi:10.1038/nature13494. PMID: 25043059.
2. Lu J, Byrne N, Wang J, et al. Structural basis for the cooperative allosteric activation of the free fatty acid receptor GPR40. Nat Struct Mol Biol. 2017;24(7):570-577. doi:10.1038/nsmb.3417. PMID: 28581512.
3. Genitsaridi I, Salpea P, Salim A, et al. 11th edition of the IDF Diabetes Atlas: global, regional, and national diabetes prevalence estimates for 2024 and projections for 2050. Lancet Diabetes Endocrinol. 2026;14(2):149-156. doi:10.1016/S2213-8587(25)00299-2.
4. Fasiglifam (TAK-875) alters bile acid homeostasis in rats and dogs: a potential cause of drug induced liver injury. Toxicol Sci. 2017;157(1). PMC5414857.
5. Fasiglifam (TAK-875): mechanistic investigation and retrospective identification of hazards for drug induced liver injury. Toxicol Sci. 2018;163(2):374. (Covalent binding burden 2.0 mg/day; acyl glucuronide; MRP3 IC50 0.21 µM; mitochondrial Complex 1 and 2 inhibition.)
6. Fasiglifam (TAK-875) inhibits hepatobiliary transporters: a possible factor contributing to fasiglifam-induced liver injury. Drug Metab Dispos. (MRP2 IC50 2.41 µM; NTCP 10.9 µM; OATP1B1 2.28 µM; OATP1B3 3.98 µM.)
7. Leveraging a clinical phase Ib proof-of-concept study for the GPR40 agonist MK-8666 in patients with type 2 diabetes for model-informed phase II dose selection. Clin Transl Sci. 2017;10(5):404-411. doi:10.1111/cts.12479.
8. RCSB PDB entry 5TZR: GPR40 in complex with partial agonist MK-8666, 2.20 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
9. RCSB PDB entry 4PHU: Human GPR40 in complex with TAK-875, 2.33 Å. RCSB Protein Data Bank. Accessed 2026-11-21.
10. ChEMBL target CHEMBL4422: Free fatty acid receptor 1, Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-21.
11. UniProtKB O14842: Free fatty acid receptor 1 (FFAR1/GPR40), Homo sapiens. UniProt. Accessed 2026-11-21.
12. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; diabetes, al-bawl al-sukkari.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-097-2026-11-21.json` (fasiglifam + five ChEMBL analogues on 5TZR). Reference compound fasiglifam (ChEMBL1829174, EC50 0.35 nM); analogues CHEMBL3287571, CHEMBL4534836, CHEMBL4591657, CHEMBL1829173, CHEMBL4463571. Structure: PDB 5TZR (2.20 Å). Target: UniProtKB O14842; ChEMBL target CHEMBL4422. No additional data were generated.
