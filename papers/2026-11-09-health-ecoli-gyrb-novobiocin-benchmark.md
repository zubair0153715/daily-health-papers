# No Lead Beats Novobiocin Beyond Noise on Escherichia coli GyrB: A Corrected Vina Benchmark on 7P2M and the Wrong-Site Comparator Problem

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-09 · **Health Papers Agent — Paper HP-015** (daily 5-paper run)

**Keywords:** DNA gyrase; GyrB; Escherichia coli; novobiocin; ciprofloxacin; fluoroquinolone resistance; molecular docking; AutoDock Vina

---

## Abstract

Fluoroquinolone resistance in Gram-negative bacteria is driven by mutations in the quinolone-resistance-determining region of gyrA (S83L, D87N) and parC (S80I) — the GyrA subunit and topoisomerase IV, not GyrB. The GyrB ATPase site is therefore a resistance-bypassing target, and its classic inhibitor is novobiocin. We ran the LeadForge pipeline live on 9 November 2026 (UniProtKB P0AES6 → ChEMBL CHEMBL1826, 50 ligands → RDKit → PAINS/ADMET → AutoDock Vina 1.2.7 on PDB 7P2M, 1.16 Å, grid 0.01 Å from the co-crystallised inhibitor centroid). A first pipeline run resolved the wrong target (Thermus thermophilus GyrB plus human maltase-glucoamylase, CHEMBL2074) and was discarded. In the corrected run, four GyrB ATPase-domain inhibitors (measured IC50 3–8 nM) docked at −7.17 to −8.78 kcal/mol. The best, CHEMBL4293447 (−8.78), beats the true ATP-site reference novobiocin (−7.76, Kd 28 nM) by 1.02 kcal/mol — inside Vina's ±1–2 kcal/mol noise — and beats ciprofloxacin (−7.26) by 1.52 kcal/mol, also inside noise. Ciprofloxacin does not bind the GyrB ATP site at all (it binds the GyrA–DNA cleavage complex), so its respectable score shows absolute Vina scores are not evidence of binding. The falsifiable next step is a head-to-head E. coli GyrB ATPase assay of CHEMBL4293447, CHEMBL4294536 and novobiocin under identical conditions, plus MICs against gyrA S83L/D87N mutants to test the resistance-bypass claim directly.

---

## 1. Introduction

Bacterial antimicrobial resistance directly caused an estimated 1.27 million deaths in 2019 (Murray et al., 2022), and the WHO 2024 Bacterial Priority Pathogens List ranks carbapenem- and third-generation-cephalosporin-resistant Enterobacterales — the family containing *Escherichia coli* and *Klebsiella pneumoniae* — as a critical priority. Fluoroquinolones, once the workhorse oral therapy for Gram-negative infection, are now WHO Watch-group antibiotics, restricted to a limited set of indications because resistance is widespread. In *E. coli*, high-level fluoroquinolone resistance is caused by sequential chromosomal mutations in the quinolone-resistance-determining region (QRDR): gyrA S83L first, then parC S80I, then gyrA D87N, with ciprofloxacin MICs rising to 8–32 mg/L and beyond (Microorganisms, 2023; the same S83L/D87N/S80I panel was reported in wildlife *E. coli* isolates, Scientific Reports, doi:10.1038/s41598-025-18971-2). All of those mutations sit in GyrA and ParC — the subunits that cut and rejoin DNA. None of them touches GyrB.

DNA gyrase is an A2B2 heterotetramer: GyrA performs DNA breakage and reunion, GyrB hydrolyses ATP to power the supercoiling cycle (Champoux, 2001). The GyrB ATPase site is a structurally separate pocket from the fluoroquinolone site, which means a GyrB inhibitor should, in principle, retain activity against every QRDR mutant. The proof that the site is druggable is old: novobiocin, an aminocoumarin licensed in 1964 as Albamycin, is a competitive inhibitor of the GyrB ATPase reaction, binding the N-terminal ATP pocket with nanomolar affinity (ChEMBL record CHEMBL36506; Kd 28 nM against *E. coli* GyrB). Its oral form was withdrawn for lack of efficacy, and it weakly inhibits human Hsp90 — but as a target-site proof it stands. The site has been re-validated recently: Cotman et al. (2023) developed benzothiazole GyrB ATP-pocket inhibitors with potent activity against *Acinetobacter baumannii* and *Pseudomonas aeruginosa*, both WHO-priority pathogens, with no cross-resistance to novobiocin, and solved the *E. coli* GyrB24 co-crystal structure 7P2M (1.16 Å) with their inhibitor LMD43.

This paper asks a narrow, testable question: among the known *E. coli* GyrB ligands in ChEMBL, is there one that docks better than novobiocin on 7P2M, matches or beats its measured potency, and is more drug-like — and does the standard comparator, ciprofloxacin, even belong in the comparison? The falsifiable hypothesis is that at least one known GyrB inhibitor beats novobiocin beyond Vina's noise floor on a correctly centred grid. The paper tests that hypothesis against the measured ChEMBL potencies, against the noise floor, and against a deliberately included wrong-site control.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 9 November 2026: the daily literature digest at `~/workspace/research-team/digests/2026-11-09.md`, PubMed, ChEMBL (EBI), UniProtKB, PubChem and RCSB PDB. Key sources: Murray et al. (2022) for the AMR mortality burden; WHO (2024) for the priority-pathogens list; Champoux (2001) for the gyrase mechanism; Microorganisms (2023) for the QRDR mutation panel and resistance rates; Cotman et al. (2023) for the 7P2M structure and the benzothiazole series; ChEMBL activity records for the measured potencies below. Every citation in this paper was verified against its publisher or database record on the day of writing; no citation was generated from memory.

### 2.2 Molecular docking — and a discarded first run

The LeadForge pipeline was run live on 9 November 2026 with ciprofloxacin as the query: UniProtKB target identification → ChEMBL bioactivities → PubChem verification → RDKit Morgan-fingerprint similarity screen (25 compounds) → RDKit ADMET/PAINS panel plus ToxGuard Tox21 kNN read-across (12 assays) → composite ranking → AutoDock Vina 1.2.7 docking (box 22.5 Å, exhaustiveness 8, best of 3 poses).

The first run was discarded, and the reason is documented here because it is a fault class, not a footnote. With the topic string "DNA gyrase (GyrB subunit)", the pipeline resolved UniProtKB Q5SHZ4 — DNA gyrase subunit B from *Thermus thermophilus* — and ChEMBL target CHEMBL2074. CHEMBL2074 was verified against the ChEMBL API to be human maltase-glucoamylase (MGAM, UniProt O43451), not a gyrase at all: its 55 "leads" were alpha-glucosidase inhibitors docked onto a thermophile GyrB structure (PDB 6ENH). That run's scores are meaningless and are not reported in this paper; its raw JSON is kept as `hidden_files/dock-HP-015-WRONG-TARGET-2026-11-09.json` for the audit trail. The corrected run used the precise target string "Escherichia coli DNA gyrase subunit B", which resolved UniProtKB P0AES6 (*E. coli* strain K12, DNA gyrase subunit B) and ChEMBL CHEMBL1826 (DNA gyrase subunit B, single protein, *E. coli*, 50 bioactivities). All results below are from the corrected run only. A data-quality note: several of the retrieved ChEMBL ligands contain aluminium and failed RDKit sanitisation (explicit-valence warnings in the run log); they were excluded by the screen and none is in the docked set.

Docking used PDB 7P2M (1.16 Å), *E. coli* GyrB24 in complex with the benzothiazole inhibitor LMD43/EBL2560 (Cotman et al., 2023), auto-picked as the highest-resolution inhibitor-bound structure. Centre audit, performed after the run from the PDB file itself: the docking centre [−18.60, −15.05, 6.55] is 0.01 Å from the centroid of the co-crystallised ligand N1N (LMD43); the only other hetero group, a phosphate ion, is 10.68 Å away — the grid is on the inhibitor's ATP pocket, not on a crystallisation artefact. Novobiocin, the true ATP-site reference, is not among the pipeline's top-5 ranked leads (its similarity to the ciprofloxacin query is low), so it was docked separately with the identical protocol (same structure, centre and box; PubChem CID 54675769) and is reported in the same table. Ciprofloxacin was docked by the pipeline as the QUERY; it is retained in the table as a wrong-site control, not as a comparator — it binds the GyrA–DNA cleavage complex, a different pocket on the same enzyme.

### 2.3 PAINS screen

The RDKit PAINS filter was applied to every ranked lead. All five docked compounds are PAINS-clean; a PAINS alert is reported, never hidden, and none occurred here. The Tox21 kNN read-across panel (12 assays) is reported in the pipeline JSON; no compound in the docked set raised a high-probability toxicity flag.

### 2.4 Honesty limits

Docking is not activity. Vina's scoring error is ±1–2 kcal/mol, so only margins above ~2 kcal/mol are treated as real differences. No experimental data were generated. No molecular dynamics or free-energy refinement was run. Measured potencies are ChEMBL records for the *E. coli* GyrB target and were not re-measured; the four leads' IC50s (3–8 nM) come from a single assay format (inhibition of *E. coli* GyrB residues 1–220) while novobiocin's values come from different assays (Kd, ATPase IC50, supercoiling IC50), so cross-assay comparisons are indicative only. Only five compounds were docked.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | ChEMBL ID | Best affinity (kcal/mol) | Measured potency vs E. coli GyrB (ChEMBL) | MW | logP | Lipinski violations | PAINS |
|---|---|---|---|---|---|---|---|
| CHEMBL4293447 | CHEMBL4293447 | −8.78 | IC50 6.0 nM (pChEMBL 8.22) | 542.59 | 4.90 | 1 | Clean |
| CHEMBL4294536 | CHEMBL4294536 | −7.93 | IC50 3.0 nM (pChEMBL 8.52) | 542.59 | 4.73 | 1 | Clean |
| CHEMBL4278317 | CHEMBL4278317 | −7.84 | IC50 8.0 nM (pChEMBL 8.10) | 554.60 | 4.92 | 1 | Clean |
| Novobiocin (true ATP-site reference) | CHEMBL36506 | −7.76 | Kd 28 nM; IC50 154 nM (ATPase) / 200 nM (supercoiling) | 612.63 | 3.63 | 2 | Clean |
| Ciprofloxacin (QUERY, wrong-site control) | CHEMBL100 | −7.26 | No GyrB ATP-site activity (binds GyrA–DNA) | 331.35 | 1.58 | 0 | Clean |
| CHEMBL4281775 | CHEMBL4281775 | −7.17 | IC50 6.0 nM (pChEMBL 8.22) | 561.59 | 4.41 | 1 | Clean |

The best lead, CHEMBL4293447, beats novobiocin by 1.02 kcal/mol and beats ciprofloxacin by 1.52 kcal/mol. Both margins sit inside Vina's ±1–2 kcal/mol noise: no lead beats either reference beyond noise. The measured potencies tell the same story of a tie: the four leads' IC50s span only 3–8 nM (a 2.7-fold range, within normal assay variation), and the most potent measured compound, CHEMBL4294536 (3.0 nM), ranks only second by docking, while the weakest measured, CHEMBL4278317 (8.0 nM), ranks third. Across the four leads, docking rank and potency rank correlate at Spearman ρ = 0.35 (n = 4, one tied pair) — weak, and with a 2.7-fold potency spread there is almost nothing for a ranker to reproduce. The four leads are one chemotype family: thiazole/pyridine-carboxamide GyrB ATPase-domain inhibitors from a single 2018 *European Journal of Medicinal Chemistry* series (assay on *E. coli* GyrB residues 1–220; e.g. CHEMBL4293447, activity record 18804670, assay CHEMBL4275017). The docked set therefore tests one scaffold four ways, not four scaffolds.

Two controls frame the table. First, ciprofloxacin's −7.26: a compound with no activity at this pocket scores within 1.5 kcal/mol of the best lead. Absolute Vina scores are not evidence of binding; only the margin against a same-site reference means anything, and here the margin against novobiocin is 1.02 kcal/mol — noise. Second, novobiocin's own profile: the reference is the worst compound in the table by drug-likeness (MW 612.63, 2 Lipinski violations, PSA 200.01, withdrawn) and yet the most potent by binding (Kd 28 nM). Every lead beats novobiocin on drug-likeness (MW 542–562, 1 violation) but none beats it on docking beyond noise. The trade the series offers is therefore developability, not potency.

### 3.2 Comparison with published docking

No published Vina benchmark of these four compounds on *E. coli* GyrB was found in the literature sweep, so there is no published docking table to compare against. The structural context is the Cotman et al. (2023) series itself: their compound 27 achieved a 10-fold improved aqueous solubility, 10-fold improved inhibition of topoisomerase IV from *A. baumannii* and *P. aeruginosa*, 10-fold decreased inhibition of human topoisomerase IIα, and no cross-resistance to novobiocin relative to their starting compound 1. Our docked leads predate that optimisation (2018 series) and carry the liabilities Cotman et al. optimised away: MW >540, logP 4.4–4.9, one Lipinski violation each. The 7P2M structure is the optimised series' structure, not the 2018 series' — a mismatch worth stating: the grid is shaped by a benzothiazole (LMD43), while the docked leads are a different chemotype.

### 3.3 The standardisation problem: one scaffold, one assay format, one structure

Three standardisation gaps limit this paper. First, scaffold diversity: all four leads come from one 2018 series, so the benchmark cannot say whether the ATP pocket prefers this chemotype or merely tolerates it. Second, assay format: the leads' IC50s are all from the GyrB 1–220 ATPase-domain assay, while novobiocin's values span binding (Kd 28 nM), ATPase (154 nM) and supercoiling (200 nM) assays — the 5- to 7-fold gap between novobiocin's Kd and its IC50s is a reminder that the leads' 3–8 nM IC50s and novobiocin's 28 nM Kd are not directly comparable quantities. Third, the resistance-bypass claim that motivates the target has not been tested for these leads: no MIC data against gyrA QRDR mutants were in the retrieved records.

## 4. Discussion

### 4.1 The reframe

The paper's hypothesis — that a known GyrB inhibitor beats novobiocin beyond noise — fails on docking and is untestable on measured potency, because the measured potencies are tied. That is not a null result; it reframes the series. The 2018 compounds are already single-digit-nanomolar GyrB inhibitors; the problem they need to solve is not potency but the developability gap the Cotman series later closed (solubility, plasma free fraction, human topoisomerase IIα selectivity). A docking benchmark that rewards only the score will keep re-selecting the same potent-but-heavy scaffold. The useful ranking for this series is a multi-objective one: docking score, solubility, and human topoisomerase IIα selectivity — and the falsifiable claim is about MICs in QRDR mutants, not about a docking margin.

### 4.2 Why the "win" must not be over-read

CHEMBL4293447's −8.78 is the best score in the table and its 1.02 kcal/mol margin over novobiocin is the largest margin available — and it is still noise. The preparation noise measured in this pipeline family is ~0.43 kcal/mol (same molecule docked twice), and Vina's own error is ±1–2 kcal/mol; a 1.02 kcal/mol margin clears neither bar that matters. The ciprofloxacin control (§3.1) shows why the absolute value is not a fallback: −7.26 for a non-binder. Nothing in this table supports prioritising CHEMBL4293447 over novobiocin, or over the other three leads, on docking alone.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

No PAINS alerts occurred in the docked set, so there is no PAINS constraint on the proposed validation beyond the standard ones: aggregation and redox controls in the enzyme assay, and a detergent control in the cell assay. The more relevant artefact risk for this series is the opposite one — the compounds are large, lipophilic (logP 4.4–4.9) and poorly soluble, so apparent potency in a cell assay can be driven by aggregation or membrane partitioning. The validation design therefore includes a solubility measurement and a counter-screen against human topoisomerase IIα (the selectivity liability Cotman et al. optimised against) before any MIC claim.

### 4.4 Testable hypotheses

1. **CHEMBL4293447 inhibits *E. coli* GyrB ATPase more potently than novobiocin under identical conditions.** Measurement: ATPase assay (GyrB 1–220) for CHEMBL4293447, CHEMBL4294536 and novobiocin in the same run, same ATP concentration. Fails if CHEMBL4293447's IC50 is not lower than novobiocin's.
2. **The leads bypass fluoroquinolone resistance.** Measurement: MICs of the four leads and ciprofloxacin against isogenic *E. coli* carrying gyrA S83L, gyrA S83L/D87N and parC S80I. Fails if the leads' MICs rise with the mutants the way ciprofloxacin's do.
3. **The docking margin is a pocket-shape artefact of 7P2M.** Measurement: re-dock all six compounds on the novobiocin-bound *E. coli* GyrB structure 1AJ6 with the same protocol. Fails if CHEMBL4293447 still leads by the same margin.
4. **The series' liability is solubility, not potency.** Measurement: kinetic solubility and human topoisomerase IIα inhibition for the four leads. Fails if solubility is high and human topoisomerase IIα is not inhibited — in which case the Cotman optimisation was unnecessary for this scaffold.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): *E. coli* GyrB (1–220) expression and ATPase assay set-up, novobiocin as the internal control, solubility measurement for the four leads. Stage 2 (weeks 3–6): head-to-head ATPase IC50s in triplicate, plus human topoisomerase IIα counter-screen. Stage 3 (weeks 7–10): MICs against wild-type *E. coli* and the three QRDR-mutant isogenics, with ciprofloxacin as the control. Stage 4 (weeks 11–12): re-docking on 1AJ6 and a go/no-go on hypotheses 1–4. Compound requirement is milligrams; the four leads are research compounds requiring synthesis or a supplier quote, novobiocin and ciprofloxacin are commercially available.

## 5. Limitations

1. Docking only: no experimental data were generated; every number is a Vina score or a ChEMBL record.
2. No lead beats novobiocin beyond Vina's ±1–2 kcal/mol noise; the best margin is 1.02 kcal/mol.
3. Ciprofloxacin is a wrong-site control, not a comparator; its score (−7.26) demonstrates that absolute Vina scores do not establish binding.
4. All four leads are one chemotype from one 2018 series; scaffold diversity is zero.
5. Measured potencies mix assay formats (GyrB 1–220 ATPase IC50s for the leads; Kd, ATPase and supercoiling IC50s for novobiocin); cross-assay comparisons are indicative only.
6. The 7P2M grid is shaped by a benzothiazole (LMD43), not by the docked chemotype; re-docking on the novobiocin-bound 1AJ6 was not run.
7. No MIC data against QRDR mutants were available; the resistance-bypass claim is untested for these leads.
8. The first pipeline run resolved the wrong target (human maltase-glucoamylase) and was discarded; the corrected run is reported, but the fault shows the pipeline's target resolution needs a human check every time.
9. No molecular dynamics, no MM-GBSA rescoring, no human topoisomerase IIα selectivity data for the leads.

## 6. Conclusion

On the high-resolution *E. coli* GyrB structure 7P2M, four known GyrB ATPase-domain inhibitors dock at −7.17 to −8.78 kcal/mol, and the best, CHEMBL4293447, beats the true ATP-site reference novobiocin (−7.76) by only 1.02 kcal/mol — inside Vina's noise. Their measured IC50s (3–8 nM) are essentially tied with each other, and the series' real gap is developability (MW >540, logP ~4.4–4.9), not potency. The honest conclusion is that this benchmark cannot prioritise among these compounds on docking, and that the next experiment is a head-to-head ATPase assay plus MICs against gyrA QRDR mutants — the measurement that would actually test the resistance-bypass claim. No cure claim is made, and no clinical recommendation follows.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. The docking pipeline is the LeadForge pipeline (UniProtKB → ChEMBL → PubChem → RDKit → AutoDock Vina). No funding was received; no conflicts of interest are declared.

## References

1. Murray CJL, Ikuta KS, Sharara F, Swetschinski L, Aguilar GR, Gray A, et al. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399(10325):629-655. doi:10.1016/S0140-6736(21)02724-0. PMID: 35065702. (1.27 million deaths directly attributable to bacterial AMR in 2019.)
2. World Health Organization. WHO Bacterial Priority Pathogens List, 2024. Geneva: WHO; 2024. (Carbapenem- and third-generation-cephalosporin-resistant Enterobacterales: critical priority.)
3. Champoux JJ. DNA topoisomerases: structure, function, and mechanism. Annu Rev Biochem. 2001;70:369-413. doi:10.1146/annurev.biochem.70.1.369. PMID: 11395412. (GyrA breakage/reunion; GyrB ATPase.)
4. Investigation of delafloxacin resistance in multidrug-resistant *Escherichia coli* strains and the detection of *E. coli* ST43 international high-risk clone. Microorganisms. 2023;11(6):1602. doi:10.3390/microorganisms11061602. (gyrA S83L/D87N, parC S80I/E84V; ciprofloxacin resistance 51%.)
5. Cotman AE, Durcik M, Benedetto Tiz D, Fulgheri F, Secci D, Sterle M, et al. Discovery and hit-to-lead optimization of benzothiazole scaffold-based DNA gyrase inhibitors with potent activity against *Acinetobacter baumannii* and *Pseudomonas aeruginosa*. J Med Chem. 2023;66(2):1380-1425. doi:10.1021/acs.jmedchem.2c01597. PMID: 36634346. (PDB 7P2M, 1.16 Å; no cross-resistance to novobiocin.)
6. ChEMBL database (EBI). Target CHEMBL1826 (*Escherichia coli* DNA gyrase subunit B); activity record 18804670: CHEMBL4293447, IC50 6.0 nM, assay CHEMBL4275017 (Eur J Med Chem, 2018, document CHEMBL4270612); novobiocin CHEMBL36506: Kd 28 nM (J Med Chem, 2011, document CHEMBL2176884), IC50 154 nM ATPase / 200 nM supercoiling (Antimicrob Agents Chemother, 2008, document CHEMBL1275417). Accessed 9 November 2026.
7. RCSB Protein Data Bank. PDB 7P2M (*E. coli* GyrB24–LMD43, 1.16 Å); PDB 6ENH (*Thermus thermophilus* GyrB, used only in the discarded run). Accessed 9 November 2026.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-015-2026-11-09.json` (LeadForge pipeline run, corrected, 9 November 2026): UniProtKB P0AES6, ChEMBL target CHEMBL1826 (50 bioactivities), 26 ranked leads, Vina 1.2.7 docking on PDB 7P2M (centre [−18.60, −15.05, 6.55], box 22.5 Å, exhaustiveness 8). Novobiocin docking: `hidden_files/dock-HP-015-novobiocin-2026-11-09.json` (PubChem CID 54675769, same protocol). Discarded first run: `hidden_files/dock-HP-015-WRONG-TARGET-2026-11-09.json` (UniProtKB Q5SHZ4, ChEMBL CHEMBL2074 human maltase-glucoamylase). ChEMBL IDs: CHEMBL4293447, CHEMBL4294536, CHEMBL4278317, CHEMBL4281775, novobiocin CHEMBL36506, ciprofloxacin CHEMBL100. PDB file used for the centre audit: `clinic-demo/app/discovery/data/pdb_cache/7P2M.pdb`. No additional data were generated.
