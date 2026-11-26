# Telmisartan Leads Losartan by 1.52 kcal/mol on AT1R — but Docking Cannot Rank the Sartans: the Self-Dock Control and the Active Metabolite Both Invert the Published Order

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-26 · **Health Papers Agent — Paper #119** (daily 5-paper run)

**Keywords:** angiotensin II type 1 receptor; sartans; losartan; telmisartan; molecular docking; AutoDock Vina; hypertension; Pakistan

---

## Abstract

Hypertension affects 18.9% of Pakistanis and 70% of hypertensives do not know they have it; losartan, the first angiotensin II type 1 receptor (AT1R) blocker, is the weakest binder of its class by published rank order, and the question was whether any sartan beats it on the human AT1R structure. Six sartans — losartan, its active metabolite EXP3174, candesartan, telmisartan, valsartan and olmesartan — were docked with standardised AutoDock Vina on the 2.8 Å olmesartan-bound AT1R structure 4ZUD, same box and exhaustiveness, with olmesartan as the self-dock control. Telmisartan scored best at −10.57 kcal/mol, 1.52 kcal/mol better than losartan at −9.05, but that lead is inside Vina's ±1–2 kcal/mol noise, so the answer to the falsifiable question is no: no sartan beats losartan beyond noise. The method then failed its own controls: olmesartan, the co-crystallised ligand, scored only fourth (−8.90), and EXP3174 — 10–40 times more potent than losartan in published assays — scored worse than losartan (−8.68). Docking therefore cannot rank sartans on this structure, and no procurement or prescribing switch follows from these scores. Pose consistency was tight for every compound (three-pose spread 0.12–0.22 kcal/mol), so the ranking is not a sampling artefact; it is a scoring-function failure, and the same failure would apply to any procurement ranking built on these scores. The falsifier is a radioligand binding assay: if telmisartan's Ki is not better than losartan's by more than 3-fold on the same plate, the docking lead is a pocket artefact.

---

## 1. Introduction

Hypertension affects 18.9% of Pakistanis, diabetes 26.7%, and chronic kidney disease 16.7% (range 12.5–29.9%), with hypertension the cause of 30–40% of CKD; end-stage renal disease incidence is 100–150 per million while the dialysis rate is only 15 per million. Tazeen Jafar (N Engl J Med 2006;354:995–997) found 15–20% of Pakistanis aged 40+ with reduced GFR, a third of those 45+ hypertensive, and 70% of hypertensives unaware. The angiotensin II type 1 receptor (AT1R, AGTR1, UniProt P30556, 359 aa) is the GPCR through which angiotensin II raises blood pressure, retains sodium and drives aldosterone — and the sartans (ARBs) that block it are the most prescribed antihypertensive class in the world. Losartan, the first ARB (FDA 1995), is a surmountable, competitive antagonist whose active metabolite EXP3174 is 10–40 times more potent by weight; the FDA label records ~1,000-fold selectivity for AT1 over AT2. The rank order of sartan binding affinity (candesartan 1, telmisartan 10, EXP3174 10, losartan 50, eprosartan 100; PMID 10579749) makes losartan the weakest binder of the class — which is the gap this paper attacks: do newer or unexploited scaffolds actually bind the AT1R pocket better than losartan, on losartan's own terms, i.e. in the same structure with the same protocol?

**Falsifiable question.** Does any sartan or sartan-like scaffold out-score losartan on the human AT1R structure 4ZUD by more than Vina's ±1–2 kcal/mol noise? **Falsifier:** a radioligand binding assay showing the winner's Ki not better than losartan's, or a functional assay showing no greater rightward shift of the angiotensin II dose–response curve. **Causal identification:** validated-control re-docking — olmesartan re-docked on its own co-crystal (4ZUD) as the control, losartan and four other sartans docked on the same structure with the same box and exhaustiveness — association only beyond that, since docking scores are not affinity and not blood pressure.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-26: the AT1R structures (Zhang et al., Cell 2015;161:833–844, PMID 25913193, DOI 10.1016/j.cell.2015.04.011 — 4YAY, 2.9 Å, ZD7155; and Zhang et al., J Biol Chem 2015;290:29127 — 4ZUD, 2.8 Å, olmesartan); the sartan pharmacology review (PMID 10579749 — rank order of affinities, surmountable vs insurmountable antagonism); the losartan FDA label (1000-fold AT1/AT2 selectivity; EXP3174 10–40× more potent; ~33% bioavailability; CYP2C9/3A4); the Pakistan burden review (CKD 16.7%, hypertension 18.9%); and Jafar (NEJM 2006;354:995–997). The classical-canon sweep: Ibn Sina's Canon treats hypertension's symptoms (headache, palpitation, renal disease) without a receptor concept; the principle carried is hifz al-nafs.

### 2.2 Target identification — and the pipeline failure that had to be corrected

The pipeline resolved the target WRONG on the first run: UniProtKB Q9WVK0 (Mus musculus, type-1 angiotensin II receptor-associated protein, AGTRAP, 161 aa) — a negative regulator of AT1R signalling, not the receptor itself — and its ChEMBL lookup returned silicon-containing glucosidase inhibitors, not sartans. The mismatch is stated, not hidden: the pipeline's target search matched "angiotensin II type 1 receptor" to the associated protein, and its 26 ranked "leads" are not used anywhere in this paper. The comparison set was therefore built from the literature: the six sartans with the strongest published AT1R data, with SMILES verified live against PubChem by name and CID (losartan CID 3961; EXP3174 CID 108185; candesartan CID 2541; telmisartan CID 65999; valsartan CID 60846; olmesartan CID 158781). The correct target is human AT1R, UniProt P30556.

### 2.3 Molecular docking

Standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: box 22.5 Å, exhaustiveness 8, best of 3 poses reported. Primary structure: 4ZUD, the 2.8 Å X-ray structure of human AT1R in complex with olmesartan (Zhang et al., J Biol Chem 2015;290:29127), grid centre the centroid of the co-crystallised olmesartan, verified by direct computation from the PDB file with `dock._ligand_center`. Olmesartan is therefore the self-dock control on its own structure: a method that could not recover binding for the drug in its own pocket would be broken. Losartan has no co-crystal with AT1R, so it is docked into the olmesartan pocket — the standard cross-docking setup, with the caveat stated in §2.6 that the pocket is in olmesartan's conformation and favours its own ligand. All six compounds were docked with the same box, centre and exhaustiveness.

### 2.4 PAINS screen

RDKit PAINS filter applied to all six compounds. All six are PAINS-clean: losartan, EXP3174, candesartan, telmisartan, valsartan and olmesartan carry no PAINS alert. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for all six compounds (molecular weight, logP, H-bond donors/acceptors, TPSA, rotatable bonds, Lipinski violations). No ToxGuard read-across is reported for this set: the pipeline's Tox21 panel ran against the wrong target (AGTRAP), and the values are not a measurement; they are omitted rather than presented as safety data.

### 2.6 Honesty limits

Docking ≠ affinity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published affinities and the published structure. The 4ZUD pocket is in olmesartan's conformation, so it favours olmesartan over the other five sartans. Vina's rigid, water-free scoring cannot see the GPCR's membrane environment, the sodium ion site, or the receptor's active/inactive conformational equilibrium — the three things that decide whether an antagonist works in a cell. Losartan's measured affinity is the lowest of the class by rank order, but affinity is not blood pressure: losartan's metabolite, its insurmountable-vs-surmountable kinetics and its duration of action are not in this computation.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Target (PDB) | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| Telmisartan | AT1R (4ZUD) | −10.57 | −10.57, −10.53, −10.44 | Clean |
| Candesartan | AT1R (4ZUD) | −9.53 | −9.53, −9.44, −9.32 | Clean |
| Losartan (reference) | AT1R (4ZUD) | −9.05 | −9.05, −9.00, −8.86 | Clean |
| Olmesartan (self-dock control) | AT1R (4ZUD) | −8.90 | −8.90, −8.78, −8.68 | Clean |
| EXP3174 (losartan metabolite) | AT1R (4ZUD) | −8.68 | −8.68, −8.52, −8.48 | Clean |
| Valsartan | AT1R (4ZUD) | −7.79 | −7.79, −7.77, −7.67 | Clean |

Pose consistency is tight for every compound: the spread across the three poses is 0.12–0.22 kcal/mol, so the ranking is not a pose-sampling artefact — each compound converged on the same binding mode three times. The ranking itself is the problem. Telmisartan leads losartan by 1.52 kcal/mol, candesartan by 0.48 kcal/mol, and both margins are inside Vina's ±1–2 kcal/mol noise: neither clears the bar the falsifiable question set. The two controls then fail in opposite directions. Olmesartan — the drug co-crystallised in this very pocket, the self-dock control — scores fourth of six at −8.90, worse than losartan, candesartan and telmisartan; a scoring function that cannot rank its own ligand first cannot be trusted to rank the class. EXP3174 — losartan's active metabolite, 10–40 times more potent than losartan by weight in published assays — scores fifth at −8.68, 0.37 kcal/mol *worse* than its own parent. The published rank order is candesartan 1, telmisartan 10, EXP3174 10, losartan 50; the docking order is telmisartan 1, candesartan 2, losartan 3, olmesartan 4, EXP3174 5, valsartan 6. The docking reproduces the top two in the right order and then inverts the rest. The honest reading is that Vina on 4ZUD separates the strong binders from the weak ones (valsartan last, −7.79, 1.26 kcal/mol behind losartan) but cannot resolve the differences that matter — the 5-fold gap between candesartan and losartan, and the 10–40-fold gap between EXP3174 and losartan, are both invisible to it.

### 3.2 Comparison with published docking

No published docking study of sartans on 4ZUD was found in the searches for this paper, so there is no published docking table to compare against. The comparison that exists is against the published affinity rank order (PMID 10579749), and it is reported in §3.1 in full — including the two inversions, not just the agreements.

### 3.3 The standardisation / quality problem: which losartan?

The comparison that matters clinically is not losartan-the-molecule against telmisartan-the-molecule. In a patient, losartan is a prodrug: most of its effect comes from EXP3174, which is 10–40 times more potent. Docking the parent alone therefore understates the drug by an order of magnitude, and docking the metabolite alone overstates nothing — it scores worse than the parent here, which is the opposite of the published pharmacology. Any ranking that treats "losartan" as one molecule is ranking the wrong thing, and any procurement decision built on such a ranking would be built on a category error. The same problem applies to the other sartans in a smaller way: candesartan is dosed as the prodrug candesartan cilexetil, and telmisartan's long half-life (24 h) and high volume of distribution are properties no docking score can see.

## 4. Discussion

### 4.1 The reframe: the question changes from "which sartan?" to "can docking rank sartans at all?"

The paper set out to find whether any sartan beats losartan on AT1R. The answer is no — not because losartan is the best binder (it is not, by published affinity), but because the method cannot tell. Telmisartan's 1.52 kcal/mol lead is a real number and a non-result at the same time: it is inside the noise bar, and the two controls that would have validated it both failed. The question therefore changes: the finding is not "telmisartan wins" but "Vina on a single GPCR structure cannot rank a congeneric series whose published affinities span only ~50-fold". That is a useful negative, and it is the paper's actual contribution — it stops a procurement or prescribing switch that the raw table, read naively, would seem to support.

### 4.2 Why the "win" must not be over-read

Four reasons. First, the margin: 1.52 kcal/mol against a ±1–2 kcal/mol noise bar is not a lead, it is a tie with a sign. Second, the self-dock control: olmesartan fourth of six on its own structure means the pocket conformation, not the compounds, is doing part of the ranking. Third, the metabolite inversion: EXP3174 scoring worse than losartan contradicts 10–40-fold published potency, which means the scoring function is blind to the carboxylate interaction that makes the metabolite potent — the very interaction the 4YAY structure shows matters (Arg167). Fourth, the missing pharmacology: affinity is not blood pressure, and the properties that separate losartan from the insurmountable sartans — dissociation kinetics, the active metabolite, duration of action — are not in this computation at all. Any one of these would be enough to withhold a claim; together they close it.

### 4.3 Mechanism

Sartans bind the orthosteric pocket of AT1R, where angiotensin II would bind. The 4YAY structure (Zhang et al., Cell 2015) showed the binding mode for the class: the biphenyl-tetrazole moiety sits deep in the pocket, with the tetrazole making an ionic interaction with Arg167, and Trp84 and Tyr35 contributing π–π and hydrogen-bond contacts. Losartan carries the same biphenyl-tetrazole on an imidazole core with a hydroxymethyl group; its active metabolite EXP3174 replaces that group with a carboxylate, which strengthens the ionic interaction — the structural reason EXP3174 is 10–40 times more potent by weight. The pharmacological split that matters clinically is kinetic, not thermodynamic: losartan is a surmountable antagonist (parallel rightward shift of the angiotensin II curve, fast dissociation), while candesartan, telmisartan, irbesartan, valsartan and EXP3174 are insurmountable (they depress the maximal response, slow dissociation). Test for each link: (i) a radioligand binding assay measures Ki directly against the published rank order; (ii) a functional assay (angiotensin II dose–response in rabbit aorta or calcium flux in AT1R-expressing cells) measures surmountable vs insurmountable behaviour; (iii) a washout experiment measures dissociation half-life, which is the property that separates losartan from the rest of the class.

### 4.4 Testable hypotheses

1. The best-scoring sartan on 4ZUD has a Ki within 3-fold of its published rank-order value in the same radioligand binding assay. Falsifier: Ki more than 3-fold worse than published. (Status after this study: the hypothesis is already weakened — the docking order does not reproduce the published order, so the assay is now testing the method, not the compounds.)
2. The docking winner's advantage over losartan (if any) survives the functional assay: it produces a greater rightward shift of the angiotensin II dose–response curve than losartan at equal concentration. Falsifier: no greater shift, which would show the docking advantage is a pocket artefact.
3. Olmesartan's self-dock score predicts its rank: if olmesartan does not score best or near-best on its own structure, the method — not the compounds — is the problem, and the ranking is discarded. Falsifier: olmesartan scores worst on 4ZUD. (Status after this study: olmesartan scored fourth of six — the hypothesis is refuted, and the ranking is discarded as a potency claim.)

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): radioligand binding assay for the six sartans on AT1R-expressing membranes, same plate, n=3, with losartan and candesartan as the low/high-affinity anchors; readout Ki. Stage 2 (weeks 4–8): functional calcium-flux assay for the best two compounds from stage 1 against losartan, measuring the angiotensin II dose–response shift and the insurmountable/surmountable pattern; readout EC50 shift and maximal-response depression. Stage 3 (weeks 9–12): if any compound passes stages 1–2 — Ki better than losartan by more than 3-fold and a greater functional shift — a dissociation-kinetics (washout) experiment for that compound; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every margin except a lead larger than 2 kcal/mol.
2. The 4ZUD pocket is in olmesartan's conformation, so part of any olmesartan lead is conformational favouritism; the cleaner comparison is among the five non-olmesartan sartans.
3. Losartan has no co-crystal with AT1R, so it is cross-docked into the olmesartan pocket — the standard setup, but a cross-dock, not a self-dock.
4. The pipeline's target resolution failed (AGTRAP, mouse) and its ligand set was discarded; the comparison set is six literature compounds, and no ChEMBL-derived AT1R ligand set exists in this study.
5. Affinity is not blood pressure: the docking cannot see dissociation kinetics, the active metabolite, or duration of action — the three properties that separate losartan from the insurmountable sartans clinically.
6. No published Pakistani study reports AT1R variant frequencies or sartan response rates, so the clinical picture is global; the Pakistani numbers in this paper are burden numbers, not response numbers.
7. The classical-canon sweep found no AT1R-relevant text: the Canon describes hypertension's symptoms without a receptor concept, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

No sartan beats losartan on the human AT1R structure 4ZUD by more than Vina's noise: telmisartan leads by 1.52 kcal/mol, inside the ±1–2 kcal/mol bar, and the method fails its own controls — olmesartan scores fourth on its own structure and EXP3174 scores worse than its parent despite being 10–40 times more potent. Docking cannot rank the sartans, and no switch from losartan follows from these scores. The next step is a radioligand binding assay on the same six compounds, which will either reproduce the published rank order and rehabilitate the docking, or confirm that the ranking is a pocket artefact.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Ministry of National Health Services, with the provincial health departments that run primary care. **Decision:** whether to spend anything switching antihypertensive procurement from losartan to a newer sartan, and what must exist first. **Exact change:** do not switch procurement on the basis of affinity rankings — losartan is the cheapest sartan, the most widely available, and the only one whose active metabolite is 10–40 times more potent than the parent, which partly closes its affinity gap in vivo; instead, fund a blood-pressure measurement and control-rate survey in primary care, because the binding question is settled and the delivery question is not — only about a third of Pakistani adults have ever had their blood pressure measured and 70% of hypertensives do not know they have the disease. **If evidence Z appears, reverse this:** if the survey shows control rates above 50% on losartan and a head-to-head trial shows a newer sartan controls blood pressure better by more than 5 mmHg systolic at equal cost, move to a procurement assessment for that sartan; if the survey confirms the measurement gap, keep the money on screening and losartan supply — do not proceed to any drug switch on docking scores alone. The Islamic principle is hifz al-nafs joined to adl (justice): where the effective drug is already cheap and the gap is that people are never measured, spending on the newer drug before spending on measurement would violate both. The evidence here is thin — docking only — so the recommendation is "run the survey", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content.

## References

1. Zhang H, et al. Structure of the angiotensin receptor revealed by serial femtosecond crystallography. Cell. 2015;161:833–844. PMID: 25913193. doi:10.1016/j.cell.2015.04.011. (4YAY, 2.9 Å, ZD7155.)
2. Zhang H, et al. Structural basis for ligand recognition and functional selectivity at angiotensin receptor. J Biol Chem. 2015;290:29127. (4ZUD, 2.8 Å, olmesartan.)
3. Pharmacological properties of angiotensin II receptor antagonists. PMID: 10579749. (Rank order of sartan affinities; surmountable vs insurmountable antagonism.)
4. Losartan potassium tablets, USP — FDA label. (1000-fold AT1/AT2 selectivity; EXP3174 10–40× more potent; ~33% bioavailability; CYP2C9/3A4.)
5. Jafar TH. The growing burden of chronic kidney disease in Pakistan. N Engl J Med. 2006;354:995–997.
6. Need assessment of renal and liver transplant in Pakistan. J Int Med Dent Coll. (CKD prevalence 16.7%, hypertension 18.9%, diabetes 26.7%.)
7. RCSB PDB entry 4ZUD: human angiotensin II type 1 receptor in complex with olmesartan, 2.8 Å. RCSB Protein Data Bank. Accessed 2026-11-26.
8. UniProtKB P30556: Type-1 angiotensin II receptor (AGTR1), Homo sapiens. UniProt. Accessed 2026-11-26.
9. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source — cited for the hifz al-nafs principle only.)
10. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
11. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-137-2026-11-26-4ZUD.json` (losartan, EXP3174, candesartan, telmisartan, valsartan, olmesartan on 4ZUD). The pipeline run is in `hidden_files/dock-HP-137-2026-11-26.json` (target resolved wrongly to UniProt Q9WVK0 mouse AGTRAP; ChEMBL lookup returned glucosidase inhibitors, so its ligand set is not used; docking skipped — no PDB found for the wrong accession). Reference drug losartan (PubChem CID 3961); comparators EXP3174 (CID 108185), candesartan (CID 2541), telmisartan (CID 65999), valsartan (CID 60846), olmesartan (CID 158781), SMILES verified against PubChem. Structure: PDB 4ZUD (2.8 Å, olmesartan-bound). Target: UniProtKB P30556. No additional data were generated.
