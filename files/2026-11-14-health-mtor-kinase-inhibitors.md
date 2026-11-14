# ATP-Competitive mTOR Inhibitors Are All Sub-Nanomolar but Docking Spreads Them Over 1.78 kcal/mol — and Ranks Them Backwards

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification.**

**Author:** Zubair Ali, Pharm-D student, Faculty of Pharmacy, SMBBMU, Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 14 November 2026
**Topic ID:** HP-058

## Abstract

The mechanistic target of rapamycin (mTOR) is a serine/threonine kinase that controls cell growth and is frequently deregulated in cancer. First-generation mTOR drugs (rapalogs such as everolimus) are allosteric: they bind the FRB domain via FKBP12 and block substrate recruitment. Second-generation inhibitors compete directly with ATP in the kinase domain and inhibit both mTOR complexes. We benchmarked rigid AutoDock Vina docking against measured mTOR inhibition data for five ATP-competitive inhibitors (IC50 0.10–0.20 nM), docked into the Torin2-bound kinase-domain structure 4JSX (3.5 Å). The five compounds are essentially equipotent in the assay — a two-fold range, equivalent to ~0.4 kcal/mol — but docking spread them over 1.78 kcal/mol (−7.67 to −9.45 kcal/mol) and ranked them backwards (Spearman ρ = −0.4, n = 5): the 0.20 nM compound scored best (−9.45 kcal/mol) and the 0.13 nM compound scored worst (−7.67 kcal/mol). The negative control could not be scored at all: everolimus, a 958-Da macrolide with ~30 rotatable bonds, crashed the docking run (Vina non-zero exit after ~20 min of compute), so no ATP-site score was obtained. The method invents differences where the assay sees near-equality, and it cannot even run the reference drug. Two pipeline lessons are recorded: the automated PDB lookup hung on the structure search, and its <3.0 Å resolution filter can never select a kinase-domain structure for mTOR, because every structure better than 3.0 Å is an FRB-domain fragment. Docking scores should not prioritise analogues among sub-nanomolar mTOR inhibitors.

**Keywords:** mTOR; kinase inhibitor; everolimus; Torin2; molecular docking; AutoDock Vina; ATP-competitive; cancer

## Introduction

The mechanistic target of rapamycin (mTOR) is a phosphoinositide 3-kinase-related protein kinase (PIKK) that controls cell growth in response to nutrients and growth factors and is frequently deregulated in cancer. It operates in two complexes, mTORC1 and mTORC2, with different substrates and functions. The first drugs against it — sirolimus (rapamycin) and its analogues everolimus and temsirolimus — are allosteric: the drug binds FKBP12, and the drug–protein complex binds the FRB domain of mTOR, blocking substrate recruitment and restricting access to the active site (Yang et al., *Nature* 2013). They inhibit mTORC1 preferentially and incompletely, and they do not touch mTORC2. Resistance and feedback reactivation of AKT limited their efficacy, which drove the development of second-generation, ATP-competitive mTOR kinase inhibitors that occupy the ATP pocket and inhibit both complexes (García-Echeverría et al., *Bioorg Med Chem Lett* 2010).

This paper benchmarks rigid docking for five ATP-competitive mTOR inhibitors with measured IC50 values of 0.10–0.20 nM, and asks whether docking can rank compounds that the assay can barely distinguish. Everolimus serves as the negative control: it does not bind the ATP site at all, so a method that scores it alongside ATP-competitive inhibitors cannot discriminate binding modes.

## Methods

### 2.1 Target and compound selection

Human mTOR (UniProt P42345) was resolved to ChEMBL target CHEMBL2842 (47 known ligands). The reference compound was everolimus (PubChem CID 6436034; C53H83NO14; MW 958.24), an allosteric rapalog. The pipeline ranked 26 leads and docked the top five. All five are ATP-competitive kinase inhibitors with sub-nanomolar measured IC50 values, and all are PAINS-clean. Everolimus ranked 14th of 26 in the pipeline and has no ChEMBL mTOR IC50 attached in this run; it is included as the mechanistic negative control.

### 2.2 Structure: why the pipeline could not pick it

The automated PDB lookup (`find_pdb_for_uniprot`) hung during this run — it iterates up to twelve candidate structure downloads through a flaky proxy — and was bypassed. Its design would have failed anyway: it accepts only structures better than 3.0 Å, and for mTOR every structure better than 3.0 Å is an FRB-domain fragment (for example 4DRI at 1.45 Å and 3FAP at 1.85 Å). The kinase-domain structures are all 3.3–3.5 Å. We therefore selected 4JSX manually: the mTORΔN–mLST8 complex with Torin2 bound (Yang et al., *Nature* 2013;497:217–223; PMID 23636326), 3.5 Å, residues 1376–2549. The docking centre was the co-crystallised Torin2 centroid (chain A, [49.98, −1.37, −47.78]) — the ATP-binding pocket itself. All docking used AutoDock Vina 1.2.7, exhaustiveness 8, box 22.5 Å. The active site is, as Yang et al. describe it, "highly recessed owing to the FRB domain and an inhibitory helix protruding from the catalytic cleft" — a confined pocket, which matters for interpreting the scores.

### 2.3 Limitations of the docking model, stated in advance

The structure is **3.5 Å** resolution — the lowest-resolution structure used in this series — so side-chain positions in the pocket are uncertain. Receptor preparation drops HETATM records, so Mg2+ and the ATPγS present in the related structure 4JSP are **absent** from the docked receptor. Rigid docking carries a documented ±1–2 kcal/mol noise band. The measured potency range (0.10–0.20 nM, two-fold, ~0.4 kcal/mol) is far below that noise band, so no ranking can be resolved even in principle. Everolimus is very large (MW 958, ~30 rotatable bonds) and may be under-sampled at exhaustiveness 8. The rank correlation uses only five compounds.

### 2.4 Literature

Measured potencies and source documents were taken from ChEMBL (accessed 14 November 2026) and verified against the original papers. The 4JSX structure and the FRB-gatekeeper mechanism are from Yang et al. (2013). The allosteric/ATP-competitive distinction is from García-Echeverría et al. (2010).

## Results

### 3.1 The compounds

The five inhibitors come from four independent series (Table 1): a triazine (CHEMBL1091714, Verheijen et al. 2010), a pyrimido-pyrimidine from a 2015 patent document (CHEMBL3693444), and two pyrazolopyrimidines (CHEMBL576090, Richard et al. 2009; CHEMBL606423, Curran et al. 2010), plus CHEMBL1801204, whose value is compiled in the García-Echeverría et al. (2010) review. All five share the morpholine/morpholine-like hinge-binding motif typical of PI3K/mTOR kinase inhibitors. Their measured IC50 values span only 0.10–0.20 nM. One value is assay-dependent: CHEMBL1801204 is recorded at 0.13 nM in the pipeline's record and at 0.8 nM in a second assay record; the lower value was used, which favours the docking comparison.

**Table 1. ATP-competitive mTOR inhibitors docked on 4JSX (Torin2-bound kinase domain, 3.5 Å).**

| Compound | Measured IC50 (nM) | Source | Vina score (kcal/mol) |
|---|---|---|---|
| CHEMBL576090 | 0.20 | Richard et al. 2009 | −9.45 |
| CHEMBL1091714 | 0.10 | Verheijen et al. 2010 | −9.32 |
| CHEMBL606423 | 0.19 | Curran et al. 2010 | −9.06 |
| CHEMBL3693444 | 0.15 | Patent document, 2015 | −7.94 |
| CHEMBL1801204 | 0.13 | García-Echeverría et al. 2010 | −7.67 |
| Everolimus (QUERY) | allosteric, no ATP-site activity | — | docking failed (Vina error after ~20 min, no score) |

### 3.2 The ranking is backwards — and the spread exceeds the signal

The five inhibitors scored between −7.67 and −9.45 kcal/mol: a 1.78 kcal/mol spread for compounds whose measured potencies differ by 0.4 kcal/mol. The rank correlation was Spearman ρ = −0.4 (n = 5): the least potent compound (CHEMBL576090, 0.20 nM) scored best (−9.45 kcal/mol), and the second most potent (CHEMBL1801204, 0.13 nM) scored worst (−7.67 kcal/mol). The method does not merely fail to resolve the ranking — it inverts it, and it manufactures a 1.78 kcal/mol spread where the assay reports near-equality. Three compounds cluster at −9.06 to −9.45 and two at −7.67 to −7.94, a 1.1 kcal/mol gap between the clusters that has no counterpart in the measured data.

### 3.3 The negative control could not be run

Everolimus was included as the mechanistic negative control: it binds the FRB domain via FKBP12 and does not occupy the ATP site, so it should score poorly there — the same logic as miltefosine in the trypanothione reductase paper in this series, which scored −4.54 kcal/mol against −7.75 to −8.56 for genuine inhibitors. No such comparison was possible here. The everolimus dock ran for ~20 min of Vina compute on the 4JSX receptor and then failed with a non-zero exit and no score; the run's JSON records the error. A 958-Da macrolide with ~30 rotatable bonds against a 342-kDa receptor is beyond what this setup can handle in reasonable time. The control is therefore reported as failed, not as a score — and the failure is itself informative: the pipeline that ranks small ATP-competitive inhibitors cannot even evaluate the reference drug it was asked about.

## Discussion

Three findings, in order of importance.

**First, the method invents differences where the assay sees near-equality.** Five inhibitors spanning 0.10–0.20 nM — a 0.4 kcal/mol range — were spread over 1.78 kcal/mol by docking, and ranked backwards (ρ = −0.4). The two clusters (−9.06 to −9.45 vs −7.67 to −7.94) have no counterpart in the measured data. Any analogue-prioritisation scheme built on these scores would have synthesised the wrong compounds first. The honest interpretation is that, within a set of sub-nanomolar inhibitors, Vina scores carry no ranking information at all — the measured differences are four times smaller than the method's noise.

**Second, the control failure matters as much as the ranking failure.** Everolimus is the clinically relevant reference for this target — the drug actually given to patients — and the docking setup could not produce a number for it. A benchmark that cannot run its own reference compound is incomplete, and any pipeline that silently drops large flexible ligands will systematically exclude exactly the macrolide and natural-product-like chemotypes that mTOR drug discovery started from.

**Third, the pipeline's automation failed twice on this target, in ways that generalise.** The PDB lookup hung on the structure search (twelve candidate downloads through a flaky proxy), and its <3.0 Å resolution filter can never select a kinase-domain structure for mTOR, because every sub-3.0 Å structure is an FRB-domain fragment. A resolution-first heuristic is a domain-blind heuristic: for multi-domain targets it will confidently pick the wrong domain. Structure selection needs a ligand-site check (is an ATP-site ligand bound?) before a resolution check.

For the clinic, the implication is narrow but real: ATP-competitive mTOR inhibitors are a genuine advance over rapalogs — they inhibit both mTORC1 and mTORC2, where everolimus is mTORC1-biased — but choosing among sub-nanomolar candidates requires assays, not docking scores. The compounds in Table 1 are all potent enough that the decision between them should turn on selectivity (mTOR vs PI3K), pharmacokinetics and toxicity, none of which a Vina score measures.

## Limitations

1. **No lab data.** All results are computational; no mTOR assay was run.
2. **Low resolution.** 4JSX is 3.5 Å; side-chain positions in the pocket are uncertain.
3. **Cofactors removed.** Mg2+ was dropped during receptor preparation; the docked pocket lacks it.
4. **Measured range below noise.** The 0.10–0.20 nM range (~0.4 kcal/mol) is far inside Vina's ±1–2 kcal/mol noise band; ranking was unresolvable in principle.
5. **Small n.** The rank correlation uses five compounds from four different series; a single additional compound could change ρ substantially.
6. **Assay heterogeneity.** The five IC50 values come from four different papers and one patent document, measured in different assays; cross-series comparison adds noise beyond the docking itself.
7. **Everolimus docking failed.** The macrolide's ~30 rotatable bonds against the 342-kDa receptor ended in a Vina error after ~20 min; no ATP-site score was obtained, so the negative-control comparison is absent rather than negative.
8. **One assay discrepancy.** CHEMBL1801204 has a second assay record at 0.8 nM; using the lower (0.13 nM) value favoured the docking comparison and it still failed.

## Conclusion

Rigid docking into the mTOR kinase domain (4JSX, Torin2-bound, 3.5 Å) cannot rank five ATP-competitive inhibitors that the assay reports as essentially equipotent (IC50 0.10–0.20 nM): it spread them over 1.78 kcal/mol and ranked them backwards (Spearman ρ = −0.4), with the 0.20 nM compound scoring best and the 0.13 nM compound worst. The reference drug everolimus could not be docked at all — the run failed after ~20 min — so no negative-control comparison was possible. Within a sub-nanomolar series, docking scores carry no ranking information, and analogue prioritisation should rest on measured selectivity, pharmacokinetics and toxicity instead. Structure selection for multi-domain targets must check the ligand site before the resolution.

## Acknowledgments

Manuscript drafted with AI assistance (Lapis). The author reviewed all computed values against the raw docking outputs and all citations against the primary sources. This is an AI-assisted draft, not a peer-reviewed publication; all claims require independent laboratory verification. No funding was received. The author declares no conflicts of interest.

## References

1. Yang H, Rudge DG, Koos JD, Vaidialingam B, Yang HJ, Pavletich NP. mTOR kinase structure, mechanism and regulation. *Nature*. 2013;497(7448):217–223. PMID: 23636326. doi:10.1038/nature12122.
2. García-Echeverría C, et al. Allosteric and ATP-competitive kinase inhibitors of mTOR for cancer treatment. *Bioorg Med Chem Lett*. 2010;20(15):4308–4312. PMID: 20561789. doi:10.1016/j.bmcl.2010.05.099.
3. Verheijen JC, et al. 2-Arylureidophenyl-4-(3-oxa-8-azabicyclo[3.2.1]octan-8-yl)triazines as highly potent and selective mTOR inhibitors. *Bioorg Med Chem Lett*. 2010;20(8):2648–2653. PMID: 20223663. doi:10.1016/j.bmcl.2010.02.031.
4. Richard DJ, et al. Incorporation of water-solubilizing groups in pyrazolopyrimidine mTOR inhibitors. *Bioorg Med Chem Lett*. 2009;19(24):6830–6835. PMID: 19896845. doi:10.1016/j.bmcl.2009.10.096.
5. Curran KJ, et al. Pyrazolopyrimidines as highly potent and selective, ATP-competitive inhibitors of the mammalian target of rapamycin (mTOR). *Bioorg Med Chem Lett*. 2010;20(4):1440–1444. PMID: 20089401. doi:10.1016/j.bmcl.2009.12.086.

## Data Availability

All docking outputs are available from the author on request. Pipeline output: `dock-HP-058-2026-11-14.json` (docking done separately — the automated PDB lookup hung); kinase-domain docking: `dock-HP-058-2026-11-14-4JSX.json` (4JSX, Torin2-centred). Structure: PDB 4JSX (3.5 Å). Measured potencies: ChEMBL target CHEMBL2842, accessed 14 November 2026 (documents CHEMBL1156955, CHEMBL3638644, CHEMBL1156748, CHEMBL1800032, CHEMBL1156873). Compound structures: PubChem CID 6436034 (everolimus); ChEMBL IDs CHEMBL1091714, CHEMBL3693444, CHEMBL576090, CHEMBL1801204, CHEMBL606423.
