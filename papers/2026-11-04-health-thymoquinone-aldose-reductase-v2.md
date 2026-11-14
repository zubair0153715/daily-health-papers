# Epalrestat Outscores Thymoquinone by 1.5 kcal/mol on Aldose Reductase at the True Inhibitor Site: A Grid-Centre Audit Refutes the Docking Lead

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 4 November 2026 · **Paper #1 v2 — Health track** (Daily Research Papers; resubmission of the paper rejected by ChemRxiv on 3 November 2026)

**Keywords:** thymoquinone; aldose reductase; molecular docking; grid centre; re-docking; PAINS; *Nigella sativa*; diabetic complications

---

## Abstract

Standardised AutoDock Vina docking reported thymoquinone (TQ), the marker quinone of *Nigella sativa*, outscoring the aldose-reductase reference drug epalrestat (−7.27 vs −6.48 kcal/mol). We re-tested that lead with new computation: an exhaustiveness-16 repeat, RDKit ADMET, a grid-centre audit of all five screened targets, and re-docking validation against the crystallographic inhibitor. The exhaustiveness-16 repeat confirmed the lead in the original box (TQ −7.25 vs epalrestat −6.47 kcal/mol), but the audit showed the aldose-reductase grid was centred on the NADP+ cofactor centroid, 13.26 Å from the co-crystallised inhibitor IDD594, with the crystal pose mostly outside the 22.5 Å box. Re-docking the inhibitor at that centre failed (RMSD 17.0 Å; 16.4 Å after correcting the atom mapping). Re-centring on the inhibitor centroid, re-docking passed (RMSD 1.16 Å, no superposition; 1.29 Å Kabsch-aligned; ≤2 Å criterion), and at the true inhibitor site epalrestat outscores TQ by 1.45 kcal/mol at exhaustiveness 8 (−9.08 vs −7.63) and 1.56 kcal/mol at exhaustiveness 16 (−9.22 vs −7.65). The docking lead is therefore refuted, not confirmed. The audit found the same centre error in two more targets: the DPP-4 grid was a glycan sugar 45.24 Å from the inhibitor (corrected re-dock: TQ −6.88 vs sitagliptin −9.05), and the PTP1B and α-amylase rows are withdrawn — 9C66 is a MENA EVH1-domain structure with no PTP1B catalytic domain, and 5U3A is an apo structure centred on an N-terminal residue. Only the PPAR-γ centre was correct (TQ −6.47 vs pioglitazone −8.98). TQ is Lipinski-clean (MW 164.2, logP 1.67, 0 violations) but remains PAINS-positive (quinone_A(370)). The falsifiable next step is an in-vitro aldose-reductase assay with the corrected expectation — TQ does not outscore epalrestat at the true site — plus HPLC standardisation of Pakistani-market kalonji oils, where TQ content varies ~260-fold.

---

## 1. Introduction

Pakistan carries one of the world's heaviest diabetes burdens: roughly 34.5 million adults live with diabetes, a prevalence near 30.8%, with an estimated 9.3 million cases undiagnosed. Diabetic complications — neuropathy, retinopathy, nephropathy and cataract — rather than hyperglycaemia itself, account for most of the morbidity.

*Nigella sativa* (kalonji, black seed) is among the most widely used traditional adjuncts for diabetes in Pakistan. Its marker compound thymoquinone (2-isopropyl-5-methyl-1,4-benzoquinone; TQ) has reported antioxidant and anti-inflammatory activity, and a substantial in-vitro literature claims activity against a striking range of targets. Yet the clinical literature is contradictory: meta-analyses of randomised trials report only a modest HbA1c reduction of ~−0.54%, with very high heterogeneity (I² 94–99%) and low certainty. Two under-examined confounders may explain the contradiction. First, product quality: a Swiss HPLC screening of commercial *N. sativa* products found TQ content ranging from 3.08 to 809.4 mg/100 g — a ~260-fold range — and a Malaysian survey found 0.07–1.88% TQ; most trials neither standardised nor even assayed TQ content. Second, chemistry: TQ is a quinone, a classic PAINS scaffold whose redox-cycling and Michael-acceptor reactivity can produce apparent activity against many targets in vitro without specific pharmacology.

Our first version of this paper (submitted to ChemRxiv, rejected 3 November 2026 as a proposed framework without new research data) reported a standardised computational screen of TQ against five diabetes-related targets and found one lead: TQ outscored epalrestat on aldose reductase (AR), the rate-limiting enzyme of the polyol pathway. This revision presents the new research data ChemRxiv asked for — an exhaustiveness-16 repeat, a full ADMET profile, interaction analysis, and, decisively, a grid-centre audit with re-docking validation — and the new data overturn the lead. The paper's result is now a correction, not a claim: at the crystallographic inhibitor site, epalrestat beats TQ by ~1.5 kcal/mol, and two of the five screen rows were never valid at all. We report the correction in full because a docking pipeline that can silently centre its grid on a cofactor, a glycan, or a protein's own N-terminus will produce confident-looking numbers for the wrong pocket — and the only defence is to audit the centre and re-dock the crystal ligand.

## 2. Methods

### 2.1 Molecular docking

Docking used AutoDock Vina 1.2.7 with the LeadForge pipeline protocol: for each target, TQ and the reference drug were docked into the same binding site with the same protocol (same PDB structure, same grid centre, same exhaustiveness, box 22.5 Å, 3 poses per ligand). Structures were retrieved from the RCSB Protein Data Bank. Affinities are reported as the best of three poses (kcal/mol); all three poses are reported in the tables. Vina's scoring noise is approximately ±1–2 kcal/mol; differences smaller than this cannot be treated as significant on scores alone. The original screen (20 October 2026) used exhaustiveness 8; this revision repeats the aldose-reductase comparison at exhaustiveness 16 with the identical centre, box and receptor.

### 2.2 ADMET and PAINS screen

TQ was profiled with RDKit 2026.03.6 (Crippen logP, TPSA, Lipinski and Veber drug-likeness) and screened with the RDKit FilterCatalog PAINS set (Baell & Holloway, 2010); matching filter names are reported verbatim.

### 2.3 Grid-centre audit

For each screened target, the recorded grid centre was compared against the centroids of every non-water HETATM group in the PDB file, in file order, and against the centroid of the co-crystallised inhibitor where one exists. The audit reproduces the centre-selection logic of the docking pipeline (`dock.py _ligand_center`), which picks the first non-junk HETATM group in file order; the junk list excludes waters, ions and cryo additives but not glycans, modified protein residues, or cofactors. A centre was judged correct only if it coincided with the co-crystallised inhibitor's centroid.

### 2.4 Re-docking validation

The co-crystallised AR inhibitor IDD594 (residue LDT, chain A, seqnum 320; 24 heavy atoms) was re-docked into 1US0 at the original centre and at the corrected centre (the crystal LDT centroid), exhaustiveness 8, 3 poses. The ligand SMILES were derived from the RCSB CCD entry for LDT and verified against the CCD formula (C16H12BrF2NO3S) and element sequence. RMSD was computed on heavy atoms only, in the common receptor frame with no superposition as the primary metric, with Kabsch-aligned RMSD also reported. The standard success criterion is RMSD ≤2 Å for the best pose. Atom correspondence was established by graph isomorphism, with the substructure-match tuple inverted on both sides (a mapping error in the first calculation was caught by an element-consistency check and corrected; the corrected-mapping values are reported here).

### 2.5 Interaction analysis

Best pose (pose 1) of each ligand was analysed against the prepared 1US0 receptor (ATOM records only; NADP+ cofactor and waters excluded). Hydrogen bonds are geometric candidates only: donor–acceptor distance ≤3.5 Å, no angle criterion (PDBQT carries no angle information). Close contacts are any ligand heavy atom to any receptor heavy atom ≤4.0 Å. Contacts are reported as observed contacts in the docked poses, not as established binding modes.

### 2.6 Honesty limits

This is a computational study. No wet-lab data are presented. No clinical claim is made. Docking affinity is not enzyme inhibition, and a docking score is not evidence of efficacy. Where a result is withdrawn in this revision, the withdrawal is stated in the Results, not hidden.

## 3. Results

### 3.1 The exhaustiveness-16 repeat confirms the lead — in the original box

| Ligand | Exhaustiveness 8, original (20 Oct 2026) | Exhaustiveness 8, v2 rerun | Exhaustiveness 16, v2 |
|---|---|---|---|
| Thymoquinone | −7.27 / −7.24 / −7.15 | −7.269 / −7.211 / −7.063 | **−7.245** / −7.204 / −7.078 |
| Epalrestat (ref) | −6.48 / −6.38 / −5.98 | −6.753 / −6.736 / −5.916 | **−6.474** / −6.084 / −5.899 |
| Margin (TQ − epalrestat, best) | −0.79 | −0.52 | −0.77 |

At higher exhaustiveness the lead survived with the same direction and a similar margin (−0.77 kcal/mol). Every TQ pose still beat every epalrestat pose. The margin remains inside Vina's ±1–2 kcal/mol noise, so even in the original box this was a lead, not a confirmed win. The repeat rules out a sampling artefact; it does not rule out a site artefact — which is what the audit then found.

### 3.2 The grid centre was the NADP+ cofactor, not the inhibitor site

| Item | Value |
|---|---|
| Grid centre used (original protocol) | [21.26, −6.13, 27.39] |
| NADP+ cofactor (NDP) centroid | [21.26, −6.13, 27.39] — identical |
| Co-crystallised inhibitor IDD594 (LDT) centroid | [16.47, −7.21, 15.08] |
| Distance, grid centre to inhibitor centroid | 13.26 Å |
| Crystal inhibitor pose, z-range | 9.7–19.0 Å; box z-range 16.14–38.64 Å — pose mostly outside the box |

The centre-selection code picks the first non-junk HETATM group in file order. In 1US0 that group is NDP, the NADP+ cofactor — not the inhibitor LDT. The crystal inhibitor pose sits ~13 Å away, mostly outside the 22.5 Å box. Every TQ and epalrestat pose in the original screen was therefore docked into a cofactor-centred box, not the crystallographic inhibitor site. The receptor preparation compounds the problem: it keeps ATOM records only, so NADP+ is excluded from the receptor even though the AR inhibitor pocket is NADP+-adjacent in the crystal — docked poses may occupy space the cofactor would clash with in reality.

### 3.3 Re-docking fails at the original centre and passes at the corrected centre

| Centre | Re-docked ligand | Best-pose affinity (kcal/mol) | RMSD, no superposition (Å) | RMSD, Kabsch-aligned (Å) | Verdict (≤2 Å) |
|---|---|---|---|---|---|
| Original [21.26, −6.13, 27.39] | IDD594 (LDT) | −7.943 | 17.00 (16.42 after mapping correction) | 5.02 (3.89) | FAIL |
| Corrected [16.47, −7.21, 15.08] | IDD594 (LDT) | −9.192 | **1.16** | 1.29 | PASS |

At the original centre the re-docked inhibitor lands ~15 Å from its crystal pose (bromine atom: crystal (14.88, −3.75, 9.69) vs docked pose 1 (19.13, −4.58, 24.37)). At the corrected centre — the crystal LDT centroid — the best pose reproduces the crystallographic binding mode within 1.16 Å. The protocol is therefore validated at the corrected centre and unvalidated at the original one. The RMSD failure is a protocol-centre artefact, not a failure of Vina itself.

### 3.4 At the true inhibitor site, epalrestat beats thymoquinone by ~1.5 kcal/mol

| Ligand | Exhaustiveness 8, corrected centre | Exhaustiveness 16, corrected centre |
|---|---|---|
| Thymoquinone | −7.626 / −7.044 / −6.621 | −7.652 / −7.054 / −6.935 |
| Epalrestat (ref) | **−9.080** / −8.679 / −8.576 | **−9.215** / −9.176 / −8.560 |
| Margin (TQ − epalrestat, best) | +1.45 | +1.56 |

The margin flips sign and exceeds the noise band at both exhaustiveness levels: epalrestat outscores TQ by 1.45 kcal/mol at exhaustiveness 8 and 1.56 kcal/mol at exhaustiveness 16. The v1 lead does not survive re-centring. TQ's corrected-centre score (−7.63/−7.65) is close to its original-box score (−7.27/−7.25); what changed is epalrestat, which scores −9.08/−9.22 at the true site against −6.48/−6.47 in the cofactor-centred box. The original comparison flattered TQ by docking the reference drug into the wrong pocket.

### 3.5 Audit of the other four targets: one correct, one corrected, two withdrawn

| Target | PDB | Recorded centre was | Distance to inhibitor | Corrected-centre result | Status |
|---|---|---|---|---|---|
| DPP-4 | 4A5S | NAG C 1, a glycan sugar | 45.24 Å | TQ −6.884 / −6.283 / −6.145; sitagliptin −9.049 / −8.794 / −8.749 | Corrected; TQ still loses (by 2.17 kcal/mol) |
| PPAR-γ | 9F7W | Co-crystallised ligand 2OH (bisphenol A) | 0.29 Å | Not re-docked; centre correct | Stands: TQ −6.47 vs pioglitazone −8.98 |
| PTP1B | 9C66 | CSO A 7, a modified cysteine of MENA EVH1 | — | Not possible | **Withdrawn** — 9C66 is a MENA EVH1-domain structure, not a PTP1B catalytic domain; it contains no PTP1B inhibitor site |
| Pancreatic α-amylase | 5U3A | PCA A 1, the protein's N-terminal pyroglutamic acid | — | Not possible | **Withdrawn** — 5U3A is an apo structure with no inhibitor; the centre was the protein's own N-terminus |

Three of the five original centres were wrong, and the root cause is the same in each case: the centre picker takes the first non-junk HETATM group, and the junk list does not cover glycans (NAG), modified protein residues (CSO, PCA), or cofactors (NDP). The DPP-4 correction strengthens the v1 conclusion for that target (TQ loses by more, 2.17 kcal/mol, at the true site). The PPAR-γ result stands because its centre was the co-crystallised ligand. The PTP1B and α-amylase rows are withdrawn outright: no valid docking comparison existed for those targets in this study, and no corrected re-dock is possible in those PDB entries.

### 3.6 ADMET: Lipinski-clean, PAINS-positive

| Property | Thymoquinone |
|---|---|
| Formula / MW | C10H12O2 / 164.2 (exact 164.0837) |
| logP (Crippen) | 1.67 |
| H-bond donors / acceptors | 0 / 2 |
| TPSA | 34.14 Å² |
| Rotatable bonds | 1 |
| Lipinski violations / Veber | 0 / pass |
| PAINS | **Positive — quinone_A(370)**, 1 matching filter |

TQ passes Lipinski and Veber with zero violations, which is why it looks like a clean lead on paper. The PAINS alert is the counterweight: as a quinone, TQ redox-cycles and can react with proteins as a Michael acceptor, which predicts exactly the published picture of apparent activity against many unrelated targets in vitro. Any in-vitro "hit" for TQ must be treated as guilty until proven innocent, with redox controls in the assay design.

### 3.7 Interactions at the corrected centre (observed contacts only)

| Ligand | H-bonds ≤3.5 Å (geometric candidates) | Close-contact residues ≤4.0 Å (n) |
|---|---|---|
| Thymoquinone | 1 — ALA299:N, 3.42 Å | 10 — ALA299, PHE115, TRP111, LEU300, PHE122, CYS303, TRP79, TYR309, CYS80, CYS298 |
| Epalrestat | 2 — TRP20:NE1, 3.43 Å and 3.04 Å | 10 — TRP20, TRP111, PHE122, CYS303, THR113, PHE115, TYR309, LEU300, TRP79, TRP219 |
| Shared | — | 7 — CYS303, LEU300, PHE115, PHE122, TRP111, TRP79, TYR309 |

At the true site, neither ligand contacts the classic catalytic residues TYR48 or HIS110; both sit in the specificity-pocket region (LEU300, CYS303, PHE122, TRP111). These are observed contacts in the docked poses, not established binding modes — the poses are validated only in the sense that the re-docked crystal ligand reproduces its pose (RMSD 1.16 Å); no per-ligand pose validation exists. For the record, the original-box interaction analysis gave TQ 2 H-bonds (LYS77:NZ 3.37 Å, SER210:N 3.31 Å) and epalrestat 0 H-bonds, with 5 shared contact residues (CYS298, GLN183, TRP20, TYR209, TYR48) — those contacts describe the cofactor-centred box and are superseded by the corrected-centre analysis above.

### 3.8 The standardisation problem survives the correction

Commercial TQ content varies ~260-fold (3.08–809.4 mg/100 g; Malaysian survey 0.07–1.88%). Two capsules labelled identically can therefore deliver pharmacologically trivial or substantial TQ. No published study has characterised TQ content in Pakistani-market kalonji oils. This finding is independent of the docking correction: whatever TQ does or does not do at aldose reductase, any trial that does not assay TQ content is, in effect, testing an unknown dose.

## 4. Discussion

### 4.1 The lead was a centre artefact

The exhaustiveness-16 repeat shows the original result was reproducible; the audit shows it was reproducibly wrong. A docking score is a statement about a specific box, and the box was centred on the NADP+ cofactor. The reference drug suffered more from the mis-centring than TQ did, which is why the comparison flipped. The lesson is narrow and general at once: reproducibility across exhaustiveness does not validate a docking comparison — only a centre audit and a re-docking test do. Any pipeline that selects its grid centre automatically from HETATM order should audit the centre against the co-crystallised ligand before any score is believed.

### 4.2 Two screen rows were never valid

The PTP1B and α-amylase withdrawals are the more serious finding. 9C66 is not a PTP1B structure at all — it is the MENA EVH1 domain bound to a polyproline segment of PTP1B — and 5U3A is an apo amylase with no inhibitor to centre on. Docking a ligand into those entries and reporting the numbers as target comparisons was an error, and this revision withdraws both rows rather than re-interpreting them. The DPP-4 correction shows the constructive side of the same audit: at the true site TQ loses by more (2.17 kcal/mol), so the v1 conclusion for DPP-4 is strengthened, not weakened.

### 4.3 What survives

Three things survive the correction. First, the standardisation problem: the ~260-fold market variance in TQ content is a real, literature-backed confounder for every black-seed trial, and characterising Pakistani-market oils by HPLC remains a publishable Pharm-D-level finding on its own. Second, the PAINS constraint: TQ's quinone alert means any future assay must include redox and detergent controls, and an effect that vanishes under those controls is an artefact worth reporting. Third, the assay question itself, reframed: the enzyme assay no longer tests whether TQ beats epalrestat — it tests whether TQ inhibits aldose reductase at all at a plausible concentration, with epalrestat as the positive control and the corrected docking as the (negative) prior.

### 4.4 Why this paper is worth publishing as a correction

A negative result that overturns the author's own lead, with the mechanism of the error identified and the corrected numbers reported, is more useful than the original claim would have been. The centre-selection bug — first non-junk HETATM group, with glycans, modified residues and cofactors not treated as junk — is a failure mode any automated docking pipeline can hit, and the audit procedure in §2.3 is cheap enough to run on every structure before docking begins.

## 5. Future work

One short programme, in order: (1) HPLC standardisation of ten Pakistani-market kalonji oils against a TQ reference standard, reporting the range and the fraction below any plausible active threshold; (2) an in-vitro aldose-reductase inhibition assay (IC50) of the standardised samples plus a TQ reference standard, with epalrestat as the positive control, replicates, and redox controls (catalase, DTT) — confirmation is reproducible inhibition in a plausible range surviving redox controls, refutation is no inhibition or an effect abolished by redox controls; (3) re-docking of TQ and epalrestat with the NADP+ cofactor retained in the receptor, to test whether the corrected-centre margin survives a cofactor-aware preparation. No clinical claim and no trial design follow from this paper.

## 6. Limitations

1. Docking only; no experimental data. 2. The corrected-centre margin (1.45–1.56 kcal/mol) is at the edge of Vina's ±1–2 kcal/mol noise; it is a reversal of direction, not a precise potency estimate. 3. The receptor preparation excludes NADP+ and waters, so corrected-centre poses may occupy space the cofactor would clash with in reality; a cofactor-aware re-dock is the required check (§5). 4. The re-docking validation covers 1US0 only; the DPP-4 corrected re-dock was run without a crystal-ligand re-dock of N7F, so its poses are unvalidated. 5. The PTP1B and α-amylase targets were not re-screened against valid structures in this revision; their rows are withdrawn, not replaced. 6. The literature synthesis rests on the 36-source review of 20 October 2026 and inherits its limits, including the low certainty of the clinical meta-analyses. 7. No Pakistani-market TQ data exist yet — the HPLC step is itself an untested premise.

## 7. Conclusion

New computation overturns our own lead. Thymoquinone does not outscore epalrestat on aldose reductase: at the crystallographic inhibitor site, validated by a re-dock that reproduces the crystal pose within 1.16 Å, epalrestat wins by 1.45–1.56 kcal/mol. The original lead was an artefact of a grid centred on the NADP+ cofactor, and the same audit withdrew two further screen rows and corrected a third. What remains is a cleaner question — does standardised TQ inhibit aldose reductase at all? — and a cheaper defence for every docking pipeline: audit the centre, re-dock the crystal ligand, and only then believe the score.

---

## Acknowledgments

**AI assistance:** This manuscript was drafted with the assistance of an AI research assistant (Lapis, Meta Muse Spark), which also performed the literature searches and docking computations. The author takes responsibility for the content.

## References

1. Screening of thymoquinone content in commercial *Nigella sativa* products (TQ 3.08–809.4 mg/100 g). ResearchGate. https://www.researchgate.net/publication/362959334_Screening_of_Thymoquinone_Content_in_Commercial_Nigella_sativa_Products_to_Identify_a_Promising_and_Safe_Study_Medication
2. *Nigella sativa* safety, CYP interactions and regulatory status. PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC10886913/
3. *Nigella sativa* and thymoquinone: nutrition, bioactivity and safety review. *Frontiers in Nutrition* 2023;10:1126272. https://www.frontiersin.org/articles/10.3389/fnut.2023.1126272/full
4. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. *J Chem Inf Model.* 2021;61(8):3891–3898.
5. Baell JB, Holloway GA. New substructure filters for removal of pan assay interference compounds (PAINS) from screening libraries and for their exclusion in bioassays. *J Med Chem.* 2010;53(7):2719–2740.
6. RCSB Protein Data Bank entries 1US0 (aldose reductase), 4A5S (DPP-4), 9F7W (PPAR-γ), 9C66 (MENA EVH1 domain), 5U3A (pancreatic α-amylase, apo). https://www.rcsb.org/
7. Ali Z, et al. Black Seed (Kalonji): Hadith, Frequency Healing — systematic review of 36 sources. Internal report, 20 October 2026. (Clinical HbA1c and heterogeneity figures; market-variance synthesis.)
8. Ali Z. Diabetes in Pakistan: situation and solutions. Internal report, 26 October 2026. (Pakistan diabetes burden figures.)
9. Ali Z. Thymoquinone as a Putative Aldose Reductase Inhibitor for Diabetic Complications (Paper #1 v1, 2 November 2026). Internal manuscript, superseded by this revision. (Original screen; withdrawn PTP1B and α-amylase rows.)

## Data availability

New computational data for this revision: `~/workspace/black-seed-project/v2_admet_tq.json` (RDKit ADMET + PAINS), `v2_exhaust16_ar.json` (exhaustiveness-16 repeat), `v2_redock_1us0.json` (re-docking validation, original centre, with grid-centre audit), `v2_interactions_1us0.json` (interaction analysis, original centre), `v2c_ar_docking.json` (corrected-centre docking, exhaustiveness 8 and 16), `v2c_redock_1us0.json` (re-docking validation, corrected centre), `v2c_interactions_1us0.json` (interaction analysis, corrected centre), `v2c_centre_audit.json` (grid-centre audit of DPP-4, PPAR-γ, PTP1B and α-amylase, with corrected-centre DPP-4 re-dock). Pose files: `v2_pose_tq_1us0.pdbqt`, `v2_pose_epalrestat_1us0.pdbqt`, `v2c_pose_tq_1us0.pdbqt`, `v2c_pose_epalrestat_1us0.pdbqt`, `v2c_pose_tq_4a5s.pdbqt`, `v2c_pose_sitagliptin_4a5s.pdbqt`, `v2_redock_lig_ldt.pdbqt`, `v2_redock_out_ldt.pdbqt`, `v2c_redock_lig_ldt.pdbqt`, `v2c_redock_out_ldt.pdbqt`. Original screen: `~/workspace/black-seed-project/dock_results.json`, `dock_results2.json` (AutoDock Vina 1.2.7, 20 Oct 2026). AutoDock Vina 1.2.7 throughout. This revision presents new computational data (listed above); no wet-lab data are included.
