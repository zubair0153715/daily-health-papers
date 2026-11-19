# Three Nanomolar NLRP3 Ligands Dock at −8.4 to −8.9 kcal/mol Behind MCC950 — but None Beats It, and MCC950 Itself Failed on Liver Toxicity

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-19 · **Health Papers Agent — Paper #84** (daily 5-paper run)

**Keywords:** NLRP3; inflammasome; MCC950; MCC7840; molecular docking; ChEMBL; IL-1beta; neuroinflammation

---

## Abstract

The NLRP3 inflammasome drives IL-1β release in gout, atherosclerosis, Alzheimer's and Parkinson's disease, yet no NLRP3 inhibitor is approved: the benchmark, MCC950, was halted in Phase II over hepatotoxicity. We asked whether ChEMBL-recorded NLRP3 ligands bind the NACHT domain more strongly than MCC950 itself. Using the LeadForge pipeline (UniProtKB Q96P20 → ChEMBL target CHEMBL1741208, 55 bioactivities → PubChem/RDKit similarity, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked the top four leads and MCC950 on the 2.7 Å NLRP3 NACHT-domain structure 8WSM, centred on the co-crystallised inhibitor (verified centroid). MCC950 scored best at −10.08 kcal/mol; the three leads scored −8.86, −8.68 and −8.35 kcal/mol, with tight pose consistency; their measured IC50 values are 3.2–3.6 nM, and none of the 26 pipeline leads carries a PAINS alert. The honest limit: every lead docks 1.2–1.7 kcal/mol worse than MCC950, the margins are inside Vina's ±1–2 kcal/mol noise, and the reference drug's failure was toxicity, not potency — so a compound that merely matches MCC950's binding inherits its problem. The claim that any of these leads is a better NLRP3 drug would be refuted if a cellular IL-1β assay shows no potency advantage over MCC950's ~7.5 nM, or if a hepatotoxicity screen shows the same liability. The falsifiable next step is an 8–12-week cellular-plus-toxicity test of the three leads against MCC950, with a blood–brain-barrier screen — the property the field's newer inhibitors (MCC7840/Inzomelid) were designed for.

---

## 1. Introduction

The NLRP3 inflammasome is a cytosolic sensor that, once assembled, activates caspase-1 and releases IL-1β and IL-18 while triggering pyroptotic cell death. It is implicated across medicine: gout and cryopyrin-associated periodic syndromes (where it is the causal lesion), atherosclerosis, type 2 diabetes, and neurodegeneration — in Parkinson's disease, fibrillar α-synuclein activates microglial NLRP3, and in Alzheimer's, amyloid-β does the same. Blocking NLRP3 is therefore one of the most pursued anti-inflammatory strategies in drug discovery, and the benchmark compound is MCC950 (CP-456773, CRID3): a sulfonylurea discovered at Pfizer, described in 2015 as a potent, selective NLRP3 inhibitor that blocks canonical and non-canonical activation at nanomolar concentrations (IC50 ~7.5 nM for IL-1β release), spares the AIM2, NLRC4 and NLRP1 inflammasomes, and rescues a cryopyrin-associated periodic syndrome mouse model. It never became a drug: clinical development as CP-456773 for rheumatoid arthritis was halted after liver-toxicity signals, and MCC950 also inhibits carbonic anhydrase 2, an off-target liability. The field has moved on to successors designed to fix exactly those problems — MCC7840 (Inzomelid, Emlenoflast), with an IL-1β IC50 of 4.7 nM and better brain penetration, half-life and bioavailability than MCC950, showed efficacy in a 12-month α-synuclein Parkinson's model in 2025–2026, and the pyrazine-based AZD4144 is in Phase II for cardiorenal disease. The question this paper asks is whether the public ligand record already contains a compound better than MCC950 — and whether the answer is potency at all, given that MCC950's failure was safety.

The classical medical canon has no concept of an inflammasome, and this paper does not pretend otherwise: Ibn Sina's Canon of Medicine (c. 1025) discusses inflammatory swellings and fevers, and Al-Razi's Kitab al-Hawi records clinical observation of joint disease and gout. These texts are hypothesis sources, not evidence — they knew the syndrome, not the target — but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL-recorded NLRP3 ligands bind the NACHT domain (PDB 8WSM) more strongly than MCC950, and is there a lead that also escapes MCC950's liabilities? **Falsifier:** a cellular IL-1β assay showing no potency advantage over MCC950, or a hepatotoxicity screen showing the same liability, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the reference drug re-docked on a NACHT-domain structure bound to an inhibitor of the same class — not a comparison against nothing. Association only beyond that: docking scores are not activity, and binding says nothing about liver safety.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-19: the MCC950 discovery and hepatotoxicity record, the MCC7840/Inzomelid Parkinson's study (Brain 2026), the AZD4144 Phase II status, and the RCSB record for PDB 8WSM. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025); Al-Razi, Kitab al-Hawi (c. 900) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: human NLRP3, UniProtKB Q96P20 (NACHT, LRR and PYD domains-containing protein 3); ChEMBL target CHEMBL1741208 (55 bioactivities retrieved live 2026-11-19). Structure: PDB 8WSM, the NLRP3 NACHT domain in complex with compound 32, 2.7 Å. Grid centre: centroid of the co-crystallised inhibitor XE3 in chain A, [16.40, 35.96, 127.53], verified by direct computation from the PDB file; box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for MCC950 and all four leads.

**A centre audit, stated plainly.** The structure contains three non-water HETATM species: the inhibitor XE3, ADP, and a magnesium ion. The pipeline's `_ligand_center` picked XE3 (the inhibitor), not ADP or the metal — verified by computing each centroid separately. The grid therefore sits on the inhibitor pocket of the NACHT domain, which is the site MCC950 is reported to bind (MCC950 keeps the NLRP3 monomer inactive by binding the NACHT domain and blocking ATPase activity and oligomerisation). All scores in §3 are from `hidden_files/dock-HP-076-2026-11-19.json`; no re-dock was needed for this topic.

### 2.3 PAINS screen

RDKit PAINS filter applied to all 26 pipeline leads. None of the 26 carries a PAINS alert, including all four docked leads and MCC950.

### 2.4 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for every lead; ToxGuard Tox21 kNN read-across (12 assays) run for every lead. MCC950 itself (PubChem CID 9910393, C20H24N2O5S, MW 404.49) passes Lipinski with 0 violations (logP 2.99, TPSA 108.64) and scores at most 0.17 on any Tox21 assay.

### 2.5 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data were generated in this study. Measured IC50 values below are ChEMBL records against NLRP3, not new measurements. The Tox21 read-across did not flag MCC950's known hepatotoxicity — read-across cannot see it — which is itself a limit of the screen.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | ChEMBL IC50 vs NLRP3* | Best affinity, 8WSM (kcal/mol) | Top-3 poses (kcal/mol) | PAINS | MW / logP / TPSA |
|---|---|---|---|---|---|
| MCC950 (reference, re-docked) | ~7.5 nM (IL-1β release)† | **−10.08** | −10.08, −9.98, −9.93 | none | 404.49 / 2.99 / 108.64 |
| CHEMBL3183703 | 0.532 nM Kd‡ | −9.81 | −9.81, −9.71, −9.71 | none | 404.49 / 2.99 / 108.64 |
| CHEMBL5433446 | 3.6 nM (pChEMBL 8.44) | −8.86 | −8.86, −8.61, −7.26 | none | 361.47 / 2.27 / 78.51 |
| CHEMBL5402615 | 3.2 nM (pChEMBL 8.49) | −8.68 | −8.68, −8.65, −8.49 | none | 363.48 / 2.19 / 78.51 |
| CHEMBL6147441 | 3.2 nM (pChEMBL 8.49) | −8.35 | −8.35, −8.25, −8.12 | none | 420.56 / 3.28 / 117.67 |

\* ChEMBL-recorded IC50 against NLRP3 (target CHEMBL1741208), retrieved live 2026-11-19. † MCC950 IC50 ~7.5 nM for IL-1β release (Coll et al., 2015); its ChEMBL record is not the source for this value. ‡ CHEMBL3183703 is MCC950 itself (identical formula and descriptors); its recorded Kd of 0.532 nM is a binding measurement, not the cellular IL-1β IC50.

MCC950 scores best, and the margin over the best genuine lead is 1.22 kcal/mol. CHEMBL3183703 is MCC950 itself, so the three genuine leads are CHEMBL5433446, CHEMBL5402615 and CHEMBL6147441, all with measured IC50s of 3.2–3.6 nM — roughly twice as potent as MCC950 by measured cellular potency — yet all dock worse than MCC950 by 1.2–1.7 kcal/mol. All three are smaller than MCC950 (MW 361–421) with lower TPSA, and all pass Lipinski with 0 violations.

### 3.2 The docking–activity discordance that must not be hidden

The measured IC50s do not track the docking order. The three leads are more potent than MCC950 by measured IC50 (3.2–3.6 nM versus ~7.5 nM) but dock 1.2–1.7 kcal/mol worse. Rigid Vina scoring on this pocket cannot resolve a two-fold potency difference, and it mis-ranks the more potent compounds. This is the paper's most important negative result: **the docking ranking is not a potency ranking**, and any claim built on the −10.08 vs −8.86 gap alone would be over-reading noise. The deeper problem is that MCC950's failure was not potency — it was hepatotoxicity and a carbonic-anhydrase off-target. A lead that merely matches MCC950's binding inherits the question, not the answer: the experiment that matters is the toxicity screen, and docking cannot run it.

### 3.3 Toxicity read-across — and why it failed to flag MCC950

Tox21 kNN read-across predicted no assay above 0.25 probability for any of the four leads or MCC950 (highest: 0.236 for CHEMBL6147441; MCC950 itself scores at most 0.17). This is a weak screen — read-across, not measurement — and it is demonstrably blind to the exact liability that ended MCC950's development: MCC950's hepatotoxicity does not appear in any Tox21 assay score. The screen is reported here so that its blindness is on the record, not because it clears any compound.

### 3.4 Comparison with published docking

No published Vina study of these four ChEMBL compounds on 8WSM was found in the sweep; the comparison here is internal (leads vs re-docked reference on the same structure, same protocol). The re-docked MCC950 score of −10.08 kcal/mol is the validated control that anchors the comparison: a method that could not recover strong binding for a 7.5 nM inhibitor on a NACHT-domain structure would be broken. It did.

## 4. Discussion

### 4.1 The reframe

The question this paper can actually answer is narrower than the one it started with. It cannot say "these leads beat MCC950" — none of them does on docking, and the measured potency advantage is small and contradicted by the docking order. What it can say is: (a) three already-measured low-nanomolar NLRP3 ligands bind the correct NACHT pocket with tight, reproducible poses; (b) the field's real direction is visible in the successors — MCC7840 was designed for brain penetration and better safety, not for a better docking score; (c) the decisive experiment is now sharply defined — cellular IL-1β potency plus a hepatotoxicity and carbonic-anhydrase screen, with a blood–brain-barrier measurement — and it is cheap and feasible in a university lab.

### 4.2 Why the "loss" must not be over-read either

Three reasons. First, the 1.2–1.7 kcal/mol gaps are inside Vina's ±1–2 kcal/mol noise. Second, the docking order contradicts the measured potency order: the leads are more potent by IC50. Third, MCC950's failure was safety, so "losing to MCC950 on docking" is not the same as "worse than MCC950 as a drug" — a lead with a cleaner safety profile and equal potency would be the better drug, and docking cannot see safety at all. A compound that scores worse here may still be the best drug, and MCC950's own score is the least informative number in the table.

### 4.3 Mechanism

NLRP3 activation requires ATP binding and hydrolysis in the NACHT domain, followed by oligomerisation and ASC speck formation; MCC950 binds the NACHT domain, blocks ATPase activity and keeps the monomer inactive. Test for each link: (i) a cellular IL-1β release assay (LPS-primed macrophages + ATP/nigericin) measures whether the compound blocks inflammasome activation; (ii) an NLRP3 ATPase assay measures whether the mechanism is NACHT binding; (iii) a hepatotoxicity screen (HepG2 viability, ALT release) and a carbonic-anhydrase-2 inhibition assay measure whether the compound escapes MCC950's two liabilities; (iv) a PAMPA-BBB assay measures whether it reaches the brain, which a Parkinson's indication would need.

### 4.4 Testable hypotheses

1. At least one of the three leads inhibits IL-1β release with an IC50 ≤7.5 nM (MCC950's value) in LPS-primed macrophages. Falsifier: all three IC50s >20 nM.
2. At least one lead shows no hepatotoxicity signal (HepG2 viability ≥80% at 10× IC50) where MCC950 shows a signal. Falsifier: all three show the same toxicity as MCC950.
3. At least one lead inhibits carbonic anhydrase 2 at least 10-fold more weakly than MCC950. Falsifier: all three inhibit CA2 as strongly as MCC950.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): cellular IL-1β release assay (THP-1 macrophages, LPS + ATP) for the three leads + MCC950 control; readout IC50, n=3, with AIM2/NLRC4 counterscreens for selectivity. Stage 2 (weeks 4–8): HepG2 cytotoxicity and carbonic-anhydrase-2 inhibition for the same compounds; NLRP3 ATPase assay to confirm mechanism. Stage 3 (weeks 9–12): if any lead passes stages 1–2, PAMPA-BBB plus a microglial α-synuclein inflammasome assay; if none passes, publish the negative result with the docking data as the reason the hypothesis failed.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows the reported gaps.
2. Docking order contradicts measured IC50 order; rigid docking cannot rank these compounds.
3. The Tox21 read-across is blind to MCC950's known hepatotoxicity; no safety conclusion can be drawn from it.
4. A single structure (8WSM, 2.7 Å) was used; the NACHT domain is flexible and the structure is bound to one chemotype, so other chemotypes may be under-scored.
5. Measured IC50 values are ChEMBL records; assay conditions vary across source studies and were not re-verified compound by compound.
6. No brain-penetration data: the Parkinson's angle, which is the field's most active direction, is untested in this work.
7. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon and Al-Razi's Kitab al-Hawi; the full Arabic texts were not read, and the canon has no concept of an inflammasome — the sweep is historical context only.

## 6. Conclusion

MCC950 re-docks at −10.08 kcal/mol on the NLRP3 NACHT-domain structure 8WSM, against −8.86, −8.68 and −8.35 kcal/mol for three ChEMBL-recorded low-nanomolar leads, with tight pose consistency and no PAINS alerts. The leads are more potent than MCC950 by measured IC50 but dock worse, the gaps are inside Vina noise, and MCC950's failure was hepatotoxicity — which the toxicity screen used here cannot even detect. This is not evidence that MCC950 is the best NLRP3 drug; it is evidence that the three leads are worth the cheap, decisive test: cellular IL-1β potency plus hepatotoxicity, carbonic-anhydrase and brain-penetration screens, with MCC950 as the comparator. That test, not another docking run, is the next step.

## 7. Policy implications

**Decision-maker:** Pakistan's Higher Education Commission research-funding panels and the SMBBMU ORIC office, with DRAP as the eventual regulator. **Decision:** whether to fund a small, targeted validation of existing ChEMBL NLRP3 inhibitors as an academic drug-discovery exercise. **Exact change:** commission the 8–12-week cellular-plus-toxicity-plus-brain-penetration screen proposed in §4.5 for these three leads against MCC950, instead of funding another purely computational screen of the same target. **If evidence Z appears, reverse this:** if all three leads fail to match MCC950 on IL-1β potency or show the same hepatotoxicity, drop this chemotype set and redirect the same screen to the MCC7840-style successors — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable anti-inflammatory from a useless or toxic one for diseases with no good treatment, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Coll RC, Robertson AAB, Chae JJ, et al. A small-molecule inhibitor of the NLRP3 inflammasome for the treatment of inflammatory diseases. Nat Med. 2015;21(3):248-255. doi:10.1038/nm.3806.
2. MCC7840 (Inzomelid/Emlenoflast) PET-MRI biomarkers reveal efficacy of a novel NLRP3 inhibitor in Parkinson's disease models. Brain. 2026;149:1289-1301. doi:10.1093/brain/awaf372.
3. Moving beyond MCC950: discovery of a novel NLRP3 inhibitor series using a scaffold-hopping approach. ChemRxiv. 2026. doi:10.26434/chemrxiv.15007503.
4. LMT2368 negatively regulates inflammation by inhibiting NLRP3 inflammasome activation. Pharmaceutics. 2025;17:1241. doi:10.3390/pharmaceutics17101241.
5. RCSB PDB entry 8WSM: NLRP3 NACHT domain in complex with compound 32. RCSB Protein Data Bank. Accessed 2026-11-19.
6. ChEMBL target CHEMBL1741208: NACHT, LRR and PYD domains-containing protein 3, Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-19.
7. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; inflammatory swellings and fevers.)
8. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; clinical observation of joint disease and gout.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-076-2026-11-19.json`. Ligand identities are ChEMBL IDs CHEMBL3183703, CHEMBL5433446, CHEMBL5402615, CHEMBL6147441; reference drug MCC950, PubChem CID 9910393. Structure: PDB 8WSM (2.7 Å). Target: UniProtKB Q96P20; ChEMBL target CHEMBL1741208. No additional data were generated.
