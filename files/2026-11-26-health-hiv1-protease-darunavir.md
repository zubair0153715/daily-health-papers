# Docking Cannot Rank HIV-1 Protease Inhibitors: Saquinavir Leads Darunavir by 0.91 kcal/mol on the Wild Type, but Darunavir Ranks Last on Its Own Structure and I50V Costs It Only 0.31 kcal/mol

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-26 · **Health Papers Agent — Paper #120** (daily 5-paper run)

**Keywords:** HIV-1 protease; darunavir; protease inhibitors; drug resistance; molecular docking; AutoDock Vina; Pakistan

---

## Abstract

Pakistan's HIV epidemic is growing fast — new infections rose from 16,000 in 2010 to 48,000 in 2024, yet only 21% of people living with HIV know their status — and darunavir, the protease inhibitor with the highest genetic barrier, loses affinity to the I50V and I84V mutations. Five approved protease inhibitors — darunavir, lopinavir, atazanavir, saquinavir and tipranavir — were docked with standardised AutoDock Vina on the wild-type HIV-1 protease structure 4LL3 (1.95 Å) and the I50V mutant structure 6DH6 (1.97 Å), same box and exhaustiveness, with darunavir as the self-dock control on both. On the wild type saquinavir scored best at −10.74 kcal/mol, 0.91 kcal/mol better than darunavir at −9.83, but that lead is inside Vina's ±1–2 kcal/mol noise, so no inhibitor beats darunavir beyond noise. The method then failed its own controls: darunavir — the best inhibitor by published Ki (<5 pM) — scored worst of the five on its own wild-type structure, and the I50V mutation cost it only 0.31 kcal/mol by docking against a published 15-fold Ki loss. Docking therefore cannot rank protease inhibitors or resolve the resistance it was designed to study, and no regimen change follows from these scores. Pose consistency was tight on the wild type (three-pose spread 0.09–0.25 kcal/mol) and on the mutant for four compounds; lopinavir's mutant score rests on a single pose, its other two poses being about 1 kcal/mol worse, so its rank on the mutant is not converged. The falsifier is a FRET-based enzyme inhibition assay: if saquinavir's Ki is not better than darunavir's on the same plate, the docking lead is a pocket artefact.

---

## 1. Introduction

Pakistan has one of the fastest-growing HIV epidemics in the WHO Eastern Mediterranean Region: new infections rose 200% in 15 years, from 16,000 in 2010 to 48,000 in 2024, and an estimated 350,000 people are living with HIV — but only 21% know their status, 16% are on antiretroviral therapy and 7% have achieved viral suppression (WHO/UNAIDS, World AIDS Day 1 December 2025). Treatment has expanded eightfold (6,500 on ART in 2013 to 55,500 in 2024; centres from 13 to 95), yet the gap is still a diagnosis gap first and a drug gap second — and Larkana, the author's own city, was the site of the 2019 outbreak in which children were infected through unsafe injections. The protease inhibitors that anchor second-line therapy all bind the same target — HIV-1 protease, a 99-amino-acid homodimeric aspartyl protease (UniProt P03366) whose Asp25/Asp25' catalytic dyad cleaves the Gag-Pol polyprotein — and all of them lose potency to the same mutations. Darunavir (FDA 2006), the most potent protease inhibitor in the clinic, was designed to fit within the substrate envelope and to hydrogen-bond the protease backbone rather than its mutable side chains: its dissociation constant is 4.5 pM, its Ki against wild-type protease is below 5 pM, and it takes three or more darunavir resistance-associated mutations (RAMs) for a significant fold change in susceptibility. Resistance still arrives — I50V and I84V are the two primary S1/S1' pocket mutations — and the question this paper attacks is whether the older protease inhibitors, or any new scaffold, can match darunavir on the wild-type enzyme and on the mutant that beats it.

**Falsifiable question.** Does any approved protease inhibitor out-score darunavir on the wild-type HIV-1 protease structure 4LL3 by more than Vina's ±1–2 kcal/mol noise, and does any of them hold its score on the I50V mutant structure (6DH6) where darunavir loses affinity? The I84V structure (6DH0) was not docked in this run and its resistance is carried by the published Ki alone (see §2.3). **Falsifier:** an enzyme inhibition assay showing the winner's Ki not better than darunavir's (<5 pM wild-type, 25.6 pM I84V, 74.5 pM I50V/A71V; Lockbaum et al. 2019), or a viral replication assay showing no better EC50. **Causal identification:** validated-control re-docking — darunavir re-docked on its own wild-type co-crystal (4LL3) and on its own mutant co-crystal (6DH6) as the controls, four other protease inhibitors docked on the same two structures with the same box and exhaustiveness — association only beyond that, since docking scores are not Ki and not viral suppression.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-26: the WHO/UNAIDS Pakistan HIV figures (World AIDS Day 1 December 2025; UNAIDS Fact Sheet 2024 — 350,000 PLHIV, 48,000 new infections in 2024, 21%/16%/7% cascade); the darunavir analogue structural study (Lockbaum et al., ACS Infect Dis 2019;5:316–325, PMID 30543749, DOI 10.1021/acsinfecdis.8b00336 — 12 structures including 6DH0 I84V and 6DH6 I50V; Ki WT <5.0 pM, I84V 25.6 ± 5.6 pM, I50V/A71V 74.5 ± 5.6 pM; EC50 WT 7.7 ± 1.6 nM); the wild-type darunavir structure paper (Kozisek et al., FEBS J 2014;281:1834 — 4LL3, 1.95 Å); the compiled Ki/EC50 table for approved protease inhibitors ("Molecular basis for drug resistance in HIV-1 protease", review); and the darunavir resistance-mutation set (11 IAS-USA-listed DRV RAMs including V11I, V32I, L33F, I47V, I50V, I54L/M, G73S, L76V, I84V). The classical-canon sweep: Ibn Sina's Canon and Al-Razi's Kitab al-Hawi describe epidemic disease and its spread without a virus concept; the principle carried is hifz al-nafs, sharpened by the Larkana outbreak's lesson — unsafe injection practice as a transmission route that no drug can fix.

### 2.2 Target identification — and the pipeline's empty ligand set

The pipeline resolved the target correctly: UniProtKB P03366 (HIV-1 protease, group M subtype B, isolate BH10) → ChEMBL lookup returned only the QUERY (darunavir) and no other ligands — the ChEMBL target mapping for this viral enzyme returned a single compound, so no ChEMBL-derived ligand set exists in this study. The comparison set was therefore built from the literature: the four other protease inhibitors with the strongest published wild-type data, with SMILES verified live against PubChem by name and CID (darunavir CID 213039; lopinavir CID 92727; atazanavir CID 148192; saquinavir CID 441243; tipranavir CID 54682461). The pipeline's single-lead result is stated, not hidden: it is a retrieval failure, not a finding that darunavir has no competitors.

### 2.3 Molecular docking

Standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: box 22.5 Å, exhaustiveness 8, best of 3 poses reported. Two structures were docked, both darunavir-bound: 4LL3, the 1.95 Å wild-type HIV-1 protease in complex with darunavir (Kozisek et al., FEBS J 2014;281:1834); and 6DH6, the 1.97 Å I50V mutant in complex with darunavir (Lockbaum et al., ACS Infect Dis 2019;5:316–325). Grid centre on each structure is the centroid of its co-crystallised darunavir, verified by direct computation from the PDB file with `dock._ligand_center`. Darunavir is therefore the self-dock control on both structures: a method that could not recover binding for the drug in its own pocket would be broken — and §3.1 shows what happened. The same five compounds, the same box and exhaustiveness, on both structures. The third structure, 6DH0 (the 1.90 Å I84V mutant in complex with darunavir, Lockbaum et al. 2019), was not docked: the run was stopped to save compute time and its resistance is carried by the published Ki (25.6 ± 5.6 pM) alone, stated in §3.1. Two caveats, stated not smoothed over: each mutant pocket is in darunavir's own conformation, so it favours darunavir over the other four inhibitors; and the I50V structure (6DH6) is the single I50V mutant while the published Ki for the double mutant is I50V/A71V (74.5 pM), so the docking and the Ki are not on identical proteins.

### 2.4 PAINS screen

RDKit PAINS filter applied to all five compounds. All five are PAINS-clean: darunavir, lopinavir, atazanavir, saquinavir and tipranavir carry no PAINS alert. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.5 ADMET and toxicity read-across

RDKit descriptors computed for all five compounds (molecular weight, logP, H-bond donors/acceptors, TPSA, rotatable bonds, Lipinski violations). No ToxGuard read-across is reported for this set: the pipeline's Tox21 panel ran on the single QUERY only, and a single-compound read-across is not safety data; it is omitted rather than presented.

### 2.6 Honesty limits

Docking ≠ Ki. Vina noise is ±1–2 kcal/mol, and the Ki differences that matter here are picomolar — a 5-fold Ki difference is ~1 kcal/mol of binding free energy, inside the noise — so this docking can rank scaffolds but cannot resolve the resistance it was designed to study; the published Ki values (Lockbaum et al. 2019) carry that claim, not this computation. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond their published Ki/EC50 values and the published structures. The mutant pockets are in darunavir's conformation. Vina's rigid, water-free scoring cannot see the flap dynamics, the catalytic water, or the substrate-envelope fit that actually decides whether an inhibitor survives a mutation. Tipranavir's published EC50 (500 nM) is far worse than its Ki (0.088 nM) because of plasma protein binding — a reminder that enzyme potency is not antiviral potency, and neither is a docking score.

## 3. Results

### 3.1 Docking: the comparison tables

**Wild-type HIV-1 protease (4LL3)**

| Compound | Best affinity (kcal/mol) | Poses (kcal/mol) | Published Ki (nM) | PAINS |
|---|---|---|---|---|
| Saquinavir | −10.74 | −10.74, −10.73, −10.50 | 0.065 | Clean |
| Lopinavir | −10.27 | −10.27, −10.14, −10.14 | 0.005 | Clean |
| Atazanavir | −10.13 | −10.13, −9.97, −9.88 | 0.046 | Clean |
| Tipranavir | −9.94 | −9.94, −9.86, −9.85 | 0.088 | Clean |
| Darunavir (reference, self-dock control) | −9.83 | −9.83, −9.72, −9.65 | <0.005 | Clean |

**I50V mutant HIV-1 protease (6DH6)**

| Compound | Best affinity (kcal/mol) | Poses (kcal/mol) | WT → I50V shift (kcal/mol) | PAINS |
|---|---|---|---|---|
| Saquinavir | −10.71 | −10.71, −10.60, −10.29 | +0.03 | Clean |
| Tipranavir | −10.35 | −10.35, −10.33, −10.10 | −0.41 | Clean |
| Lopinavir | −10.15 | −10.15, −9.17, −9.04 | +0.12 | Clean |
| Atazanavir | −10.06 | −10.06, −9.86, −9.85 | +0.07 | Clean |
| Darunavir (reference, self-dock control) | −9.52 | −9.52, −9.27, −9.03 | +0.31 | Clean |

Pose consistency is tight on the wild type (three-pose spread 0.09–0.25 kcal/mol for every compound), so the ranking is not a pose-sampling artefact. On the mutant it is tight for four compounds (spread 0.21–0.49) and wide for one: lopinavir's poses on 6DH6 spread 1.11 kcal/mol (−10.15, −9.17, −9.04), so its −10.15 is a single-pose result, not a converged binding mode, and its rank on the mutant should be read as no better than its second pose (−9.17). The ranking itself is the problem. On the wild type, saquinavir leads darunavir by 0.91 kcal/mol, lopinavir by 0.44, atazanavir by 0.30 — all three inside Vina's ±1–2 kcal/mol noise, so no compound beats darunavir beyond noise. Worse, the ranking inverts the published Ki order almost completely: by Ki the order is darunavir ≈ lopinavir (5 pM) > atazanavir (46 pM) > saquinavir (65 pM) > tipranavir (88 pM), while by docking it is saquinavir > lopinavir > atazanavir > tipranavir > darunavir — darunavir, the best inhibitor by Ki and the co-crystallised ligand in this very structure, scores worst of the five. The I50V comparison is no better. The published Ki says I50V/A71V costs darunavir 15-fold (74.5 vs <5 pM, ~1.6 kcal/mol of binding free energy); the docking says it costs 0.31 kcal/mol. Every compound's wild-type-to-mutant shift is inside noise (darunavir +0.31, lopinavir +0.12, atazanavir +0.07, saquinavir +0.03), and tipranavir apparently *improves* on the mutant by 0.41 kcal/mol — a result with no published support and no plausible mechanism, which is what noise looks like. The I84V mutation was not docked (see §2.3); its published cost to darunavir is 25.6 ± 5.6 pM, a 5-fold loss that the docking, by the I50V evidence, would not have resolved either.

### 3.2 Comparison with published docking

No published docking study of protease inhibitors on 4LL3 or 6DH6 was found in the searches for this paper, so there is no published docking table to compare against. The comparison that exists is against the published Ki values (Lockbaum et al. 2019; compiled review table), and it is reported in §3.1 in full — including the inversion, not just the agreements. One assay-variation note: the review compilation lists darunavir's Ki as 15 pM against Lockbaum's <5 pM — a 3-fold spread between published values for the same compound, which is itself larger than most of the docking margins in this paper.

### 3.3 The standardisation / quality problem: enzyme potency is not antiviral potency

The comparison that matters clinically is not Ki against Ki. Tipranavir's Ki is 0.088 nM — second-best in the set by enzyme potency — but its EC50 is 500 nM, the worst in the set by a factor of 50, because of plasma protein binding. Lopinavir's Ki is 0.005 nM, joint-best, but it is dosed with ritonavir boosting because its pharmacokinetics alone are poor. Darunavir's advantage is not its Ki — lopinavir matches it — but its genetic barrier: three or more RAMs for a significant fold change, against one or two for the older inhibitors. A docking table that ranks saquinavir first has ranked the wrong property, and any regimen decision built on it would be built on a category error.

## 4. Discussion

### 4.1 The reframe: the question changes from "which inhibitor?" to "can docking rank inhibitors at all?"

The paper set out to find whether any protease inhibitor beats darunavir on the wild-type enzyme and holds its score on the mutants. The answer is no — not because darunavir is unbeatable (its Ki is matched by lopinavir and its resistance mutations are real), but because the method cannot tell. Saquinavir's 0.91 kcal/mol lead is a real number and a non-result at the same time: it is inside the noise bar, and the control that would have validated it — darunavir on its own structure — scored worst of the five. The I50V comparison then fails the same way: a published 15-fold Ki loss appears as 0.31 kcal/mol, and one compound apparently improves on the mutant. The question therefore changes: the finding is not "saquinavir wins" but "Vina on single protease structures cannot rank a congeneric series whose published Ki values span only ~18-fold, and cannot resolve a 15-fold resistance effect". That is a useful negative, and it is the paper's actual contribution — it stops a regimen switch that the raw table, read naively, would seem to support.

### 4.2 Why the "win" must not be over-read

Four reasons. First, the margin: 0.91 kcal/mol against a ±1–2 kcal/mol noise bar is not a lead, it is a tie with a sign. Second, the self-dock control: darunavir last of five on its own wild-type structure means the pocket conformation, not the compounds, is doing part of the ranking. Third, the mutant comparison: a 15-fold published Ki loss appearing as 0.31 kcal/mol, and tipranavir improving on the mutant, means the docking is blind to the S1/S1' pocket changes that actually decide resistance. Fourth, the missing pharmacology: Ki is not EC50, and the property that separates darunavir from the older inhibitors — the genetic barrier, three or more RAMs — is not in this computation at all. Any one of these would be enough to withhold a claim; together they close it.

### 4.3 Mechanism

HIV-1 protease is a homodimer; each 99-residue monomer contributes one catalytic aspartate (Asp25/Asp25') to the active site, and two flexible flaps close over the substrate. Darunavir's bis-tetrahydrofuran (bis-THF) moiety makes a network of hydrogen bonds to the backbone atoms of Asp29 and Asp30 — backbone, not side chains — which is why mutations at those positions cost it less than they cost the peptidomimetic inhibitors: the virus cannot mutate its backbone. The same design logic puts darunavir inside the substrate envelope, the consensus volume that the protease's natural substrates occupy, so any mutation that pushes darunavir out also pushes the substrate out and costs the virus fitness. The two primary resistance mutations attack the S1/S1' hydrophobic pocket from opposite sides: I50V shortens the flap-tip residue that packs against the inhibitor's P1' group, and I84V shortens the pocket wall itself. Lockbaum et al. showed both cost darunavir affinity (Ki <5 pM wild-type, 25.6 pM I84V, 74.5 pM I50V/A71V) but leave it picomolar — the reason darunavir needs three or more RAMs for a significant fold change. Test for each link: (i) an enzyme inhibition assay measures Ki directly against the published values; (ii) a viral replication assay measures EC50 against the published 7.7 nM (wild-type); (iii) a selection experiment measures the genetic barrier — the number of passages to resistance and the mutations selected — against darunavir's published high barrier.

### 4.4 Testable hypotheses

1. The best-scoring protease inhibitor on 4LL3 has a Ki within 3-fold of its published wild-type value in the same enzyme assay. Falsifier: Ki more than 3-fold worse than published. (Status after this study: the hypothesis is already weakened — the docking order does not reproduce the published Ki order, so the assay is now testing the method, not the compounds.)
2. Darunavir's docking score falls least between 4LL3 and the I50V structure (6DH6) of any compound in the set — the computational signature of its high genetic barrier. Falsifier: another inhibitor loses less score on the mutant than darunavir does. (Status after this study: saquinavir loses 0.03 and atazanavir 0.07, both less than darunavir's 0.31 — the hypothesis is refuted on the docking evidence, which is why the docking, not darunavir, is the thing that failed.)
3. No compound in the set out-scores darunavir on 4LL3 by more than 2 kcal/mol. Falsifier: a compound does, which would reopen the question of whether darunavir's scaffold is the best starting point. (Status after this study: the hypothesis holds — the largest lead is 0.91 kcal/mol — but it holds vacuously, because the method cannot resolve the differences it was asked to measure.)

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): FRET-based enzyme inhibition assay for the five protease inhibitors on wild-type, I50V and I84V HIV-1 protease, same plate, n=3, with darunavir's published Ki values (<5, 74.5, 25.6 pM) as the controls; readout Ki. Stage 2 (weeks 4–8): viral replication (EC50) assay for the best two compounds from stage 1 against wild-type HIV-1 in MT-4 cells, with darunavir's published 7.7 nM as the control, plus a cytotoxicity counter-screen. Stage 3 (weeks 9–12): if any compound passes stages 1–2 — Ki within 3-fold of darunavir's on wild-type and a smaller fold-loss on the mutants — a serial-passage selection experiment under that compound to measure the resistance barrier; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows the ~1 kcal/mol that separates a 5-fold Ki difference — the exact scale of the I84V effect.
2. The mutant pockets are in darunavir's conformation, so part of any darunavir lead on 6DH6 is conformational favouritism; the cleaner comparison is among the four non-darunavir inhibitors.
3. The I50V structure (6DH6) is the single I50V mutant while the published Ki for the double mutant is I50V/A71V (74.5 pM), so the docking and the Ki are not on identical proteins; the I84V structure (6DH0) was not docked (run time) and its resistance is carried by the published Ki alone.
4. The pipeline's ChEMBL lookup returned only darunavir, so no ChEMBL-derived protease-inhibitor set exists in this study; the comparison set is five literature compounds.
5. Enzyme potency is not antiviral potency: tipranavir's Ki is 0.088 nM but its EC50 is 500 nM, and the docking sees neither protein binding nor cell penetration.
6. No published Pakistani study reports HIV-1 protease resistance genotypes, so the resistance picture is global; the Pakistani numbers in this paper are burden and cascade numbers, not resistance numbers.
7. The classical-canon sweep found no HIV-relevant text: the Canon and Kitab al-Hawi describe epidemic disease without a virus concept, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

No protease inhibitor beats darunavir on the wild-type HIV-1 protease structure 4LL3 by more than Vina's noise: saquinavir leads by 0.91 kcal/mol, inside the ±1–2 kcal/mol bar, and the method fails its own controls — darunavir scores worst of five on its own structure, and the I50V mutation costs it only 0.31 kcal/mol by docking against a published 15-fold Ki loss. Docking cannot rank the protease inhibitors or resolve the resistance it was designed to study, and no regimen change follows from these scores. The next step is a FRET-based enzyme inhibition assay on the same five compounds, which will either reproduce the published Ki order and rehabilitate the docking, or confirm that the ranking is a pocket artefact.

## 7. Policy implications

**Decision-maker:** Pakistan's National AIDS Control Programme (NACP) and the Common Management Unit for AIDS, TB and Malaria, with the provincial AIDS control programmes. **Decision:** whether to spend anything on protease-inhibitor resistance testing or on a darunavir switch, and what must exist first. **Exact change:** do not spend on resistance genotyping or on switching regimens on the basis of docking — the cascade gap is diagnosis, not drugs: only 21% of people living with HIV know their status and only 16% are on treatment, so the money goes first to testing and linkage, and to the unsafe-injection control that caused the Larkana outbreak; in parallel, add protease genotyping (I50V, I84V, L76V) to the existing HIV drug-resistance surveillance at the National Institute of Health, so Pakistan's own resistance picture is measured rather than assumed from global data. **If evidence Z appears, reverse this:** if surveillance shows darunavir RAMs above 10% in treatment-experienced patients, or if the cascade reaches 60% diagnosed and on treatment, move to a regimen assessment for darunavir-based second-line therapy; if surveillance confirms RAMs below 5%, keep darunavir as the reserve and spend the same money on testing — do not proceed to any regimen change on docking scores alone. The Islamic principle is hifz al-nafs, sharpened by the Larkana lesson: where the transmission route is a needle, the obligation is to fix the needle, not to buy a better drug. The evidence here is thin — docking only — so the recommendation is "run the testing and the surveillance", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content.

## References

1. World Health Organization / UNAIDS. HIV infections rise in Pakistan; WHO and UNAIDS call to action. 1 December 2025. (350,000 people living with HIV; new infections 16,000 in 2010 to 48,000 in 2024; 21% know status, 16% on treatment, 7% virally suppressed; ART 6,500 in 2013 to 55,500 in 2024; centres 13 to 95.)
2. Lockbaum GJ, et al. Structural adaptation of darunavir analogues against primary mutations in HIV-1 protease. ACS Infect Dis. 2019;5:316–325. PMID: 30543749. doi:10.1021/acsinfecdis.8b00336. (6DH0 I84V, 6DH6 I50V; Ki WT <5.0 pM, I84V 25.6 ± 5.6 pM, I50V/A71V 74.5 ± 5.6 pM; EC50 WT 7.7 ± 1.6 nM.)
3. Kozisek M, et al. Thermodynamic and structural analysis of HIV protease resistance to darunavir — analysis of heavily mutated patient-derived HIV-1 proteases. FEBS J. 2014;281:1834. (4LL3, 1.95 Å, wild-type + darunavir.)
4. Molecular basis for drug resistance in HIV-1 protease. (Review; compiled Ki/EC50 table for approved protease inhibitors — darunavir Ki 15 pM, EC50 1–4 nM; lopinavir Ki 0.005 nM; atazanavir Ki 0.046 nM; saquinavir Ki 0.065 nM; tipranavir Ki 0.088 nM, EC50 500 nM.)
5. RCSB PDB entry 4LL3: structure of wild-type HIV protease in complex with darunavir, 1.95 Å. RCSB Protein Data Bank. Accessed 2026-11-26.
6. RCSB PDB entry 6DH6: HIV-1 protease NL4-3 I50V mutant in complex with darunavir, 1.97 Å. RCSB Protein Data Bank. Accessed 2026-11-26.
7. UniProtKB P03366: HIV-1 protease, Human immunodeficiency virus type 1 group M subtype B (isolate BH10). UniProt. Accessed 2026-11-26.
8. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source — cited for the hifz al-nafs principle only.)
9. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
10. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-131-2026-11-26-4LL3.json` (darunavir, lopinavir, atazanavir, saquinavir, tipranavir on 4LL3) and `hidden_files/dock-HP-131-2026-11-26-6DH6.json` (same five compounds on 6DH6). The pipeline run is in `hidden_files/dock-HP-131-2026-11-26.json` (target UniProt P03366; ChEMBL lookup returned only the QUERY, so no ChEMBL-derived ligand set exists; docking skipped — no PDB found by the auto-picker). Reference drug darunavir (PubChem CID 213039); comparators lopinavir (CID 92727), atazanavir (CID 148192), saquinavir (CID 441243), tipranavir (CID 54682461), SMILES verified against PubChem. Structures: PDB 4LL3 (1.95 Å, wild-type + darunavir), 6DH6 (1.97 Å, I50V + darunavir). Target: UniProtKB P03366. No additional data were generated.
