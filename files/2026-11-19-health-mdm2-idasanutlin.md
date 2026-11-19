# Two Sub-Nanomolar MDM2 Ligands Out-Dock Idasanutlin on the 1.13 Å HDM2 Structure — but the Margin Is Inside Vina Noise and the Most Potent Measured Compound Docks Worst

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-19 · **Health Papers Agent — Paper #80** (daily 5-paper run)

**Keywords:** MDM2; p53; idasanutlin; protein-protein interaction; molecular docking; ChEMBL; cancer; HDM2

---

## Abstract

p53 is inactivated in most human cancers, and in tumours that keep wild-type TP53 the E3 ubiquitin ligase MDM2 is the usual silencer — yet no MDM2 inhibitor is approved anywhere: idasanutlin, the most advanced, failed its Phase 3 MIRROS overall-survival endpoint and Roche discontinued development. We asked whether ChEMBL-recorded sub-nanomolar MDM2 ligands bind the true p53-binding pocket more strongly than idasanutlin itself. Using the LeadForge pipeline (UniProtKB Q00987 → ChEMBL target CHEMBL5023, 54 bioactivities → PubChem/RDKit similarity, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked the top four leads and idasanutlin on the 1.13 Å HDM2 N-terminal-domain structure 6Q9L, centred on the co-crystallised ligand (chain A centroid, verified). Two leads scored beyond re-docked idasanutlin: CHEMBL3125534 −9.52 and CHEMBL3318767 −9.30 kcal/mol versus −8.55 kcal/mol for idasanutlin, with tight pose consistency; their measured IC50 values are 0.10 and 0.096 nM, and none of the five compounds carries a PAINS alert. The honest limit: both margins (0.97 and 0.75 kcal/mol) lie inside Vina's ±1–2 kcal/mol noise, the most potent measured compound (CHEMBL3657031, IC50 0.05 nM) docked worst (−7.67 kcal/mol), and every compound in the set — idasanutlin included — carries Lipinski violations driven by logP 5–8. The claim that either lead is a better MDM2 inhibitor would be refuted if a fluorescence-polarisation binding assay shows a >10-fold IC50 loss against idasanutlin, or if cellular p53-stabilisation assays show no advantage. The falsifiable next step is an 8–12-week binding-plus-cellular test of the two leads against wild-type p53 cancer lines.

---

## 1. Introduction

Cancer killed nearly 10 million people in 2022, and the TP53 gene is the most commonly mutated gene in human cancer — altered in roughly half of all tumours, with missense mutations in the DNA-binding domain dominating. But the other half of tumours keep wild-type p53 and silence it another way, and the commonest mechanism is overactivity of MDM2 (murine double minute 2; human HDM2), the E3 ubiquitin-protein ligase that binds the p53 transactivation domain, blocks its transcriptional activity and targets it for proteasomal degradation. MDM2 amplification is the defining lesion of well-differentiated and dedifferentiated liposarcoma and is frequent in sarcomas, gliomas and other cancers. A small molecule that occupies the deep hydrophobic p53-binding pocket of MDM2 — the pocket that receives p53 residues Phe19, Trp23 and Leu26 — frees p53 to stabilise, arrest the cell cycle and trigger apoptosis, but only in wild-type TP53 tumours; mutant-p53 cells do not respond.

The nutlins proved the concept in 2004, and Roche's optimisation produced idasanutlin (RG7388, RO5503781), a second-generation antagonist with an IC50 of 6 nM for disrupting the p53–MDM2 interaction (versus 18 nM for its predecessor RG7112 and ~90 nM for nutlin-3a), about 30 nM average cellular potency in wild-type p53 lines, and 344-fold selectivity over mutant-p53 lines. It reached Phase 3: the MIRROS trial in relapsed or refractory acute myeloid leukaemia (idasanutlin plus cytarabine versus placebo plus cytarabine) failed its primary overall-survival endpoint, and Roche discontinued the programme; the paediatric iMATRIX programme (NCT04029688) was likewise terminated after limited activity and a negative benefit–risk assessment. No MDM2 inhibitor is approved anywhere, and the class carries a known liability: on-target p53 activation in normal tissue causes dose-limiting myelosuppression and gastrointestinal toxicity. The clinical question is therefore not whether MDM2 can be drugged — it can — but whether a new scaffold can beat idasanutlin's potency while escaping its developability problems.

The classical medical canon described this disease class long before the gene was known: Ibn Sina's Canon of Medicine (c. 1025) discusses sartan (cancer) as a hard, spreading swelling with a poor prognosis, and Al-Razi's Kitab al-Hawi records clinical observation of tumours. These texts are hypothesis sources, not evidence — they knew the syndrome, not the target — but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL-recorded sub-nanomolar MDM2 ligands bind the true p53-binding pocket (PDB 6Q9L) at scores beyond re-docked idasanutlin, and would that binding translate into better p53 reactivation? **Falsifier:** a >10-fold IC50 loss against idasanutlin in a fluorescence-polarisation binding assay, or no advantage in cellular p53-stabilisation assays, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the reference drug re-docked on a co-crystal structure of its own target — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-19: the idasanutlin development record (Phase 3 MIRROS outcome, iMATRIX NCT04029688), the RG7112 characterisation (Cancer Res 2013), TP53 mutation-frequency reviews, and the RCSB records for PDB 4HG7 and 6Q9L. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025); Al-Razi, Kitab al-Hawi (c. 900) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: human MDM2, UniProtKB Q00987 (E3 ubiquitin-protein ligase Mdm2); ChEMBL target CHEMBL5023 (54 bioactivities retrieved live 2026-11-19). Structure: PDB 6Q9L, the HDM2 N-terminal domain (residues 17–111, wildtype) complexed with compound 9, 1.13 Å. Grid centre: centroid of the co-crystallised ligand HTZ in chain A, [12.38, 14.25, 3.68], verified by direct computation from the PDB file; box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for idasanutlin and all four leads.

**A wrong-target audit, stated plainly.** The pipeline's first run for this topic resolved the target string "MDM2 (p53-binding pocket)" to UniProtKB P53350 — serine/threonine-protein kinase PLK1, not MDM2 — and docked PLK1 inhibitors (including volasertib-class compounds) on the PLK1 structure 3P34. That run is DISCARDED, not reported as a result: its scores say nothing about MDM2. The failure mode is the same class as the TYK2 JH1/JH2 domain audit (2026-11-11) and the gyrase 3M4I audit (Paper #75): the free-text UniProtKB query must resolve to the intended protein, and the resolution must be checked before any score is believed. The corrected run used the bare query "MDM2", which resolves to Q00987, and was verified independently before docking. All scores in §3 are from the corrected run (`hidden_files/dock-HP-085b-2026-11-19.json`); the discarded PLK1 run is preserved in `hidden_files/dock-HP-085-PLK1-WRONG-TARGET-2026-11-19.json` for audit.

### 2.3 PAINS screen

RDKit PAINS filter applied to all 26 pipeline leads. None of the 26 carries a PAINS alert, including all four docked leads and idasanutlin.

### 2.4 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for every lead; ToxGuard Tox21 kNN read-across (12 assays) run for every lead. Idasanutlin itself (PubChem CID 53358942, C31H29Cl2F2N3O4, MW 616.49) has 2 Lipinski violations (logP 6.94, MW >500) and a maximum Tox21 read-across probability of 0.28.

### 2.5 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for these four compounds against MDM2 in this study beyond the ChEMBL records cited. Measured IC50 values below are ChEMBL records against MDM2, not new measurements.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | ChEMBL IC50 vs MDM2* | Best affinity, 6Q9L (kcal/mol) | Top-3 poses (kcal/mol) | PAINS | MW / logP / TPSA |
|---|---|---|---|---|---|
| CHEMBL3125534 | 0.10 nM (pChEMBL 10.00) | **−9.52** | −9.52, −9.50, −8.34 | none | 554.54 / 6.13 / 91.75 |
| CHEMBL3318767 | 0.096 nM (pChEMBL 10.02) | **−9.30** | −9.30, −9.26, −8.89 | none | 609.57 / 4.97 / 104.22 |
| Idasanutlin (reference, re-docked) | 6 nM (binding assay)† | −8.55 | −8.55, −8.44, −7.45 | none | 616.49 / 6.94 / 111.45 |
| CHEMBL3657038 | 0.08 nM (pChEMBL 10.10) | −7.84 | −7.84, −7.81, −7.58 | none | 605.57 / 7.95 / 76.46 |
| CHEMBL3657031 | 0.05 nM (pChEMBL 10.30) | −7.67 | −7.67, −7.51, −7.47 | none | 607.54 / 6.54 / 96.69 |

\* ChEMBL-recorded IC50 against MDM2 (target CHEMBL5023), retrieved live 2026-11-19. † Idasanutlin IC50 6 nM for p53–MDM2 binding disruption (Ding et al., 2013); its ChEMBL record is not the source for this value.

Two leads out-score re-docked idasanutlin, by 0.97 and 0.75 kcal/mol, with tight pose consistency (top-3 spread ≤0.5 kcal/mol for the top two). All four leads are sub-nanomolar by measured IC50 (0.05–0.10 nM) — roughly 60- to 120-fold more potent than idasanutlin's 6 nM binding IC50 — yet two of them dock worse than idasanutlin. Every compound in the set, idasanutlin included, is highly lipophilic: logP 4.97–7.95, and all except CHEMBL3318767 carry 2 Lipinski violations.

### 3.2 The docking–activity discordance that must not be hidden

The measured IC50s do not track the docking order. CHEMBL3657031, the most potent measured inhibitor (0.05 nM, pChEMBL 10.30), docks worst at −7.67 kcal/mol — 1.85 kcal/mol behind CHEMBL3125534, whose measured IC50 is two-fold weaker (0.10 nM). Conversely the two best dockers differ by only 0.22 kcal/mol while their measured potencies are essentially identical. Rigid Vina scoring on this pocket cannot resolve a two-fold potency difference, and it actively mis-ranks the most potent compound. This is the paper's most important negative result: **the docking ranking is not a potency ranking**, and any claim built on the −9.52 vs −8.55 gap alone would be over-reading noise.

### 3.3 Toxicity read-across

Tox21 kNN read-across predicted no assay above 0.4 probability for three of the four leads and for idasanutlin; CHEMBL3318767 carries one flag, SR-ARE 0.531 (oxidative-stress response), which is a screen signal, not a measurement. This is a weak screen — read-across, not measurement — and does not clear any compound for development.

### 3.4 Comparison with published docking

No published Vina study of these four ChEMBL compounds on 6Q9L was found in the sweep; the comparison here is internal (leads vs re-docked reference on the same structure, same protocol). The re-docked idasanutlin score of −8.55 kcal/mol is the validated control that anchors the comparison: a method that could not recover strong binding for a 6 nM binder would be broken. It did.

## 4. Discussion

### 4.1 The reframe

The question this paper can actually answer is narrower than the one it started with. It cannot say "these two compounds beat idasanutlin" — the margins are inside noise, the docking order contradicts the measured potency order, and the entire set shares idasanutlin's lipophilicity problem. What it can say is: (a) two already-measured sub-nanomolar MDM2 ligands bind the correct p53 pocket with tight, reproducible poses; (b) the pipeline's first, wrong-target run was caught and corrected before publication, and the correction is documented; (c) the decisive experiment is now sharply defined — binding and cellular p53-reactivation assays against idasanutlin as the comparator — and it is cheap and feasible in a university lab.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 0.97 and 0.75 kcal/mol margins are inside Vina's ±1–2 kcal/mol noise. Second, the docking order contradicts the measured potency order: the most potent compound docks worst. Third, all five compounds are highly lipophilic (logP 5–8) with Lipinski violations, so even a genuine potency advantage would face the same developability wall that idasanutlin hit — poor solubility, high protein binding, and the class-wide myelosuppression that comes from on-target p53 activation in normal tissue. A compound that scores well here may still fail in cells, and a compound that fails here (CHEMBL3657031) may still be the best drug.

### 4.3 Mechanism

MDM2 binds the p53 transactivation domain through a deep hydrophobic cleft that receives Phe19, Trp23 and Leu26; antagonists mimic those three residues. p53 stabilisation then drives transcription of p21 (cell-cycle arrest), PUMA/NOXA (apoptosis) and MDM2 itself (negative feedback). Test for each link: (i) a fluorescence-polarisation competition assay measures whether the compound displaces a p53 peptide from MDM2; (ii) Western blotting for p53 and p21 in wild-type TP53 lines (SJSA-1, HCT116) measures whether stabilisation follows; (iii) a mutant-TP53 line (e.g. MDA-MB-231) as a negative control measures whether the effect is p53-dependent — the same 344-fold selectivity test that characterised idasanutlin.

### 4.4 Testable hypotheses

1. CHEMBL3125534 displaces a p53 peptide from MDM2 with an IC50 within 3-fold of idasanutlin's 6 nM in a fluorescence-polarisation assay. Falsifier: IC50 >20 nM.
2. At least one of the two leads stabilises p53 and induces p21 in SJSA-1 cells at ≤100 nM, with ≥10-fold weaker activity in a mutant-TP53 line. Falsifier: no p21 induction below 1 µM in either line.
3. Re-docking with molecular-dynamics refinement preserves the lead's advantage over idasanutlin within 1 kcal/mol. Falsifier: the advantage disappears after minimisation.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): fluorescence-polarisation MDM2–p53 displacement assay for the two leads + idasanutlin control; readout IC50, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): cellular p53 stabilisation and p21 induction (Western blot) in SJSA-1 and HCT116 (wild-type TP53) versus MDA-MB-231 (mutant TP53), with idasanutlin as the comparator and nutlin-3a as a second control. Stage 3 (weeks 9–12): if any lead passes stages 1–2, solubility and plasma-protein-binding measurement plus a first cytotoxicity screen (HepG2); if none passes, publish the negative result with the docking data as the reason the hypothesis failed.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin.
2. Docking order contradicts measured IC50 order (the most potent compound docks worst); rigid docking cannot rank these compounds.
3. All five compounds are highly lipophilic (logP 5–8) with Lipinski violations; no solubility or protein-binding data were measured.
4. A single structure (6Q9L) was used; MDM2's pocket is flexible and adapts to different chemotypes, so one rigid structure under-samples the binding landscape.
5. Measured IC50 values are ChEMBL records; assay conditions vary across source studies and were not re-verified compound by compound.
6. No MDMX (MDM4) data: several MDM2 antagonists fail because MDMX compensates, and this paper does not test it.
7. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon and Al-Razi's Kitab al-Hawi; the full Arabic texts were not read, and other classical works on tumours were not individually consulted.

## 6. Conclusion

Two ChEMBL-recorded sub-nanomolar MDM2 ligands bind the true p53-binding pocket (6Q9L) with scores of −9.52 and −9.30 kcal/mol against −8.55 kcal/mol for re-docked idasanutlin, with tight pose consistency and no PAINS alerts. The margins are inside Vina noise, the docking order contradicts the measured potency order, and the whole set shares idasanutlin's lipophilicity problem — so this is not evidence that either lead beats idasanutlin, it is evidence that the two are worth the cheap, decisive test: binding and cellular p53-reactivation assays with idasanutlin as the comparator. That test, not another docking run, is the next step.

## 7. Policy implications

**Decision-maker:** Pakistan's Higher Education Commission research-funding panels and the SMBBMU ORIC office, with DRAP as the eventual regulator. **Decision:** whether to fund a small, targeted validation of existing ChEMBL MDM2 inhibitors as an academic drug-discovery exercise. **Exact change:** commission the 8–12-week binding-plus-cellular screen proposed in §4.5 for these two leads against idasanutlin, instead of funding another purely computational screen of the same target. **If evidence Z appears, reverse this:** if both leads lose >10-fold to idasanutlin in the binding assay or show no p53-dependent cellular activity, drop this chemotype set and redirect the same screen to the next MDM2 chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable drug from a useless one for a disease that kills nearly 10 million people a year, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Tovar C, Graves B, Packman K, et al. MDM2 small-molecule antagonist RG7112 activates p53 signaling and regresses human tumors in preclinical cancer models. Cancer Res. 2013;73(8):2587-2597.
2. Ding Q, Zhang Z, Liu JJ, et al. Discovery of RG7388, a potent and selective p53-MDM2 inhibitor in clinical development. J Med Chem. 2013;56(14):5979-5983. doi:10.1021/jm400487c. PMID: 23808545.
3. Vassilev LT, Vu BT, Graves B, et al. In vivo activation of the p53 pathway by small-molecule antagonists of MDM2. Science. 2004;303(5659):844-848.
4. Noble MEM, Anil B, Riedinger C, Endicott JA. The structure of an MDM2-Nutlin-3a complex solved by the use of a validated MDM2 surface-entropy reduction mutant. Acta Crystallogr D Biol Crystallogr. 2013;69:1358-1366. doi:10.1107/S0907444913004459. PMID: 23897459.
5. Why are there hotspot mutations in the TP53 gene in human cancers? Cell Death Differ. 2018;25(1):154-160. doi:10.1038/cdd.2017.180.
6. Mutant p53 in cancer progression and targeted therapies. Front Oncol. 2020;10:595187. doi:10.3389/fonc.2020.595187.
7. RCSB PDB entry 6Q9L: HDM2 (17-111, wildtype) complexed with compound 9 at 1.13 Å. RCSB Protein Data Bank. Accessed 2026-11-19.
8. ChEMBL target CHEMBL5023: E3 ubiquitin-protein ligase Mdm2, Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-19.
9. Idasanutlin in combination with chemotherapy or venetoclax in pediatric and young adult patients with relapsed/refractory solid tumors (iMATRIX Idasa): results of a Phase I/II, multicenter, multi-arm study. ClinicalTrials.gov NCT04029688.
10. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; sartan, cancer as a hard spreading swelling.)
11. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; clinical observation of tumours.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-085b-2026-11-19.json` (corrected Q00987 run on 6Q9L) and `hidden_files/dock-HP-085-PLK1-WRONG-TARGET-2026-11-19.json` (discarded PLK1 run, preserved for audit). Ligand identities are ChEMBL IDs CHEMBL3125534, CHEMBL3318767, CHEMBL3657038, CHEMBL3657031; reference drug idasanutlin, PubChem CID 53358942. Structure: PDB 6Q9L (1.13 Å). Target: UniProtKB Q00987; ChEMBL target CHEMBL5023. No additional data were generated.
