# A Tideglusib Analogue Out-Docks Berberine on Sortase A by 0.60 kcal/mol — but Vina Cannot Rank the Measured Potencies

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-27 · **Health Papers Agent — Paper #124** (daily 5-paper run)

**Keywords:** sortase A; SrtA; Staphylococcus aureus; MRSA; anti-virulence; berberine; tideglusib; molecular docking; ChEMBL; Pakistan

---

## Abstract

Methicillin-resistant Staphylococcus aureus (MRSA) caused more than 100,000 deaths attributable to antimicrobial resistance in 2019, yet no approved drug targets sortase A (SrtA), the transpeptidase that anchors virulence factors to the staphylococcal cell wall. We asked whether any published SrtA inhibitor beats berberine — the best-known plant-derived SrtA inhibitor (IC50 ~26 µM) — on docking to the SrtA active site. Using the LeadForge pipeline (UniProtKB Q9S446 → ChEMBL target CHEMBL5362, 54 bioactivities → PubChem/RDKit, PAINS and ADMET screen) we docked berberine and four ChEMBL SrtA actives with AutoDock Vina on PDB 1T2O at the catalytic-triad centre. A tideglusib analogue, CHEMBL4646173, out-docked berberine by 0.60 kcal/mol (−7.36 vs −6.76 kcal/mol), but the docking ranking inverts the measured ranking: the most potent measured compound, CHEMBL5269466 (IC50 160 nM), docks only third (−6.67 kcal/mol), while berberine — the weakest measured compound at ~26 µM — docks second. Vina cannot rank this set. The falsifiable next step is a head-to-head FRET assay of all five compounds on the same day: if CHEMBL5269466 does not confirm below 1 µM, or if CHEMBL4646173 does not confirm below 5 µM, the docking ranking is refuted and the lead list re-opens. Two pipeline failures were caught and corrected before any number was reported: the first automated run resolved the target to the wrong protein (SraP, not SrtA), and the second docked 22.1 Å from the catalytic site on a selenomethionine residue — both runs are preserved in the data files, and neither contributes a number to this paper.

---

## 1. Introduction

Resistance has outrun the antibiotic pipeline, and the arithmetic is now measured rather than warned about: bacterial antimicrobial resistance caused an estimated 1.27 million deaths directly attributable to resistance in 2019, with 4.95 million deaths associated with it, and meticillin-resistant Staphylococcus aureus alone caused more than 100,000 attributable deaths — the single deadliest pathogen–drug combination in the analysis (Antimicrobial Resistance Collaborators, Lancet 2022;399:629–655). S. aureus was the second-leading pathogen for resistance-attributable deaths. Every new antibiotic that kills bacteria selects for resistance to itself; the field's response has been to look for targets that disarm rather than kill.

Sortase A is the cleanest version of that idea. SrtA is a 206-amino-acid membrane cysteine transpeptidase (UniProt Q9S446, gene srtA) that recognises the LPXTG sorting signal on surface proteins, cleaves after threonine, and anchors the protein to peptidoglycan. The anchored proteins are the pathogen's toolkit: adhesins that bind host tissue, immune-evasion proteins, and the machinery of biofilm formation. A bacterium without SrtA still grows — sortase is not essential and is not itself a virulence factor — but it cannot display its virulence factors, so it adheres poorly, forms weak biofilms, and is cleared more easily. That is the anti-virulence proposition: an inhibitor should attenuate infection without the bactericidal selection pressure that breeds resistance. It is also the proposition's weakness: because SrtA inhibition is not directly bactericidal, it is harder to screen (no MIC readout), harder to dose (attenuation, not killing), and — as of the most recent review — no approved drug targets SrtA (Hintzen et al., Chemistry 2024).

The published inhibitors fall into three generations. The first is the 2009 high-throughput screen of ~30,000 compounds (Suree et al., Bioorg Med Chem 2009;17:7174–7185), which produced pyridazinone and pyrazolethione analogues with sub-micromolar IC50 values — the most potent SrtA inhibitors reported, and still the benchmark. The second is the natural-product literature: berberine chloride, the isoquinoline alkaloid of Coptis chinensis, inhibits S. aureus sortase with an IC50 of 8.7 µg/mL (~26 µM), and the flavonoids myricetin, quercetin and curcumin inhibit in the 13–16 µg/mL range (Kim et al. 2004, and subsequent reviews). The third, most recent generation is repurposing and peptidomimetics: tideglusib analogues inhibit SrtA in the 0.9–12.6 µM range (J Med Chem 2020), and the peptidomimetic BzLPRDSar blocks biofilm formation in multidrug-resistant S. aureus (Microbiol Spectr 2026). A 2026 review in Open Biology concludes the target is promising but unproven in humans, with the open questions being selectivity across sortase homologues and whether attenuation translates into clinical benefit.

**Falsifiable question.** Does any published ChEMBL SrtA inhibitor beat berberine on docking to the SrtA active site, and does the docking ranking agree with the measured potencies? **Falsifier:** a head-to-head FRET assay in which the best docker fails to confirm below 5 µM, or the best measured compound (CHEMBL5269466, 160 nM) fails to confirm below 1 µM — either result refutes the ranking this paper reports. **Causal identification:** validated-control re-docking (berberine as the published reference, same structure, same grid, same protocol) — association only beyond that, since no experiment was run and docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-27: the global AMR burden analysis (Lancet 2022;399:629–655, doi:10.1016/S0140-6736(21)02724-0); the Suree et al. 2009 HTS and SAR paper (Bioorg Med Chem 2009;17:7174–7185, doi:10.1016/j.bmc.2009.08.067, PMID 19781950); the berberine sortase work (Kim et al. 2004, IC50 8.7 µg/mL); the tideglusib-analogue paper (J Med Chem 2020, doi:10.1021/acs.jmedchem.0c00803); the SrtA chemical-biology review (J Med Chem 2021, doi:10.1021/acs.jmedchem.1c00386); the complete-assessment review (Hintzen et al., Chemistry 2024, doi:10.1002/chem.202401103); the peptidomimetic study (Microbiol Spectr 2026, doi:10.1128/spectrum.02327-25, PMID 41773879); the 2026 Open Biology review (Open Biol 2026;16(9):250415, doi:10.1098/rsob.250415, PMID 42710897); and the SrtA structure paper (Zong et al., J Biol Chem 2004; PDB 1T2O). Measured IC50s for the four ChEMBL leads were retrieved live from the ChEMBL API on 2026-11-27 (target CHEMBL5362). The classical-canon sweep is in §4.3: Ibn Sina's Canon of Medicine, Book II (materia medica), records barberry (Berberis spp., the berberine source) among medicinal plants, and Al-Razi's Kitab al-Hawi records clinical observation of wound infection — neither describes sortase or an inhibitor, so the Islamic-principle discussion rests on hifz al-nafs and la darar, not on a classical source about this target.

### 2.2 Target identification — and the two failures that were caught

The pipeline resolves the target in two steps (UniProtKB text search, then ChEMBL target by accession), and both steps failed on the first attempt — which is why this section is written in full rather than summarised. **Failure 1 (wrong protein).** The query "Staphylococcus aureus sortase A" resolved to UniProt Q2FUW1 — SraP, a serine-rich adhesin for platelets, not sortase — and ChEMBL then returned CHEMBL2074, human maltase-glucoamylase. The 26 "leads" from that run were iminosugar glucosidase inhibitors (Tanimoto similarity to berberine 0.07–0.11), and the docking ran on PDB 4M00, which is the SraP ligand-binding region, not SrtA. Every number from that run is invalid for the SrtA question; the run is preserved as `dock-HP-113-2026-11-27-WRONG-TARGET-SraP.json` as the record of the failure, and contributes nothing to this paper. **Correction.** The target was re-specified by its reviewed accession: UniProt Q9S446 (gene srtA, 206 aa, Staphylococcus aureus). ChEMBL target by accession then returned CHEMBL5362, "Sortase A", single protein, S. aureus, with 54 bioactivities. Berberine was verified against PubChem (C20H18NO4+, MW 336.37, logP 3.1, 0 H-bond donors, 4 acceptors, TPSA 40.8 Å², 2 rotatable bonds, 0 Lipinski violations, PAINS-clean). The similarity screen against the 54 ChEMBL SrtA actives returned 25 leads; the top four by composite score were docked alongside berberine.

### 2.3 Molecular docking — and the grid-centre failure

**Failure 2 (wrong grid centre).** The re-run docked on PDB 1T2O (Zong et al. 2004, 2.3 Å, Se-SrtA C184A) — the correct protein — but the pipeline's centre picker landed on a selenomethionine residue. 1T2O contains no drug-like ligand, so the picker's fallback took the first HETATM group with ≥6 atoms, which is MSE141 of chain A. The grid centre (−22.31, −31.38, −5.00) is the exact centroid of MSE141 and sits 22.1 Å from the catalytic Ala184 Cα. The scores from that run (−8.57 to −7.11 kcal/mol) are systematically ~1 kcal/mol stronger than the corrected scores and measure binding near a methionine, not inhibition. They are reported here only as the failure record, in §3.3. **Correction.** The grid was re-centred on the catalytic triad: the centroid of all 26 atoms of His120, Ala184 (the Cys184→Ala mutation in this structure) and Arg197 in chain A, giving [−39.89, −18.59, −0.79]. All five ligands were re-docked with AutoDock Vina 1.2.7 at that centre (box 22.5 Å, exhaustiveness 8, best of 3 poses). The re-dock is the only docking result this paper reports. Two limits of the structure must be stated: 1T2O is the C184A mutant, so the catalytic thiol that covalent inhibitors would engage is absent; and it is an apo structure with no inhibitor bound, so the pocket is the substrate-binding site as defined by the triad, not a ligand-validated site.

### 2.4 PAINS screen

RDKit PAINS filter applied to berberine and all four ChEMBL leads. All five are PAINS-clean. No PAINS alert is hidden anywhere in this paper; there is none to hide. (Berberine's isoquinoline core is a known assay-interference risk in some formats, but it carries no PAINS alert under the RDKit filter used here; the FRET validation in §4.5 includes the redox and detergent controls that would expose such an artefact.)

### 2.5 Honesty limits

Docking scores are not activity: Vina's noise is ±1–2 kcal/mol, the structure is a C184A apo mutant, and no molecular dynamics or free-energy refinement was run. The ChEMBL IC50s are compared across records, not within one experiment — CHEMBL4646173, CHEMBL4637697 and CHEMBL4645185 each carry two ChEMBL records differing up to 10-fold (e.g. 1,200 vs 12,600 nM), which is assay-to-assay spread, not a measurement. Berberine's ~26 µM is converted from the published 8.7 µg/mL using MW 336.37. No experimental data were generated in this study.

## 3. Results

### 3.1 Docking: the comparison table (corrected centre)

| Compound | ChEMBL ID | Best affinity (kcal/mol) | Poses (kcal/mol) | Measured IC50 (SrtA) | MW (Da) | logP | TPSA (Å²) | PAINS |
|---|---|---|---|---|---|---|---|---|
| CHEMBL4646173 (tideglusib analogue) | CHEMBL4646173 | **−7.36** | −7.36, −7.24, −7.04 | 1,200 nM (also 12,600 nM) | 348.43 | 3.57 | 44.0 | clean |
| Berberine (reference) | — (PubChem) | −6.76 | −6.76, −6.73, −6.36 | ~26,000 nM (8.7 µg/mL) | 336.37 | 3.10 | 40.8 | clean |
| CHEMBL5269466 | CHEMBL5269466 | −6.67 | −6.67, −6.58, −6.52 | **160 nM** | 530.58 | 4.65 | 88.2 | clean |
| CHEMBL4645185 (tideglusib analogue) | CHEMBL4645185 | −6.35 | −6.35, −6.23, −6.23 | 900 nM (also 12,600 nM) | 300.38 | 3.01 | 44.0 | clean |
| CHEMBL4637697 (tideglusib analogue) | CHEMBL4637697 | −6.07 | −6.07, −6.02, −6.00 | 1,200 nM (also 5,000 nM) | 333.37 | 1.72 | 79.3 | clean |

All five docked into the same grid (1T2O, catalytic-triad centre [−39.89, −18.59, −0.79], box 22.5 Å). CHEMBL4646173 beats berberine by 0.60 kcal/mol — inside Vina's ±1–2 kcal/mol noise, so the "win" is not established by docking alone. The three tideglusib analogues are the J Med Chem 2020 series; CHEMBL5269466 is the most potent measured SrtA inhibitor in this set (160 nM, ChEMBL record from the J Med Chem 2021 review).

### 3.2 The ranking inversion — the real result

The docking ranking and the measured ranking disagree at every position that matters. By measurement: CHEMBL5269466 (160 nM) > CHEMBL4645185 (900 nM) > CHEMBL4646173 ≈ CHEMBL4637697 (1,200 nM) > berberine (~26,000 nM). By docking: CHEMBL4646173 (−7.36) > berberine (−6.76) > CHEMBL5269466 (−6.67) > CHEMBL4645185 (−6.35) > CHEMBL4637697 (−6.07). The best measured compound docks third; the worst measured compound docks second; the best docker is third by measurement. Berberine's −6.76 kcal/mol would imply low-micromolar binding, but its measured IC50 is ~26 µM — docking over-ranks it by roughly an order of magnitude. CHEMBL5269466's −6.67 kcal/mol would imply low-micromolar binding, but its measured IC50 is 160 nM — docking under-ranks it by roughly an order of magnitude. A paper that reported only the docking table would conclude that berberine is a near-lead and CHEMBL5269466 is unremarkable; the measured data say the opposite. This is the same failure mode this series found for HIV-1 protease inhibitors (Paper #121): rigid docking on an apo, mutated structure cannot rank congeneric and non-congeneric inhibitors together, and a docking "win" of 0.60 kcal/mol inside a ±1–2 kcal/mol noise band is not a win at all. The docking result is therefore reported as a negative: **Vina cannot rank these SrtA inhibitors, and no lead is declared on docking.**

### 3.3 The wrong-centre run, for the record

The uncorrected run (grid on MSE141, 22.1 Å from the catalytic site) returned CHEMBL5269466 −8.57, CHEMBL4646173 −8.10, berberine −7.94, CHEMBL4637697 −7.39, CHEMBL4645185 −7.11 kcal/mol — every score ~0.7–1.9 kcal/mol stronger than the corrected run, with a different rank order (CHEMBL5269466 first, not third). Had the centre error gone uncaught, this paper would have reported a false −8.57 kcal/mol "lead" and a false ranking. The correction cost one re-dock; the lesson is the standing one for this pipeline (AGENTS.md, 2026-11-11): never trust an auto-picked grid centre on a ligand-free structure — verify it against the catalytic residues, and report the check.

### 3.4 Comparison with published docking

Suree et al. (2009) docked their pyridazinone leads by induced-fit docking into the solution structure of the covalent SrtA–LPAT complex and reported poses consistent with sub-micromolar IC50s — but with a different method (induced-fit, not rigid Vina), a different structure, and no Vina scores to compare against, so no numerical comparison is possible. No published Vina scores exist for berberine or the tideglusib analogues on 1T2O. This paper's docking table therefore stands alone as a Vina ranking, and §3.2 is the statement that the ranking fails against measurement.

## 4. Discussion

### 4.1 The reframe

The question was "what beats berberine?" and the honest answer is that docking cannot answer it for this target. The measured data already answer it: CHEMBL5269466 at 160 nM is ~160-fold more potent than berberine, and the tideglusib analogues at 0.9–1.2 µM are ~20-fold more potent. The field does not need a better docker; it needs the measured compounds tested in the assay that matters — biofilm inhibition in live S. aureus — because SrtA inhibition is attenuation, and attenuation is only meaningful if the bacterium actually fails to adhere and form biofilm. The reframe is therefore from "find a better score" to "test the best measured compound in the functional assay": CHEMBL5269466 has never, to our knowledge, been reported in a biofilm assay, and that is the gap, not the docking table.

### 4.2 Why the "win" must not be over-read

Three corrections guard the headline. First, the 0.60 kcal/mol margin for CHEMBL4646173 over berberine is inside Vina noise — it is not a win. Second, the docking ranking is inverted against measurement, so even a larger margin would need assay confirmation. Third, the measured IC50s themselves carry up to 10-fold record-to-record spread (CHEMBL4646173: 1,200 vs 12,600 nM), so the "1,200 nM" figures are order-of-magnitude, not precise. What is solid is the direction: three tideglusib analogues and one 160 nM compound are all far more potent than berberine by measurement, and all five are PAINS-clean and drug-like (MW 300–531, 0–1 Lipinski violations). The memorable number is the distance: **22.1 Å** — the grid was centred on the wrong residue, and the uncorrected scores were inflated by ~1 kcal/mol. A pipeline that does not check its grid centre will manufacture leads.

### 4.3 Mechanism — and the classical canon

SrtA cleaves the LPXTG sorting signal between threonine and glycine and transfers the cleaved protein to peptidoglycan via its catalytic Cys184–His120–Arg197 triad; an inhibitor that occupies that pocket blocks anchoring of every LPXTG protein at once — adhesins, immune-evasion factors, biofilm proteins — which is why one target can attenuate many virulence functions. Test for each link: (i) the FRET assay with the Abz-LPETG–Dnp substrate measures catalytic inhibition directly, against the published IC50s; (ii) a fibrinogen/fibronectin adhesion assay measures whether anchoring actually fails in live bacteria; (iii) a crystal-violet biofilm assay measures the functional consequence, against the BzLPRDSar peptidomimetic as the positive control. The classical canon knows the disease, not the enzyme: Ibn Sina's Canon of Medicine (c. 1025), Book II, records barberry (Berberis spp., the berberine source) among medicinal plants, and Al-Razi's Kitab al-Hawi (c. 900) records clinical observation of wound infection — but neither describes sortase, so the principle carried forward is hifz al-nafs (preservation of life, defined by Al-Ghazali in Al-Mustasfa and systematised by Al-Shatibi in Al-Muwafaqat) joined to la darar (no harm) and stewardship (khilafah): a drug that disarms rather than kills imposes less selection pressure for resistance, which is harm-avoidance extended to the next patient, not just this one. The Canon was not re-read in full for this paper; the berberine–SrtA link is modern (Kim et al. 2004), not a classical claim.

### 4.4 Testable hypotheses

1. CHEMBL5269466 inhibits S. aureus SrtA with an IC50 below 1 µM in the FRET assay on the same day as berberine. Falsifier: IC50 above 1 µM, which would refute the ChEMBL record and remove the lead.
2. CHEMBL4646173 inhibits SrtA with an IC50 below 5 µM in the same assay. Falsifier: IC50 above 5 µM, which would refute its docking "win" over berberine.
3. CHEMBL5269466 at its IC50 reduces S. aureus biofilm formation by at least 50% in a crystal-violet assay without reducing bacterial growth (OD600 unchanged). Falsifier: no biofilm reduction at the IC50, or growth inhibition at the same concentration — either would show the compound is not a functional anti-virulence lead.
4. Berberine's FRET IC50 reproduces within 3-fold of the published ~26 µM under the same conditions. Falsifier: an IC50 below 5 µM, which would suggest the published value was an artefact of assay conditions.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): FRET assay — recombinant SrtA catalytic domain (residues 60–206), Abz-LPETG–Dnp substrate, all five compounds on one plate, n=3, with berberine as the reference and the Suree pyridazinone series as the positive control if obtainable; redox and detergent controls to expose aggregation artefacts; readout IC50. Stage 2 (weeks 4–6): adhesion assay (fibrinogen binding) and crystal-violet biofilm assay for the two best compounds from Stage 1, with growth curves (OD600) to confirm the effect is anti-virulence, not antibacterial; readout percentage biofilm reduction at the IC50. Stage 3 (weeks 7–12): if a compound passes stages 1–2 — IC50 below 1 µM and ≥50% biofilm reduction without growth inhibition — a Galleria mellonella infection model against the ML346 precedent; if none passes, publish the negative result with the ChEMBL table as the reason the hypothesis failed. No animal work is proposed before stages 1–2 pass.

## 5. Limitations

1. Docking only, on a C184A apo mutant structure with no inhibitor bound; Vina noise is ±1–2 kcal/mol and the docking ranking is inverted against measurement, so no lead is declared on docking.
2. The measured IC50s are retrieved across ChEMBL records, not within one experiment; three compounds carry duplicate records differing up to 10-fold.
3. Berberine's ~26 µM is converted from a published 8.7 µg/mL; the original assay used a different SrtA construct than the ChEMBL records for the other compounds.
4. No experimental data were generated in this study; all potencies are retrieved, not measured.
5. The Suree et al. pyridazinone series — the most potent published SrtA inhibitors (sub-micromolar) — were not docked here, because the pipeline's lead set is drawn from ChEMBL SrtA actives and those compounds' ChEMBL records were not in the top-ranked set; the comparison against the strongest incumbent is therefore incomplete and is the first item in the validation plan.
6. No Pakistani MRSA isolate data exist for SrtA: no local study reports SrtA sequence variation or sortase-inhibitor susceptibility in Pakistani MRSA, so the policy section recommends measurement, not a drug decision.
7. The classical-canon sweep did not re-read the Canon or Kitab al-Hawi in full; the Islamic-principle discussion rests on hifz al-nafs and la darar as principles, not on a classical source about this target. The full 23 volumes of Kitab al-Hawi exist in English only in selections.

## 6. Conclusion

A tideglusib analogue, CHEMBL4646173, out-docks berberine on sortase A by 0.60 kcal/mol (−7.36 vs −6.76 kcal/mol), but the margin is inside Vina noise and the docking ranking inverts the measured ranking — the 160 nM lead CHEMBL5269466 docks third, and berberine, the weakest measured compound at ~26 µM, docks second. Vina cannot rank these sortase A inhibitors, and no lead is declared on docking. The measured data already point to the better compounds, and the next step is the cheap, decisive test: one head-to-head FRET assay plus one biofilm assay, not a bigger docking screen.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the Ministry of National Health Services, with the National Institute of Health and university microbiology departments as the technical arms. **Decision:** whether to spend anything on an anti-virulence programme for MRSA, and what must exist first. **Exact change:** do not fund a docking screen or import a sortase inhibitor on a docking score — this paper shows a docking ranking can invert the measured ranking, and a grid-centre error of 22.1 Å inflated scores by ~1 kcal/mol; instead, fund one measurement first: a head-to-head FRET assay of the four ChEMBL compounds plus berberine against the SrtA catalytic domain, run in a Pakistani university lab, with the biofilm assay as the second gate. **If evidence Z appears, reverse this:** if the assay confirms CHEMBL5269466 below 1 µM with ≥50% biofilm reduction and no growth inhibition, move to a lead-optimisation assessment for that compound; if the assay refutes the ChEMBL potencies, drop the list and re-open the Suree pyridazinone series — do not proceed to any drug evaluation on docking scores alone. The Islamic principle is hifz al-nafs joined to la darar and stewardship (khilafah): where a measurement can distinguish a drug that disarms the pathogen from one that merely scores well, running the measurement is the obligation; prescribing on a docking score would risk the next patient's resistance. The evidence here is thin — retrieved potencies and a failed docking ranking — so the recommendation is "run the assay", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399(10325):629–655. doi:10.1016/S0140-6736(21)02724-0.
2. Suree N, et al. Discovery and structure-activity relationship analysis of Staphylococcus aureus sortase A inhibitors. Bioorg Med Chem. 2009;17(20):7174–7185. doi:10.1016/j.bmc.2009.08.067. PMID: 19781950.
3. Kim SH, et al. Inhibition of the bacterial surface protein anchoring transpeptidase sortase by isoquinoline alkaloids. (Berberine chloride IC50 8.7 µg/mL against S. aureus sortase.) 2004.
4. Tideglusib and its analogues as inhibitors of Staphylococcus aureus SrtA. J Med Chem. 2020. doi:10.1021/acs.jmedchem.0c00803.
5. Chemical biology of sortase A inhibition: a gateway to anti-infective therapeutic agents. J Med Chem. 2021. doi:10.1021/acs.jmedchem.1c00386.
6. Hintzen JCJ, Abujubara H, Tietze D, Tietze A. The complete assessment of small molecule and peptidomimetic inhibitors of sortase A towards antivirulence treatment. Chemistry. 2024. doi:10.1002/chem.202401103.
7. Targeted sortase A inhibition by novel peptidomimetic antivirulents against staphylococcal infections. Microbiol Spectr. 2026. doi:10.1128/spectrum.02327-25. PMID: 41773879.
8. Molecular basis and therapeutic potential of sortase A inhibitors as new antibiotics against MDR pathogens. Open Biol. 2026;16(9):250415. doi:10.1098/rsob.250415. PMID: 42710897.
9. Zong Y, Bice TW, Ton-That H, Schneewind O. Crystal structures of Staphylococcus aureus sortase A and its substrate complex. J Biol Chem. 2004. (PDB 1T2O, 2.3 Å, Se-SrtA C184A.)
10. UniProtKB Q9S446: Sortase A (srtA), Staphylococcus aureus, 206 aa. UniProt. Accessed 2026-11-27.
11. ChEMBL target CHEMBL5362: Sortase A, Staphylococcus aureus (54 bioactivities); activities for CHEMBL5269466, CHEMBL4646173, CHEMBL4637697, CHEMBL4645185 retrieved live 2026-11-27. ChEMBL, EMBL-EBI.
12. RCSB PDB entry 1T2O: crystal structure of Se-SrtA, C184-Ala, 2.3 Å. RCSB Protein Data Bank. Accessed 2026-11-27.
13. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Book II materia medica — cited for the barberry record only.)
14. Al-Ghazali. Al-Mustasfa min 'Ilm al-Usul. c. 1109. (Defines the five necessities of the law, including hifz al-nafs.)
15. Al-Shatibi. Al-Muwafaqat fi Usul al-Shari'a. 14th c. (Systematises maqasid al-shariah.)

## Data availability

All potencies, descriptors and docking scores reported here are in `hidden_files/dock-HP-113-2026-11-27.json` (LeadForge pipeline run: target UniProt Q9S446; ChEMBL target CHEMBL5362, 54 bioactivities; 25 similarity leads; berberine PubChem-verified) and `hidden_files/dock-HP-113-2026-11-27-redock.json` (re-dock at the catalytic-triad centre [−39.89, −18.59, −0.79], Vina 1.2.7, box 22.5 Å, exhaustiveness 8). The two failed runs are preserved: `hidden_files/dock-HP-113-2026-11-27-WRONG-TARGET-SraP.json` (target resolved to SraP/maltase-glucoamylase; docking on PDB 4M00) and the wrong-centre scores in the pipeline JSON (grid on MSE141, 22.1 Å from the catalytic site). Reference drug berberine (PubChem, C20H18NO4+); comparators CHEMBL5269466, CHEMBL4646173, CHEMBL4637697, CHEMBL4645185, with measured IC50s retrieved live from ChEMBL on 2026-11-27. Structure: PDB 1T2O (2.3 Å, C184A mutant, no ligand). No additional data were generated.
