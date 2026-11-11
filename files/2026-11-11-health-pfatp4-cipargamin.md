# No Structure to Dock On: A ChEMBL Potency Analysis of PfATP4 Inhibitors Against Cipargamin, and Why the Best Number Is a 3D7-Only Number

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-11 · **Health Papers Agent — Paper #42** (daily 5-paper run)

**Keywords:** PfATP4; cipargamin; malaria; artemisinin resistance; spiroindolone; ChEMBL; G358S; Plasmodium falciparum

---

## Abstract

Malaria caused an estimated 282 million cases and 610,000 deaths in 2024, and partial artemisinin resistance is now confirmed or suspected in at least eight African countries, so a drug with a new mechanism is no longer optional. Cipargamin (KAE609), a spiroindolone that inhibits the parasite sodium pump PfATP4, cleared parasites in a median of 8 hours versus 24 hours for artemether-lumefantrine in a phase II trial, but day-28 cure was only just over 65% and the PfATP4 G358S mutation appeared in 65% of treatment failures, so the next PfATP4 drug must beat cipargamin on resistance, not on speed. We ran the LeadForge pipeline (UniProtKB A0A143ZZK9, corrected ChEMBL target CHEMBL6066156, 26 bioactivities across 7 compounds, PubChem verification of cipargamin, RDKit ADMET and PAINS screen) and analysed the four PfATP4 actives with measured potency against cipargamin, with docking deliberately SKIPPED because no X-ray structure of PfATP4 exists. The best record is a dihydroquinazolinone S-enantiomer at EC50 4.6 nM on the 3D7 strain, against cipargamin's literature IC50 of 0.5 to 1.4 nM, but the same compound collapses to 4,100 nM on the Dd2 strain and 7,500 nM on the G358S mutant, while its R-enantiomer holds 18.2, 26.4 and 81.3 nM across the same three assays, and two N-acetamide indoles score 150 and 790 nM with PAINS alerts. The falsifiable next step is a head-to-head Na+-ATPase assay of the two enantiomers plus cipargamin on 3D7, Dd2 and G358S membrane preparations on the same plate: a lead only matters if it keeps potency where the S-enantiomer loses it.

---

## 1. Introduction

The World Health Organization's World Malaria Report 2025 estimates 282 million malaria cases and 610,000 deaths in 2024, about 95% of deaths in the African Region and mostly in children under five, with cases rising by roughly 9 million on the previous year. Partial resistance to artemisinin derivatives — the backbone of treatment for two decades — is now confirmed or suspected in at least eight African countries, with early signs that partner drugs are also losing efficacy. Pakistan illustrates the stakes close to home: after the 2022 floods added 6.6 million cases over three years, the country treated 2 million confirmed cases in 2024, down from a peak of 2.7 million in 2023 but far above the 399,097 cases of 2021, and the World Malaria Report 2025 puts Pakistan above 3 million estimated cases a year. A new antimalarial mechanism is therefore a public-health requirement, not a research luxury.

PfATP4 is the most advanced new mechanism. It is a P-type cation-transporting ATPase (1,264 amino acids, gene PF3D7_1211900) on the parasite plasma membrane that extrudes sodium against an inward gradient, maintaining the low cytosolic sodium the intraerythrocytic parasite needs to survive. The spiroindolone NITD609 was identified in 2010 as a fast-acting, low-nanomolar schizonticide whose activity was abolished by mutations in the gene encoding PfATP4, and in 2013 Spillman and colleagues showed directly that PfATP4 is a sodium efflux pump and that spiroindolones disrupt parasite sodium homeostasis through it. Cipargamin — NITD609 renamed, KAE609 — is the most advanced compound in the class: in vitro IC50 values of 0.5–1.4 nM against drug-sensitive and drug-resistant laboratory strains, activity against artemisinin-resistant isolates carrying kelch13 mutations (asexual blood-stage IC50 2.4 nM), and activity against mature stage V gametocytes, suggesting transmission-blocking potential.

Clinically, cipargamin is fast but fragile. In the randomised, open-label, dose-escalation phase II trial in sub-Saharan Africa (NCT03334747), single doses of 50–150 mg gave a median parasite clearance time of 8 hours versus 24 hours for artemether-lumefantrine, but PCR-corrected adequate clinical and parasitological response at day 28 was only just over 65% for each dose, and the treatment-emerging PfATP4 mutation G358S was detected in 65% of treatment failures. Hepatic safety was acceptable (2 of 135 cipargamin patients versus 2 of 51 controls with grade ≥2 liver-enzyme rises), so the drug's problem is not tolerability but resistance: a single point mutation, selected within one trial, undoes a monotherapy. Cipargamin will therefore only ever be used with a combination partner, and the partner — or the next PfATP4 inhibitor — must be chosen on resistance coverage, not on speed.

Structural biology has just caught up. Until October 2025 there was no experimental PfATP4 structure at all, which is why this topic was previously filed as undockable. On 20 October 2025 Haile and colleagues published a 3.7 Å cryo-EM structure of endogenous PfATP4 purified from CRISPR-engineered parasites (PDB 9N10, EMDB 48800/48801), revealing the ATP and ion-binding sites and a previously unknown apicomplexan-specific binding partner, PfABP — and showing that the experimental model differs from earlier homology models by 10.3–22.9 Å RMSD. That difference is itself a warning: any docking done on a homology model of PfATP4 before October 2025 was docking on a wrong shape.

**Hypothesis (falsifiable):** among ChEMBL PfATP4 actives, the best 3D7 potency does not identify the best lead — the ranking that matters is potency retained across parasite strains (3D7 versus Dd2) and on the G358S mutant that defeated cipargamin in the clinic. The test is a head-to-head Na+-ATPase assay of the top leads and cipargamin on 3D7, Dd2 and G358S preparations on the same plate.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-11 (web search; PubMed via the daily digest of 2026-11-11). Key sources: the WHO World Malaria Report 2025 and WHO EMRO Pakistan figures; Rottmann et al. 2010 for the spiroindolone discovery and NITD609 potency; Spillman et al. 2013 for PfATP4 as the sodium pump and spiroindolone target; Schmitt et al. 2022 for the phase II efficacy and the G358S finding; Ndayisaba et al. 2021 for hepatic safety; Yipsirimetee et al. 2022 for activity against artemisinin-resistant isolates and gametocytes; Haile et al. 2025 for the cryo-EM structure; Ashton et al. 2024 and Awalt et al. 2025 for the two newest PfATP4 chemotypes in ChEMBL. Every citation in the References section was verified (journal, year, DOI or PMID checked, not invented).

### 2.2 ChEMBL potency analysis (docking SKIPPED — see 2.3)

Standardised LeadForge pipeline, exactly as Papers #1/#3, except for the corrected target and the skipped docking step: UniProtKB A0A143ZZK9 → corrected ChEMBL target CHEMBL6066156 (see correction below), 26 bioactivities retrieved → PubChem verification of cipargamin (CID 44469321) → RDKit Morgan-fingerprint similarity screen versus cipargamin → RDKit ADMET/PAINS + ToxGuard Tox21 kNN → composite lead ranking (similarity × 40 + Lipinski × 20 + Veber × 10 + PAINS × 10 + tox × 20). The four compounds with a pChEMBL value are reported with their best ChEMBL record; all other records for those compounds (strain and mutant variants) are reported alongside, because the strain comparison is the point of this paper.

**Target correction (verified live, 2026-11-11):** the pipeline's default path is wrong for this target. The UniProtKB lookup itself is correct — A0A143ZZK9, "P-type sodium-transporting ATPase4", Plasmodium falciparum (isolate 3D7), 1,264 amino acids — but the pipeline's ChEMBL target lookup returns a list of unrelated human targets and takes the first: CHEMBL2074, "Maltase-glucoamylase", Homo sapiens (UniProt O43451). Step 2 of the first run therefore queried maltase-glucoamylase bioactivities and found 0 — correctly, for the wrong enzyme. The true PfATP4 target was found by direct ChEMBL API lookup (target component accession A0A143ZZK9 → component 23361 → CHEMBL6066156, "P-type sodium-transporting ATPase4", SINGLE PROTEIN, Plasmodium falciparum isolate 3D7), and the run was repeated with only that lookup overridden (driver script `run_docking_pfatp4.py`, kept in the pipeline directory). The first run's step-2 zero is discarded; its UniProt and PubChem steps were correct and are retained.

### 2.3 Why docking was skipped

Two independent reasons, both verified. First, the pipeline's structure picker is X-ray-only by design, and no X-ray structure of PfATP4 exists. Second, the only experimental structure that does exist — the 3.7 Å cryo-EM structure PDB 9N10 (Haile et al. 2025) — carries no bound inhibitor, so there is no co-crystallised ligand from which to derive a grid centre, and its atomic model covers only 982 of the 1,264 residues. Hand-rolling a grid centre on 9N10 (from the sodium site, the ATP site, or a homology-model pocket) would repeat the 2026-11-11 TYK2 centre-pick error, in which a hand-picked centre produced a bogus docking score. The pipeline uses `dock._ligand_center` and never a hand-rolled pick; with no ligand in the structure there is nothing for it to centre on. Rigid AutoDock Vina docking on a 3.7 Å cryo-EM apo structure of a membrane pump in complex with an uncharacterised modulator protein (PfABP) would produce numbers that look like results and are not. The AlphaFold model of PfATP4 was not used either: Haile et al. show the experimental model differs from homology-based predictions by 10.3–22.9 Å RMSD, so a predicted model is not a substitute for an experimental binding site. The paper is therefore a potency and resistance-landscape analysis, and says so in its title.

### 2.4 PAINS screen

RDKit PAINS filter applied to every lead. Two of the four leads carry a PAINS alert (Section 3.1); the alerts are reported, not hidden, and they change the validation design (Section 4.3).

### 2.5 Honesty limits

No docking was performed, so there are no docking scores or binding-mode claims in this paper at all — nothing is inferred about where any compound binds PfATP4. "Measured" potencies are single-assay ChEMBL maxima from biochemical Na+-ATPase activity assays (type B), not whole-parasite growth inhibition and not head-to-head values; EC50 figures from the 2024 series and IC50 figures from the 2025 series come from different laboratories, years and assay setups and cannot be ranked against each other as if they were measured on one plate. Cipargamin itself has no bioactivity record against CHEMBL6066156 in ChEMBL at all — its potency figures in this paper are literature values (Rottmann et al. 2010; Yipsirimetee et al. 2022), not ChEMBL records. The pipeline's composite score is dominated by similarity to cipargamin (40 of 100 points), so it ranks analogues above different chemotypes by construction. No experimental data were generated.

## 3. Results

### 3.1 Potency: the comparison table

| Rank (composite score) | Compound | Similarity to cipargamin | Composite score | Best ChEMBL record (pChEMBL) | PAINS |
|---|---|---|---|---|---|
| 1 | Cipargamin (query, PubChem CID 44469321) | 1.000 | 98.5 | Literature: IC50 0.5–1.4 nM (Rottmann et al. 2010); no ChEMBL record on this target | none |
| 2 | CHEMBL5591927 — dihydroquinazolinone-3-carboxamide, S-enantiomer | 0.173 | 64.7 | EC50 4.6 nM (8.34), 3D7 Na+-ATPase assay | none |
| 3 | CHEMBL5594154 — dihydroquinazolinone-3-carboxamide, R-enantiomer | 0.173 | 64.7 | EC50 18.2 nM (7.74), 3D7 Na+-ATPase assay | none |
| 4 | CHEMBL6174048 — N-acetamide indole | 0.135 | 53.0 | IC50 150 nM (6.82), 3D7 Na+-ATPase assay | PAINS alert |
| 5 | CHEMBL6175630 — N-acetamide indole | 0.120 | 52.5 | IC50 790 nM (6.10), 3D7 Na+-ATPase assay | PAINS alert |

Cipargamin itself is clean by the pipeline's drug-likeness panel: MW 390.25, logP 4.34, 3 hydrogen-bond donors, 2 acceptors, TPSA 56.92 Å², 0 rotatable bonds, zero Lipinski violations, formula C19H14Cl2FN3O, no PAINS alert. Its ToxGuard Tox21 kNN read-across gives the highest predicted activity on the oxidative-stress response assay SR-ARE (0.407) — a prediction, not a measurement. The four leads are likewise Lipinski-clean (MW 365–469, logP 2.82–4.33, zero violations), and their ToxGuard profiles are quiet (highest single-assay predictions 0.27–0.51, all kNN read-across, not measurements).

The two dihydroquinazolinone records (ranks 2–3) are the two enantiomers of one scaffold from Ashton et al. 2024: identical molecular weight (468.88), logP (2.82) and descriptors, mirror-image SMILES, and the S-enantiomer is the more potent on 3D7 (4.6 versus 18.2 nM) — consistent with Ashton et al. advancing the S-enantiomer (S-WJM992) as frontrunner, a compound that inhibited PfATP4 Na+-ATPase activity, blocked gamete development, and showed efficacy in a mouse malaria model. The two N-acetamide indoles (ranks 4–5) are from Awalt et al. 2025, whose frontrunner WJM664 showed potent asexual-stage activity and transmission-blocking activity but low efficacy in the mouse model, attributed to PfATP4 species differences and moderate systemic exposure.

### 3.2 The strain problem: the best number is a 3D7-only number

The ChEMBL record for the S-enantiomer contains more than its headline 4.6 nM. The same compound was assayed on three parasite preparations in the same study (Ashton et al. 2024, document CHEMBL5576146):

| Compound | 3D7 wild type (CHEMBL5579326) | Dd2 wild type (CHEMBL5579327) | Dd2 G358S mutant (CHEMBL5579328) |
|---|---|---|---|
| CHEMBL5591927 (S-enantiomer) | EC50 4.6 nM | EC50 4,100 nM | EC50 7,500 nM |
| CHEMBL5594154 (R-enantiomer) | EC50 18.2 nM | EC50 26.4 nM | EC50 81.3 nM |

The S-enantiomer loses ~890-fold going from 3D7 to Dd2 wild type, and a further ~1.8-fold on the G358S mutant (7,500 nM). The R-enantiomer, four-fold weaker on 3D7, is stable: 18.2 → 26.4 nM across strains (1.5-fold) and 81.3 nM on G358S (3.1-fold versus its own Dd2 wild type). On the Dd2 background the "worse" enantiomer is ~155-fold more potent than the "better" one (26.4 versus 4,100 nM), and on the G358S mutant it is ~92-fold more potent (81.3 versus 7,500 nM). The pipeline's best-record ranking, which takes the single highest pChEMBL value per compound, reports only the 4.6 nM and hides all of this: a reader who took Table 3.1 at face value would advance the wrong enantiomer.

Two cautions before this is over-read. First, these are biochemical Na+-ATPase activity EC50s on membrane preparations, not whole-parasite growth inhibition; a strain difference in a membrane assay may reflect preparation or assay conditions as well as target pharmacology, and the 3D7-versus-Dd2 gap for the S-enantiomer is large enough to demand replication before any mechanistic claim. Second, the G358S shift itself is small for both enantiomers (1.8-fold and 3.1-fold versus their own Dd2 wild type): unlike cipargamin, whose G358S mutation was treatment-emergent in the clinic, this chemotype shows no catastrophic cross-resistance to the cipargamin resistance mutation — the S-enantiomer's problem on Dd2 is present before G358S is introduced.

### 3.3 What the pipeline's filter hides

ChEMBL6066156 carries 26 bioactivities across 7 compounds, but only 4 compounds have a pChEMBL value, because the pipeline's step 2 filters on pChEMBL ≥ 5. Two further N-acetamide indoles (CHEMBL6150594, CHEMBL6162944) each record IC50 ~400 nM in the same 2025 assay series (CHEMBL6119961) with the standard relation "~" rather than "=", so ChEMBL assigns them no pChEMBL value and the pipeline excludes them entirely. Sixteen of the 26 activities are single-concentration percentage-inhibition records at 2 µM in the Na+-ATPase assays, including artenimol (CHEMBL307261, dihydroartemisinin) — a negative control of sorts, since artemisinin's target is not PfATP4. The honest count of the evidence base is therefore: four compounds with a usable potency value, two more at ~400 nM hidden by a filter, and the rest single-point screens. The PfATP4 ChEMBL target is thin — 26 activities, two documents — because most PfATP4 pharmacology lives in whole-parasite growth assays annotated to the organism rather than the target, and cipargamin itself is not among the target's compounds at all.

### 3.4 Comparison with published potency data

The literature values for cipargamin are stronger than any ChEMBL record in this analysis: Rottmann et al. 2010 report IC50 0.5–1.4 nM across laboratory strains, and Yipsirimetee et al. 2022 report asexual blood-stage IC50 2.4 ± 0.7 nM against artemisinin-resistant isolates (kelch13 C580Y, G449A, R539T), with male gametocyte IC50 115.6 ± 66.9 nM and female gametocyte IC50 104.9 ± 84.3 nM. The best ChEMBL lead (4.6 nM, 3D7 Na+-ATPase EC50) is therefore not more potent than cipargamin by any measure — it is roughly 3- to 9-fold weaker than cipargamin's best literature values, on a different assay type, and it collapses on Dd2. The 2024 and 2025 chemotypes are best read as proof that PfATP4 accepts more than one chemotype, not as potency improvements on cipargamin. The clinical comparison that matters is the one already published: cipargamin clears parasites in 8 hours but cures only just over 65% at day 28 as monotherapy, with G358S in 65% of failures.

## 4. Discussion

### 4.1 The reframe

The question was whether a standardised screen can rank new PfATP4 leads against cipargamin. The answer is that the question, as the pipeline asks it, is mis-specified twice. First, the pipeline's target lookup silently substitutes a different protein — human maltase-glucoamylase for the parasite sodium pump — and the correction, not the ranking, is the methodological result: any future run on a target whose ChEMBL name does not match the UniProt protein name must check the target's organism and components before trusting a score. Second, the ranking the pipeline does produce is a best-record ranking: it takes the single highest pChEMBL per compound and discards the strain and mutant records that sit beside it in the same document. For PfATP4 that discards the only information that matters, because the clinical failure of cipargamin was a resistance failure (G358S, 65% of failures), not a potency failure. A lead that is 4.6 nM on 3D7 and 7,500 nM on the G358S mutant is not a lead; it is a 3D7 artefact. The R-enantiomer, four-fold weaker on the headline number, is the better lead on every background that resembles a patient.

### 4.2 Why the "win" must not be over-read

The S-enantiomer's 4.6 nM is a single-assay biochemical maximum on one strain, not a head-to-head win over cipargamin, whose literature IC50 is 0.5–1.4 nM. The two enantiomers' identical composite scores (64.7) are an artefact of the scoring: identical descriptors and identical similarity to cipargamin (0.173) produce identical scores for compounds whose strain profiles differ by two orders of magnitude. The N-acetamide indoles' 150 and 790 nM are IC50s from a different assay series than the dihydroquinazolinones' EC50s and cannot be ranked against them. And no docking exists to suggest a binding-mode advantage for any compound here — the structural claims in this paper come from the published cryo-EM structure, not from this run.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

Both N-acetamide indoles carry a PAINS alert. The indole-acetamide scaffold is a known frequent-hitter chemotype, so their 150 and 790 nM values must be confirmed with detergent controls, a counter-screen against an unrelated ATPase (for example a human P-type ATPase preparation), and a check for aggregation by dynamic light scattering before any potency claim is trusted. The dihydroquinazolinones are PAINS-clean, which makes the enantiomer result cleaner to interpret — but PAINS-clean is not the same as validated: the 890-fold 3D7-to-Dd2 gap for the S-enantiomer needs the same replication as any PAINS-flagged hit.

### 4.4 Testable hypotheses

1. In a head-to-head Na+-ATPase assay on the same plate, the S-enantiomer will be >100-fold weaker on Dd2 than on 3D7 membrane preparations, while the R-enantiomer will stay within 3-fold. Refuted if both enantiomers hold potency on Dd2.
2. On G358S mutant PfATP4, neither dihydroquinazolinone enantiomer will lose more than 5-fold potency versus its own Dd2 wild type, reproducing the ChEMBL record and showing no cross-resistance to the cipargamin resistance mutation. Refuted if either loses >10-fold.
3. The R-enantiomer will match or beat the S-enantiomer in whole-parasite growth inhibition on Dd2 and on a G358S parasite line, reversing the 3D7 ranking. Refuted if the S-enantiomer remains more potent on Dd2 parasites.
4. The two N-acetamide indoles will lose ≥50% of their apparent potency in the presence of detergent or on a counter-screen ATPase, consistent with a PAINS artefact. Refuted if potency is detergent-insensitive and counter-screen-clean.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): repeat the Na+-ATPase activity assay for both dihydroquinazolinone enantiomers, the two N-acetamide indoles and cipargamin, on 3D7 and Dd2 membrane preparations, 10-point dose–response in triplicate on the same plate, with detergent and counter-screen controls — the deliverable is a head-to-head table replacing the ChEMBL maxima, and the explicit test of hypothesis 1. Stage 2 (weeks 4–6): the same assay on G358S and, if available, other PfATP4 mutant preparations, plus whole-parasite SYBR Green growth inhibition on 3D7, Dd2 and a G358S line for the surviving lead — the deliverable is the fold-change in potency, which is the only number that matters for this target. Stage 3 (weeks 7–12): for the lead that survives stage 2, a dual gamete formation assay for transmission-blocking activity, and a structural rationalisation against the 9N10 cryo-EM model — mapping the resistance mutations onto the experimental structure, not docking on it — plus a P. berghei mouse-model check with the species-difference caveat from Awalt et al. in mind. Stop rule: a lead whose Dd2 potency is >100-fold worse than its 3D7 potency is a 3D7 artefact, not a publication — 3D7 potency is not the endpoint. A lead that fails the detergent or counter-screen controls is an artefact, not a lead.

## 5. Limitations

1. No docking was performed — this paper contains no binding-mode or docking-score claims at all, by design (see 2.3).
2. "Measured" potencies are single-assay ChEMBL maxima from biochemical Na+-ATPase activity assays; they are not whole-parasite growth inhibition values and not head-to-head values, and cipargamin's own figures are literature values because it has no ChEMBL record on this target.
3. The pipeline's composite score is similarity-dominated and identical for the two enantiomers; the ranking in Table 3.1 must not be read as a potency ranking, and the best-record rule hides the strain data that reverse it.
4. The 890-fold 3D7-to-Dd2 gap for the S-enantiomer is a single-study observation from one document; it may reflect assay conditions as well as pharmacology and needs replication.
5. Two further compounds at IC50 ~400 nM were excluded by the pipeline's pChEMBL filter because ChEMBL records their relation as "~" with no pChEMBL value; the evidence base is thinner than the table suggests.
6. The resistance discussion rests on one clinical mutation (G358S) and published cryo-EM and virology, not on any measurement in this run.
7. No data are presented on pharmacokinetics, combination partners, cost, or access — cipargamin's clinical future is as a combination, which this analysis does not address.
8. No local (Pakistan) epidemiological or access data beyond the national estimates in Section 1 were collected.

## 6. Conclusion

Against cipargamin, the ChEMBL PfATP4 top tier is thin and misleading at first glance: the best record is a dihydroquinazolinone S-enantiomer at EC50 4.6 nM on 3D7, against cipargamin's literature IC50 of 0.5–1.4 nM — but the same compound is 4,100 nM on Dd2 and 7,500 nM on the G358S mutant, while its R-enantiomer holds 18.2, 26.4 and 81.3 nM across the same three assays, and the two N-acetamide indoles score 150 and 790 nM with PAINS alerts. Docking was skipped because no X-ray structure of PfATP4 exists and the only experimental structure is a 3.7 Å cryo-EM apo complex with no bound inhibitor. The next step is a head-to-head Na+-ATPase assay of the two enantiomers plus cipargamin on 3D7, Dd2 and G358S preparations on the same plate: a lead only matters if it keeps potency where the S-enantiomer loses it.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all tools and data sources used are free and public (UniProtKB, ChEMBL, PubChem, RCSB PDB, EMDB).

## References

1. World Health Organization. World Malaria Report 2025. Geneva: World Health Organization; 2025. Estimated 282 million cases and 610,000 deaths in 2024; partial artemisinin resistance confirmed or suspected in at least eight African countries.
2. World Health Organization Regional Office for the Eastern Mediterranean / Ministry of National Health Services, Pakistan. WHO and Pakistan warn climate change is worsening malaria amid 2 million annual cases. 24 April 2025. https://www.emro.who.int/pak/pakistan-news/who-and-pakistan-warn-climate-change-is-worsening-malaria-amid-2-million-annual-cases.html
3. Rottmann M, McNamara C, Yeung BKS, et al. Spiroindolones, a potent compound class for the treatment of malaria. Science. 2010;329(5996):1175–1180. PMID 20813948. doi:10.1126/science.1193225
4. Spillman NJ, Allen RJW, McNamara CW, et al. Na+ regulation in the malaria parasite Plasmodium falciparum involves the cation ATPase PfATP4 and is a target of the spiroindolone antimalarials. Cell Host Microbe. 2013;13(2):227–237. PMID 23414762. doi:10.1016/j.chom.2012.12.006
5. Schmitt EK, Ndayisaba G, Yeka A, et al. Efficacy of cipargamin (KAE609) in a randomized, phase II dose-escalation study in adults in sub-Saharan Africa with uncomplicated Plasmodium falciparum malaria. Clin Infect Dis. 2022;74(10):1831. doi:10.1093/cid/ciab716
6. Ndayisaba G, Yeka A, Asante KP, et al. Hepatic safety and tolerability of cipargamin (KAE609), in adult patients with Plasmodium falciparum malaria: a randomized, phase II, controlled, dose-escalation trial in sub-Saharan Africa. Malar J. 2021;20:478. doi:10.1186/s12936-021-04009-1
7. Yipsirimetee et al. Assessment in vitro of the antimalarial and transmission-blocking activities of cipargamin and ganaplacide in artemisinin-resistant Plasmodium falciparum. Antimicrob Agents Chemother. 2022;66(3):e01481-21. doi:10.1128/aac.01481-21
8. Haile MT, Shukla A, Zhen J, et al. Endogenous structure of antimalarial target PfATP4 reveals an apicomplexan-specific P-type ATPase modulator. Nat Commun. 2025;16:9092. PMID 41115914. doi:10.1038/s41467-025-64815-y
9. Ashton TD, Calic PPS, Dans MG, et al. Property and activity refinement of dihydroquinazolinone-3-carboxamides as orally efficacious antimalarials that target PfATP4. J Med Chem. 2024;67(16):14493–14523. PMID 39134060. doi:10.1021/acs.jmedchem.4c01241
10. Awalt JK, Ooi ZK, Ashton TD, et al. Optimization and characterization of N-acetamide indoles as antimalarials that target PfATP4. J Med Chem. 2025;68(8):8933–8966. PMID 40228810. doi:10.1021/acs.jmedchem.5c00614
11. Spillman NJ. The malaria parasite cation ATPase PfATP4 and its role in the mechanism of action of a new arsenal of antimalarial drugs. Int J Parasitol Drugs Drug Resist. 2015;5(3):149–162. doi:10.1016/j.ijpddr.2015.07.001
12. Protein Data Bank. P. falciparum P-type ATPase, PfATP4 (cryo-EM, 3.7 Å). PDB ID 9N10. https://www.rcsb.org/structure/9N10

## Data availability

All potency values reported here are in `hidden_files/dock-HP-022-2026-11-11.json` (corrected pipeline run on CHEMBL6066156; docking skipped with reason recorded). The discarded first run's step-2 zero (wrong target CHEMBL2074, human maltase-glucoamylase) was overwritten by the corrected run in the same file; the correction is documented in the file's `corrections` field and in Section 2.2. Target: UniProt A0A143ZZK9; ChEMBL target CHEMBL6066156; compounds: cipargamin (PubChem CID 44469321), CHEMBL5591927, CHEMBL5594154, CHEMBL6174048, CHEMBL6175630; structure: PDB 9N10 / EMDB 48800, 48801. No additional data were generated.
