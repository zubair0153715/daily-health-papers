# Ambrisentan Scores Worst at −7.37 kcal/mol on the ET-1-Bound ETA Structure 8HCQ — and the Inversion Proves Antagonists Cannot Be Ranked on an Agonist-Bound Structure

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-24 · **Health Papers Agent — Paper #108** (daily 5-paper run)

**Keywords:** endothelin receptor type A; ETA antagonist; ambrisentan; pulmonary arterial hypertension; molecular docking; bosentan; macitentan; Pakistan

---

## Abstract

Pulmonary arterial hypertension affects about 25 people per million and is fatal without treatment, yet no endothelin-receptor antagonist has ever been co-crystallised with its target — the first endothelin receptor type A (ETA) structures, solved by cryo-electron microscopy in 2023, hold the agonist endothelin-1, not an antagonist. We asked whether the established endothelin-receptor antagonists bosentan, macitentan, sitaxentan and zibotentan occupy the ETA pocket more strongly than ambrisentan, the most ETA-selective drug in the class. Using the LeadForge pipeline (UniProtKB P25101 → PubChem/RDKit, PAINS and ADMET screen → AutoDock Vina 1.2.7), we docked the five antagonists on 8HCQ, the 3.0 Å cryo-EM structure of ETA bound to endothelin-1, centred on the endothelin-1 residues that occupy the pocket (centre audit via dock._ligand_center). Ambrisentan scored −7.37 kcal/mol — worst in the set. Bosentan scored best at −8.72 kcal/mol, followed by sitaxentan at −8.46, zibotentan at −8.34 and macitentan at −7.57 kcal/mol. The honest limit: the structure is in the active, endothelin-1-bound conformation, so these are pocket-occupancy numbers on an agonist-bound receptor, not antagonist potencies — and the ranking inverts the clinical one, since ambrisentan is the most ETA-selective drug in the set (ETA:ETB about 4,000:1) while the top scorer, bosentan, is the least selective, a dual antagonist. The falsifiable next step is a radioligand binding comparison (Ki) for ETA under identical conditions: if bosentan's Ki is not better than ambrisentan's, the pocket-occupancy ranking is refuted — and the decisive test is an antagonist-bound ETA structure, which does not yet exist.

---

## 1. Introduction

Pulmonary arterial hypertension (PAH) is a progressive disease of the small pulmonary arteries — vasoconstriction, smooth-muscle proliferation and vascular remodelling that raise pulmonary vascular resistance until the right ventricle fails. Its prevalence is about 25 per million people, and the Global Burden of Disease 2021 study estimates 2.28 cases per 100,000 population. No Pakistan-specific PAH epidemiology was found in this sweep; the burden numbers above are global, and the absence of local data is itself part of the policy question in §7.

Endothelin-1 (ET-1) is a 21-amino-acid peptide and one of the most potent vasoconstrictors known. It acts through two G-protein-coupled receptors: ETA, on vascular smooth muscle, which mediates vasoconstriction and proliferation, and ETB, on endothelium, which mediates vasodilatation through nitric oxide and clears ET-1 from the circulation. In PAH, ET-1 is overexpressed, and blocking its receptors lowers pulmonary vascular resistance. The endothelin-receptor antagonists (ERAs) are one of the three pillars of PAH therapy, alongside phosphodiesterase-5 inhibitors and prostacyclins.

The reference drug of this paper is ambrisentan (Letairis, Gilead), approved by the FDA on 15 June 2007 for PAH. It is the most ETA-selective antagonist in the class, with an ETA:ETB selectivity of about 4,000:1. In the ARIES-1 and ARIES-2 trials (Galiè et al., Circulation 2008;117:3010–3019; PMID 18506008), ambrisentan improved six-minute walk distance by 31 and 51 metres at 5 and 10 mg (ARIES-1) and by 32 and 59 metres at 2.5 and 5 mg (ARIES-2) against placebo. Its liver warning was removed in 2011 after more than 7,800 patient-years of exposure without a hepatotoxicity signal, and its risk-evaluation programme was removed in April 2025 (verify at submission — the date rests on the sweep's check). The comparators span the class's history. Bosentan (Tracleer, Actelion) was the first ERA, approved in 2001, a dual ETA/ETB antagonist that requires monthly liver monitoring. Macitentan (Opsumit, Actelion) is a dual antagonist with improved tissue penetration; in the SERAPHIN trial (Pulido et al., N Engl J Med 2013;369:809–820; PMID 23984728) it reduced the composite of morbidity and mortality by 45% (hazard ratio 0.55). Sitaxentan (Thelin, Pfizer), a selective ETA antagonist, was withdrawn worldwide in 2010 after fatal hepatotoxicity. Zibotentan (AstraZeneca) is a highly selective ETA antagonist that was never approved, studied in cancer and in systemic sclerosis digital ulcers.

The structural gap is the paper's premise. No ETA–antagonist crystal structure exists: the structures sometimes cited for the class, 5XPR and 5GLH, are endothelin receptor type B, not ETA. The first ETA structures were solved by cryo-electron microscopy in 2023 (Ji et al., Nat Commun 2023;14:1268): 8HCQ at 3.0 Å and 8HCX at 3.5 Å, both of ETA bound to endothelin-1 in complex with Gq — the active, agonist-bound conformation. Every docking study of an ETA antagonist therefore has a choice: dock into an agonist-bound pocket, or not dock at all. This paper docks, and says plainly what the numbers are.

The classical medical canon knows the disease, not the target: Ibn Sina's Canon of Medicine (c. 1025) describes breathlessness and heart failure as syndromes, but not the endothelin receptor. The principle carried forward here is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do the established endothelin-receptor antagonists bosentan, macitentan, sitaxentan and zibotentan occupy the ETA pocket of the endothelin-1-bound structure (PDB 8HCQ) at scores beyond ambrisentan, and would that occupancy translate into stronger ETA antagonism? **Falsifier:** a radioligand binding assay for ETA under identical conditions showing bosentan's Ki no better than ambrisentan's, or an antagonist-bound ETA structure (when solved) giving a different rank order, refutes the claim for that compound. **Causal identification:** validated-control re-docking is not available here — there is no antagonist-bound structure to validate against — so the identification is weaker than in the other papers in this series, and the paper says so: this is pocket-occupancy on an agonist-bound structure, association only, not a potency comparison.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-24: the first ETA structures (Ji et al., Nat Commun 2023;14:1268); the ARIES-1/2 trials (Galiè et al., Circulation 2008;117:3010–3019; PMID 18506008); the SERAPHIN trial (Pulido et al., N Engl J Med 2013;369:809–820; PMID 23984728); the FDA approval of ambrisentan (15 June 2007) and the removal of its liver warning (2011) and risk-evaluation programme (April 2025); the sitaxentan withdrawal (2010); the bosentan approval (2001); the PAH burden estimates (Global Burden of Disease 2021); and the UniProtKB record for P25101. No Pakistan-specific PAH epidemiology was found.

### 2.2 Target identification

The pipeline resolved the target correctly on the first run: UniProtKB P25101 (endothelin receptor type A, Homo sapiens) → ChEMBL lookup returned no target record (chembl_targets empty), so no ChEMBL ligands were retrieved and the similarity screen was skipped — stated, not hidden. No PDB structure was found by the pipeline at all (no_pdb_found), so docking was skipped in the pipeline run and the comparison set was built from the literature: the five ERAs with the strongest published data, with SMILES verified against PubChem by molecular formula (ambrisentan C22H22N2O4; bosentan C27H29N5O6S; macitentan C19H20Br2N6O4S; sitaxentan C18H15ClN2O6S2; zibotentan C19H16N6O4S).

### 2.3 Molecular docking

The five antagonists were docked on 8HCQ, the 3.0 Å cryo-EM structure of human ETA in complex with endothelin-1 and Gq, using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: grid centre the centroid of endothelin-1 residues 16–21, the residues that occupy the orthosteric pocket, [122.27, 115.66, 128.27], verified by direct computation from the PDB file with `dock._ligand_center`; box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for all five compounds. Two technical notes, stated not smoothed over. First, the receptor preparation required a documented fix: the PDB's charge annotation on ASP/GLU carboxylates breaks RDKit's sanitizer ("Explicit valence ... greater than permitted"), so columns 79–80 were blanked before parsing — coordinates and elements unchanged, standard sanitization then succeeds with proper aromaticity (845 aromatic carbons; the sanitize=False fallback perceives none and would mistype every aromatic receptor carbon in Vina). The fix is in `health-papers-agent/dock_lenient.py`. Second, the `_prep_receptor` step keeps all ATOM records, so the endothelin-1 peptide chain L (171 ATOM lines) was stripped from the cached 8HCQ.pdb before docking — it would otherwise block the pocket — and the original PDB was restored afterwards; the derived 8HCQ_rec.pdbqt in the cache is intentionally the chain-L-stripped receptor, and any future 8HCQ dock must use the stripped receptor, never the endothelin-1-occupied one. The G-protein chains (A/B/G) and the scFv (chain E) remain; they are far from the 22.5 Å box and harmless. There is no self-dock control in this paper, because no antagonist is co-crystallised with ETA: ambrisentan is the reference drug, not a validated control, and the paper's identification is weaker for it.

### 2.4 PAINS screen

RDKit PAINS filter applied to all five antagonists. All five are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for ambrisentan: molecular weight 378.43, logP 3.52, 1 hydrogen-bond donor, 5 acceptors, TPSA 81.54 Å², 7 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass — the smallest and most drug-like compound in the set. The four comparators: bosentan (MW 551.63, logP 4.20, HBD 2, HBA 10, TPSA 145.65 Å², 10 rotatable bonds, 1 violation), sitaxentan (MW 454.91, logP 3.96, HBD 1, HBA 8, TPSA 107.73 Å², 6 rotatable bonds, 0 violations), zibotentan (MW 424.44, logP 2.71, HBD 1, HBA 9, TPSA 132.99 Å², 6 rotatable bonds, 0 violations) and macitentan (MW 588.28, logP 3.57, HBD 2, HBA 8, TPSA 128.22 Å², 11 rotatable bonds, 1 violation). The largest compound in the set, macitentan, does not score best — it sits fourth — so the size bias is visible but not total. No ToxGuard read-across is reported for this set: the pipeline's Tox21 panel ran only on the QUERY, and the values are not a measurement; they are omitted rather than presented as safety data.

### 2.6 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published trial results. The five antagonists' measured potencies are clinical walk-distance and event outcomes, not binding Ki values in a common assay, and their binding poses are not annotated anywhere — all five are ERAs by pharmacology, but the pose is assumed, not shown. The structure used (8HCQ) holds endothelin-1, the agonist, in the active conformation, so the pocket is in the agonist-bound state, not the antagonist-bound state — the scores are pocket-occupancy numbers, and the reference drug's low score may reflect a poor fit to the active conformation rather than weak antagonism.

## 3. Results

### 3.1 Docking: the comparison table (8HCQ, 3.0 Å — the endothelin-1-bound structure)

| Compound | Clinical status | Best affinity, 8HCQ (kcal/mol) | Top-3 poses (kcal/mol) | Margin vs ambrisentan |
|---|---|---|---|---|
| Bosentan | Approved 2001; dual ETA/ETB; monthly liver monitoring | −8.72 | −8.72, −8.54, −8.43 | −1.35 |
| Sitaxentan | Withdrawn 2010 (fatal hepatotoxicity) | −8.46 | −8.46, −8.40, −8.05 | −1.09 |
| Zibotentan | Never approved; highly selective ETA antagonist | −8.34 | −8.34, −8.16, −7.97 | −0.97 |
| Macitentan | Approved; SERAPHIN 45% morbidity–mortality reduction | −7.57 | −7.57, −7.54, −7.47 | −0.20 |
| Ambrisentan (reference) | Approved 2007; most ETA-selective (4,000:1) | −7.37 | −7.37, −7.36, −7.36 | — |

Ambrisentan scores −7.37 kcal/mol on 8HCQ — worst in the set, with perfectly consistent poses (−7.37, −7.36, −7.36), so the low score is stable, not a sampling failure. Bosentan scores best at −8.72 kcal/mol, 1.35 kcal/mol ahead of the reference drug — the only gap in the table larger than Vina's noise, apart from sitaxentan's 1.09 kcal/mol gap. Macitentan sits fourth at −7.57 kcal/mol, only 0.20 kcal/mol ahead of ambrisentan. The honest reading is an inversion: the ranking on this structure is the reverse of the clinical ranking by ETA selectivity, and the drug with the best clinical selectivity scores worst.

### 3.2 Comparison with published data

No published Vina study of these antagonists on 8HCQ was found in the sweep; the comparison here is internal (antagonists vs reference drug on the same structure, same protocol). The structural literature is the published ground truth for the binding mode: the 8HCQ structure (Ji et al. 2023) shows endothelin-1 occupying the orthosteric pocket in the active conformation, and the structures sometimes cited for the class, 5XPR and 5GLH, are ETB, not ETA — they were not used. The published potency order is the reverse of the docking order: ambrisentan's ETA:ETB selectivity is about 4,000:1, zibotentan is highly selective, sitaxentan was selective, macitentan is dual, and bosentan is dual — yet the docking order is bosentan, sitaxentan, zibotentan, macitentan, ambrisentan. A scoring function that ranks the least selective drug first and the most selective drug last, on an agonist-bound structure, is measuring pocket occupancy in the active conformation, not antagonist potency. The decisive published fact is not a potency number but a structural one: no antagonist-bound ETA structure exists, so no docking study of this class can be validated against a co-crystal.

### 3.3 The clinical confounder that docking cannot see

Ambrisentan's clinical record is the paper's most important context, and docking cannot see any of it. The drug improved six-minute walk distance by up to 59 metres, had its liver warning removed after more than 7,800 patient-years without a hepatotoxicity signal, and had its risk-evaluation programme removed in 2025 — the cleanest liver record in the class. Sitaxentan, the second-best scorer here, was withdrawn worldwide in 2010 for fatal hepatotoxicity. Bosentan, the best scorer, requires monthly liver monitoring. A compound that out-scores ambrisentan here by 1.35 kcal/mol but carries a hepatotoxicity risk would be a worse drug, and docking cannot tell the two apart. The docking order cannot explain why the class's most selective drug has the cleanest liver record while its second-best scorer was withdrawn for liver failure; the trial data and the pharmacovigilance record can.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since the first ETA structures were solved. Before 2023, the question was "can we dock ERAs at all?" — now it is "what does docking into an agonist-bound structure actually measure?" The benchmark is therefore a screen with a two-part bar: occupy the pocket on 8HCQ and show a binding Ki that matches the occupancy. This paper supplies the first half of the bar and shows the second half is where the pipeline must go next: the occupancy ranking inverts the clinical ranking, and the class's defining problem is liver safety, not pocket occupancy.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the structure is agonist-bound, so every score in §3.1 is a pocket-occupancy number on the active conformation, not an antagonist potency — and the reference drug's low score may be a property of the conformation, not of the drug. Second, the ranking inverts the clinical selectivity order (bosentan first, ambrisentan last), which is the opposite of what a potency ranking should look like — a scoring function that inverts the known order on the only available structure cannot be trusted to rank this family. Third, the two gaps larger than noise (bosentan's 1.35 and sitaxentan's 1.09 kcal/mol) both belong to drugs with liver liabilities, while the cleanest drug in the class scores worst — the scores correlate with the liability, not with the benefit, which is the worst possible direction for a screening tool.

### 4.3 The inversion is the experiment's design constraint, not a reason to stop

The five antagonists were chosen by clinical history, not by pipeline rank, and the largest of them (macitentan, MW 588.28) does not score best — it sits fourth — so the size bias is visible but not total in this set. The honest handling is to report the scores with the caveat attached, and to design the validation assay so the inversion is answered by the experiment: a radioligand binding assay measures Ki regardless of which conformation the receptor was solved in, and a hepatocyte toxicity assay measures the liability docking cannot see. A compound that scores well because it fits the active conformation is not a failure of the compound; it is a failure of the scoring setup, and the assay is what tells the two apart.

### 4.4 Mechanism

Ambrisentan is a selective ETA antagonist: it occupies the orthosteric pocket of ETA, blocks endothelin-1 binding, and so reduces smooth-muscle vasoconstriction and proliferation, lowering pulmonary vascular resistance. Test for each link: (i) a radioligand binding assay (with ambrisentan as the comparator) measures Ki directly against the published selectivity; (ii) a smooth-muscle contraction assay measures functional vasodilatation — a fall in contraction without a fall in binding would break the claimed mechanism; (iii) a hepatocyte toxicity assay measures whether the analogue reproduces the class's liver liability — a rise in ALT release is the likeliest way a "better" antagonist becomes a worse drug, because hepatotoxicity is the liability that withdrew one member of this class.

### 4.5 Testable hypotheses

1. Bosentan binds ETA with a Ki no better than ambrisentan in the same radioligand assay. Falsifier: Ki more than 3-fold better than ambrisentan, which would show the docking ranking was real.
2. Ambrisentan's ETA:ETB selectivity (about 4,000:1) is preserved in the same assay. Falsifier: selectivity below 100:1, which would show the published selectivity does not reproduce.
3. The 8HCQ pose predicts the safety profile: an antagonist whose docked pose makes the same deep-pocket contacts as bosentan carries the same liver liability as bosentan. Falsifier: an antagonist with those contacts shows no hepatocyte toxicity signal.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): radioligand binding assay for the five antagonists — ambrisentan, bosentan, macitentan, sitaxentan, zibotentan — on recombinant human ETA and ETB; readout Ki and selectivity ratio, n=3, with a known weak binder as a negative control. Stage 2 (weeks 4–8): smooth-muscle contraction assay for the best compound from stage 1 against ambrisentan at matched Ki multiples. Stage 3 (weeks 9–12): if any antagonist passes stages 1–2 — Ki within 3-fold of ambrisentan and selectivity above 100:1 — a hepatocyte toxicity assay; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows the 0.97 and 0.20 kcal/mol gaps, though not the 1.35 and 1.09 kcal/mol gaps.
2. The ranking inverts the clinical selectivity order, so the set cannot be used to rank antagonists — the scores are pocket-occupancy numbers on an agonist-bound structure.
3. There is no self-dock control in this paper, because no antagonist is co-crystallised with ETA; the identification is weaker than in the other papers in this series.
4. The structure used (8HCQ) holds endothelin-1, the agonist, in the active conformation at 3.0 Å cryo-EM resolution — the pocket is in the agonist-bound state, and the lower resolution (against the 1.87–2.10 Å crystal structures in this series) adds coordinate uncertainty.
5. One rigid structure was used (8HCQ); the other ETA structure (8HCX, 3.5 Å) was not docked, and no antagonist-bound ETA structure exists.
6. No data on the clinical confounder: docking cannot distinguish the haemodynamic benefit the class achieves from the hepatotoxicity that withdrew one member of it.
7. The ChEMBL ligand retrieval returned no data for this target, and the pipeline found no PDB structure at all, so the comparison set and the structure were both chosen from the literature rather than from the pipeline.
8. No Pakistan-specific PAH epidemiology was found; the burden numbers are global, and the absence of local data is a limitation of the policy section, not of the docking.
9. The classical-canon sweep found no ETA-relevant text: the Canon of Medicine describes breathlessness and heart failure as syndromes, not the receptor, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

Ambrisentan, the most ETA-selective antagonist in the class (ETA:ETB about 4,000:1) and the one with the cleanest liver record, scores worst at −7.37 kcal/mol on the 3.0 Å endothelin-1-bound ETA structure 8HCQ with no PAINS alert — a pocket-occupancy number, not a potency, and not a discovery. Bosentan scores best at −8.72 kcal/mol, followed by sitaxentan at −8.46, zibotentan at −8.34 and macitentan at −7.57 kcal/mol. The docking verdict is an inversion, and it is useful precisely as one: antagonists cannot be ranked by rigid Vina scoring on an agonist-bound structure, the ranking reverses the clinical selectivity order, and the next screen must be a radioligand binding assay plus a hepatocyte toxicity assay, not a bigger docking set. What the docking cannot do is resolve the safety split: the same pocket that binds ambrisentan at −7.37 kcal/mol is the pocket whose blockade lowers pulmonary vascular resistance, and only a binding assay and a liver assay can tell whether a successor keeps the haemodynamic benefit without the liver cost. The next step is the cheap, decisive test — a radioligand binding assay for the five antagonists against ambrisentan — not another docking run.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the National Pulmonary Hypertension Programme, with the SMBBMU ORIC office as the local route. **Decision:** whether to spend anything on endothelin-receptor antagonists in Pakistan, and what must exist first. **Exact change:** do not fund any ERA procurement or evaluation — no ERA is cheap, the class's liver liabilities need monitoring capacity Pakistan's PAH services may not have, and there is no Pakistan-specific PAH epidemiology, so the patients who could benefit cannot even be counted. Instead, fund a PAH registry and echocardiography screening in high-risk groups (connective-tissue disease, congenital heart disease, chronic lung disease), so the 25-per-million population is counted before any targeted drug is discussed; and, in parallel, ask the programme to note explicitly that the binding question is unsettled for this pocket — ambrisentan scores −7.37 kcal/mol on the only available ETA structure, and no antagonist-bound structure exists — and that the remaining gap is a structure, not a drug. **If evidence Z appears, reverse this:** if a PAH registry identifies a cohort and an antagonist-bound ETA structure is solved showing a candidate with a binding Ki better than ambrisentan and no liver signal, move to a drug-evaluation assessment for that candidate; if the registry shows PAH is rarer in Pakistan than the global 25 per million, drop the ERA route and redirect the same money to the pulmonary conditions Pakistan's patients actually carry — do not proceed to any drug evaluation on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable antagonist from an unusable one for a fatal disease, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Ji Y, et al. Cryo-EM structures of the endothelin receptor type A. Nat Commun. 2023;14:1268.
2. Galiè N, et al. Ambrisentan for the treatment of pulmonary arterial hypertension (ARIES-1 and ARIES-2). Circulation. 2008;117:3010–3019. PMID: 18506008.
3. Pulido T, et al. Macitentan and morbidity and mortality in pulmonary arterial hypertension (SERAPHIN). N Engl J Med. 2013;369:809–820. PMID: 23984728.
4. European Medicines Agency. Thelin (sitaxentan) — withdrawal of the marketing authorisation. 2010.
5. U.S. Food and Drug Administration. FDA approves ambrisentan (Letairis) for pulmonary arterial hypertension. 15 June 2007.
6. RCSB PDB entry 8HCQ: Cryo-EM structure of the endothelin receptor type A in complex with endothelin-1 and Gq, 3.0 Å. RCSB Protein Data Bank. Accessed 2026-11-24.
7. UniProtKB P25101: Endothelin receptor type A, Homo sapiens. UniProt. Accessed 2026-11-24.
8. Global Burden of Disease 2021. Pulmonary arterial hypertension prevalence. 2021.
9. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; describes breathlessness and heart failure as syndromes — cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-140-2026-11-24-8HCQ.json` (ambrisentan + four ERAs on 8HCQ). The pipeline run is in `hidden_files/dock-HP-140-2026-11-24.json` (no PDB structure found — docking skipped; ChEMBL ligand retrieval returned no data). Reference drug ambrisentan; comparators bosentan, macitentan, sitaxentan, zibotentan (SMILES verified against PubChem by molecular formula). Structure: PDB 8HCQ (3.0 Å cryo-EM). Target: UniProtKB P25101. No additional data were generated.
