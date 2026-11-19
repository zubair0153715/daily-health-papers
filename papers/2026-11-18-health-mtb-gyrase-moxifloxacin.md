# Four Nanomolar Gyrase Inhibitors Out-Score Moxifloxacin at the M. tuberculosis Cleavage Site — but the Margin Is Inside Vina Noise and the D94G Test Is Still Missing

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-18 · **Health Papers Agent — Paper #75** (daily 5-paper run)

**Keywords:** tuberculosis; DNA gyrase; moxifloxacin; fluoroquinolone resistance; gyrA; molecular docking; ChEMBL; MDR-TB

---

## Abstract

Multidrug-resistant tuberculosis (MDR-TB) kills because fluoroquinolones fail: resistance is dominated by gyrA mutations D94G and A90V in the quinolone resistance-determining region, and moxifloxacin — a core drug of the WHO BPaLM regimen — loses activity against them. We asked whether ChEMBL-recorded nanomolar inhibitors of the Mycobacterium tuberculosis DNA gyrase A/B complex bind the true fluoroquinolone cleavage site more strongly than moxifloxacin itself. Using the LeadForge pipeline (UniProtKB P9WG45 → ChEMBL target CHEMBL3430898, 46 bioactivities → PubChem/RDKit similarity, PAINS and ADMET screen → AutoDock Vina 1.2.7), we re-docked the top four leads and moxifloxacin on the moxifloxacin-bound cleavage complex 5BS8 (2.4 Å), centred on the co-crystallised moxifloxacin. The four leads scored −10.87 to −10.37 kcal/mol versus −9.38 kcal/mol for re-docked moxifloxacin, with tight pose consistency (top-3 spread ≤0.6 kcal/mol); their measured enzyme IC50 values are 5, 10, 65 and 780 nM, and none carries a PAINS alert. The honest limit: every margin over moxifloxacin (0.99–1.49 kcal/mol) lies inside Vina's ±1–2 kcal/mol noise, so docking alone cannot rank these compounds, and none has yet been tested against a D94G or A90V mutant enzyme or whole cells. The claim that any of these four is a better fluoroquinolone-alternative would be refuted if re-docking on a D94G cleavage complex, or a mutant-enzyme assay, shows a ≥2 kcal/mol or >10-fold IC50 loss. The falsifiable next step is a 8–12-week enzyme-plus-MIC test of the four leads against wild-type and D94G/A90V M. tuberculosis gyrase and clinical isolates.

---

## 1. Introduction

Tuberculosis returned to the top of the infectious-disease mortality list: the WHO Global Tuberculosis Report 2024 records about 10.8 million people falling ill with TB in 2023 and about 1.25 million deaths, with TB again the leading cause of death from a single infectious agent. Around 400,000 people each year develop multidrug-resistant or rifampicin-resistant TB (MDR/RR-TB), and Pakistan is among the eight countries that together account for two-thirds of the global burden. For MDR/RR-TB that remains fluoroquinolone-susceptible, WHO recommends the 6-month all-oral BPaL/BPaLM regimens — bedaquiline, pretomanid, linezolid, and moxifloxacin in BPaLM — so the fluoroquinolone is load-bearing: lose it and the regimen collapses into longer, more toxic alternatives.

Fluoroquinolone resistance in M. tuberculosis is almost entirely a gyrase story. Mutations in the quinolone resistance-determining region (QRDR) of gyrA, above all D94G and A90V, block drug binding at the DNA-cleavage complex. In a 2025 South Korean series of 304 isoniazid- and/or rifampicin-resistant isolates, 34 carried gyrA/gyrB mutations and D94G (44.8%) and A90V (24.1%) were the most frequent gyrA changes; every gyrA mutant was moxifloxacin-resistant. In São Paulo, among rifampicin- and/or isoniazid-resistant isolates tested by line-probe assay, 38 of 41 second-line mutations were fluoroquinolone mutations (35 in gyrA), and 97% of MDR strains carrying a second-line mutation were pre-XDR — MDR plus fluoroquinolone resistance. The clinical question is therefore narrow and urgent: is there a compound that still binds the cleavage site when D94G or A90V is present?

The classical medical canon described this disease long before the bacillus was known: Ibn Sina's Canon of Medicine (c. 1025) discusses pulmonary wasting disease ("sil") as a distinct consumptive syndrome, and Al-Razi's Kitab al-Hawi records clinical observation of chronic cough with wasting. These texts are hypothesis sources, not evidence — they knew the syndrome, not the target — but they establish that the disease burden this paper addresses is centuries old in the region, and the Islamic principle behind acting on it is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL-recorded nanomolar inhibitors of M. tuberculosis DNA gyrase bind the true fluoroquinolone cleavage site (PDB 5BS8) at scores beyond re-docked moxifloxacin, and would that binding survive the D94G/A90V mutations? **Falsifier:** a ≥2 kcal/mol loss on re-docking against a D94G (or A90V) cleavage complex, or a >10-fold IC50 shift in a mutant-enzyme assay, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the reference drug re-docked on its own co-crystal structure — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-18: PubMed-indexed and publisher sources on M. tuberculosis gyrA/gyrB fluoroquinolone resistance (2025–2026), the WHO Global Tuberculosis Report 2024, the RCSB records for PDB 3M4I and 5BS8, and the ChEMBL record for target CHEMBL3430898. The Islamic-canon sweep covered the available digitised canon relevant to the question: Ibn Sina, Al-Qanun fi al-Tibb (c. 1025); Al-Razi, Kitab al-Hawi (c. 900) — consulted in the literature-map summaries, not in full Arabic text (see Limitations).

### 2.2 Molecular docking

Standardised AutoDock Vina 1.2.7 protocol, exactly as Papers #1/#3. Target: M. tuberculosis DNA gyrase, UniProtKB P9WG45 (DNA gyrase subunit B, H37Rv; the ChEMBL bioactivity target is the GyrA/GyrB protein complex CHEMBL3430898). Structure: PDB 5BS8, the gyrase–fluoroquinolone cleaved complex with moxifloxacin co-crystallised, 2.4 Å (Blower et al., PNAS 2016). Grid centre: centroid of the co-crystallised moxifloxacin (MFX) in 5BS8, [40.10, 2.92, 22.41], box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The same centre, box and exhaustiveness were used for moxifloxacin and all four leads.

**A corrected-centre audit, stated plainly.** The pipeline first auto-picked PDB 3M4I (1.95 Å) and docked all five compounds there, scoring −6.35 to −5.60 kcal/mol. That run is DISCARDED, not reported as a result: 3M4I is the isolated GyrB TOPRIM domain fragment, and its auto-picked centre sat on a small HETATM ion — it is not the fluoroquinolone site. Moxifloxacin binds the cleavage complex (GyrA + DNA + Mg²⁺), whose structure is 5BS8. This is the same class of error as the TYK2 JH1/JH2 domain audit (2026-11-11): the PDB domain must match the drug's binding site. All scores in §3 are from the corrected 5BS8 re-dock (`hidden_files/redock_hp065.py`, output `dock-HP-065c-2026-11-18.json`); the discarded 3M4I run is preserved in `dock-HP-065-2026-11-18.json` for audit. DNA chains in 5BS8 are ATOM records and are retained in the receptor; the Mg²⁺ ions are HETATM and are dropped by the receptor preparation, so the fluoroquinolone Mg²⁺–water bridge is absent from scoring — a stated limitation (§5).

### 2.3 PAINS screen

RDKit PAINS filter applied to all 26 pipeline leads. None of the four docked leads carries a PAINS alert. One of the 26 leads (rank 24, CHEMBL3628453) carries a PAINS alert; it was not docked and is not proposed here.

### 2.4 ADMET and toxicity read-across

RDKit descriptors (Lipinski/Veber) computed for every lead; ToxGuard Tox21 kNN read-across (12 assays) run for every lead. Moxifloxacin itself (PubChem CID 152946, C21H24FN3O4, MW 401.44) passes Lipinski with 0 violations and scores 0 on all 12 measured Tox21 assays.

### 2.5 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for these four compounds against mutant gyrase or whole-cell M. tuberculosis in this study. Measured IC50 values below are ChEMBL records against the wild-type gyrase complex, not new measurements.

## 3. Results

### 3.1 Docking: the comparison table

| Compound | ChEMBL IC50 vs gyrase complex* | Best affinity, 5BS8 (kcal/mol) | Top-3 poses (kcal/mol) | PAINS | MW / logP / TPSA |
|---|---|---|---|---|---|
| CHEMBL4250651 | 10 nM (pChEMBL 8.00) | **−10.87** | −10.87, −10.66, −10.63 | none | 424.44 / 1.75 / 137.99 |
| CHEMBL4238919 | 5 nM (pChEMBL 8.30) | **−10.68** | −10.68, −10.49, −10.24 | none | 424.44 / 1.75 / 137.99 |
| CHEMBL3286436 | 65 nM (pChEMBL 7.19) | **−10.41** | −10.41, −10.13, −9.84 | none | 456.55 / 2.71 / 106.97 |
| CHEMBL3403255 | 780 nM (pChEMBL 6.11) | **−10.37** | −10.37, −9.95, −9.91 | none | 396.44 / 4.61 / 57.26 |
| Moxifloxacin (reference, re-docked) | approved drug; MIC breakpoint 1.0 µg/mL† | −9.38 | −9.38, −9.03, −9.00 | none | 401.44 / 2.37 / 83.80 |

\* ChEMBL-recorded IC50 against M. tuberculosis DNA gyrase A/B complex (target CHEMBL3430898), retrieved live 2026-11-18. † Moxifloxacin resistance breakpoint 1.0 µg/mL in Löwenstein–Jensen phenotypic testing (Kim et al., 2025).

All four leads out-score re-docked moxifloxacin, by 0.99–1.49 kcal/mol, with tight pose consistency (top-3 spread ≤0.6 kcal/mol for every compound). Two leads, CHEMBL4238919 and CHEMBL4250651, share identical descriptors (MW 424.44, logP 1.75, TPSA 137.99) — they are close analogues, not independent scaffolds, so the "four leads" are effectively three chemotypes. Their TPSA of 137.99 Å² sits just under Veber's 140 Å² limit: a permeability flag, not a failure.

### 3.2 The docking–activity discordance that must not be hidden

The measured IC50s do not track the docking order. CHEMBL3403255, the weakest measured inhibitor (780 nM, 156-fold weaker than CHEMBL4238919's 5 nM), docks at −10.37 kcal/mol — essentially tied with the 5 nM compound. Conversely the 5 nM and 10 nM compounds differ by only 0.19 kcal/mol in docking. Rigid Vina scoring on this site cannot resolve a 100-fold potency range. This is the paper's most important negative result: **the docking ranking is not a potency ranking**, and any claim built on the −10.87 vs −9.38 gap alone would be over-reading noise.

### 3.3 Toxicity read-across

Tox21 kNN read-across predicted no assay above 0.4 probability for any of the four leads (highest: SR-ARE 0.38 for CHEMBL4238919; all others ≤0.33). This is a weak screen — read-across, not measurement — and does not clear any compound for development.

### 3.4 Comparison with published docking

No published Vina study of these four ChEMBL compounds on 5BS8 was found in the sweep; the comparison here is internal (leads vs re-docked reference on the same structure, same protocol). The re-docked moxifloxacin score of −9.38 kcal/mol on its own co-crystal structure is the validated control that anchors the comparison: a method that could not recover strong binding for the co-crystallised drug would be broken. It did.

## 4. Discussion

### 4.1 The reframe

The question this paper can actually answer is narrower than the one it started with. It cannot say "these four compounds beat moxifloxacin" — the margins are inside noise and the docking order contradicts the measured IC50 order. What it can say is: (a) four already-measured nanomolar gyrase inhibitors bind the correct fluoroquinolone site with tight, reproducible poses; (b) the pipeline's first, wrong-site run was caught and corrected before publication, and the correction is documented; (c) the decisive experiment is now sharply defined — mutant-enzyme and whole-cell testing against D94G/A90V — and it is cheap and feasible in a university lab.

### 4.2 Why the "win" must not be over-read

Three reasons. First, the 0.99–1.49 kcal/mol margins are inside Vina's ±1–2 kcal/mol noise. Second, the docking order contradicts the measured potency order by up to 156-fold. Third, the Mg²⁺–water bridge that anchors fluoroquinolones in the cleavage complex is absent from this scoring, and resistance mutations D94G/A90V act precisely by perturbing that region — so the site was modelled without one of its key physical features. A compound that scores well here may still fail against the mutant.

### 4.3 Mechanism

Fluoroquinolones trap gyrase on cleaved DNA by intercalating at the DNA break and chelating the catalytic Mg²⁺ via a water bridge; GyrA residues 90 and 94 sit at the drug-binding pocket, and D94G removes a carboxylate that organises the water network while A90V introduces steric bulk. A genuine D94G-active alternative must either tolerate the lost carboxylate or bind without the Mg²⁺ bridge. Test for each link: (i) mutant-enzyme cleavage assay measures whether the compound still traps the mutant complex; (ii) whole-cell MIC against D94G/A90V clinical isolates measures whether it still kills; (iii) a D94G cleavage-complex structure, if one becomes available, would let docking test the mechanism directly.

### 4.4 Testable hypotheses

1. CHEMBL4238919 (5 nM wild-type IC50) retains an IC50 within 10-fold of wild-type against D94G gyrase in a supercoiling/cleavage assay. Falsifier: >10-fold shift.
2. At least one of the four leads has a whole-cell MIC ≤1 µg/mL against a D94G clinical isolate. Falsifier: all four MICs >4 µg/mL.
3. Re-docking on a D94G-modelled cleavage complex preserves the lead's score within 2 kcal/mol of its wild-type score. Falsifier: ≥2 kcal/mol loss.

### 4.5 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): recombinant wild-type and D94G/A90V M. tuberculosis gyrase supercoiling inhibition assay for the four leads + moxifloxacin control; readout IC50, n=3, with redox/aggregation controls. Stage 2 (weeks 4–8): whole-cell MIC (microdilution) against H37Rv and 3–5 D94G/A90V clinical isolates from a Pakistani reference laboratory, with moxifloxacin and bedaquiline controls. Stage 3 (weeks 9–12): if any lead passes stages 1–2, cytotoxicity (HepG2) and hERG screen; if none passes, publish the negative result with the docking data as the reason the hypothesis failed.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows every reported margin.
2. The Mg²⁺ ions were dropped from the receptor, removing the fluoroquinolone water-bridge interaction; scores may not reflect true binding energetics.
3. No mutant structure or mutant assay exists in this work — the D94G/A90V question, which is the whole point, is untested.
4. Docking order contradicts measured IC50 order (156-fold discordance); rigid docking cannot rank these compounds.
5. Two of the four leads are close analogues, not independent chemotypes; TPSA 137.99 Å² for both is a permeability flag.
6. Measured IC50 values are ChEMBL records against the wild-type complex; assay conditions vary across source studies and were not re-verified compound by compound.
7. The Islamic-canon sweep used the literature-map summaries of Ibn Sina's Canon and Al-Razi's Kitab al-Hawi; the full Arabic texts were not read, and other classical works on consumption (e.g. in the Canon's Book III) were not individually consulted.

## 6. Conclusion

Four ChEMBL-recorded nanomolar inhibitors of M. tuberculosis DNA gyrase bind the true fluoroquinolone cleavage site (5BS8) with scores of −10.87 to −10.37 kcal/mol against −9.38 kcal/mol for re-docked moxifloxacin, with tight pose consistency and no PAINS alerts. The margins are inside Vina noise and the docking order contradicts the measured potency order, so this is not evidence that any of them beats moxifloxacin — it is evidence that the four are worth the cheap, decisive test: wild-type versus D94G/A90V enzyme and whole-cell assays. That test, not another docking run, is the next step.

## 7. Policy implications

**Decision-maker:** Pakistan's National TB Programme and the provincial TB reference laboratories, with DRAP as regulator. **Decision:** whether to fund a small, targeted validation of existing ChEMBL gyrase inhibitors against local D94G/A90V isolates. **Exact change:** commission the 8–12-week enzyme-plus-MIC screen proposed in §4.5 for these four leads against Pakistani D94G/A90V isolates, instead of continuing to rely on imported fluoroquinolone-susceptibility assumptions for BPaLM eligibility. **If evidence Z appears, reverse this:** if all four leads lose >10-fold activity against D94G/A90V enzyme or isolates, drop this chemotype set and redirect the same screen to the next four ChEMBL gyrase inhibitors — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable drug from a useless one for a disease that kills ~1.25 million people a year, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. World Health Organization. Global Tuberculosis Report 2024. Geneva: WHO; 2024.
2. Blower TR, Williamson BH, Kerns RJ, Berger JM. Crystal structure and stability of gyrase-fluoroquinolone cleaved complexes from Mycobacterium tuberculosis. Proc Natl Acad Sci U S A. 2016;113(7):1706-1713. doi:10.1073/pnas.1525047113. PMID: 26792525.
3. Piton J, Petrella S, Delarue M, Andre-Leroux G, Jarlier V, Aubry A, Mayer C. Structural insights into the quinolone resistance mechanism of Mycobacterium tuberculosis DNA gyrase. PLoS One. 2010;5(8):e12245. doi:10.1371/journal.pone.0012245. PMID: 20805881.
4. Liu X, Peng Y, Li J, Jiao Y, Wu Y, Zhang Y, Gao X, Xiang Y, Ren J, Ma Q, Li X, Zhao Z, Han Z, Shen X, Ma X, Tie Y, et al. Development of a point-of-care dual one-step recombinase-aided PCR assay for rapid identification of Mycobacterium tuberculosis gyrA mutations conferring fluoroquinolone resistance. Front Microbiol. 2026;17:1772984. doi:10.3389/fmicb.2026.1772984.
5. Fluoroquinolone and second-line injectable resistance among rifampicin- and isoniazid-resistant Mycobacterium tuberculosis clinical isolates: a molecular study from a high-burden setting. Microorganisms. 2025;13(11):2470.
6. Kim S, Kim HJ, Heo R. Mutations in gyrA and gyrB among drug-resistant Mycobacterium tuberculosis isolates in South Korea. J Vis Exp. 2025. (JoVE Visualize record, published 31 October 2025.)
7. ChEMBL target CHEMBL3430898: DNA gyrase subunit A/DNA gyrase subunit B, Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv), protein complex. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-18.
8. World Health Organization. WHO announces updated definitions of extensively drug-resistant tuberculosis. WHO News; 27 January 2021.
9. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; pulmonary wasting disease, "sil".)
10. Al-Razi. Kitab al-Hawi fi al-Tibb (Comprehensive Book of Medicine). c. 900. (Classical source; clinical observation of chronic consumptive disease.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-065c-2026-11-18.json` (corrected 5BS8 re-dock) and `hidden_files/dock-HP-065-2026-11-18.json` (discarded 3M4I run, preserved for audit). Ligand identities are ChEMBL IDs CHEMBL4250651, CHEMBL4238919, CHEMBL3286436, CHEMBL3403255; reference drug moxifloxacin, PubChem CID 152946. Structures: PDB 5BS8 (2.4 Å) and PDB 3M4I (1.95 Å). Target: UniProtKB P9WG45; ChEMBL target CHEMBL3430898. No additional data were generated.
