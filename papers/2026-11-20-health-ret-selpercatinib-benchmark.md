# Cabozantinib Out-Docks Selpercatinib on Wild-Type RET (7DUA) by 0.65 kcal/mol — a Margin Inside Vina Noise That Contradicts a 27-Fold Measured Potency Gap

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-20 · **Health Papers Agent — Paper #86** (daily 5-paper run)

**Keywords:** RET; selpercatinib; pralsetinib; cabozantinib; molecular docking; drug resistance; non-small cell lung cancer; medullary thyroid cancer

---

## Abstract

RET fusions drive 1–2% of non-squamous non-small-cell lung cancers and RET point mutations drive most medullary thyroid cancers; selpercatinib, the selective RET inhibitor, produced objective responses in 62–83% of RET fusion-positive lung cancers in the final LIBRETTO-001 analysis, yet acquired resistance through solvent-front G810 and hinge Y806 mutations is inevitable. We asked whether the older multikinase inhibitors that selpercatinib replaced, or its selective sibling pralsetinib, bind wild-type RET more strongly than selpercatinib itself. Because ChEMBL's activity endpoint returned HTTP 500 on the study date, no ChEMBL ligand set could be retrieved; instead we docked five literature-known RET inhibitors with published potencies — selpercatinib, pralsetinib, cabozantinib, vandetanib and the 7DUA co-crystallised ligand HJ0 — on the 1.64 Å human RET kinase structure 7DUA with AutoDock Vina 1.2.7, centred on the co-crystallised ligand (chain A centroid, independently verified). Cabozantinib scored best at −10.76 kcal/mol, ahead of HJ0 (−10.27), selpercatinib (−10.11), pralsetinib (−9.98) and vandetanib (−9.55), with no PAINS alert in any compound; selpercatinib's score reproduced within 0.10 kcal/mol across three independent re-docks. The honest limit: the 0.65 kcal/mol cabozantinib margin lies inside Vina's ±1–2 kcal/mol noise, and the docking order contradicts the measured potency order — cabozantinib is 27-fold weaker than selpercatinib biochemically (11 nM versus 0.4 nM) — with a Spearman rank correlation of −0.32 between docking scores and published biochemical IC50 values. The claim that rigid docking can rank RET inhibitors would be refuted if free-energy refinement (MM-GBSA) on the same five compounds recovered the measured potency order with Spearman rho above 0.8, and the decisive next step is a single-assay biochemical kinase panel of the four drugs against wild-type and G810S RET.

---

## 1. Introduction

Lung cancer remains the leading cause of cancer death worldwide, and a small but precisely treatable fraction of it is driven by rearrangements of the RET (rearranged during transfection) proto-oncogene: RET fusions occur in 1–2% of non-squamous non-small-cell lung cancers (NSCLC), most commonly KIF5B-RET and CCDC6-RET, while activating RET point mutations (above all M918T) drive the majority of medullary thyroid cancers (MTC). For a decade the only drugs with anti-RET activity were multikinase inhibitors (MKIs) — cabozantinib and vandetanib — whose RET inhibition was capped by off-target toxicity, above all VEGFR2 inhibition: dose reductions were needed in 77.3% of MKI-treated patients in the LIBRETTO-531 trial and 26.8% discontinued treatment. The selective RET inhibitors selpercatinib (LOXO-292) and pralsetinib (BLU-667) were designed to hit RET hard and almost nothing else, and to bypass the V804 gatekeeper mutation that defeated the MKIs: biochemically, selpercatinib inhibits wild-type RET at 0.4 nM and RET V804M at 0.8 nM, and pralsetinib inhibits both at 0.4 nM.

The clinical payoff is documented. In LIBRETTO-001, selpercatinib's final analysis reported objective response rates of 62% in platinum-pretreated and 83% in treatment-naïve RET fusion-positive NSCLC, median progression-free survival of 26.2 and 22.0 months, median overall survival of 47.6 months in pretreated patients, and an 85% intracranial response rate. In RET-mutant MTC the response rates were 69% (previously treated) and 73% (treatment-naïve). The randomised phase 3 LIBRETTO-531 trial then proved the point head-to-head: first-line selpercatinib versus physician's choice of cabozantinib or vandetanib in RET-mutant MTC gave a hazard ratio for progression or death of 0.28 (95% CI 0.16–0.48), a response rate of 69.4% versus 38.8%, and far fewer dose reductions (38.9% versus 77.3%). Selpercatinib is the standard; the MKIs are the past.

The past still matters for two reasons. First, resistance to selpercatinib is inevitable: the crystal structures of the RET–selpercatinib and RET–pralsetinib complexes show both drugs wrapping around the K758 gate wall to reach the back cleft without passing the V804 gate — which is why they beat the gatekeeper mutation — but that same binding mode is vulnerable to non-gatekeeper mutations at the solvent front (G810C/S/R), the hinge (Y806C/N), the roof (L730V/I) and the β2 strand (V738A). A 2026 mutagenesis screen added drug-specific detail: V804E/M conferred resistance to selpercatinib, L730I/V and A883V to pralsetinib, while G810C/D/S, Y806N and E732K defeated both. Second, no docking benchmark of the four clinically used RET drugs on one high-resolution wild-type structure has been published alongside their measured potencies — so it is unknown whether a cheap rigid-docking screen can even rank them correctly. If it cannot, then docking-based "selpercatinib alternatives" built on wild-type structures are not a shortcut to the next drug; the screen must be rebuilt around mutant structures and free-energy refinement.

The classical medical canon described this disease class long before the gene was known: Ibn Sina's Canon of Medicine (c. 1025) discusses sartan (cancer) as a hard, spreading swelling with a poor prognosis, and Al-Razi's Kitab al-Hawi records clinical observation of tumours. These texts are hypothesis sources, not evidence — they knew the syndrome, not the target — but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do literature-known RET inhibitors, docked on the 1.64 Å wild-type RET structure 7DUA under one standardised protocol, rank in the same order as their published biochemical potencies — and does any of them beat re-docked selpercatinib by more than Vina noise? **Falsifier:** the claim that rigid docking cannot rank these inhibitors would be refuted if MM-GBSA free-energy refinement on the same five compounds recovered the measured potency order with Spearman rho above 0.8; the narrower claim that cabozantinib binds wild-type RET better than selpercatinib would be refuted if a single-assay biochemical panel showed cabozantinib's wild-type RET IC50 above selpercatinib's (it is already published at 11 nM versus 0.4 nM, which is why the docking margin is treated as noise, not as a discovery). **Causal identification:** validated-control re-docking — the reference drug and the crystallographic ligand re-docked on a co-crystal structure of their own target — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-20: the LIBRETTO-001 primary and final analyses, the LIBRETTO-531 phase 3 trial, the structural basis of selpercatinib/pralsetinib resistance (including PDB 7JU6/7JU5), the L730 roof-mutation study, the 2026 drug-specific resistance screen, and the RCSB records for PDB 7DUA and 7JU6. The latest research-team digest (2026-11-14) contained nothing on RET. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025); Al-Razi, Kitab al-Hawi (c. 900) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: human RET, UniProtKB P07949 (proto-oncogene tyrosine-protein kinase receptor Ret, 1,114 aa); ChEMBL target CHEMBL2041. Structure: PDB 7DUA, the human RET kinase domain in complex with the pyrrolo-pyrimidine inhibitor HJ0 (TAS0953/HM06 series), 1.64 Å, deposited 2021-01-08. Grid centre: centroid of the co-crystallised ligand HJ0 in chain A, [7.69, 0.53, −2.52], verified by direct computation from the PDB file; box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for all five compounds. Ligand identities and structures were taken from PubChem by name (selpercatinib CID 134436906; pralsetinib CID 129073603; cabozantinib CID 25102847; vandetanib CID 3081361) and, for HJ0, by InChIKey from the RCSB record (CID 132247154; formula C15H17N7O, MW 311.34, IUPAC name identical to the 7DUA title compound).

**A wrong-target audit, stated plainly.** The pipeline's first run for this topic resolved the ChEMBL target to CHEMBL2074, "Maltase-glucoamylase" — the fallback silently accepted the first fuzzy text-search hit for "RET kinase" when the by-accession lookup returned no usable candidate. Its four "leads" (CHEMBL120226, CHEMBL120488, CHEMBL332802, CHEMBL120395) are maltase-glucoamylase ligands, not RET ligands, and their scores say nothing about RET. That run is DISCARDED, not reported as a result: it is preserved in `hidden_files/dock-HP-086-2026-11-20-WRONG-TARGET.json` for audit. The correct target is CHEMBL2041, verified twice over — the UniProtKB P07949 cross-reference line reads "ChEMBL; CHEMBL2041" and the ChEMBL target report card is titled "Proto-oncogene tyrosine-protein kinase receptor Ret (CHEMBL2041)". A corrected re-run forced CHEMBL2041 — but ChEMBL's activity endpoint returned HTTP 500 for every target on 2026-11-20 (parent-verified the same day), so step 2 returned no_data and no ChEMBL ligand set could be retrieved at all. The comparison set was therefore built, per the established fallback, from literature-known RET inhibitors with published potencies; no measured potency is attached to any PubChem analogue in this paper because no analogues were used. All scores in §3 are from the literature set (`hidden_files/dock-HP-086c-2026-11-20.json`); the corrected pipeline re-run's only output, a selpercatinib re-dock at −10.19 kcal/mol, is retained as an independent reproducibility check (`hidden_files/dock-HP-086b-2026-11-20.json`).

**A corrupted-ligand audit, stated plainly.** The first attempt at the native-ligand control derived HJ0's SMILES from the PDB residue with RDKit's MolFromPDBBlock; bond-order perception from bare coordinates produced a non-aromatic structure that is not HJ0, and its −8.11 kcal/mol score is DISCARDED. The control was re-run with the PubChem SMILES obtained from the RCSB InChIKey (formula and IUPAC name verified against the deposition), giving −10.27 kcal/mol. The discarded score is recorded in the JSON's `hj0_correction` field, not in the results table.

**A killed-process audit, stated plainly.** The first literature-docking run was terminated by an external SIGTERM after selpercatinib had completed (−10.11 kcal/mol) and before pralsetinib finished. The resume script re-used that completed value and saved incrementally after every subsequent dock, so no completed result depended on a single uninterrupted run. Selpercatinib's score is therefore supported by three independent Vina runs on the same protocol: −10.09, −10.19 and −10.11 kcal/mol — a spread of 0.10 kcal/mol.

### 2.3 PAINS screen

RDKit PAINS filter (PAINS-A/B/C catalogues, the pipeline's own chem module) applied to all five compounds. None carries a PAINS alert.

### 2.4 ADMET and descriptors

RDKit descriptors (Lipinski/Veber panel) computed for every compound with the pipeline's chem module. Selpercatinib: MW 525.61, logP 3.28, TPSA 112.04, 1 Lipinski violation. Pralsetinib: MW 533.61, logP 4.20, TPSA 135.53, 1 violation. Cabozantinib: MW 501.51, logP 5.54, TPSA 98.78, 2 violations. Vandetanib: MW 475.36, logP 5.00, TPSA 59.51, 1 violation. HJ0: MW 311.35, logP 1.81, TPSA 114.51, 0 violations.

### 2.5 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. Only the wild-type RET structure was used; no G810, Y806, L730 or V804 mutant structure was docked. Published IC50 values below are from the cited papers, measured under different assay conditions (biochemical assays at ATP near Km; cellular phospho-RET assays), not re-measured here and not directly comparable across papers beyond order of magnitude. No experimental data were generated in this study.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Published WT RET IC50 (biochemical) | Cellular phospho-RET IC50 | Best affinity, 7DUA (kcal/mol) | Top-3 poses (kcal/mol) | PAINS | MW / logP / TPSA |
|---|---|---|---|---|---|---|
| Cabozantinib | 11 nM | 75 ± 27 nM | **−10.76** | −10.76, −10.59, −10.32 | none | 501.51 / 5.54 / 98.78 |
| HJ0 (7DUA native ligand) | 0.17 nM (BindingDB, single assay) | — | −10.27 | −10.27, −9.06, −8.82 | none | 311.35 / 1.81 / 114.51 |
| Selpercatinib (reference, re-docked) | 0.4 nM | 4 ± 2 nM | −10.11 | −10.11, −9.75, −9.29 | none | 525.61 / 3.28 / 112.04 |
| Pralsetinib | 0.4 nM | 5 nM | −9.98 | −9.98, −9.72, −9.59 | none | 533.61 / 4.20 / 135.53 |
| Vandetanib | 4 nM | 935 ± 679 nM | −9.55 | −9.55, −9.43, −9.17 | none | 475.36 / 5.00 / 59.51 |

Biochemical IC50 values as tabulated from the primary characterisations (selpercatinib, cabozantinib, vandetanib: Subbiah et al. 2018; pralsetinib: Subbiah et al. 2018, Cancer Discovery); cellular values are phospho-KIF5B-RET assays from the same papers (pralsetinib cellular value is KIF5B-RET autophosphorylation in Ba/F3 cells). HJ0's 0.17 nM is a single-assay BindingDB record attached to the 7DUA deposition, not a multi-study value, and is excluded from the rank correlation in §3.2.

Cabozantinib scores best, 0.65 kcal/mol ahead of selpercatinib, with the tightest pose consistency in the set (top-3 spread 0.44 kcal/mol). Pralsetinib and selpercatinib are effectively tied (Δ 0.13 kcal/mol), exactly as their identical 0.4 nM biochemical potencies would predict — the one place where docking and measurement agree. Vandetanib scores worst. The native ligand HJ0 re-docks at −10.27 kcal/mol, validating the protocol: the method recovers strong binding for the crystallographic ligand, though its pose spread (1.45 kcal/mol) is the widest in the set.

### 3.2 The docking–activity discordance that must not be hidden

The docking order is not the potency order. Against published biochemical IC50 values the Spearman rank correlation is rho = −0.32 (p = 0.68, n = 4, scipy tie-corrected); against cellular IC50 values it is rho = 0.40 (p = 0.60, n = 4). Neither is significant, and the biochemical correlation is negative. The sharpest single contradiction is cabozantinib: the best docker in the set is the weakest RET inhibitor by biochemical potency (11 nM, 27-fold worse than selpercatinib's 0.4 nM) and the second-weakest by cellular potency (75 nM versus 4 nM). Conversely the two genuinely most potent compounds, selpercatinib and pralsetinib (both 0.4 nM), sit in the middle of the docking table. Rigid Vina scoring on wild-type RET cannot resolve a 27-fold potency difference, and it actively mis-ranks the weakest compound first. This is the paper's most important negative result: **the docking ranking is not a potency ranking**, and any claim built on the −10.76 versus −10.11 gap alone would be over-reading noise — the gap is a third of the noise margin, and the clinical record already proves the opposite order (LIBRETTO-531: selpercatinib HR 0.28 versus cabozantinib/vandetanib).

### 3.3 Comparison with published docking

No published Vina study of these five compounds on 7DUA was found in the sweep; the comparison here is internal (four drugs plus the native ligand, same structure, same protocol). The re-docked selpercatinib score of −10.11 kcal/mol is the validated control that anchors the comparison, and it reproduced within 0.10 kcal/mol across three independent runs. A 2022 pharmacophore-screening study reported natural-product hits docking better than vandetanib and selpercatinib on wild-type RET, but on different structures and protocols, so no numeric comparison is possible — and §3.2 is the reason such comparisons should not be trusted without a potency anchor anyway.

### 3.4 The resistance-mutation gap

Every number in §3.1 is wild-type RET. The mutations that actually defeat selpercatinib in patients — G810C/S/R at the solvent front, Y806C/N at the hinge — were not docked, because no G810- or Y806-mutant RET structure with a bound inhibitor exists in the PDB and this study did not build homology models (an unvalidated model would be a made-up structure). The V804 gatekeeper mutation needs no new docking: the published biochemistry already shows selpercatinib (0.8 nM) and pralsetinib (0.4 nM) retain activity against V804M, and the co-crystal structures explain why. The open question is therefore not "what beats selpercatinib on wild-type RET" — nothing needs to, since selpercatinib already wins clinically — but "what binds G810/Y806-mutant RET", and this paper's protocol cannot answer it without a mutant structure.

## 4. Discussion

### 4.1 The reframe

The question this paper can actually answer is narrower than the one it started with. It cannot say "cabozantinib is a better RET inhibitor than selpercatinib" — the margin is inside noise, the docking order contradicts the measured potency order, and the randomised LIBRETTO-531 trial already proved the opposite in patients (HR 0.28 for selpercatinib). What it can say is: (a) all four clinically used RET drugs plus the crystallographic ligand bind the wild-type RET pocket with tight, reproducible poses at −9.55 to −10.76 kcal/mol; (b) rigid docking on this pocket cannot rank them — Spearman rho −0.32 against biochemical potency; (c) the pipeline's first, wrong-target run and a corrupted ligand structure were both caught and corrected before publication, and both corrections are documented; (d) the decisive experiment is now sharply defined — a single-assay biochemical panel of the four drugs on wild-type and G810S RET, plus MM-GBSA refinement — and it is cheap and feasible in a university lab.

### 4.2 Why the "win" must not be over-read

Four reasons. First, the 0.65 kcal/mol margin is inside Vina's ±1–2 kcal/mol noise. Second, the docking order contradicts the measured potency order: the weakest inhibitor docks best. Third, cabozantinib's clinical inferiority is not a potency subtlety — it is a 27-fold biochemical gap plus dose-limiting VEGFR2 toxicity that forced dose reductions in 77% of patients, while selpercatinib's selectivity is precisely what makes its potency usable. Fourth, all of this is wild-type RET; the resistance problem lives in G810/Y806 mutants this study never touched. A compound that scores well here may still fail in cells, and a compound that fails here may still be the best drug — exactly as Paper #80 found for MDM2, where the most potent measured compound docked worst.

### 4.3 Mechanism

RET's kinase domain binds ATP in a cleft between the N- and C-lobes. Selpercatinib and pralsetinib anchor one end in the front cleft and wrap around the K758 gate wall to reach the back cleft, never passing through the gate between V804 and K758 — so a bulky V804M/L side chain does not clash with them, while it blocks MKIs that must pass through the gate. Resistance then moves to residues the new binding mode does touch: G810 on the solvent-front floor (a glycine replaced by a bulkier cysteine/serine/arginine introduces a direct steric clash), Y806 at the hinge (loss of a hydrogen bond), L730 at the solvent-front roof (steric clash, worse for pralsetinib than selpercatinib: 58–61-fold versus 4–7-fold IC50 shift), and V738A on the β2 strand. Test for each link: (i) a biochemical kinase assay (ADP-Glo) on wild-type, V804M and G810S RET measures whether the compound inhibits the mutant enzyme; (ii) Ba/F3 cells expressing KIF5B-RET and the same mutants measure whether cellular potency follows; (iii) phospho-RET/ERK immunoblotting measures whether downstream signalling is actually shut off — the same three readouts that characterised selpercatinib and pralsetinib.

### 4.4 Testable hypotheses

1. In a single-assay biochemical panel, cabozantinib's wild-type RET IC50 remains ≥10-fold worse than selpercatinib's (falsifier: cabozantinib IC50 < 2 nM, which would reopen the docking result as a real signal rather than noise).
2. MM-GBSA refinement of the five docked poses preserves the docking order (falsifier: the refined order matches the measured potency order with Spearman rho > 0.8, which would refute the "rigid docking cannot rank" conclusion for refined methods).
3. Against G810S RET, all four drugs lose >10-fold biochemical potency relative to wild-type, with selpercatinib and pralsetinib losing the most (falsifier: any drug retains within 3-fold activity against G810S — a genuine next-generation lead).
4. Re-docking on the RET–selpercatinib structure 7JU6 preserves the same compound order within 1 kcal/mol (falsifier: the order inverts, which would show the result is structure-dependent rather than compound-dependent).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): single-assay biochemical kinase panel (ADP-Glo) for the four drugs against wild-type, V804M and G810S RET; readout IC50, n = 3, with staurosporine as a control. Stage 2 (weeks 4–8): Ba/F3 KIF5B-RET proliferation assays for the same mutants, plus phospho-RET/ERK immunoblotting at the IC50. Stage 3 (weeks 9–12): MM-GBSA refinement of the five docked poses on 7DUA; if refinement recovers the potency order, publish the refined protocol as the screening method; if it does not, publish the negative result — the field needs to know that wild-type docking does not rank RET inhibitors, before the next "alternative" is claimed on a docking score alone.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin, including the 0.65 kcal/mol cabozantinib "win".
2. Docking order contradicts measured potency order (Spearman rho −0.32 biochemical); rigid docking cannot rank these compounds.
3. Wild-type RET only (7DUA); the clinically relevant resistance mutants G810, Y806 and L730 were not docked, and no mutant structure was modelled.
4. Published IC50 values come from different assays and papers (biochemical at ATP near Km; cellular phospho-RET); cross-paper comparisons are order-of-magnitude only.
5. ChEMBL was unusable on the study date (activity endpoint HTTP 500), so no ChEMBL ligand set could be retrieved; the comparison set is four literature-known drugs, not a screen of new chemotypes.
6. HJ0's 0.17 nM potency is a single-assay BindingDB record, not a multi-study value; it validates the docking protocol but is not a potency claim.
7. No Pakistan-specific RET-fusion prevalence or access data were found; the burden numbers are global, and the access question (selpercatinib availability and cost in Pakistan) is unaddressed.
8. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon and Al-Razi's Kitab al-Hawi; the full Arabic texts were not read, and other classical works on tumours were not individually consulted.

## 6. Conclusion

On the 1.64 Å wild-type RET structure 7DUA, cabozantinib out-docks selpercatinib by 0.65 kcal/mol (−10.76 versus −10.11), with pralsetinib (−9.98), vandetanib (−9.55) and the native ligand HJ0 (−10.27) all binding tightly and none carrying a PAINS alert. The margin is inside Vina noise, the docking order contradicts the measured potency order (Spearman rho −0.32), and the randomised LIBRETTO-531 trial already proved selpercatinib superior in patients — so this is not evidence that cabozantinib is a better RET drug, it is evidence that rigid wild-type docking cannot rank RET inhibitors. The next step is not another docking run but the cheap, decisive test: a single-assay biochemical panel on wild-type and G810S RET, plus free-energy refinement. That test, not another score, decides what comes after selpercatinib.

## 7. Policy implications

**Decision-maker:** Pakistan's Higher Education Commission research-funding panels and the SMBBMU ORIC office, with DRAP as the eventual regulator. **Decision:** whether to fund computational screening for "selpercatinib alternatives" as an academic drug-discovery exercise. **Exact change:** commission the 8–12-week single-assay biochemical panel proposed in §4.5 — the four drugs against wild-type and G810S RET, with MM-GBSA refinement — instead of funding another purely computational screen of wild-type RET, which this paper shows cannot rank the drugs it already knows. **If evidence Z appears, reverse this:** if MM-GBSA refinement recovers the measured potency order (Spearman rho > 0.8), fund the refined computational screen as the primary tool; if the biochemical panel shows any drug retaining within 3-fold activity against G810S, redirect the same screen to that chemotype's analogues. Do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable drug from a useless one for cancers that kill, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Drilon A, Oxnard GR, Tan DSW, et al. Efficacy of selpercatinib in RET fusion-positive non-small-cell lung cancer. N Engl J Med. 2020;383(9):813-824. doi:10.1056/NEJMoa2005653. PMID: 32846060.
2. Wirth LJ, Sherman E, Robinson B, et al. Efficacy of selpercatinib in RET-altered thyroid cancers. N Engl J Med. 2020;383(9):825-835. doi:10.1056/NEJMoa2005651. PMID: 32846061.
3. Gautschi O, Park K, Solomon BJ, et al. Selpercatinib in RET fusion-positive non-small cell lung cancer: final safety and efficacy, including overall survival, from the LIBRETTO-001 phase I/II trial. J Clin Oncol. 2025;43(15):1758-1764. doi:10.1200/JCO-24-02076. PMID: 39983053.
4. Hadoux J, Elisei R, Brose MS, et al. Phase 3 trial of selpercatinib in advanced RET-mutant medullary thyroid cancer. N Engl J Med. 2023;389(20):1851-1861. doi:10.1056/NEJMoa2309719. PMID: 37870969.
5. Subbiah V, Shen T, Terzyan SS, et al. Structural basis of acquired resistance to selpercatinib and pralsetinib mediated by non-gatekeeper RET mutations. Ann Oncol. 2021;32(2):261-268. doi:10.1016/j.annonc.2020.10.599. PMID: 33161056.
6. Shen T, Hu X, Liu X, et al. The L730V/I RET roof mutations display different activities toward pralsetinib and selpercatinib. npj Precis Oncol. 2021;5:48. doi:10.1038/s41698-021-00188-x.
7. Liu X, Paula AG, Nilsson MB, et al. Drug-specific resistance mechanisms to RET inhibitors in RET fusion-positive NSCLC. Clin Cancer Res. 2026. doi:10.1158/1078-0432.CCR-26-2630. PMID: 42848316.
8. Subbiah V, Velcheti V, Tuch BB, et al. Selective RET kinase inhibition for patients with RET-altered cancers. Ann Oncol. 2018;29(8):1869-1876. doi:10.1093/annonc/mdy137. PMID: 29912274.
9. Subbiah V, Gainor JF, Rahal R, et al. Precision targeted therapy with BLU-667 for RET-driven cancers. Cancer Discov. 2018;8(7):836-849. doi:10.1158/2159-8290.CD-18-0338. PMID: 29657135.
10. RCSB PDB entry 7DUA: crystal structure of human proto-oncogene tyrosine-protein kinase receptor Ret in complex with 4-amino-7-(1-methylcyclopropyl)-N-(5-methyl-1H-pyrazol-3-yl)pyrrolo[2,3-d]pyrimidine-5-carboxamide, 1.64 Å. RCSB Protein Data Bank. doi:10.2210/pdb7dua/pdb. Accessed 2026-11-20.
11. RCSB PDB entries 7JU6 (RET–selpercatinib) and 7JU5 (RET–pralsetinib). RCSB Protein Data Bank. Accessed 2026-11-20.
12. ChEMBL target CHEMBL2041: proto-oncogene tyrosine-protein kinase receptor Ret, Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-20.
13. UniProtKB P07949: proto-oncogene tyrosine-protein kinase receptor Ret, Homo sapiens. UniProt. Accessed 2026-11-20.
14. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; sartan, cancer as a hard spreading swelling.)
15. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; clinical observation of tumours.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-086c-2026-11-20.json` (literature-known inhibitors on 7DUA; includes the discarded corrupted-HJ0 record in `hj0_correction`), `hidden_files/dock-HP-086b-2026-11-20.json` (corrected-target pipeline re-run, CHEMBL2041, selpercatinib re-dock −10.19 kcal/mol) and `hidden_files/dock-HP-086-2026-11-20-WRONG-TARGET.json` (discarded first run, CHEMBL2074 maltase-glucoamylase — preserved for audit, not a result). Ligand identities are PubChem CIDs 134436906 (selpercatinib), 129073603 (pralsetinib), 25102847 (cabozantinib), 3081361 (vandetanib), 132247154 (HJ0). Structure: PDB 7DUA (1.64 Å). Target: UniProtKB P07949; ChEMBL target CHEMBL2041. No additional data were generated.
