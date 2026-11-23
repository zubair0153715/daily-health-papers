# The HBV Polymerase Benchmark Cannot Run: No Experimental Structure, No ChEMBL Target — and What the Organism-Level Data Say About Tenofovir

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-22 · **Health Papers Agent — Paper #95** (daily 5-paper run)

**Keywords:** hepatitis B virus; HBV polymerase; tenofovir; entecavir; molecular docking; ChEMBL; drug resistance; AlphaFold

---

## Abstract

Chronic hepatitis B infects an estimated 254 million people and killed about 1.1 million in 2022, yet only 13% of those infected have been diagnosed and 3% treated — and Pakistan alone carries an estimated 12.6 million of the combined hepatitis B and C burden. Tenofovir is the first-line nucleos(t)ide analogue, but it rarely achieves a functional cure because covalently closed circular DNA persists in hepatocytes, and long-term therapy selects resistance mutations. We asked whether any measured anti-HBV compound binds the viral polymerase more strongly than tenofovir, using the LeadForge pipeline (UniProtKB → ChEMBL → PubChem/RDKit → AutoDock Vina 1.2.7) with tenofovir disoproxil fumarate as the reference drug. The benchmark cannot run, and this paper documents exactly why: the pipeline's first run resolved the target to the wrong protein entirely — human RNA helicase DDX3X (UniProtKB O00571) — and its corrected run resolved the true target, HBV Protein P (UniProtKB P03156, genotype D, 832 amino acids), but ChEMBL holds no single-protein HBV polymerase target, and the pipeline's fallback then silently selected an unrelated human target (ABCC9, CHEMBL1971), whose 41 bioactivities were discarded. No experimental high-resolution structure of HBV polymerase exists — the only structural record is a 14.5 Å cryo-EM density of the encapsidated enzyme — so docking was skipped rather than run on a substitute. The usable evidence is organism-level: ChEMBL target CHEMBL613497 (Hepatitis B virus) holds 3,659 potency records with pChEMBL values across 2,513 molecules, topped by entecavir (IC50 0.06 nM in dHepaRG cells) and tenofovir (EC50 0.064 nM in HepG2.2.15 cells) — but those two numbers come from different assays and the tenofovir value sits far below the published micromolar range for the same cell line, so no head-to-head ranking can be built on them. The honest limit: no docking score exists in this paper, no analogue can be claimed to beat tenofovir, and the claim that the benchmark is impossible would be refuted by the deposition of a single high-resolution HBV polymerase structure with a bound inhibitor. The falsifiable next step is an 8–12-week validation of an AlphaFold-based HBV polymerase model against the published deep-mutational-scanning fitness map, followed by a HepG2.2.15 antiviral assay of the best-scoring tenofovir analogues.

---

## 1. Introduction

Chronic hepatitis B virus (HBV) infection is one of the largest untreated epidemics in the world. The World Health Organization's Global Hepatitis Report 2024 estimates that 254 million people were living with chronic HBV infection in 2022, that about 1.2 million people became newly infected that year, and that roughly 1.1 million died from HBV-related cirrhosis or hepatocellular carcinoma — more deaths than tuberculosis caused in 2023. Only 13% of the 254 million had been diagnosed and only 3% had received antiviral treatment. The burden is concentrated: five countries — China (83.7 million), India (35.3 million), Indonesia (18.9 million), Nigeria (15.7 million) and Pakistan (12.6 million) — account for 55% of the combined global HBV and HCV burden. In Pakistan, where this paper's author studies pharmacy, hepatitis B is therefore not a distant problem; it is the disease in the next ward.

The drugs that exist work, and they do not cure. Tenofovir (as the disoproxil fumarate or alafenamide prodrug) and entecavir are the first-line nucleos(t)ide analogues recommended by the WHO 2024 guidelines: once inside the hepatocyte they are phosphorylated to their active diphosphate/triphosphate forms, compete with the natural substrate deoxyadenosine triphosphate for incorporation by the HBV polymerase, and terminate the growing viral DNA chain because they lack a 3′-hydroxyl group. They suppress viral replication, reduce progression of liver disease and lower hepatocellular carcinoma incidence — but they rarely achieve a functional cure, because the covalently closed circular DNA (cccDNA) template persists in the hepatocyte nucleus, and because long-term therapy selects resistance mutations in the polymerase: rtL180M/rtM204(I/V) for lamivudine, entecavir and telbivudine, and rtA181V/rtN236T for adefovir and tenofovir. Resistance develops very slowly for entecavir and tenofovir, which is why they remain first-line — but "very slowly" is not "never", and a patient who has taken tenofovir for a decade with detectable virus has few options left.

The question this paper asks is the standard one for this series: among compounds with measured anti-HBV potency already in ChEMBL, does any bind the HBV polymerase more strongly than tenofovir itself? The answer turns out to be that the question cannot be asked in that form yet — and the reason is not a lack of compounds but a lack of infrastructure: no target record and no structure. That negative answer is the paper. A benchmark that cannot run is worth documenting precisely, because every future HBV polymerase docking study will hit the same two walls, and because the pipeline that produced this paper hit a third wall of its own — it resolved the target to the wrong protein twice before the audit caught it.

The classical medical canon knew the organ long before it knew the virus: Ibn Sina's Canon of Medicine (c. 1025) treats diseases of the liver (amrad al-kabid), including jaundice and chronic liver disease, with dietary and supportive management — the Canon knows the syndrome, not the target. These texts are hypothesis sources, not evidence, but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL ligands with measured anti-HBV potency bind the HBV polymerase (UniProtKB P03156) more strongly than tenofovir, as measured by standardised AutoDock Vina docking on an experimental structure? **Falsifier:** the deposition of a single high-resolution HBV polymerase structure with a bound inhibitor, on which tenofovir re-docks and a ligand out-scores it beyond Vina noise, refutes the claim that the benchmark cannot run. **Causal identification:** validated-control re-docking — the approved drug re-docked on a co-crystal structure of its own target — is the method this series uses, and it is unavailable here; association only beyond that. The absence of a structure is a fact about the field, not a failure of this run.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-22: the WHO Global Hepatitis Report 2024 and the WHO 2024 chronic hepatitis B guidelines; the 2022 global burden analysis (Cui et al., Lancet Gastroenterology & Hepatology 2026); the nucleos(t)ide analogue mechanism and resistance review (Menendez-Arias et al., Current Opinion in Virology 2014; PMID 24814823); the only structural record of the enzyme (Wang et al., Proceedings of the National Academy of Sciences 2014; PMID 25034253); the deep mutational scanning fitness map of HBV polymerase (Yu et al., Cell 2024; PMID 38723628); the full-length homology-model study (Patil et al., Journal of Biomolecular Structure and Dynamics 2024); the ChEMBL target search and the UniProtKB records for P03156 and O00571; and the Islamic-canon sweep (Ibn Sina, Al-Qanun fi al-Tibb, c. 1025 — consulted in the literature-map summaries, not in full Arabic text; see Limitations).

### 2.2 Target identification — resolved to the wrong protein twice, caught and corrected

The pipeline's first run, on the text query "Hepatitis B virus polymerase", resolved the target to human ATP-dependent RNA helicase DDX3X (UniProtKB O00571; ChEMBL CHEMBL5553, 57 bioactivities). DDX3X is a real HBV-relevant host protein — it interacts with viral proteins — but it is not the HBV polymerase, and its 26 ranked leads are DDX3X ligands, not HBV polymerase ligands. That run is discarded in full. The error class is the same as the TYK2 wrong-domain error in this series (Paper #92): the pipeline's target search prefers human entries, and a text query that names a virus returns a human protein that the virus touches.

The corrected run used the accession directly ("P03156") and resolved the true target: HBV Protein P, UniProtKB P03156, Hepatitis B virus genotype D subtype ayw (isolate France/Tiollais/1979), 832 amino acids — a multifunctional enzyme that converts the viral RNA genome into double-stranded DNA inside cytoplasmic capsids, with DNA-directed DNA polymerase activity, RNA-directed DNA polymerase (reverse transcriptase) activity, and RNase H activity, and with protein priming at the epsilon loop of the pregenomic RNA. **Verify the UniProt accession, the ChEMBL target name, the PDB title, the domain and the ligand identity before any score is quoted** — that audit rule, written after Paper #92, is what caught both errors here.

### 2.3 The ChEMBL gap — no single-protein HBV polymerase target exists

With the correct accession, the pipeline's precise lookup (ChEMBL target by UniProt accession P03156) returned zero targets, verified live 2026-11-22. A ChEMBL target search for "Hepatitis B virus polymerase" returns no single-protein HBV polymerase target either; the closest record is CHEMBL613497, "Hepatitis B virus", an ORGANISM-level target holding whole-virus and cell-based assay data. The pipeline's fallback then silently selected an unrelated human target — ATP-binding cassette sub-family C member 9 (ABCC9, CHEMBL1971) — because the gene symbol of P03156 is "P" and the fallback matches any target name containing that letter. Its 41 bioactivities and 26 ranked leads are ABCC9 ligands and are discarded with the DDX3X set. The fallback is a defect, not a feature: a one-letter gene symbol must never select a target, and this paper is the report that proves it. The two discarded runs are preserved in `hidden_files/dock-HP-089-2026-11-22.json` (the corrected run, including the discarded ABCC9 ligand set) and disclosed here, not deleted.

### 2.4 Organism-level ligand data — the only usable ChEMBL evidence

Because no enzyme-level target exists, the ligand evidence was pulled directly from the organism-level target CHEMBL613497 with a dedicated script (`health-papers-agent/hbv_organism_activities.py`, ChEMBL API, live 2026-11-22): all EC50/IC50 activities with a pChEMBL value, 3,659 records across 2,513 molecules, ranked by pChEMBL. Molecule names for the top entries were verified against the ChEMBL molecule records. These are whole-virus and cell-based potencies (HepG2.2.15, HepG2-hNTCP, dHepaRG cells), not enzyme inhibition — the distinction is stated in every row of the table, because a cell EC50 is not a polymerase Ki and cannot be compared with one.

### 2.5 Molecular docking — skipped, and why no substitute was used

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3 — except that it was not run. The pipeline's docking step returned `no_pdb_found`: there is no experimental high-resolution structure of HBV polymerase in the Protein Data Bank. The only structural record is the 14.5 Å cryo-EM density of the encapsidated reverse transcriptase inside authentic RNA-filled cores (Wang et al. 2014; EMDB EMD-2509), which resolves a donut-shaped density, not an atomic active site. Published docking on HBV polymerase therefore uses homology models extrapolated from HIV-1 reverse transcriptase (Das et al. 2001; Chong & Chu 2002) or, more recently, full-length models built with Phyre2/Modeller (Patil et al. 2024) and AlphaFold 2 predictions (Yu et al. 2024). This paper does not dock on any of those models: a homology model is a hypothesis about the active site, and a docking score on a hypothesised pocket is a model-on-model number that cannot be falsified against a crystal structure. The reference drug was verified computationally instead: tenofovir disoproxil fumarate, PubChem CID 6398764, RDKit descriptors computed live (molecular weight 635.52 as the fumarate salt, logP 2.75, 3 hydrogen-bond donors, 16 acceptors, TPSA 260.04 Å², 15 rotatable bonds, 2 Lipinski violations — expected for a prodrug salt — PAINS-clean, maximum Tox21 kNN probability 0.196).

### 2.6 Honesty limits

No docking score exists in this paper. No analogue can be claimed to beat tenofovir. The organism-level potencies in §3.2 are cell-based EC50/IC50 values from different assays, cell lines and readouts, and are not comparable head to head. The tenofovir value in the table conflicts with the published range for the same cell line and is flagged, not smoothed over. No experimental data were generated in this study.

## 3. Results

### 3.1 The audit table — two wrong resolutions, one correct target, no structure

| Step | What the pipeline did | Result | Verdict |
|---|---|---|---|
| Target, text query "Hepatitis B virus polymerase" | UniProtKB search, human preferred | Human DDX3X (O00571), ChEMBL CHEMBL5553, 57 bioactivities | Wrong protein — discarded |
| Target, accession "P03156" | UniProtKB direct | HBV Protein P (P03156), genotype D, 832 aa | Correct target |
| ChEMBL target by accession P03156 | Precise lookup | Zero targets | No enzyme-level target exists |
| ChEMBL fallback | Text search, gene "P" match | Human ABCC9 (CHEMBL1971), 41 bioactivities, 26 leads | Wrong protein — discarded |
| Structure search | RCSB PDB, live | No experimental structure | Docking skipped (`no_pdb_found`) |
| Organism-level pull | ChEMBL CHEMBL613497 | 3,659 pChEMBL records, 2,513 molecules | Usable evidence (§3.2) |

### 3.2 Organism-level potencies — the strongest measured anti-HBV compounds in ChEMBL

| Molecule (ChEMBL ID) | Best recorded potency | Assay (cell line, readout) |
|---|---|---|
| Entecavir (CHEMBL5314362) | IC50 0.06 nM (pChEMBL 10.22) | dHepaRG cells, extracellular viral DNA by qPCR, 6 days (CHEMBL4269044) |
| Tenofovir, anhydrous (CHEMBL483) | EC50 0.064 nM (pChEMBL 10.19) | HepG2.2.15 cells, viral DNA by PCR, 6 days (CHEMBL4606644) |
| Unnamed investigational (CHEMBL5285547) | EC50 0.1 nM (pChEMBL 10.0) | HepG2.2.15 cells (CHEMBL5246443) |
| Unnamed investigational (CHEMBL4875146) | EC50 0.2 nM (pChEMBL 9.7) | HepG2-hNTCP cells, HBV DNA, washout design (CHEMBL4841965) |
| Unnamed investigational (CHEMBL5206918) | IC50 0.2 nM (pChEMBL 9.7) | HepG2.2.15 cells, HBsAg in supernatant (CHEMBL5140686) |
| Unnamed investigational (CHEMBL5180441) | IC50 0.2 nM (pChEMBL 9.7) | HepG2.2.15 cells, HBsAg in supernatant (CHEMBL5140686) |
| Unnamed investigational (CHEMBL4647919) | EC50 0.25 nM (pChEMBL 9.6) | HepG2.A64 cells, rtL180M/T184L/M204V mutant, viral replication (CHEMBL4606642) |
| Unnamed investigational (CHEMBL4859319) | EC50 0.27 nM (pChEMBL 9.57) | HepG2-hNTCP cells, HBV DNA, washout design (CHEMBL4841965) |

Two things are visible in this table and both matter. First, the two approved drugs sit at the top of the entire ChEMBL organism-level record — entecavir and tenofovir are the most potent measured anti-HBV compounds in the database, ahead of every investigational molecule in the top eight. Second, the table is not a ranking: entecavir's 0.06 nM was measured in dHepaRG cells by extracellular viral DNA, tenofovir's 0.064 nM in HepG2.2.15 cells by viral DNA, and the HBsAg readouts measure a different endpoint again. A 0.004 nM gap between two drugs in two different assays is not a difference; it is two different experiments. The most useful row is the seventh: CHEMBL4647919 holds EC50 0.25 nM against the rtL180M/T184L/M204V triple mutant — the entecavir-resistance genotype — in HepG2.A64 cells. That is the only row in the top eight that speaks to the resistance problem at all, and its molecule is unnamed in ChEMBL.

### 3.3 The tenofovir value conflicts with the published range — flagged, not hidden

The tenofovir record in §3.2 (EC50 0.064 nM, HepG2.2.15, activity 20613339, assay CHEMBL4606644) sits far below the published micromolar range for tenofovir in the same cell line — the comparative literature reports tenofovir EC50 values around 1 µM in HepG2.2.15 cells, roughly four orders of magnitude higher. One of the two must be wrong for this assay, or the record carries a unit or compound-form error that ChEMBL does not flag. This paper does not resolve the conflict; it reports the record exactly as ChEMBL holds it, with its activity and assay IDs so any reader can check it, and it does not build any claim on the number. The lesson generalises: a ChEMBL pChEMBL ranking across assays is a triage list, not a league table, and a single anomalous record at the top of the list is a reason to verify, not a reason to celebrate. The entecavir record (IC50 0.06 nM, dHepaRG, activity 18775795) is consistent with entecavir's known sub-nanomolar potency and is not flagged the same way.

### 3.4 The resistance landscape the benchmark would have to address

The resistance mutations are the reason a successor to tenofovir is wanted at all. Lamivudine resistance (rtM204V/I, usually with rtL180M) emerges in a large fraction of patients within years; entecavir resistance requires rtL180M + rtM204V/I plus an additional change (rtT184, rtS202 or rtM250) and develops very slowly; adefovir resistance (rtA181V, rtN236T) is uncommon; tenofovir resistance is the slowest of all, with rtA181V/rtN236T the documented pattern and no single mutation conferring high-level resistance. The deep mutational scanning fitness map (Yu et al. 2024) now gives this landscape a residue-level basis: nearly every single-codon variant of the polymerase was assayed for fitness, the map identifies the conserved prolines that stall ribosomes and enforce the polymerase's cis-preference for its own pregenomic RNA, and an AlphaFold 2 model of the polymerase was used to relate the fitness map to structure. That map — not a docking score — is the best available guide to which polymerase residues a new inhibitor must engage and which mutations it must survive.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since tenofovir was approved. Before approval, the question was "can the HBV polymerase be inhibited at all?" — now it is "which molecule, if any, beats tenofovir, and on what evidence?" The benchmark protocol this series uses — re-dock the approved drug on its own co-crystal structure, then dock the analogues on the same structure — cannot run for HBV polymerase, because the structure does not exist and the target record does not exist. The paper's contribution is therefore infrastructural: it names the two missing pieces, proves they are missing with live queries rather than asserting it, and shows what evidence does exist (organism-level potencies) and what it cannot do (rank drugs across assays). A field that cannot benchmark its own reference drug cannot tell whether its docking papers are measuring binding or measuring the homology model.

### 4.2 Why the "win" must not be over-read

There is no win in this paper, and that is the point. Three reasons the organism-level table must not be read as a ranking: first, the assays differ in cell line (dHepaRG vs HepG2.2.15 vs HepG2-hNTCP), readout (viral DNA vs HBsAg) and duration; second, the tenofovir value conflicts with the published range for the same cell line by four orders of magnitude; third, a cell EC50 conflates polymerase inhibition with cell entry, phosphorylation, efflux and cytotoxicity, so it cannot rank polymerase binders at all. The two discarded pipeline runs are a fourth reason for caution in general: a pipeline that silently substitutes a human helicase or a human ABC transporter for a viral polymerase will produce a complete, plausible-looking ranking that survives any check that does not verify the target accession.

### 4.3 Mechanism

Tenofovir diphosphate competes with dATP at the polymerase active site and terminates chain elongation; entecavir triphosphate competes with dGTP and additionally impairs protein priming. Test for each link: (i) a polymerase activity assay on a purified or reconstituted HBV polymerase measures inhibition directly against tenofovir as comparator — this assay does not exist in a standardised form today, which is itself part of the infrastructure gap; (ii) a HepG2.2.15 antiviral assay measures viral DNA reduction at matched concentrations, with a cytotoxicity counter-screen (CC50) so that a potent-looking compound is not simply a toxic one; (iii) a resistance panel — wild-type plus rtL180M/rtM204V, rtA181V/rtN236T and the entecavir-resistance triple mutant — measures whether the analogue keeps activity where the approved drugs lose it, because a molecule that only beats tenofovir on wild-type virus is not a successor.

### 4.4 Testable hypotheses

1. An AlphaFold 2 model of HBV Protein P, validated against the Yu et al. deep-mutational-scanning fitness map, predicts the resistance mutations (rtM204V/I, rtA181V, rtN236T) as residues whose mutation preserves fitness while reducing inhibitor binding. Falsifier: the model places those residues outside the predicted active site.
2. The unnamed investigational compound CHEMBL4647919 inhibits the rtL180M/T184L/M204V triple mutant in HepG2.A64 cells at an EC50 within 3-fold of its recorded 0.25 nM. Falsifier: EC50 worse than 1 nM on re-test.
3. Tenofovir's recorded EC50 of 0.064 nM in assay CHEMBL4606644 does not reproduce in a fresh HepG2.2.15 viral-DNA assay. Falsifier: the fresh assay returns a value within 3-fold of 0.064 nM, which would force a revision of the published micromolar range instead.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): build the AlphaFold 2 model of HBV Protein P (P03156) and validate it against the published deep-mutational-scanning fitness map — the model must place the known resistance residues in or adjacent to the active site and must reproduce the fitness cost of mutating the YMDD motif. Stage 2 (weeks 4–8): HepG2.2.15 antiviral assay for tenofovir, entecavir and the two best-characterised investigational compounds from §3.2, with CC50 counter-screen, n=3, same readout (viral DNA by qPCR) and same duration for all four — the first head-to-head comparison in this paper's evidence base. Stage 3 (weeks 9–12): resistance-panel assay (wild-type plus the three mutant genotypes in §4.3) for the best compound from stage 2; if none beats tenofovir on the panel, publish the negative result with the organism-level data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. No docking was run; no docking score exists in this paper. The benchmark is impossible on current infrastructure, and that is the finding, not an omission to be filled by a substitute structure.
2. The organism-level potencies are cell-based EC50/IC50 values from different assays, cell lines and readouts; they cannot rank drugs head to head.
3. The tenofovir EC50 of 0.064 nM conflicts with the published micromolar range for the same cell line by roughly four orders of magnitude; the conflict is unresolved.
4. Two pipeline runs resolved the target to the wrong protein (DDX3X, then ABCC9 via a one-letter gene-symbol fallback); the audit caught both, but the episode shows the pipeline's target resolution needs independent verification every run — and the fallback must be fixed so a one-letter gene symbol can never select a target.
5. The homology-model literature (Das et al. 2001; Chong & Chu 2002; Patil et al. 2024) and the AlphaFold model (Yu et al. 2024) were read as published summaries; no model was built or validated in this study.
6. No data on the clinical confounder: only 13% of people with chronic HBV have been diagnosed and 3% treated, so the binding question is secondary to the access question for most patients.
7. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon; the full Arabic text was not read, and other classical works on liver disease were not individually consulted.

## 6. Conclusion

Tenofovir remains the reference drug for chronic hepatitis B, and this paper cannot say whether any compound beats it on the polymerase — because the benchmark cannot run. ChEMBL holds no single-protein HBV polymerase target, no experimental high-resolution structure of the enzyme exists, and the pipeline that attempted the benchmark resolved the target to the wrong protein twice (human DDX3X, then human ABCC9) before the audit caught it. What does exist is organism-level evidence: 3,659 potency records across 2,513 molecules, topped by entecavir and tenofovir themselves, with one investigational compound active at 0.25 nM against the entecavir-resistance triple mutant — but those numbers come from different assays and the tenofovir record conflicts with the published range, so no ranking can be built on them. The next step is not another docking run on a homology model; it is the cheap, decisive infrastructure work — validate an AlphaFold model of HBV Protein P against the deep-mutational-scanning fitness map, then run a single head-to-head HepG2.2.15 assay of tenofovir, entecavir and the best investigational compounds on the same readout. Until that exists, any HBV polymerase docking score should be read as a score against a hypothesis, not against the enzyme.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Higher Education Commission research-funding panels, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund HBV polymerase structure-and-assay infrastructure — an AlphaFold-model validation plus a standardised HepG2.2.15 assay — instead of funding another purely computational screen of a target with no structure. **Exact change:** commission the 8–12-week validation proposed in §4.5 for the HBV polymerase, and, in parallel, ask DRAP's registration reviewers to note that tenofovir's ChEMBL record contains a four-orders-of-magnitude discrepancy for the same cell line — a single anomalous potency record must not anchor a procurement or formulary decision without a fresh assay. **If evidence Z appears, reverse this:** if a high-resolution HBV polymerase structure is deposited, drop the infrastructure-first recommendation and fund the docking benchmark on that structure immediately; if the fresh assay reproduces tenofovir at 0.064 nM, revise the published potency range instead of discarding the record. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable HBV drug from a useless one for a disease that kills about 1.1 million people a year — 12.6 million of them in Pakistan — running the test is the obligation; prescribing on an untested docking score, or on an unverified database record, would violate it. The evidence here is thin — no docking, no enzyme assay — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. World Health Organization. Global hepatitis report 2024: action for access in low- and middle-income countries. Geneva: WHO; 2024.
2. Cui F, et al. The burden of chronic hepatitis B and C in 2022 and progress towards elimination: a global report. Lancet Gastroenterol Hepatol. 2026. doi:10.1016/S2468-1253(25)00375-9.
3. World Health Organization. Guidelines for the prevention, diagnosis, care and treatment for people with chronic hepatitis B infection. Geneva: WHO; 2024. ISBN 978-92-4-009090-3.
4. Menendez-Arias L, Alvarez M, Pacheco B. Nucleoside/nucleotide analog inhibitors of hepatitis B virus polymerase: mechanism of action and resistance. Curr Opin Virol. 2014;8:1-9. doi:10.1016/j.coviro.2014.04.005. PMID: 24814823.
5. Wang JC-Y, Nickens DG, Lentz TB, Loeb DD, Zlotnick A. Encapsidated hepatitis B virus reverse transcriptase is poised on an ordered RNA lattice. Proc Natl Acad Sci U S A. 2014;111(31):11329-11334. doi:10.1073/pnas.1321424111. PMID: 25034253.
6. Yu Y, Kass MA, Zhang M, Youssef N, Freije CA, Brock KP, Aguado LC, Seifert LL, Venkittu S, Hong X, Shlomai A, de Jong YP, Marks DS, Rice CM, Schneider WM. Deep mutational scanning of hepatitis B virus reveals a mechanism for cis-preferential reverse transcription. Cell. 2024;187(11):2735-2745.e12. doi:10.1016/j.cell.2024.04.008. PMID: 38723628.
7. Patil VS, Harish DR, Charla R, Vetrivel U, Jalalpure SS, Bhandare VV, Deshpande SH, Hegde HV, Roy S. Structural insights into modeling of hepatitis B virus reverse transcriptase and identification of its inhibitors from potential medicinal plants of Western Ghats: an in silico and in vitro study. J Biomol Struct Dyn. 2024;42(21):11731-11749. doi:10.1080/07391102.2023.2264400.
8. ChEMBL target CHEMBL613497: Hepatitis B virus (organism). ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-22.
9. UniProtKB P03156: Protein P, Hepatitis B virus genotype D subtype ayw. UniProt. Accessed 2026-11-22.
10. UniProtKB O00571: ATP-dependent RNA helicase DDX3X, Homo sapiens. UniProt. Accessed 2026-11-22.
11. PubChem CID 6398764: tenofovir disoproxil fumarate. National Library of Medicine. Accessed 2026-11-22.
12. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; diseases of the liver, amrad al-kabid.)

## Data availability

All numbers reported here are in `hidden_files/dock-HP-089-2026-11-22.json` (corrected P03156 pipeline run, including the discarded ABCC9/CHEMBL1971 ligand set) and `hidden_files/hbv-organism-activities-2026-11-22.json` (3,659 ChEMBL organism-level potency records for CHEMBL613497, top 30 by pChEMBL). Reference drug tenofovir disoproxil fumarate (PubChem CID 6398764). Target: UniProtKB P03156; no ChEMBL single-protein target exists; organism-level target ChEMBL CHEMBL613497. No docking was run: no experimental HBV polymerase structure exists. No additional data were generated.
