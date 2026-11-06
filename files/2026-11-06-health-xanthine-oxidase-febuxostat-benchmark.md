# Febuxostat Beats Itself by 0.03 kcal/mol: A Vina Benchmark of Xanthine Oxidase Inhibitors on 2E1Q, and the Selenium Ligands the Pipeline Cannot Dock

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-06 · **Health Papers Agent — Paper #3** (daily 5-paper run)

**Keywords:** xanthine oxidase; febuxostat; molecular docking; AutoDock Vina; gout; hyperuricaemia; ChEMBL; selenium

---

## Abstract

Gout is driven by hyperuricaemia, and xanthine oxidase catalyses the final steps of uric-acid formation while also generating reactive oxygen species, making it the established target for urate-lowering therapy. Febuxostat, a non-purine xanthine oxidase inhibitor, is effective but carries a contested cardiovascular safety record: the FDA-mandated CARES trial found higher all-cause and cardiovascular mortality with febuxostat than with allopurinol despite no difference in the primary composite endpoint, leading to a boxed warning, while the later FAST trial found no excess mortality, and a 2025 Japanese nationwide claims cohort of patients with chronic kidney disease found no significant difference in composite cardiovascular outcomes (hazard ratio 0.93). We asked whether a standardised automated docking pipeline could find a xanthine oxidase inhibitor that binds more tightly than febuxostat. The LeadForge pipeline was run live on 6 November 2026 on human xanthine dehydrogenase/oxidase (UniProt P47989, ChEMBL CHEMBL1929, 53 bioactivities); 25 compounds passed the similarity screen and 26 were ranked. Five leads were docked with AutoDock Vina 1.2.7 on PDB 2E1Q (2.6 Å), the grid centred exactly on the co-crystallised ligand — febuxostat itself — at [35.35, 15.17, 152.43]. No lead beats febuxostat: the best-scoring "lead", CHEMBL1164729 at −7.53 kcal/mol, is febuxostat itself entered under a second ChEMBL ID, scoring 0.03 kcal/mol from the query entry (−7.50). The best genuine lead, CHEMBL5436777 (IC50 1.0 nM), scored −7.42 kcal/mol, 0.08 kcal/mol from febuxostat — a tie inside Vina's ±1–2 kcal/mol noise. Two of the five leads, both selenium-containing analogues, could not be docked at all because the pipeline cannot prepare selenium ligands. Febuxostat's own Tox21 read-across panel returns probability 1.0 on three assays, an identity artifact, not a toxicity signal. The falsifiable next step is a head-to-head xanthine oxidase enzyme inhibition assay of CHEMBL5436777 against febuxostat under identical conditions, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable potency advantage; a measured potency advantage greater than 2-fold for CHEMBL5436777, or a successful docking of the selenium analogues after the ligand-preparation fault is fixed, would refute the claim that no lead in this set improves on febuxostat.

---

## 1. Introduction

Gout is driven by hyperuricaemia: when serum urate exceeds its solubility limit, monosodium urate crystals deposit in joints and soft tissues and trigger recurrent inflammatory arthritis. Xanthine oxidase catalyses the final two steps of purine catabolism — hypoxanthine to xanthine, and xanthine to uric acid — and in the process generates reactive oxygen species, so inhibiting the enzyme lowers urate and, in principle, reduces oxidative stress. Allopurinol, a purine analogue, was the standard xanthine oxidase inhibitor for decades; febuxostat, a non-purine inhibitor, was developed as a more selective alternative and is effective at lowering serum urate. The clinical question around febuxostat is not potency but cardiovascular safety, and the evidence is contradictory. The FDA-mandated CARES trial (6,190 patients with gout and cardiovascular disease, 2018) found no difference in the primary composite cardiovascular endpoint between febuxostat and allopurinol, but higher all-cause mortality (7.8% vs 6.4%) and higher cardiovascular mortality (4.3% vs 3.2%) with febuxostat, and the FDA added a boxed warning. The FAST trial (6,128 patients, 2020) found febuxostat non-inferior to allopurinol on the primary cardiovascular endpoint and reported no increase in overall or cardiovascular mortality. Most recently, Inoue et al. (Nephrology, 2025) reported a Japanese nationwide claims cohort of patients with chronic kidney disease (eGFR <60 mL/min/1.73 m²) in which febuxostat versus allopurinol gave a composite cardiovascular outcome hazard ratio of 0.93 (95% CI 0.79–1.08, p = 0.33) — no statistically significant difference, including across eGFR strata. Both CARES and FAST excluded patients with eGFR <30, so the most severe kidney disease remains untested in randomised trials. Against this background, a better xanthine oxidase inhibitor would be one that binds the enzyme more tightly than febuxostat — or, failing that, one with a safety profile that does not carry the CARES shadow.

The question this paper asks is narrower and methodological: can a standardised, automated docking pipeline rank known xanthine oxidase inhibitors against febuxostat on the enzyme's inhibitor pocket, and how large is the pipeline's own error? The falsifiable hypothesis is that five known potent xanthine oxidase inhibitors, docked under an identical protocol, will score within Vina's noise of febuxostat — and that any apparent "win" smaller than 2 kcal/mol is not a discovery.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 6 November 2026: the daily literature digest (2026-11-06), PubMed E-utilities and web search (verified references below), ChEMBL (EBI) and RCSB PDB. Key sources: the CARES trial (White et al., N Engl J Med 2018) and the FAST trial (Mackenzie et al., Lancet 2020) for the cardiovascular safety evidence, Inoue et al. (Nephrology 2025) for the chronic kidney disease cohort, and the RCSB entry for PDB 2E1Q.

### 2.2 Compound selection (LeadForge pipeline)

The LeadForge pipeline was run live on 6 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target resolution: human xanthine dehydrogenase/oxidase, UniProt P47989 (gene XDH, 1,333 amino acids), ChEMBL CHEMBL1929 (single-protein, human), 53 bioactivities retrieved. Febuxostat was verified in PubChem (MW 316.38; 2-(3-cyano-4-isobutoxyphenyl)-4-methylthiazole-5-carboxylic acid). Twenty-five compounds passed the Morgan-fingerprint similarity screen and 26 were ranked by composite score (similarity ×40 + Lipinski ×20 + Veber ×10 + PAINS ×10 + tox ×20). The top five ranked leads were taken forward to docking. All five are known xanthine oxidase inhibitors with published ChEMBL potencies: febuxostat itself (Ki 0.1 nM, as CHEMBL1164729), CHEMBL5436777 (IC50 1.0 nM), CHEMBL3331615 (IC50 2.05 nM) and CHEMBL3331613 (IC50 2.29 nM). None of the non-febuxostat leads has a preferred name, an approval, or a development phase in ChEMBL.

### 2.3 Molecular docking

Docking was performed 6 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure was human xanthine oxidoreductase, PDB 2E1Q (2.6 Å, E803V mutant), with the grid centred on the centroid of its co-crystallised ligand DYI — which is febuxostat itself — at [35.35, 15.17, 152.43]. The centre was verified directly against the PDB file: the distance from the computed centroid to the DYI centroid is 0.01 Å, and the FAD cofactor sits 38 Å away, so the box covers the inhibitor pocket and not the cofactor site. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all four leads and febuxostat were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probability was NR-AhR 0.254 for CHEMBL5436777. Febuxostat's own panel is different in kind: it returns probability 1.0 on three assays (SR-ATAD5, NR-AhR and NR-AR). That is a nearest-neighbour identity artifact — the query matches a training compound exactly — not a measured toxicity signal, and the same 1.0 flags appear on the identical CHEMBL1164729 entry, which proves the flags are an artifact of identity, not of chemistry. The two selenium analogues returned low read-across probabilities (NR-AhR 0.283 and 0.261) with no flags.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement or binding-free-energy calculation was performed; a single crystal structure (2E1Q, one xanthine oxidoreductase conformation, E803V mutant) was used; two of the five leads could not be docked at all; and the four leads are already-known xanthine oxidase inhibitors, so no novelty of chemistry is claimed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Xanthine oxidase potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL1164729 (= febuxostat) | Ki 0.1 nM | **−7.53** | −7.53, −7.17, −6.67 | clean |
| Febuxostat (reference, query) | Ki 0.1 nM (same molecule) | −7.50 | −7.50, −7.22, −6.67 | clean |
| CHEMBL5436777 | IC50 1.0 nM | −7.42 | −7.42, −6.55, −6.16 | clean |
| CHEMBL3331615 | IC50 2.05 nM | DOCKING FAILED | — | clean |
| CHEMBL3331613 | IC50 2.29 nM | DOCKING FAILED | — | clean |

All docking on PDB 2E1Q (human xanthine oxidoreductase, 2.6 Å), grid centre [35.35, 15.17, 152.43] (DYI/febuxostat centroid), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 6 November 2026. CHEMBL1164729/febuxostat: MW 316.38, logP 3.72, 0 Lipinski violations. CHEMBL5436777: MW 359.41, logP 2.83, 0 violations. CHEMBL3331615: MW 363.28, logP 2.72, 0 violations. CHEMBL3331613: MW 335.22, logP 2.08, 0 violations.

The headline is stated plainly: no lead beats febuxostat. The best-scoring "lead", CHEMBL1164729 at −7.53 kcal/mol, is febuxostat itself — the identical SMILES and molecular weight, Tanimoto similarity 1.0, and an identical toxicity panel to the query. The duplicate-entry fault has struck again: the same molecule scored −7.53 as a ChEMBL hit and −7.50 as the query, 0.03 kcal/mol apart — a much smaller self-difference than the 1.75 kcal/mol seen for trametinib on MEK1, because here both entries entered Vina from the same starting conformer. The best genuine lead, CHEMBL5436777 (IC50 1.0 nM), scored −7.42 kcal/mol, 0.08 kcal/mol from febuxostat — a tie inside Vina's noise. The total spread across the three docked molecules is 0.11 kcal/mol, far below the noise floor, and the ranking is in the wrong potency order: the most potent compound by recorded Ki (febuxostat, 0.1 nM) and the least potent docked compound (CHEMBL5436777, IC50 1.0 nM) are separated by 0.08 kcal/mol, a ten-fold potency difference that Vina cannot see.

Two of the five leads could not be docked at all, and the reason is a pipeline fault, reported here rather than hidden. CHEMBL3331615 and CHEMBL3331613 are selenium analogues of febuxostat — the thiazole sulfur replaced by selenium (C16H16N2O3Se and C14H12N2O3Se). Ligand preparation failed for both: RDKit's UFFTYPER reports "unrecognized atom type Se2+2" (atom 17 in CHEMBL3331615, atom 15 in CHEMBL3331613), so no 3D conformer could be built and Vina never ran. These are the second- and third-most potent leads by recorded IC50 (2.05 and 2.29 nM), so the pipeline's blind spot falls exactly on the compounds it was supposed to test. Their PAINS-clean status and drug-like descriptors (MW 363.28 and 335.22, logP 2.72 and 2.08, 0 Lipinski violations) are reported from the ChEMBL/RDKit descriptors, not from docking.

### 3.2 Comparison with published docking

No published Vina score for febuxostat or any of these leads on 2E1Q was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for febuxostat and CHEMBL5436777 on 2E1Q are now on record for others to reproduce, together with the duplicate-entry control that quantifies the pipeline's own error on this target (0.03 kcal/mol) and the documented selenium failure. The ordering is not comparable to published potency: the three docked molecules span a ten-fold potency range (Ki 0.1 nM to IC50 1.0 nM) while their docking scores span 0.11 kcal/mol — Vina ranks poses, not Ki values, and here it cannot rank a molecule against its own duplicate by more than 0.03 kcal/mol.

### 3.3 The standardisation / quality problem

Three automated steps that could silently corrupt this result did corrupt it, in three different ways. The lead list contains the reference drug itself under a second ChEMBL ID, which the pipeline treats as a new compound — fixed only by canonicalising SMILES before ranking. The ligand-preparation step cannot type selenium, so two of five leads silently drop out of docking — fixed only by adding a selenium-capable force-field typing path or an explicit fallback. And the toxicity read-across panel returns probability 1.0 on three assays for the reference drug itself, because the query matches a training compound exactly — a panel that flags its own reference drug as maximally toxic on three assays cannot be read as evidence about any lead. The grid-centre step, by contrast, worked correctly this time: the centre landed 0.01 Å from the co-crystallised ligand, because the DYI ligand is the first drug-like HETATM group in 2E1Q and the FAD cofactor is 38 Å away. The lesson is that each automated step must be verified against the structure and the reference drug, not trusted because it worked on the last target.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a measurement of the pipeline's own error and blind spots. There is no lead here: the best "lead" is febuxostat, the best genuine lead is 0.08 kcal/mol from febuxostat, and two of the five leads were never tested at all. The durable findings are the benchmark values for febuxostat on 2E1Q (−7.50 and −7.53 kcal/mol for the two entries, with full pose lists), the 0.03 kcal/mol duplicate-entry control, and the selenium ligand-preparation fault. The clinical context sharpens the point: the unmet need in this field is not a marginally tighter binder but a xanthine oxidase inhibitor without febuxostat's contested cardiovascular record, and docking alone cannot speak to that need — a compound that scored 2 kcal/mol better would still need the CARES/FAST question answered in a trial.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the winner is the reference drug. Second, the 0.08 kcal/mol margin of the best genuine lead is smaller than the pipeline's own duplicate-entry error and far inside Vina's ±1–2 kcal/mol noise. Third, potency and docking score disagree within the lead set: a ten-fold potency spread (Ki 0.1 nM to IC50 1.0 nM) collapses to a 0.11 kcal/mol docking spread, in no consistent direction.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

No PAINS alerts is good, but PAINS-clean is a low bar, and the selenium analogues carry a different artifact risk: selenium is redox-active, so any future enzyme assay of CHEMBL3331615 or CHEMBL3331613 must include redox controls (e.g. catalase/superoxide dismutase counterscreens and a detergent control) to distinguish genuine xanthine oxidase inhibition from redox cycling. The Tox21 read-across panel is unusable as a discriminator here — it returns 1.0 on three assays for febuxostat itself — so safety claims for any lead must come from measured data, not from this panel.

### 4.4 Testable hypotheses

1. CHEMBL5436777 inhibits recombinant human xanthine oxidase with an IC50 within 2-fold of its ChEMBL value (1.0 nM) under identical assay conditions, and inhibits it no more potently than febuxostat — the docking predicts no measurable advantage; a >2-fold advantage for CHEMBL5436777 would refute the noise interpretation.
2. After the ligand-preparation fault is fixed, CHEMBL3331615 and CHEMBL3331613 dock on 2E1Q within 1 kcal/mol of febuxostat — a pipeline fix to be verified, not assumed.
3. Canonicalising the SMILES of all 26 ranked leads and re-running the pipeline removes the febuxostat duplicate and changes no other lead's rank — a pipeline fix to be verified, not assumed.
4. A Vina re-dock of the co-crystallised ligand DYI (febuxostat) into 2E1Q reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant human xanthine oxidase enzyme inhibition assay (uric-acid formation, spectrophotometric) for CHEMBL5436777 and febuxostat, same plate, n = 3, with a pre-registered 2-fold decision rule and a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable potency advantage. Stage 2 (weeks 3–6): fix the selenium ligand-preparation fault (selenium-capable typing or manual conformer generation), dock CHEMBL3331615 and CHEMBL3331613 on 2E1Q under the identical protocol, and assay whichever selenium analogue docks within 1 kcal/mol of febuxostat, with redox controls (catalase/superoxide dismutase counterscreens, detergent control) to expose redox-cycling artifacts. Stage 3 (weeks 7–12): urate-lowering comparison in a hyperuricaemic cell or animal model only for a compound that clears Stage 1 or Stage 2 with a measured >2-fold potency advantage; no compound advances to an animal model on a docking score alone. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. The 0.08 kcal/mol margin of the best genuine lead is far inside Vina's ±1–2 kcal/mol noise and smaller than the pipeline's own duplicate-entry error. 3. Two of the five leads (both selenium analogues, IC50 2.05 and 2.29 nM) could not be docked because the pipeline cannot prepare selenium-containing ligands. 4. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of DYI was performed. 5. A single crystal structure (2E1Q, one xanthine oxidoreductase conformation, E803V mutant) was used; the enzyme's molybdenum centre and induced-fit effects are not modelled. 6. The Tox21 read-across panel is unusable as a discriminator here because it returns probability 1.0 on three assays for febuxostat itself (identity artifact). 7. All leads are already-known xanthine oxidase inhibitors; no new chemical matter is proposed. 8. The pipeline's lead deduplication and ligand preparation both failed silently and required manual reporting — other silent defaults in the same pipeline are not yet audited. 9. The cardiovascular safety evidence (CARES, FAST, Inoue et al.) is summarised from the published trials; no new safety analysis was performed, and the eGFR <30 population remains untested in randomised trials.

## 6. Conclusion

No xanthine oxidase inhibitor in this set beats febuxostat: the best-scoring "lead" is febuxostat itself, the best genuine lead is 0.08 kcal/mol away — a tie inside Vina's noise — and two of the five leads could not be docked at all because the pipeline cannot prepare selenium ligands. The durable findings are the benchmark values for febuxostat on 2E1Q, the 0.03 kcal/mol duplicate-entry control, and the selenium fault. The next experiment is a head-to-head xanthine oxidase IC50 assay of CHEMBL5436777 against febuxostat, not more docking — and the next pipeline change is SMILES canonicalisation before ranking and a selenium-capable ligand-preparation path.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. White WB, Saag KG, Becker MA, et al. Cardiovascular safety of febuxostat or allopurinol in patients with gout. *N Engl J Med.* 2018;378(13):1200–1210. doi:10.1056/NEJMoa1710895.
2. Mackenzie IS, Ford I, Nuki G, et al. Long-term cardiovascular safety of febuxostat compared with allopurinol in patients with gout (FAST): a multicentre, prospective, randomised, open-label, non-inferiority trial. *Lancet.* 2020;396(10264):1745–1757. doi:10.1016/S0140-6736(20)32234-0.
3. Inoue, et al. Febuxostat versus allopurinol and cardiovascular outcomes in patients with chronic kidney disease: a Japanese nationwide claims cohort study. *Nephrology.* 2025. doi:10.1111/nep.70149.
4. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
5. RCSB Protein Data Bank. Crystal structure of human xanthine oxidoreductase E803V mutant in complex with febuxostat. PDB ID 2E1Q, 2.6 Å. https://www.rcsb.org/structure/2E1Q (accessed 6 November 2026).
6. ChEMBL database, European Bioinformatics Institute. Target: xanthine dehydrogenase/oxidase (CHEMBL1929); bioactivities accessed 6 November 2026. https://www.ebi.ac.uk/chembl/.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-009-2026-11-06.json` (pipeline run: UniProt P47989, ChEMBL CHEMBL1929, 53 bioactivities, 25 compounds passed the similarity screen, 26 ranked leads; docking on PDB 2E1Q, grid centre [35.35, 15.17, 152.43], Vina 1.2.7). ChEMBL IDs: febuxostat (CHEMBL1164729, query), CHEMBL5436777, CHEMBL3331615, CHEMBL3331613. PDB ID 2E1Q. No additional data were generated.
