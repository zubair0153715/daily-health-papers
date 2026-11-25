# Etavopivat Out-Scores Mitapivat by 0.09 kcal/mol on the Mitapivat-Bound PKR Structure 8XFD — a Dead Heat Between Two Pyruvate-Kinase Activators, and a 2.74 kcal/mol Gap to the Discontinued Tebapivat

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-24 · **Health Papers Agent — Paper #106** (daily 5-paper run)

**Keywords:** pyruvate kinase; PKR activator; mitapivat; beta-thalassaemia; sickle-cell disease; molecular docking; etavopivat; Pakistan

---

## Abstract

Beta-thalassaemia is Pakistan's most common inherited blood disorder: 5–8% of the population carries the trait, more than 10 million carriers, about 5,000 children born with thalassaemia major every year, and roughly 100,000 people living with transfusion-dependent disease. Red-cell pyruvate kinase (PKR) activation raises red-cell ATP and lowers 2,3-diphosphoglycerate, a mechanism now validated by mitapivat, approved for pyruvate-kinase deficiency in 2022 and for thalassaemia anaemia in December 2025. We asked whether the newer activators etavopivat and tebapivat bind the allosteric activator pocket more strongly than mitapivat. Using the LeadForge pipeline (UniProtKB P30613 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we docked mitapivat, etavopivat and tebapivat on 8XFD, the 2.10 Å crystal structure of erythrocyte pyruvate kinase in complex with mitapivat itself, centred exactly on the co-crystallised mitapivat (centre audit via dock._ligand_center). Mitapivat re-docked at −11.06 kcal/mol. Etavopivat scored −11.15 kcal/mol — ahead by 0.09 kcal/mol, a dead heat inside Vina's ±1–2 kcal/mol noise — while tebapivat scored −8.32 kcal/mol, 2.74 kcal/mol behind mitapivat, a gap larger than the noise. The honest limit: all three are PAINS-clean and Lipinski-compliant, so the difference is not a size or artefact effect, but the scores are rigid-docking numbers on one structure, and mitapivat's own score moves by 0.96 kcal/mol between the erythrocyte structure used here and the liver-isoform structure 7FS3 (−12.02 kcal/mol) — a measure of the method's structural sensitivity. The falsifiable next step is a single-assay PKR activation comparison (EC50) of the three activators under identical conditions: if etavopivat's EC50 is not within 3-fold of mitapivat's, the dead-heat claim is refuted.

---

## 1. Introduction

Mature red blood cells have no nucleus and no mitochondria, so glycolysis is their only source of ATP, and pyruvate kinase — which catalyses phosphoenolpyruvate plus ADP to pyruvate plus ATP — is the rate-limiting step. The red-cell isoform, PKR, is encoded by the PKLR gene on chromosome 1q21, together with the liver isoform PKL; more than 300 pathogenic PKLR variants are described, and pyruvate-kinase deficiency is an autosomal-recessive cause of chronic haemolytic anaemia through ATP depletion, red-cell dehydration, membrane damage and haemolysis, with accumulation of proximal intermediates including 2,3-bisphosphoglycerate (2,3-BPG), which right-shifts the haemoglobin–oxygen curve. PKR is a tetramer in equilibrium between a less-active T-state and a more-active R-state, induced by fructose-1,6-bisphosphate; allosteric activators stabilise the R-state. The therapeutic logic in thalassaemia and sickle-cell disease is twofold: activation raises ATP, improving membrane integrity and red-cell survival, and lowers 2,3-DPG, raising haemoglobin–oxygen affinity and reducing haemoglobin S polymerisation and sickling.

That logic is now clinically validated. Mitapivat (Pyrukynd, Agios) was approved by the FDA on 17 February 2022 for haemolytic anaemia in adults with pyruvate-kinase deficiency — the first disease-modifying therapy for the disorder — on the ACTIVATE trial (Al-Samkari et al., N Engl J Med 2022;386:1432–1442), where a haemoglobin response of at least 1.5 g/dL was achieved in 16 of 40 patients (40%) on mitapivat against 0 of 40 on placebo, and ACTIVATE-T, where 10 of 27 regularly transfused patients (37%) achieved at least a 33% transfusion-burden reduction and 6 of 27 (22%) became transfusion-free. In thalassaemia, the ENERGIZE Phase 3 trial (Musallam et al., Lancet 2025;406:33–42) randomised 194 adults with non-transfusion-dependent α- or β-thalassaemia 2:1 to mitapivat 100 mg twice daily or placebo: a haemoglobin response of at least 1.0 g/dL was achieved in 55 of 130 (42%) on mitapivat against 1 of 64 (2%) on placebo, with a mean haemoglobin rise of 0.96 g/dL against placebo. The ENERGIZE-T trial in transfusion-dependent thalassaemia reported a transfusion-reduction response in 30.4% on mitapivat against 12.6% on placebo (FDA and Agios summaries; the peer-reviewed publication was not located in this sweep). On that evidence the FDA approved mitapivat (Aqvesme) in December 2025 for anaemia in adults with α- or β-thalassaemia, transfusion-dependent and non-transfusion-dependent — the only approved medicine for anaemia in both — at 100 mg twice daily, with a boxed warning for hepatocellular injury (five patients in the ENERGIZE programme, two hospitalised) and a restricted REMS programme with liver monitoring. In sickle-cell disease, the RISE UP Phase 3 trial (Lancet 2026;408:1705–16) found a haemoglobin response in 56 of 138 (41%) on mitapivat against 2 of 69 (3%) on placebo, but the co-primary endpoint of annualised sickle-cell pain-crisis rate was not met (2.6 against 3.1 per year, p=0.1213); whether the FDA acted on the sickle-cell application by its 1 November 2026 target date was not verified in this sweep and is not claimed here.

The successors are close behind. Etavopivat (FT-4202, Novo Nordisk), a once-daily oral PKR activator, met both co-primary endpoints in the HIBISCUS Phase 2/3 trial in sickle-cell disease (topline April 2026): annualised vaso-occlusive crisis rate down 27% against placebo, median time to first crisis 38.4 against 20.9 weeks, and a haemoglobin rise above 1 g/dL at week 24 in 48.7% against 7.2% on placebo; a new-drug application was filed with the FDA and a marketing authorisation application with the EMA in November 2026, with decisions expected in 2027. Tebapivat (AG-946, Agios), a once-daily activator designed from the same allosteric pocket, showed haemoglobin responses of 43.8%, 47.1% and 29.4% at three doses against 33.3% on placebo in its Phase 2 sickle-cell trial — and Agios announced on 21 July 2026 that it will not advance tebapivat in sickle-cell disease, judging it undifferentiated against the other activators.

Pakistan is where this mechanism matters most. Beta-thalassaemia trait affects 5–8% of the population — more than 10 million carriers — about 5,000 children are born with β-thalassaemia major every year, and roughly 100,000 patients live with transfusion-dependent thalassaemia major, with no centralised national registry, so the headcounts are estimates. Comprehensive treatment costs about PKR 7.8 billion a year for roughly 60,000 registered patients (an older JPMA estimate), with blood transfusion about PKR 30,000 a year and iron chelation about PKR 150,000 a year per child. Consanguineous marriage, estimated at 60–70% in some surveys, is a major driver. Sickle-cell disease in Pakistan has no reliable national prevalence figure — only referral-laboratory frequencies exist — and it is concentrated in Lyari (Karachi) and parts of Khyber Pakhtunkhwa and Balochistan.

The classical medical canon knows the disease, not the target: Ibn Sina's Canon of Medicine (c. 1025) describes anaemia as a syndrome of pallor and weakness, but not pyruvate kinase. The principle carried forward here is hifz al-nafs, preservation of life (see §7): where a cheap oral activator can raise haemoglobin in a country with 100,000 transfusion-dependent patients, testing it properly is the obligation.

**Falsifiable question.** Do the newer PKR activators etavopivat and tebapivat bind the allosteric activator pocket of the mitapivat-bound structure (PDB 8XFD) at scores beyond re-docked mitapivat, and would that binding translate into stronger PKR activation? **Falsifier:** a PKR activation assay (EC50) under identical conditions showing etavopivat's EC50 more than 3-fold worse than mitapivat's, or a haemoglobin-response trial in which etavopivat fails to match mitapivat, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the approved drug re-docked on a co-crystal structure of its own target with its own bound ligand as the centre — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-24: the pyruvate-kinase-deficiency review (Grace et al., Trends Mol Med 2023;29:406–418); the ACTIVATE trial (Al-Samkari et al., N Engl J Med 2022;386:1432–1442; PMID 35417638; doi:10.1056/NEJMoa2116634); the ENERGIZE trial (Musallam et al., Lancet 2025;406:33–42; doi:10.1016/S0140-6736(25)00635-X); the RISE UP Phase 3 trial (Lancet 2026;408:1705–16); the FDA approval notices for Pyrukynd (2022) and Aqvesme (December 2025); the etavopivat HIBISCUS topline and November 2026 filings (Novo Nordisk); the tebapivat Phase 2 results and the July 2026 discontinuation announcement (Agios); the PKR structures 8XFD (Han et al., Crystals 2024; doi:10.3390/cryst14050441), 8TBT (Jin & Padyana, ChemMedChem 2024; PMID 38109501) and 2VGB; the thalassaemia burden in Pakistan (JPMA review); and the UniProtKB record for P30613. The ENERGIZE-T numbers rest on FDA and Agios summaries, not on a located peer-reviewed publication, and are labelled as such wherever they appear.

### 2.2 Target identification

The pipeline resolved the target correctly on the first run: UniProtKB P30613 (pyruvate kinase PKLR, Homo sapiens, EC 2.7.1.40) → ChEMBL lookup returned no target record (chembl_targets empty), so no ChEMBL ligands were retrieved and the similarity screen was skipped — stated, not hidden. The comparison set was therefore built from the literature: the three PKR activators with human data, with SMILES verified against PubChem by molecular formula (mitapivat C24H26N4O3S; etavopivat C22H23N3O6S; tebapivat C18H16N8OS).

### 2.3 Molecular docking

The three activators were docked on 8XFD, the 2.10 Å crystal structure of the human erythrocyte pyruvate-kinase tetramer in complex with mitapivat, using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: grid centre the centroid of the co-crystallised mitapivat (ligand WV2, 32 heavy atoms, chain B), [9.10, 11.33, 23.79], verified by direct computation from the PDB file with `dock._ligand_center` (the centre audit confirmed WV2 is the drug-like HETATM group; fructose-1,6-bisphosphate, 20 atoms, and the magnesium ions were correctly not picked); box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for all three compounds. Mitapivat is therefore the self-dock control on its own structure: a method that could not recover strong binding for the drug in its own pocket would be broken. Two technical notes, stated not smoothed over. First, the pipeline's first run docked mitapivat on 7FS3, the 1.66 Å structure of liver pyruvate kinase (PKL) in complex with "allosteric modulator 15" — the same PKLR gene, but the liver isoform, not the red-cell isoform this paper is about; that score (−12.02 kcal/mol) is retained only as a cross-isoform sensitivity check. Second, the receptor preparation for 8XFD required a documented fix: the PDB's charge annotation on ASP/GLU carboxylates breaks RDKit's sanitizer ("Explicit valence ... greater than permitted"), so columns 79–80 were blanked before parsing — coordinates and elements unchanged, standard sanitization then succeeds with proper aromaticity (768 aromatic carbons; the sanitize=False fallback perceives none and would mistype every aromatic receptor carbon in Vina). The fix is in `health-papers-agent/dock_lenient.py`.

### 2.4 PAINS screen

RDKit PAINS filter applied to all three activators. All three are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for mitapivat: molecular weight 450.56, logP 3.20, 1 hydrogen-bond donor, 5 acceptors, TPSA 82.61 Å², 6 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. The two comparators: etavopivat (MW 457.51, logP 0.77, HBD 1, HBA 7, TPSA 109.27 Å², 5 rotatable bonds, 0 violations) and tebapivat (MW 392.45, logP 1.68, HBD 2, HBA 7, TPSA 120.30 Å², 4 rotatable bonds, 0 violations). Unlike the antagonist classes in other papers in this series, all three activators are Lipinski-compliant and drug-like by the standard counts — so the docking differences in §3 cannot be dismissed as a size or lipophilicity artefact. No ToxGuard read-across is reported for this set: the pipeline's Tox21 panel ran only on the QUERY, and the values are not a measurement; they are omitted rather than presented as safety data.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published trial results. The three activators' measured potencies are clinical haemoglobin responses, not activation EC50s in a common assay, and their binding poses are not annotated anywhere — all three are PKR activators by pharmacology, but the pose is assumed, not shown. The structure used (8XFD) holds mitapivat, so the pocket is in the reference drug's own conformation, which favours mitapivat over the other two — a bias in the reference drug's favour, stated here.

## 3. Results

### 3.1 Docking: the comparison table (8XFD, 2.10 Å — the mitapivat-bound structure)

| Compound | Clinical status | Best affinity, 8XFD (kcal/mol) | Top-3 poses (kcal/mol) | Margin vs mitapivat |
|---|---|---|---|---|
| Etavopivat | Phase 2/3 met endpoints; NDA filed Nov 2026 | −11.15 | −11.15, −10.85, −10.11 | −0.09 |
| Mitapivat (reference) | Approved (PK deficiency 2022; thalassaemia Dec 2025) | −11.06 | −11.06, −10.97, −10.96 | — |
| Tebapivat (AG-946) | Phase 2; SCD programme stopped Jul 2026 | −8.32 | −8.32, −8.27, −8.21 | +2.74 |

Mitapivat re-docks at −11.06 kcal/mol on 8XFD, with the tightest pose consistency in the set (−11.06, −10.97, −10.96): the method recovers strong binding for the drug in its own pocket, so the protocol is not broken. Etavopivat scores −11.15 kcal/mol — ahead by 0.09 kcal/mol, a dead heat inside Vina noise, and its pose spread is wider (−11.15, −10.85, −10.11), so even the best pose is not a stable win. Tebapivat scores −8.32 kcal/mol, 2.74 kcal/mol behind mitapivat with tight poses (−8.32, −8.27, −8.21) — a gap larger than the noise, and therefore the one difference in the table that docking can actually claim. The honest reading is a dead heat between the two clinical-stage activators, with one real gap: the discontinued activator scores clearly worse.

### 3.2 Comparison with published data

No published Vina study of mitapivat, etavopivat or tebapivat on 8XFD was found in the sweep; the comparison here is internal (activators vs re-docked reference drug on the same structure, same protocol). The structural literature is the published ground truth for the binding mode: the 8XFD structure (Han et al. 2024) shows mitapivat in the allosteric activator pocket, 8TBT (Jin & Padyana 2024) shows an AG-946-series activator in the same pocket at 2.34 Å, and 2VGB shows the active R-state apo enzyme at 2.73 Å. The cross-isoform check is informative: the pipeline's mitapivat dock on 7FS3, the liver isoform with a different modulator, scored −12.02 kcal/mol — 0.96 kcal/mol better than the −11.06 kcal/mol on the erythrocyte structure. The same compound, the same protocol, two isoforms of the same gene: the score moves by almost a full kilocalorie. That is a direct measure of this method's structural sensitivity, and it is why the 0.09 kcal/mol gap between etavopivat and mitapivat cannot be read as a difference at all.

### 3.3 The clinical confounder that docking cannot see

Mitapivat's clinical record is the paper's most important context, and docking cannot see any of it. The drug raised haemoglobin by at least 1.0 g/dL in 42% of non-transfusion-dependent thalassaemia patients against 2% on placebo, and cut transfusion burden by at least half in 30.4% of transfusion-dependent patients against 12.6% — but it also carries a boxed warning for hepatocellular injury, with five cases in the ENERGIZE programme, two hospitalised, and a restricted REMS programme with liver monitoring. In sickle-cell disease it raised haemoglobin in 41% against 3% on placebo yet failed its pain-crisis endpoint (2.6 against 3.1 crises per year, p=0.1213) — a drug can fix the laboratory value and miss the outcome that matters to the patient. Etavopivat, by contrast, met both co-primary endpoints in HIBISCUS, including a 27% reduction in vaso-occlusive crises and a near-doubling of the median time to first crisis. A compound that out-scores mitapivat here by 0.09 kcal/mol but fails the crisis endpoint would be a worse drug for sickle-cell disease, and docking on a single erythrocyte structure cannot tell the two apart. The docking order cannot explain why the class raises haemoglobin reliably and prevents crises only sometimes; the trial data can.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since mitapivat was approved. Before approval, the question was "can a PKR activator raise haemoglobin?" — now it is "which activator, if any, beats mitapivat on activation and keeps its safety profile, including the liver?" The benchmark is therefore a screen with a two-part bar: beat −11.06 kcal/mol on 8XFD and show no hepatocellular-injury signal. This paper supplies the first half of the bar and shows the second half is where the pipeline must go next: etavopivat ties mitapivat on docking, tebapivat trails by more than noise, and the liver question was not docked at all.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 0.09 kcal/mol margin between etavopivat and mitapivat is one-tenth of Vina's noise, and smaller than the 0.96 kcal/mol by which the same compound's score moves between two isoforms of the same gene. Second, the pocket is in mitapivat's own conformation, which biases the comparison in the reference drug's favour — etavopivat tying mitapivat in mitapivat's pocket is interesting, but a tie in a biased pocket is still a tie. Third, the clinical record cuts against any docking-based ranking: etavopivat met its crisis endpoints where mitapivat did not, and tebapivat was stopped for lack of differentiation, not for lack of binding — the decisions that matter were made on trial data, not on scores.

### 4.3 The tebapivat gap is the experiment's design constraint, not a reason to stop

Tebapivat's −8.32 kcal/mol is the one gap in the table larger than the noise, and it agrees with the clinical decision to stop the programme — but agreement is not evidence. Tebapivat was designed against the same allosteric pocket (its series has its own structure, 8TBT), so docking it into the mitapivat-bound conformation of 8XFD may under-score it for a conformational reason, not a potency reason. The honest handling is to report the gap with the caveat attached, and to design the validation assay so the question is answered by the experiment: a PKR activation assay measures EC50 regardless of which crystal conformation the pocket was solved in, and a haemoglobin-response comparison measures the outcome that matters. A compound that scores poorly because the pocket was solved around its competitor is not a failure of the compound; it is a failure of the scoring setup, and the assay is what tells the two apart.

### 4.4 Mechanism

Mitapivat is an allosteric PKR activator: it binds the activator pocket at the subunit interface, stabilises the R-state tetramer, and so increases pyruvate-kinase activity, raising red-cell ATP and lowering 2,3-DPG. Test for each link: (i) a PKR activation assay (with mitapivat as the comparator) measures EC50 directly against the published haemoglobin responses; (ii) a red-cell ATP and 2,3-DPG assay in thalassaemic and sickle red cells measures whether the analogue reproduces the mechanism — a rise in ATP without a fall in 2,3-DPG would break the claimed mechanism; (iii) a haemolysis/sickling assay measures functional red-cell survival at matched concentration, with a cytotoxicity counter-screen.

### 4.5 Testable hypotheses

1. Etavopivat activates PKR with an EC50 within 3-fold of mitapivat in the same assay. Falsifier: EC50 > 3-fold worse than mitapivat.
2. Etavopivat raises red-cell ATP and lowers 2,3-DPG to the same extent as mitapivat at matched activation. Falsifier: ATP rise < 50% of mitapivat's at the same EC50 multiple.
3. Tebapivat's docking gap predicts its activation: tebapivat's EC50 is more than 10-fold worse than mitapivat's. Falsifier: EC50 within 3-fold of mitapivat's, which would show the docking gap was a conformational artefact.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): PKR activation assay for the three activators — etavopivat, mitapivat, tebapivat — on recombinant human PKR; readout EC50, n=3, with a known weak activator as a negative control. Stage 2 (weeks 4–8): red-cell ATP and 2,3-DPG assay in thalassaemic red cells for the best compound from stage 1 against mitapivat at matched EC50 multiples. Stage 3 (weeks 9–12): if any activator passes stages 1–2, a haemolysis and sickling assay in sickle red cells; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows the 0.09 kcal/mol gap between etavopivat and mitapivat.
2. The ranking cannot separate the two clinical-stage activators (0.09 kcal/mol apart), so the set cannot test ranking at the top — only the 2.74 kcal/mol gap to tebapivat exceeds noise.
3. The pocket is in mitapivat's own conformation, which biases the comparison in the reference drug's favour; tebapivat's series has its own structure (8TBT), which was not docked.
4. Mitapivat's own score moves by 0.96 kcal/mol between the erythrocyte structure (8XFD) and the liver-isoform structure (7FS3) — a direct measure of structural sensitivity that dwarfs the headline gap.
5. One rigid structure was used (8XFD, activator-bound, 2.10 Å); the R-state apo structure (2VGB) and the AG-946-bound structure (8TBT) were not docked.
6. No data on the clinical confounder: docking cannot distinguish the haemoglobin rise the class achieves from the hepatocellular-injury warning it carries, nor the crisis endpoint mitapivat missed and etavopivat met.
7. The ChEMBL ligand retrieval returned no data for this target, so the comparison set was built from the literature rather than from measured ChEMBL potencies; the three activators' potencies are clinical haemoglobin responses, not activation EC50s in a common assay.
8. The ENERGIZE-T numbers rest on FDA and Agios summaries, not on a located peer-reviewed publication.
9. The classical-canon sweep found no PKR-relevant text: the Canon of Medicine describes the anaemia syndrome, not the enzyme, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

Mitapivat, the PKR activator approved for pyruvate-kinase deficiency in 2022 and for thalassaemia anaemia in December 2025, re-docks at −11.06 kcal/mol on the 2.10 Å erythrocyte structure 8XFD with tight pose consistency and no PAINS alert — a validated control, not a discovery. Etavopivat scores −11.15 kcal/mol, ahead by 0.09 kcal/mol: a dead heat, not a win, and smaller than the 0.96 kcal/mol by which mitapivat's own score moves between two isoforms of the same gene. Tebapivat scores −8.32 kcal/mol, 2.74 kcal/mol behind — the one gap in the table larger than the noise, and it agrees with the decision to stop its sickle-cell programme, though agreement is not evidence. The docking verdict is a dead heat at the top with one real gap at the bottom, and it is useful precisely as one: the two clinical-stage activators cannot be separated by rigid Vina scoring on a single structure, the scores are sensitive to which structure is used, and the next screen must be an activation assay plus a red-cell ATP/2,3-DPG assay, not a bigger docking set. What the docking cannot do is resolve the safety split: the same pocket that binds mitapivat at −11.06 kcal/mol is the pocket whose activation carries a boxed warning for hepatocellular injury, and only a liver-monitoring assessment can tell whether a successor keeps the haemoglobin benefit without the liver cost. The next step is the cheap, decisive test — a PKR activation assay for the three activators against mitapivat — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the National Thalassaemia Programme, with the SMBBMU ORIC office as the local route. **Decision:** whether to evaluate mitapivat for Pakistan's thalassaemia population, and where the programme's limited money should go. **Exact change:** commission a cost-effectiveness and liver-monitoring assessment for mitapivat in transfusion-dependent thalassaemia — including the boxed hepatocellular-injury warning and the REMS liver-monitoring burden — instead of funding another computational screen of PKR activators; and, in parallel, fund carrier screening and prevention, which is the only intervention that reduces the 5,000 new thalassaemia-major births a year, rather than treating the 100,000 patients already dependent on transfusion. **If evidence Z appears, reverse this:** if the assessment shows mitapivat reduces transfusion burden by at least 30% at a cost the programme can bear, with liver injury manageable under monitoring, move to a procurement evaluation; if the liver signal or the price makes it unusable in Pakistan, drop the activator route and redirect the same money to transfusion and chelation capacity — do not proceed to any procurement on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable activator from an unaffordable or unsafe one for the country's largest inherited blood disorder, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the assessment", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Grace RF, et al. Updates and advances in pyruvate kinase deficiency. Trends Mol Med. 2023;29:406–418.
2. Al-Samkari H, et al. Mitapivat versus placebo for pyruvate kinase deficiency (ACTIVATE). N Engl J Med. 2022;386:1432–1442. PMID: 35417638. doi:10.1056/NEJMoa2116634.
3. Musallam KM, et al. Mitapivat in non-transfusion-dependent thalassaemia (ENERGIZE). Lancet. 2025;406:33–42. doi:10.1016/S0140-6736(25)00635-X.
4. Mitapivat in sickle-cell disease (RISE UP, phase 3). Lancet. 2026;408:1705–16.
5. Han C, et al. Crystal structure of pyruvate kinase tetramer in complex with mitapivat. Crystals. 2024. doi:10.3390/cryst14050441.
6. Jin Y, Padyana A, et al. Structure-based design of tebapivat (AG-946). ChemMedChem. 2024. PMID: 38109501.
7. U.S. Food and Drug Administration. FDA approves treatment for anemia in adults with pyruvate kinase deficiency (Pyrukynd). 17 February 2022.
8. U.S. Food and Drug Administration. FDA approves first oral treatment for anemia in thalassaemia (Aqvesme). December 2025.
9. Thalassaemia in Pakistan: burden and prevention. J Pak Med Assoc (review). https://archive.jpma.org.pk/article-details/10402. Accessed 2026-11-24.
10. RCSB PDB entry 8XFD: Crystal structure of pyruvate kinase tetramer in complex with allosteric activator, mitapivat, 2.10 Å. RCSB Protein Data Bank. Accessed 2026-11-24.
11. UniProtKB P30613: Pyruvate kinase PKLR, Homo sapiens. UniProt. Accessed 2026-11-24.
12. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; describes the anaemia syndrome — cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-146-2026-11-24-8XFD.json` (mitapivat + two PKR activators on 8XFD). The pipeline run is in `hidden_files/dock-HP-146-2026-11-24.json` (mitapivat −12.02 kcal/mol on 7FS3, the liver isoform — cross-isoform sensitivity check only; ChEMBL ligand retrieval returned no data). Reference drug mitapivat; comparators etavopivat, tebapivat (SMILES verified against PubChem by molecular formula). Structure: PDB 8XFD (2.10 Å). Target: UniProtKB P30613. No additional data were generated.
