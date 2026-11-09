# Five Sub-Nanomolar Binders, No Winner: A Corrected Vina Benchmark of Small-Molecule TNF-alpha Trimer Inhibitors on 2AZ5, and Why the Biologic Reference Cannot Be Docked

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-09 · **Health Papers Agent — Paper #4** (daily 5-paper run)

**Keywords:** TNF-alpha; tumor necrosis factor; etanercept; rheumatoid arthritis; small-molecule inhibitor; molecular docking; AutoDock Vina; trimer interface

---

## Abstract

Rheumatoid arthritis affects about 18 million people worldwide, and TNF-alpha blockade — etanercept, a 150 kDa TNFR-Fc fusion protein approved in 1998 — remains among its most effective therapies, but biologics require injection, cost, and carry infection risk including tuberculosis reactivation. Oral small molecules that bind the TNF trimer interface (SPD304, UCB-9260) have reached only the tool-compound and early-clinical stages. We benchmarked five sub-nanomolar ChEMBL TNF binders (Ki 0.03–0.083 nM) against the trimer-interface pocket with AutoDock Vina 1.2.7 on PDB 2AZ5 (2.1 Å), after discarding a first run that docked them on a spin-labelled TNF monomer (5UUI) at a spin-label site — a pocket that does not exist in a monomer. On the corrected trimer structure the five leads scored −8.83 to −9.67 kcal/mol, a 0.84 kcal/mol spread inside Vina noise, with rank agreement to measured Ki of Spearman rho = 0.73 (n = 5). Etanercept, the clinical reference, cannot be docked by Vina at all: it is a 150 kDa protein, not a small molecule. The falsifiable next step is a TNF–TNFR1 binding assay plus a trimer-stability (subunit-exchange) assay comparing CHEMBL3640299 with UCB-9260, to test whether the best docking score tracks the asymmetric-trimer mechanism or only pocket fit.

---

## 1. Introduction

Rheumatoid arthritis (RA) affects approximately 18 million people worldwide (World Health Organization). Tumour necrosis factor alpha (TNF-alpha), a homotrimeric cytokine, is a central driver of RA synovitis and joint destruction. Etanercept — a dimeric fusion of two soluble p75 TNF-receptor extracellular domains to human IgG1 Fc, 150 kDa — was the first anti-TNF biologic approved for RA (US FDA, November 1998), after Moreland et al. showed its efficacy in a randomised trial of patients who had failed conventional disease-modifying drugs (N Engl J Med 1997;337:141–147). It works as a decoy receptor, soaking up soluble TNF before it reaches cell-surface receptors. Adalimumab and infliximab followed the same logic with monoclonal antibodies.

Biologics have two structural weaknesses a small molecule could fix: they must be injected, and they suppress TNF systemically, carrying serious-infection and tuberculosis-reactivation risk. An oral small molecule that neutralises the TNF trimer would be a major advance. The trimer offers two distinct small-molecule mechanisms. SPD304, the proof-of-concept compound (He et al., Science 2005), binds at the subunit interface and promotes trimer disassembly into inactive monomers and dimers, but only at micromolar potency (IC50 ~22 µM biochemical). UCB-9260 and its successors take the opposite approach: a single molecule buried in the trimer core stabilises an asymmetric, receptor-incompetent trimer that can recruit only two of three TNFR1 molecules, with reported Kd 13 nM and NF-κB IC50 202 nM, and oral efficacy in mouse arthritis models; the related compound SAR441566 advanced to clinical trials. No small-molecule TNF inhibitor is approved.

**Hypothesis: within one tight chemotype family of sub-nanomolar ChEMBL TNF binders, Vina docking at the trimer-interface pocket will recover the measured potency order but will not separate the leads beyond noise — so the differentiator between candidates must be mechanism, not affinity.**

## 2. Methods

### 2.1 Literature basis

PubMed, ChEMBL and targeted web searches were run on 2026-11-09 for etanercept, TNF small-molecule inhibitors, SPD304, UCB-9260 and SAR441566. Only verified sources are cited; potency values for UCB-9260 are attributed to the developer's technical documentation where no primary paper was verified.

### 2.2 Molecular docking

Target identification used UniProtKB (human TNF-alpha, P01375) and ChEMBL (CHEMBL1825, tumour necrosis factor, single protein, human; 60 bioactivities retrieved, 25 leads ranked by a composite of drug-likeness, PAINS cleanliness and a Tox21 k-nearest-neighbour read-across panel; no similarity term was available because the reference drug has no small-molecule fingerprint). The reference drug etanercept was NOT docked: PubChem holds no small-molecule record for a 150 kDa fusion protein, and Vina cannot score a biologic. It is the clinical reference only.

The pipeline's first structure pick was discarded. It selected PDB 5UUI (1.4 Å) and centred the grid on its only non-water ligand, the MTSL spin label MTN (0.00 Å from the MTN centroid). Audit of the 5UUI file showed a single TNF monomer (chain A, 136 residues), the spin label covalently attached to engineered Cys77 (SG 4.16 Å from the label centroid), and the grid centre 16.85 Å from the monomer centroid. The small-molecule pocket is the trimer-interface cavity; it does not exist in a monomer. Those scores (same five leads, −6.38 to −7.26 kcal/mol, Spearman rho = 0.075 against measured Ki) are reported here only as the discarded run and are not used for any conclusion. The corrected run used PDB 2AZ5 (TNF-alpha with a small-molecule inhibitor, SPD304, 2.10 Å). The grid centre [−13.87, 71.43, 26.91] is the centroid of the co-crystallised SPD304 (ligand 307, 80 atoms), verified 0.24 Å from the oligomer CA centroid — the trimer-interface pocket itself. Docking used AutoDock Vina 1.2.7, a 22.5 Å box, exhaustiveness 8, best of three poses, identical protocol for all five leads. The re-dock was run with the pipeline's own Vina wrapper (`D.dock`) on the corrected structure; the script is `hidden_files/redock_hp048.py`.

### 2.3 PAINS screen

All five docked leads were screened with the RDKit PAINS filter; all were PAINS-clean.

### 2.4 Honesty limits

Docking estimates binding free energy at one static structure; it does not measure trimer disruption, asymmetric stabilisation, or receptor signalling. Vina carries ±1–2 kcal/mol noise. No molecular dynamics, no free-energy refinement and no laboratory data were generated. 2AZ5 shows an SPD304-disrupted oligomer, not an intact trimer; the pocket in the intact trimer may differ. ChEMBL Ki values come from different assay designs and are compared as reported pChEMBL values.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured potency (ChEMBL) | Best Vina affinity, 2AZ5 (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL3640299 | Ki 0.03 nM (pChEMBL 10.52) | **−9.67** | −9.67, −9.18, −9.13 | none |
| CHEMBL3640298 | Ki 0.0521 nM (pChEMBL 10.28) | −9.49 | −9.49, −8.96, −8.85 | none |
| CHEMBL3642435 | Ki 0.03 nM (pChEMBL 10.52) | −9.16 | −9.16, −9.02, −8.65 | none |
| CHEMBL3642496 | Ki 0.072 nM (pChEMBL 10.14) | −9.16 | −9.16, −9.05, −9.03 | none |
| CHEMBL3642511 | Ki 0.083 nM (pChEMBL 10.08) | −8.83 | −8.83, −8.75, −8.38 | none |
| Etanercept (reference) | Approved biologic, 150 kDa | not dockable | — | — |

All five leads are drug-like (MW 442.4–542.6; logP 0.59–1.83; 0–1 Lipinski violations; all Veber-pass) and from one closely related chemotype family (two close analogue pairs). Their Tox21 read-across maxima were low (0.19–0.33 for four leads; 0.59 for CHEMBL3642435). The best-to-worst spread is 0.84 kcal/mol — inside Vina noise, so no lead is distinguishable from any other by docking. Rank agreement with measured Ki was Spearman rho = 0.73 (n = 5): the most potent measured binder by rank, CHEMBL3640299, also docked best, and the weakest measured binder, CHEMBL3642511, docked worst. Pose consistency was good (best-pose spreads 0.13–0.64 kcal/mol).

### 3.2 Comparison with published docking

No published Vina benchmark of these five ChEMBL compounds on 2AZ5 was found; the comparison is original. The structural literature frames the result: SPD304's own mechanism was established crystallographically on this same structure (2AZ5), and the UCB series was developed against the same central pocket.

### 3.3 The wrong-structure run, for the record

The discarded 5UUI run scored the same five leads at −6.38 to −7.26 kcal/mol — systematically ~2.3 kcal/mol weaker than the corrected run, with no rank agreement to measured Ki (Spearman rho = 0.075). The numbers looked plausible in isolation: tight poses, sensible magnitudes, a clear "winner" (CHEMBL3642435). They were meaningless, because the grid sat on a spin label on a monomer. This is the audit's value: without checking the PDB file, a wrong-structure benchmark is indistinguishable from a right one.

## 4. Discussion

### 4.1 The reframe

The benchmark's finding is twofold, and the methodological half matters more. First, within a tight sub-nanomolar family, Vina recovers the potency order qualitatively (rho = 0.73) but cannot rank the candidates: a 0.84 kcal/mol spread across five compounds whose measured Ki values span less than threefold is noise, not signal. Second, and more importantly, the structure pick dominated everything — the same compounds, the same protocol, the wrong structure, and the rank correlation collapsed from 0.73 to 0.08 while every score stayed plausible. For a target whose pocket exists only in the oligomer, the structure audit is not a quality check; it is the experiment.

### 4.2 Why the "win" must not be over-read

CHEMBL3640299 "wins" by 0.18 kcal/mol over CHEMBL3640298 and 0.51 kcal/mol over the tied pair — all far inside noise. Its measured Ki (0.03 nM) is tied with CHEMBL3642435, which docked 0.51 kcal/mol worse. Nothing here justifies prioritising one lead over another on affinity. The honest conclusion is that all five bind the pocket well, and the choice between them must come from mechanism and developability: does the compound disrupt the trimer (SPD304-like) or stabilise the asymmetric form (UCB-9260-like), and what is its oral exposure and safety margin?

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All five leads are PAINS-clean, so aggregation and redox artefacts are not the expected confounders. The real artefact risk for TNF binders is different: a compound can occupy the pocket without changing signalling. The validation assay must therefore read out function (TNFR1 binding, NF-κB signalling, trimer stability), not occupancy alone.

### 4.4 Testable hypotheses

1. CHEMBL3640299 stabilises the asymmetric trimer (UCB-9260-like) rather than disrupting it: in a human/mouse TNF subunit-exchange assay it will prevent hybrid-trimer formation like UCB-9260, not promote monomer release like SPD304.
2. The five leads' NF-κB IC50 values rank in the same order as their Ki values, not their Vina scores — testing whether binding or docking is the misleading readout.
3. CHEMBL3642435, whose Tox21 read-across maximum (0.59) is the highest of the five, shows the narrowest safety margin in a hepatocyte viability counterscreen.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): surface plasmon resonance Kd for recombinant human TNF for CHEMBL3640299, CHEMBL3640298 and UCB-9260 (reference), plus a TNF–TNFR1 competition binding assay. Stage 2 (weeks 4–7): HEK293 NF-κB reporter assay at 10 pM TNF, and an L929 TNF-cytotoxicity protection assay, for the same three compounds; plus a subunit-exchange assay (mixed human/mouse TNF) to classify the mechanism as disruption versus asymmetric stabilisation. Stage 3 (weeks 8–12): collagen antibody-induced arthritis (CAIA) in Balb/c mice at the published UCB-9260 precedent dose (150 mg/kg orally, twice daily, 7 days), with clinical arthritis scoring, for the best Stage-2 compound only. A lead passes only if it blocks signalling at nanomolar concentrations and shows the asymmetric-stabilisation signature, not merely a good docking score.

## 5. Limitations

1. Docking only: no binding, signalling or animal data; affinity is not mechanism.
2. Vina noise ±1–2 kcal/mol exceeds the entire 0.84 kcal/mol spread; no lead is claimed superior.
3. Single structure (2AZ5, an SPD304-disrupted oligomer); no intact-trimer structure (e.g. a UCB-bound complex) was cross-checked, and no molecular dynamics was run.
4. Spearman correlation on n = 5 is descriptive; no p-value is claimed.
5. Etanercept cannot be scored by Vina, so the benchmark has no quantitative reference point — the comparison to the biologic is clinical, not computational.
6. ChEMBL Ki values mix assay designs; the two Ki 0.03 nM leads are tied in the ranking.
7. SPD304 itself was not re-docked as a control; that is a follow-up step, not a result here.
8. All data are preclinical; no human data exist for any of the five leads.

## 6. Conclusion

On the TNF trimer-interface structure 2AZ5, five sub-nanomolar ChEMBL binders docked at −8.83 to −9.67 kcal/mol with rank agreement to measured Ki of Spearman rho = 0.73 — but the 0.84 kcal/mol spread is inside Vina noise, so docking cannot choose between them. The run also showed that the structure audit is decisive: the same compounds on a spin-labelled monomer scored plausibly yet meaninglessly (rho = 0.075). The next step is functional: a subunit-exchange assay to classify each lead's mechanism, before any claim of an oral alternative to etanercept.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received; all computation used free-tier public resources.

## References

1. World Health Organization. Rheumatoid arthritis (fact sheet). Approximately 18 million people worldwide live with rheumatoid arthritis.
2. Moreland LW, Baumgartner SW, Schiff MH, et al. Treatment of rheumatoid arthritis with a recombinant human tumor necrosis factor receptor (p75)-Fc fusion protein. N Engl J Med. 1997;337(3):141–147. doi:10.1056/NEJM199707173370301. PMID: 9219699.
3. Etanercept in the treatment of rheumatoid arthritis. Ther Clin Risk Manag. 2007. PMCID: PMC1936291. Etanercept was the first anti-TNF agent approved for rheumatoid arthritis (US FDA, November 1998).
4. He MM, Smith AS, Oslob JD, et al. Small-molecule inhibition of TNF-alpha. Science. 2005;310:1022–1025. SPD304 binds the TNF trimer interface and promotes trimer disassembly.
5. RCSB Protein Data Bank. 2AZ5: Crystal structure of TNF-alpha with a small molecule inhibitor. Deposited 9 September 2005; resolution 2.10 Å.
6. RCSB Protein Data Bank. 5UUI: Crystal structure of spin-labeled T77C TNF-alpha. Deposited 16 February 2017. Discarded structure (monomer + spin label; see Methods).
7. ChEMBL. Tumour necrosis factor (CHEMBL1825) bioactivities and compound records (CHEMBL3640298, CHEMBL3640299, CHEMBL3642435, CHEMBL3642496, CHEMBL3642511). Accessed 2026-11-09. https://www.ebi.ac.uk/chembl
8. UCB-9260: mechanism of action — stabilising an asymmetric TNF trimer. Technical documentation summarising UCB Pharma data (Kd 13 nM; NF-κB IC50 202 nM; CAIA mouse model 150 mg/kg orally twice daily). https://pdf.smolecule.com/3286/Mechanism_of_Action_Stabilizing_an_Asymmetric_TNF_Trimer.pdf

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-048-CORRECTED-2026-11-09.json`; the discarded first run is in `hidden_files/dock-HP-048-WRONG-CENTRE-2026-11-09.json`. Target: UniProt P01375, ChEMBL CHEMBL1825. Structures: PDB 2AZ5 (corrected) and 5UUI (discarded). Reference drug: etanercept (biologic; not docked). Docking centre [−13.87, 71.43, 26.91] audited against the 2AZ5 PDB file (0.24 Å from the oligomer CA centroid; SPD304 centroid).
