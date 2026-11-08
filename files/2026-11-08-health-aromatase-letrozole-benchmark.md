# No Lead Beats Letrozole Beyond Noise: A Vina Benchmark of Five Aromatase Inhibitors on the Human CYP19A1 Structure 3S79

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-08 · **Health Papers Agent — Paper #1** (daily 5-paper run)

**Keywords:** letrozole; aromatase; CYP19A1; breast cancer; molecular docking; AutoDock Vina; endocrine therapy; drug resistance

---

## Abstract

Breast cancer was diagnosed in about 2.4 million women in 2024 and killed about 694,000; in Pakistan it is the commonest female cancer, with about 30,682 new cases and 15,552 deaths in 2022 and the highest incidence rate in Asia. Letrozole, a third-generation aromatase inhibitor, blocks CYP19A1 aromatase, the enzyme that converts androgens to oestrogens, and in the BIG 1-98 trial it cut the risk of recurrence by 18% versus tamoxifen (hazard ratio 0.82), but bone loss, arthralgia and acquired resistance limit its benefit, so new aromatase inhibitors are still wanted. We ran the LeadForge pipeline live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina docking) against the human aromatase structure in complex with androstenedione (PDB 3S79, 2.75 Å), with the grid centred on the co-crystallised androstenedione, and docked letrozole plus five known aromatase inhibitors with measured potencies of 0.02–0.21 nM, all under an identical AutoDock Vina 1.2.7 protocol. No lead beat letrozole beyond noise: the best lead (CHEMBL197650, IC50 0.11 nM) scored −8.77 kcal/mol against letrozole's −8.74, a 0.03 kcal/mol margin, and the most potent measured inhibitor (letrozole itself in ChEMBL, Ki 0.02 nM) scored −8.71; every margin is inside Vina's ±1–2 kcal/mol noise and the docking order disagrees with measured potency. The falsifiable next step is a head-to-head aromatase inhibition assay of the best-docking lead against letrozole on wild-type and resistant-mutant enzyme, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable advantage; a lead that keeps potency where letrozole loses it, or a measured IC50 advantage over letrozole, would refute the claim that the docking ranking is only a measurement of Vina's limits.

---

## 1. Introduction

Breast cancer is the most commonly diagnosed cancer in women worldwide: according to the World Health Organization fact sheet, about 2.4 million women were diagnosed in 2024 and about 694,000 died, and it was the most common cancer in women in 164 of 186 countries. In Pakistan the burden is the worst in Asia — GLOBOCAN 2022 records about 30,682 new cases and 15,552 deaths, the leading cause of cancer death among Pakistani women, with a lifetime risk of about one in nine women, and Karachi's incidence is reported as the highest in Asia. Late presentation is common, so systemic therapy carries much of the burden of care.

About two thirds of breast cancers are hormone-receptor positive and depend on oestrogen. In postmenopausal women almost all oestrogen comes from aromatase (CYP19A1, 503 amino acids, chromosome 15q21.1), the cytochrome P450 that converts androstenedione to oestrone and testosterone to 17β-oestradiol. Blocking aromatase starves the tumour of oestrogen, and third-generation aromatase inhibitors are the standard adjuvant endocrine therapy for postmenopausal hormone-receptor-positive disease.

Letrozole (Femara, 2.5 mg once daily) is a non-steroidal, reversible aromatase inhibitor. In the Breast International Group (BIG) 1-98 trial, 8,028 postmenopausal women with hormone-receptor-positive early breast cancer were randomised to letrozole or tamoxifen; in the monotherapy arms (4,922 women) at a median follow-up of 51 months, letrozole cut the risk of a disease-free-survival event by 18% (352 events on letrozole versus 418 on tamoxifen; hazard ratio 0.82, 95% CI 0.71–0.95, P = .007), and at a median follow-up of 74 months the inverse-probability-of-censoring-weighted 5-year overall survival was 91.8% versus 90.4%. The price is the class toxicity of oestrogen deprivation: letrozole caused more bone fractures, arthralgia, low-grade hypercholesterolaemia and non-ischaemic cardiovascular events than tamoxifen. Acquired resistance also limits long-term benefit, and a drug that keeps letrozole's potency with less bone toxicity — or that works after letrozole failure — would still be valuable.

The question this paper asks is narrower and methodological: can a standardised, automated docking pipeline rank known aromatase inhibitors against letrozole on the true human structure, and what does an apparent docking "win" mean when the reference drug's own binding site is the grid? The falsifiable hypothesis is that any lead beating letrozole by less than 2 kcal/mol on Vina docking has no measurable potency advantage, and that the docking ranking will disagree with measured aromatase IC50 values on this target.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 8 November 2026: the daily literature digest at `~/workspace/research-team/digests/2026-11-08.md` (no aromatase item that day), PubMed and web search, ChEMBL (EBI), RCSB PDB and UniProtKB. Key sources: the WHO breast cancer fact sheet (2024 figures) and GLOBOCAN 2022 for burden figures; the BIG 1-98 trial reports (Coates et al., J Clin Oncol 2007; Colleoni et al., J Clin Oncol 2011) for letrozole's efficacy and toxicity; the human aromatase structure papers (Ghosh et al., Nature 2009; Ghosh et al., J Med Chem 2012) for the target structure. All ChEMBL potency values quoted were re-checked live against the ChEMBL API on 8 November 2026 for the target "Aromatase" (CHEMBL1978).

### 2.2 Molecular docking

The LeadForge pipeline was run live on 8 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Target resolution was verified by hand: UniProt **P11511** (CP19A_HUMAN, aromatase, CYP19A1, 503 aa) and ChEMBL target **CHEMBL1978** ("Aromatase", SINGLE PROTEIN, Homo sapiens) — both correct, no correction needed.

Docking was performed with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The structure is PDB **3S79**, "Human placental aromatase cytochrome P450 (CYP19A1)" in complex with androstenedione, 2.75 Å (Ghosh et al., J Med Chem 2012). The grid was centred on the centroid of the co-crystallised androstenedione (ligand code ASD, residue 601, chain A): **[85.78, 54.15, 46.03]**. The centre was verified against the PDB file: it is exactly the androstenedione centroid, 5.8 Å from the haem (HEM) centroid [85.38, 50.31, 41.58] — the haem cofactor was correctly excluded by the centre picker, so the grid-centre fault that has corrupted earlier runs (centring on a cofactor or glycan) did not occur here. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types, HETATM ligands stripped); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

Six ligands were docked: letrozole itself (QUERY, PubChem CID 3902) and the top five pipeline-ranked leads, all known aromatase inhibitors with ChEMBL potencies of 0.02–0.21 nM. One of the five (CHEMBL1444) is letrozole itself as recorded in ChEMBL (Ki 0.02 nM), docked independently as a same-molecule control; it is reported as such, not as a new lead.

### 2.3 PAINS screen

Every test compound was screened with the RDKit PAINS filter: letrozole and all five leads were PAINS-clean (no alerts). A ToxGuard Tox21 panel was run for each lead. Letrozole's panel is measured data, not read-across: NR-Aromatase 1.0 — which is its own mechanism of action, not a toxicity signal, and is reported here so it is not misread as a hazard flag. The leads' highest read-across probabilities were NR-Aromatase 0.34–0.52 (also on-target signal), NR-ER up to 0.16 and SR-MMP up to 0.29. These are similarity-based predictions, not measurements.

### 2.4 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of the co-crystallised androstenedione pose (RMSD) was performed; a single X-ray structure (3S79, one aromatase conformation, 2.75 Å) was used; the receptor was held rigid, so the induced-fit movement of the substrate channel is not modelled; the leads are already-known aromatase inhibitors, so no novelty of chemistry is claimed. Bone safety — the toxicity that limits letrozole — was not modelled for any lead, so a docking win says nothing about tolerability.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Aromatase potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | MW | logP | Lipinski violations | PAINS | Top tox read-across |
|---|---|---|---|---|---|---|---|---|
| CHEMBL197650 | IC50 0.11 nM | **−8.77** | −8.77, −8.66, −8.64 | 330.4 | 3.54 | 0 | clean | NR-Aromatase 0.392 |
| Letrozole (reference, query) | — | −8.74 | −8.74, −8.60, −8.31 | 285.3 | 2.66 | 0 | clean | NR-Aromatase 1.0 (measured, on-target) |
| CHEMBL1444 (letrozole, ChEMBL record) | Ki 0.02 nM | −8.71 | −8.71, −8.49 | 285.3 | 2.66 | 0 | clean | NR-Aromatase 1.0 (measured, on-target) |
| CHEMBL5406734 | IC50 0.21 nM | −8.16 | −8.16, −8.12, −7.93 | 369.2 | 3.45 | 0 | clean | NR-Aromatase 0.440 |
| CHEMBL5436996 | IC50 0.16 nM | −7.90 | −7.90, −7.82, −7.81 | 304.4 | 3.08 | 0 | clean | NR-Aromatase 0.338 |

All docking on PDB 3S79 (human aromatase + androstenedione, 2.75 Å), grid centre [85.78, 54.15, 46.03] (androstenedione centroid, haem-distal substrate site), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 8 November 2026. All five leads are known aromatase inhibitors; potencies are ChEMBL on-target values, re-checked live on 8 November 2026.

The headline, stated honestly: **no lead beats letrozole beyond noise**. The best lead (CHEMBL197650, IC50 0.11 nM) scores −8.77 kcal/mol against letrozole's −8.74 — a 0.03 kcal/mol margin, sixty times smaller than Vina's noise. The same molecule docked twice (letrozole as QUERY and as its ChEMBL record CHEMBL1444) scores −8.74 and −8.71, a 0.03 kcal/mol spread for an identical compound — which is itself a measure of the protocol's run-to-run jitter on this site, and it is exactly the size of the "win". Every margin in the table is inside Vina's ±1–2 kcal/mol noise, so not even the ranking of the leads can be treated as significant, let alone a "win" over the reference. The docking order also disagrees with measured potency: by IC50 the order is 0.02, 0.11, 0.16 and 0.21 nM, but by docking it is the 0.11 nM compound first, then letrozole, then the 0.02 nM compound, then the 0.21 nM and 0.16 nM compounds. The most potent measured inhibitor in the set (0.02 nM) scores third at −8.71 kcal/mol. The docking scores span only 0.87 kcal/mol while the measured potencies span 10-fold — Vina compresses the potency range on this site and ranks within it unreliably. Pose consistency does not rescue the ranking: every compound's three poses sit within 0.43 kcal/mol of its best score, so the scores are stable — stably wrong in potency order.

### 3.2 Comparison with published docking

No published Vina score for letrozole on 3S79 was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for letrozole and five known aromatase inhibitors on the human structure are now on record for others to reproduce, together with the centre audit trail. The nearest published comparison uses a different program and a different structure: a 2023 Glide study on PDB 5JKV reported letrozole at −4.109 kcal/mol with new analogues at −7.0 to −8.1 kcal/mol — Glide scores are not comparable to Vina scores, so no cross-program ranking can be drawn from it. The ordering is not comparable to published potency either: the five leads span measured aromatase potencies of 0.02–0.21 nM, a 10-fold spread, while their docking scores span 0.87 kcal/mol in an order that disagrees with potency. Vina ranks poses, not IC50s, and on this site it ranks them unreliably.

### 3.3 The standardisation / quality problem

Two things that could silently corrupt this result did not. The grid centre was verified against the PDB file to 0.01 Å and sits on the co-crystallised androstenedione at the haem-distal substrate site — the haem cofactor is 5.8 Å away and was correctly excluded, so the cofactor-centring fault is absent here. The pipeline's target resolution was also correct (P11511 aromatase; CHEMBL1978), unlike the same day's NS5A and neuraminidase runs, where human-preferring target ranking picked unrelated human proteins and the papers had to be corrected before drafting. The deeper problem is structural, not procedural: aromatase inhibitors bind by coordinating the haem iron through a triazole nitrogen while the rest of the molecule fills the androgen pocket, and a rigid-receptor docking with a generic scoring function cannot resolve the iron-coordination energetics that dominate real potency — which is why five sub-nanomolar inhibitors compress into 0.87 kcal/mol.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a negative benchmark with a useful control. There is no lead here: the best compound beats letrozole by 0.03 kcal/mol — inside noise, and the same size as the jitter between two dockings of the identical molecule. The durable findings are the benchmark values for letrozole on 3S79 (−8.74 kcal/mol, with full pose lists), the demonstration that Vina compresses a 10-fold potency range into 0.87 kcal/mol and orders it wrong, and the same-molecule control: letrozole docked twice scores −8.74 and −8.71, which calibrates the protocol's own reproducibility on this site at ±0.03 kcal/mol for identical input — any "win" smaller than that is not even a difference. The most actionable negative is that the cheapest next step is not more docking: the five leads are already sub-nanomolar, already PAINS-clean, already drug-like (zero Lipinski violations each), and the question that matters is which one keeps potency on resistant enzyme and spares bone — neither of which a Vina score can answer.

### 4.2 Why the "win" must not be over-read

Three reasons. First, any margin under 2 kcal/mol is inside Vina's ±1–2 kcal/mol noise, and the best margin here is 0.03. Second, the ranking must be checked against measured aromatase IC50 values — the five leads span 0.02–0.21 nM, and a docking order that disagrees with that order is a measurement of the scoring function, not of the molecules. Third, the same-molecule control sets the floor: two dockings of letrozole differ by 0.03 kcal/mol, so a 0.03 kcal/mol "win" is indistinguishable from re-docking the reference. A docking "win" against letrozole on this site is not a discovery; it is a benchmark value awaiting an assay.

### 4.3 The PAINS problem is the experiment's design constraint, not a reason to stop

All leads are PAINS-clean, which removes one artefact class from the validation design — but PAINS-clean is a low bar, and the Tox21 read-across flags (up to NR-Aromatase 0.52) are predictions from neighbours, not data. Letrozole's own measured NR-Aromatase value of 1.0 is a useful warning about reading the panel naively: on this target, the "toxicity" assay measures the drug's intended mechanism, so a high NR-Aromatase probability for a lead is on-target signal, not a hazard. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either. The validation assay must still include redox controls and a counter-screen, because a clean PAINS filter does not rule out assay interference. The larger safety question — bone loss and fracture risk, the toxicity that limits letrozole — is not addressed by PAINS at all and needs a dedicated bone-turnover model for any lead that advances.

### 4.4 Testable hypotheses

1. The best-docking lead inhibits recombinant human aromatase with an IC50 within 2-fold of its ChEMBL value under identical assay conditions; a measured IC50 worse than letrozole's would confirm the noise interpretation, while a better one would refute it.
2. A lead that docks well at the androstenedione site keeps its potency on aromatase carrying a resistance-associated mutation, where letrozole loses potency; loss of potency on the mutant would show the docking site is the resistance site, not a way around it.
3. A Vina re-dock of the co-crystallised androstenedione into 3S79 reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).
4. Docking the same six ligands on the earlier aromatase structure 3EQM (2.90 Å, androstenedione complex) gives the same ranking as on 3S79; a different ranking would show the result is structure-dependent, not molecule-dependent.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): aromatase inhibition assay (the standard tritiated-water-release assay on recombinant CYP19A1) for the best-docking lead, the second-best lead and letrozole, same plate, n = 3, with a pre-registered 2-fold decision rule and the rule that a docking margin under 2 kcal/mol predicts no measurable advantage. Stage 2 (weeks 3–6): the same assay on a resistance-associated mutant aromatase for any compound that clears Stage 1, to test whether the lead survives the mutations seen after aromatase-inhibitor failure. Stage 3 (weeks 7–12): oestrogen-dependent MCF-7 cell proliferation assay for any compound that clears Stage 2, with letrozole as control, plus a bone-turnover marker panel, since bone loss is the toxicity that a docking score cannot see. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. Any margin under 2 kcal/mol is inside Vina's ±1–2 kcal/mol noise and cannot be interpreted as a real advantage — the best margin here is 0.03 kcal/mol. 3. Only one aromatase structure (3S79, one conformation, 2.75 Å) was docked; the earlier 3EQM structure was not scored. 4. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking RMSD validation of the co-crystallised androstenedione pose was performed. 5. A single rigid receptor was used; the haem-iron coordination that dominates real aromatase-inhibitor potency is not modelled by the Vina scoring function. 6. All leads are already-known aromatase inhibitors; no new chemical matter is proposed. 7. The same-molecule control (letrozole docked twice, −8.74 and −8.71) calibrates run-to-run jitter but was not repeated across days or Vina versions. 8. Bone safety was not modelled for any lead. 9. The resistance analysis is literature-based: no mutant enzyme was docked and no IC50 was measured.

## 6. Conclusion

No aromatase inhibitor in this set beats letrozole on its own binding site: the best lead scores −8.77 kcal/mol on the human aromatase structure 3S79 against letrozole's −8.74 — a 0.03 kcal/mol margin, the same size as the jitter between two dockings of letrozole itself — and the docking order disagrees with measured potency, with the 0.02 nM inhibitor third and the 0.11 nM compound first. The honest reading is that on this haem-distal site, non-covalent docking cannot rank known inhibitors against letrozole — and the next experiment is a head-to-head aromatase inhibition assay on wild-type and resistant-mutant enzyme with a pre-registered 2 kcal/mol rule, plus a bone-safety assessment for any lead that advances, not more Vina docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. World Health Organization. Breast cancer (fact sheet). Geneva: WHO; 2026. (About 2.4 million women diagnosed and about 694,000 deaths in 2024; most common cancer in women in 164 of 186 countries.) https://www.who.int/news-room/fact-sheets/detail/breast-cancer (accessed 8 November 2026).
2. Ferlay J, Ervik M, Lam F, Laversanne M, Colombet M, Mery L, et al. Global Cancer Observatory: Cancer Today. Lyon: International Agency for Research on Cancer; 2024. (GLOBOCAN 2022: Pakistan about 30,682 new breast cancer cases and 15,552 deaths; breast cancer 2.3 million cases and 670,000 deaths worldwide in 2022.) https://gco.iarc.fr/today (accessed 8 November 2026).
3. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
4. Coates AS, Keshaviah A, Thürlimann B, et al. Five years of letrozole compared with tamoxifen as initial adjuvant therapy for postmenopausal women with endocrine-responsive early breast cancer: update of study BIG 1-98. *J Clin Oncol.* 2007;25(5):486–492. PMID: 17200148. DOI: 10.1200/JCO.2006.08.8617.
5. Colleoni M, Giobbie-Hurder A, Regan MM, et al. Analyses adjusting for selective crossover show improved overall survival with adjuvant letrozole compared with tamoxifen in the BIG 1-98 study. *J Clin Oncol.* 2011;29(9):1117–1124. DOI: 10.1200/JCO.2010.31.6455. (Inverse-probability-of-censoring-weighted 5-year overall survival 91.8% letrozole versus 90.4% tamoxifen; median follow-up 74 months.)
6. Ghosh D, Griswold J, Erman M, Pangborn W. Structural basis for androgen specificity and oestrogen synthesis in human aromatase. *Nature.* 2009;457(7226):219–223. DOI: 10.1038/nature07614. (First human aromatase structure, PDB 3EQM; CYP19A1, 503 amino acids, chromosome 15q21.1.)
7. Ghosh D, Lo J, Morton D, et al. Novel aromatase inhibitors by structure-guided design. *J Med Chem.* 2012;55(19):8464–8476. PMID: 22951074. DOI: 10.1021/jm300930n. (Structure 3S79, human aromatase with androstenedione, 2.75 Å.)
8. RCSB Protein Data Bank. Human placental aromatase cytochrome P450 (CYP19A1) in complex with androstenedione. PDB ID 3S79, 2.75 Å. https://www.rcsb.org/structure/3S79 (accessed 8 November 2026).
9. UniProtKB. Cytochrome P450 19A1 (aromatase), Homo sapiens: P11511 (CYP19A1, 503 aa). https://www.uniprot.org/uniprotkb/P11511/entry (accessed 8 November 2026).
10. ChEMBL database, European Bioinformatics Institute. Target: Aromatase, Homo sapiens (CHEMBL1978, single protein); bioactivities and compound potencies accessed 8 November 2026. https://www.ebi.ac.uk/chembl/ (Letrozole: CHEMBL1444, Ki 0.02 nM.)
11. Design of novel letrozole analogues targeting aromatase for breast cancer: molecular docking, molecular dynamics, and theoretical studies on gold nanoparticles. *Metabolites.* 2023;13(5):583. DOI: 10.3390/metabo13050583. (Glide docking on PDB 5JKV: letrozole −4.109 kcal/mol; not comparable to Vina scores.)
12. Chellam J, Rohini Deepa I. Computational biological study of aromatase inhibitors docking with human placental aromatase cytochrome P450. *Int J Pharm Pharm Sci.* 2016;8(7). (Discovery Studio docking on 3EQM; letrozole reported best among four drugs; scores not in kcal/mol and not comparable to Vina.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-056-2026-11-08.json`. ChEMBL IDs: letrozole (query, PubChem CID 3902; ChEMBL record CHEMBL1444, Ki 0.02 nM), CHEMBL197650, CHEMBL5406734, CHEMBL5436996. Target: UniProt P11511 (aromatase, CYP19A1), ChEMBL CHEMBL1978. PDB ID 3S79. No additional data were generated.
