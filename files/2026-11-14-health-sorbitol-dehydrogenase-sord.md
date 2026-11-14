# Sorbitol Dehydrogenase Inhibitors Show No Rank Correlation on Three Docking Centres — and SORD Inhibition Already Failed to Help Diabetic Nerves in Rats

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification.**

**Author:** Zubair Ali, Pharm-D student, Faculty of Pharmacy, SMBBMU, Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 14 November 2026
**Topic ID:** HP-054

## Abstract

Sorbitol dehydrogenase (SORD) catalyses the second step of the polyol pathway, oxidising sorbitol to fructose. Its inhibitors were developed as a treatment for diabetic neuropathy, on the logic that blocking fructose formation should help. We benchmarked rigid AutoDock Vina docking against measured human SORD inhibition data for five Pfizer piperazino-pyrimidine sorbitol dehydrogenase inhibitors (SDIs), including the reference compound CP-166572. Three human SORD structures exist in the Protein Data Bank. The pipeline picked 1PL8 — the highest-resolution structure — but 1PL8 is an NAD+ complex with no inhibitor, and its automatic centre fell on the NAD+ cofactor centroid, 11.62 Å from the catalytic Zn2+. We ran two corrected dockings: one centred on the catalytic Zn2+ of 1PL8, and one on 1PL6, the inhibitor-bound structure, whose co-crystallised ligand is CP-166572 itself. On the NAD+ centre the most potent measured inhibitor — CHEMBL90344, IC50 27 nM — scored worst (−6.61 kcal/mol), and the rank correlation against measured potency was Spearman ρ = −0.2 (n = 4). On the Zn2+ centre all five compounds fell inside a single 0.79 kcal/mol band and ρ = +0.2. On the correct, inhibitor-bound structure the correlation was ρ = +0.35, and the re-dock control failed outright: CP-166572, re-docked into its own crystal structure, scored weakest of the five (−6.20 kcal/mol). No centre ranks the compounds. The result is consistent with the published animal record: in streptozotocin-diabetic rats the SORD inhibitor WAY-135706 lowered fructose but corrected neither nerve conduction velocity nor endoneurial blood flow, while an aldose reductase inhibitor corrected both; and biallelic loss-of-function SORD mutations cause hereditary motor neuropathy in humans, meaning pharmacological SORD inhibition mimics a disease-causing state. SORD is a weak target for diabetic neuropathy, and rigid docking without a metal-aware model cannot rank its inhibitors.

**Keywords:** sorbitol dehydrogenase; SORD; polyol pathway; diabetic neuropathy; molecular docking; AutoDock Vina; CP-166572; Pakistan

## Introduction

Pakistan carries the world's highest national diabetes prevalence: one in four adults (26.7%; 30.8% age-adjusted) — 33 million people — lived with diabetes in 2021, with an estimated 400,000 diabetes deaths that year and 26.9% of cases undiagnosed (IDF Diabetes Atlas, 10th edition, 2021). Diabetic neuropathy is one of the most common complications, and it has no disease-modifying treatment. The polyol pathway is the classic biochemical explanation for it: under hyperglycaemia, aldose reductase (AR) reduces glucose to sorbitol, consuming NADPH, and sorbitol dehydrogenase (SORD) then oxidises sorbitol to fructose, consuming NAD+. Tissues that lack SORD — retina, kidney, Schwann cells — accumulate sorbitol, and the pathway has been blamed for osmotic and oxidative nerve injury.

Two earlier papers in this series covered the first step of the pathway: aldose reductase, where the inhibitor epalrestat is approved in Japan and where docking could at least separate strong from weak inhibitors. This paper covers the second step, SORD, which was proposed as an independent target: if sorbitol is the problem, blocking its conversion to fructose should not help — but the original hypothesis was the reverse, that fructose formation and the NADH/NAD+ shift drive injury, so blocking SORD should help. Pfizer developed a series of piperazino-pyrimidine SDIs in 1998–2002, culminating in orally active compounds that normalised sciatic-nerve fructose in diabetic rats. No SDI ever reached the clinic. This paper asks two questions: (1) can rigid docking rank known SORD inhibitors at all, and (2) does the published evidence support SORD as a target for diabetic neuropathy?

## Methods

### 2.1 Target and compound selection

Human sorbitol dehydrogenase (UniProt Q00796) was resolved to ChEMBL target CHEMBL2275 (57 known ligands). The reference compound was CP-166572 (PubChem CID 132302; 2-hydroxymethyl-4-[4-(N,N-dimethylaminosulfonyl)-1-piperazino]pyrimidine; C11H19N5O3S), a Pfizer-series SDI. No ChEMBL SORD IC50 is recorded for CP-166572, so it serves as a structural reference only. The pipeline ranked 26 leads by measured potency and docked the top five. All five are PAINS-clean.

### 2.2 Structures and the centre problem

Three human SORD structures exist in the Protein Data Bank, all from Pauly et al. (*Structure* 2003;11(9):1071–1085; PMID 12962626): **1PL6** (2.00 Å, "Human SDH/NADH/inhibitor complex"), **1PL7** (2.20 Å, apo) and **1PL8** (1.90 Å, "human SDH/NAD+ complex"). The pipeline picked 1PL8 — the highest-resolution structure — but 1PL8 contains no inhibitor, only NAD+, Zn2+ and waters. Its automatic centre therefore fell on the NAD+ cofactor centroid, [97.83, 30.36, 26.67] — 11.62 Å from the catalytic Zn2+ of chain A, [94.58, 35.23, 36.71], with the nicotinamide ring sitting within 8 Å of the metal. The substrate pocket sits at the edge of a 22.5 Å box centred there.

The structurally correct choice is 1PL6. Its co-crystallised ligand, HETATM 572, is 4-[2-(hydroxymethyl)pyrimidin-4-yl]-N,N-dimethylpiperazine-1-sulfonamide, formula C11H19N5O3S — **CP-166572 itself**, bound in the substrate pocket 6.28 Å from the catalytic Zn2+ (chain-A 572 centroid [102.75, 37.00, 35.25]; Zn-A [96.63, 36.11, 36.32]). The pipeline chose by resolution and missed the inhibitor-bound structure. We therefore ran three dockings, all AutoDock Vina 1.2.7, exhaustiveness 8, box 22.5 Å: (i) the pipeline's automatic run on 1PL8 centred on the NAD+ centroid; (ii) a corrected run on 1PL8 centred on the catalytic Zn2+; (iii) a corrected run on 1PL6 centred on the co-crystallised CP-166572 centroid — in which the CP-166572 dock is a re-dock control against its own crystal pose.

### 2.3 Limitations of the docking model, stated in advance

The receptor preparation drops HETATM records, so the catalytic Zn2+ is **not present** in the docked receptor in any of the three runs: no metal coordination is modelled, and scores reflect only the shape and electrostatics of the apo pocket — even on 1PL6, where the metal sits 6.28 Å from the ligand. This is the same limitation reported for the urease paper in this series ("dock weakly without Ni2+"). SORD is a zinc-dependent dehydrogenase; any inhibitor that coordinates the metal will be scored wrongly. Rigid docking carries a documented ±1–2 kcal/mol noise band, and the rank correlation below uses only four compounds with measured values.

### 2.4 Literature

Measured potencies and source documents were taken from ChEMBL (accessed 14 November 2026) and verified against the original papers. The Cameron et al. (1997) head-to-head rat study and the Cortese et al. (2020) human genetics study were read in full. Diabetes burden figures are from the IDF Diabetes Atlas, 10th edition (2021). Structure identities and ligand 572 were verified by direct parse of the 1PL6 PDB file (HETNAM/FORMUL records) and the RCSB entry records for 1PL6, 1PL7 and 1PL8.

## Results

### 3.1 The compounds

The five docked compounds are all Pfizer piperazino-pyrimidines (Table 1). CHEMBL90344 (27 nM) is the stereochemically defined form of Mylari et al.'s enantiomeric SDI 6; CHEMBL91846 (173 nM) is the same scaffold with stereochemistry unspecified — a 6.4-fold measured difference between the two forms, equivalent to ~1.1 kcal/mol at 298 K, inside Vina's noise band. CHEMBL151268 (93 nM) and CHEMBL423753 (140 nM) are regioisomers from Chu-Moyer et al. (2002), differing only in methyl placement on the pyrimidine ring. Two of the four measured values were confirmed in a second assay at higher values (CHEMBL151268: 350 nM; CHEMBL423753: 480 nM); the lower value was used, which favours the docking comparison.

**Table 1. Docked SORD inhibitors: measured potency and Vina scores on three centres.**

| Compound | Measured IC50 (nM) | Source | 1PL8 NAD+ centre | 1PL8 Zn2+ centre | 1PL6 inhibitor centre |
|---|---|---|---|---|---|
| CHEMBL90344 | 27 | Mylari et al. 2001 | −6.61 | −6.48 | −6.54 |
| CHEMBL151268 | 93 | Chu-Moyer et al. 2002 | −8.22 | −6.78 | −6.95 |
| CHEMBL423753 | 140 | Chu-Moyer et al. 2002 | −7.92 | −7.04 | −6.95 |
| CHEMBL91846 | 173 | Mylari et al. 2001 | −6.95 | −6.43 | −6.37 |
| CP-166572 (QUERY) | not recorded | Pfizer series | −6.99 | −6.25 | −6.20 |

### 3.2 NAD+ centre (1PL8, pipeline auto-pick): the most potent inhibitor scores worst

On the pipeline's automatic (NAD+ cofactor) centre, CHEMBL151268 scored best (−8.22 kcal/mol) and CHEMBL90344 — the most potent measured inhibitor at 27 nM — scored worst (−6.61 kcal/mol). The rank correlation against measured potency was Spearman ρ = −0.2 (n = 4): negative. The best score is also the least trustworthy: CHEMBL151268's third pose on this centre was **+38.31 kcal/mol**, a clash artefact, showing that the NAD+ pocket produces unstable poses. Scores on this centre were systematically stronger (best −8.22) than on the Zn2+ centre (best −7.04), by ~1.2 kcal/mol — the cofactor site gives spuriously favourable scores for compounds that do not belong there.

### 3.3 Zn2+ centre (1PL8, corrected): all five compounds inside one noise band

On the corrected Zn2+ centre, the spread collapsed: all five compounds scored between −6.25 and −7.04 kcal/mol, a 0.79 kcal/mol range — less than half of Vina's noise band. The 27 nM compound ranked third (−6.48); the 140 nM regioisomer ranked first (−7.04); the reference CP-166572 ranked last (−6.25). Spearman ρ = +0.2 (n = 4). Correcting the centre moved the correlation from −0.2 to +0.2, i.e. from nothing to nothing. The two regioisomers (93 vs 140 nM measured) separated in the wrong direction: the weaker compound scored better (−7.04 vs −6.78).

### 3.4 Inhibitor centre (1PL6, corrected): the re-dock control fails

On the correct structure — 1PL6, with CP-166572 co-crystallised in the pocket — the five compounds again fell inside a single 0.75 kcal/mol band (−6.20 to −6.95 kcal/mol), and Spearman ρ = +0.35 (n = 4): still essentially zero. Poses were stable this time (CHEMBL151268's three poses: −6.95, −6.90, −6.87), so the failure is not pose instability. The decisive result is the re-dock control: **CP-166572, re-docked into its own crystal structure, scored −6.20 kcal/mol — the weakest of the five compounds.** A method that cannot recognise the native ligand as the best binder in its own pocket cannot be trusted to rank analogues. The two regioisomers tied at −6.95, which is acceptable (93 vs 140 nM is a 1.5-fold difference), but the 27 nM compound ranked third again (−6.54).

### 3.5 The target's own record

The docking failure is not the interesting finding; the target's record is. Cameron et al. (1997) ran the decisive head-to-head in streptozotocin-diabetic rats: the SORD inhibitor WAY-135706 (250 mg/kg/day) versus the aldose reductase inhibitor WAY-121509 (10 mg/kg/day). WAY-135706 did what an SORD inhibitor should do biochemically — it raised sorbitol further (1.6–8.2-fold) and lowered fructose — and it did nothing that mattered functionally: motor nerve conduction velocity (−20.2% deficit) and sensory conduction velocity (−13.9%) were uncorrected, and endoneurial blood flow (−48.6% deficit) was uncorrected. The AR inhibitor corrected both. The authors' conclusion was explicit: the first step of the polyol pathway matters far more than the second for diabetic neuropathy.

The genetics then made it worse. Cortese et al. (2020) showed that biallelic loss-of-function SORD mutations are the most frequent cause of recessive hereditary motor neuropathy: 45 affected individuals from 38 families, carrying (most commonly) c.757delG (p.Ala253GlnfsTer27), with complete loss of SORD protein and raised intracellular sorbitol. SORD loss in *Drosophila* caused synaptic degeneration and motor impairment. The treatment that worked in that model was not more SORD inhibition — it was aldose reductase inhibition, reducing sorbitol influx. Pharmacological SORD inhibition mimics a disease-causing state.

Against that, the SDI programme's best results were real but narrow: Mylari et al. (2001) reported an enantiomeric SDI at least ten times more potent than their weak starting lead, with potent inhibition of SDH in diabetic rat sciatic nerve; Chu-Moyer et al. (2002) reported compound 86, a selective SORD inhibitor with ED90 of 1–2 mg/kg/day in chronically diabetic rats, normalising sciatic-nerve fructose for ~17 h after a single oral 2 mg/kg dose. Fructose was normalised. Nerves were not helped — that was Cameron's result, published four years earlier.

## Discussion

Three findings, in order of importance.

**First, the target fails its own test.** An inhibitor that corrects the biochemical marker (fructose) without correcting nerve function is not a neuropathy drug. Cameron et al. showed this in 1997, and the programme continued for five more years on the strength of fructose endpoints. The Cortese et al. genetics result then inverted the rationale entirely: SORD loss *causes* neuropathy. Any future SORD inhibitor programme would have to explain why partial pharmacological inhibition is safe when complete genetic loss is pathogenic — and why it should work when the animal data says the second polyol step does not drive the functional deficit.

**Second, rigid docking cannot rank SORD inhibitors — on any centre, including the right one.** On the NAD+ centre ρ = −0.2, on the Zn2+ centre ρ = +0.2, on the inhibitor-bound structure ρ = +0.35, and the most potent compound never ranks first. The re-dock control is the cleanest statement of the failure: the co-crystallised ligand scores worst in its own pocket. Two structural reasons compound the problem: the catalytic Zn2+ — the defining feature of the active site, 6.28 Å from the ligand — is absent from the docked receptor in every run, and the method is rigid. A metal-aware method (explicit Zn coordination, or a structure with the metal retained) is a precondition for any meaningful SORD docking, not a refinement.

**Third, structure choice matters more than the compounds — and resolution-first picking gets it wrong.** The pipeline picked 1PL8 because it is the highest-resolution structure (1.90 Å vs 2.00 Å), and 1PL8 is the one structure of the three with no inhibitor in it. Moving the box 11.62 Å, from the NAD+ centroid to the Zn2+, shifted every score by up to 1.4 kcal/mol and flipped the ranking — a larger effect than the 1.1 kcal/mol separating the two stereoisomer forms. Papers that dock into 1PL8 without stating their centre are not comparable with each other, and pipelines that pick structures by resolution alone will repeat this error. The NAD+ centre also produces spuriously strong scores and unstable poses (+38.31 kcal/mol), which a single "best score" table would hide.

For Pakistan, where one in four adults lives with diabetes, the practical implication is to direct limited drug-discovery effort at the first polyol step — aldose reductase, where epalrestat is already approved in Japan and where the animal evidence is positive — rather than the second. SORD remains interesting as a diagnostic and genetics target (the Cortese et al. finding makes SORD sequencing relevant for unexplained hereditary neuropathy), but not as an inhibition target for diabetic neuropathy.

## Limitations

1. **No lab data.** All results are computational; no SORD assay was run.
2. **No metal in the model.** The catalytic Zn2+ was dropped during receptor preparation in all three runs; metal coordination is unmodelled, even on 1PL6.
3. **Rigid docking, ±1–2 kcal/mol noise.** The 6.4-fold measured difference between the two stereoisomer forms (1.1 kcal/mol) is below the method's resolution.
4. **Small n.** The rank correlation uses four compounds with measured values; a single additional compound could change ρ substantially.
5. **No measured potency for the reference.** CP-166572 has no ChEMBL SORD IC50; its role is structural only — though its co-crystal structure makes it the ideal re-dock control, which failed.
6. **Second-assay values.** Two compounds have higher IC50s in a second assay (350 and 480 nM); using the lower values favoured the docking comparison and it still failed.
7. **No RMSD for the re-dock.** The re-dock control is reported as a score only; the docked pose was not compared atom-by-atom with the crystal pose.

## Conclusion

Rigid docking into human SORD cannot rank known piperazino-pyrimidine inhibitors: Spearman ρ was −0.2 on the pipeline's NAD+ centre, +0.2 on the corrected Zn2+ centre, and +0.35 on the inhibitor-bound structure 1PL6 — and the co-crystallised ligand CP-166572 re-docked worst in its own pocket (−6.20 kcal/mol). The deeper finding is that the target itself failed: SORD inhibition lowered fructose without helping diabetic nerves in rats, and human SORD loss causes hereditary neuropathy. The polyol pathway's second step should not be pursued as a diabetic-neuropathy target on the current evidence; the first step, aldose reductase, is where the evidence sits. Any future SORD docking must be metal-aware, must use the inhibitor-bound structure, and must state its centre.

## Acknowledgments

Manuscript drafted with AI assistance (Lapis). The author reviewed all computed values against the raw docking outputs and all citations against the primary sources. This is an AI-assisted draft, not a peer-reviewed publication; all claims require independent laboratory verification. No funding was received. The author declares no conflicts of interest.

## References

1. Cameron NE, Cotter MA, Dines KC, Maxfield EK. Pharmacological manipulation of the polyol pathway in the prevention of diabetic neuropathy: sorbitol dehydrogenase inhibition versus aldose reductase inhibition. *Diabetologia*. 1997;40(3):271–281. doi:10.1007/s001250050674.
2. Cortese A, Zhu Y, Rebelo AP, et al. Biallelic mutations in SORD cause a common and potentially treatable hereditary neuropathy with implications for diabetes. *Nat Genet*. 2020;52(5):473–481. PMID: 32367058. doi:10.1038/s41588-020-0615-4.
3. Mylari BL, Oates PJ, Beebe DA, Brackett NS, Coutcher JB, Dina MS, Zembrowski WJ. Sorbitol dehydrogenase inhibitors (SDIs): a new potent, enantiomeric SDI, 4-[2-(1R-hydroxy-ethyl)-pyrimidin-4-yl]piperazine-1-sulfonic acid dimethylamide. *J Med Chem*. 2001;44(17):2695–2700. PMID: 11495581. doi:10.1021/jm0102001.
4. Chu-Moyer MY, Ballinger WE, Beebe DA, et al. Orally-effective, long-acting sorbitol dehydrogenase inhibitors: synthesis, structure-activity relationships, and in vivo evaluations of novel heterocycle-substituted piperazino-pyrimidines. *J Med Chem*. 2002;45(2):511–528. PMID: 11784155. doi:10.1021/jm010440g.
5. Pauly TA, Ekstrom JL, Beebe DA, et al. X-ray crystallographic and kinetic studies of human sorbitol dehydrogenase. *Structure*. 2003;11(9):1071–1085. PMID: 12962626. doi:10.1016/S0969-2126(03)00167-9.
6. International Diabetes Federation. *IDF Diabetes Atlas*, 10th edition. Brussels: IDF; 2021. Pakistan: 33 million adults (20–79 years) with diabetes; prevalence 26.7% (30.8% age-adjusted); 400,000 diabetes deaths in 2021; 26.9% undiagnosed.

## Data Availability

All docking outputs are available from the author on request. Pipeline output: `dock-HP-054-2026-11-14.json` (1PL8, NAD+ centre); corrected dockings: `dock-HP-054-2026-11-14-Zn.json` (1PL8, Zn2+ centre) and `dock-HP-054-2026-11-14-1PL6.json` (1PL6, co-crystallised CP-166572 centre). Structures: PDB 1PL6 (2.00 Å), 1PL7 (2.20 Å), 1PL8 (1.90 Å). Measured potencies: ChEMBL target CHEMBL2275, accessed 14 November 2026 (assays CHEMBL800733, CHEMBL801253, CHEMBL882165). Compound structures: PubChem CID 132302 (CP-166572); ChEMBL IDs CHEMBL90344, CHEMBL91846, CHEMBL151268, CHEMBL423753.
