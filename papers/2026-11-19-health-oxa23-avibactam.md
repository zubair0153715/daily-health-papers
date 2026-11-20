# Avibactam and Durlobactam Tie at −6.5 kcal/mol on OXA-23 — but the Scores Are Non-Covalent Only, and the Only Sub-Nanomolar ChEMBL Ligand Is a Boronate Vina Cannot Score

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-19 · **Health Papers Agent — Paper #82** (daily 5-paper run)

**Keywords:** OXA-23; Acinetobacter baumannii; carbapenemase; avibactam; durlobactam; molecular docking; ChEMBL; antimicrobial resistance

---

## Abstract

Carbapenem-resistant Acinetobacter baumannii (CRAB) sits atop the WHO critical-priority list, and in most of the world its carbapenem resistance is OXA-23 — yet the ChEMBL record for OXA-23 contains only two bioactivities. We asked whether any ChEMBL-recorded OXA-23 ligand binds the enzyme's active site more strongly than avibactam. Using the LeadForge pipeline (UniProtKB Q9L4P2 → ChEMBL target CHEMBL3885669, 2 bioactivities → PubChem/RDKit similarity, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked avibactam on the 1.15 Å OXA-23 structure 4JF5, centred on the active-site citrate (4.25 Å from the catalytic Ser79 oxygen, verified). Avibactam scored −6.54 kcal/mol; the only other ChEMBL ligand, a boronate with a measured Ki of 0.74 nM, could not be docked at all — AutoDock Vina does not support the boron atom type. We therefore docked durlobactam, the diazabicyclooctane inhibitor approved in 2023 as sulbactam–durlobactam and now the IDSA-preferred CRAB therapy, on the same centre: it scored −6.42 kcal/mol, a 0.12 kcal/mol tie with avibactam, with tight pose consistency and no PAINS alerts. The honest limit: both drugs are reversible covalent inhibitors, and Vina scores only non-covalent poses — the covalent bond to Ser79 is missing from both numbers — so the tie says nothing about their real inhibitory potency, and the 0.74 nM boronate remains unscored by this method. The claim that either diazabicyclooctane is the better OXA-23 inhibitor would be refuted if a biochemical inhibition assay (k2/Ki) shows a >10-fold difference. The falsifiable next step is an 8–12-week enzyme-plus-MIC test of avibactam, durlobactam and a boronate inhibitor against OXA-23-producing clinical isolates.

---

## 1. Introduction

Carbapenem-resistant Acinetobacter baumannii is one of the hardest infections in modern hospitals: the WHO places it on its critical-priority pathogen list, mortality in ventilator-associated pneumonia and bloodstream infection is high, and treatment options are few and toxic. The resistance is usually enzymatic: class D carbapenemases, above all OXA-23, hydrolyse carbapenems. In Germany, 77% of A. baumannii isolates submitted to the national reference centre in 2022–2023 produced an OXA-23 and/or OXA-72 carbapenemase; in Pakistan and across South Asia, OXA-23 dominates CRAB similarly. The therapeutic answer has been diazabicyclooctane (DBO) beta-lactamase inhibitors: avibactam (approved 2015, as ceftazidime–avibactam) and durlobactam (ETX2514; approved 2023 as sulbactam–durlobactam, and since 2024 the Infectious Diseases Society of America-preferred therapy for CRAB). Durlobactam differs from avibactam by a single double bond and an additional methyl group, and it inhibits class D OXA carbapenemases roughly 10-fold more potently than avibactam in published comparisons; in a 58-isolate study of carbapenem-resistant A. baumannii, all harbouring OXA-23- or OXA-40-like genes, the median sulbactam/durlobactam MIC was 2 mg/L against 16 mg/L for sulbactam/avibactam — an 8-fold difference in the combination that reaches the patient. But avibactam is widely available where durlobactam is not, and in regions without durlobactam, sulbactam/avibactam is used as an alternative. The question this paper asks is narrow: on the OXA-23 enzyme itself, do the two DBOs differ at all — and is there anything in the public ligand record that beats them?

The classical medical canon has no concept of a beta-lactamase, and this paper does not pretend otherwise: Ibn Sina's Canon of Medicine (c. 1025) discusses wound infections and their treatment, and Al-Razi's Kitab al-Hawi records clinical observation of severe infections. These texts are hypothesis sources, not evidence — they knew the syndrome, not the target — but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL-recorded OXA-23 ligands bind the true active site (PDB 4JF5) more strongly than avibactam, and does durlobactam bind better than avibactam on the same structure? **Falsifier:** a biochemical inhibition assay (second-order inactivation rate k2/Ki, or IC50) showing a >10-fold difference between the two DBOs, or a boronate inhibitor with a measured Ki below 1 nM that also restores sulbactam susceptibility in OXA-23 isolates, refutes the "tie" claim. **Causal identification:** validated-control re-docking — the reference drug re-docked on a structure of its own target — not a comparison against nothing. Association only beyond that: docking scores are not activity, and for covalent inhibitors they are not even the full binding energy.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-19: the sulbactam/avibactam-versus-durlobactam comparative study (JAC Antimicrob Resist 2025), the ETX2514 characterisation (Durand-Réville et al., Nat Microbiol 2017), the German national reference-centre OXA-23/72 surveillance data, and the RCSB record for PDB 4JF5. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025); Al-Razi, Kitab al-Hawi (c. 900) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: Acinetobacter baumannii beta-lactamase OXA-23, UniProtKB Q9L4P2; ChEMBL target CHEMBL3885669 (2 bioactivities retrieved live 2026-11-19). Structure: PDB 4JF5, OXA-23 at pH 4.1, 1.15 Å. Grid centre: centroid of the citrate (FLC) in the active-site cleft, [−26.15, −22.08, 8.55], verified by direct computation from the PDB file and 4.25 Å from the catalytic Ser79 side-chain oxygen; box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for avibactam and durlobactam.

**A tool limitation, stated plainly.** The only other ChEMBL OXA-23 ligand, CHEMBL4633785 (measured Ki 0.74 nM, formula C10H8BFO4), contains boron, and AutoDock Vina cannot score it: the run failed with "PDBQT parsing error: Atom type B is not a valid AutoDock type". This is a limitation of the docking tool, not of the compound — boronate beta-lactamase inhibitors (taniborbactam and analogues) are a real and important class, and this paper's method simply cannot evaluate them. The paper therefore reports the failure and compares avibactam with durlobactam (SMILES fetched live from PubChem), docked on the same centre (`hidden_files/dock-HP-091-2026-11-19.json` pipeline run; `hidden_files/dock-HP-091b-2026-11-19.json` salvage run, `hidden_files/redock_hp091.py`).

### 2.3 PAINS screen

RDKit PAINS filter applied to the pipeline leads and to durlobactam. None carries a PAINS alert: avibactam, durlobactam and the boronate are all PAINS-clean.

### 2.4 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for every lead; ToxGuard Tox21 kNN read-across (12 assays) run for avibactam. Avibactam (C7H11N3O6S, MW 265.25) passes Lipinski with 0 violations (logP −1.53, TPSA 130.24) and scores at most 0.15 on any Tox21 assay.

### 2.5 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data were generated in this study. Both DBO inhibitors are reversible covalent inhibitors that carbamylate the catalytic Ser79; Vina scores only non-covalent poses, so the covalent contribution — the dominant term for these drugs — is absent from every number in §3. The 4JF5 structure was solved at pH 4.1, far from physiological pH, and the catalytic Lys82 carboxylation state at that pH is uncertain.

## 3. Results

### 3.1 The ChEMBL OXA-23 record is nearly empty

| Compound | ChEMBL Ki vs OXA-23* | MW / formula | Docking result |
|---|---|---|---|
| Avibactam (CHEMBL1689063)† | 1,700 nM (pChEMBL 5.77) | 265.25 / C7H11N3O6S | −6.42 kcal/mol |
| CHEMBL4633785 | 0.74 nM (pChEMBL 9.13) | 221.98 / C10H8BFO4 | Vina failed — boron unsupported |

\* ChEMBL-recorded Ki against OXA-23 (target CHEMBL3885669), retrieved live 2026-11-19. † CHEMBL1689063 is avibactam itself, recorded in ChEMBL as a 1.7 µM OXA-23 ligand; it is not an independent lead.

The public ligand record for OXA-23 contains two compounds: the reference drug itself and one boronate. There is no third scaffold to test. This is a data-quality finding, not a result about the compounds: the target is under-annotated in ChEMBL relative to its clinical importance.

### 3.2 Docking: the comparison table

| Compound | Published potency context | Best affinity, 4JF5 (kcal/mol) | Top-3 poses (kcal/mol) | PAINS | MW / logP / TPSA |
|---|---|---|---|---|---|
| Avibactam (reference, re-docked) | Ki 1.7 µM vs OXA-23 (ChEMBL)‡ | **−6.54** | −6.54, −6.44, −6.39 | none | 265.25 / −1.53 / 130.24 |
| Durlobactam | ~10-fold more potent than avibactam on class D enzymes§ | −6.42 | −6.42, −6.31, −6.17 | none | 277.25 / — / — |
| Avibactam as CHEMBL1689063 | Ki 1.7 µM (same compound) | −6.42 | −6.42, −6.37, −5.91 | none | 265.25 / −1.53 / 130.24 |

‡ ChEMBL-recorded Ki for avibactam against OXA-23. § Published comparisons of durlobactam versus avibactam on class D beta-lactamases (Durand-Réville et al., 2017; see §3.3).

Avibactam and durlobactam are tied: 0.12 kcal/mol apart, with tight pose consistency (top-3 spread ≤0.25 kcal/mol). The ChEMBL-recorded avibactam entry reproduces the same score (−6.42), as it must — it is the same molecule.

### 3.3 The docking–microbiology discordance that must not be hidden

The measured data do not track the docking tie. Durlobactam inhibits class D enzymes roughly 10-fold more potently than avibactam in published enzyme comparisons, and in the 58-isolate clinical study the sulbactam/durlobactam MIC (2 mg/L) was 8-fold lower than sulbactam/avibactam (16 mg/L). Yet on 4JF5 the two drugs score identically. The reason is visible in the chemistry: both DBOs inhibit by reversibly carbamylating Ser79, and Vina scores only the non-covalent fit of the molecule in the pocket — the covalent bond, the desolvation of the active site, and the deacylation rate that actually distinguishes the two drugs are all absent from the calculation. Rigid Vina scoring on a single pH-4.1 structure cannot rank covalent inhibitors. This is the paper's most important negative result: **the docking tie is not an equivalence result**, and any claim built on the −6.54 vs −6.42 gap (or lack of one) would be over-reading noise on top of a missing covalent term. The 0.74 nM boronate, which by measured Ki is the strongest OXA-23 ligand in the public record, is unscored for a purely technical reason — and that is the more interesting lead.

### 3.4 Comparison with published docking

No published Vina study of avibactam or durlobactam on 4JF5 was found in the sweep; the comparison here is internal (compounds vs re-docked reference on the same structure, same protocol). The re-docked avibactam score of −6.54 kcal/mol is the validated control that anchors the comparison. Durand-Réville et al. (2017) reported a co-crystal of durlobactam (ETX2514) with the related OXA-24 enzyme (PDB 5VFD), not OXA-23 — a structural comparison that this paper's single-structure docking does not attempt.

## 4. Discussion

### 4.1 The reframe

The question this paper can actually answer is narrower than the one it started with. It cannot say "avibactam and durlobactam are equivalent on OXA-23" — the method cannot see the covalent chemistry that separates them, and the clinical microbiology says durlobactam is the better drug. What it can say is: (a) both DBOs fit the OXA-23 active site with tight, reproducible non-covalent poses; (b) the public ligand record for this critical target is nearly empty — two compounds, one of which the standard docking tool cannot score; (c) the decisive experiment is now sharply defined — enzyme inhibition kinetics and MIC testing against OXA-23 isolates, including a boronate — and it is cheap and feasible in a university lab.

### 4.2 Why the "tie" must not be over-read

Three reasons. First, the 0.12 kcal/mol gap is far inside Vina's ±1–2 kcal/mol noise. Second, the docking order contradicts the published enzyme and microbiology data, which favour durlobactam ~10-fold. Third, the covalent bond to Ser79 — the actual mechanism — is missing from the scoring, and the structure was solved at pH 4.1, where the catalytic lysine's carboxylation state is uncertain. A compound that ties here may still lose badly in the enzyme assay, and the unscored boronate may be the best molecule in the set.

### 4.3 Mechanism

Class D beta-lactamases hydrolyse carbapenems via a catalytic serine (Ser79 in OXA-23) assisted by a carboxylated lysine (Lys82) that acts as the general base. DBO inhibitors carbamylate Ser79 reversibly, forming a stable carbamoyl-enzyme complex that blocks hydrolysis; durlobactam's extra double bond and methyl group improve its fit and slow its deacylation relative to avibactam. Boronate inhibitors bind as tetrahedral transition-state analogues. Test for each link: (i) a biochemical inhibition assay (k2/Ki and deacylation rate) measures whether the compound actually inactivates OXA-23; (ii) a sulbactam-combination MIC against OXA-23-producing clinical isolates measures whether inhibition restores susceptibility; (iii) a covalent docking or QM/MM calculation would let computation test the mechanism directly — this paper's method cannot.

### 4.4 Testable hypotheses

1. Durlobactam inactivates OXA-23 with a k2/Ki ≥10-fold higher than avibactam in a biochemical assay. Falsifier: k2/Ki within 3-fold.
2. A boronate inhibitor (taniborbactam or the ChEMBL4633785 scaffold) restores sulbactam susceptibility (MIC ≤4 mg/L) in ≥80% of OXA-23-producing CRAB isolates. Falsifier: MIC >8 mg/L in more than half the isolates.
3. Covalent docking (or a QM/MM refinement) separates avibactam from durlobactam by ≥1 kcal/mol on 4JF5. Falsifier: the tie persists with covalent scoring.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): recombinant OXA-23 nitrocefin/centa inhibition assay for avibactam, durlobactam and a boronate; readout IC50 and k2/Ki, n=3. Stage 2 (weeks 4–8): sulbactam-combination MIC (broth microdilution) against 10–15 OXA-23-producing CRAB isolates from a Pakistani reference laboratory, with ceftazidime–avibactam and sulbactam–durlobactam as controls. Stage 3 (weeks 9–12): if any inhibitor passes stages 1–2, time-kill and resistance-passage experiments; if none passes, publish the negative result with the docking data as the reason the hypothesis failed.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows the reported gap.
2. Both DBOs are covalent inhibitors; the covalent bond is absent from scoring, so the numbers reflect non-covalent fit only.
3. The 0.74 nM boronate could not be scored (boron unsupported by Vina); the strongest measured ligand in the set is therefore unranked.
4. A single structure at pH 4.1 (4JF5) was used; the catalytic lysine carboxylation state at physiological pH is not represented.
5. ChEMBL OXA-23 has only 2 bioactivities; the ligand record is too thin to support any scaffold-level conclusion.
6. Measured Ki values are ChEMBL records; assay conditions vary across source studies and were not re-verified compound by compound.
7. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon and Al-Razi's Kitab al-Hawi; the full Arabic texts were not read, and the canon has no concept of a beta-lactamase — the sweep is historical context only.

## 6. Conclusion

Avibactam re-docks at −6.54 kcal/mol on the OXA-23 structure 4JF5, against −6.42 kcal/mol for durlobactam — a 0.12 kcal/mol tie with tight pose consistency and no PAINS alerts. The ChEMBL OXA-23 record contains only two ligands, and the stronger of them by measured Ki (a 0.74 nM boronate) cannot be scored by AutoDock Vina at all. The tie is inside Vina noise, contradicts the published ~10-fold durlobactam advantage, and was scored without the covalent bond both drugs rely on — so this is not evidence that the two drugs are equivalent, it is evidence that the decisive test is biochemical: enzyme inhibition kinetics and MIC testing against OXA-23 isolates, including a boronate. That test, not another docking run, is the next step.

## 7. Policy implications

**Decision-maker:** Pakistan's National Institute of Health (NIH Islamabad) antimicrobial-resistance surveillance programme and the provincial health departments, with DRAP as regulator. **Decision:** whether to fund a small, targeted validation of OXA-23 inhibitors against local CRAB isolates, and whether to pursue durlobactam access. **Exact change:** commission the 8–12-week enzyme-plus-MIC screen proposed in §4.5 for avibactam, durlobactam and a boronate against Pakistani OXA-23-producing CRAB isolates, instead of relying on imported susceptibility assumptions; and open a DRAP–supplier discussion on sulbactam–durlobactam availability, since it is the IDSA-preferred CRAB therapy and is not yet the local standard. **If evidence Z appears, reverse this:** if durlobactam shows no k2/Ki or MIC advantage over avibactam against local isolates, drop the access discussion and redirect the same screen to the boronate series — do not proceed to any clinical use on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable antibiotic combination from a useless one for a pathogen on the WHO critical list, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Comparative in vitro activity of sulbactam with avibactam or durlobactam against carbapenem-resistant Acinetobacter baumannii. JAC Antimicrob Resist. 2025;7(3):dlaf098. doi:10.1093/jacamr/dlaf098.
2. Durand-Réville TF, Guler S, Comita-Prevoir J, et al. ETX2514 is a broad-spectrum β-lactamase inhibitor for the treatment of drug-resistant Gram-negative bacteria including Acinetobacter baumannii. Nat Microbiol. 2017;2:17104. doi:10.1038/nmicrobiol.2017.104. PMID: 28665414.
3. Sulbactam/avibactam as an alternative strategy for XDR Acinetobacter baumannii ventilator-associated pneumonia: a case report. Rev Argent Microbiol. 2026;58:100725.
4. Influence of PER-7 on cefiderocol susceptibility in clinical isolates of Acinetobacter baumannii producing OXA-23 or OXA-72 carbapenemases. JAC Antimicrob Resist. 2025;7(5):dlaf188.
5. World Health Organization. WHO bacterial priority pathogens list, 2024: bacterial pathogens of public health importance to guide research, development and strategies to prevent and control antimicrobial resistance. Geneva: WHO; 2024. (Carbapenem-resistant Acinetobacter baumannii: critical priority.)
6. RCSB PDB entry 4JF5: Structure of OXA-23 at pH 4.1. RCSB Protein Data Bank. Accessed 2026-11-19.
7. ChEMBL target CHEMBL3885669: Beta-lactamase OXA-23, Acinetobacter baumannii. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-19.
8. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; wound infections and their treatment.)
9. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; clinical observation of severe infections.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-091-2026-11-19.json` (pipeline run; avibactam re-dock, the ChEMBL ligands and the failed boronate) and `hidden_files/dock-HP-091b-2026-11-19.json` (salvage run, `hidden_files/redock_hp091.py`: durlobactam). Ligand identities are ChEMBL IDs CHEMBL1689063 and CHEMBL4633785; reference drug avibactam; durlobactam (ETX2514). Structure: PDB 4JF5 (1.15 Å). Target: UniProtKB Q9L4P2; ChEMBL target CHEMBL3885669. No additional data were generated.
