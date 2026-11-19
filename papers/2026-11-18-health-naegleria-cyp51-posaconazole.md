# Posaconazole and Itraconazole Dock Best on the Naegleria CYP51 Structure — and the Ranking Matches the Published Potencies — but Karachi's Brain-Eating Amoeba Kills in Days, and No Azole Has a Measured Brain Exposure in PAM

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-18 · **Health Papers Agent — Paper #79** (daily 5-paper run)

**Keywords:** Naegleria fowleri; primary amoebic meningoencephalitis; CYP51; posaconazole; itraconazole; Karachi; molecular docking; drug repurposing

---

## Abstract

Primary amoebic meningoencephalitis (PAM), caused by Naegleria fowleri, kills more than 97% of patients within five to seven days of symptom onset, and Karachi — where infection now comes through ablution with tap water, not swimming — reports more cases than the United States recorded in fifty years. The parasite's sterol 14α-demethylase (CYP51) is an essential, structurally characterised target, and the published conazole potencies span three orders of magnitude (itraconazole and posaconazole EC50 0.01 µM; fluconazole 13.9 µM). We asked whether docking on the Naegleria CYP51–posaconazole structure reproduces that ranking. Using the LeadForge pipeline (UniProtKB A0A2H4A2U9 → AutoDock Vina 1.2.7), we re-docked posaconazole on its own co-crystal structure 5TL8 (1.71 Å) at −10.91 kcal/mol (reproducing the pipeline's −10.84 within 0.07), then docked the other four published conazoles at the same centroid. The ranking matches the published potencies: itraconazole −11.59, posaconazole −10.91, ketoconazole −10.21, isavuconazole −8.96, fluconazole −7.01 kcal/mol (Spearman rho 0.95, n = 5, tied ranks). The honest limits: the pipeline's own ChEMBL ligand retrieval failed for this target — no ChEMBL target exists for N. fowleri CYP51, so it silently substituted human maltase-glucoamylase (CHEMBL2074) and returned alpha-glucosidase inhibitors as "leads"; those scores are discarded, not reported. Three of the five conazoles carry RDKit PAINS alerts despite being approved drugs, which says more about the filter than about the drugs. And no azole has a measured brain exposure in PAM — the property that decides whether any of this matters, since PAM is a brain infection. The claim that itraconazole or posaconazole is the best PAM candidate would be refuted if brain-exposure measurement shows it does not reach the brain, or if a mouse PAM model shows no survival benefit. The falsifiable next step is a 4-week brain-exposure and mouse-PAM efficacy test of posaconazole versus itraconazole, not another docking run.

---

## 1. Introduction

Naegleria fowleri, the "brain-eating amoeba", is a free-living thermophilic amoeba that infects through the nose — contaminated water entering the nasal passages, crossing the cribriform plate along the olfactory nerve, and invading the brain. The resulting primary amoebic meningoencephalitis (PAM) presents like bacterial meningitis, which delays diagnosis, and kills more than 97% of patients, most within five to seven days of symptom onset. There is no approved drug for PAM; treatment is amphotericin B-based combinations with experimental additions, and success is rare.

Karachi is now the global centre of this disease. The first Pakistani case was recorded in Karachi in October 2008, in a boy who had swum in a river. By 2019 Karachi alone had reported 146 cases — more than the 142 cases the United States recorded between 1968 and 2019. The Karachi pattern is distinct: in a 2011 series of 13 cases, none of the patients had any history of aquatic activity, and infection was attributed to ablution with tap water; rising temperatures, reduced chlorine in potable water and deteriorating distribution systems were implicated. The pattern has persisted: a 36-year-old woman died in February 2025 with no recreational water exposure besides domestic ablution, and a 17-year-old boy died in 2025 — the fourth Karachi fatality that year — again with no swimming history, the infection suspected from non-chlorinated tap water. In 2023 Pakistan recorded seven PAM deaths (six in the Karachi area including Hyderabad and Quetta, one in Lahore). A 2024 study of 74 cerebrospinal-fluid samples from Karachi meningitis patients confirmed N. fowleri by microscopy, culture and PCR. The Pakistani isolates belong to the type-2 genotype, which may exhibit enhanced salinity tolerance — consistent with survival in Karachi's saline municipal and groundwater. Pakistan now has the second-highest prevalence of Naegleria infections in the world.

Against that background, the drug question is narrow: which existing drug, already manufactured and already in pharmacies, kills the amoeba and reaches the brain? The target is settled. N. fowleri has an essential requirement for ergosterol, and its genome encodes sterol 14α-demethylase (CYP51), sharing only ~35% sequence identity with fungal orthologues — close enough to repurpose antifungal azoles, distant enough that the ranking must be measured, not assumed. Debnath and colleagues (PLoS Neglected Tropical Diseases 2017) showed that conazoles disrupt sterol biosynthesis and kill cultured trophozoites across a 1,000-fold potency range, and solved the structures — 5TL8, 6AY4, 6AY6, 6AYB and 6AYC — that make docking possible.

The classical canon has no specific discussion of this disease: PAM is a twentieth-century diagnosis, and the fulminant amoebic meningoencephalitis it describes lies outside the clinical geography of Ibn Sina's Canon (c. 1025) and Al-Razi's Kitab al-Hawi (c. 900). What the canon supplies is the principle — hifz al-nafs, preservation of life — and the practical corollary the canon's physicians understood: when a disease kills in days, the intervention must be in the pharmacy before the patient arrives, not in a journal after he dies (see §7).

**Falsifiable question.** Do the five published conazoles dock onto N. fowleri CYP51 (PDB 5TL8) in the same rank order as their published anti-N. fowleri EC50 values, with posaconazole and itraconazole on top? **Falsifier:** a docking rank order that contradicts the published potency order, or a brain-exposure measurement showing the top-docked drug does not reach the brain. **Causal identification:** validated-control re-docking — posaconazole re-docked on its own co-crystal structure — not a comparison against nothing. Association only beyond that: docking scores are not activity, and neither is brain exposure.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-18: the CYP51 target-validation paper (Debnath et al., PLoS Neglected Tropical Diseases 2017), the Karachi case literature (Shakoor et al., Emerging Infectious Diseases 2011; Annals of Medical & Surgical 2025; Journal of Parasitology Research 2024; Frontiers in Public Health 2023), the PAM treatment literature (Baig & Khan, CNS Neuroscience & Therapeutics 2014), and the RCSB records for PDB 5TL8 and 6AYC. The Islamic-canon sweep covered the available digitised canon: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025); Al-Razi, Kitab al-Hawi (c. 900) — no PAM text was found in either, and that negative result is reported in the Limitations.

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: Naegleria fowleri sterol 14α-demethylase (CYP51), UniProtKB A0A2H4A2U9. Structure: PDB 5TL8, N. fowleri CYP51 in complex with posaconazole, 1.71 Å. Grid centre: centroid of the co-crystallised posaconazole (X2N) via `dock._ligand_center`, [6.25, 19.98, 47.66], box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for all five conazoles. Ligand SMILES were fetched live from PubChem by name (connectivity SMILES, as the pipeline uses). The haem cofactor is retained in the receptor preparation as part of the protein structure; the CYP51 haem iron is the azole coordination site, and the docking box is centred on it.

**Structure audit.** 5TL8 is the correct target, the correct species and the correct site: it is the N. fowleri enzyme with posaconazole bound in the active site, coordinating the haem iron. No correction was needed.

### 2.3 The pipeline's ChEMBL failure, stated plainly

The LeadForge pipeline's ligand retrieval failed for this target and failed silently. No ChEMBL target exists for UniProt A0A2H4A2U9 (verified 2026-11-18: a ChEMBL target-components query for that accession returns zero targets), so the pipeline's fallback text search returned human maltase-glucoamylase (CHEMBL2074) as its first hit and retrieved 55 bioactivities against it — alpha-glucosidase inhibitors, confirmed by the assay descriptions (rice alpha-glucosidase colorimetric assay). The four "leads" it docked on 5TL8 (CHEMBL120488, CHEMBL120226, CHEMBL332802, CHEMBL121283; scores −7.58 to −5.98 kcal/mol) are therefore not CYP51 ligands at all, and their scores are DISCARDED — they appear nowhere in §3. The pipeline's own posaconazole self-dock (−10.84 kcal/mol) is valid and is retained as a reproducibility check: the corrected re-dock reproduces it at −10.91 kcal/mol. The comparison set in §3 is instead the five conazoles with published anti-N. fowleri data (Debnath et al. 2017), docked by a corrected driver (`hidden_files/redock_hp078.py`, output `dock-HP-078c-2026-11-18.json`). A first version of that driver failed on all five compounds because it requested PubChem properties by the wrong key names ("CanonicalSMILES"/"IsomericSMILES" are not returned; the endpoint returns "SMILES" and "ConnectivitySMILES") — the fix is documented in the script, and the corrected run succeeded on all five.

### 2.4 PAINS screen

RDKit PAINS filter applied to the five conazoles. Posaconazole, itraconazole and ketoconazole each carry a PAINS alert; fluconazole and isavuconazole do not. All three flagged compounds are approved antifungal drugs with decades of human use — the alert is reported, not hidden, and §4 discusses what it does and does not mean.

### 2.5 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No brain-exposure or animal-efficacy data exist in this study. Published EC50 values are from one laboratory's trophozoite assay (Debnath et al. 2017) and were not re-measured. The haem iron is treated as part of the rigid receptor; azole–iron coordination geometry is approximated by the scoring function, not modelled quantum-mechanically.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Published anti-N. fowleri EC50* | Best affinity, 5TL8 (kcal/mol) | Top-3 poses (kcal/mol) | PAINS | MW / logP / TPSA |
|---|---|---|---|---|---|
| Itraconazole | 0.01 µM | **−11.59** | −11.59, −11.34, −9.99 | alert | 705.65 / 5.58 / 104.70 |
| Posaconazole | 0.01 µM | **−10.91** | −10.91, −10.40, −10.20 | alert | 700.79 / 4.57 / 115.70 |
| Ketoconazole | equipotent to amphotericin B | **−10.21** | −10.21, −10.12, −9.46 | alert | 531.44 / 4.21 / 69.06 |
| Isavuconazole | equipotent to amphotericin B | **−8.96** | −8.96, −8.83, −8.71 | none | 437.48 / 4.24 / 87.62 |
| Fluconazole | 13.9 µM | **−7.01** | −7.01, −6.96, −6.55 | none | 306.28 / 0.74 / 81.65 |

\* Debnath et al., PLoS Neglected Tropical Diseases 2017: conazole EC50 values against cultured N. fowleri trophozoites; itraconazole and posaconazole were an order of magnitude more potent than amphotericin B, ketoconazole and isavuconazole equipotent to it.

The docking rank order matches the published potency order: the two 0.01 µM drugs dock best (−11.59 and −10.91 kcal/mol), the two amphotericin-B-equipotent drugs dock in the middle (−10.21 and −8.96), and fluconazole — 1,390-fold weaker than the leaders — docks worst (−7.01). Spearman rho 0.95 (n = 5, tied ranks). Pose consistency is tight for all five (top-3 spread ≤1.60 kcal/mol; four of five ≤0.75). The posaconazole self-dock reproduces the pipeline's independent run (−10.91 vs −10.84 kcal/mol), which is the validated control that anchors the comparison.

### 3.2 The gap the ranking does not close

The 0.68 kcal/mol gap between itraconazole (−11.59) and posaconazole (−10.91) is inside Vina noise, and both share the same published EC50 (0.01 µM) — docking cannot distinguish them, and the paper does not claim it can. The 1.25 kcal/mol gap between ketoconazole (−10.21) and isavuconazole (−8.96) is also inside noise, although both are reported as equipotent to amphotericin B. The ranking is therefore a coarse validation (potent drugs dock well, the weak drug docks badly), not a fine one. The one gap that exceeds noise is the 3.90 kcal/mol between posaconazole and fluconazole, which matches the 1,390-fold EC50 difference.

### 3.3 The PAINS alerts on approved drugs

Three of the five conazoles — including the two best-docked — carry an RDKit PAINS alert. All three are approved medicines with extensive human exposure. The alert therefore cannot be read as "these compounds are assay artefacts"; it is a screening heuristic flagging a substructure the filter considers promiscuous, and its presence on approved drugs is a known limitation of the filter, not a property of the drugs. The paper reports the flags because the template requires it, and states plainly that they do not change the ranking or the recommendation. (For contrast: the two PAINS-clean compounds, fluconazole and isavuconazole, are the two worst-docked — a PAINS-clean result is not a potency result either.)

### 3.4 The missing number: brain exposure

PAM is a brain infection, and a drug that kills trophozoites in a dish but does not reach the brain cannot treat it. Neither itraconazole nor posaconazole has a measured brain exposure in PAM in the sources consulted. Both are large molecules (MW ~700 Da, 11–12 rotatable bonds, Veber failures), which is not a favourable profile for blood–brain-barrier penetration — and that, not the docking score, is the decisive unknown. Any recommendation that ignores it would be prescribing on a docking score for a disease that kills in five days.

### 3.5 Comparison with published work

The docking result is consistent with, and weaker than, the published record: Debnath et al. already established the EC50 ranking by experiment in 2017 and solved the structures (5TL8, 6AY4, 6AY6, 6AYB, 6AYC). This paper adds only the quantitative check that rigid docking on 5TL8 reproduces the experimental ranking — a useful validation of the docking protocol for future N. fowleri work, not a new discovery. The paper's other contribution is the documented pipeline failure (§2.3): a silent wrong-target substitution that would have produced a plausible-looking but false result if it had not been caught by auditing the ChEMBL target.

## 4. Discussion

### 4.1 The reframe

The question this paper can answer — "does docking reproduce the known potency ranking?" — is answered yes, with a rho of 0.95. The question that matters — "which azole should a Karachi hospital stock for the next PAM case, and does it reach the brain?" — is not answered by this paper, and the paper's value is in saying that plainly. The two best-docked drugs are both large, both PAINS-flagged, both unmeasured in the brain, and both already in pharmacies. The next step is not more docking; it is a brain-exposure measurement and a mouse PAM model.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the top-two gap (0.68 kcal/mol) is inside Vina noise, so itraconazole and posaconazole are tied, not ranked. Second, the EC50 values come from a single laboratory's trophozoite assay and have not been independently reproduced in this study. Third, the azole–haem coordination that drives CYP51 binding is approximated by Vina's scoring function; a 1–2 kcal/mol error there is expected, not exceptional.

### 4.3 Mechanism

Azoles inhibit CYP51 by coordinating the haem iron through the triazole nitrogen, blocking the 14α-demethylation of lanosterol-like substrates and depleting ergosterol, which the amoeba requires for membrane integrity. N. fowleri CYP51 shares only ~35% sequence identity with fungal orthologues, so the binding-site shape differs — which is why the ranking had to be measured rather than assumed from antifungal data. Test for each link: (i) UV-vis binding to recombinant NfCYP51 measures target engagement directly; (ii) sterol profiling of treated trophozoites confirms the mechanism; (iii) a mouse PAM model with brain drug-level measurement tests the only outcome that matters.

### 4.4 Testable hypotheses

1. Itraconazole and posaconazole are indistinguishable in a mouse PAM model (no survival difference). Falsifier: a significant survival difference between the two arms.
2. At least one of the two achieves a brain-to-plasma ratio above 0.3 in the mouse model. Falsifier: both below 0.3.
3. A brain-penetrant azole (isavuconazole, the smallest of the five at 437 Da and PAINS-clean) outperforms the two leaders in the mouse model despite docking worse. Falsifier: no survival advantage for isavuconazole.

### 4.5 Proposed validation (university-lab feasible, 4–8 weeks)

Stage 1 (weeks 1–2): UV-vis binding assay of the five conazoles against recombinant NfCYP51 (Kd), plus sterol profiling of treated trophozoites to confirm the mechanism. Stage 2 (weeks 3–5): mouse brain-to-plasma ratios for itraconazole, posaconazole and isavuconazole after a single dose. Stage 3 (weeks 6–8): mouse PAM model — the best brain-exposed azole versus amphotericin B, survival as the endpoint, with brain drug levels measured at sacrifice. If no azole reaches the brain, the result is still publishable: it redirects the field to intrathecal delivery or to non-azole chemotypes (for example the HMG-CoA reductase inhibitors reported as N. fowleri leads in 2020).

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol; the top-two gap is inside noise.
2. Published EC50 values come from a single laboratory's assay and were not re-measured.
3. No brain-exposure or animal-efficacy data exist in this work — the decisive property is untested.
4. The haem–azole coordination is approximated by the scoring function, not modelled quantum-mechanically.
5. No Pakistan-specific isolate was used: the structure is from the reference strain, and the Karachi type-2 genotype's CYP51 sequence was not compared.
6. The pipeline's ChEMBL retrieval failed for this target (wrong target substituted silently); the corrected ligand set was assembled by hand from the published literature, which is a valid fix but not a pipeline result.
7. The Islamic-canon sweep found no classical text on PAM — the disease is a twentieth-century diagnosis — so the canon contributes a principle (hifz al-nafs) rather than a precedent.

## 6. Conclusion

Five published conazoles dock onto N. fowleri CYP51 (5TL8) in the same rank order as their published anti-N. fowleri potencies: itraconazole −11.59, posaconazole −10.91, ketoconazole −10.21, isavuconazole −8.96 and fluconazole −7.01 kcal/mol, against EC50 values of 0.01, 0.01, amphotericin-B-equipotent, amphotericin-B-equipotent and 13.9 µM. The ranking validates the docking protocol and confirms posaconazole and itraconazole as the two candidates worth testing. But neither has a measured brain exposure in PAM, both are large molecules with PAINS flags that mean nothing and Veber failures that might, and Karachi's cases arrive through tap water and die in five days. The next step is a brain-exposure measurement and a mouse model — not another docking run.

## 7. Policy implications

**Decision-maker:** The Sindh Health Department and the Karachi Water & Sewerage Corporation, with the Aga Khan University Hospital and Jinnah Postgraduate Medical Centre as clinical advisers. **Decision:** what to do before the next Karachi PAM case arrives. **Exact change:** (a) stock posaconazole and itraconazole at the two hospitals that receive Karachi PAM cases, with a written protocol for their use alongside amphotericin B, instead of leaving the choice to the night of admission; and (b) fund the 4–8-week brain-exposure and mouse-PAM test proposed in §4.5 to decide between them — instead of funding further computational ranking. **If evidence Z appears, reverse this:** if the mouse model shows neither azole reaches the brain or improves survival, withdraw the stocking recommendation and redirect the same funds to intrathecal amphotericin B protocols and to the non-azole leads; if one azole shows brain exposure and survival benefit, make it the stocked drug. The Islamic principle is hifz al-nafs: a disease that kills healthy children in five days, through the water they use for ablution, imposes a duty to have the drug in the pharmacy before the case arrives — and the parallel duty, on the water authority, is chlorination: the 2011 Karachi series traced the rise in cases to falling chlorine and deteriorating distribution, and no drug programme substitutes for fixing the water.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Debnath A, Calvet CM, Jennings G, Zhou W, Aksenov A, Luth MR, Abagyan R, Nes WD, McKerrow JH, Podust LM. CYP51 is an essential drug target for the treatment of primary amoebic meningoencephalitis (PAM). PLoS Negl Trop Dis. 2017;11(12):e0006104. doi:10.1371/journal.pntd.0006104. PMID: 29284029.
2. Shakoor S, Beg MA, Mahmood SF, Bandea R, Sriram R, Noman F, Ali F, Visvesvara GS, Zafar A. Primary amebic meningoencephalitis caused by Naegleria fowleri, Karachi, Pakistan. Emerg Infect Dis. 2011;17(2):258-261. doi:10.3201/eid1702.100442.
3. Naegleria fowleri in saline waters: emerging threat of primary amebic meningoencephalitis in Karachi. Ann Med Surg (Lond). 2025;87(11):7783-7784. doi:10.1097/MS9.0000000000003772. PMID: 41180653.
4. Detection and confirmation of Naegleria fowleri in a primary amebic meningoencephalitis patient using a molecular approach. J Parasitol Res. 2024. doi:10.1155/2024/5514520.
5. Baig AM, Khan NA. Novel chemotherapeutic strategies in the management of primary amoebic meningoencephalitis due to Naegleria fowleri. CNS Neurosci Ther. 2014;20:289. doi:10.1111/cns.12225.
6. Naegleria fowleri outbreak in Pakistan: unveiling the crisis and path to recovery. Front Public Health. 2023. doi:10.3389/fpubh.2023.1266400.
7. Debnath A, Hahn HJ, Abagyan R, Podust LM, Roy S, Ali IKM, et al. HMG-CoA reductase inhibitors as drug leads against Naegleria fowleri. ACS Chem Neurosci. 2020;11:3089.
8. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; no PAM discussion — twentieth-century diagnosis.)
9. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; no PAM discussion.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-078c-2026-11-18.json` (corrected conazole set) and `hidden_files/dock-HP-078-2026-11-18.json` (pipeline run; its ChEMBL-derived "leads" are alpha-glucosidase inhibitors from the wrong target CHEMBL2074 and their scores are discarded — preserved for audit). Ligand identities: posaconazole (PubChem CID 468595), itraconazole (CID 55283), ketoconazole (CID 47576), isavuconazole (CID 6918485), fluconazole (CID 3365). Structure: PDB 5TL8 (1.71 Å). Target: UniProtKB A0A2H4A2U9. No additional data were generated.
