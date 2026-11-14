# Rigid Docking Separates Genuine Trypanothione Reductase Inhibitors from Miltefosine but Ranks the Series Backwards

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification.**

**Author:** Zubair Ali, Pharm-D student, Faculty of Pharmacy, SMBBMU, Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 14 November 2026
**Topic ID:** HP-024

## Abstract

Trypanothione reductase (TR) is the flavoenzyme that keeps the trypanothione redox system of *Leishmania* and *Trypanosoma* parasites reduced; humans have no equivalent enzyme, which makes it a selective antiparasitic target. *Leishmania donovani* TR has no deposited crystal structure, so we docked against the *Leishmania infantum* homologue (87.2% sequence identity), structure 4ADW, centred on the bound physiological substrate trypanothione. We benchmarked rigid AutoDock Vina docking against measured inhibition data for four β-carboline–quinazolinone TR inhibitors (Ki 0.8–9.2 µM), with miltefosine — the oral clinical drug for visceral leishmaniasis, which is not a TR inhibitor — as a negative control. Docking separated the classes cleanly: the four genuine inhibitors scored −7.75 to −8.56 kcal/mol, while miltefosine scored −4.54 kcal/mol, a gap of at least 3.21 kcal/mol. Within the inhibitor series, however, the ranking was inverted (Spearman ρ = −0.6, n = 4): the two weakest measured inhibitors (Ki 7.2 and 9.2 µM) scored best (−8.56 and −8.40 kcal/mol), and the most potent (Ki 800 nM) ranked third (−8.13 kcal/mol). All four inhibitors fell inside a 0.81 kcal/mol band — one noise band — while their measured potencies span 11.5-fold. Rigid docking can tell a TR inhibitor from a non-inhibitor, but it cannot rank this series. The result supports TR as a target — the first-line antimonials act through it — while warning that docking scores alone should not prioritise analogues for synthesis.

**Keywords:** trypanothione reductase; Leishmania donovani; Leishmania infantum; visceral leishmaniasis; molecular docking; AutoDock Vina; miltefosine; β-carboline

## Introduction

Visceral leishmaniasis (VL, kala-azar) is fatal in over 95% of cases if untreated, with an estimated 50,000–90,000 new cases worldwide each year, of which only 25–45% are reported to WHO. In Pakistan VL is endemic in the northern high-altitude areas — Gilgit-Baltistan and Azad Jammu Kashmir, with Khyber Pakhtunkhwa also at risk — where *Leishmania infantum* is the most commonly reported causative species; most cases are children under six. Reported VL numbers are small (seven cases in 2014), while cutaneous leishmaniasis dominates the national burden (over 10,000 cases in Khyber Pakhtunkhwa alone in 2026). Treatment rests on a handful of drugs: pentavalent antimonials, amphotericin B, paromomycin, and miltefosine, the only oral agent. Resistance and toxicity limit all of them, and no vaccine exists.

Trypanothione reductase (TR, EC 1.8.1.12) is the parasite's analogue of human glutathione reductase: it reduces trypanothione, the spermidine–glutathione conjugate that replaces glutathione in trypanosomatids. The trypanothione system is unique to these parasites, and human glutathione reductase shares only ~40% sequence identity with TR and has different substrate specificity, so TR inhibition should be selective. The target is validated by the oldest drugs in the field: pentavalent antimonials are reduced to Sb(III) in the parasite, and Sb(III) binds the catalytic cysteines of TR (Baiocco et al., *J Med Chem* 2009). Miltefosine, by contrast, does not act on TR: its antileishmanial mechanism is attributed to interference with phospholipid metabolism and membrane function (Dorlo et al., *J Antimicrob Chemother* 2012). That contrast makes miltefosine an ideal negative control for a docking benchmark: a method that scores it alongside genuine TR inhibitors cannot discriminate; a method that separates it can.

This paper benchmarks rigid docking on four β-carboline–quinazolinone TR inhibitors reported by Chauhan et al. (*MedChemComm* 2015), the only measured TR inhibitor series with usable potency data in ChEMBL for *L. donovani* TR, and asks whether docking can rank them.

## Methods

### 2.1 Target, structure and the homologue problem

*Leishmania donovani* trypanothione reductase (UniProt P39050, 491 amino acids) was resolved to ChEMBL target CHEMBL2176840, which holds only six known ligands. P39050 has **no PDB cross-reference in UniProt**: no *L. donovani* TR structure has been deposited. The closest experimental structure is the *L. infantum* enzyme (UniProt A4HSF7, also 491 amino acids), with 87.2% ungapped sequence identity to P39050; the two species belong to the same *L. donovani* complex, and *L. infantum* is the species most commonly reported in Pakistani VL. We used 4ADW (3.61 Å), the *L. infantum* TR structure with the physiological substrate trypanothione bound (Baiocco et al., *ChemMedChem* 2013;8:1175; PMID 23733388). The docking centre was the chain-A trypanothione centroid [21.56, 41.03, −18.76], i.e. the active site itself. All docking used AutoDock Vina 1.2.7, exhaustiveness 8, box 22.5 Å.

### 2.2 Compounds

The four inhibitors are β-carboline–quinazolinone hybrids from Chauhan et al. (2015): CHEMBL3735035 (Ki 800 nM), CHEMBL3735110 (Ki 6.5 µM), CHEMBL3736154 (Ki 7.2 µM) and CHEMBL3735109 (Ki 9.2 µM), all measured against *L. donovani* TR and all PAINS-clean. The reference compound was miltefosine (PubChem CID 3599; C21H46NO4P; hexadecyl 2-(trimethylazaniumyl)ethyl phosphate), verified directly against PubChem after the pipeline's in-run query lookup failed. Miltefosine has no reported TR inhibitory activity and serves as the negative control.

### 2.3 Limitations of the docking model, stated in advance

The receptor is a **homologue** (87.2% identity), not the assay species, and at **3.61 Å** resolution — the lowest-resolution structure used in this series. Receptor preparation drops HETATM records, so the FAD prosthetic group and NADPH — both present in the crystal structure and both shaping the active site — are **absent** from the docked receptor. Rigid docking carries a documented ±1–2 kcal/mol noise band. Miltefosine's hexadecyl tail has ~19 rotatable bonds and may be under-sampled at exhaustiveness 8. The rank correlation uses only four compounds.

### 2.4 Literature

Measured potencies were taken from ChEMBL (accessed 14 November 2026) and verified against the source document. The 4ADW structure, the antimony mechanism and the miltefosine mechanism were verified against the primary literature. Pakistan burden figures are from the WHO leishmaniasis fact sheet and a 2019 case report from Khyber Pakhtunkhwa.

## Results

### 3.1 The compounds

The four inhibitors share the β-carboline–quinazolinone scaffold and differ only in their quinazolinone N-substituent: CHEMBL3735035 carries an N-pentyl group (Ki 800 nM); CHEMBL3735110 an N-ethyl group (Ki 6.5 µM); CHEMBL3736154 an N-(4-chlorophenyl) group (Ki 7.2 µM); CHEMBL3735109 an N-(4-methoxybenzyl) group (Ki 9.2 µM). Their measured potencies span 11.5-fold, equivalent to ~1.4 kcal/mol at 298 K — inside Vina's noise band, which already limits what any ranking can show.

**Table 1. β-Carboline–quinazolinone TR inhibitors and miltefosine docked on 4ADW (*L. infantum* TR, 3.61 Å), substrate-centred.**

| Compound | Measured Ki | Vina score (kcal/mol) | Top-3 poses |
|---|---|---|---|
| CHEMBL3736154 | 7.2 µM | −8.56 | −8.56, −8.31, −8.06 |
| CHEMBL3735109 | 9.2 µM | −8.40 | −8.40, −8.32, −7.72 |
| CHEMBL3735035 | 800 nM | −8.13 | −8.13, −7.55, −7.16 |
| CHEMBL3735110 | 6.5 µM | −7.75 | −7.75, −7.54, −7.22 |
| Miltefosine (QUERY) | no TR activity | −4.54 | −4.54, −4.47, −4.26 |

### 3.2 Docking separates inhibitors from the non-inhibitor

The class separation is unambiguous: every genuine TR inhibitor scored −7.75 kcal/mol or better, while miltefosine scored −4.54 kcal/mol — a gap of at least 3.21 kcal/mol, more than three times Vina's noise band. Miltefosine's poses were also uniformly weak (−4.54, −4.47, −4.26), so the result is not a single bad pose. The method can tell a TR inhibitor from a drug that works elsewhere. This is the first clean negative-control separation in this series.

### 3.3 Within the series, the ranking is inverted

Within the four inhibitors the ranking fails: Spearman ρ = −0.6 (n = 4). The two weakest measured inhibitors scored best — CHEMBL3736154 (7.2 µM) at −8.56 and CHEMBL3735109 (9.2 µM) at −8.40 — while the most potent, CHEMBL3735035 (800 nM), ranked third at −8.13. All four inhibitors sit inside a 0.81 kcal/mol band, less than half of Vina's noise band, so the inversion is a within-noise effect rather than a large error — but it is an inversion all the same, and it means docking scores cannot prioritise analogues in this series. The N-pentyl compound is 8–11-fold more potent than the others in the assay and unremarkable in the dock.

## Discussion

Two findings, pulling in opposite directions.

**First, the negative control works.** Miltefosine's −4.54 kcal/mol against −7.75 to −8.56 for genuine inhibitors is the clearest discrimination this series has produced. It shows that rigid docking into the trypanothione pocket is not simply rewarding any large hydrophobic molecule: the pocket recognises the β-carboline–quinazolinone scaffold and rejects an alkylphosphocholine. For a screening pipeline, that is useful — docking can be used as a first-pass filter to discard compounds that do not belong in the pocket at all.

**Second, within-series ranking fails, and the reasons are visible.** The measured potency range (11.5-fold, ~1.4 kcal/mol) is inside the method's noise band, so even a perfect method would struggle — but the inversion is systematic, not random: both of the weakest compounds out-scored the strongest. Three contributors are identifiable: (i) the structure is a homologue at 3.61 Å, so side-chain positions in the pocket are uncertain; (ii) FAD and NADPH are missing from the docked receptor, removing the cofactor contacts that shape the pocket; and (iii) the series differs only in the quinazolinone N-substituent, a region the rigid model may score mainly by size — the two largest substituents (4-chlorophenyl, 4-methoxybenzyl) scored best, suggesting the model rewards bulk where the assay rewards the smaller N-pentyl group. Any of these alone could invert a within-noise ranking.

For Pakistan, the practical points are: TR remains a sound target — it is parasite-specific, and the antimonials that still anchor VL treatment act through it — and the *L. infantum* structure is the right homologue for Pakistani VL, since *L. infantum* is the species most commonly reported there. But analogue prioritisation for TR needs more than Vina scores: the Chauhan et al. series itself was reported with its own molecular docking in 2015, and the field should treat docking as a filter (inhibitor vs non-inhibitor) rather than a ranker within a congeneric series, until a metal/cofactor-aware, higher-resolution model is available.

## Limitations

1. **No lab data.** All results are computational; no TR assay was run.
2. **Homologue structure.** Docking used *L. infantum* TR (87.2% identity), not the *L. donovani* enzyme the Ki values were measured against.
3. **Low resolution.** 4ADW is 3.61 Å; side-chain positions in the pocket are uncertain.
4. **Cofactors removed.** FAD and NADPH were dropped during receptor preparation; the docked pocket lacks them.
5. **Rigid docking, ±1–2 kcal/mol noise.** The measured 11.5-fold potency range (~1.4 kcal/mol) is inside the noise band.
6. **Small n.** The rank correlation uses four compounds; a single additional compound could change ρ substantially.
7. **Miltefosine sampling.** Its long flexible tail may be under-sampled at exhaustiveness 8, though its score is so weak that better sampling is unlikely to close a 3.21 kcal/mol gap.
8. **Single source series.** All four inhibitors come from one 2015 paper; the benchmark does not test other TR chemotypes.

## Conclusion

Rigid docking into the *L. infantum* trypanothione reductase structure 4ADW separates genuine β-carboline–quinazolinone TR inhibitors (−7.75 to −8.56 kcal/mol) from the non-inhibitor miltefosine (−4.54 kcal/mol) by more than 3 kcal/mol, but ranks the inhibitor series backwards (Spearman ρ = −0.6): the weakest measured inhibitors score best. Docking is a usable first-pass filter for TR — it recognises the scaffold and rejects outsiders — but it cannot prioritise analogues within a congeneric series, and scores alone should not decide which analogue to synthesise next. TR itself remains a sound, parasite-specific target for visceral leishmaniasis, a disease that is rare but present in northern Pakistan and fatal in over 95% of untreated cases.

## Acknowledgments

Manuscript drafted with AI assistance (Lapis). The author reviewed all computed values against the raw docking outputs and all citations against the primary sources. This is an AI-assisted draft, not a peer-reviewed publication; all claims require independent laboratory verification. No funding was received. The author declares no conflicts of interest.

## References

1. Chauhan SS, Pandey S, Shivahare R, et al. Novel β-carboline–quinazolinone hybrid as an inhibitor of *Leishmania donovani* trypanothione reductase: synthesis, molecular docking and bioevaluation. *MedChemComm*. 2015;6:351–356. doi:10.1039/C4MD00298A.
2. Baiocco P, Colotti G, Franceschini S, Ilari A. Molecular basis of antimony treatment in leishmaniasis. *J Med Chem*. 2009;52(8):2603–2612. PMID: 19317451. doi:10.1021/jm900185q.
3. Baiocco P, et al. Inhibition of *Leishmania infantum* trypanothione reductase by azole-based compounds: a comparative analysis with its physiological substrate by X-ray crystallography. *ChemMedChem*. 2013;8(7):1175–1183. PMID: 23733388. doi:10.1002/cmdc.201300176.
4. Dorlo TPC, Balasegaram M, Beijnen JH, de Vries PJ. Miltefosine: a review of its pharmacology and therapeutic efficacy in the treatment of leishmaniasis. *J Antimicrob Chemother*. 2012;67(11):2576–2597. doi:10.1093/jac/dks275.
5. World Health Organization. Leishmaniasis. WHO fact sheet. Geneva: WHO; 2023. https://www.who.int/news-room/fact-sheets/detail/leishmaniasis
6. Visceral leishmaniasis in a resident of Swat, Khyber Pakhtunkhwa, Pakistan. *Cureus*. 2019;11(11):e6059. doi:10.7759/cureus.6059.

## Data Availability

All docking outputs are available from the author on request. Pipeline output: `dock-HP-024-2026-11-14.json` (docking skipped — no *L. donovani* TR structure); homologue docking: `dock-HP-024-2026-11-14-4ADW.json` (4ADW, substrate-centred). Structure: PDB 4ADW (3.61 Å). Measured potencies: ChEMBL target CHEMBL2176840, document CHEMBL3734756, accessed 14 November 2026. Compound structures: PubChem CID 3599 (miltefosine); ChEMBL IDs CHEMBL3735035, CHEMBL3735110, CHEMBL3736154, CHEMBL3735109.
