# Doravirine Re-Docks at −11.85 kcal/mol on Its Own Cryo-EM RT Structure 7Z2G — but the Pipeline's First Answer Was a Protease Structure, and ChEMBL Holds No Comparison Set

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-23 · **Health Papers Agent — Paper #100** (daily 5-paper run)

**Keywords:** HIV-1; reverse transcriptase; doravirine; NNRTI; molecular docking; ChEMBL; drug resistance; K103N; Y181C

---

## Abstract

About 40 million people were living with HIV in 2023, and the non-nucleoside reverse transcriptase inhibitors (NNRTIs) remain a backbone of antiretroviral therapy — yet the class's history is a history of resistance: K103N alone defeats efavirenz and nevirapine. Doravirine, a pyridinone NNRTI approved in 2018, was designed to keep activity against those mutants, with published IC50 values of 12 nM (wild-type), 21 nM (K103N), 31 nM (Y181C) and 33 nM (K103N/Y181C), and no viral breakthrough in resistance selections at clinically relevant concentrations where rilpivirine and efavirenz both broke through. We asked whether any measured RT ligand binds the NNRTI pocket more strongly than doravirine. The LeadForge pipeline resolved the target to UniProtKB P03366 (Gag-Pol polyprotein) and ChEMBL CHEMBL5823 — and then failed twice: ChEMBL returned zero bioactivities for CHEMBL5823, so no comparison set exists, and the pipeline's PDB picker selected 2HS1, verified live as the 0.84 Å structure of HIV-1 protease (V32I mutant) with darunavir, not reverse transcriptase — its −9.3 kcal/mol "doravirine" score is a docking into the protease active site and is discarded here as meaningless. On the correct structure, the 3.65 Å cryo-EM wild-type RT/DNA complex with doravirine (PDB 7Z2G), doravirine re-docked at −11.85 kcal/mol (poses −11.85, −11.68, −8.16) centred exactly on the co-crystallised ligand 2KW (centre audit via dock._ligand_center). The paper's finding is therefore a validated control plus two honest negatives: the method recovers strong binding for the drug in its own pocket, but the "does any analogue beat doravirine" question cannot be answered from ChEMBL as queried, and the pipeline's structure picker cannot be trusted on polyprotein targets. The falsifiable next step is a wild-type and K103N/Y181C RT polymerase assay of doravirine against its own published IC50s, with the 7Z2G pose as the structural hypothesis — not another docking run.

---

## 1. Introduction

HIV-1 reverse transcriptase (RT) is the enzyme that copies the viral RNA genome into DNA, and it has been a drug target since the first antiretroviral, zidovudine, in 1987. The NNRTIs bind an allosteric hydrophobic pocket — the NNRTI-binding pocket (NNIBP) — about 10 Å from the polymerase active site, and lock the enzyme in a non-productive conformation. The class's weakness is its low genetic barrier: a single substitution, K103N, raises the EC50 of efavirenz more than 50-fold and of nevirapine beyond measurement, and K103N, Y181C and G190A together account for more than 90% of transmitted NNRTI resistance in the United States. Doravirine (formerly MK-1439), a pyridinone NNRTI approved by the FDA in 2018, was designed around that failure: its flexible binding mode keeps hydrogen bonding to Lys101 and hydrophobic contacts to Tyr181, Tyr188, Phe227 and Leu234 even when the pocket mutates. In biochemical assays it inhibits wild-type RT at 4.5 nM and the K103N and Y181C mutants at 5.5 and 6.1 nM; in cell culture with 100% normal human serum its IC50 is 12 nM against wild-type virus, 21 nM against K103N, 31 nM against Y181C and 33 nM against the K103N/Y181C double mutant — and its inhibitory quotients (clinical trough over IC50) of 39, 27 and 25 against those three mutants dwarf rilpivirine's 4.6, 1.4 and 0.8 and efavirenz's 2.5, 60 and 1.9. In resistance selections at clinically relevant concentrations, no viral breakthrough was observed with doravirine against K103N, Y181C, G190A or K103N/Y181C, while breakthrough viruses were readily detected with rilpivirine and efavirenz.

The clinical record since approval supports that design. Through week 192 of the DRIVE-FORWARD and DRIVE-AHEAD phase 3 trials, resistance to doravirine was uncommon — genotypic 1.3%, phenotypic 1.0% — and the mutations that did emerge (most commonly V106A/I/M and F227C) were distinct from the classic NNRTI mutations: K103N, Y181C, K101E, E138K and G190A were not detected in any participant who met resistance-testing criteria. A 2025 real-world study of 102 virologically suppressed patients with past NNRTI resistance-associated mutations switched to doravirine-containing regimens found no virological failure at week 48 (0/87) or week 96 (0/86), even though 25% had documented historical doravirine resistance-associated mutations. The question this paper asks is the standard one for this series: among compounds with measured RT potency already in ChEMBL, does any bind the NNRTI pocket more strongly than doravirine — and can the pipeline even ask that question correctly?

The classical medical canon predates HIV by nine centuries and offers no target for it; the Canon of Medicine (c. 1025) knows no virus. The principle carried forward here is hifz al-nafs, preservation of life (see §7): where a cheap assay can distinguish a usable NNRTI from a useless one, running the assay is the obligation.

**Falsifiable question.** Do ChEMBL ligands with measured HIV-1 RT potency bind the NNRTI pocket of the doravirine-bound structure (PDB 7Z2G) at scores beyond re-docked doravirine, and would that binding translate into stronger RT inhibition, including against K103N/Y181C? **Falsifier:** an RT polymerase assay showing an IC50 worse than the analogue's published value, or loss of activity against the K103N/Y181C double mutant, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the approved drug re-docked on a co-crystal structure of its own target, with the co-crystallised drug as the centre — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-23: the doravirine resistance-suppression study (Lai et al., Antimicrob Agents Chemother 2016; doi:10.1128/AAC.02650-15); the DRIVE-FORWARD/DRIVE-AHEAD week-192 resistance analysis (J Acquir Immune Defic Syndr 2026;101(3):308–315; PMID 41129125); the real-world switch study in patients with past NNRTI mutations (J Antimicrob Chemother 2025;80:810–816; doi:10.1093/jac/dkae481); the doravirine cryo-EM structures (Singh et al., Proc Natl Acad Sci USA 2022;119:e2203660119; PMID 35858448; doi:10.1073/pnas.2203660119); the 2HS1 protease structure paper (Kovalevsky et al., J Mol Biol 2006;363:161–173; PMID 16962136); the RCSB records for PDB 7Z2G and 2HS1; and the UNAIDS 2024 global HIV estimates.

### 2.2 Target identification

The pipeline resolved the target to UniProtKB P03366 (Gag-Pol polyprotein, HIV-1 group M subtype B, isolate BH10) → ChEMBL CHEMBL5823, "Gag-Pol polyprotein", SINGLE PROTEIN, verified live 2026-11-23. This is the correct protein family but the wrong granularity: Gag-Pol is a 1,447-residue polyprotein that is cleaved into protease, reverse transcriptase and integrase, and the pipeline's downstream steps treated it as one target. That is the root cause of both failures in §2.3–2.4, and the standing fix for this series is now to query viral polyprotein targets by accession of the mature enzyme (for RT, the p66 subunit) rather than by the polyprotein name.

### 2.3 The pipeline's two failures, stated not smoothed over

First, ChEMBL bioactivity retrieval for CHEMBL5823 returned zero records (step 2: `no_data`, count 0). No known ligands with measured potency were retrieved, so the similarity screen was skipped and the only "lead" ranked was the query compound itself, doravirine (score 97.5). There is therefore no comparison set in this run, and the question "does any analogue beat doravirine" has no computational answer here. That is a data-retrieval failure, not a finding about doravirine.

Second, the pipeline's PDB picker selected 2HS1 and docked doravirine on it at −9.3 kcal/mol. Verified live 2026-11-23, 2HS1 is the ultra-high-resolution (0.84 Å) crystal structure of the HIV-1 protease V32I mutant in complex with the protease inhibitor darunavir (TMC114) — a different enzyme, a different pocket, a different drug class. A −9.3 kcal/mol score for an NNRTI in a protease active site is a property of the wrong protein and is discarded in full: it appears in this paper only as the artefact it is, with its file reference, so that no reader mistakes it for a result. The same polyprotein-granularity error has bitten this series before (Paper #95, HBV polymerase resolved to a human helicase), and the lesson is the same: the pipeline's structure pick must be verified against the target enzyme by hand, every run.

### 2.4 Molecular docking — the redock on the correct structure

The benchmark structure is 7Z2G: the cryo-EM structure of wild-type HIV-1 RT with a DNA aptamer in complex with doravirine, 3.65 Å (Singh et al., PNAS 2022). A targeted redock script (`health-papers-agent/redock_hp088_7z2g.py`) docked doravirine on 7Z2G using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: grid centre the centroid of the co-crystallised doravirine (ligand 2KW, 29 heavy atoms — C17H11ClF3N5O3, matching doravirine), [72.10, 82.05, 65.58], verified by direct computation from the PDB file with `dock._ligand_center` (the centre audit confirmed 2KW is the largest drug-like HETATM group in the file; the two 21-atom OMC groups are modified nucleotides of the DNA aptamer, correctly excluded); box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The receptor preparation keeps the DNA aptamer ATOM records, so the NNRTI pocket is realistic — the primer grip and the YMDD motif sit in their doravirine-bound, non-productive conformation, and removing the DNA would have left a hole where the pocket actually sits. Doravirine is therefore the self-dock control on its own structure: a method that could not recover strong binding for the drug in the pocket it was crystallised in would be broken. The docked doravirine is the parent SMILES as returned by PubChem (CID 58460047); the crystal holds the same molecule, so no prodrug/metabolite caveat applies here (unlike Paper #96, sofosbuvir).

### 2.5 PAINS screen

RDKit PAINS filter applied to doravirine. PAINS-clean: no alerts. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.6 ADMET and toxicity read-across

RDKit descriptors computed for doravirine: molecular weight 425.75, logP 2.65, 1 hydrogen-bond donor, 5 acceptors, TPSA 105.7 Å², 4 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. ToxGuard Tox21 kNN read-across (12 assays) for doravirine: maximum predicted probability 0.328 (SR-ARE), a weak read-across (maximum neighbour similarity 0.241), not a measurement, and it does not clear the compound for development — it is the profile of an already-approved drug, reported for completeness.

### 2.7 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond doravirine's published IC50s. There is no comparison set: ChEMBL returned zero bioactivities for CHEMBL5823, so the benchmark question is unanswered, not answered in the negative. One rigid cryo-EM structure was used (7Z2G, 3.65 Å); the NNRTI pocket is flexible and adapts to different chemotypes, so one structure under-samples the binding landscape. The third pose (−8.16 kcal/mol) sits 3.7 kcal/mol above the best pose, so the pose ensemble is not tight.

## 3. Results

### 3.1 Docking: the comparison table (7Z2G, 3.65 Å — the drug's own structure)

| Compound | Measured RT potency (published) | Best affinity, 7Z2G (kcal/mol) | Top-3 poses (kcal/mol) | Median pose |
|---|---|---|---|---|
| Doravirine (reference) | IC50 12 nM (WT); 21 nM (K103N); 31 nM (Y181C); 33 nM (K103N/Y181C) | −11.85 | −11.85, −11.68, −8.16 | −11.68 |
| (no comparison ligands — ChEMBL returned 0 bioactivities for CHEMBL5823) | — | — | — | — |

Doravirine re-docks at −11.85 kcal/mol on its own structure, with the top two poses tight (−11.85, −11.68): the method recovers strong binding for the drug in the pocket it was crystallised in, so the protocol is not broken. There is no analogue to compare it against, so no "beats doravirine" claim can be made in either direction. The discarded pipeline score (−9.3 kcal/mol on 2HS1, HIV-1 protease + darunavir) is not in the table, because it is not a measurement of this target.

### 3.2 Comparison with published data

No published Vina study of doravirine on 7Z2G was found in the sweep; the comparison here is internal (the drug re-docked on its own structure, same protocol as Papers #1/#3). The structural literature is the published ground truth for the binding mode: the 7Z2G cryo-EM structure shows doravirine in the NNIBP with its triazole hydrogen-bonded to Lys101 and its chlorobenzonitrile and trifluoromethyl groups in hydrophobic contact with Tyr181, Tyr188, Phe227 and Leu234, and shows the DNA primer 3′-end positioned at the active site in a non-productive state — the structural basis for the drug's retained activity against K103N and Y181C, whose side chains do not contact the drug's flexible core. The mutant structure 7Z2H (E138K/M184I RT/DNA + doravirine, 3.58 Å, same paper) shows the E138K mutation opening the pocket entrance, which the authors link to faster dissociation of rilpivirine — a mechanism doravirine's binding mode partly avoids.

### 3.3 The clinical confounder that docking cannot see

Doravirine's clinical record is the paper's most important context, and docking cannot see any of it. The drug's value is not that it binds RT more tightly than its predecessors — it is that it keeps binding when the pocket mutates, and that through 192 weeks of phase 3 follow-up only 1.3% of treated patients developed genotypic resistance, with the classic K103N/Y181C/G190A mutations never appearing. The real-world switch study makes the same point from the other side: patients whose viruses already carried NNRTI mutations, switched to doravirine while suppressed, did not fail. A compound that out-scores doravirine here by 1 kcal/mol but loses activity against K103N/Y181C would be a worse drug, and docking on a wild-type structure cannot tell the two apart. The docking order cannot explain why the drug's resistance barrier is high; the structure and the trial data together can.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since doravirine was approved. Before approval, the question was "can an NNRTI keep activity against K103N and Y181C?" — now it is "which molecule, if any, beats doravirine on the wild-type pocket *and* keeps its mutant profile?" The benchmark is therefore a screen for successors with a two-part bar: beat −11.85 kcal/mol on 7Z2G and keep activity against K103N/Y181C. This paper supplies the first half of the bar and shows the second half is where the pipeline must be fixed before it can supply the first: the comparison set does not exist in ChEMBL as queried, and the structure picker chose a protease.

### 4.2 Why the "win" must not be over-read

There is no win to over-read. Three reasons the paper is a control plus two negatives, not a discovery. First, there is no comparison set — ChEMBL returned zero bioactivities for CHEMBL5823. Second, the pipeline's first structure was the wrong enzyme entirely, and the −9.3 kcal/mol it produced must be discarded, not averaged in. Third, even the valid re-dock is a single rigid structure at 3.65 Å cryo-EM resolution, and the third pose sits 3.7 kcal/mol above the best, so the pose ensemble is not tight.

### 4.3 The pipeline failure is the experiment's design constraint, not a reason to stop

The two failures have the same root cause and the same fix. The polyprotein granularity (P03366 → CHEMBL5823) broke both the ligand retrieval and the structure pick. The fix, now standing practice for this series: query viral polyprotein targets by the mature enzyme's accession (RT p66), verify the ChEMBL target's bioactivity count before docking, and verify the picked PDB entry's title against the target enzyme by hand before any score is reported. A pipeline that docks the right drug into the wrong enzyme and reports the number is worse than a pipeline that reports nothing — this paper reports the nothing, with the artefact named.

### 4.4 Mechanism

Doravirine binds the NNIBP ~10 Å from the polymerase active site, hydrogen-bonded to Lys101, and locks RT in a non-productive conformation with the DNA primer 3′-end mispositioned at the active site. Test for each link: (i) an RT polymerase assay (primer-extension, with doravirine as the comparator) measures IC50 directly against the published 12 nM wild-type value; (ii) the same assay on K103N, Y181C and K103N/Y181C mutant RT measures whether a candidate kept the resistance barrier that defines the class — loss of activity against the double mutant is the likeliest way a "better" NNRTI becomes a worse drug; (iii) a cell-based antiviral assay in the presence of human serum measures EC50 against doravirine at matched concentration, with a cytotoxicity counter-screen.

### 4.5 Testable hypotheses

1. Doravirine inhibits wild-type HIV-1 RT in a polymerase assay with an IC50 within 3-fold of its published 12 nM value. Falsifier: IC50 > 3-fold worse than published.
2. A candidate NNRTI that out-scores doravirine on 7Z2G keeps activity against K103N/Y181C mutant RT within 5-fold of wild-type. Falsifier: >10-fold loss against the double mutant.
3. The 7Z2G pose predicts the resistance profile: a candidate whose docked pose loses the Lys101 hydrogen bond loses activity against K103N first. Falsifier: a candidate without the Lys101 contact keeps wild-type potency against K103N.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): fix the pipeline query (mature-enzyme accession, verified ChEMBL bioactivity count, hand-verified PDB title) and re-run the ligand retrieval for HIV-1 RT to build the comparison set this paper could not — five ChEMBL RT ligands with measured potency, docked on 7Z2G at the audited centre. Stage 2 (weeks 4–8): RT polymerase primer-extension assay for doravirine against its published IC50s, plus the best-scoring candidate from stage 1, on wild-type and K103N/Y181C mutant RT. Stage 3 (weeks 9–12): if any candidate passes stages 1–2, cell-based antiviral assay in human serum plus a cytotoxicity counter-screen; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows any margin under ~2 kcal/mol.
2. There is no comparison set: ChEMBL returned zero bioactivities for CHEMBL5823, so the benchmark question is unanswered.
3. The pipeline's first structure (2HS1) was HIV-1 protease, not RT; the −9.3 kcal/mol score on it is discarded, and the pipeline's structure picker needs independent verification every run.
4. One rigid cryo-EM structure was used (7Z2G, 3.65 Å); the NNRTI pocket is flexible, and the third pose sits 3.7 kcal/mol above the best, so the pose ensemble is not tight.
5. Docking was on the wild-type structure only; the K103N/Y181C resistance question — the one that matters clinically — was not docked, because no mutant RT structure with a candidate ligand was in the comparison set.
6. No data on the clinical confounder: docking cannot distinguish the 1.3% genotypic resistance rate from the >90% transmitted-resistance share of K103N/Y181C/G190A.
7. The classical-canon sweep found no HIV-relevant text: the Canon of Medicine predates the virus by nine centuries, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this disease.

## 6. Conclusion

Doravirine, the pyridinone NNRTI designed to survive K103N and Y181C, re-docks at −11.85 kcal/mol on its own 3.65 Å cryo-EM structure 7Z2G with tight top-two pose consistency and no PAINS alert — a validated control, not a discovery. No analogue can be claimed to beat it or lose to it: ChEMBL returned zero bioactivities for the pipeline's target CHEMBL5823, so there is no comparison set, and the pipeline's first structure was HIV-1 protease with darunavir, whose −9.3 kcal/mol score is discarded as a measurement of the wrong enzyme. The paper's useful result is therefore the control plus the two named failures: the method works on the right structure, the query path does not, and the fix — mature-enzyme accession, verified bioactivity count, hand-verified PDB title — is specified so the next run can ask the question this one could not. What the docking cannot do is resolve the resistance question that defines this drug: the same NNRTI pocket that binds doravirine at −11.85 kcal/mol is the pocket whose K103N and Y181C mutations defeat the older drugs, and only a mutant-RT assay can tell whether a successor keeps doravirine's barrier. The next step is the cheap, decisive test — fix the query, build the comparison set, and run a wild-type plus K103N/Y181C polymerase assay — not another docking run on an unverified structure.

## 7. Policy implications

**Decision-maker:** Pakistan's National AIDS Control Programme and the DRAP registration office, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of NNRTI benchmarking as an academic drug-discovery exercise, and whether to prioritise doravirine-containing regimens in procurement for patients with prior NNRTI exposure. **Exact change:** commission the 8–12-week pipeline-fix plus polymerase screen proposed in §4.6 for the five best ChEMBL RT ligands against doravirine, instead of funding another purely computational screen of the same target on unverified structures; and, in parallel, ask the AIDS programme to note explicitly that the binding question is settled for the wild-type pocket — doravirine re-docks at −11.85 kcal/mol — and that the remaining gap is the mutant pocket and the comparison set, not the drug's potency: every rupee spent re-docking doravirine into the wrong enzyme is a rupee not spent testing candidates against K103N/Y181C. **If evidence Z appears, reverse this:** if a candidate beats doravirine's re-dock by >2 kcal/mol on 7Z2G and keeps activity against K103N/Y181C within 5-fold, drop the access-only framing and fund the candidate's development; if the fixed query returns no candidate within noise of doravirine, drop this ligand set and redirect the same screen to the next NNRTI chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable NNRTI from a useless one for a disease affecting about 40 million people, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only, and a single-compound control at that — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. UNAIDS. Global HIV & AIDS statistics — 2024 fact sheet. Geneva: UNAIDS; 2024. (About 40 million people living with HIV in 2023.)
2. Lai MT, et al. Doravirine suppresses common nonnucleoside reverse transcriptase inhibitor-associated mutants at clinically relevant concentrations. Antimicrob Agents Chemother. 2016;60(8):5015-5024. doi:10.1128/AAC.02650-15.
3. Doravirine resistance patterns identified through week 192 in the DRIVE-FORWARD and DRIVE-AHEAD phase 3 clinical trials. J Acquir Immune Defic Syndr. 2026;101(3):308-315. PMID: 41129125.
4. No virological failure in patients living with HIV with past NNRTI resistance-associated mutations switched to doravirine-containing regimens. J Antimicrob Chemother. 2025;80:810-816. doi:10.1093/jac/dkae481.
5. Singh AK, et al. Cryo-EM structures of wild-type and E138K/M184I mutant HIV-1 RT/DNA complexed with inhibitors doravirine and rilpivirine. Proc Natl Acad Sci USA. 2022;119:e2203660119. doi:10.1073/pnas.2203660119. PMID: 35858448.
6. Kovalevsky AY, et al. Ultra-high resolution crystal structure of HIV-1 protease mutant reveals two binding sites for clinical inhibitor TMC114. J Mol Biol. 2006;363:161-173. doi:10.1016/j.jmb.2006.08.007. PMID: 16962136.
7. RCSB PDB entry 7Z2G: Cryo-EM structure of HIV-1 reverse transcriptase with a DNA aptamer in complex with doravirine, 3.65 Å. RCSB Protein Data Bank. Accessed 2026-11-23.
8. RCSB PDB entry 2HS1: Ultra-high resolution X-ray crystal structure of HIV-1 protease V32I mutant with TMC114 (darunavir), 0.84 Å. RCSB Protein Data Bank. Accessed 2026-11-23.
9. ChEMBL target CHEMBL5823: Gag-Pol polyprotein, Human immunodeficiency virus type 1. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-23. (Zero bioactivities returned.)
10. UniProtKB P03366: Gag-Pol polyprotein, Human immunodeficiency virus type 1 group M subtype B (isolate BH10). UniProt. Accessed 2026-11-23.
11. PubChem CID 58460047: doravirine. National Library of Medicine. Accessed 2026-11-23.
12. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; predates HIV by nine centuries — no HIV-relevant text; cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-088-7z2g-2026-11-23.json` (doravirine on 7Z2G) and `hidden_files/dock-HP-088-2026-11-23.json` (P03366 pipeline run, including the discarded 2HS1 docking step). Reference drug doravirine (PubChem CID 58460047). Structure: PDB 7Z2G (3.65 Å); discarded structure PDB 2HS1 (HIV-1 protease + darunavir). Target: UniProtKB P03366; ChEMBL target CHEMBL5823 (zero bioactivities). No additional data were generated.
