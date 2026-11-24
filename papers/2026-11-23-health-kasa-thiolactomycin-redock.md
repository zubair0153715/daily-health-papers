# Thiolactomycin Re-Docks at −6.92 kcal/mol on Its Own KasA Structure 2WGE — a Weak Binder in the Right Pocket, and a Pipeline That Resolved KasA to a Human Enzyme

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-23 · **Health Papers Agent — Paper #103** (daily 5-paper run)

**Keywords:** Mycobacterium tuberculosis; KasA; thiolactomycin; mycolic acid; molecular docking; ChEMBL; tuberculosis; FAS-II; drug resistance

---

## Abstract

In 2023, tuberculosis caused an estimated 10.8 million new cases and 1.25 million deaths, and Pakistan is among the eight countries accounting for two-thirds of the global burden — yet the front-line drug isoniazid is defeated by katG mutations in most resistant strains, because isoniazid must be activated before it can inhibit its target, InhA. KasA, the β-ketoacyl-ACP synthase of the FAS-II mycolic-acid pathway, is isoniazid-independent: it needs no activation, so a KasA inhibitor bypasses the commonest isoniazid-resistance route entirely. Thiolactomycin, the thiolactone natural product that first proved KasA druggable, inhibits both KasA and KasB, and overexpression of either enzyme raises resistance to it — but no KasA inhibitor has reached the clinic. We asked whether any measured KasA ligand binds the active site more strongly than thiolactomycin. The LeadForge pipeline resolved the target correctly to UniProtKB P9WQD9 (M. tuberculosis KasA, H37Rv) — and then failed twice: ChEMBL resolved to CHEMBL2074, verified live as human maltase-glucoamylase, so zero bioactivities were returned and no comparison set exists; and the pipeline's PDB picker selected 6P9K, KasA in complex with the preclinical indazole JSF-3285, not thiolactomycin — its −6.11 kcal/mol score is a docking into the JSF-3285 pocket and is reported here only as the artefact. On the correct structure, the 1.80 Å crystal structure of KasA with bound thiolactomycin (PDB 2WGE), thiolactomycin re-docked at −6.92 kcal/mol (poses −6.92, −6.88, −5.79) centred exactly on the co-crystallised ligand TLM (centre audit via dock._ligand_center). The paper's finding is therefore a validated control plus two honest negatives: the method recovers binding for the drug in its own pocket, but the score is weak — consistent with a weak, early inhibitor, not with a drug — and the "does any analogue beat thiolactomycin" question cannot be answered from ChEMBL as queried. The falsifiable next step is a KasA enzyme assay of thiolactomycin against its published mechanism, with the 2WGE pose as the structural hypothesis — not another docking run.

---

## 1. Introduction

The mycobacterial cell wall is a waxy, nearly impermeable barrier built from mycolic acids — very-long-chain α-alkyl-β-hydroxy fatty acids that make up as much as 60% of the wall and let the bacillus persist inside human macrophages. Mycobacteria make them with two fatty-acid systems: the mammalian-like FAS-I, which builds C14–C16 chains de novo, and the bacterial FAS-II, which elongates them to C54–C56. In FAS-II, the acyl carrier protein AcpM shuttles the growing chain between discrete enzymes: FabH primes, MabA and InhA process, and the β-ketoacyl-AcpM synthases KasA and KasB do the elongation — KasA the early rounds, KasB the later steps. Inhibiting cell-wall biosynthesis is fatal for the organism, which is why the pathway has been a drug target since isoniazid: but isoniazid inhibits InhA only after activation by the catalase-peroxidase KatG, and katG mutations are the commonest cause of isoniazid resistance. KasA needs no activation. A KasA inhibitor therefore bypasses the resistance route that defeats the front-line drug — the isoniazid-independent angle that defines this target.

Thiolactomycin (TLM), a thiolactone natural product, is the molecule that proved KasA druggable. It inhibits fatty-acid and mycolic-acid biosynthesis by targeting both KasA and KasB: overexpression of KasA, KasB or KasAB in Mycobacterium bovis BCG raises resistance to it in vitro and in vivo, and a multidrug-resistant clinical isolate was found highly sensitive to it — the first evidence that a KasA inhibitor could counter multidrug-resistant tuberculosis. Its analogues, designed from the structure, were more potent both in vitro against fatty-acid and mycolic-acid biosynthesis and in vivo against M. tuberculosis. The first atomic view came in 2009: the crystal structures of KasA in apo form and bound to thiolactomycin, which also revealed a polyethylene-glycol molecule mimicking a fatty-acid substrate of about 40 carbons — a platform for designing thiolactomycin analogues with higher affinity. The class has since advanced past thiolactomycin itself: the indazole JSF-3285, optimised from the earlier inhibitor DG167 by a structure-based approach, gained a 30-fold increase in mouse plasma exposure, and showed substantial activity in acute and chronic mouse models of infection, with efficacious reductions in colony-forming units at doses as low as 5 mg/kg once daily orally, and improved the efficacy of isoniazid or rifampicin. It is a preclinical candidate. The question this paper asks is the standard one for this series: among compounds with measured KasA potency already in ChEMBL, does any bind the active site more strongly than thiolactomycin — and can the pipeline even ask that question correctly?

The classical medical canon knows the disease, not the target: Ibn Sina's Canon of Medicine (c. 1025) treats consumption (sil) and chronic cough — the syndrome, not the enzyme. The principle carried forward here is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL ligands with measured M. tuberculosis KasA potency bind the active site of the thiolactomycin-bound structure (PDB 2WGE) at scores beyond re-docked thiolactomycin, and would that binding translate into stronger KasA inhibition and antimycobacterial activity? **Falsifier:** a KasA enzyme assay showing an IC50 worse than the analogue's published value, or a whole-cell MIC above 25 µg/mL against M. tuberculosis H37Rv, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the reference inhibitor re-docked on a co-crystal structure of its own target, with the co-crystallised inhibitor as the centre — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-23: the thiolactomycin KasA/KasB mechanism paper (J Biol Chem 2000;275:16857–16864; doi:10.1074/jbc.M000569200); the KasA crystal structures with thiolactomycin (Luckner et al., Structure 2009;17:1004–1013; doi:10.1016/j.str.2009.04.012; PMID 19604480); the JSF-3285 preclinical-candidate paper and the 6P9K structure (Inoyama et al., Cell Chem Biol 2020;27:560; PMID 32197094; doi:10.1016/j.chembiol.2020.02.007); the WHO Global Tuberculosis Report 2024 (10.8 million cases, 1.25 million deaths in 2023); and the RCSB records for PDB 2WGE and 6P9K.

### 2.2 Target identification

The pipeline resolved the target to UniProtKB P9WQD9 (3-oxoacyl-[acyl-carrier-protein] synthase 1, KasA, Mycobacterium tuberculosis strain ATCC 25618 / H37Rv), verified live 2026-11-23. This is the correct target. What failed was the ChEMBL resolution: the pipeline selected CHEMBL2074, verified live as "Maltase-glucoamylase", SINGLE PROTEIN, Homo sapiens — a human digestive enzyme. It is the same fallback ID the pipeline returned for FtsZ in Paper #101, which suggests CHEMBL2074 is the pipeline's default when its ChEMBL search fails, not a genuine match. The standing fix for this series is now to verify the ChEMBL target's name and organism before any ligand retrieval is trusted — and to treat a repeated CHEMBL2074 as a failed search, not a result.

### 2.3 The pipeline's two failures, stated not smoothed over

First, ChEMBL bioactivity retrieval for the wrong target CHEMBL2074 returned zero records (step 2: `no_data`, count 0). No known ligands with measured potency were retrieved, so the similarity screen was skipped and the only "lead" ranked was the query compound itself, thiolactomycin (score 97.5 by the pipeline's composite). There is therefore no comparison set in this run, and the question "does any analogue beat thiolactomycin" has no computational answer here. That is a data-retrieval failure, not a finding about thiolactomycin.

Second, the pipeline's PDB picker selected 6P9K and docked thiolactomycin on it at −6.11 kcal/mol. Verified live 2026-11-23, 6P9K is the crystal structure of M. tuberculosis KasA in complex with O6G — JSF-3285, the preclinical indazole candidate. The enzyme is right; the pocket is the JSF-3285 pocket, optimised by structure-based design for a later, more potent indazole, not the thiolactomycin pocket. A −6.11 kcal/mol score for thiolactomycin in the JSF-3285 pocket is a property of the wrong ligand's pocket and is reported here only as the artefact it is, with its file reference, so that no reader mistakes it for the control. The same structure-picker error has now bitten this series four times in two days (Papers #95, #100, #101, #103), and the lesson is the same: the picked PDB entry's title and bound ligands must be verified by hand, every run.

### 2.4 Molecular docking — the redock on the correct structure

The benchmark structure is 2WGE: the 1.80 Å crystal structure of M. tuberculosis KasA with bound thiolactomycin (Luckner et al., Structure 2009). A targeted redock script (`health-papers-agent/redock_hp093_2wge.py`) docked thiolactomycin on 2WGE using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: grid centre the centroid of the co-crystallised thiolactomycin (ligand TLM, 14 heavy atoms — C11H14O2S, matching thiolactomycin), [38.10, 1.00, −6.78], verified by direct computation from the PDB file with `dock._ligand_center` (the centre audit confirmed TLM is the largest drug-like HETATM group in the file; the seven glycerols, the isopropyl alcohol, the sodium ion and the waters were correctly excluded); box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The receptor preparation keeps the polyethylene-glycol substrate mimic in the structure, so the long acyl-chain channel is realistic. Thiolactomycin is therefore the self-dock control on its own structure: a method that could not recover binding for the drug in the pocket it was crystallised in would be broken. The docked thiolactomycin is the parent SMILES as returned by PubChem (CID 135403829); the crystal holds the same molecule, so no prodrug/metabolite caveat applies here.

### 2.5 PAINS screen

RDKit PAINS filter applied to thiolactomycin. PAINS-clean: no alerts. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.6 ADMET and toxicity read-across

RDKit descriptors computed for thiolactomycin: molecular weight 210.30, logP 2.98, 1 hydrogen-bond donor, 3 acceptors, TPSA 37.3 Å², 2 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. ToxGuard Tox21 kNN read-across (12 assays) for thiolactomycin: maximum predicted probability 0.308 (SR-ARE), a weak read-across (maximum neighbour similarity 0.242), not a measurement, and it does not clear the compound for development — it is the profile of a natural-product starting point, reported for completeness.

### 2.7 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond thiolactomycin's published mechanism. There is no comparison set: ChEMBL returned zero bioactivities for the wrongly resolved target, so the benchmark question is unanswered, not answered in the negative. One rigid structure was used (2WGE, 1.80 Å); KasA's active site adapts to different chemotypes, and the long acyl-chain channel means one structure under-samples the binding landscape. The docked compound is thiolactomycin itself, not its more potent analogues or JSF-3285, which is the molecule that actually advanced to preclinical candidacy.

## 3. Results

### 3.1 Docking: the comparison table (2WGE, 1.80 Å — the drug's own structure)

| Compound | Measured potency (published) | Best affinity, 2WGE (kcal/mol) | Top-3 poses (kcal/mol) | Median pose |
|---|---|---|---|---|
| Thiolactomycin (reference) | KasA/KasB inhibitor (natural product; mechanism published, no single IC50 in this run) | −6.92 | −6.92, −6.88, −5.79 | −6.88 |
| (no comparison ligands — ChEMBL resolved to human maltase-glucoamylase, 0 bioactivities) | — | — | — | — |

Thiolactomycin re-docks at −6.92 kcal/mol on its own structure, with the top two poses tight (−6.92, −6.88) and the third 1.1 kcal/mol higher: the method recovers binding for the drug in the pocket it was crystallised in, so the protocol is not broken — but the score is weak. A −6.92 kcal/mol re-dock is the weakest self-dock control in this series so far (doravirine −11.85, PC190723 −9.43, venetoclax −10.22), and it is consistent with what the literature says about thiolactomycin: a weak, early natural-product inhibitor whose value is as a starting point, not as a drug. There is no analogue to compare it against, so no "beats thiolactomycin" claim can be made in either direction. The discarded pipeline score (−6.11 kcal/mol on 6P9K, the JSF-3285 pocket) is not in the table, because it is not a measurement of this pocket — though it is worth noting that it is also weak, and that the 0.81 kcal/mol gap between the two pockets is inside Vina noise, which is itself a warning about how little either number can say about a weak binder.

### 3.2 Comparison with published data

No published Vina study of thiolactomycin on 2WGE was found in the sweep; the comparison here is internal (the inhibitor re-docked on its own structure, same protocol as Papers #1/#3). The structural literature is the published ground truth for the binding mode: the 2WGE structure shows thiolactomycin in the KasA active site, and the polyethylene-glycol molecule in the same structure mimics a fatty-acid substrate of about 40 carbons — the atomic view of the long-chain channel that makes KasA a target. The medicinal-chemistry literature gives the paper its most useful context: the thiolactomycin analogues designed from that structure were more potent in vitro and in vivo, and the indazole JSF-3285 — optimised from DG167 by a structure-based approach, with a 30-fold increase in mouse plasma exposure and efficacy at 5 mg/kg once daily in acute and chronic mouse models — is the proof that the pocket rewards optimisation. The gap between thiolactomycin's −6.92 and JSF-3285's candidacy is the gap this series exists to measure.

### 3.3 The clinical confounder that docking cannot see

Thiolactomycin's clinical story is the paper's most important context, and docking cannot see any of it. The drug's value was never its potency — it was the proof of concept: a KasA inhibitor works against a multidrug-resistant clinical isolate, and overexpression of the target raises resistance, which is the genetic proof of mechanism. And its failure was never its affinity alone — it was potency and pharmacokinetics together, which is why the class's advance is JSF-3285, a molecule optimised for exposure as much as for binding. A compound that out-scores thiolactomycin here by 1 kcal/mol but keeps its weak exposure would be no advance at all, and docking on a wild-type structure cannot tell the two apart. The docking order cannot explain why no KasA inhibitor has reached the clinic; the exposure data together with the structure can.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since thiolactomycin was published. Before 2000, the question was "can KasA be inhibited at all?" — now it is "which molecule, if any, beats thiolactomycin in the active site *and* survives the exposure test that stopped the class?" The benchmark is therefore a screen for successors with a two-part bar: beat −6.92 kcal/mol on 2WGE and keep mouse exposure. This paper supplies the first half of the bar — and shows it is a low bar, because the reference drug is weak — and the second half is where the work is: the comparison set does not exist in ChEMBL as queried, and the structure picker chose the successor's pocket.

### 4.2 Why the "win" must not be over-read

There is no win to over-read. Three reasons the paper is a control plus two negatives, not a discovery. First, there is no comparison set — ChEMBL resolved to a human enzyme and returned zero bioactivities. Second, the pipeline's first structure was the JSF-3285 complex and its −6.11 kcal/mol score measured the wrong pocket, and that score must be discarded, not averaged in. Third, even the valid re-dock is weak (−6.92 kcal/mol) and a single rigid structure, and the third pose sits 1.1 kcal/mol above the best, so the pose ensemble is not tight.

### 4.3 The pipeline failure is the experiment's design constraint, not a reason to stop

The two failures have different root causes and the same fix. The ChEMBL failure is a fallback error (CHEMBL2074 returned twice in one day for two unrelated bacterial targets); the structure failure is a bound-ligand error (the successor's complex picked over the reference's own). The fix, now standing practice for this series: verify the ChEMBL target's name and organism before ligand retrieval, treat a repeated CHEMBL2074 as a failed search, and verify the picked PDB entry's title and bound ligands by hand before any score is reported — with a centre audit that names the ligand the centre came from, as this redock does. A pipeline that docks the right drug into the wrong pocket and reports the number is worse than a pipeline that reports nothing — this paper reports the nothing, with the artefact named.

### 4.4 Mechanism

Thiolactomycin binds the KasA active site and blocks the condensation of the growing acyl-AcpM chain with malonyl-AcpM, halting FAS-II elongation and therefore mycolic-acid biosynthesis. Test for each link: (i) a KasA enzyme assay (condensation of acyl-AcpM with malonyl-AcpM, with thiolactomycin as the comparator) measures IC50 directly against the published mechanism; (ii) a mycolic-acid biosynthesis assay (radiolabelled acetate incorporation) measures pathway inhibition in whole cells; (iii) a whole-cell MIC assay against M. tuberculosis H37Rv and a multidrug-resistant clinical isolate measures antimycobacterial activity at matched concentration, with a cytotoxicity counter-screen; (iv) a KasA-overexpression strain measures whether a candidate kept the on-target logic — loss of activity on overexpression is the genetic proof that defines the class.

### 4.5 Testable hypotheses

1. Thiolactomycin inhibits M. tuberculosis KasA in an enzyme assay with an IC50 within 3-fold of its published mechanism. Falsifier: IC50 > 3-fold worse than published.
2. A candidate KasA inhibitor that out-scores thiolactomycin on 2WGE keeps activity against a multidrug-resistant clinical isolate within 5-fold of H37Rv. Falsifier: >10-fold loss against the resistant isolate.
3. The 2WGE pose predicts the resistance profile: a candidate whose docked pose loses contact with the active-site residues where KasA overexpression raises resistance loses activity against the overexpression strain first. Falsifier: a candidate without those contacts keeps wild-type potency on overexpression.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): fix the pipeline query (verify ChEMBL target name and organism; treat CHEMBL2074 as a failed search; hand-verify PDB title and bound ligands with a centre audit) and re-run the ligand retrieval for M. tuberculosis KasA to build the comparison set this paper could not — five ChEMBL KasA ligands with measured potency, docked on 2WGE at the audited centre, plus JSF-3285 docked on 2WGE as the positive control the field already has. Stage 2 (weeks 4–8): KasA enzyme assay for thiolactomycin against its published mechanism, plus the best-scoring candidate from stage 1, on wild-type KasA. Stage 3 (weeks 9–12): if any candidate passes stages 1–2, MIC assay against H37Rv and a multidrug-resistant clinical isolate plus a KasA-overexpression strain; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows any margin under ~2 kcal/mol.
2. There is no comparison set: ChEMBL resolved to human maltase-glucoamylase and returned zero bioactivities, so the benchmark question is unanswered.
3. The pipeline's first structure (6P9K) was the JSF-3285 complex; the −6.11 kcal/mol score on it measured the successor's pocket, not thiolactomycin's own, and is discarded — the centre audit is what separates the two.
4. One rigid structure was used (2WGE, 1.80 Å); KasA's active site and its long acyl-chain channel adapt to different chemotypes, so one structure under-samples the binding landscape.
5. Docking was on the wild-type structure only; the multidrug-resistance question — the one that matters clinically — was not docked, because no resistant-strain KasA structure with a candidate ligand was in the comparison set.
6. No data on the clinical confounder: docking cannot distinguish the proof-of-concept activity against a multidrug-resistant isolate from the potency and exposure problems that kept the class out of the clinic.
7. The classical-canon sweep found no KasA-relevant text: the Canon of Medicine treats consumption, not enzymes, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

Thiolactomycin, the thiolactone natural product that first proved KasA druggable, re-docks at −6.92 kcal/mol on its own 1.80 Å structure 2WGE with tight top-two pose consistency and no PAINS alert — a validated control, and a weak one. No analogue can be claimed to beat it or lose to it: ChEMBL resolved the target to a human digestive enzyme and returned zero bioactivities, so there is no comparison set, and the pipeline's first structure was the JSF-3285 complex, whose −6.11 kcal/mol score measured the successor's pocket and is discarded as a measurement of thiolactomycin's own. The paper's useful result is therefore the control plus the two named failures, and the low bar they set: the reference drug docks at −6.92 kcal/mol, the weakest self-dock control in this series, which is exactly why the class advanced to JSF-3285 — a molecule optimised for exposure, not just for binding. What the docking cannot do is resolve the potency-and-exposure question that defines this class: the same active site that binds thiolactomycin at −6.92 kcal/mol is the site whose optimisation produced a preclinical candidate, and only a KasA enzyme assay plus a whole-cell MIC can tell whether a successor keeps the isoniazid-independent logic that made KasA interesting. The next step is the cheap, decisive test — fix the query, build the comparison set, dock JSF-3285 as the positive control, and run a KasA enzyme assay plus MIC — not another docking run on an unverified structure.

## 7. Policy implications

**Decision-maker:** Pakistan's National TB Control Programme and the DRAP registration office, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of KasA inhibition as an academic drug-discovery exercise, and whether to prioritise isoniazid-independent targets in procurement for drug-resistant tuberculosis. **Exact change:** commission the 8–12-week pipeline-fix plus enzyme screen proposed in §4.6 for the five best ChEMBL KasA ligands against thiolactomycin, with JSF-3285 as the positive control, instead of funding another purely computational screen of the same target on unverified structures; and, in parallel, ask the TB programme to note explicitly that the binding question is settled for the wild-type active site — thiolactomycin re-docks at −6.92 kcal/mol — and that the remaining gap is potency and exposure, not the drug's mechanism: every rupee spent re-docking thiolactomycin into the JSF-3285 pocket is a rupee not spent testing candidates against a multidrug-resistant isolate. **If evidence Z appears, reverse this:** if a candidate beats thiolactomycin's re-dock by >2 kcal/mol on 2WGE and keeps activity against a multidrug-resistant isolate within 5-fold, drop the access-only framing and fund the candidate's development; if the fixed query returns no candidate within noise of thiolactomycin, drop this ligand set and redirect the same screen to the next KasA chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable KasA inhibitor from a useless one for a disease that killed 1.25 million people in 2023, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only, and a single-compound control at that — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. World Health Organization. Global tuberculosis report 2024. Geneva: WHO; 2024. (10.8 million new cases, 1.25 million deaths in 2023.)
2. Thiolactomycin and related analogues as novel anti-mycobacterial agents targeting KasA and KasB condensing enzymes in Mycobacterium tuberculosis. J Biol Chem. 2000;275:16857-16864. doi:10.1074/jbc.M000569200.
3. Luckner SR, et al. Crystal structures of Mycobacterium tuberculosis KasA show mode of action within cell wall biosynthesis and its inhibition by thiolactomycin. Structure. 2009;17:1004-1013. doi:10.1016/j.str.2009.04.012. PMID: 19604480.
4. Inoyama D, et al. A preclinical candidate targeting Mycobacterium tuberculosis KasA. Cell Chem Biol. 2020;27:560. doi:10.1016/j.chembiol.2020.02.007. PMID: 32197094.
5. RCSB PDB entry 2WGE: Crystal structure of KasA of Mycobacterium tuberculosis with bound TLM, 1.80 Å. RCSB Protein Data Bank. Accessed 2026-11-23.
6. RCSB PDB entry 6P9K: Crystal structure of Mycobacterium tuberculosis KasA in complex with O6G (JSF-3285). RCSB Protein Data Bank. Accessed 2026-11-23.
7. ChEMBL target CHEMBL2074: Maltase-glucoamylase, Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-23. (Wrong target for M. tuberculosis KasA; zero bioactivities returned.)
8. UniProtKB P9WQD9: 3-oxoacyl-[acyl-carrier-protein] synthase 1 (KasA), Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv). UniProt. Accessed 2026-11-23.
9. PubChem CID 135403829: thiolactomycin. National Library of Medicine. Accessed 2026-11-23.
10. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; treats consumption, sil — cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-093-2wge-2026-11-23.json` (thiolactomycin on 2WGE) and `hidden_files/dock-HP-093-2026-11-23.json` (P9WQD9 pipeline run, including the discarded 6P9K docking step). Reference inhibitor thiolactomycin (PubChem CID 135403829). Structure: PDB 2WGE (1.80 Å); discarded structure PDB 6P9K (KasA + JSF-3285). Target: UniProtKB P9WQD9; ChEMBL target CHEMBL2074 (human maltase-glucoamylase — wrong target; zero bioactivities). No additional data were generated.
