# No Structure to Dock On: Five Single-Digit-Nanomolar TbNMT Inhibitors Share One Scaffold, and the Blood–Brain Barrier — Not Potency — Decides Whether Any of Them Treats Stage-2 Sleeping Sickness

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-18 · **Health Papers Agent — Paper #77** (daily 5-paper run)

**Keywords:** sleeping sickness; Trypanosoma brucei; N-myristoyltransferase; DDD85646; blood–brain barrier; neglected tropical disease; ChEMBL

---

## Abstract

Human African trypanosomiasis (sleeping sickness) is down to 471 reported cases worldwide in 2025, and the WHO target is interruption of transmission by 2030 — but the last cases are the hardest, and they need drugs that reach the brain. DDD85646, a pyrazole-sulfonamide inhibitor of Trypanosoma brucei N-myristoyltransferase (TbNMT), is potent (enzyme IC50 1–2 nM) and cures stage-1 (haemolymphatic) infection in rodents, yet poor central nervous system exposure restricts it to stage 1. We asked whether ChEMBL holds a DDD85646 analogue that keeps the potency and fixes the brain exposure. Using the LeadForge pipeline (UniProtKB Q388H8 → ChEMBL target CHEMBL3988596, 60 bioactivities → PubChem/RDKit similarity, PAINS and ADMET screen), we retrieved five single-digit-nanomolar TbNMT inhibitors, including DDD85646 itself. Docking was not performed: no Trypanosoma brucei NMT crystal structure exists in the PDB (verified 2026-11-18; the only NMT structures are from Leishmania major and Aspergillus fumigatus), and docking a T. brucei inhibitor onto another species' enzyme would be a false result. The honest finding is structural, not numerical: all five compounds share one scaffold (identical TPSA 92.15 Å², the published pyrazole-sulfonamide core), so none obviously escapes the parent's brain-exposure problem on descriptors alone — the smallest and least lipophilic analogue, CHEMBL4112331 (MW 426.55, logP 2.31), is the only one inside all standard CNS descriptor bands, and even it sits at TPSA 92.15 Å², just above the usual <90 Å² blood–brain-barrier guideline. The claim that any analogue is a stage-2 candidate would be refuted if PAMPA-BBB or MDCK-MDR1 testing shows no analogue beats DDD85646's brain exposure. The falsifiable next step is a 4-week BBB-permeability screen of the four analogues, not another potency assay.

---

## 1. Introduction

Sleeping sickness, caused by Trypanosoma brucei gambiense (92% of cases) and T. b. rhodesiense and transmitted by the tsetse fly, is fatal without treatment and has two stages: a haemolymphatic stage with non-specific symptoms, and a meningoencephalitic stage in which parasites enter the central nervous system, causing the sleep disturbance, psychiatric symptoms and coma that give the disease its name. In 1998 more than 34,000 cases were reported, with the WHO estimating the true number at ten times that; by 2025 only 471 cases were reported worldwide, most of them in the Democratic Republic of the Congo. Guinea was validated by WHO in January 2025 as having eliminated gambiense sleeping sickness as a public health problem (fewer than one case per 10,000 people in endemic areas over 2019–2023). The WHO roadmap's harder goal is interruption of transmission — zero cases — by 2030.

Treatment has modernised fast: fexinidazole (2018) was the first all-oral drug, and acoziborole — a single-dose oral drug with 98.1% efficacy in trials — received a positive scientific opinion from the European Medicines Agency in 2026. Against that background, a new NMT inhibitor must answer a sharp question: what does it add that acoziborole does not already provide? The honest answer for a DDD85646 analogue is: nothing, unless it reaches the brain — because stage-2 disease is the unmet need, and DDD85646's failure was a brain-exposure failure, not a potency failure.

TbNMT catalyses the co-translational transfer of myristate from myristoyl-CoA to the N-terminal glycine of target proteins; bioinformatic analysis suggests more than 60 potential substrates in T. brucei, including ADP-ribosylation factor-1 (ARF-1) and ARF-like protein 1 (ARL-1), both essential for bloodstream parasite viability. RNAi knockdown of NMT is lethal in culture and abrogates infectivity in animal models. DDD85646 was discovered at Dundee: it inhibits TbNMT (IC50 2 nM as published; 1 nM in the ChEMBL record), kills T. brucei in culture (EC50 2 nM), has good oral pharmacokinetics and cures rodent models of peripheral infection — and its development stopped at the blood–brain barrier.

The classical Islamic medical canon has no specific discussion of trypanosomiasis: sleeping sickness is a sub-Saharan disease outside the clinical geography of Ibn Sina's Canon (c. 1025) and Al-Razi's Kitab al-Hawi (c. 900), and the canon sweep for this paper found no relevant text (see Limitations). What the canon does supply is the principle: hifz al-nafs (preservation of life) and maslaha (public benefit) applied to the neglected — the duty to test a cheap discriminating experiment for a disease of the poorest, rather than to abandon it because the case count is now small. A disease with 471 cases a year is exactly where a small, cheap test matters most, because no company will run it (see §7).

**Falsifiable question.** Does any ChEMBL-recorded DDD85646 analogue combine single-digit-nanomolar TbNMT inhibition with predicted blood–brain-barrier penetration better than DDD85646 itself? **Falsifier:** PAMPA-BBB or MDCK-MDR1 testing showing no analogue beats DDD85646's brain exposure, or a measured brain-to-plasma ratio below 0.1 for the best analogue. **Causal identification:** none available in this study — this is a descriptor and literature analysis, association only, stated in bold. No docking was possible, so there is no validated-control re-docking to anchor a causal claim.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-18: the Dundee DDD85646 papers (Nature 2010; Journal of Medicinal Chemistry 2012; Acta Crystallographica F 2015), the WHO human African trypanosomiasis fact sheet, the 2025–2026 elimination literature (Guinea validation; acoziborole EMA opinion; 471 cases in 2025), and the RCSB/PDBe records for NMT structures. The Islamic-canon sweep covered the available digitised canon: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025); Al-Razi, Kitab al-Hawi (c. 900) — no trypanosomiasis text was found in either, and that negative result is reported in the Limitations rather than hidden.

### 2.2 Why there is no docking section

Standardised AutoDock Vina docking requires an experimental structure of the target. The LeadForge pipeline (UniProtKB Q388H8, ChEMBL target CHEMBL3988596) found no PDB entry for T. brucei NMT: `find_pdb_for_uniprot` returned `no_pdb_found` because the TrEMBL entry Q388H8 carries no PDB cross-reference. A direct RCSB full-text search on 2026-11-18 returned seven NMT structures — 5AG4, 5AG5, 5AG6, 5AG7, 5AGE (all Leishmania major NMT) and 4UWI, 4UWJ (both Aspergillus fumigatus NMT). None is T. brucei. Docking a T. brucei inhibitor onto the Leishmania enzyme would produce a number that looks like a result and is not one; the paper therefore reports no docking scores at all. This follows the precedent of Paper #70 (HP-067, Plasmodium PI4K), where the same situation was handled the same way.

### 2.3 Compound retrieval and screens

LeadForge pipeline, 2026-11-18: UniProtKB Q388H8 (glycylpeptide N-tetradecanoyltransferase, T. brucei brucei strain 927/4 GUTat10.1) → ChEMBL target CHEMBL3988596 (60 bioactivities) → PubChem verification of DDD85646 (CID 44199337) → RDKit Morgan-fingerprint similarity screen (top 25) → ADMET/PAINS/ToxGuard panel → composite ranking. RDKit descriptors and Tox21 kNN read-across (12 assays) computed for every lead; PAINS filter applied to all 26 leads.

### 2.4 Honesty limits

No docking, no experimental data, no BBB measurement in this study. Measured IC50 values are ChEMBL records. Blood–brain-barrier penetration is assessed here only through computed descriptors against standard CNS guidelines (TPSA <90 Å², MW <450 Da, logP 2–4) — descriptors predict, they do not measure. The ChEMBL IC50 for DDD85646 (1 nM) differs from the published value (2 nM); both are reported.

## 3. Results

### 3.1 The five single-digit-nanomolar inhibitors

| Compound | ChEMBL IC50 vs TbNMT* | MW | logP | TPSA (Å²) | Rotatable bonds | Lipinski violations | PAINS |
|---|---|---|---|---|---|---|---|
| CHEMBL1230468 (= DDD85646) | 1.0 nM (pChEMBL 9.00) | 495.44 | 3.62 | 92.15 | 5 | 0 | none |
| CHEMBL4115085 | 4.0 nM (pChEMBL 8.40) | 462.53 | 2.59 | 92.15 | 5 | 0 | none |
| CHEMBL4111551 | 1.0 nM (pChEMBL 9.00) | 460.99 | 2.96 | 92.15 | 5 | 0 | none |
| CHEMBL3357685 | 1.0 nM (pChEMBL 9.00) | 537.52 | 4.51 | 92.15 | 7 | 1 | none |
| CHEMBL4112331 | 1.0 nM (pChEMBL 9.00) | 426.55 | 2.31 | 92.15 | 5 | 0 | none |
| DDD85646 (reference, PubChem CID 44199337) | published IC50 2 nM; EC50 2 nM vs T. brucei | 495.44 | 3.62 | 92.15 | 5 | 0 | none |

\* ChEMBL-recorded IC50 against T. brucei NMT (target CHEMBL3988596), retrieved live 2026-11-18. CHEMBL1230468 is DDD85646 itself (similarity 1.0, identical descriptors), so the "five leads" are the reference plus four analogues.

### 3.2 One scaffold, one TPSA, one problem

All five compounds share TPSA 92.15 Å² exactly — the same polar surface, the same pyrazole-sulfonamide core. The analogues differ only in peripheral substitution (MW 427–538, logP 2.31–4.51). That means the potency is a property of the scaffold, and the scaffold's brain problem is likely shared: DDD85646's poor CNS exposure is a property of this chemotype's polar surface and efflux profile, and changing a peripheral substituent rarely moves TPSA at all — indeed, here it did not move by a single unit. Against standard CNS descriptor bands (TPSA <90 Å², MW <450 Da, logP 2–4), only CHEMBL4112331 sits inside all three bands except TPSA, where it too is 92.15 Å² — 2.15 Å² over the line. CHEMBL3357685 (MW 537.52, logP 4.51, one Lipinski violation) is the worst BBB bet of the four.

### 3.3 Toxicity read-across

Tox21 kNN read-across predicted no assay at or above 0.3 probability for any of the five compounds, including DDD85646. This is a weak screen — read-across, not measurement — and it cannot see CNS exposure or efflux.

### 3.4 Comparison with published work

DDD85646's published profile (Frearson et al., Nature 2010; Brand et al., Journal of Medicinal Chemistry 2012): enzyme IC50 2 nM, T. brucei EC50 2 nM, good oral pharmacokinetics, cures rodent peripheral infection, poor CNS exposure. The ChEMBL record (IC50 1 nM) is consistent within assay variation. The fragment-screen paper (Acta Crystallographica F 2015) states the consequence plainly: poor CNS exposure restricts DDD85646 to the haemolymphatic (stage-1) form, and new chemical matter was sought specifically to occupy the DDD85646 binding site with better brain penetration. No analogue in this set has a published brain-exposure measurement.

## 4. Discussion

### 4.1 The reframe

The question is not "which analogue is most potent" — four of the five are 1 nM, and potency stopped being the problem in 2010. The question is "which analogue, if any, crosses the blood–brain barrier", and this paper's descriptor analysis suggests the answer may be "none of these four": they share the parent's polar surface exactly, and the parent does not cross. The honest contribution of this paper is therefore a negative one — it narrows the search. It says: do not spend the next assay on enzyme potency for this scaffold; spend it on permeability, and if permeability fails, leave the scaffold.

### 4.2 Why a docking score would have made this paper worse

If a Leishmania NMT structure had been used as a surrogate, the paper could have reported attractive-looking scores (−10 kcal/mol and better) for compounds whose target is a different species' enzyme. Those scores would have been uninterpretable: NMT active sites are conserved enough to dock plausibly and different enough that a 1–2 kcal/mol difference means nothing. Refusing the surrogate dock is the methodologically correct choice, and it is also the reason this paper is shorter on numbers than its neighbours.

### 4.3 Mechanism

NMT transfers myristate from myristoyl-CoA to N-terminal glycine residues of substrate proteins; DDD85646 occupies the peptide-substrate pocket, not the myristoyl-CoA site. Inhibition blocks myristoylation of essential substrates (ARF-1, ARL-1), mislocalises them, and kills the parasite rapidly. For stage-2 disease the inhibitor must additionally cross the blood–brain barrier — which requires low polar surface, moderate lipophilicity, and escape from efflux transporters (P-glycoprotein, BCRP). Test for each link: (i) PAMPA-BBB measures passive permeability; (ii) MDCK-MDR1 efflux ratio measures transporter liability; (iii) a mouse brain-to-plasma ratio measures the outcome that matters.

### 4.4 Testable hypotheses

1. CHEMBL4112331 has a PAMPA-BBB permeability above the CNS-positive threshold and an MDCK-MDR1 efflux ratio below 2. Falsifier: permeability below threshold or efflux ratio ≥2.
2. No analogue in this set achieves a mouse brain-to-plasma ratio above 0.3. Falsifier: any analogue exceeds 0.3.
3. Acoziborole's single-dose efficacy (98.1%) makes a stage-1-only NMT inhibitor clinically redundant in gambiense HAT. Falsifier: a setting where acoziborole is unavailable or contraindicated and a stage-1 NMT inhibitor changes outcomes.

### 4.5 Proposed validation (university-lab feasible, 4–8 weeks)

Stage 1 (weeks 1–2): PAMPA-BBB + MDCK-MDR1 for the four analogues and DDD85646; readout is permeability and efflux ratio, with a CNS-positive control. Stage 2 (weeks 3–5): for any analogue passing stage 1, mouse brain-to-plasma ratio after a single oral dose; if none passes, stop — publish the negative result. Stage 3 (weeks 6–8): only for an analogue with brain exposure: whole-cell EC50 against T. b. gambiense and T. b. rhodesiense bloodstream forms, plus a stage-2 mouse model. Total cost is small; the decision it buys is whether this scaffold lives or dies.

## 5. Limitations

1. No docking (no T. brucei NMT structure exists) and no experimental data in this study; the BBB assessment is descriptor-based only.
2. Measured IC50 values are ChEMBL records; the DDD85646 ChEMBL value (1 nM) differs from the published value (2 nM).
3. TPSA/logP/MW bands are guidelines, not measurements; efflux transporters can defeat even a descriptor-perfect molecule.
4. All five compounds share one scaffold; the analysis cannot speak to other NMT chemotypes.
5. No human NMT selectivity data are reported here; human NMT inhibition would be a toxicity liability and was not assessed beyond Tox21 read-across.
6. The Islamic-canon sweep found no classical text on trypanosomiasis — the disease lies outside the canon's clinical geography — so the canon contributes a principle (hifz al-nafs, maslaha for the neglected) rather than a precedent.
7. No cost or access analysis for acoziborole in the DRC was available for this paper.

## 6. Conclusion

Five single-digit-nanomolar inhibitors of T. brucei NMT exist in ChEMBL — DDD85646 and four analogues at 1–4 nM, all PAINS-clean and Lipinski-clean except one. No T. brucei NMT structure exists, so no docking was performed and none is claimed. The five share one scaffold and one polar surface (TPSA 92.15 Å²), which means none obviously escapes the parent's published failure: poor brain exposure restricting it to stage-1 disease. The smallest analogue, CHEMBL4112331, is the only one inside the standard CNS descriptor bands apart from TPSA, and it is the only one worth the cheap permeability test. If it fails that test, the scaffold should be retired and the field's attention should stay on the drugs that already work — fexinidazole and acoziborole — and on the 2030 transmission-interruption goal.

## 7. Policy implications

**Decision-maker:** The WHO Department of Control of Neglected Tropical Diseases and the DRC national sleeping-sickness programme, with DNDi as technical adviser. **Decision:** whether any further public money should go to the DDD85646 scaffold. **Exact change:** fund only the 4-week PAMPA-BBB/MDCK-MDR1 screen proposed in §4.5 for the four analogues, and fund no efficacy work on this scaffold until an analogue passes it — instead of continuing potency-first screening that has already produced five 1 nM compounds and zero stage-2 drugs. **If evidence Z appears, reverse this:** if CHEMBL4112331 (or any analogue) shows a brain-to-plasma ratio above 0.3, escalate it to the stage-2 mouse model and a head-to-head comparison with acoziborole; if none passes, retire the scaffold and redirect the same funds to acoziborole delivery and tsetse control in the DRC, where the remaining 471 cases are. The Islamic principle is hifz al-nafs with maslaha for the neglected (mustad'afun): for a disease of the poorest, with 471 cases left, the obligation is to spend the small amount on the discriminating test and the large amount on delivery — not to keep polishing a potency number that stopped mattering in 2010.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and pipeline computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Frearson JA, Brand S, McElroy SP, Cleghorn LAT, Smid O, Stojanovski L, Price HP, Guther MLS, Torrie LS, Robinson DA, Hallyburton I, Mpamhanga CP, Brannigan JA, Wilkinson AJ, Hodgkinson M, Hui R, Qiu W, Raimi OG, van Aalten DMF, Brenk R, Gilbert IH, Read KD, Fairlamb AH, Ferguson MAJ, Smith DF, Wyatt PG. N-myristoyltransferase inhibitors as new leads to treat sleeping sickness. Nature. 2010;464(7289):728-732. doi:10.1038/nature08893. PMID: 20360736.
2. Brand S, Cleghorn LAT, McElroy SP, Robinson DA, Smith VC, Hallyburton I, Harrison JR, Norcross NR, Spinks D, Bayliss T, Norval S, Stojanovski L, Torrie LS, Frearson JA, Brenk R, Fairlamb AH, Ferguson MAJ, Read KD, Wyatt PG, Gilbert IH. Discovery of a novel class of orally active trypanocidal N-myristoyltransferase inhibitors. J Med Chem. 2012;55(1):140-152. doi:10.1021/jm201091t.
3. Robinson DA, Wyatt PG. Identification and structure solution of fragment hits against kinetoplastid N-myristoyltransferase. Acta Crystallogr F Struct Biol Commun. 2015;71(Pt 5):586-593. doi:10.1107/S2053230X15003040.
4. World Health Organization. Trypanosomiasis, human African (sleeping sickness). Fact sheet. Geneva: WHO.
5. Kagbadouno M, et al. Elimination of gambiense human African trypanosomiasis as a public health problem in Republic of Guinea: paving the way for zero transmission. PLoS Negl Trop Dis. 2026.
6. Hunting down the last cases of sleeping sickness. Horizon: The EU Research & Innovation Magazine. 2026. (471 cases reported worldwide in 2025; acoziborole 98.1% efficacy; EMA positive scientific opinion, 2026.)
7. ChEMBL target CHEMBL3988596: glycylpeptide N-tetradecanoyltransferase, Trypanosoma brucei brucei (strain 927/4 GUTat10.1), single protein. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-18.
8. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; no trypanosomiasis discussion — the disease lies outside the canon's clinical geography.)
9. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; no trypanosomiasis discussion.)

## Data availability

No docking was performed: no Trypanosoma brucei NMT structure exists in the PDB (verified 2026-11-18; RCSB full-text search returns only Leishmania major NMT, 5AG4–5AG7 and 5AGE, and Aspergillus fumigatus NMT, 4UWI–4UWJ). All compound data reported here are in `hidden_files/dock-HP-068-2026-11-18.json`. Ligand identities are ChEMBL IDs CHEMBL1230468 (DDD85646), CHEMBL4115085, CHEMBL4111551, CHEMBL3357685, CHEMBL4112331; reference drug DDD85646, PubChem CID 44199337. Target: UniProtKB Q388H8; ChEMBL target CHEMBL3988596. No additional data were generated.
