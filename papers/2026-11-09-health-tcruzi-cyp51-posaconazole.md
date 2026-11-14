# Posaconazole Still Leads, and the Most Potent Measured Inhibitor Scores Worst: A Vina Benchmark of Trypanosoma cruzi CYP51 Inhibitors on 4C27 That Fails to Reproduce the Potency Order

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-09 · **Health Papers Agent — Paper HP-025** (daily 5-paper run)

**Keywords:** Trypanosoma cruzi; CYP51; Chagas disease; posaconazole; albaconazole; sterol 14alpha-demethylase; molecular docking; AutoDock Vina

---

## Abstract

Chagas disease affects an estimated 6–7 million people, and the only approved drugs, benznidazole and nifurtimox, cure poorly in the chronic stage. Posaconazole, a sterol 14α-demethylase (CYP51) inhibitor, looked like the answer until the CHAGASAZOL trial showed 81–92% of posaconazole-treated patients PCR-positive for Trypanosoma cruzi DNA at follow-up, versus 38% on benznidazole — so the target, not just the drug, is in question. We ran the LeadForge pipeline live on 9 November 2026 (UniProtKB Q7Z1V1 → ChEMBL CHEMBL1075110, 56 ligands → RDKit → PAINS/ADMET → AutoDock Vina 1.2.7 on PDB 4C27, 1.95 Å, grid centred exactly on the co-crystallised inhibitor, 0.00 Å from its centroid). Posaconazole re-docked at −10.57 kcal/mol and no lead beat it: the best challenger, CHEMBL5189694 (measured Kd 24 nM), scored −9.40, 1.17 kcal/mol worse — inside Vina's ±1–2 kcal/mol noise. The striking failure is albaconazole (CHEMBL298817): the most potent measured inhibitor in the set (IC50 1.0 nM against T. cruzi CYP51) but the worst docking score, −8.16, 2.41 kcal/mol behind posaconazole. Across the four compounds with measured values, docking rank and potency rank correlate at Spearman ρ = −0.2. The falsifiable next step is a head-to-head recombinant TcCYP51 inhibition assay of albaconazole, posaconazole and CHEMBL5189694 under identical conditions, with MM-GBSA rescoring to test whether the ranking failure is a scoring artefact.

---

## 1. Introduction

Chagas disease (American trypanosomiasis), caused by the protozoan parasite *Trypanosoma cruzi*, infects an estimated 6–7 million people worldwide, mostly in Latin America, causes more than 10,000 deaths every year, and puts more than 100 million people at risk across 21 endemic continental Latin American countries (World Health Organization, 2024). About 20–30% of infected people develop chronic disease — progressive cardiomyopathy and/or gastrointestinal dysfunction — after an indeterminate stage that can last years or decades. There is no vaccine, and the only approved drugs, benznidazole and nifurtimox, have low cure rates in the chronic stage and considerable toxicity.

Sterol 14α-demethylase (CYP51) is the most studied alternative target. *T. cruzi* depends on endogenous sterol biosynthesis for membrane formation, and CYP51 catalyses the oxidative removal of the 14α-methyl group from the sterol core — the same step azole antifungals block in fungi. The case for the target looked strong: the antifungal triazole posaconazole showed trypanocidal activity in murine models, and the crystal structure of *T. cruzi* CYP51 in complex with posaconazole (PDB 3K1O, 2.89 Å) showed the drug coordinated to the haem iron in the active site (Lepesheva et al., 2010). On that basis posaconazole entered clinical trials for chronic Chagas disease.

The CHAGASAZOL trial ended that optimism. In a prospective randomised trial of 78 adults with chronic *T. cruzi* infection, posaconazole 400 mg twice daily, posaconazole 100 mg twice daily, and benznidazole 150 mg twice daily were given for 60 days, with parasite DNA monitored by real-time PCR during treatment and 10 months after (Molina et al., 2014). During treatment almost every patient tested PCR-negative. At follow-up, 92% of the low-dose posaconazole group and 81% of the high-dose group tested PCR-positive, versus 38% of the benznidazole group (intention-to-treat; per-protocol 90% and 80% versus 6%). Posaconazole showed antitrypanosomal activity but failed significantly more often than benznidazole. The question this paper asks is therefore sharper than "find a better CYP51 inhibitor": it is whether docking on the CYP51 structure can even rank known inhibitors correctly — because if it cannot reproduce the potency order of compounds whose measured values are already known, it cannot be trusted to prioritise new ones.

The structural literature gives the target a second chance. The same group that solved the posaconazole complex also solved *T. cruzi* CYP51 with fluconazole (PDB 3KHM) and with the experimental inhibitor VNF, and identified the VNI/VNF carboxamide scaffold as selective for trypanosomal CYP51 — it does not inhibit the human ortholog (selectivity index > 200), kills more than 99% of *T. cruzi* amastigotes at 1 µM, and shows low general cytotoxicity (Lepesheva et al., 2007). VNI has been reported to cure both acute and chronic Chagas disease in mice (cited in Friggeri et al., 2014). A later β-phenylimidazole series reached EC50 values of 1.0–5.5 nM against *T. cruzi* amastigotes, with two distinct binding modes that exploit the substrate-access channel entrance and the haem-propionate ceiling of the cavity (Friggeri et al., 2014). And an N-indolyl-oxopyridinyl series, crystallised in PDB 4C27, suppressed ≥99.8% parasitaemia in mice at 25 mg/kg twice daily for 4 days (Vieira et al., 2014). The target is therefore not dead — but the clinical failure of its best-known drug means any computational ranking must first prove it can reproduce known potencies.

The falsifiable hypothesis of this paper is that AutoDock Vina docking on the high-resolution *T. cruzi* CYP51 structure 4C27 ranks known CYP51 inhibitors in the same order as their measured potencies. The paper tests that hypothesis against the measured ChEMBL values, against Vina's own noise floor, and against the internal reproducibility of docking the same molecule twice — and reports where the hypothesis fails as carefully as where it holds.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 9 November 2026: the daily literature digest at `~/workspace/research-team/digests/2026-11-09.md`, PubMed, ChEMBL (EBI), UniProtKB, PubChem and RCSB PDB. Key sources: WHO (2024) for the disease burden; Molina et al. (2014) for the CHAGASAZOL result; Lepesheva et al. (2010) for the posaconazole/fluconazole/VNF co-crystal structures; Chen et al. (2010) for the fluconazole-bound structures 2WUZ/2WX2; Lepesheva et al. (2007) for the VNI/VNF selective scaffold; Lepesheva (2011) for the target review; Friggeri et al. (2014) for the β-phenylimidazole series and the VNI mouse-cure report; Vieira et al. (2014) for the 4C27 structure and the N-indolyl-oxopyridinyl series. Every citation in this paper was verified against its publisher or database record on the day of writing; no citation was generated from memory.

### 2.2 Molecular docking

The LeadForge pipeline was run live on 9 November 2026 with the reference drug posaconazole as the query: UniProtKB target identification (Q7Z1V1, sterol 14-alpha demethylase, *Trypanosoma cruzi* strain CL Brener, gene CYP51) → ChEMBL target CHEMBL1075110, 56 bioactivities retrieved → PubChem verification of the query → RDKit Morgan-fingerprint similarity screen (25 compounds) → RDKit ADMET/PAINS panel plus ToxGuard Tox21 kNN read-across (12 assays) → composite ranking → AutoDock Vina 1.2.7 docking. A data-quality note: several of the 56 retrieved ChEMBL ligands contain aluminium and failed RDKit sanitisation (explicit-valence warnings in the run log); they were excluded by the screen and none is in the docked set.

Docking used PDB 4C27 (1.95 Å), the *T. cruzi* CYP51 structure co-crystallised with the N-indolyl-oxopyridinyl inhibitor 26N (Vieira et al., 2014), auto-picked by the pipeline as the highest-resolution inhibitor-bound structure. The grid (22.5 Å box, exhaustiveness 8, best of 3 poses) was centred on the co-crystallised inhibitor. Centre audit, performed after the run from the PDB file itself: the docking centre [−10.75, −39.85, −23.88] is exactly the centroid of the chain-B 26N inhibitor (0.00 Å apart; the 92-atom entry is the two alternate conformations of the 46-atom ligand), while the chain-B haem centroid is 9.9 Å away — the grid is on the inhibitor site, not on the haem. The reference drug posaconazole was docked twice by the pipeline (once as the QUERY, once as its ChEMBL record CHEMBL1397), which gives an internal reproducibility check. Measured potencies quoted below are the values recorded in ChEMBL for target CHEMBL1075110, as returned by the pipeline's `known_activity` field; note that they mix Kd and IC50 values, which are not interchangeable, so the rank comparison is indicative, not a formal correlation.

Two deliberate limitations of the structure choice are stated here, not buried: (i) 4C27 is bound to the 26N inhibitor, not to posaconazole — the posaconazole-bound structure 3K1O exists but at lower resolution (2.89 Å), so posaconazole was re-docked into a site shaped by a different ligand; (ii) Vina treats the haem iron as a fixed point charge and cannot model the coordinate bond between an azole nitrogen and the Fe(II/III) centre, which is the dominant interaction for every azole in this set.

### 2.3 PAINS screen

The RDKit PAINS filter was applied to every ranked lead. A PAINS alert is reported, never hidden; it changes the validation design (redox and aggregation controls in the proposed assay). The filter flagged posaconazole itself (see §3.1) — an approved drug — which is reported as a filter false-positive illustration, not as a liability of the drug.

### 2.4 Honesty limits

Docking is not activity. Vina's scoring error is ±1–2 kcal/mol, so only margins above ~2 kcal/mol are treated as real differences. No experimental data were generated. No molecular dynamics or free-energy refinement was run. Measured potencies come from ChEMBL records for the target and were not re-measured; the Kd/IC50 mixture (§2.2) limits the rank analysis to four compounds.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | ChEMBL ID | Best affinity (kcal/mol) | Measured potency vs TcCYP51 (ChEMBL) | MW | logP | Lipinski violations | PAINS |
|---|---|---|---|---|---|---|---|
| Posaconazole (QUERY re-dock) | CHEMBL1397 | −10.57 | Kd 18.0 nM (pChEMBL 7.75) | 700.79 | 4.57 | 1 | Alert |
| Posaconazole (as CHEMBL1397) | CHEMBL1397 | −10.14 | Kd 18.0 nM (pChEMBL 7.75) | 700.79 | 4.57 | 1 | Alert |
| CHEMBL5189694 | CHEMBL5189694 | −9.40 | Kd 24.0 nM (pChEMBL 7.62) | 528.39 | 4.03 | 1 | Clean |
| CHEMBL3431164 | CHEMBL3431164 | −8.58 | IC50 50.12 nM (pChEMBL 7.30) | 435.50 | 3.78 | 0 | Clean |
| Albaconazole | CHEMBL298817 | −8.16 | IC50 1.0 nM (pChEMBL 9.00) | 431.83 | 3.07 | 0 | Clean |

Posaconazole still leads. No lead in the docked set beats the posaconazole re-dock, and the best challenger, CHEMBL5189694 — an unnamed tetrazole-triazole azole (C22H15F7N6O2) with a measured Kd of 24 nM — trails by 1.17 kcal/mol, inside Vina's ±1–2 kcal/mol noise: a tie, not a loss. CHEMBL3431164, a non-azole pyridazine (C24H26FN5O2, IC50 50.12 nM), trails by 1.99 kcal/mol and is also inside the noise band.

Two internal checks frame the table. First, the same molecule docked twice — posaconazole as QUERY (−10.57) and as CHEMBL1397 (−10.14) — differs by 0.43 kcal/mol. That is the preparation noise of this run (essentially identical to the 0.42 kcal/mol found in the PfDHODH benchmark of the same pipeline), and it is the floor below which no difference in this table means anything. Second, the RDKit PAINS filter flags posaconazole itself. Posaconazole is an approved drug with a known safety record; the flag is a property of the filter's promiscuity rules on large triazoles, and it is reported here precisely so that the clean PAINS results for the other four compounds are not over-read as a safety claim — the filter's false-positive rate on this chemotype is demonstrated inside this very table.

### 3.2 The ranking failure: albaconazole

Albaconazole (CHEMBL298817; INN/USAN, research code UR-9825, ChEMBL maximum phase 2) is the most potent measured inhibitor in the set: ChEMBL records an IC50 of 1.0 nM against *T. cruzi* CYP51 (pChEMBL 9.00), 18-fold more potent than posaconazole's recorded Kd of 18.0 nM. It is also the most drug-like compound in the table (MW 431.83, logP 3.07, zero Lipinski violations, PAINS-clean). And it has the worst docking score in the set: −8.16 kcal/mol, 2.41 kcal/mol behind the posaconazole re-dock — a margin that clears Vina's noise band, so this is a real ranking failure, not a tie.

Across the four distinct compounds with measured values, the measured potency order is albaconazole (1.0 nM) > posaconazole (18 nM) > CHEMBL5189694 (24 nM) > CHEMBL3431164 (50.12 nM), while the docking order is the near-reverse: posaconazole (−10.57) > CHEMBL5189694 (−9.40) > CHEMBL3431164 (−8.58) > albaconazole (−8.16). Spearman rank correlation ρ = −0.2 (n = 4) — no correlation, slightly negative. The single most likely mechanistic cause is stated in §2.2: Vina cannot model the azole–haem iron coordinate bond, and albaconazole's potency plausibly depends on exactly that interaction plus the quinazolinone scaffold's fit, neither of which the scoring function rewards. A second contributor is the structure choice: the grid is shaped by the 26N inhibitor in 4C27, and albaconazole's difluorophenyl–triazole geometry may fit the posaconazole-shaped pocket of 3K1O better than the 26N-shaped pocket used here — a hypothesis that is testable by re-docking on 3K1O (see §4.4).

### 3.3 Comparison with published docking

No published Vina benchmark of these four compounds on *T. cruzi* CYP51 was found in the literature sweep, so there is no published docking table to compare against. The structural literature does, however, give a qualitative check: the β-phenylimidazole series of Friggeri et al. (2014) binds in two distinct modes — one entering the substrate-access channel, the other under the haem-propionate ceiling — and the 26N inhibitor of 4C27 occupies the channel mode. Our grid, centred on 26N, therefore samples the channel mode. Compounds whose potency depends on the ceiling mode would be systematically under-scored here, which is a second testable explanation for albaconazole's result.

### 3.4 The standardisation problem: the target, not the drug

The CHAGASAZOL numbers (§1) are the standardisation problem for this target. Posaconazole cleared parasites during treatment in essentially all patients and still failed in 81–92% at follow-up. Two readings are possible: the drug never reached sterilising exposure in the chronic-stage tissue compartments, or CYP51 inhibition alone cannot sterilise chronic infection. The VNI mouse-cure report (Friggeri et al., 2014) and the ≥99.8% parasitaemia suppression of the 4C27 series (Vieira et al., 2014) argue the target can work in animals — but both are acute or short-course mouse models, and CHAGASAZOL is a chronic human trial. The honest statement is that the target's clinical validity is unproven, and a docking benchmark cannot settle it; it can only rank compounds for the assay that can.

## 4. Discussion

### 4.1 The reframe

The paper's hypothesis — that Vina on 4C27 reproduces the measured potency order — fails. That failure is the result, and it is more useful than a win would have been: it tells the next run what not to do. A pipeline that had reported albaconazole as the weakest compound and moved on would have discarded the most potent measured inhibitor in its own dataset. The reframe is that for CYP51, docking is a pose generator and a gross filter (it correctly puts all five compounds in a narrow −8 to −11 kcal/mol band, consistent with all of them being real binders), not a ranker. Ranking needs a scoring function that sees the haem coordination — MM-GBSA rescoring, or a metal-aware method — and a second structure (3K1O) to test pocket-shape dependence.

### 4.2 Why the "win" must not be over-read

There is no win in this table, and the near-win deserves the same caution: CHEMBL5189694's −9.40 is 1.17 kcal/mol behind posaconazole, inside noise, and its measured Kd (24 nM) is also essentially tied with posaconazole's (18 nM). The two compounds are indistinguishable by either measure used here. The 0.43 kcal/mol preparation noise (§3.1) means even the posaconazole re-dock value itself carries a ±0.4 kcal/mol preparation uncertainty before Vina's own ±1–2 kcal/mol is added. Nothing in this table supports prioritising one compound over another on docking score alone.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

Posaconazole's PAINS alert (§3.1) is the design constraint in miniature: a filter that flags an approved drug cannot be used as a go/no-go gate on this chemotype. The proposed validation therefore treats PAINS as a prompt for controls — redox-cycling and aggregation controls in the enzyme assay, and a detergent control in the cell assay — rather than as an exclusion criterion. Albaconazole and CHEMBL3431164 are PAINS-clean, which is a genuine (if modest) advantage for them; CHEMBL5189694 is also clean.

### 4.4 Testable hypotheses

1. **Albaconazole binds TcCYP51 more tightly than posaconazole under identical assay conditions.** Measurement: recombinant TcCYP51 spectral binding (Soret shift) and reconstituted enzyme inhibition for albaconazole, posaconazole and CHEMBL5189694 in the same run, same buffer, same substrate (eburicol). Fails if albaconazole's IC50 is not lower than posaconazole's.
2. **The ranking failure is a pocket-shape artefact of 4C27.** Measurement: re-dock all five compounds on the posaconazole-bound structure 3K1O (2.89 Å) with the same protocol, and on 4C27 with the haem iron retained as a metal constraint. Fails if albaconazole still ranks last on both.
3. **The ranking failure is a scoring-function artefact.** Measurement: MM-GBSA rescoring of the Vina poses for all five compounds. Fails if the MM-GBSA order still anti-correlates with the measured order.
4. **Albaconazole's potency translates to the parasite.** Measurement: *T. cruzi* amastigote assay (Tulahuen strain, as in Friggeri et al., 2014) for albaconazole vs posaconazole, with a human CYP51 counter-screen for selectivity. Fails if albaconazole's amastigote EC50 is not lower than posaconazole's, or if it inhibits human CYP51 at comparable concentrations.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant TcCYP51 expression and purification (published constructs exist; Lepesheva et al., 2010), spectral binding titrations for the five compounds. Stage 2 (weeks 3–6): reconstituted enzyme inhibition assay (lanosterol/eburicol substrate, NADPH–cytochrome P450 reductase), IC50 determination in triplicate with posaconazole as the internal control, plus redox/aggregation controls. Stage 3 (weeks 7–10): *T. cruzi* amastigote assay and human CYP51 counter-screen. Stage 4 (weeks 11–12): re-docking on 3K1O and MM-GBSA rescoring, then a go/no-go on the basis of hypotheses 1–4. Total compound requirement is milligrams; albaconazole and posaconazole are commercially available, CHEMBL5189694 and CHEMBL3431164 are research compounds requiring synthesis or a supplier quote.

## 5. Limitations

1. Docking only: no experimental data were generated; every number is a Vina score or a ChEMBL record.
2. Vina cannot model the azole–haem iron coordinate bond, the dominant interaction for four of the five compounds — the most likely cause of the ranking failure.
3. The grid is shaped by the 26N inhibitor in 4C27, not by posaconazole; re-docking on 3K1O was not run.
4. Measured potencies mix Kd and IC50 values from ChEMBL; the rank correlation (n = 4) is indicative only.
5. Only five compounds were docked (top 5 ranked leads including the query); the remaining 21 ranked leads were not docked, so a better-scoring scaffold may exist in the set.
6. No molecular dynamics, no MM-GBSA rescoring, no selectivity data against human CYP51 for the two unnamed leads.
7. The clinical validity of CYP51 as a Chagas target is unproven (CHAGASAZOL); a better inhibitor is not yet a better treatment.
8. PAINS and Tox21 read-across are computational flags, not toxicology.

## 6. Conclusion

On the high-resolution *T. cruzi* CYP51 structure 4C27, posaconazole still leads the docking table at −10.57 kcal/mol and no lead beats it — but the table fails the test that matters: the most potent measured inhibitor, albaconazole (IC50 1.0 nM), scores worst (−8.16 kcal/mol), and docking rank does not track measured potency (Spearman ρ = −0.2). The honest conclusion is that Vina on this structure is a pose generator, not a ranker, for CYP51. The next experiment is a head-to-head recombinant enzyme assay of albaconazole, posaconazole and CHEMBL5189694, with re-docking on 3K1O and MM-GBSA rescoring to find out whether the failure is the pocket or the scoring function. No cure claim is made, and no clinical recommendation follows.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. The docking pipeline is the LeadForge pipeline (UniProtKB → ChEMBL → PubChem → RDKit → AutoDock Vina). No funding was received; no conflicts of interest are declared.

## References

1. World Health Organization. Chagas disease (American trypanosomiasis). Fact sheet. Geneva: WHO; 2024. (6–7 million infected; >10,000 deaths/year; 21 endemic countries; >100 million at risk.)
2. Molina I, Gómez i Prat J, Salvador F, Treviño B, Sulleiro E, Serre N, Pou D, Roure S, Cabezos J, Valerio L, Blanco-Grau A, Sánchez-Montalvá A, Vidal X, Pahissa A. Randomized trial of posaconazole and benznidazole for chronic Chagas' disease. N Engl J Med. 2014;370(20):1899-1908. doi:10.1056/NEJMoa1313122. PMID: 24827034. (CHAGASAZOL, NCT01162967.)
3. Lepesheva GI, Hargrove TY, Anderson S, Kleshchenko Y, Furtak V, Wawrzak Z, Villalta F, Waterman MR. Structural insights into inhibition of sterol 14α-demethylase in the human pathogen *Trypanosoma cruzi*. J Biol Chem. 2010;285(36):25582-25590. doi:10.1074/jbc.M110.133215. PMID: 20530488. (PDB 3K1O posaconazole, 3KHM fluconazole, VNF.)
4. Chen CK, Leung SS, Guilbert C, Jacobson MP, McKerrow JH, Podust LM. Structural characterization of CYP51 from *Trypanosoma cruzi* and *Trypanosoma brucei* bound to the antifungal drugs posaconazole and fluconazole. PLoS Negl Trop Dis. 2010;4(3):e651. PMID: 20386598. (PDB 2WUZ, 2WX2.)
5. Lepesheva GI, Ott RD, Hargrove TY, Kleshchenko YY, Schuster I, Nes WD, Hill GC, Villalta F, Waterman MR. Sterol 14α-demethylase as a potential target for antitrypanosomal therapy: enzyme inhibition and parasite cell growth. Chem Biol. 2007;14(11):1283-1293. (VNI/VNF selective scaffold; no human CYP51 inhibition; >99% amastigote kill at 1 µM.)
6. Lepesheva GI. Targeting *Trypanosoma cruzi* sterol 14α-demethylase (CYP51). Adv Parasitol. 2011;75:65-87. doi:10.1016/B978-0-12-385863-4.00004-6. PMID: 21820552.
7. Friggeri L, Hargrove TY, Rachakonda G, Williams AD, Wawrzak Z, Di Santo R, De Vita D, Waterman MR, Tortorella S, Villalta F, Lepesheva GI. Structural basis for rational design of inhibitors targeting *Trypanosoma cruzi* sterol 14α-demethylase: two regions of the enzyme molecule potentiate its inhibition. J Med Chem. 2014;57(15):6704-6717. doi:10.1021/jm500739f. PMID: 25033013. (β-phenylimidazoles, EC50 1.0–5.5 nM; VNI mouse cure cited therein.)
8. Vieira DF, Choi JY, Calvet CM, Siqueira-Neto JL, Johnston JB, Kellar D, Gut J, Cameron MD, McKerrow JH, Roush WR, Podust LM. Binding mode and potency of N-indolyl-oxopyridinyl-4-amino-propanyl-based inhibitors targeting *Trypanosoma cruzi* CYP51. J Med Chem. 2014;57:10162. doi:10.1021/jm501568b. PMID: 25393646. (PDB 4C27, 1.95 Å; ≥99.8% parasitaemia suppression in mice.)
9. ChEMBL database (EBI). Target CHEMBL1075110 (*Trypanosoma cruzi* sterol 14-alpha demethylase); compounds CHEMBL1397 (posaconazole, Kd 18.0 nM), CHEMBL298817 (albaconazole, IC50 1.0 nM), CHEMBL5189694 (Kd 24.0 nM), CHEMBL3431164 (IC50 50.12 nM). Accessed 9 November 2026.
10. RCSB Protein Data Bank. PDB 4C27 (*T. cruzi* CYP51–26N, 1.95 Å); PDB 3K1O (*T. cruzi* CYP51–posaconazole, 2.89 Å). Accessed 9 November 2026.
11. Merck Manual Professional Edition. Chagas Disease. (Chronic disease develops in 20–30% of patients.) Accessed 9 November 2026.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-025-2026-11-09.json` (LeadForge pipeline run, 9 November 2026): UniProtKB Q7Z1V1, ChEMBL target CHEMBL1075110 (56 bioactivities), 26 ranked leads, Vina 1.2.7 docking on PDB 4C27 (centre [−10.75, −39.85, −23.88], box 22.5 Å, exhaustiveness 8). ChEMBL IDs: posaconazole CHEMBL1397, albaconazole CHEMBL298817, CHEMBL5189694, CHEMBL3431164. PDB file used for the centre audit: `clinic-demo/app/discovery/data/pdb_cache/4C27.pdb`. No additional data were generated.
