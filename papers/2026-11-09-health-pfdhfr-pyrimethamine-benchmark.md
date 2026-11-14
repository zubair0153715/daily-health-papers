# Pyrimethamine Docks Worst on Its Own Resistant Mutant — And That Is the Correct Answer: A Vina Benchmark on Quadruple-Mutant PfDHFR-TS 1J3K

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-09 · **Health Papers Agent — Paper #5** (daily 5-paper run)

**Keywords:** Plasmodium falciparum; dihydrofolate reductase; pyrimethamine; sulfadoxine-pyrimethamine; antimalarial resistance; molecular docking; AutoDock Vina; quadruple mutant

---

## Abstract

Malaria caused about 263 million cases and 597,000 deaths in 2023, and sulfadoxine–pyrimethamine — still used for intermittent preventive treatment in pregnancy and seasonal chemoprevention — is compromised by point mutations in Plasmodium falciparum dihydrofolate reductase (PfDHFR): N51I, C59R, S108N and I164L, whose quadruple combination confers high-level pyrimethamine resistance. We benchmarked pyrimethamine against four sub-nanomolar ChEMBL diaminopyrimidine analogues on the quadruple-mutant enzyme (PDB 1J3K, 2.10 Å) with AutoDock Vina 1.2.7, after discarding two pipeline runs that resolved the wrong target (human maltase-glucoamylase) or a sparsely annotated 3D7 record. On the mutant structure pyrimethamine docked worst (−7.48 kcal/mol; its duplicate record CHEMBL36 −7.45), behind CHEMBL21885 (−8.38), CHEMBL21778 (−7.52) and CHEMBL282275 (−7.49). Against wild-type Ki values the rank correlation is a perfect inversion (Spearman rho = −1.0, n = 4) — but the Ki values are wild-type, while the structure is mutant. Against matched S108N-mutant Ki values (pyrimethamine 71.7 nM; analogues 10.6–66.2 nM) the correlation is weakly positive (rho = 0.40) and pyrimethamine is worst in both. The falsifiable next step is a head-to-head enzyme assay of all four compounds on wild-type and quadruple-mutant PfDHFR-TS under identical conditions, to test whether the docking order tracks the mutant enzyme.

---

## 1. Introduction

Malaria caused an estimated 263 million cases and 597,000 deaths in 2023 (WHO World Malaria Report 2024), almost all from Plasmodium falciparum. Sulfadoxine–pyrimethamine (SP) remains in use for intermittent preventive treatment in pregnancy, perennial chemoprevention in infants, and seasonal chemoprevention in children — not because it still works everywhere, but because it is cheap, single-dose and safe in pregnancy. Its efficacy is eroding through point mutations in the two folate-pathway enzymes it targets: dihydrofolate reductase (PfDHFR, hit by pyrimethamine) and dihydropteroate synthase (PfDHPS, hit by sulfadoxine).

For PfDHFR the resistance ladder is well mapped. S108N alone gives low-level tolerance; N51I/S108N and C59R/S108N double mutants give moderate resistance; the N51I/C59R/S108N triple mutant gives high-level resistance; adding I164L — the quadruple mutant — makes the parasite effectively resistant to pyrimethamine. In the MalariaGEN Pf7 dataset (8,492 African samples) the triple mutant was the most frequent dhfr haplotype (80%), while I164L remained rare (seen twice). The quintuple mutant (dhfr triple plus dhps A437G/K540E) is associated with SP treatment failure in children and a shorter prophylactic period in pregnancy.

The structural basis was solved in 2003: Yuvaniyama et al. crystallised wild-type PfDHFR-TS with WR99210 (1J3I), the double mutant (C59R+S108N) with pyrimethamine (1J3J), and the quadruple mutant with WR99210 (1J3K) (Nat Struct Biol 2003;10:357–365). Their key finding was mechanistic: pyrimethamine is rigid, and the S108N mutation places an asparagine side chain where the drug needs to sit; WR99210's flexible side chain adopts a conformation that fits the widened mutant active site. That mechanism makes a sharp, testable prediction for docking: on the quadruple-mutant structure, pyrimethamine should score worst, and flexible analogues should score better — the opposite of the wild-type potency order. **Hypothesis: Vina docking on quadruple-mutant PfDHFR-TS (1J3K) will rank pyrimethamine last, inverting the wild-type Ki order, because the docking structure and the potency assay measure different enzyme forms.**

## 2. Methods

### 2.1 Literature basis

PubMed, ChEMBL, RCSB PDB and targeted searches were run on 2026-11-09 for PfDHFR resistance mutations, SP haplotype prevalence, and the 1J3I/1J3J/1J3K structures. Only verified sources are cited. Mutant Ki values were verified against live ChEMBL activity records on 2026-11-09 (see Results).

### 2.2 Molecular docking

Target identification used UniProtKB and ChEMBL. Two pipeline runs were discarded before the valid run. Run 1 resolved the target string to UniProt D0QXK4 but then to ChEMBL CHEMBL2074 — human maltase-glucoamylase — and returned 55 irrelevant ligands with no PDB found; the fallback that picks the first candidate from a generic text-search list was the fault, the same fault class as the HP-015 wrong-target run. Run 2 used accession Q8I1R6 (3D7 DHFR-TS) and the correct ChEMBL target CHEMBL4296323, but that record holds only 2 bioactivities, and Q8I1R6 carries no PDB cross-references in UniProt, so again no structure was found. The valid run used accession P13922 (K1-strain DHFR-TS, 608 amino acids), which maps to ChEMBL CHEMBL1939 (44 bioactivities retrieved, 26 leads ranked by a composite of similarity to pyrimethamine, Lipinski/Veber drug-likeness, PAINS cleanliness and a Tox21 read-across panel) and to PDB entries 1J3I, 1J3J and 1J3K. The pipeline selected 1J3K (quadruple mutant N51I+C59R+S108N+I164L with WR99210, NADPH and dUMP, 2.10 Å). The reference drug pyrimethamine was verified against PubChem (CID 4993; C12H13ClN4; MW 248.72; logP 2.52). Docking used AutoDock Vina 1.2.7, a 22.5 Å box, exhaustiveness 8, best of three poses. The grid centre was audited from the PDB file itself: centre [28.86, 6.13, 60.19] lies 0.01 Å from the centroid of the chain-A WR99210 molecule (WRA A609) — the DHFR active site — with the mutated residue Asn108 (OD1) 5.51 Å away and the NADPH cofactor centroid 12.08 Å away. (The file holds two WR99210 molecules, one per DHFR chain; averaging them would place the centre 32 Å from either pocket, so the audit used the chain-A molecule, as the pipeline's multimer-aware picker does.)

### 2.3 PAINS screen

All five docked compounds were screened with the RDKit PAINS filter; all were PAINS-clean.

### 2.4 Honesty limits

Docking estimates binding free energy at one static structure; it does not measure enzyme inhibition. Vina carries ±1–2 kcal/mol noise, so differences below ~2 kcal/mol are not claims of superiority. No molecular dynamics, no free-energy refinement and no laboratory data were generated. The pipeline's recorded Ki values are wild-type enzyme values; mutant Ki values were fetched separately from ChEMBL and are reported alongside. Pyrimethamine's wild-type Ki varies across assays (0.19–1.5 nM in the records retrieved), so fold-change figures depend on the assay pair chosen.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured Ki, wild-type PfDHFR | Measured Ki, S108N mutant | Best Vina affinity, 1J3K (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|---|
| CHEMBL21885 | 0.6 nM (pChEMBL 9.22) | 66.2 nM | **−8.38** | −8.38, −7.46, −7.02 | none |
| CHEMBL21778 | 0.4 nM (pChEMBL 9.40) | 10.6 nM | −7.52 | −7.52, −7.02, −6.93 | none |
| CHEMBL282275 | 0.3 nM (pChEMBL 9.52) | 31.5 nM | −7.49 | −7.49, −6.81, −6.54 | none |
| Pyrimethamine (QUERY) | 0.19 nM (pChEMBL 9.72) | 71.7 nM | −7.48 | −7.48, −6.90, −6.87 | none |
| CHEMBL36 (= pyrimethamine) | 0.19 nM (pChEMBL 9.72) | 71.7 nM | −7.45 | −7.45, −6.89, −6.86 | none |

All five are diaminopyrimidine analogues of one scaffold family (identical TPSA 77.82; HBD 2; HBA 4; 2 rotatable bonds; MW 228.3–293.2; logP 2.18–3.17; 0 Lipinski violations). Pyrimethamine appears twice — as the QUERY (PubChem CID 4993) and as CHEMBL36 — and the two independent dockings agree to 0.03 kcal/mol (−7.48 vs −7.45), a preparation-noise control. The best-to-worst spread is 0.93 kcal/mol, inside Vina noise. Pyrimethamine's measured Tox21 panel is notable: unlike the analogues (k-nearest-neighbour read-across maxima 0.23–0.33), pyrimethamine itself is in the Tox21 database with measured activity at NR-AR 1.0, NR-AR-LBD 1.0 and SR-ARE 1.0 — an in-vitro androgen-receptor and oxidative-stress signal that is a property of the drug, not a prediction.

Against wild-type Ki the rank correlation with docking is a perfect inversion (Spearman rho = −1.0, n = 4): the most potent measured binder (pyrimethamine, Ki 0.19 nM) docked worst, and the least potent (CHEMBL21885, Ki 0.6 nM) docked best. Against the matched S108N-mutant Ki values the correlation reverses sign (rho = +0.40, n = 4), and pyrimethamine is worst in both the docking and the mutant assay. The S108N fold-losses versus wild-type Ki are 26-fold (CHEMBL21778), 48-fold (pyrimethamine, using the 1.5 nM wild-type record from the same assay series as the mutant record), 105-fold (CHEMBL282275) and 110-fold (CHEMBL21885).

### 3.2 Comparison with published docking

No published Vina benchmark of these four ChEMBL analogues on 1J3K was found; the comparison is original. The structural literature predicts exactly the qualitative pattern observed: the rigid pyrimethamine clashes with Asn108 in the mutant pocket, while flexible side chains (WR99210 in the crystal structure) fit. WR99210 itself was not among the docked leads and was not re-docked as a control — that is a follow-up step.

### 3.3 The standardisation / quality problem

The wild-type Ki values span only 3-fold (0.19–0.6 nM), so the "perfect inversion" is a rank statement about a near-equipotent set, not a large potency difference — and it is computed against the wrong enzyme form. The honest comparison is the matched one (mutant Ki vs mutant structure), where the correlation is weak-positive and pyrimethamine is correctly last. The second quality problem is assay variability: pyrimethamine's own wild-type Ki is 0.19 nM in one ChEMBL record and 1.5 nM in another — an 8-fold spread that exceeds the entire potency range of the four leads. Any ranking built on single Ki records is fragile.

## 4. Discussion

### 4.1 The reframe

The naive reading of this benchmark — "Vina perfectly anti-correlates with potency" — is wrong, and the reason it is wrong is the paper's real finding. Docking scores and Ki values are only comparable when they describe the same enzyme. The pipeline's Ki values are wild-type; the structure is the quadruple mutant. Once the comparison is matched (S108N Ki against the mutant structure), the inversion vanishes, the correlation turns weakly positive, and the mechanistically expected result appears: pyrimethamine, the rigid drug the mutations evolved to exclude, scores worst. The benchmark therefore validates the structural account of resistance rather than refuting docking — but it also shows how easily a benchmark can manufacture a striking, false conclusion by mixing enzyme forms.

### 4.2 Why the "win" must not be over-read

CHEMBL21885 "wins" by 0.86–0.90 kcal/mol over the other three leads — inside Vina noise, and its best pose (−8.38) is 0.92 kcal/mol clear of its own second pose (−7.46), so even its top score is a single-pose event. Against the S108N enzyme it is the second-worst of the four (Ki 66.2 nM, 110-fold loss). Nothing here makes it a lead; it is a candidate for the matched assay, nothing more. The matched correlation (rho = 0.40, n = 4) is descriptive, not inferential.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five compounds are PAINS-clean. The relevant artefact control for DHFR assays is different: NADPH depletion and the bifunctional enzyme's TS domain. The proposed validation therefore reads out DHFR activity directly (NADPH oxidation) on both enzyme forms, with WR99210 as the flexible positive control and a no-enzyme blank.

### 4.4 Testable hypotheses

1. In a head-to-head assay on wild-type and quadruple-mutant PfDHFR-TS under identical conditions, the four compounds rank by mutant Ki in the same order as their 1J3K docking scores (CHEMBL21885 best, pyrimethamine worst) — testing whether the matched correlation (rho = 0.40) holds with clean data.
2. WR99210 re-docked on 1J3K scores better than all four leads, reproducing its crystallographic fit and validating the grid.
3. A flexible analogue of CHEMBL21885 designed to keep the WR99210-like side-chain freedom retains mutant Ki within 10-fold of wild-type — testing the flexibility hypothesis directly.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): recombinant wild-type and quadruple-mutant (N51I/C59R/S108N/I164L) PfDHFR-TS enzyme assays (NADPH oxidation) for pyrimethamine, WR99210 and the four ChEMBL analogues under identical conditions; readouts Ki for both enzyme forms and the mutant/wild-type ratio. Stage 2 (weeks 4–7): P. falciparum 3D7 (wild-type) and V1/S (quadruple-mutant) blood-stage growth inhibition (SYBR Green assay), with chloroquine as control. Stage 3 (weeks 8–12): human DHFR counterscreen for the best compound, to test selectivity — the property that decides whether a PfDHFR inhibitor is a drug or a poison. A lead passes only if its mutant/wild-type Ki ratio is under 10-fold and its human-DHFR selectivity exceeds 100-fold.

## 5. Limitations

1. Docking only: no enzyme, parasite or animal data; affinity is not inhibition.
2. Vina noise ±1–2 kcal/mol exceeds the entire 0.93 kcal/mol spread; no lead is claimed superior.
3. Single structure (1J3K, quadruple mutant); no wild-type structure (1J3I) comparison was run, and no molecular dynamics.
4. Spearman correlations on n = 4 are descriptive; no p-value is claimed.
5. Ki values come from different assay designs and, for pyrimethamine, disagree 8-fold between wild-type records.
6. The S108N Ki values are single-mutant, not quadruple-mutant, measurements — the matched comparison is approximate.
7. WR99210 was not re-docked as a control.
8. All data are preclinical; SP remains the deployed drug and no clinical recommendation follows.

## 6. Conclusion

On quadruple-mutant PfDHFR-TS (1J3K), pyrimethamine docked worst (−7.48 kcal/mol) while four sub-nanomolar analogues led, the best by 0.90 kcal/mol, inside Vina noise. The wild-type comparison looks like a perfect inversion (Spearman rho = −1.0) but mixes enzyme forms; against matched S108N-mutant Ki values the correlation is weakly positive (rho = 0.40) and pyrimethamine is worst in both. The result supports the structural account of pyrimethamine resistance — a rigid drug excluded by Asn108 — and sets the validation bar: matched wild-type and quadruple-mutant enzyme assays under identical conditions before any claim of a resistance-beating analogue.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all computation used free-tier public resources.

## References

1. World Health Organization. World Malaria Report 2024. 263 million cases and 597,000 deaths in 2023.
2. Yuvaniyama J, Chitnumsub P, Kamchonwongpaisan S, Vanichtanankul J, Sirawaraporn W, Taylor P, Walkinshaw MD, Yuthavong Y. Insights into antifolate resistance from malarial DHFR-TS structures. Nat Struct Biol. 2003;10:357–365. doi:10.1038/nsb921. PMID: 12704428.
3. Disparate co-evolution and prevalence of sulfadoxine and pyrimethamine resistance alleles and haplotypes at dhfr and dhps genes across Africa. Sci Rep. 2025. doi:10.1038/s41598-025-98035-7. Triple-mutant dhfr haplotype 80% of Pf7 African samples; I164L rare.
4. Prevalence of pfdhfr-pfdhps sextuple and gametocyte-associated quintuple sulfadoxine-pyrimethamine resistance mutations in Plasmodium falciparum isolates from pregnant women in Mozambique. Pathogens. 2026;15(5):504. Quintuple mutant 54% of isolates; sextuple 7%.
5. McCollum AM, Basco LK, Tahar R, et al. Hitchhiking and selective sweeps of Plasmodium falciparum sulfadoxine and pyrimethamine resistance alleles in a population from Central Africa. Antimicrob Agents Chemother. 2008;52(11):4089–4097. doi:10.1128/AAC.00623-08.
6. RCSB Protein Data Bank. 1J3K: Quadruple mutant (N51I+C59R+S108N+I164L) Plasmodium falciparum dihydrofolate reductase-thymidylate synthase complexed with WR99210, NADPH, and dUMP. Deposited 3 February 2003; resolution 2.10 Å.
7. RCSB Protein Data Bank. 1J3J: Double mutant (C59R+S108N) Plasmodium falciparum dihydrofolate reductase-thymidylate synthase complexed with pyrimethamine, NADPH, and dUMP. Deposited 3 February 2003; resolution 2.30 Å.
8. ChEMBL. Bifunctional dihydrofolate reductase-thymidylate synthase, Plasmodium falciparum K1 (CHEMBL1939) bioactivities and compound records (CHEMBL36, CHEMBL21778, CHEMBL282275, CHEMBL21885). Accessed 2026-11-09. https://www.ebi.ac.uk/chembl
9. PubChem. Pyrimethamine, CID 4993. https://pubchem.ncbi.nlm.nih.gov/compound/4993

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-023-2026-11-09.json`. Discarded runs: `hidden_files/dock-HP-023-WRONG-TARGET-2026-11-09.json` (human maltase-glucoamylase) and `hidden_files/dock-HP-023-3D7-THIN-2026-11-09.json` (3D7 record, 2 bioactivities, no PDB). Target: UniProt P13922, ChEMBL CHEMBL1939. Structure: PDB 1J3K. Reference drug: pyrimethamine, PubChem CID 4993. Docking centre [28.86, 6.13, 60.19] audited against the 1J3K PDB file (0.01 Å from the chain-A WR99210 centroid).
