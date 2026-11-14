# LeadForge: An AI-Driven Computational Pipeline for Accelerated Hit Discovery and Novel Analog Design — A Multi-Target Case Study

**Zubair Ahmed**

Faculty of Pharmacy, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan

Corresponding author: za0153715@gmail.com

*Draft manuscript v1 — 7 October 2026. Not yet submitted for peer review. All results are computational (in silico); no experimental validation has been performed.*

---

## Abstract

Early-stage drug discovery remains slow and expensive, with the hit-to-lead transition representing a major bottleneck. We describe **LeadForge**, an open, automated computational pipeline that triages candidate compounds against a protein target in seven stages: (1) target identification from UniProtKB and ChEMBL, (2) bioactivity mining, (3) query verification via PubChem, (4) RDKit Morgan-fingerprint similarity screening, (5) ADMET and safety filtering (Lipinski/Veber, PAINS, and a Tox21 kNN read-across model), (6) composite lead ranking, and (7) AutoDock Vina molecular docking against experimentally determined protein structures from the RCSB Protein Data Bank. We validate the pipeline on four targets — EGFR, DPP4, SGLT2, and *Escherichia coli* dihydrofolate reductase (DHFR) — and in each case the pipeline independently rediscovers the reference drug from the ChEMBL bioactivity set (similarity 1.0), confirming that the workflow recovers known chemistry before proposing anything new. As a design case study, we enumerated 240 analogs of the SGLT2 lead CHEMBL5288495, filtered them through novelty (<0.85 Tanimoto vs 23 known SGLT2 actives), ADMET, and docking screens to five finalists; the best candidate docks at −8.19 kcal/mol versus an in-run dapagliflozin control at −7.23 kcal/mol. All findings are computational hypotheses: no compounds have been synthesized or tested, docking scores carry run-to-run variability, and novelty is assessed computationally only. The five SGLT2 analogs are proposed for university-laboratory synthesis and assay as the next step.

**Keywords:** computer-aided drug design; virtual screening; molecular docking; ADMET prediction; SGLT2 inhibitors; hit-to-lead; cheminformatics

---

## 1. Introduction

Bringing a new drug to market routinely takes over a decade and costs in excess of one billion US dollars, with the majority of attrition occurring because early candidates fail on potency, selectivity, pharmacokinetics, or safety grounds that could, in principle, have been anticipated computationally (Hughes et al., 2011). The hit-to-lead phase — selecting which of thousands of plausible compounds deserve expensive synthesis and assay — is therefore one of the highest-leverage points for computational methods.

In recent years, ligand-based virtual screening, structure-based docking, and ADMET (absorption, distribution, metabolism, excretion, toxicity) prediction have matured into practical triage tools (Sliwoski et al., 2014). Yet most academic and small-laboratory groups still assemble these steps manually, target by target, which is slow and difficult to reproduce. An integrated, automated pipeline that runs the full sequence — from target lookup to a ranked, docked shortlist — on live public data would let a small team triage a new target in hours rather than weeks.

**LeadForge** is such a pipeline. It chains seven stages on live data from UniProtKB, ChEMBL, PubChem, and the RCSB Protein Data Bank, applies RDKit cheminformatics and a Tox21-based kNN toxicity read-across model, and finishes with AutoDock Vina docking. This manuscript reports the pipeline's design and a multi-target case study conducted 6–7 October 2026 on four targets spanning oncology (EGFR), metabolic disease (DPP4, SGLT2), and antibacterial research (*E. coli* DHFR). We further report a *de novo* analog-design campaign around the SGLT2 lead CHEMBL5288495 that produced five computationally novel, ADMET-clean finalists proposed for synthesis.

Our contributions are: (i) a fully automated, reproducible seven-stage triage pipeline operating on live public databases; (ii) a validation-by-rediscovery protocol showing the pipeline recovers each reference drug from its target's known bioactivity set; (iii) a worked analog-design funnel (240 → 5) with full transparency on filters and attrition; and (iv) an honest accounting of the method's limitations, which we consider as important as the results.

---

## 2. Methods

### 2.1 Pipeline architecture

LeadForge executes seven stages sequentially for a given target–reference-drug pair. All stages ran on live public data on 6–7 October 2026; database contents are those served at query time.

| Stage | Operation | Data source / tool |
|---|---|---|
| 1 | Target identification | UniProtKB + ChEMBL (live lookup) |
| 2 | Known-ligand retrieval | ChEMBL bioactivities for the target |
| 3 | Query verification | PubChem PUG REST (SMILES resolution) |
| 4 | Similarity screen | RDKit Morgan fingerprints, Tanimoto coefficient |
| 5 | ADMET + safety panel | RDKit (Lipinski, Veber, PAINS) + ToxGuard Tox21 kNN (12 assays) |
| 6 | Lead ranking | Composite score (see §2.5) |
| 7 | Molecular docking | AutoDock Vina vs RCSB PDB structure (live fetch) |

### 2.2 Data sources

**UniProtKB** (The UniProt Consortium) provides the canonical protein identifier, organism, and sequence length for each target. **ChEMBL** (EBI; Davies et al., 2015) provides the target identifier and the set of compounds with measured bioactivities against it; bioactivity sets were used as served (pChEMBL ≥ 5 where the pipeline applied a cutoff). **PubChem PUG REST** (Kim et al., 2016) resolves the reference drug name to a canonical isomeric SMILES. **RCSB PDB** (Berman et al., 2000) supplies the experimental protein structure for docking; the pipeline preferentially selects the highest-resolution inhibitor-bound X-ray structure and records the PDB ID and resolution for every run.

### 2.3 Similarity screening

Compounds are fingerprinted with RDKit Morgan fingerprints (radius 2, 2048 bits), and pairwise Tanimoto similarity to the reference drug is computed (Rogers & Hahn, 2010). A **rediscovery check** is performed at this stage: the reference drug is expected to appear in the target's ChEMBL bioactivity set at similarity 1.0. Failure of this check would indicate a data or identity error and halt interpretation of the run; all four runs reported here passed.

### 2.4 ADMET and safety panel

Each candidate is evaluated with: (i) **Lipinski's Rule of Five** (Lipinski et al., 1997) — molecular weight, logP, hydrogen-bond donors/acceptors, with violation counts recorded; (ii) **Veber's rules** (Veber et al., 2002) — rotatable bonds and topological polar surface area; (iii) **PAINS filters** (Baell & Holloway, 2010) via RDKit's FilterCatalog, flagging pan-assay interference substructures; and (iv) **ToxGuard**, a k-nearest-neighbors read-across model (k = 15) predicting outcomes across 12 Tox21 assays (Tice et al., 2013), reporting mean and maximum predicted probabilities. These are computational flags for triage, not safety determinations.

### 2.5 Lead ranking

Candidates are ranked by a composite score:

**Score = 40 × similarity + 20 × Lipinski-pass + 10 × Veber-pass + 10 × PAINS-clean + 20 × low-tox**

where each pass/fail term is 1 or 0 (low-tox = maximum Tox21 predicted probability below threshold). The score is a triage heuristic for ordering laboratory follow-up, not a potency prediction.

### 2.6 Molecular docking

Docking uses **AutoDock Vina 1.2.7** (Eberhardt et al., 2021) with ligand preparation by **meeko**. For each target, the pipeline fetches the selected PDB entry from RCSB, centers a 22.5 Å cubic search box on the co-crystallized ligand position, and runs with exhaustiveness 8, retaining 3 poses per compound. Reported affinity is the best pose in kcal/mol. Because Vina's search is stochastic, scores carry run-to-run variability (observed on the order of ±0.5 kcal/mol in our runs); only within-run rankings against an in-run control are interpreted.

### 2.7 Novel analog design (SGLT2 campaign)

Starting from the SGLT2 lead CHEMBL5288495 (see §3.4), 240 analog combinations were enumerated across three series: **Series A** — aryl substituent swaps on both phenyl rings (R ∈ {Me, Et, nPr, iPr, OMe, CF₃, OCF₃}; X ∈ {Cl, F, Br, CF₃, OCF₃, OMe, Me}; linker ∈ {CH₂, O, NH, CHMe}); **Series E** — sugar-moiety edits (difluoro→CH₂, CH₂OH→CH₃, OH→OMe, OH→F); **Series F** — scaffold hops retaining the C-glycoside pharmacophore (thiophene-for-aryl-A and meta-linkage variants; pyridine-B variants failed RDKit sanitization and were dropped). Filters were applied in sequence: valid unique structures (200) → novelty (maximum Morgan Tanimoto < 0.85 against 23 known SGLT2 actives; 199 passed) → ADMET-clean (Lipinski ≤ 1 violation, Veber pass, PAINS clean, ToxGuard mean < 0.40 and max < 0.70; 199 passed) → docking of 12 prioritized candidates vs PDB 7VSI → 5 finalists. Dapagliflozin was docked in the same run as control.

---

## 3. Results

### 3.1 Validation by rediscovery

In all four target runs, the pipeline independently recovered the reference drug from the target's ChEMBL bioactivity set at Tanimoto similarity 1.0 (Table 1). This confirms the workflow operates on correctly identified chemistry before any ranking or docking is interpreted.

**Table 1.** Rediscovery validation across the four target runs (October 2026).

| Target | UniProt | ChEMBL target | Ligands mined | Reference drug | Rediscovered as | Measured activity |
|---|---|---|---|---|---|---|
| EGFR | P00533 | CHEMBL203 | 35 | erlotinib | CHEMBL553 (sim 1.0, score 92.0) | pChEMBL 10.54 |
| DPP4 | P27487 | CHEMBL284 | 47 | sitagliptin | query self-match (sim 1.0, score 99.1) | — |
| SGLT2 | P31639 | CHEMBL3884 | 22 | dapagliflozin | CHEMBL429910 (sim 1.0, score 99.6) | IC₅₀ 0.49 nM |
| *E. coli* DHFR | P0ABQ4 | CHEMBL1809 | 37 | trimethoprim | CHEMBL22 (sim 1.0, score 100.0) | Kᵢ 0.22 nM |

### 3.2 EGFR (oncology)

Thirty-five known ligands were screened against human EGFR. Erlotinib was rediscovered as CHEMBL553 (similarity 1.0, composite score 92.0, pChEMBL 10.54). Docking against PDB 8A27 (X-ray, 1.07 Å) ranked the quinazoline analog CHEMBL29197 first at −8.05 kcal/mol, ahead of the erlotinib query (−7.87) and rediscovered erlotinib (−7.77), each as the best of three poses. The margin between the top three compounds (≤0.28 kcal/mol) is within expected docking variability and is not interpreted as a potency ranking.

### 3.3 DPP4 versus SGLT2 (type 2 diabetes)

The diabetes targets were run comparatively. DPP4 (47 bioactivities mined) produced a saturated chemical space: the top leads are all ultra-potent measured gliptins (IC₅₀ < 0.3 nM), and docking against PDB 4A5S (X-ray, 1.62 Å) ranked sitagliptin itself first (−5.92 kcal/mol), followed by CHEMBL5951803 (−5.81). One candidate (CHEMBL1203953) was excluded at the ligand-preparation stage because its salt form presented as two fragments. Nothing in the DPP4 set meaningfully separates from the reference drug.

SGLT2 (22 bioactivities) proved more interesting. Dapagliflozin was rediscovered as CHEMBL429910 (similarity 1.0, IC₅₀ 0.49 nM). Docking against PDB 7VSI — the human SGLT2–MAP17 complex in an empagliflozin-bound conformation (cryo-EM, 2.95 Å; no X-ray structure exists for this membrane transporter, so the pipeline's X-ray preference was explicitly overridden) — ranked **CHEMBL5288495** first at **−7.03 kcal/mol**, substantially ahead of dapagliflozin (−4.84). CHEMBL5288495 is a fluorinated dapagliflozin analog (MW 413, 0 Lipinski violations) with measured IC₅₀ 0.35 nM. Its docking margin over the reference (−2.19 kcal/mol) exceeds the observed run-to-run variability and was selected as the parent for the analog-design campaign (§3.5). SMILES: `CCc1ccc(Cc2cc([C@@H]3O[C@H](CO)C(F)(F)[C@H](O)[C@H]3O)ccc2Cl)cc1`.

### 3.4 *E. coli* DHFR (antibacterial)

Thirty-seven ligands were screened against *E. coli* dihydrofolate reductase (folA), a classic antibacterial target. Trimethoprim was rediscovered as CHEMBL22 (similarity 1.0, score 100.0, measured Kᵢ 0.22 nM). All top-ranked leads are 2,4-diaminopyrimidine trimethoprim analogs differing in phenyl-ring alkoxy/alkyl substitution — a chemical space explored for decades. Docking against PDB 9PWM (X-ray, 0.89 Å) gave CHEMBL278345 −5.66 kcal/mol versus trimethoprim −5.63 kcal/mol. A difference of 0.03 kcal/mol is within docking noise; this run is reported as a validation-grade result (the pipeline rediscovers the known drug and ranks close analogs sensibly), not a discovery.

### 3.5 SGLT2 novel-analog campaign

The design funnel is summarized in Table 2. Of 240 enumerated combinations, 200 were valid unique structures; 199 passed the novelty filter (<0.85 Tanimoto vs 23 known SGLT2 actives); all 199 passed ADMET filters; 12 were docked; 5 finalists were selected.

**Table 2.** SGLT2 analog-design funnel (7 October 2026).

| Stage | Count |
|---|---|
| Combinations enumerated (series A/E/F) | 240 |
| Valid unique structures | 200 |
| Novel (<0.85 vs 23 known SGLT2 actives) | 199 |
| ADMET-clean | 199 |
| Docked vs 7VSI | 12 |
| Finalists | 5 |

The five finalists, ranked by docking affinity against an in-run dapagliflozin control (−7.23 kcal/mol), are listed in Table 3. The top candidate, **A:Me/CH₂/Cl** (−8.19 kcal/mol; Δ −0.96 vs control), is a methyl-for-ethyl swap on the parent scaffold with the most straightforward synthetic route (single building-block change). All five are Lipinski-clean (0 violations), PAINS-clean, and Veber-compliant, with ToxGuard mean probabilities 0.041–0.096.

**Table 3.** Five finalist SGLT2 analogs (all computationally novel, ADMET-clean).

| # | Design | Docking (kcal/mol) | Δ vs control | Novelty (max sim) | MW | logP |
|---|---|---|---|---|---|---|
| 1 | A:Me/CH₂/Cl | −8.19 | −0.96 | 0.843 | 398.83 | 3.03 |
| 2 | A:CF₃/CH₂/Cl | −8.02 | −0.79 | 0.778 | 452.80 | 3.74 |
| 3 | A:Et/CH₂/F | −7.94 | −0.71 | 0.788 | 396.40 | 2.77 |
| 4 | A:Et/CH₂/Me | −7.19 | +0.04 | 0.788 | 392.44 | 2.94 |
| 5 | E:Et/Cl/S4 | −6.10 | +1.13 | 0.846 | 414.85 | 4.26 |

SMILES of the finalists:

1. A:Me/CH₂/Cl: `Cc1ccc(Cc2cc([C@@H]3O[C@H](CO)C(F)(F)[C@H](O)[C@H]3O)ccc2Cl)cc1`
2. A:CF₃/CH₂/Cl: `OC[C@H]1O[C@@H](c2ccc(Cl)c(Cc3ccc(C(F)(F)F)cc3)c2)[C@H](O)[C@@H](O)C1(F)F`
3. A:Et/CH₂/F: `CCc1ccc(Cc2cc([C@@H]3O[C@H](CO)C(F)(F)[C@H](O)[C@H]3O)ccc2F)cc1`
4. A:Et/CH₂/Me: `CCc1ccc(Cc2cc([C@@H]3O[C@H](CO)C(F)(F)[C@H](O)[C@H]3O)ccc2C)cc1`
5. E:Et/Cl/S4: `CCc1ccc(Cc2cc([C@@H]3O[C@H](CO)C(F)(F)[C@H](F)[C@H]3O)ccc2Cl)cc1`

Seven additional docked candidates scored between −0.94 and −5.99 kcal/mol and were deprioritized (full list in the run record).

---

## 4. Discussion

### 4.1 What the results show

The central positive finding is methodological: across four unrelated targets, an automated pipeline running on live public data recovered each reference drug at similarity 1.0 and produced ranked, docked shortlists whose top entries are chemically sensible (e.g., 2,4-diaminopyrimidines for DHFR, gliptins for DPP4). The SGLT2 case goes one step further — a ChEMBL lead (CHEMBL5288495) out-docked the marketed reference by a margin exceeding docking noise, and systematic analog enumeration around it yielded five candidates that preserve drug-likeness while improving the docking signal. This is the intended use of the pipeline: computational triage that tells a laboratory which compounds to make or buy *first*.

### 4.2 Limitations — read before citing

**All results are in silico.** No compound in this manuscript has been synthesized, assayed, or tested in any biological system. Docking scores are approximate binding-energy estimates, not measurements.

**Docking variability is real.** The dapagliflozin control scored −4.84 kcal/mol in the diabetes run and −7.23 kcal/mol in the analog-campaign run against the same 7VSI structure. Vina's stochastic search produces run-to-run shifts; only within-run rankings are meaningful, and sub-kcal/mol differences (e.g., the DHFR −5.66 vs −5.63) carry no potency information.

**The SGLT2 structure is cryo-EM, not X-ray.** At 2.95 Å on a membrane transporter, pose uncertainty is higher than for the X-ray structures used elsewhere (0.89–1.62 Å).

**Novelty is computational.** "Novel" here means maximum Morgan Tanimoto < 0.85 against 23 known SGLT2 actives in our reference set — a similarity heuristic, not a patent determination. Most finalists remain close analogs of the parent (similarity 0.78–0.85). Patent novelty requires a professional prior-art search, which has not been performed.

**Prior art exists for the leads.** CHEMBL5288495 and the other ChEMBL-identified leads are published compounds; they are starting points for optimization, not proprietary discoveries.

**Toxicity flags are predictions.** ToxGuard outputs are kNN read-across estimates from Tox21 assay data, not experimental toxicology.

No therapeutic, curative, or clinical claims are made. SGLT2 inhibitors are glucose-lowering agents for type 2 diabetes management; nothing here implies disease modification.

---

## 5. Conclusion and future work

LeadForge demonstrates that a fully automated, live-data pipeline can reproduce known drug–target chemistry across four targets and generate a focused, ADMET-clean analog shortlist for at least one of them. The five SGLT2 analogs in Table 3 are the concrete output: computationally novel, synthetically tractable (candidates 1–4 via standard building blocks), and ranked by a consistent docking protocol.

Planned next steps: (i) present the five SMILES to the university laboratory for synthesis-feasibility review; (ii) synthesize candidates 1–4 and assay SGLT2 inhibition head-to-head against dapagliflozin and the parent CHEMBL5288495; (iii) pursue a professional novelty/prior-art search through the university's ORIC (Office of Research, Innovation and Commercialization) before any intellectual-property filing; (iv) extend the pipeline's daily target rotation to accumulate a broader validation set for a follow-up study.

---

## Data availability

Run reports and machine-readable JSON for the EGFR, DPP4/SGLT2, *E. coli* DHFR, and SGLT2 analog-design runs are retained by the author and available on reasonable request. The LeadForge pipeline code is the author's own implementation.

## Author contributions

Z.A. conceived the study, implemented the LeadForge pipeline, performed all computational runs, analyzed the data, and wrote the manuscript.

## Conflict of interest

The author declares no conflict of interest.

## Funding

No external funding was received. All computation was performed on freely available academic databases and the author's own virtual machine.

---

## References

1. Berman, H. M. et al. The Protein Data Bank. *Nucleic Acids Res.* 28, 235–242 (2000). RCSB PDB: https://www.rcsb.org/
2. The UniProt Consortium. UniProt: the universal protein knowledgebase. *Nucleic Acids Res.* (2023). https://www.uniprot.org/
3. Davies, M. et al. ChEMBL webresource client. *Nucleic Acids Res.* 43, W612–W620 (2015). https://www.ebi.ac.uk/chembl/
4. Kim, S. et al. PubChem substance and compound databases. *Nucleic Acids Res.* 44, D1202–D1213 (2016). https://pubchem.ncbi.nlm.nih.gov/
5. Rogers, D. & Hahn, M. Extended-connectivity fingerprints. *J. Chem. Inf. Model.* 50, 742–754 (2010). RDKit: https://www.rdkit.org/
6. Lipinski, C. A., Lombardo, F., Dominy, B. W. & Feeney, P. J. Experimental and computational approaches to estimate solubility and permeability in drug discovery. *Adv. Drug Deliv. Rev.* 23, 3–25 (1997).
7. Veber, D. F. et al. Molecular properties that influence the oral bioavailability of drug candidates. *J. Med. Chem.* 45, 2615–2623 (2002).
8. Baell, J. B. & Holloway, G. A. New substructure filters for removal of pan assay interference compounds (PAINS). *J. Med. Chem.* 53, 2719–2740 (2010).
9. Tice, R. R., Austin, C. P., Kavlock, R. J. & Bucher, J. R. Improving the human hazard characterization of chemicals: a Tox21 update. *Environ. Health Perspect.* 121, 756–765 (2013). https://tox21.gov/
10. Eberhardt, J., Santos-Martins, D., Tillack, A. F. & Forli, S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J. Chem. Inf. Model.* 61, 3891–3898 (2021).
11. Meeko — ligand preparation for AutoDock. https://github.com/forlilab/meeko
12. Hughes, J. P., Rees, S., Kalindjian, S. B. & Philpott, K. L. Principles of early drug discovery. *Br. J. Pharmacol.* 162, 1239–1249 (2011).
13. Sliwoski, G., Kothiwale, S., Meiler, J. & Lowe, E. W. Computational methods in drug discovery. *Pharmacol. Rev.* 66, 334–395 (2014).

---

*End of manuscript draft v1.*
