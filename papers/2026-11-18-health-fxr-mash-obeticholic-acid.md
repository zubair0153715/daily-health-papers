# Sub-Nanomolar FXR Agonists Out-Dock Obeticholic Acid on the CDCA-Bound FXR Structure — but All Four Are Lipinski Failures and the Pruritus–LDL Trade-Off Is a Class Problem, Not a Potency Problem

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-18 · **Health Papers Agent — Paper #76** (daily 5-paper run)

**Keywords:** FXR; farnesoid X receptor; MASH; MASLD; obeticholic acid; molecular docking; pruritus; LDL cholesterol

---

## Abstract

Obeticholic acid (OCA), the first farnesoid X receptor (FXR) agonist, improved liver histology in MASH but failed regulatory approval for the indication: its antifibrotic benefit travels with dose-dependent pruritus (23% vs 6% on placebo in FLINT; up to 51% at higher doses) and a pro-atherogenic lipid shift (higher LDL cholesterol, lower HDL), and its United States NASH programme ended with a Complete Response Letter in 2023. We asked whether more potent FXR agonists solve this problem. Using the LeadForge pipeline (UniProtKB Q96RI1 → ChEMBL target CHEMBL2047, 57 bioactivities → PubChem/RDKit similarity, PAINS and ADMET screen → AutoDock Vina 1.2.7), we docked the top four leads and OCA on the FXR ligand-binding domain structure 6HL1 (1.6 Å, chenodeoxycholic acid bound), centred on the co-crystallised bile acid. The four leads scored −10.42 to −8.88 kcal/mol versus −8.39 kcal/mol for re-docked OCA, and their measured potencies are sub-nanomolar (EC50 0.1, 0.1 and 0.251 nM; IC50 0.09 nM). The honest limit: all four are highly lipophilic (logP 6.2–8.4), three carry two Lipinski violations and molecular weights above 600 Da, one lead's pose set includes a +8.90 kcal/mol non-binding mode, and docking cannot measure partial agonism, pruritus or LDL effects at all — the liabilities that actually killed OCA. The claim that greater FXR potency means a better MASH drug would be refuted if these leads show full-agonist suppression of CYP7A1 per unit of antifibrotic signal, or pruritus/LDL signals in the same range as OCA in a relevant model. The falsifiable next step is a partial-agonism assay (co-regulator recruitment plus CYP7A1 suppression) and a lipid/pruritus read-out for the two least lipophilic leads, not another affinity screen.

---

## 1. Introduction

Metabolic dysfunction-associated steatotic liver disease (MASLD) is the most prevalent chronic liver disease worldwide, affecting roughly one in three adults, and its progressive inflammatory form, metabolic dysfunction-associated steatohepatitis (MASH), can advance to fibrosis, cirrhosis and hepatocellular carcinoma. About 20% of people with MASLD have MASH. Pakistan carries a rising burden of the metabolic syndrome that drives MASLD — diabetes, obesity and dyslipidaemia — yet has almost no local MASH trial or registry infrastructure, so treatment decisions are imported from trials run elsewhere.

FXR is a nuclear bile-acid sensor that regulates bile-acid homeostasis, lipid metabolism, inflammation and fibrosis, and it was for a decade the most clinically advanced MASH target. OCA, a semi-synthetic derivative of chenodeoxycholic acid (6-ethyl-CDCA, INT-747), is the first and still the only FXR agonist approved for clinical use — conditionally, for primary biliary cholangitis (PBC) in 2016. In MASH it showed real antifibrotic signal: in the FLINT phase 2 trial (283 patients, OCA 25 mg daily for 72 weeks), 45% of OCA patients improved histologically versus 21% on placebo (relative risk 2.2, 95% CI 1.4–3.3; p = 0.0002), and REGENERATE showed ≥1-stage fibrosis improvement without worsening of MASH. But the benefit came with the liabilities that define the class: pruritus in 23% of OCA patients versus 6% on placebo in FLINT (up to 51% at higher doses), higher LDL and total cholesterol, lower HDL, higher alkaline phosphatase and rising insulin/HOMA. The US NASH application received a Complete Response Letter in 2023, Intercept discontinued NASH-directed investment, and EU commercialisation of OCA was discontinued in 2024. Meanwhile the field moved on: resmetirom, a liver-directed thyroid-hormone-receptor-β agonist, received accelerated US approval in 2024 after biopsy-based phase 3 data, and semaglutide 2.4 mg received accelerated US approval for MASH in 2025. Second-generation FXR agonists — cilofexor, tropifexor, vonafexor, EDP-305, nidufexor — mostly stalled in phase 2 or were discontinued.

The classical canon knew the liver as the seat of metabolic disease: Ibn Sina's Canon of Medicine (c. 1025), Book III, discusses diseases of the liver ("kabid") and their systemic effects, and Al-Razi's Kitab al-Hawi records clinical observation of jaundice and hepatic wasting. These texts described the syndrome without any concept of steatohepatitis or nuclear receptors; they are hypothesis sources, not evidence. The Islamic principle behind acting on MASH is hifz al-nafs (preservation of life) with maslaha (public benefit): a disease affecting a third of adults, with no approved FXR therapy, is exactly the kind of burden where a cheap, discriminating test beats another round of untested claims (see §7).

**Falsifiable question.** Do sub-nanomolar FXR agonists bind the bile-acid pocket of FXR more strongly than obeticholic acid, and does stronger binding predict a better efficacy–liability profile for MASH? **Falsifier:** if the leads behave as full agonists (CYP7A1 suppression per unit of antifibrotic signal no better than OCA) or carry pruritus/LDL signals in the same range as OCA in a relevant model, the potency claim is refuted. **Causal identification:** validated-control re-docking — OCA re-docked on a bile-acid-bound FXR structure — not a comparison against nothing. Association only beyond that: docking scores are not activity, and affinity is not partial agonism.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-18: 2025–2026 reviews and primary sources on FXR agonists in liver disease (Pharmaceuticals 2025; Frontiers in Pharmacology 2026; World Journal of Hepatology 2026), the FLINT and REGENERATE results, the resmetirom and semaglutide approvals, and the RCSB record for PDB 6HL1. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025), Book III (liver); Al-Razi, Kitab al-Hawi (c. 900) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: human farnesoid X receptor (NR1H4), UniProtKB Q96RI1; ChEMBL bioactivity target CHEMBL2047 ("bile acid receptor", Homo sapiens). Structure: PDB 6HL1, the FXR ligand-binding domain with chenodeoxycholic acid (CDCA) bound and an NCoA-2 co-activator peptide, 1.6 Å ("Molecular tuning of farnesoid X receptor partial agonism", Nature Communications 2019). Grid centre: centroid of the co-crystallised CDCA via `dock._ligand_center`, [11.31, −14.17, 12.48], box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for OCA and all four leads.

**Structure audit.** 6HL1 is the correct domain and the correct site: it is the FXR ligand-binding domain with the endogenous bile-acid agonist CDCA in the pocket — the same pocket OCA occupies as a CDCA derivative. No correction was needed (contrast Paper #75, where the pipeline's first structure was the wrong domain and was discarded). CDCA is not a cofactor, glycan, lipid or modified residue, so the centre picker lands on the drug site.

### 2.3 PAINS screen

RDKit PAINS filter applied to all 26 pipeline leads. No lead carries a PAINS alert — including all four docked compounds.

### 2.4 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for every lead; ToxGuard Tox21 kNN read-across (12 assays) run for every lead. OCA itself (PubChem CID 447715, C26H44O4, MW 420.63) carries one Lipinski violation (logP 5.11) and passes Veber.

### 2.5 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No partial-agonism, co-regulator-recruitment, lipid or pruritus assay exists in this study — and those are the measurements that decide whether an FXR agonist is usable. Measured EC50/IC50 values below are ChEMBL records, not new measurements, and come from different assay formats.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | ChEMBL potency vs FXR* | Best affinity, 6HL1 (kcal/mol) | Top-3 poses (kcal/mol) | PAINS | MW / logP / Lipinski violations |
|---|---|---|---|---|---|
| CHEMBL5559957 | EC50 0.1 nM (pChEMBL 10.00) | **−10.42** | −10.42, −8.96, −7.93 | none | 608.57 / 8.41 / 2 |
| CHEMBL5559067 | EC50 0.1 nM (pChEMBL 10.00) | **−10.20** | −10.20, −9.84, **+8.90** | none | 623.67 / 8.00 / 2 |
| CHEMBL5912129 | EC50 0.251 nM (pChEMBL 9.60) | **−9.58** | −9.58, −9.46, −8.26 | none | 496.97 / 6.20 / 1 |
| CHEMBL4783777 | IC50 0.09 nM (pChEMBL 10.05) | **−8.88** | −8.88, −7.94, −6.87 | none | 615.68 / 6.44 / 2 |
| Obeticholic acid (reference, re-docked) | approved FXR agonist (PBC); failed for MASH | −8.39 | −8.39, −7.27, −7.18 | none | 420.63 / 5.11 / 1 |

\* ChEMBL-recorded potency against human bile-acid receptor FXR (target CHEMBL2047), retrieved live 2026-11-18. None of the four leads has a preferred name or any clinical phase in ChEMBL (max_phase: none) — all are preclinical chemotypes.

Three of the four leads out-score re-docked OCA, by 1.19–2.03 kcal/mol; the fourth (CHEMBL4783777) beats it by only 0.49 kcal/mol, inside noise. But the pose table carries two warnings. CHEMBL5559957's top-3 poses spread 2.49 kcal/mol (−10.42 to −7.93), poor consistency for a supposedly sub-nanomolar binder. CHEMBL5559067's third pose is +8.90 kcal/mol — a non-binding mode, meaning Vina found the ligand clashing in one of three runs. The headline −10.42 and −10.20 scores are the best of inconsistent sets, not reproducible minima.

### 3.2 The potency–druggability inversion

The measured potencies are extraordinary — EC50 0.09–0.251 nM, roughly three orders of magnitude more potent than a typical nanomolar lead — and that is precisely the problem. Every lead is extremely lipophilic (logP 6.2–8.4); three carry two Lipinski violations with molecular weights of 609–624 Da. These are greasy, oversized molecules: the kind that bind tightly in a hydrophobic nuclear-receptor pocket, accumulate in liver, and carry exactly the off-target and distribution liabilities that make FXR agonists hard to dose. OCA itself, at logP 5.11 and MW 421, already sits at the edge of drug-likeness and still produced pruritus in a quarter of patients and a pro-atherogenic lipid shift. Making the molecule greasier and 1,000-fold more potent does not address either liability; if anything it concentrates exposure where the liabilities live.

### 3.3 Toxicity read-across

Tox21 kNN read-across predicted no assay above 0.4 probability for any of the four leads (highest: NR-AhR 0.37 for CHEMBL5912129; SR-ARE 0.33 for CHEMBL4783777; none ≥0.3 for the two most potent leads). This is a weak screen — read-across, not measurement — and it cannot see pruritus (a sensory-neuronal, bile-acid-driven phenotype) or LDL elevation at all.

### 3.4 Comparison with published work

No published Vina study of these four ChEMBL compounds on 6HL1 was found in the sweep; the comparison here is internal (leads vs re-docked reference on the same structure, same protocol). The re-docked OCA score of −8.39 kcal/mol is the validated control: OCA is a CDCA derivative docked into the CDCA pocket, so a method that could not recover strong binding would be broken. The 6HL1 source paper itself (Nature Communications 2019) is about tuning partial agonism — the property this paper cannot measure — which is the right frame: the field's question is not "who binds tightest" but "who activates least while still working".

## 4. Discussion

### 4.1 The reframe

The FXR story has already answered the potency question: sub-nanomolar agonists exist (tropifexor EC50 0.2 nM; these four leads at 0.09–0.251 nM), and the class still failed in MASH. OCA's failure was not a failure of affinity — it was a failure of efficacy–liability separation. This paper's docking result therefore reframes the target: the next FXR candidate for MASH must be judged on partial agonism and tissue selectivity, not on beating OCA's −8.39 kcal/mol. A compound that scores −10.42 but behaves as a full agonist is a worse drug than one that scores −8.50 and behaves as a partial agonist.

### 4.2 Why the "win" must not be over-read

Four reasons. First, two of the four margins over OCA are large but the pose sets are inconsistent (2.49 kcal/mol spread; a +8.90 kcal/mol mode), so the best scores are not reproducible minima. Second, three leads fail Lipinski twice over — they are unlikely to become oral drugs without major rework. Third, docking measures affinity for one static pocket; FXR signalling depends on which co-regulators the ligand recruits, and Vina cannot see that. Fourth, pruritus and LDL elevation — the two liabilities that ended OCA's MASH programme — are invisible to every screen in this pipeline.

### 4.3 Mechanism

FXR activation in hepatocytes induces SHP, which suppresses CYP7A1 and bile-acid synthesis, and modulates lipid and inflammatory signalling via AMPK, MAPK and PI3K/AKT pathways; in ileal enterocytes it drives FGF19. The antifibrotic benefit and the lipid liability both flow from the same receptor, so separation must come from partial agonism (recruiting a subset of co-regulators), tissue-selective distribution (gut-restricted or liver-targeted), or combination with a lipid-lowering partner — not from more affinity. Test for each link: (i) co-regulator recruitment profiling distinguishes full from partial agonists; (ii) CYP7A1 suppression per unit of antifibrotic gene signal quantifies the separation; (iii) a lipid panel in a diet-induced MASH model measures the LDL cost directly.

### 4.4 Testable hypotheses

1. CHEMBL5912129 (the least lipophilic lead, logP 6.2, 1 violation) shows partial-agonist behaviour: ≤50% of OCA's maximal co-activator recruitment at saturating concentration. Falsifier: recruitment ≥80% of OCA's maximum.
2. At least one of the four leads suppresses CYP7A1 less per unit of antifibrotic signal (e.g. SHP induction) than OCA in primary human hepatocytes. Falsifier: no lead separates the two read-outs by ≥2-fold.
3. No lead's docking advantage survives a drug-likeness filter: the two most potent leads cannot be reformulated below logP 6 without losing >10-fold potency. Falsifier: a sub-600 Da, logP <5 analogue retains EC50 <1 nM.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): FXR co-regulator recruitment assay (TR-FRET) for the four leads + OCA control, reporting Emax and EC50; readout distinguishes full from partial agonists. Stage 2 (weeks 4–8): primary human hepatocyte assay — CYP7A1 suppression versus SHP/antifibrotic gene induction, with lipid-output read-out (ApoB secretion as an LDL proxy). Stage 3 (weeks 9–12): the single best-separated lead goes to a diet-induced MASH mouse model for liver fat, fibrosis markers and plasma lipids; if no lead separates efficacy from liability, publish the negative result — it confirms that potency is not the bottleneck.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol; two leads have inconsistent pose sets.
2. No partial-agonism, co-regulator, lipid or pruritus measurement exists in this work — the decisive properties are untested.
3. Measured EC50/IC50 values are ChEMBL records from different assay formats (EC50 vs IC50 mixed); they are not directly comparable across compounds.
4. Three leads fail Lipinski twice over (logP 6.4–8.4, MW >600 Da); drug-likeness is a major, unaddressed problem.
5. No molecular dynamics or free-energy refinement; the FXR pocket is flexible and co-regulator-dependent.
6. No Pakistan-specific MASH epidemiology or local patient data were available for this analysis.
7. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon (Book III, liver) and Al-Razi's Kitab al-Hawi; the full Arabic texts were not read, and other classical works on liver disease were not individually consulted.

## 6. Conclusion

Four sub-nanomolar FXR agonists dock at −10.42 to −8.88 kcal/mol on the CDCA-bound FXR structure 6HL1, against −8.39 kcal/mol for re-docked obeticholic acid, with no PAINS alerts. The result does not make any of them a better MASH drug: all four are highly lipophilic, three are Lipinski failures, two have inconsistent pose sets, and docking cannot measure the partial agonism, pruritus or LDL effects that actually decided OCA's fate. The value of this paper is the negative framing it forces — the FXR field does not need a tighter binder; it needs a partial agonist that separates antifibrotic efficacy from lipid and itch liabilities, and the cheap test for that is a co-regulator recruitment assay, not another affinity screen.

## 7. Policy implications

**Decision-maker:** Pakistan's drug regulator (DRAP) and the National Institute of Health, with the Pakistan Society for the Study of Liver Diseases as clinical adviser. **Decision:** whether any FXR agonist programme deserves scarce public research funding for MASH in Pakistan. **Exact change:** fund the 8–12-week partial-agonism screen proposed in §4.5 for the two least lipophilic leads (CHEMBL5912129 and CHEMBL4783777) before any proposal for animal efficacy work or clinical translation of an FXR agonist, and require every future FXR proposal to report a co-regulator-recruitment Emax and a lipid read-out alongside affinity — instead of accepting docking scores or EC50 values as evidence of a usable drug. **If evidence Z appears, reverse this:** if a lead shows partial-agonist behaviour with a ≥2-fold efficacy–liability separation, escalate it to the diet-induced MASH model; if none separates, drop FXR agonism for MASH in the local programme and redirect the same funds to the approved mechanisms (resmetirom-class THR-β agonism or GLP-1-based therapy) rather than chasing a tighter binder. The Islamic principle is hifz al-nafs with maslaha: public money for a disease affecting a third of adults must buy a discriminating test, not another untested potency claim; funding a full agonist on affinity alone would spend the community's resources on a known failure mode.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Obeticholic acid and other farnesoid-X-receptor (FXR) agonists in the treatment of liver disorders. Pharmaceuticals. 2025;18(9):1424. doi:10.3390/ph18091424.
2. Obeticholic acid as an index farnesoid X receptor scaffold in metabolic dysfunction-associated steatohepatitis: a testable model for efficacy-liability separation and biomarker interpretation. Front Pharmacol. 2026. doi:10.3389/fphar.2026.1879097.
3. Molecular tuning of farnesoid X receptor partial agonism. Nat Commun. 2019. doi:10.1038/s41467-019-10853-2. PMID: 31266946.
4. Sanyal AJ, Lopez P, Lawitz EJ, Lucas KJ, Loeffler J, Kim W, Goh GB, Huang JF, Serra C, Andreone P, et al. Tropifexor for nonalcoholic steatohepatitis: an adaptive, randomized, placebo-controlled phase 2a/b trial. Nat Med. 2023;29:392-400.
5. Patel K, Harrison SA, Elkhashab M, Trotter JF, Herring R, Rojter SE, Kayali Z, Wong VWS, Greenbloom S, Jayakumar S, et al. Cilofexor, a nonsteroidal FXR agonist, in patients with noncirrhotic NASH: a phase 2 randomized controlled trial. Hepatology. 2020;72:58-71.
6. Rinella ME, Neuschwander-Tetri BA, Siddiqui MS, Abdelmalek MF, Caldwell S, Barb D, Kleiner DE, Loomba R. AASLD Practice Guidance on the clinical assessment and management of nonalcoholic fatty liver disease. Hepatology. 2023.
7. Harrison SA, Bedossa P, Guy CD, Schattenberg JM, Loomba R, Taub R, Labriola D, Moussa SE, Neff GW, Rinella ME, et al. A phase 3, randomized, controlled trial of resmetirom in NASH with liver fibrosis. N Engl J Med. 2024.
8. ChEMBL target CHEMBL2047: bile acid receptor (farnesoid X receptor, NR1H4), Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-18.
9. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; diseases of the liver, Book III.)
10. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; clinical observation of hepatic disease.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-062-2026-11-18.json`. Ligand identities are ChEMBL IDs CHEMBL5559957, CHEMBL5559067, CHEMBL5912129, CHEMBL4783777; reference drug obeticholic acid, PubChem CID 447715. Structure: PDB 6HL1 (1.6 Å). Target: UniProtKB Q96RI1; ChEMBL target CHEMBL2047. No additional data were generated.
