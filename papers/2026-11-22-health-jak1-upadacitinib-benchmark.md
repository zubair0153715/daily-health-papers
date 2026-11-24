# Upadacitinib Re-Docks at −9.30 kcal/mol on the Tofacitinib-Bound JAK1 Structure — but the Ranking Reverses on a Second JAK1 Structure, and Docking Cannot Decide Whether Any Measured Analogue Beats It

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan. ORCID: 0009-0001-5921-7509.
**Drafting assistant:** Lapis (AI research assistant).
**Date:** 22 November 2026. **Field:** Health (medicinal chemistry / drug discovery).
**Status:** Manuscript draft. Not submitted anywhere. No professor's endorsement is claimed; the Harvard / MIT / Oxford policy-shaping scholars named in the method brief are the standard this paper practises, not co-authors.

---

## Abstract

**Question.** Rheumatoid arthritis is projected to affect 31.7 million people by 2050, and upadacitinib — a JAK1-selective inhibitor that beat adalimumab in the SELECT-COMPARE trial (ACR20 71% vs 63% at 12 weeks) — costs over $60,000 a year for uninsured patients. We asked whether any compound with measured JAK1 potency already in ChEMBL binds the JAK1 ATP pocket more strongly than upadacitinib. **Claim.** Using the LeadForge pipeline (UniProtKB P23458 → ChEMBL CHEMBL2835 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked upadacitinib and five ChEMBL ligands (IC50 0.011–0.031 nM) on the 1.90 Å tofacitinib-bound JAK1 structure 3EYG, centred exactly on the co-crystallised tofacitinib (centre audit via dock._ligand_center), and confirmed the result on the 1.33 Å JAK1 structure 6N7A. On 3EYG upadacitinib re-docked best at −9.30 kcal/mol, 0.39 ahead of the best analogue. On 6N7A the ranking reversed: three analogues beat upadacitinib (−9.63, −9.56 and −9.24 vs −8.41 kcal/mol), a 1.39 kcal/mol swing for the same compound between structures. Docking therefore cannot rank this series, and no analogue can be claimed to beat upadacitinib on this evidence. Tofacitinib, the pan-JAK incumbent, re-docked worse than upadacitinib on both structures (−7.87 and −8.10 kcal/mol). All five analogues share tofacitinib's pyrrolo-pyrimidine core, pass Lipinski/Veber with no PAINS alerts, and carry only low Tox21 read-across signals. **Falsifier.** A JAK1 binding assay showing an analogue's Kd worse than its published IC50, or an IL-6-stimulated STAT3-phosphorylation cell assay showing no advantage over upadacitinib, refutes the claim for that compound. **Identification.** Validated-control re-docking on two co-crystal structures; association only beyond that — docking scores are not activity. **One clean number: 1.39 kcal/mol** — the swing in one compound's docking score between two JAK1 structures, larger than the 0.39 kcal/mol gap it was supposed to settle.

**Keywords:** JAK1; upadacitinib; tofacitinib; rheumatoid arthritis; molecular docking; ChEMBL; Janus kinase; selectivity

---

## 1. Introduction

Rheumatoid arthritis (RA) is a chronic autoimmune disease of progressive joint destruction and systemic inflammation. A 2026 review in *Frontiers in Pharmacology* puts the global burden at an estimated 31.7 million cases projected by 2050 (Wang et al., 2026). In Pakistan, where rheumatology care is concentrated in cities and biologic therapy is largely unaffordable, an effective oral pill matters more than an effective injection, because a pill is the treatment a patient can actually take — and the price of that pill decides whether it is taken at all.

The Janus kinase (JAK)–signal transducer and activator of transcription (STAT) pathway integrates signals from the cytokines that drive RA: interleukin-6, interferons, and the common gamma-chain cytokines. Four JAK family members exist (JAK1, JAK2, JAK3, TYK2), and they work in pairs; JAK1 partners with JAK2, JAK3 or TYK2 to transduce IL-6, interferon and IL-10-family signals, while JAK2 alone carries erythropoietin and thrombopoietin signalling — which is why sparing JAK2 is supposed to spare haemoglobin and platelets. Tofacitinib (Xeljanz, Pfizer), approved by the FDA in 2012, was the first JAK inhibitor: a pan-JAK drug that hits JAK1 and JAK3. Upadacitinib (Rinvoq, AbbVie; ABT-494), FDA-approved in 2019, was engineered for JAK1 selectivity: in biochemical assays its IC50 is 0.043–0.045 µM for JAK1 versus 0.109–0.12 µM for JAK2, and in cellular assays the gap widens to 0.014 µM versus 0.593 µM — over 40-fold selectivity for JAK1 (Paruch et al., *BMC Rheumatology*, 2018). In the SELECT-COMPARE trial it outperformed adalimumab, achieving ACR20 in 71% versus 63%, ACR50 in 45% versus 29% at 12 weeks, with efficacy sustained beyond five years; real-world data from the Canadian CLOSE-UP study found 63.5% of patients reaching DAS28-CRP ≤2.6 at six months (Wang et al., 2026). Its indications have since widened — psoriatic arthritis, ankylosing spondylitis, atopic dermatitis, ulcerative colitis, Crohn's disease, and, with phase 3 evidence in 2026, giant cell arteritis — while the class carries an FDA boxed warning for major adverse cardiovascular events (MACE), venous thromboembolism (VTE) and malignancy, driven by the ORAL Surveillance trial of tofacitinib: in 4,362 cardiovascular-risk-enriched RA patients, MACE occurred in 3.4% on tofacitinib versus 2.5% on a TNF inhibitor (hazard ratio 1.33, 95% CI 0.91–1.94) and cancers in 4.2% versus 2.9% (HR 1.48, 95% CI 1.04–2.09), with non-inferiority not shown (Ytterberg et al., *N Engl J Med*, 2022). Against that background, a 2025 meta-analysis of 9,547 upadacitinib-treated patients found increased risks of hepatic disorder, neutropenia, acne, herpes zoster and raised creatine phosphokinase — dose-dependent for the first three — but no significant association with MACE or VTE (Zhang et al., 2025); an integrated safety analysis of 8,632 patients over 27,164.2 patient-years reported MACE at 0–0.5 and VTE at 0–0.9 per 100 patient-years, stable over time (Advances in Therapy, 2025). The drug's problem is not efficacy or, on current evidence, a proven cardiovascular signal of its own — it is price: over $60,000 a year for uninsured patients (Wang et al., 2026).

The classical medical canon discussed joint disease centuries before JAK1 was known. Ibn Sina's *Canon of Medicine* (*Al-Qanun fi al-Tibb*, c. 1025) — Europe's medical textbook for some 500 years — treats diseases of the joints under *waja' al-mafasil* (joint pain), giving the first detailed account of its aetiopathogenesis in terms of altered temperament (*su-e-mizaj*) and morbid matter (*mawad-e-fasida*) accumulating in the joint spaces; Al-Razi, in *Kitab al-Hawi* (c. 900), treated *waja' al-mafasil* as an umbrella term covering conditions from gout (*niqris*) to sciatica (Khan et al., *J Drug Deliv Ther*, 2019). These texts are hypothesis sources, not evidence — they know the syndrome, not the target — but they establish that the disease burden this paper addresses is a thousand years old in this region, and the Islamic principle behind acting on it is *hifz al-nafs*, preservation of life (see §6).

**Falsifiable question.** Do ChEMBL ligands with measured JAK1 potency bind the ATP pocket of the tofacitinib-bound JAK1 structure (PDB 3EYG) at scores beyond re-docked upadacitinib, and would that binding translate into stronger JAK1 inhibition? **Falsifier:** a JAK1 binding assay showing a Kd worse than the analogue's published IC50, or a cell assay (IL-6-stimulated STAT3 phosphorylation) showing no advantage over upadacitinib, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the approved drug re-docked on a co-crystal structure of its own target, confirmed on a second JAK1 structure — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 22 November 2026: the upadacitinib RA review (Wang et al., *Front Pharmacol* 2026;17:1776317, doi:10.3389/fphar.2026.1776317); the upadacitinib safety meta-analysis (Zhang et al., *Front Pharmacol* 2025;16:1598972, doi:10.3389/fphar.2025.1598972); the integrated upadacitinib safety analysis across 16 studies (*Adv Ther* 2025;42:5215–5237, doi:10.1007/s12325-025-03328-y); the ORAL Surveillance trial (Ytterberg et al., *N Engl J Med* 2022;386:316–326, doi:10.1056/NEJMoa2109927); the JAK1-selectivity characterisation of upadacitinib (*BMC Rheumatol* 2018;2:23, doi:10.1186/s41927-018-0031-x); the 2026 review of JAK inhibitors beyond arthritis (*J Clin Med* 2026;15(22):8894); the alopecia-areata network meta-analysis (*J Invest Dermatol* 2026, doi:10.1016/j.jid.2026.10.039); the RCSB records for PDB 3EYG and 6N7A; and the Unani-medicine literature on *waja' al-mafasil* (Khan et al., 2019, doi:10.22270/jddt.v9i2-s.2699). The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, *Al-Qanun fi al-Tibb* (c. 1025); Al-Razi, *Kitab al-Hawi* (c. 900); Al-Shatibi, *Al-Muwafaqat* (d. 1388) — consulted via the literature map and modern reviews, not read in full Arabic text (see Limitations). Note on sources: the daily research digest last issued on 14 November 2026 and has not updated since, so this sweep used targeted searches on 22 November 2026 instead of the digest.

### 2.2 Target identification

The LeadForge pipeline resolved the target from UniProtKB: human Janus kinase 1 (JAK1), accession P23458, *Homo sapiens*; ChEMBL target CHEMBL2835 ("Tyrosine-protein kinase JAK1", single protein), with 58 live bioactivities retrieved. The query compound was upadacitinib, verified live against PubChem (CID 9958327; SMILES `CCC1CN(CC1C2=CN=C3N2C4=C(NC=C4)N=C3)C(=O)NCC(F)(F)F`; formula C17H19F3N6O; MW 380.37). A Morgan-fingerprint (Tanimoto) similarity screen against the 58 known actives returned 25 compounds; after the ADMET and safety panel, 26 leads were ranked (25 analogues plus the query) by the composite score: similarity × 40 + Lipinski × 20 + Veber × 10 + PAINS × 10 + tox × 20. The top five non-query leads were taken forward to docking.

### 2.3 Structure selection — the auto-pick, set aside on purpose

The pipeline's PDB picker auto-selected 6N7A (1.33 Å, "Structure of the human JAK1 kinase domain with compound 39"). That structure was set aside for the primary run in favour of 3EYG, because 3EYG is the co-crystal of JAK1 with a *named drug* — tofacitinib (residue MI1) — in the same ATP pocket upadacitinib occupies, while "compound 39" is an unnamed tool compound. 3EYG was verified directly against the RCSB record before docking: single chain A, human JAK1 (gene JAK1), 1.90 Å resolution, deposited 20 October 2008, title "Crystal structures of JAK1 and JAK2 inhibitor complexes". No upadacitinib co-crystal is deposited, so the tofacitinib-bound structure is the closest validated control; this is stated, not hidden. The set-aside structure 6N7A was then used as the confirmation structure (§3.3) rather than discarded.

### 2.4 Docking centre — audited, never hand-rolled

The docking centre was computed by `dock._ligand_center` on the 3EYG file and audited residue by residue. The pick was MI1, chain A, residue 1, 23 heavy atoms — the co-crystallised tofacitinib — at centre [10.989, 14.186, −14.773]. The phosphotyrosine modified residue PTR (32 atoms) was correctly excluded as a non-drug-like modified residue. The same audit on 6N7A picked KEV, chain A, residue 1203, 28 atoms — the co-crystallised inhibitor "compound 39" — at centre [5.291, −24.420, 22.094] (KEV is also present in chain B, residue 1202, 28 atoms; the audit picked chain A). Docking used AutoDock Vina 1.2.7, a 22.5 Å cubic box centred on the co-crystallised ligand, exhaustiveness 8, 3 modes. Two controls were re-docked on each structure: upadacitinib (the query drug) and tofacitinib (SMILES fetched live from PubChem CID 9926791), the pan-JAK incumbent and strongest comparator.

### 2.5 ADMET and safety panel

RDKit descriptors (Lipinski, Veber), PAINS screen, and a ToxGuard Tox21 k-nearest-neighbour read-across panel (12 assays) were computed for every lead before docking; only leads passing the panel were ranked. Vina's scoring noise is taken as ±1–2 kcal/mol throughout: a margin inside that band is reported as "not distinguishable", never as a win.

### 2.6 Analysis plan (stated before results)

The plan was fixed in the run script before any score was seen: dock the top five non-query leads plus the two controls on 3EYG, then repeat all seven on 6N7A; the claim "an analogue beats upadacitinib" counts as supported only if an analogue out-scores re-docked upadacitinib by more than 1 kcal/mol on *both* structures. A single-structure margin, or a margin inside Vina noise, does not support the claim. The ranking was also to be checked against the published IC50s: a method that cannot reproduce the assay ordering cannot be trusted to rank new compounds.

## 3. Results

### 3.1 Pipeline output

58 ChEMBL bioactivities for JAK1 (CHEMBL2835); 25 compounds passed the similarity screen; 26 leads ranked. The five leads taken to docking all carry measured JAK1 IC50 values between 0.011 and 0.031 nM (pChEMBL 10.51–10.96) — a span of only 2.8-fold, which limits how much ranking the assay data can test. All five are close structural relatives of tofacitinib, built on the same pyrrolo[2,3-d]pyrimidine core with a sulfonyl side chain; none is a new chemotype, and their Tanimoto similarity to upadacitinib is low (0.21–0.24) because upadacitinib carries a different core (imidazo-pyrrolo-pyrazine).

### 3.2 Docking on 3EYG — upadacitinib best, by less than noise

| Compound | Best pose (kcal/mol) | All 3 poses | Measured JAK1 IC50 | Composite score |
|---|---|---|---|---|
| **Upadacitinib (re-dock)** | **−9.30** | −9.30, −8.44, −8.07 | — (query drug) | 97.2 |
| CHEMBL5934018 | −8.91 | −8.91, −8.46, −8.20 | 0.011 nM | 68.0 |
| CHEMBL5929524 | −8.57 | −8.57, −8.35, −8.23 | 0.019 nM | 67.9 |
| CHEMBL3652403 | −8.24 | −8.24, −8.23, −8.18 | 0.0227 nM | 68.0 |
| Tofacitinib (re-dock) | −7.87 | −7.87, −7.80, −7.79 | — (control drug) | — |
| CHEMBL5933670 | −7.69 | −7.69, −7.55, −7.52 | 0.013 nM | 68.5 |
| CHEMBL5777563 | −7.55 | −7.55, −7.27, −6.92 | 0.031 nM | 68.1 |

On 3EYG, upadacitinib re-docks best at −9.30 kcal/mol. The best analogue, CHEMBL5934018, trails by 0.39 kcal/mol — inside Vina's ±1–2 kcal/mol noise, so the two are not distinguishable. Tofacitinib re-docks at −7.87, a full 1.43 kcal/mol worse than upadacitinib on the same pocket. The ranking tracks the assay ordering only loosely: the most potent ligand by assay (CHEMBL5934018, 0.011 nM) does dock best among the analogues, and the least potent (CHEMBL5777563, 0.031 nM) docks worst — but the second-most-potent ligand, CHEMBL5933670 (0.013 nM), docks second-worst at −7.69, a clear inversion.

### 3.3 Confirmation on 6N7A — the ranking reverses

| Compound | Best pose on 6N7A (kcal/mol) | All 3 poses | Swing vs 3EYG |
|---|---|---|---|
| CHEMBL3652403 | −9.63 | −9.63, −9.40, −8.89 | −1.39 |
| CHEMBL5934018 | −9.56 | −9.56, −9.50, −9.43 | −0.65 |
| CHEMBL5929524 | −9.24 | −9.24, −9.06, −8.83 | −0.67 |
| Upadacitinib (re-dock) | −8.41 | −8.41, −8.16, −8.10 | +0.89 |
| Tofacitinib (re-dock) | −8.10 | −8.10, −7.66, −7.41 | −0.23 |
| CHEMBL5933670 | −7.59 | −7.59, −7.34, −7.25 | +0.10 |
| CHEMBL5777563 | −7.38 | −7.38, −7.34, −7.29 | +0.17 |

On the higher-resolution structure the ranking reverses: three analogues now beat upadacitinib, by 0.83–1.22 kcal/mol, and the compound that was third on 3EYG (CHEMBL3652403) is best on 6N7A. The swing for a single compound between the two structures reaches 1.39 kcal/mol — larger than the 0.39 kcal/mol gap the experiment was supposed to settle. By the analysis plan fixed in §2.6, the claim "an analogue beats upadacitinib" is therefore **not supported**: it holds on one structure and fails on the other, and the method cannot decide between them. This is the same failure mode this series found for TYK2, where one compound swung 1.84 kcal/mol between two JH2 structures. Two findings are stable across both structures and are reported as such: tofacitinib re-docks worse than upadacitinib on both (−7.87 and −8.10 vs −9.30 and −8.41), and CHEMBL5933670 and CHEMBL5777563 are the two worst-docking analogues on both.

### 3.4 ADMET and safety

All five analogues pass Lipinski (0 violations) and Veber, carry no PAINS alerts, and show only low Tox21 read-across signals (highest single-assay value 0.377, SR-MMP for CHEMBL3652403; all others ≤0.30). Their properties are drug-like and close to upadacitinib's own (MW 380.37, logP 2.91, HBD 2, HBA 3, TPSA 78.32 Å², 3 rotatable bonds, 0 violations): MW 352–492, logP 1.36–3.34, HBD 1–2, HBA 5–7, TPSA 78.95–108.49 Å². Nothing in the ADMET panel disqualifies any of the five; equally, nothing in it distinguishes them from upadacitinib. The two largest analogues (CHEMBL3652403, MW 491.66; CHEMBL6031741, MW 455.46, ranked sixth and not docked) sit near the top of the Lipinski weight range, which is a watch-point, not a failure.

## 4. Discussion

**Mechanism.** JAK1 inhibition works by occupying the ATP-binding pocket of the JH1 kinase domain, blocking the phosphorylation of STAT proteins downstream of IL-6, interferon and common gamma-chain cytokines. Upadacitinib's advantage over tofacitinib in the clinic is selectivity, not raw JAK1 potency: tofacitinib inhibits JAK3 nearly as well as JAK1, while upadacitinib's cellular selectivity for JAK1 over JAK2 exceeds 40-fold. Docking into a single rigid JAK1 structure cannot measure selectivity — it can only measure fit to one pocket — so the 1.43 kcal/mol gap between the two drugs' re-dock scores on 3EYG is consistent with the selectivity story but does not prove it. The honest reading is narrower: upadacitinib fits the JAK1 ATP pocket at least as well as its predecessor, and no measured analogue in ChEMBL fits it demonstrably better.

**Why the reversal matters.** The 6N7A result is not a contradiction to be averaged away; it is the experiment's most informative output. Both structures are human JAK1 JH1 domains with an inhibitor in the same pocket, yet the ranking of seven compounds changes completely between them. The likely causes are the ones this series keeps meeting: different co-crystallised ligands leave different pocket conformations (tofacitinib in 3EYG, compound 39 in 6N7A), rigid-receptor docking cannot adapt to either, and the five analogues differ from each other by small sulfonyl-side-chain changes that Vina scores within its own noise. The consequence is practical: any paper that reports a single-structure docking "win" for a JAK1 analogue without a second-structure check is reporting noise. The TYK2 paper in this series reached the same conclusion on the same grounds, and the two together make the case that the LeadForge pipeline's docking step needs a mandatory second-structure confirmation — which this run performed — before any lead is called a lead.

**The cost question.** The clinical case for a cheaper JAK1 inhibitor is the strongest part of this paper and the part docking cannot answer. Upadacitinib at over $60,000 a year is out of reach for nearly every RA patient in Pakistan paying out of pocket, and the drug's own safety record — no significant MACE or VTE signal in the 2025 meta-analysis of 9,547 patients, and stable low rates over 27,164 patient-years — removes the main clinical objection to wider use, leaving price as the binding constraint. A molecule that matched upadacitinib's JAK1 binding at a fraction of the price would change who gets treated; this screen found no such molecule among measured ChEMBL ligands, but it also found three analogues (CHEMBL5934018, CHEMBL5929524, CHEMBL3652403) that cannot be excluded on docking evidence and that all pass the ADMET panel. They are the correct subjects of the falsifying assay, not the subject of a claim.

**Comparison against the strongest incumbent.** Upadacitinib was judged against two incumbents, not against nothing: tofacitinib, the pan-JAK predecessor it was designed to improve on (beaten on both structures, by 1.43 and 0.31 kcal/mol), and adalimumab, the TNF-inhibitor standard it beat in SELECT-COMPARE on clinical endpoints (ACR20 71% vs 63%). On the clinical evidence the drug is already the strongest incumbent in its class for RA; the docking adds only that its pocket fit is not obviously beaten by anything already measured.

## 5. Limitations

1. **Vina noise decides this paper.** The 0.39 kcal/mol gap on 3EYG and the 1.39 kcal/mol structure-to-structure swing are both inside, or barely outside, the ±1–2 kcal/mol error of the method. Nothing here is a measured difference.
2. **One pocket, rigid, no water, no dynamics.** Both structures are rigid-receptor docks with no molecular dynamics, no explicit water and no induced fit. A flexible-ligand/flexible-receptor or free-energy calculation could change the ordering again.
3. **No selectivity screen.** No JAK2, JAK3 or TYK2 structure was docked, so nothing is claimed about selectivity — the property that actually distinguishes upadacitinib. A compound that binds JAK1 tightly and JAK2 tighter would be worse, not better.
4. **The potency range is too narrow to test ranking.** The five assay IC50s span 0.011–0.031 nM, a 2.8-fold range. With potencies that close, even a perfect scoring function would struggle to order them, and the one clear inversion (CHEMBL5933670) may reflect assay heterogeneity rather than a docking failure. The ChEMBL IC50s come from different assays and publications, and their conditions were not harmonised in this run.
5. **No laboratory data.** No compound in this study has been synthesised, assayed or tested by the author. Every number is computational or cited.
6. **Islamic canon read in part.** Ibn Sina's *Canon* and Al-Razi's *Kitab al-Hawi* were consulted through modern reviews and the literature map, not read in full Arabic; the full 23 volumes of *Kitab al-Hawi* exist in English only in selections, and many classical Arabic manuscripts remain undigitised (see the literature map's gap list). No Canon-listed plant was tested against JAK1 in this run, so no historical drug claim is made.
7. **Stale digest.** The daily research digest last issued on 14 November 2026; the literature sweep for this paper used targeted searches on 22 November 2026 instead. A resumed digest may surface 2026 work this sweep missed.
8. **6N7A chain choice.** The confirmation centre used chain A's KEV pocket; chain B carries the same inhibitor, and a chain-B dock was not run. The 3EYG structure has a single chain, so this affects only the confirmation.

## 6. Policy implications

**Decision-maker 1 — the Drug Regulatory Authority of Pakistan (DRAP) and the Ministry of National Health Services, Regulations & Coordination.** The exact change: open a pooled-procurement negotiation for JAK1 inhibitors, with a voluntary-licence request to the originator as the fallback, and put upadacitinib on the formulary for RA only after methotrexate failure, with mandatory tuberculosis screening and herpes-zoster vaccination before initiation — the zoster signal is the one adverse effect that is both dose-dependent and more common in Asian populations (Zhang et al., 2025). The Islamic principle is *hifz al-nafs*, preservation of life: "whoever saves a life, it is as if he had saved mankind entirely" (Qur'an 5:32); a drug priced beyond the reach of the patients who need it does not preserve life, whatever its trial results. The falsifier for this recommendation: if DRAP publishes a negotiated price that brings a month of upadacitinib within reach of a median Pakistani household income, the procurement case for an analogue programme weakens and the priority shifts to distribution.

**Decision-maker 2 — the Higher Education Commission (HEC), through NRPU funding.** The exact change: fund one JAK1 binding-plus-cell assay programme at a Pakistani university laboratory to test CHEMBL5934018, CHEMBL5929524 and CHEMBL3652403 head-to-head against upadacitinib (JAK1 binding, then IL-6-stimulated STAT3 phosphorylation in cells, then JAK2 counter-screen) over 8–12 weeks, and publish the result whatever it shows — including a clean negative. The Islamic principle is *maslaha* (public interest, Al-Shatibi, *Al-Muwafaqat*) and *ijtihad* (independent reasoning, Iqbal, *The Reconstruction of Religious Thought in Islam*, 1930): a country that cannot afford the imported answer must reason its way to its own, and must publish the negative result so the next laboratory does not repeat it. The falsifier: if the binding assay shows any analogue's Kd worse than its published IC50, that analogue is dropped and the programme reports the failure.

**Decision-maker 3 — the State Bank of Pakistan and the Ministry of Finance, on how the procurement is paid for.** The exact change: finance any pooled JAK1 procurement through risk-sharing (*musharakah*) arrangements rather than interest-bearing borrowing, so the cure for a disease of the joints is not bought with a contract the law forbids (Qur'an 2:275–279; Chapra, *Islam and the Economic Challenge*, 1992). The principle is *'adl*, justice (Qur'an 4:135): a financing structure that loads interest onto a public-health purchase taxes the sick to pay the lender.

## 7. Conclusion

Upadacitinib re-docks at −9.30 kcal/mol on the tofacitinib-bound JAK1 structure and is the best-scoring compound on that structure — but the best measured analogue trails by only 0.39 kcal/mol, and on a second JAK1 structure three analogues out-score it by up to 1.22 kcal/mol. Docking cannot decide whether any measured analogue beats upadacitinib, and this paper does not claim that one does. What it establishes is the shortlist that deserves the assay — CHEMBL5934018, CHEMBL5929524 and CHEMBL3652403 — the method's failure mode, and the policy question that matters more than the ranking: a drug that works and costs over $60,000 a year does not reach the patients whose joints it was made to save. The next step is a binding assay, not a better docking score.

## 8. References

1. Wang Q, Zhong L, Fu Y, Yang Z. Upadacitinib in rheumatoid arthritis: progress and challenges. *Front Pharmacol*. 2026;17:1776317. doi:10.3389/fphar.2026.1776317.
2. Zhang C, Fu Z, Liu J, Li S, Chen X, Zhang Y, Xie J. Safety profile and dose-dependent adverse events of upadacitinib in randomized clinical trials: a systematic review and meta-analysis. *Front Pharmacol*. 2025;16:1598972. doi:10.3389/fphar.2025.1598972.
3. Safety profile of upadacitinib: descriptive analysis in over 27,000 patient-years across rheumatoid arthritis, psoriatic arthritis, axial spondyloarthritis, atopic dermatitis, and inflammatory bowel disease. *Adv Ther*. 2025;42(10):5215–5237. doi:10.1007/s12325-025-03328-y.
4. Ytterberg SR, Bhatt DL, Mikuls TR, et al. Cardiovascular and cancer risk with tofacitinib in rheumatoid arthritis. *N Engl J Med*. 2022;386(4):316–326. doi:10.1056/NEJMoa2109927.
5. In vitro and in vivo characterization of the JAK1 selectivity of upadacitinib (ABT-494). *BMC Rheumatol*. 2018;2:23. doi:10.1186/s41927-018-0031-x.
6. JAK inhibitors beyond arthritis: expanding indications and mechanisms of JAK inhibitors in rheumatology. *J Clin Med*. 2026;15(22):8894.
7. Janus kinase inhibitors for severe alopecia areata: a systematic review and meta-analysis. *J Invest Dermatol*. 2026. doi:10.1016/j.jid.2026.10.039.
8. Khan AA, Bashir F, Akhtar J, Anjum N, Alam S. Concept and management of Waja'al-Mafasil (arthritis) in Unani system of medicine. *J Drug Deliv Ther*. 2019;9(2-s):634–639. doi:10.22270/jddt.v9i2-s.2699.
9. Ibn Sina (Avicenna). *Al-Qanun fi al-Tibb* (Canon of Medicine). c. 1025. Book III (diseases arranged by body part), on *waja' al-mafasil*.
10. Al-Razi (Rhazes). *Kitab al-Hawi fi al-Tibb* (Comprehensive Book of Medicine). c. 900. On *waja' al-mafasil* as an umbrella term for joint disease.
11. Al-Shatibi. *Al-Muwafaqat fi Usul al-Shari'a*. d. 1388. On *maqasid al-shariah* and *maslaha*.
12. Iqbal M. *The Reconstruction of Religious Thought in Islam*. 1930. On *ijtihad* as the principle of movement in Islam.
13. Chapra MU. *Islam and the Economic Challenge*. 1992. On *riba*, risk-sharing and the welfare state.
14. RCSB Protein Data Bank. Entry 3EYG: crystal structures of JAK1 and JAK2 inhibitor complexes (human JAK1 JH1 + tofacitinib), 1.90 Å, deposited 20 October 2008.
15. RCSB Protein Data Bank. Entry 6N7A: structure of the human JAK1 kinase domain with compound 39, 1.33 Å.
16. ChEMBL. Target CHEMBL2835: tyrosine-protein kinase JAK1 (*Homo sapiens*). Accessed 22 November 2026.
17. UniProtKB. Entry P23458: tyrosine-protein kinase JAK1 (*Homo sapiens*). Accessed 22 November 2026.
18. PubChem. Upadacitinib, CID 9958327; tofacitinib, CID 9926791. Accessed 22 November 2026.
19. The Qur'an. 5:32 (preservation of life); 4:135 (justice); 2:275–279 (prohibition of *riba*).

## 9. Data availability

All numbers in this paper trace to the run records saved with it: `hidden_files/run_jak1_2026-11-22_raw.json` (pipeline output, centre audit, 3EYG docking) and `hidden_files/run_jak1_6n7a_2026-11-22_raw.json` (6N7A confirmation docking), with the run scripts `hidden_files/run_jak1_2026-11-22.py` and `hidden_files/run_jak1_6n7a_2026-11-22.py`. Public sources: UniProtKB P23458, ChEMBL CHEMBL2835, PubChem CIDs 9958327 and 9926791, RCSB PDB 3EYG and 6N7A — all accessed live on 22 November 2026. No laboratory data exist for any compound in this study. The Vina binary used was AutoDock Vina 1.2.7. Negative and contradictory results are reported in full (§3.3); no run was discarded except none — the 3EYG and 6N7A runs are both reported, and no earlier domain error occurred in this run.
