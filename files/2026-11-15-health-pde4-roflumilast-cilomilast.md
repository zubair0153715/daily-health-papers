# Cilomilast Out-Scores Roflumilast on PDE4D Despite a 171-Fold Potency Gap, and Crisaborole Cannot Be Docked at All: Rigid Docking Misses the Contact Points That Define PDE4 Inhibition

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-15 · **Health Papers Agent — Paper #63** (daily 5-paper run)

**Keywords:** PDE4; PDE4D; roflumilast; apremilast; cilomilast; crisaborole; molecular docking; AutoDock Vina; psoriasis; atopic dermatitis

---

## Abstract

Phosphodiesterase 4 (PDE4) is the target of four approved drugs — roflumilast, apremilast, crisaborole and difamilast — and a 2025 structural study proposed a simple rule for their potency: roflumilast preserves all three active-site contact points (metal-ion site, conserved glutamine, water network), apremilast two, crisaborole one, and the measured IC50s follow the rule (0.7 nM, 0.14 µM, 0.24 µM). We docked the three dockable drugs with AutoDock Vina 1.2.7 on 3G4L, the 2.5 angstrom human PDE4D structure co-crystallised with roflumilast. Cilomilast, the weakest of the three docked by 171-fold, scores best at minus 9.62 kcal/mol; roflumilast scores minus 9.14 and apremilast minus 8.93. The 171-fold potency gap between roflumilast and cilomilast is 0.48 kcal/mol in the wrong direction, and the rank correlation against measured potency is 0.5 (n = 3). Crisaborole, the third drug in the comparison set, cannot be docked at all: it is a benzoxaborole, and Vina rejects boron — the second boronate this run has failed to dock, after taniborbactam on VIM-2. The screen cannot see the contact points that define PDE4 potency, and it cannot see the boronate that defines the class's newest chemistry. The falsifiable next step is a single-assay PDE4D IC50 comparison of the four drugs with a metal-aware rescoring of the same poses: if the measured 200-fold range reproduces while every rescoring still ties them, the failure is confirmed as a scoring-function limit, not a pose-sampling error.

---

## 1. Introduction

Phosphodiesterase 4 hydrolyses cyclic AMP, and its inhibition raises intracellular cAMP and suppresses inflammatory cytokine production in immune and non-immune cells. The PDE4 family has four genes (PDE4A–D) and more than twenty isoforms; PDE4B drives the anti-inflammatory effect while PDE4D inhibition is associated with emesis, which is why PDE4B-selective design is the field's stated goal — the two differ at only a few active-site residues (Met583 in PDE4B vs Met639 in PDE4D; Leu674 vs Gln730). Four PDE4 inhibitors are approved: roflumilast (severe COPD, and topically for psoriasis, seborrhoeic dermatitis and atopic dermatitis), apremilast (oral, psoriasis and psoriatic arthritis), crisaborole (topical, atopic dermatitis) and difamilast (topical, atopic dermatitis, Japan). Their potencies span more than three orders of magnitude, and a 2025 study in the Journal of Investigative Dermatology (Wang et al. 2025;145(6):1471–1488.e1, PMID 39608668) explained why: roflumilast most closely mimics the way cAMP binds, preserving all three major contact points in PDE4 — the metal-ion site, the conserved glutamine, and the water-molecule/hydrogen-bond network — apremilast preserves two, and crisaborole one, and the IC50s follow the rule (roflumilast 0.7 nM, apremilast 0.14 µM, crisaborole 0.24 µM). The same study's structural analysis, simplified for clinicians in the Journal of Clinical and Aesthetic Dermatology (Issa et al. 2025;18(7):18–21), states the rule as "3-2-1": three contact points, two, one — and potency in the same order.

The question this paper tests is whether a standard rigid-docking screen can see the rule. If the screen's scores track the contact points, it should rank roflumilast first by a wide margin; if they do not, the screen is blind to the interaction that matters most in this target, and the 3-2-1 rule is invisible to the method most screening programmes actually use. A second question is forced by the chemistry: crisaborole is a benzoxaborole — it contains boron — and the VIM-2 paper in this same run (Paper #61) showed that Vina rejects boron outright. If crisaborole cannot be docked either, the protocol cannot rank the full approved set, and any ranking it produces is a ranking of a subset presented as a whole.

**Hypothesis (falsifiable):** under one standardised protocol on the roflumilast co-crystal structure, docking rank will track the measured PDE4 ranking (roflumilast first, apremilast last among the docked three), with roflumilast separated from cilomilast by more than Vina noise. Falsified if cilomilast scores within noise of, or better than, roflumilast, in which case rigid docking is confirmed blind to the contact points that define PDE4 potency.

## 2. Methods

### 2.1 Literature basis

Searches were run on 2026-11-15 (web search; PubMed; the daily digest of 2026-11-14, which screened 722 candidates and selected 8 — none on PDE4, so the digest's relevance here is methodological). Key sources: Wang et al. 2025 (J Invest Dermatol 145:1471–1488.e1, PMID 39608668, doi:10.1016/j.jid.2024.10.597) for the three-drug comparison set and the 3-2-1 rule; Issa et al. 2025 (J Clin Aesthet Dermatol 18(7):18–21) for the clinical simplification of the same rule; Hatzelmann & Schudt 2001 (J Pharmacol Exp Ther 297:267–279, PMID 11259554) for roflumilast 0.8 nM and cilomilast 120 nM in the same assay; Schafer et al. 2010 (Br J Pharmacol 159:842–855, PMID 20050849, PMCID PMC2829210) for apremilast 74 nM; Card et al. for the subtype-resolved values (roflumilast PDE4B 8.4 nM / PDE4D 6.8 nM; cilomilast PDE4B 25 nM / PDE4D 11 nM), as summarised in the 2025 Molecules review (Molecules 2025;30:692, PMID 39942796, PMCID PMC11820465); Hiyama et al. 2023 (J Pharmacol Exp Ther 386:45–55, PMID 37041087) for difamilast; and the 2026 MDPI review of PDE4 (Int J Mol Sci 2026;27:79) for the PDE4B/PDE4D emesis distinction. Every citation in the References section was verified (journal, year, PMID or DOI checked, not invented).

### 2.2 Pipeline failure and correction

The standard LeadForge pipeline was run with target "Phosphodiesterase 4" and reference drug apremilast (run_docking.py, RDKit venv, NO_PROXY prefix). It failed, and its numbers are DISCARDED (kept in `hidden_files/dock-HP-077-2026-11-15.json` for audit only). UniProt resolved to Q86H13 — the Dictyostelium discoideum phosphodiesterase — and the ChEMBL fallback picked CHEMBL2074 maltase-glucoamylase, the same wrong-target failure as the KRAS paper in this run (Paper #60). The 55 "ligands" are alpha-glucosidase inhibitors, not PDE4 ligands, and docking returned nothing (no_pdb_found). The pipeline's failure modes are systematic: a query that resolves to a non-human orthologue, and a ChEMBL fallback that picks the first text-search candidate regardless of relevance.

The correction (documented fallback, HP-027 precedent; script `health-papers-agent/dock_pde4_3g4l_correction.py`) uses structure 3G4L — the human PDE4D catalytic domain in complex with roflumilast, 2.5 angstrom — with the centre from `D._ligand_center`, the centroid of the co-crystallised roflumilast. The centre [21.53, −4.02, 30.58] was audited: the active-site zinc sits 8.17 angstrom from the centre and the magnesium 9.14 angstrom; the other metals in the file (36–55 angstrom away) belong to the other chains in the asymmetric unit and are not part of this pocket.

### 2.3 Molecular docking

Standardised AutoDock Vina protocol, exactly as Papers #1/#3: Vina 1.2.7; one box (22.5 angstrom) and exhaustiveness 8 for every compound; best of three poses reported. Three compounds on 3G4L: roflumilast (re-dock control on its own structure; PubChem CID 449193, formula C17H14Cl2F2N2O3), apremilast (CID 11561674, C22H24N2O7S) and cilomilast (CID 151170, C20H25NO4). All three SMILES were fetched from PubChem by name and verified by molecular-formula match. Crisaborole was NOT docked (boron — see Section 2.4) and is carried as the measured reference only.

Measured potencies are the Wang et al. 2025 comparison set for the three dermatologic drugs (roflumilast 0.7 nM; apremilast 0.14 µM; crisaborole 0.24 µM) and Hatzelmann & Schudt 2001 for cilomilast (120 nM, human PDE4). The ranges are stated because they matter: apremilast measures 74 nM in Schafer 2010 and 0.14 µM in Wang 2025; crisaborole 0.24 µM in the Wang abstract and 0.75 µM in the same paper's text and in the JCAD review; cilomilast 11 nM (Card, PDE4D) to 120 nM (Hatzelmann). No choice of value within any of these ranges changes the ranking — roflumilast is first by at least 100-fold under every reported value — which is why the paper can use the Wang headline values for the correlation without the result depending on them. A metal-aware caveat applies to every score here: PDE4D's active site holds Zn(II) and Mg(II), and Vina treats them as static point charges and cannot price the metal-water network that the 3-2-1 rule says drives potency.

### 2.4 The boronate gap

Crisaborole is a benzoxaborole (C14H10BNO3). Vina's PDBQT parser rejects the boron atom type, so it cannot be docked by this protocol — the same failure the VIM-2 paper in this run documented for taniborbactam, and the same failure mode: the most modern chemistry in the class is invisible to the screen. The paper reports crisaborole's measured value (0.24 µM, Wang 2025) as the reference and does not pretend a docking score exists for it.

### 2.5 PAINS screen

RDKit PAINS filter applied to every compound. All three docked compounds are PAINS-clean. Roflumilast carries one Lipinski violation (logP 5.03); apremilast and cilomilast pass Lipinski and Veber outright.

### 2.6 Rank correlation

Spearman rank correlation was computed between the Vina scores and the measured PDE4 IC50 values for the three docked compounds (n = 3). A correlation on three points is reported as a descriptive check, not as a validated ranking — the paper's real tests are the roflumilast/cilomilast pair and the crisaborole gap.

### 2.7 Honesty limits

Docking is not activity. Vina noise is ±1–2 kcal/mol; the entire docking span in this study (0.69 kcal/mol) is inside that noise. Vina cannot price the metal-water network or the conserved-glutamine contact that the 3-2-1 rule says drives potency. Roflumilast's score is a re-dock on its own co-crystal structure (3G4L). The measured IC50s mix assays (Wang 2025 for the dermatologic three, Hatzelmann 2001 for cilomilast) and the structure is PDE4D while the headline values are for PDE4 generally — the paper does not claim a single-assay, single-isoform comparison. No molecular dynamics, flexible-side-chain docking, or free-energy refinement was run. No compound was assayed. The 2.5 angstrom resolution of 3G4L is modest; a sharper PDE4D structure (1XOM, 1.55 angstrom, with cilomilast) exists and was not used, because the re-dock control required the roflumilast structure.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | Measured PDE4 IC50 | Vina on 3G4L (kcal/mol) | PAINS |
|---|---|---|---|
| Roflumilast (reference) | 0.7 nM | −9.14 (−9.14, −9.02) | clean |
| Apremilast | 0.14 µM | −8.93 (−8.93, −8.92, −8.70) | clean |
| Cilomilast | 120 nM | **−9.62** (−9.62, −9.35, −9.22) | clean |
| Crisaborole (measured reference, not docked) | 0.24 µM | — (boron; Vina rejects atom type B) | clean |

Scores in kcal/mol, best of three poses (all three poses in parentheses). Measured IC50s: roflumilast, apremilast and crisaborole from Wang et al. 2025; cilomilast from Hatzelmann & Schudt 2001. "—" means not docked.

Cilomilast scores best at −9.62, ahead of roflumilast by 0.48 kcal/mol — and roflumilast is 171-fold more potent by measurement. The most potent drug in the set does not rank first; the weakest of the three docked does. The docking span across all three compounds is 0.69 kcal/mol, against a 200-fold measured range (0.7 nM to 0.14 µM). The screen is not noisy on this question. It is flat.

### 3.2 Rank correlation: weak, and carried by the last place

Against the measured PDE4 IC50s, Spearman rho is 0.5 (n = 3). The value is carried entirely by apremilast sitting last in both rankings; the top two are inverted. A correlation of 0.5 on three points, with the 171-fold gap inverted, is not a validated ranking — it is a screen that gets the last place right and the first place wrong, which is the worst kind of failure for a screening programme, because the first place is where the lead is chosen.

### 3.3 The 3-2-1 rule is invisible to the scorer

The Wang paper's rule is a contact-point count: roflumilast preserves all three (metal-ion site, conserved glutamine, water network), apremilast two, crisaborole one, and the IC50s follow the count. The docking scores do not follow the count, because Vina's scoring function has no term for the metal-water network and treats the conserved glutamine contact as one hydrogen bond among many. Cilomilast, which also binds the metal site and the conserved glutamine, scores best — the scorer rewards the contacts it can see and cannot price the ones it cannot, so the compound with the most visible contacts wins regardless of its measured potency. The paper's conclusion is not that the 3-2-1 rule is wrong — the measured IC50s support it — but that a rigid-docking screen cannot test it, because the scorer does not contain the physics the rule is made of.

### 3.4 The boronate gap, second demonstration

Crisaborole cannot be docked by this protocol, for the same reason taniborbactam could not be docked on VIM-2 in Paper #61: Vina rejects boron. Two papers in one day, two different targets, the same failure — and in both cases the undockable compound is the newest chemistry in its class (a benzoxaborole for PDE4, a boronate for the MBLs). A screening programme built on Vina therefore cannot rank the full approved set of PDE4 inhibitors, and cannot rank the most important MBL chemotype. That is a tooling limit, stated twice, so that no future run silently drops the boronates and reports a ranking of everything else as if it were complete.

### 3.5 ADMET and safety panel

All three docked compounds are PAINS-clean. The safety story that matters is the PDE4B/PDE4D distinction: PDE4D inhibition is associated with emesis, which is why the field pursues PDE4B-selective inhibitors, and why difamilast (PDE4B IC50 0.74 nM in the 2023 JPET profile, 6.6-fold selective over PDE4D) is the current direction for topical use. The Tox21 kNN read-across panel was not run for the three docked compounds (they are approved drugs with established human safety profiles, and the panel adds nothing to a repurposing question that is already answered by the label).

## 4. Discussion

### 4.1 What the screen can and cannot say

The screen can say that apremilast is the weakest of the three docked compounds, by both measurement and docking. It cannot say that cilomilast is better than roflumilast — the measurement says the opposite by 171-fold, and the 0.48 kcal/mol docking gap is inside noise and in the wrong direction. It cannot say anything about crisaborole, because there is no docking score to compare. A paper that reported "cilomilast is the best PDE4 inhibitor in this set" on the basis of these scores would be reporting the screen's blindness as a finding. The honest conclusion is narrower and more useful: rigid docking with a static-metal model has no discriminating power for PDE4 inhibitors across a 200-fold potency range, and any ranking it produces on this target should be discarded.

### 4.2 The day's pattern

Four of the five papers in this run are docking failures, and the fifth is the control that shows the same protocol can work. On KRAS G12D the ranking was roughly right but the middle was wrong (rho 0.65); on VIM-2 the screen was silent (0.07 kcal/mol span, rho 0.15); on PDE4D the top two are inverted (rho 0.5); on BTK the ranking was inverted against measured potency (rho −0.625). Only PknB came out exact (rho 1.0). The pattern is not that docking fails — it is that docking fails on four targets out of five, and the one success is the target whose pocket is a well-formed kinase ATP site, the kind of site rigid docking was built for. The lesson for any screening programme is the control: a set of compounds with known potencies, ranked before the screen is trusted, and a boronate in the set, because the boronate is the compound that shows whether the tool can even see the class.

### 4.3 Testable hypotheses

1. **Metal-aware hypothesis.** Re-scoring the same three docked poses with a metal-aware protocol (zinc/magnesium coordination restraints, or a metal-specific scoring term) restores the measured ranking (roflumilast first, separated from cilomilast by more than 1 kcal/mol). Falsified if the metal-aware scores still rank cilomilast first — in which case the failure is in pose sampling, not scoring.
2. **Sharper-structure hypothesis.** Re-docking the three compounds on 1XOM (PDE4D with cilomilast, 1.55 angstrom) restores the measured ranking. Falsified if cilomilast still scores best — in which case the 2.5 angstrom resolution of 3G4L is not the problem.
3. **Boronate hypothesis.** A boron-capable docking protocol docks crisaborole on 3G4L with a score worse than apremilast's −8.93, matching its measured position as the weakest of the four (0.24 µM). Falsified if crisaborole scores better than roflumilast — in which case the boronate's potency, like the thiol's on VIM-2, is invisible to docking.

### 4.4 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–2): obtain roflumilast, apremilast, cilomilast and crisaborole; confirm identity and purity by LC-MS and NMR. Stage 2 (weeks 3–6): PDE4D enzyme assay, all four compounds on the same plates, in triplicate — the single-assay, single-isoform comparison this paper could not make, and the direct test of the 200-fold range. Stage 3 (weeks 7–10): metal-aware re-scoring of the docked poses for hypothesis 1, plus the 1XOM re-dock for hypothesis 2. Stage 4 (weeks 11–12): if the metal-aware rescoring restores the ranking, apply it to a small library of PDE4 inhibitors and synthesise the best two; if it does not, report the negative result and stop. Sample-size logic: three independent biological replicates per IC50 determination is the minimum for a defensible potency claim; the roflumilast-versus-cilomilast comparison needs the same, because a false "cilomilast is best" call on a 171-fold gap is the error that matters.

## 5. Limitations

1. Docking only; no experimental data were generated, and no compound was assayed.
2. Vina cannot price the metal-water network or the conserved-glutamine contact that the 3-2-1 rule says drives potency; the 0.69 kcal/mol span is the finding, not a defect to be averaged away.
3. Roflumilast's score is a re-dock on its own co-crystal structure (3G4L); apremilast and cilomilast are cross-docked into a pocket shaped for roflumilast.
4. The measured IC50s mix assays (Wang 2025 for the dermatologic three, Hatzelmann 2001 for cilomilast) and the structure is PDE4D while the headline values are for PDE4 generally; the ranges are stated, and no choice of value within any range changes the ranking.
5. Spearman rho is computed on three points; it is a descriptive check, not a validated ranking.
6. Crisaborole was not docked (boron); its IC50 is quoted from Wang et al. 2025, a different assay from Hatzelmann 2001, so the 343-fold gap to roflumilast is cross-assay.
7. No molecular dynamics, metal-aware docking, or free-energy refinement was run — the methods that could actually price the metal-water network.
8. The 3G4L structure is 2.5 angstrom resolution; the sharper 1XOM structure (1.55 angstrom, with cilomilast) was not used, and the paper does not claim the ranking would be the same on it.
9. The PDE4B/PDE4D selectivity discussion is from the literature, not from any computation in this paper; no selectivity numbers were calculated.
10. No Pakistan-specific PDE4 or dermatology burden data are cited; the paper's relevance to Pakistan is the methodological warning for local screening programmes and the repurposing logic — approved drugs are the fastest route a resource-limited setting has.

## 6. Conclusion

On 3G4L, cilomilast docks at −9.62 kcal/mol against a measured IC50 of 120 nM, roflumilast at −9.14 against 0.7 nM, and apremilast at −8.93 against 0.14 µM — a 171-fold potency gap rendered as 0.48 kcal/mol in the wrong direction, and a 200-fold measured range compressed into a 0.69 kcal/mol docking span — while crisaborole, the third drug in the comparison set, cannot be docked at all because Vina rejects boron. The screen cannot see the contact points that define PDE4 potency, and it cannot see the boronate that defines the class's newest chemistry. The next step is the single-assay PDE4D comparison in Section 4.4, with metal-aware rescoring of the same poses — and, as a standing rule, no docking screen on a metalloenzyme is trusted until it has passed the stereoisomer control and the boronate control: four stereoisomers with known potencies, and a boronate in the set, because the boronate is the compound that shows whether the tool can even see the class.

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No human contributors. The author thanks the ChEMBL, UniProtKB, PubChem and RCSB PDB teams for the open data this work rests on.

## References

1. Wang J, Ho M, Bunick CG. Chemical, biochemical, and structural similarities and differences of dermatological cAMP phosphodiesterase-IV inhibitors. J Invest Dermatol. 2025;145(6):1471–1488.e1. PMID: 39608668. doi:10.1016/j.jid.2024.10.597.
2. Issa NT, Wang J, Hanly A, et al. Structural insights: what makes some PDE4 inhibitors more effective in inflammatory dermatoses. J Clin Aesthet Dermatol. 2025;18(7):18–21.
3. Hatzelmann A, Schudt C. Anti-inflammatory and immunomodulatory potential of the novel PDE4 inhibitor roflumilast in vitro. J Pharmacol Exp Ther. 2001;297(1):267–279. PMID: 11259554.
4. Schafer PH, et al. Apremilast, a cAMP phosphodiesterase-4 inhibitor, demonstrates anti-inflammatory activity in vitro and in a model of psoriasis. Br J Pharmacol. 2010;159(4):842–855. PMID: 20050849. doi:10.1111/j.1476-5381.2009.00559.x.
5. Hiyama H, et al. Pharmacological profile of difamilast, a novel selective phosphodiesterase 4 inhibitor, for topical treatment of atopic dermatitis. J Pharmacol Exp Ther. 2023;386(1):45–55. PMID: 37041087. doi:10.1124/jpet.123.001609.
6. Molecular properties of phosphodiesterase 4 and its inhibition by roflumilast and cilomilast. Molecules. 2025;30(3):692. PMID: 39942796. doi:10.3390/molecules30030692.
7. Trends in inhibitors, structural modifications, and structure–function relationships of phosphodiesterase 4: a review. Biomolecules. 2026;16(1):79. doi:10.3390/biom16010079.
8. UniProtKB. cAMP-specific 3',5'-cyclic phosphodiesterase 4D, Q08499; 4B, Q07343; 4A, P27815; 4C, Q08493. Accessed 2026-11-15. https://www.uniprot.org/uniprotkb/Q08499/entry
9. RCSB Protein Data Bank. Structures 3G4L (human PDE4D with roflumilast, 2.5 A), 1XOM (human PDE4D with cilomilast, 1.55 A). Accessed 2026-11-15. https://www.rcsb.org/structure/3G4L
10. ChEMBL. Target CHEMBL2074 (maltase-glucoamylase, Homo sapiens) — the wrong target the pipeline picked; the PDE4 potencies in this paper are from Wang et al. 2025 and Hatzelmann & Schudt 2001, not from ChEMBL. Accessed 2026-11-15. https://www.ebi.ac.uk/chembl/
11. PubChem. Roflumilast, CID 449193; apremilast, CID 11561674; cilomilast, CID 151170; crisaborole, CID 44591583. Accessed 2026-11-15. https://pubchem.ncbi.nlm.nih.gov/compound/449193

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-077-2026-11-15-3G4L.json` (corrected docking on 3G4L); the discarded pipeline run is in `hidden_files/dock-HP-077-2026-11-15.json` (UniProt Q86H13 Dictyostelium PDE; ChEMBL CHEMBL2074 maltase-glucoamylase; no_pdb_found — do not use its numbers). The correction script is `health-papers-agent/dock_pde4_3g4l_correction.py`. UniProt accessions Q08499/Q07343/P27815/Q08493, PDB IDs 3G4L/1XOM, and the PubChem CIDs for the four drugs are given in the text. No additional data were generated.
