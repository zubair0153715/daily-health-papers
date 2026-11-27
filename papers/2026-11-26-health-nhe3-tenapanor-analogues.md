# Small Tenapanor Analogues Match Its NHE3 Potency at 2–4 nM — but Only Tenapanor's 1,145 Da Dimer Is Built Not to Be Absorbed

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-26 · **Health Papers Agent — Paper #118** (daily 5-paper run)

**Keywords:** NHE3; tenapanor; SLC9A3; gut-restricted inhibitor; chronic kidney disease; hypertension; sodium absorption; ChEMBL; Pakistan

---

## Abstract

Intestinal NHE3 (SLC9A3) absorbs most dietary sodium, and blocking it in the gut lowers sodium load without touching the kidney — the rationale for tenapanor, a gut-restricted NHE3 inhibitor approved for IBS-C in 2019 and for hyperphosphataemia in dialysis in 2023. We asked whether any published NHE3 inhibitor beats tenapanor on potency while keeping its gut restriction. Using the LeadForge pipeline (UniProtKB P48764 → ChEMBL → PubChem/RDKit, PAINS and ADMET screen), we compared tenapanor against the most potent measured NHE3 inhibitors in ChEMBL. The two most potent records (IC50 0.5 nM) share tenapanor's exact molecular formula (C50H66Cl4N8O10S2) and dimeric tetrahydroisoquinoline scaffold and differ only in stereochemical annotation — they are tenapanor or its stereoisomer, not new compounds — so the apparent 10-fold gain over tenapanor's published 5 nM is a record artefact, not a discovery. The genuinely distinct analogues (CHEMBL3967635, 2.0 nM; CHEMBL3978001 and CHEMBL3946835, 4.0 nM) are single-ring fragments of 455–499 Da with zero Lipinski violations: as potent as tenapanor, but small and absorbable — the opposite of the design goal. No inhibitor-bound human NHE3 structure exists (the only structure, 7X2U, is an autoinhibited apo complex), so docking was skipped rather than invented. The falsifiable next step is a head-to-head NHE3 deacidification assay of tenapanor against CHEMBL3967635 with parallel Caco-2 permeability: if the analogue is not both within 3-fold of tenapanor's potency and at least 10-fold more permeable, the gut-restriction argument fails.

---

## 1. Introduction

Sodium is the cheapest drug target in medicine and the hardest to dose: the kidney reabsorbs almost all of it, and every systemic drug that touches sodium handling touches blood pressure, potassium and volume at the same time. NHE3 (sodium/hydrogen exchanger 3, SLC9A3, UniProt P48764, 834 amino acids) is the apical Na+/H+ antiporter of the intestinal epithelium and the renal proximal tubule, exchanging one extracellular Na+ for one intracellular H+ and accounting for the majority of Na+ absorbed in both organs. In the gut it is the dominant absorptive transporter; in the kidney it is the dominant reabsorptive one — which is why inhibiting it systemically is dangerous and inhibiting it only in the gut is attractive. Tenapanor was built for exactly that split: a dimeric tetrahydroisoquinoline (THIQ) NHE3 inhibitor of 1,145 Da, deliberately too large, too polar (TPSA 218 Å²) and too flexible (29 rotatable bonds) to cross the intestinal wall, so it blocks sodium uptake where food is and never reaches the kidney. The FDA approved it for irritable bowel syndrome with constipation in September 2019 (Ibsrela) and for hyperphosphataemia in dialysis patients in October 2023 (Xphozah) — the phosphate effect coming not from phosphate binding but from tightened paracellular junctions when sodium absorption falls. In healthy volunteers it cut urinary sodium by 20–50 mmol/day with a matching rise in stool sodium, and plasma concentrations were below 0.5 ng/mL in over 95% of samples.

The burden that makes this a Pakistani question is measured, not guessed: hypertension affects 18.9% of Pakistanis, diabetes 26.7%, and chronic kidney disease 16.7% (range 12.5–29.9% across studies), with diabetic nephropathy (40–50%) and hypertension (30–40%) the leading causes; end-stage renal disease incidence is 100–150 per million population while the dialysis rate is only 15 per million — a treatment gap, not a knowledge gap. Tazeen Jafar's 2006 NEJM analysis found 15–20% of Pakistanis aged 40 or older with reduced glomerular filtration rate, a third of those 45 or older hypertensive, and 70% of hypertensives unaware of their condition. A drug that removes sodium in the gut, without a prescription that reaches the kidney, is exactly the kind of intervention a system with that gap can use — if it is real, and if it is affordable.

**Falsifiable question.** Does any published NHE3 inhibitor beat tenapanor's potency (5 nM, human NHE3) while keeping tenapanor's gut restriction (no systemic absorption)? **Falsifier:** a head-to-head deacidification assay in which a comparator is both more potent than tenapanor by more than 3-fold and no more permeable in Caco-2 — or, conversely, a comparator that matches tenapanor's potency and is shown to be gut-restricted in vivo, which would refute the claim that tenapanor's dimer is uniquely suited. **Causal identification:** validated-control comparison of measured ChEMBL potencies against tenapanor's published potency, with the physicochemical determinants of absorption (molecular weight, TPSA, Lipinski count) as the mechanism test — association only beyond that, since no docking was possible and no new experiment was run.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-26: the tenapanor discovery letter (ACS Med Chem Lett 2022;13:1043, doi:10.1021/acsmedchemlett.2c00037); the cardiorenal proof-of-concept (Spencer et al., Sci Transl Med 2014;6:227ra36, PMID 24622516); the phosphate mechanism paper (King et al., Sci Transl Med 2018;10:eaam6474, PMID 30158152); the NHE3 polymorphism potency study (Am J Physiol Gastrointest Liver Physiol 2017, doi:10.1152/ajpgi.00044.2017); the first-in-human pharmacodynamics trials (Clin Drug Investig 2017, doi:10.1007/s40261-017-0614-0); the human NHE3–CHP1 structure (Dong et al., Sci Adv 2022; PDB 7X2U, 3.20 Å cryo-EM); the Pakistan CKD/hypertension burden review (J Int Med Dent Coll, CKD prevalence 16.7%); and Jafar (N Engl J Med 2006;354:995–997). The classical-canon sweep is in §4.3: Ibn Sina's Canon of Medicine discusses diseases of the kidneys and bladder and the balance of fluids, and Al-Razi's Kitab al-Hawi records clinical observation of dropsy and renal disease — neither describes an exchanger or an inhibitor, so the Islamic-principle discussion rests on hifz al-nafs and la darar (no harm), not on a classical source about this target.

### 2.2 Target identification — and the pipeline result

The pipeline resolved the target correctly on the first run: UniProtKB P48764 (SLC9A3, Homo sapiens, 834 aa) → ChEMBL lookup returned 26 ranked leads, all from the tenapanor THIQ series, with measured human NHE3 IC50s from 0.5 to 5.0 nM. The QUERY compound (tenapanor) verified against PubChem (CID 71587953, C50H66Cl4N8O10S2, MW 1,145.07, logP 6.16, 6 H-bond donors, 12 acceptors, TPSA 218.0 Å², 29 rotatable bonds, 4 Lipinski violations). Two pipeline steps deserve stating, not hiding. First, the auto-picker found no PDB to dock on (see §2.3). Second, the two most potent ChEMBL records (CHEMBL3973684 and CHEMBL3304485, both IC50 0.5 nM) carry tenapanor's exact molecular formula and the same dimeric scaffold; RDKit canonicalisation shows they differ from the PubChem tenapanor record only in stereochemical annotation at the THIQ centres. They are tenapanor or its stereoisomer under different ChEMBL records — not independent compounds — and the paper treats them as such in §3.2. The genuinely distinct comparators are the single-THIQ fragments CHEMBL3967635, CHEMBL3978001 and CHEMBL3946835.

### 2.3 Molecular docking — skipped, and why

No docking was run, deliberately. The only experimental human NHE3 structure is 7X2U (Dong et al., Sci Adv 2022): a cryo-EM structure of the NHE3–CHP1 complex in the **autoinhibited** state at 3.20 Å, with no inhibitor bound and no resolved ligand site. There is no tenapanor-bound structure, no S3226-bound structure, and no published inhibitor-binding site on NHE3; the transporter's ion-translocation pathway is described, but tenapanor's binding site on it is not resolved. Docking tenapanor into 7X2U would mean inventing a grid centre — either the centroid of an autoinhibitory domain that tenapanor does not bind, or a guessed pocket — and reporting a Vina score for it would be fake precision. The protocol for this paper series is explicit: if no experimental structure exists that anchors the docking, docking is skipped and the paper says so. That is what happened here. The comparison therefore rests on measured potencies and physicochemistry, not on scores.

### 2.4 PAINS screen

RDKit PAINS filter applied to tenapanor and all five comparators in Table 1. All are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and physicochemistry

RDKit descriptors computed for every compound in Table 1 (molecular weight, logP, H-bond donors/acceptors, TPSA, rotatable bonds, Lipinski violations). The gut-restriction argument is a physicochemistry argument, so the descriptors are the data, not decoration: tenapanor's MW 1,145, TPSA 218 Å² and 4 Lipinski violations are the properties that keep it in the lumen, and the published human pharmacokinetics (plasma below 0.5 ng/mL in >95% of samples) are the measurement that confirms the design worked. No ToxGuard read-across is reported for this set: the pipeline's Tox21 panel ran a kNN read-across against tenapanor's nearest neighbours at maximum similarity 0.29, which is too low to report as safety data, so it is omitted rather than presented.

### 2.6 Honesty limits

No docking was run, so there is no structure-based ranking in this paper at all. The ChEMBL IC50s are compared across records, not within one experiment: the retrieved data do not carry a single common assay identifier, so the 2.0–4.0 nM figures for the fragments and the 5 nM published figure for tenapanor come from the same assay family (the cell deacidification assay in opossum kidney cells overexpressing human NHE3) but not necessarily the same run, and tenapanor's own potency varies by assay — 0.87 nM (NHE3-799R variant), 2.41 nM (799C variant), 5 nM (human NHE3), 9–13 nM (human ileum/duodenum monolayers). A 2-fold difference between two ChEMBL records is therefore inside assay noise, and only the 10-fold apparent gap (0.5 vs 5 nM) looked real before the duplicate-record correction — and that gap is the artefact §3.2 removes. No experimental data exist in this study beyond the retrieved potencies and descriptors.

## 3. Results

### 3.1 The measured-potency table

| Compound | ChEMBL ID | Measured IC50 (human NHE3) | MW (Da) | logP | TPSA (Å²) | Rot. bonds | Lipinski violations | PAINS |
|---|---|---|---|---|---|---|---|---|
| Tenapanor (reference) | — (PubChem CID 71587953) | 5 nM (published) | 1,145.07 | 6.16 | 218.0 | 29 | 4 | clean |
| CHEMBL3973684 | CHEMBL3973684 | 0.5 nM | 1,145.07 | 6.16 | 218.0 | 29 | 4 | clean |
| CHEMBL3304485 | CHEMBL3304485 | 0.5012 nM | 1,145.07 | 6.16 | 218.0 | 29 | 4 | clean |
| CHEMBL3967635 | CHEMBL3967635 | 2.0 nM | 489.85 | 4.39 | 58.64 | 4 | 0 | clean |
| CHEMBL3978001 | CHEMBL3978001 | 4.0 nM | 499.46 | 3.49 | 78.87 | 7 | 0 | clean |
| CHEMBL3946835 | CHEMBL3946835 | 4.0 nM | 455.41 | 3.86 | 72.63 | 4 | 0 | clean |

All six compounds are PAINS-clean. The table is the whole result: the two most potent records are tenapanor itself (§3.2), and the three genuinely distinct analogues are 2–4 nM — the same potency band as tenapanor once assay variation is counted.

### 3.2 The duplicate-record correction

CHEMBL3973684 and CHEMBL3304485 report IC50s of 0.5 and 0.5012 nM — an apparent 10-fold improvement over tenapanor's published 5 nM. They are not an improvement. Both carry tenapanor's exact molecular formula C50H66Cl4N8O10S2, identical RDKit descriptors to the last decimal (MW 1,145.07, logP 6.16, TPSA 218.0, 29 rotatable bonds, 4 Lipinski violations), and isomeric SMILES that differ from the PubChem tenapanor record only in the stereochemical annotation of the THIQ centres — one is annotated (S,S), the other (R,S) at the second centre. ChEMBL holds the same dimeric molecule under more than one record, with different reported potencies (0.5 nM here against 5 nM in the published programme data), which is exactly the assay-to-assay spread the literature already shows for tenapanor itself (0.87–13 nM across recombinant, variant and monolayer assays). The honest reading is that tenapanor's potency is ~0.5–5 nM depending on the assay, and no record in ChEMBL beats the top of that range with a different molecule. A paper that reported "a 0.5 nM lead beats tenapanor 10-fold" without checking the structures would be reporting a database artefact as a discovery; the check took one RDKit comparison and it is stated here, not buried.

### 3.3 The gut-restriction comparison — the real result

The three distinct analogues are single-THIQ fragments: one THIQ head group with a sulfonamide tail, 455–499 Da, TPSA 59–79 Å², 4–7 rotatable bonds, zero Lipinski violations. They are, by every standard count, better drugs than tenapanor: smaller, more drug-like, and as potent (2–4 nM vs 5 nM). And they are the wrong optimisation for this target. Tenapanor's starting hit (compound 1 in the discovery letter) was exactly such a molecule — MW 371, pIC50 6.2 human, and 98% orally bioavailable in rats — and the programme spent its effort destroying that bioavailability: adding polarity, H-bond donors and acceptors, rotatable bonds and finally dimerising, until plasma exposure fell to Cmax 6 ng/mL at 9.4 mg/kg while potency was kept (pIC50 7.1 human for the dimer). The fragments in Table 1 are the hit, rediscovered: potent, and — by their size and TPSA — absorbable. An absorbable NHE3 inhibitor reaches the renal proximal tubule, where NHE3 does the majority of sodium reabsorption, and the consequence is the dysregulation of Na+–water homeostasis and blood pressure that the discovery programme explicitly designed tenapanor to avoid. The reframe is therefore the opposite of the usual lead-optimisation story: for NHE3, the winning property is not potency (already sufficient at 5 nM) but non-absorption, and tenapanor's 4 Lipinski violations are the feature, not the flaw. The memorable number is the plasma concentration: below 0.5 ng/mL in over 95% of human samples — a drug that works by not being there.

### 3.4 Comparison with published docking

There is no published docking of tenapanor or any inhibitor on human NHE3, because there is no inhibitor-bound structure to dock into. The only structure, 7X2U, is an autoinhibited apo complex. This paper's lack of a docking table is therefore not a gap against the literature; it is the same position the literature is in.

## 4. Discussion

### 4.1 The reframe

The question "what beats tenapanor?" has two answers, and they point in opposite directions. On potency alone, nothing in ChEMBL beats it with a different molecule: the 0.5 nM records are tenapanor, and the 2–4 nM fragments match it within assay noise. On the property that actually matters — staying in the gut — tenapanor is the only compound in the set that was designed for it, and the fragments fail it by construction. The field's usual optimisation (smaller, more drug-like, more potent) is exactly wrong here, and the discovery letter is unusually honest about that: it reports the hit's 98% bioavailability as a problem to be solved, not a property to be kept.

### 4.2 Why the "win" must not be over-read

Two corrections guard the headline. First, the 0.5 nM records are not a win at all (§3.2). Second, the 2–4 nM fragments are not a win either, because their potency is measured in the same recombinant assay that gives tenapanor 0.87–5 nM — the fragments sit inside tenapanor's own assay spread, so "2.0 nM beats 5 nM" is a 2.5-fold difference between different experiments, not a measured advantage. The only comparison that would settle it is a head-to-head run of all four compounds in one assay on one day (§4.5), and it has not been done. What is solid is the physicochemistry: the fragments are 455–499 Da with TPSA under 80 Å², and molecules of that size and polarity are absorbed; tenapanor at 1,145 Da and TPSA 218 Å² is not, and the human data confirm it.

### 4.3 Mechanism — and the classical canon

Tenapanor blocks NHE3 on the apical membrane of the intestinal epithelium, so sodium stays in the lumen, water follows it, stool softens and frequency rises (IBS-C), and — the mechanism that matters for kidney disease — reduced sodium absorption tightens the paracellular junctions, so dietary phosphate is trapped in the lumen and leaves in the stool (hyperphosphataemia). In salt-fed nephrectomised rats the same gut-only blockade reduced extracellular fluid volume, left ventricular hypertrophy, albuminuria and blood pressure. Test for each link: (i) the deacidification assay measures NHE3 inhibition directly against the published 5 nM; (ii) a Caco-2 permeability assay measures whether a fragment is absorbed, against tenapanor's near-zero permeability; (iii) urinary sodium excretion in a rat model measures the in-vivo consequence, against the published 20–50 mmol/day reduction in humans. The classical canon knows the disease, not the exchanger: Ibn Sina's Canon of Medicine (c. 1025) treats diseases of the kidneys and bladder and the balance of the body's fluids at length, and Al-Razi's Kitab al-Hawi (c. 900) records clinical observation of dropsy and renal disease — but neither describes a sodium transporter, so the principle carried forward is hifz al-nafs (preservation of life, a maqsad of the Sharia defined by Al-Ghazali in Al-Mustasfa and systematised by Al-Shatibi in Al-Muwafaqat) joined to la darar (no harm): a drug designed to stay out of the body is harm-avoidance by construction, and for a disease where the treatment gap is access, the harm to avoid is a potent drug that reaches the kidney it was never meant to touch.

### 4.4 Testable hypotheses

1. CHEMBL3967635 inhibits human NHE3 with an IC50 within 3-fold of tenapanor's in the same deacidification assay on the same day. Falsifier: IC50 more than 3-fold worse than tenapanor's in that run.
2. CHEMBL3967635 is at least 10-fold more permeable than tenapanor in Caco-2 monolayers (Papp). Falsifier: permeability within 3-fold of tenapanor's — which would make the fragment, not tenapanor, the better lead.
3. In a rat model, tenapanor reduces urinary sodium excretion dose-dependently while CHEMBL3967635 at an equi-potent dose does not change stool sodium without also appearing in plasma. Falsifier: the fragment produces the same stool-sodium effect with no detectable plasma exposure, which would show gut restriction does not require the dimer.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): head-to-head NHE3 deacidification assay — tenapanor, CHEMBL3967635, CHEMBL3978001, CHEMBL3946835 — in opossum kidney cells overexpressing human NHE3, same plate, n=3, with the published 5 nM tenapanor value as the control; readout IC50. Stage 2 (weeks 4–6): Caco-2 permeability for the same four compounds, with atenolol (low) and propranolol (high) as permeability controls; readout Papp. Stage 3 (weeks 7–12): if any fragment passes stages 1–2 — potency within 3-fold of tenapanor and permeability within 3-fold of tenapanor — a rat urinary-sodium study for that compound against tenapanor; if none passes, publish the negative result with the ChEMBL table as the reason the hypothesis failed. No animal work is proposed before stages 1–2 pass.

## 5. Limitations

1. No docking was run; there is no structure-based ranking in this paper, because no inhibitor-bound human NHE3 structure exists.
2. The ChEMBL IC50s are compared across records, not within one experiment; tenapanor's own potency spans 0.87–13 nM across assays, so any 2–3-fold difference between records is inside assay noise.
3. The duplicate-record correction (§3.2) rests on RDKit canonicalisation and formula identity; the two 0.5 nM records could be a defined stereoisomer of tenapanor rather than tenapanor itself — either way they are not a new scaffold, but the exact stereochemical assignment was not resolved here.
4. Gut restriction for the fragments is inferred from physicochemistry (MW, TPSA, Lipinski count), not measured: no permeability data exist for CHEMBL3967635, CHEMBL3978001 or CHEMBL3946835, and small polar molecules are sometimes poorly absorbed for other reasons.
5. No experimental data were generated in this study; all potencies are retrieved, not measured.
6. The Pakistani burden numbers are national estimates; no Pakistani study reports NHE3 variant frequencies (notably the 799C/R polymorphism, which changes tenapanor's IC50 3-fold) or tenapanor availability, so the policy section recommends measurement, not a drug decision.
7. The classical-canon sweep found no NHE3-relevant text: the Canon and Kitab al-Hawi describe renal disease as syndromes, not the exchanger, so the Islamic-principle discussion rests on hifz al-nafs and la darar as principles, not on a classical source about this target. The full 23 volumes of Kitab al-Hawi exist in English only in selections, and were not read in full.

## 6. Conclusion

Tenapanor inhibits human NHE3 at 5 nM and is the only compound in the set designed to stay in the gut — 1,145 Da, TPSA 218 Å², 4 Lipinski violations, plasma below 0.5 ng/mL in over 95% of human samples. The most potent ChEMBL records (0.5 nM) are tenapanor itself under duplicate records, and the genuinely distinct analogues (2–4 nM) are small, absorbable fragments that match its potency and fail its design goal. The lead is therefore not a more potent molecule but the property tenapanor already has: for NHE3, non-absorption is the drug. The next step is the cheap, decisive test — one head-to-head assay plus one permeability assay — not a bigger potency screen.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Ministry of National Health Services, with the Pakistan Kidney and Liver Institute and the National Institute of Health as the technical arms. **Decision:** whether to spend anything on an NHE3 programme for CKD and hypertension, and what must exist first. **Exact change:** do not pursue or import a tenapanor-class drug on potency alone — the ChEMBL data show no molecule beats tenapanor, and the small analogues that match it would be absorbed and reach the kidney; instead, fund two measurements first: (i) a national urinary-sodium and dietary-sodium survey in CKD clinics, so the sodium load tenapanor would remove is measured rather than assumed; and (ii) NHE3 genotyping (notably the 799C/R polymorphism, which changes tenapanor's IC50 3-fold) in Pakistani CKD patients, so the target's local variation is known before any drug evaluation. **If evidence Z appears, reverse this:** if the survey shows a high-sodium CKD population and genotyping shows the sensitive 799R variant predominant, move to a drug-evaluation assessment for a gut-restricted NHE3 inhibitor; if genotyping shows the less sensitive variant predominant, or if permeability data show the small analogues are in fact gut-restricted, re-open the lead list on that evidence — do not proceed to any drug evaluation on retrieved potencies alone. The Islamic principle is hifz al-nafs joined to la darar (no harm): where a measurement can distinguish a drug that stays in the gut from one that reaches the kidney, running the measurement is the obligation; prescribing a potent, absorbable NHE3 inhibitor to a population where 70% of hypertensives do not know they have the disease would violate it. The evidence here is thin — retrieved potencies only, no docking, no experiment — so the recommendation is "run the measurements", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and pipeline computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Spencer AG, et al. Intestinal inhibition of the Na+/H+ exchanger 3 prevents cardiorenal damage in rats and inhibits Na+ uptake in humans. Sci Transl Med. 2014;6(227):227ra36. doi:10.1126/scitranslmed.3007790. PMID: 24622516.
2. King AJ, et al. Inhibition of sodium/hydrogen exchanger 3 in the gastrointestinal tract by tenapanor reduces paracellular phosphate permeability. Sci Transl Med. 2018;10(456):eaam6474. doi:10.1126/scitranslmed.aam6474. PMID: 30158152.
3. Discovery of tenapanor: a first-in-class minimally systemic inhibitor of intestinal Na+/H+ exchanger isoform 3. ACS Med Chem Lett. 2022;13(7):1043. doi:10.1021/acsmedchemlett.2c00037.
4. Dong Y, et al. Structure of a human NHE3-CHP1 complex in the autoinhibited state. Sci Adv. 2022. (PDB 7X2U, 3.20 Å cryo-EM.)
5. A common NHE3 single-nucleotide polymorphism has normal function and sensitivity to regulatory ligands. Am J Physiol Gastrointest Liver Physiol. 2017. doi:10.1152/ajpgi.00044.2017. (Tenapanor IC50 0.87 ± 0.34 nM for NHE3-799R, 2.41 ± 0.69 nM for NHE3-799C.)
6. Pharmacodynamics, safety, and tolerability of the NHE3 inhibitor tenapanor: two trials in healthy volunteers. Clin Drug Investig. 2017. doi:10.1007/s40261-017-0614-0.
7. Jafar TH. The growing burden of chronic kidney disease in Pakistan. N Engl J Med. 2006;354:995–997.
8. Need assessment of renal and liver transplant in Pakistan. J Int Med Dent Coll. (CKD prevalence 16.7%, hypertension 18.9%, diabetes 26.7%; ESRD incidence 100–150 per million; dialysis rate 15 per million.)
9. RCSB PDB entry 7X2U: structure of a human NHE3-CHP1 complex in the autoinhibited state, 3.20 Å. RCSB Protein Data Bank. Accessed 2026-11-26.
10. UniProtKB P48764: Sodium/hydrogen exchanger 3 (SLC9A3), Homo sapiens. UniProt. Accessed 2026-11-26.
11. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; diseases of the kidneys and bladder and the balance of fluids — cited for the hifz al-nafs principle only.)
12. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
13. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)

## Data availability

All potencies and descriptors reported here are in `hidden_files/dock-HP-148-2026-11-26.json` (LeadForge pipeline run: target UniProt P48764; 26 ranked leads; ChEMBL IC50s as retrieved). Reference drug tenapanor (PubChem CID 71587953, C50H66Cl4N8O10S2); comparators CHEMBL3973684, CHEMBL3304485, CHEMBL3967635, CHEMBL3978001, CHEMBL3946835, with SMILES and descriptors in the same file. Structure: PDB 7X2U (3.20 Å cryo-EM, autoinhibited, no ligand site — docking skipped). Target: UniProtKB P48764. No additional data were generated.
