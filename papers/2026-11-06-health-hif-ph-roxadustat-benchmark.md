# No Lead Beats Roxadustat Beyond Noise: A Vina Benchmark of PHD2/EGLN1 Inhibitors on 6QGV and the Missing Metal Ion

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-06 · **Health Papers Agent — Paper #5** (daily 5-paper run)

**Keywords:** PHD2; EGLN1; roxadustat; molecular docking; AutoDock Vina; anaemia; chronic kidney disease; HIF prolyl hydroxylase

---

## Abstract

Anaemia of chronic kidney disease is treated with erythropoiesis-stimulating agents that require injection and iron supplementation, and hypoxia-inducible factor prolyl-hydroxylase inhibitors (HIF-PHIs) offer an oral alternative that raises endogenous erythropoietin and improves iron mobilisation. Roxadustat, the first HIF-PHI, is approved in China, Japan and the European Union but was refused approval in the United States in 2021 on benefit-risk grounds, and the search for a better PHD2 inhibitor continues. We asked whether a standardised, fully automated docking pipeline could rank known PHD2/EGLN1 inhibitors against roxadustat. The LeadForge pipeline was run live on 6 November 2026; its first target query resolved to the wrong enzyme entirely (P4HTM, not PHD2) and was discarded, and its first structure contained the HIF peptide sitting in the binding pocket, so every ligand scored positive and that run was discarded too. On the corrected target (UniProt Q9GZT9, ChEMBL CHEMBL5697, 57 bioactivities) and the corrected structure — PDB 6QGV (1.40 Å), grid centred exactly on the co-crystallised inhibitor J2H centroid [20.93, -0.43, 33.59] — five ligands were docked with AutoDock Vina 1.2.7. The best-scoring lead, CHEMBL5572635, scored -8.38 kcal/mol against roxadustat's -7.50 kcal/mol, a margin of 0.88 kcal/mol that lies inside Vina's ±1-2 kcal/mol scoring noise. The most potent compound by measured IC50, CHEMBL3115307 (0.65 nM), scored -7.54 kcal/mol, effectively tied with roxadustat. No lead beats roxadustat beyond noise, and every score is metal-free because the pipeline's receptor preparation drops the active-site metal ion that roxadustat-class inhibitors chelate, so Vina cannot score the chelation interaction at all. The falsifiable next step is a head-to-head PHD2 enzyme inhibition assay of CHEMBL5572635 against roxadustat under identical conditions, with a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable potency advantage — a measured potency advantage greater than 2-fold for either compound, or a Fe-chelation-aware rescoring that reverses the ranking, would refute the claim that no lead here beats roxadustat.

---

## 1. Introduction

Anaemia is one of the most common complications of chronic kidney disease (CKD), driven by failing erythropoietin production and disordered iron metabolism, and it worsens fatigue, cardiovascular risk and quality of life. The established treatment is erythropoiesis-stimulating agents (ESAs), which require injection, need iron supplementation, and carry their own safety concerns at higher doses. Hypoxia-inducible factor prolyl-hydroxylase inhibitors (HIF-PHIs) are oral alternatives: by inhibiting the PHD enzymes (PHD1/2/3, encoded by EGLN2/1/3) that mark hypoxia-inducible factor alpha for degradation, they stabilise HIF, raise endogenous erythropoietin, improve iron absorption and mobilisation, and reduce hepcidin. Roxadustat (Evrenzo, FG-4592) was the first HIF-PHI: first global approval in China in December 2018, Japan in 2019 for dialysis patients and 2020 for non-dialysis patients, and the European Union in August 2021. In July 2021 the US Food and Drug Administration's Cardiovascular and Renal Drugs Advisory Committee voted 13-1 (non-dialysis) and 12-2 (dialysis) that the benefit-risk profile did not support approval — roxadustat is not approved in the United States. Daprodustat was approved by the FDA in early 2023 for dialysis patients. The phase III programme covered more than 8,000 patients. A 2025 network meta-analysis (searches through 1 May 2025, PROSPERO CRD420251066181) found that in non-dialysis CKD roxadustat gave the greatest haemoglobin rise versus placebo or ESA (mean difference 1.21 g/dL, 95% CI 0.72–1.71; SUCRA 88.6%) and in dialysis CKD 1.78 g/dL (95% CI 1.32–2.24; SUCRA 86.2%), but had the highest adverse-event incidence in non-dialysis CKD (SUCRA 18.4%); its major adverse cardiovascular event hazard ratio versus darbepoetin was similar. The clinical question is whether a better PHD2 inhibitor exists — one with a larger efficacy margin, a cleaner safety profile, or both.

The question this paper asks is narrower and methodological: can a standardised, automated docking pipeline rank known PHD2/EGLN1 inhibitors against roxadustat, and how large is the pipeline's own error? The falsifiable hypothesis is that five known sub-nanomolar to low-nanomolar PHD2 inhibitors, docked under an identical protocol, will score within Vina's noise of roxadustat — and that any apparent "win" smaller than 2 kcal/mol is not a discovery.

## 2. Methods

### 2.1 Literature basis

Sources were searched on 6 November 2026: the daily literature digest (2026-11-06), PubMed and web search (verified references below), ChEMBL (EBI) and RCSB PDB. Key sources: the regulatory history of roxadustat (first approval China December 2018; EU August 2021; FDA advisory committee votes July 2021; daprodustat FDA approval early 2023) and the 2025 network meta-analysis of HIF-PHIs in CKD (PROSPERO CRD420251066181).

### 2.2 Compound selection (LeadForge pipeline) — and a wrong-target fault caught

The LeadForge pipeline was run live on 6 November 2026 (UniProtKB → ChEMBL → PubChem → RDKit → PAINS/ADMET → Vina). Two faults were caught before any number was reported, and both are documented here because they are part of the result. The first target query, "Hypoxia-inducible factor prolyl hydroxylase", resolved in UniProtKB to Q9NXG6 — P4HTM, transmembrane prolyl 4-hydroxylase, a different enzyme from the HIF prolyl hydroxylases (PHD1/2/3 = EGLN2/1/3) that roxadustat targets — and the pipeline docked on PDB 6TP5. That whole run was discarded; its raw JSON is preserved for audit. The run was repeated with the precise gene query "EGLN1": UniProt Q9GZT9 (hypoxia-inducible factor prolyl hydroxylase 2, PHD2/EGLN1, Homo sapiens), ChEMBL CHEMBL5697 (single-protein, human), 57 bioactivities retrieved. Twenty-five compounds passed the Morgan-fingerprint similarity screen and 26 were ranked by composite score (similarity ×40 + Lipinski ×20 + Veber ×10 + PAINS ×10 + tox ×20). The top four ranked leads were taken forward to docking, with roxadustat as the query reference. All four leads are known PHD2/EGLN1 inhibitors with published ChEMBL potencies: CHEMBL5572635 (IC50 1.0 nM), CHEMBL3115302 (IC50 1.5 nM), CHEMBL3115307 (IC50 0.65 nM) and CHEMBL4127286 (IC50 1.9 nM). None of the four has a preferred name, an approval, or a development phase in ChEMBL.

### 2.3 Molecular docking — and a peptide-blocked pocket caught

Docking was performed 6 November 2026 with AutoDock Vina 1.2.7, using the LeadForge protocol: the same structure, grid centre, box (22.5 Å cube), exhaustiveness (8) and pose count (3) for every ligand; best of three poses reported. The first structure the pipeline auto-picked was PDB 7Q5V (1.17 Å, PHD2 in complex with N-oxalylglycine and the HIF-2α CODD peptide). That structure contains the HIF peptide sitting in the binding pocket: every ligand scored between +16.89 and +29.51 kcal/mol — positive scores, meaning clash, not binding — because the peptide physically occupies the site. That run was discarded in full; its raw JSON is preserved for audit. The re-dock used PDB 6QGV (1.40 Å, "HIF prolyl hydroxylase 2 (PHD2/EGLN1) in complex with a spiro[4.5]decanone inhibitor (JPHM-2-167, ligand code J2H)"), a single chain with no peptide in the pocket. The grid centre was placed exactly on the centroid of the co-crystallised inhibitor J2H — [20.93, −0.43, 33.59], verified against the PDB file to 0.01 Å. Receptor preparation used RDKit (Gasteiger charges, simplified AutoDock atom types); ligand preparation used meeko. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone.

One systematic limitation of the receptor preparation is documented here because it bears directly on the result. The active-site metal ion in 6QGV (manganese, 5.48 Å from the grid centre) is dropped by the preparation step, so the docking is metal-free. Roxadustat is a 2-oxoglutarate-competitive inhibitor that chelates the active-site iron; Vina therefore cannot score the chelation interaction at all, and every score in this paper systematically undervalues roxadustat-class binders relative to a metal-aware method. This is not a small correction to be noted in passing — it is the single largest known bias in the comparison, and it works in the leads' favour.

### 2.4 PAINS screen and toxicity read-across

Every test compound was screened with the RDKit PAINS filter: all four leads and roxadustat were PAINS-clean (no alerts). A ToxGuard Tox21 kNN read-across panel (12 assays) was run for each lead. The highest read-across probabilities were NR-ER 0.219 for roxadustat itself, NR-ER 0.163 for CHEMBL3115302, NR-AhR 0.156 for CHEMBL3115307, SR-ARE 0.156 for CHEMBL5572635 and NR-ER 0.078 for CHEMBL4127286. These are similarity-based predictions, not measurements — and roxadustat itself carries the highest flag in the panel, so a flag here does not distinguish a lead from the approved reference drug.

### 2.5 Honesty limits

What this paper cannot show: docking is not activity; Vina noise is ±1–2 kcal/mol; no experimental data are presented; no molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of J2H was performed; a single crystal structure (6QGV, one PHD2 conformation) was used; PHD1 and PHD3 were not docked (roxadustat inhibits all three PHD isoforms); the metal ion was dropped from the receptor, so the chelation interaction that defines roxadustat-class binding is unscored; and the four leads are already-known PHD2 inhibitors, so no novelty of chemistry is claimed.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | PHD2 potency, ChEMBL | Best affinity (kcal/mol) | Poses (kcal/mol) | PAINS |
|---|---|---|---|---|
| CHEMBL5572635 | IC50 1.0 nM | **−8.38** | −8.38, −8.31, −8.25 | clean |
| CHEMBL3115302 | IC50 1.5 nM | −7.96 | −7.96, −7.95, −7.82 | clean |
| CHEMBL3115307 | IC50 0.65 nM | −7.54 | −7.54, −7.32, −7.06 | clean |
| Roxadustat (reference) | — | −7.50 | −7.50, −7.48, −7.18 | clean |
| CHEMBL4127286 | IC50 1.9 nM | −6.37 | −6.37, −6.18, −6.09 | clean |

All docking on PDB 6QGV (human PHD2/EGLN1, 1.40 Å), grid centre [20.93, −0.43, 33.59] (J2H inhibitor centroid), box 22.5 Å, exhaustiveness 8, Vina 1.2.7, 6 November 2026. CHEMBL5572635: MW 418.46, logP 2.15, 0 Lipinski violations. CHEMBL3115302: MW 372.31, logP 0.65, 0 violations. CHEMBL3115307: MW 456.76, logP 2.03, 0 violations. Roxadustat: MW 352.35, logP 2.86, 0 violations. CHEMBL4127286: MW 220.18, logP −0.42, 0 violations.

The headline number is a near-tie, stated plainly: the best lead, CHEMBL5572635, beats roxadustat by 0.88 kcal/mol — inside Vina's ±1–2 kcal/mol noise. The most potent compound by measured IC50, CHEMBL3115307 (0.65 nM), scores −7.54 kcal/mol against roxadustat's −7.50 kcal/mol, a difference of 0.04 kcal/mol — a tie. The total spread across the five molecules is 2.01 kcal/mol, and the only compound clearly separated is CHEMBL4127286, which scores 1.13 kcal/mol worse than roxadustat despite a measured IC50 of 1.9 nM — the ranking is not ordered by potency. Pose consistency does not rescue the ranking: CHEMBL5572635 holds within 0.13 kcal/mol across poses and CHEMBL3115302 within 0.14 kcal/mol, so the poses are stable — but a stable score inside noise is still inside noise. No lead beats roxadustat beyond the margin the method itself cannot resolve, and the metal-free preparation means the reference drug's defining interaction was never scored.

### 3.2 Comparison with published docking

No published Vina score for roxadustat or any of these leads on 6QGV was found to benchmark against — which is itself a gap this paper fills: Vina 1.2.7 reference values for roxadustat and four known PHD2 inhibitors on 6QGV are now on record for others to reproduce, together with the two discarded runs that document what the pipeline gets wrong. The ordering is not comparable to published potency: all four leads are sub-nanomolar to low-nanomolar PHD2 inhibitors (IC50 0.65–1.9 nM, a 3-fold spread), while their docking scores span 2.01 kcal/mol in an order that does not track potency — Vina ranks poses, not IC50s.

### 3.3 The standardisation problem

Three automated steps that could silently corrupt this result did corrupt it, in two different runs. The UniProtKB free-text search for "Hypoxia-inducible factor prolyl hydroxylase" returns P4HTM first — a different enzyme with a similar name — and the pipeline docked on it without complaint. The PDB picker then chose 7Q5V, a structure whose binding pocket is occupied by the HIF peptide, and reported positive clash scores as if they were results. The first two faults are fixed by verification — check the accession, check the co-crystallised ligand and any peptide in the pocket. The third fault, the dropped metal ion, is not fixed by verification: it is a property of the preparation step itself, and it biases every score against the very mechanism that makes roxadustat work. The fix is a metal-aware preparation or a rescoring method that models iron chelation — cheap to describe, not yet implemented in this pipeline, and not optional before any lead is claimed to beat roxadustat.

## 4. Discussion

### 4.1 The reframe

The result reframes the paper from a discovery claim into a measurement of the pipeline's own limits. There is no lead here: the best margin is 0.88 kcal/mol inside noise, the most potent compound ties the reference, and the reference drug's key interaction was never scored. The durable findings are the benchmark values for roxadustat on 6QGV (−7.50 kcal/mol, with full pose lists), the two discarded runs that document the pipeline's failure modes, and the metal caveat that any future PHD2 docking paper from this pipeline must address before claiming a win.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 0.88 kcal/mol margin is smaller than Vina's nominal ±1–2 kcal/mol noise and smaller than the 2.01 kcal/mol total spread of the set. Second, potency and docking score disagree within the lead set: CHEMBL3115307, the most potent by recorded IC50 (0.65 nM), ties roxadustat at −7.54 versus −7.50, while CHEMBL4127286 (1.9 nM) scores a full 1.13 kcal/mol worse than the reference — a 3-fold potency spread against a 2.01 kcal/mol score spread, in no consistent direction. Third, the comparison is structurally unfair to roxadustat: the metal ion its class chelates was dropped from the receptor, so the best lead's margin was earned against a reference drug scored without its defining interaction.

### 4.3 The PAINS/tox picture is clean but thin

No PAINS alerts is good, but PAINS-clean is a low bar, and the Tox21 read-across flags (NR-ER 0.219 for roxadustat, NR-ER 0.163 for CHEMBL3115302) are predictions from neighbours, not data. The honest reading: nothing in the panel kills any lead, and nothing in it advances one either — least of all because the reference drug flags the same assay more strongly than any lead.

### 4.4 Testable hypotheses

1. CHEMBL5572635 inhibits recombinant PHD2 with an IC50 within 2-fold of its ChEMBL value (1.0 nM) under identical assay conditions, and inhibits it more potently than roxadustat — the docking predicts no measurable advantage; a >2-fold advantage for either compound would refute the noise interpretation.
2. A Vina re-dock of the co-crystallised ligand J2H into 6QGV reproduces its crystallographic pose within 2 Å RMSD (protocol self-validation; not yet run).
3. Re-preparing 6QGV with the active-site metal ion retained, or rescoring with an Fe-chelation-aware method, improves roxadustat's score relative to the leads and reverses or erases the 0.88 kcal/mol margin — a pipeline fix to be verified, not assumed.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): recombinant PHD2 enzyme inhibition assay (2-oxoglutarate competition, HIF peptide hydroxylation readout) for CHEMBL5572635, CHEMBL3115307 and roxadustat, same plate, n = 3, with a pre-registered 2-fold decision rule and a pre-registered rule that a docking margin under 2 kcal/mol predicts no measurable potency advantage. Stage 2 (weeks 3–6): iron-chelation assessment (spectrophotometric Fe(II) binding) for any compound that clears Stage 1, to test whether the metal-free docking systematically undervalued it. Stage 3 (weeks 7–12): PHD1 and PHD3 inhibition assays for any compound that clears Stage 2, since roxadustat's clinical profile rests on pan-PHD inhibition and a PHD2-only compound is a different candidate. Total compound cost is the binding constraint; all leads are commercially available research chemicals, not approved drugs, and none may be presented as a treatment.

## 5. Limitations

1. Docking only; no experimental data. 2. The 0.88 kcal/mol best margin is inside Vina's ±1–2 kcal/mol noise, so no margin in this paper is interpretable as a potency advantage. 3. The active-site metal ion was dropped by the receptor preparation, so the iron-chelation interaction that defines roxadustat-class binding is unscored — the comparison is biased against the reference drug. 4. No molecular-dynamics refinement, binding-free-energy calculation, or re-docking validation of J2H was performed. 5. A single crystal structure (6QGV, one PHD2 conformation) was used; the 2-oxoglutarate pocket is flexible and induced-fit effects are not modelled. 6. PHD1 and PHD3 were not docked. 7. All leads are already-known PHD2 inhibitors; no new chemical matter is proposed. 8. The pipeline's automated target resolution and structure selection both failed silently and required manual correction — other silent defaults in the same pipeline are not yet audited.

## 6. Conclusion

No PHD2 inhibitor in this set beats roxadustat: the best lead scores −8.38 kcal/mol against roxadustat's −7.50 kcal/mol, a 0.88 kcal/mol margin inside Vina's noise, and the most potent compound by measured IC50 ties the reference at −7.54 versus −7.50. The durable findings are the benchmark values for roxadustat on 6QGV and the two discarded runs that document the pipeline's failure modes — plus the metal caveat, which means this comparison was scored without the interaction that makes roxadustat work. The next experiment is a head-to-head PHD2 IC50 assay with Fe-chelation-aware rescoring, not more metal-free docking.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author thanks the ChEMBL, UniProtKB, RCSB PDB and PubChem teams for free, open data.

## References

1. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898. PMID: 34278794.
2. RCSB Protein Data Bank. HIF prolyl hydroxylase 2 (PHD2/EGLN1) in complex with a spiro[4.5]decanone inhibitor. PDB ID 6QGV, 1.40 Å. https://www.rcsb.org/structure/6QGV (accessed 6 November 2026).
3. ChEMBL database, European Bioinformatics Institute. Target: hypoxia-inducible factor prolyl hydroxylase 2 (CHEMBL5697); bioactivities accessed 6 November 2026. https://www.ebi.ac.uk/chembl/.
4. Network meta-analysis of hypoxia-inducible factor prolyl hydroxylase inhibitors in chronic kidney disease anaemia (searches through 1 May 2025; PROSPERO registration CRD420251066181). Cited descriptively; no journal or DOI is asserted here.

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-045c-2026-11-06.json` (authoritative re-dock: PDB 6QGV, 1.40 Å, J2H inhibitor centroid [20.93, −0.43, 33.59], Vina 1.2.7). Discarded runs are preserved for audit: `hidden_files/dock-HP-045-2026-11-06.json` (wrong target: UniProt Q9NXG6, P4HTM, docked on PDB 6TP5) and `hidden_files/dock-HP-045b-2026-11-06.json` (PDB 7Q5V, HIF peptide in the pocket, all scores +16.89 to +29.51 kcal/mol). ChEMBL IDs: roxadustat (query), CHEMBL5572635, CHEMBL3115302, CHEMBL3115307, CHEMBL4127286. PDB ID 6QGV. No additional data were generated.
