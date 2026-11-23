# PC190723 Re-Docks at −9.43 kcal/mol on Its Own FtsZ Structure 4DXD — but the Pipeline Docked It into the GDP Pocket, and ChEMBL Resolved FtsZ to a Human Enzyme

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent laboratory verification. Do not cite as established evidence.**

**Author:** Zubair Ali, Pharm-D student, Shaheed Mohtarma Benazir Bhutto Medical University (SMBBMU), Larkana, Pakistan
**Drafting assistant:** Lapis (AI)
**Date:** 2026-11-23 · **Health Papers Agent — Paper #101** (daily 5-paper run)

**Keywords:** Staphylococcus aureus; FtsZ; PC190723; MRSA; molecular docking; ChEMBL; cell division; antimicrobial resistance

---

## Abstract

Staphylococcus aureus was associated with more than a million deaths in 2019, and methicillin-resistant strains with more than 100,000 deaths directly attributable to resistance — yet no FtsZ inhibitor has reached the clinic. FtsZ, the essential bacterial GTPase that builds the Z-ring at the division site, is the target of PC190723, a 2,6-difluorobenzamide that stabilises FtsZ polymers, suppresses its GTPase activity, and kills staphylococci at a minimum inhibitory concentration of 1 µg/mL against both methicillin-sensitive and methicillin-resistant strains. We asked whether any measured FtsZ ligand binds the interdomain cleft more strongly than PC190723. The LeadForge pipeline resolved the target correctly to UniProtKB P0A029 (S. aureus FtsZ) — and then failed twice: ChEMBL resolved to CHEMBL2074, verified live as human maltase-glucoamylase, so zero bioactivities were returned and no comparison set exists; and the pipeline's PDB picker selected 3VOA, the GDP-form of FtsZ, whose centre is the nucleotide site, not the PC190723 cleft — its −8.83 kcal/mol score is a docking into the GDP pocket and is discarded here as a measurement of the wrong site. On the correct structure, the 2.0 Å crystal structure of S. aureus FtsZ in complex with PC190723 (PDB 4DXD), PC190723 re-docked at −9.43 kcal/mol (poses −9.43, −9.37, −9.16) centred exactly on the co-crystallised ligand 9PC (centre audit via dock._ligand_center, which correctly excluded the 28-atom GDP cofactor in favour of the 23-atom inhibitor). The paper's finding is therefore a validated control plus two honest negatives: the method recovers strong, tight binding for the drug in its own cleft, but the "does any analogue beat PC190723" question cannot be answered from ChEMBL as queried, and the pipeline's structure picker cannot be trusted when a structure holds both a nucleotide and an inhibitor. The falsifiable next step is a GTPase-plus-polymerisation assay of PC190723 against its own published MIC, with the 4DXD pose as the structural hypothesis — not another docking run.

---

## 1. Introduction

FtsZ is the most conserved protein in bacteria and archaea, and the first protein to arrive at the future division site, where it polymerises in a GTP-dependent manner into the Z-ring that recruits the divisome and guides septum synthesis. It is a structural homologue of eukaryotic tubulin, and its inhibitors work by the same logic as taxol: not by blocking assembly, but by stabilising polymers against disassembly. PC190723 — 3-[(6-chloro[1,3]thiazolo[5,4-b]pyridin-2-yl)methoxy]-2,6-difluorobenzamide — was built from the weak fragment 3-methoxybenzamide through 2,6-difluoro-3-alkyloxybenzamide optimisation, gaining roughly 8,000-fold in potency over the parent fragment, and it inhibits S. aureus at a minimum inhibitory concentration of 1 µg/mL against both methicillin-sensitive and methicillin-resistant strains. It binds the cleft between the N-terminal GTP-binding subdomain and the C-terminal subdomain — the pocket mapped by resistance mutations, the taxol-site equivalent in tubulin — where it stabilises single-stranded filaments into bundles, coils and toroids, reduces GTPase activity, and suppresses the polymer dynamics that division requires. It does not affect Escherichia coli, whose FtsZ is not susceptible, which is the Gram-positive selectivity question that has followed the class ever since.

The clinical case for the target is the synergy, not the single agent. PC190723 acts synergistically with β-lactam antibiotics in vitro and in vivo: in a murine model of MRSA infection the combination was efficacious, fluorescence microscopy showed the concomitant delocalisation of FtsZ and its β-lactam target PBP2, and combining PC190723 with imipenem markedly reduced the spontaneous frequency of PC190723-resistant mutants — while the resistant mutants that did arise showed attenuated virulence and restored β-lactam susceptibility. That is the design logic for a combination agent: the inhibitor's own resistance problem is mitigated by the partner drug. Despite that, no FtsZ inhibitor has reached the clinic: the benzamide class has struggled with pharmacological properties and a relatively high frequency of resistance mutations, and only one prodrug analogue, TXA709, was designated a Qualified Infectious Disease Product for S. aureus infections and has completed a phase I clinical trial. The question this paper asks is the standard one for this series: among compounds with measured FtsZ potency already in ChEMBL, does any bind the interdomain cleft more strongly than PC190723 — and can the pipeline even ask that question correctly?

The classical medical canon knows the wound, not the bacterium: Ibn Sina's Canon of Medicine (c. 1025) treats wounds, abscesses and putrefaction with drainage and dressings — the syndrome, not the target. The principle carried forward here is hifz al-nafs, preservation of life (see §7).

**Falsifiable question.** Do ChEMBL ligands with measured S. aureus FtsZ potency bind the interdomain cleft of the PC190723-bound structure (PDB 4DXD) at scores beyond re-docked PC190723, and would that binding translate into stronger FtsZ inhibition and antistaphylococcal activity? **Falsifier:** a GTPase or polymerisation assay showing an IC50 worse than the analogue's published value, or a whole-cell MIC above 4 µg/mL against MRSA, refutes the claim for that compound. **Causal identification:** validated-control re-docking — the reference inhibitor re-docked on a co-crystal structure of its own target, with the co-crystallised inhibitor as the centre — not a comparison against nothing. Association only beyond that: docking scores are not activity.

## 2. Methods

### 2.1 Literature basis

Searched 2026-11-23: the PC190723 discovery paper (Haydon et al., Science 2008;321:1673–1675; doi:10.1126/science.1159961); the FtsZ polymer-stabilisation mechanism (J Biol Chem 2010); the MRSA synergy and 4DXD structure paper (Tan et al., Sci Transl Med 2012;4:126ra35; PMID 22440737; doi:10.1126/scitranslmed.3003592); the SaFtsZ conformational-change structures (Matsui et al., Acta Crystallogr D Biol Crystallogr 2012;68:1175–1188; PMID 22948918); the allosteric-site fluorescence-polarisation screen and TXA709 phase I status (J Med Chem 2021; doi:10.1021/acs.jmedchem.0c02207); the 2,6-difluorobenzamide structure–activity review (ChemMedChem 2017;12:1303–1318); the global antimicrobial-resistance burden analysis (Antimicrobial Resistance Collaborators, Lancet 2022;399:629–655); and the RCSB records for PDB 4DXD and 3VOA.

### 2.2 Target identification

The pipeline resolved the target to UniProtKB P0A029 (cell division protein FtsZ, Staphylococcus aureus strain Mu50 / ATCC 700699), verified live 2026-11-23. This is the correct target. What failed was the ChEMBL resolution: the pipeline selected CHEMBL2074, verified live as "Maltase-glucoamylase", SINGLE PROTEIN, Homo sapiens — a human digestive enzyme with nothing to do with bacterial cell division. The standing fix for this series is now to verify the ChEMBL target's name and organism before any ligand retrieval is trusted.

### 2.3 The pipeline's two failures, stated not smoothed over

First, ChEMBL bioactivity retrieval for the wrong target CHEMBL2074 returned zero records (step 2: `no_data`, count 0). No known ligands with measured potency were retrieved, so the similarity screen was skipped and the only "lead" ranked was the query compound itself, PC190723 (score 99.2). There is therefore no comparison set in this run, and the question "does any analogue beat PC190723" has no computational answer here. That is a data-retrieval failure, not a finding about PC190723.

Second, the pipeline's PDB picker selected 3VOA and docked PC190723 on it at −8.83 kcal/mol. Verified live 2026-11-23, 3VOA is the GDP-form of SaFtsZ (residues 12–316), 1.73 Å — the structure that shows the straight, GDP-bound conformation, with no inhibitor bound. The centre the pipeline used is the GDP nucleotide site: PC190723 was docked into the GTP/GDP pocket, ~25 Å from the interdomain cleft where it actually binds. A −8.83 kcal/mol score for a cleft binder in the nucleotide pocket is a property of the wrong site and is discarded in full: it appears in this paper only as the artefact it is, with its file reference, so that no reader mistakes it for a result. The same structure-picker error has now bitten this series three times in two days (Papers #95, #100, #101), and the lesson is the same: the picked PDB entry's title and bound ligands must be verified by hand, every run.

### 2.4 Molecular docking — the redock on the correct structure

The benchmark structure is 4DXD: the 2.0 Å crystal structure of S. aureus FtsZ in complex with PC190723 (Tan et al., Sci Transl Med 2012). A targeted redock script (`health-papers-agent/redock_hp090_4dxd.py`) docked PC190723 on 4DXD using standardised AutoDock Vina 1.2.7, exactly as Papers #1/#3: grid centre the centroid of the co-crystallised PC190723 (ligand 9PC, 23 heavy atoms — C14H8ClF2N3O2S, matching PC190723), [−13.76, 41.85, 18.24], verified by direct computation from the PDB file with `dock._ligand_center`. The centre audit is the decisive check here: the file also holds a 28-atom GDP cofactor, and a naive largest-group pick would have centred on GDP ([5.03, 20.08, 21.23]) — the nucleotide site again. `dock._ligand_center` correctly excluded the GDP cofactor and returned the 9PC centroid, which is why this redock measures the cleft and the pipeline's 3VOA run did not. Box 22.5 Å, exhaustiveness 8, best of 3 poses reported. The receptor preparation keeps the GDP ATOM records, so the nucleotide pocket stays occupied and the cleft geometry is realistic. PC190723 is therefore the self-dock control on its own structure: a method that could not recover strong binding for the drug in the cleft it was crystallised in would be broken. The docked PC190723 is the parent SMILES as returned by PubChem (CID 25016417); the crystal holds the same molecule, so no prodrug/metabolite caveat applies here.

### 2.5 PAINS screen

RDKit PAINS filter applied to PC190723. PAINS-clean: no alerts. No PAINS alert is hidden anywhere in this paper; there is none to hide.

### 2.6 ADMET and toxicity read-across

RDKit descriptors computed for PC190723: molecular weight 355.75, logP 3.3, 1 hydrogen-bond donor, 5 acceptors, TPSA 78.1 Å², 4 rotatable bonds, 0 Lipinski violations, Lipinski pass and Veber pass. ToxGuard Tox21 kNN read-across (12 assays) for PC190723: maximum predicted probability 0.168 (NR-AhR), a weak read-across (maximum neighbour similarity 0.279), not a measurement, and it does not clear the compound for development — it is the profile of an investigational compound, reported for completeness.

### 2.7 Honesty limits

Docking ≠ activity. Vina noise is ±1–2 kcal/mol. No molecular dynamics or free-energy refinement was run. No experimental data exist for any compound in this study beyond PC190723's published MIC. There is no comparison set: ChEMBL returned zero bioactivities for the wrongly resolved target, so the benchmark question is unanswered, not answered in the negative. One rigid structure was used (4DXD, 2.0 Å); FtsZ undergoes marked conformational change between curved and straight forms, so one structure under-samples the binding landscape. The docked compound is PC190723 itself, not its prodrug TXA709, which is the molecule that actually entered phase I.

## 3. Results

### 3.1 Docking: the comparison table (4DXD, 2.0 Å — the drug's own structure)

| Compound | Measured potency (published) | Best affinity, 4DXD (kcal/mol) | Top-3 poses (kcal/mol) | Median pose |
|---|---|---|---|---|
| PC190723 (reference) | MIC 1 µg/mL vs MSSA and MRSA | −9.43 | −9.43, −9.37, −9.16 | −9.37 |
| (no comparison ligands — ChEMBL resolved to human maltase-glucoamylase, 0 bioactivities) | — | — | — | — |

PC190723 re-docks at −9.43 kcal/mol on its own structure, with tight pose consistency (−9.43, −9.37, −9.16): the method recovers strong binding for the drug in the cleft it was crystallised in, so the protocol is not broken. There is no analogue to compare it against, so no "beats PC190723" claim can be made in either direction. The discarded pipeline score (−8.83 kcal/mol on 3VOA, the GDP-form, centred on the nucleotide site) is not in the table, because it is not a measurement of this site.

### 3.2 Comparison with published data

No published Vina study of PC190723 on 4DXD was found in the sweep; the comparison here is internal (the inhibitor re-docked on its own structure, same protocol as Papers #1/#3). The structural literature is the published ground truth for the binding mode: the 4DXD structure shows PC190723 in the cleft between the N- and C-terminal subdomains, the site where the predominant resistance mutations map, and the Matsui structures show the same protein in apo and GDP-bound forms undergoing the curved-to-straight reorganisation that the inhibitor exploits. The mechanism literature gives the paper its most useful context: PC190723 is a polymer stabiliser in the taxol mould, and the 2021 fluorescence-polarisation screen finally supplied the competitive binding assay the field had lacked for the allosteric site — the tool that makes a real comparison set possible in future work.

### 3.3 The clinical confounder that docking cannot see

PC190723's clinical story is the paper's most important context, and docking cannot see any of it. The drug's value was never its single-agent MIC — it was the synergy: with a β-lactam partner it delocalised both FtsZ and PBP2, worked in a murine MRSA model, and cut the frequency of its own resistant mutants. And its failure was never its affinity — it was pharmaceutical properties and the frequency of resistance mutations in the cleft, which is why the class's only clinical advance is the prodrug TXA709, not a better binder. A compound that out-scores PC190723 here by 1 kcal/mol but keeps the same resistance frequency and the same poor properties would be no advance at all, and docking on a wild-type structure cannot tell the two apart. The docking order cannot explain why no FtsZ inhibitor has reached the clinic; the properties and the resistance data together can.

## 4. Discussion

### 4.1 The reframe

The question this paper can ask has changed since PC190723 was published. Before 2008, the question was "can FtsZ be drugged at all?" — now it is "which molecule, if any, beats PC190723 in the cleft *and* survives the properties and resistance tests that stopped the class?" The benchmark is therefore a screen for successors with a three-part bar: beat −9.43 kcal/mol on 4DXD, keep a low resistance frequency, and fix the pharmaceutical properties. This paper supplies the first part of the bar and shows the second and third parts are where the work is: the comparison set does not exist in ChEMBL as queried, and the structure picker chose the nucleotide site.

### 4.2 Why the "win" must not be over-read

There is no win to over-read. Three reasons the paper is a control plus two negatives, not a discovery. First, there is no comparison set — ChEMBL resolved to a human enzyme and returned zero bioactivities. Second, the pipeline's first structure was the GDP-form and its −8.83 kcal/mol score measured the wrong site, and that score must be discarded, not averaged in. Third, even the valid re-dock is a single rigid structure, and FtsZ's curved-to-straight reorganisation means one structure under-samples the cleft.

### 4.3 The pipeline failure is the experiment's design constraint, not a reason to stop

The two failures have different root causes and the same fix. The ChEMBL failure is a name-resolution error (FtsZ → maltase-glucoamylase); the structure failure is a bound-ligand error (GDP-form picked over the inhibitor complex). The fix, now standing practice for this series: verify the ChEMBL target's name and organism before ligand retrieval, and verify the picked PDB entry's title and bound ligands by hand before any score is reported — with a centre audit that names the ligand the centre came from, as this redock does. A pipeline that docks the right drug into the wrong site and reports the number is worse than a pipeline that reports nothing — this paper reports the nothing, with the artefact named.

### 4.4 Mechanism

PC190723 binds the interdomain cleft between the N- and C-terminal subdomains of FtsZ, stabilises single-stranded filaments into bundles and toroids, reduces GTPase activity, and suppresses the polymer dynamics the Z-ring needs to constrict — the taxol parallel on the bacterial tubulin homologue. Test for each link: (i) a GTPase assay (phosphate release, with PC190723 as the comparator) measures inhibition directly against the published mechanism; (ii) a polymerisation assay (light scattering or electron microscopy) measures filament stabilisation and bundling; (iii) a whole-cell MIC assay against MSSA and MRSA measures antistaphylococcal activity at matched concentration, with a cytotoxicity counter-screen; (iv) a resistance-frequency assay (spontaneous mutant frequency, with and without imipenem) measures whether a candidate kept the combination logic that defines the class.

### 4.5 Testable hypotheses

1. PC190723 inhibits S. aureus FtsZ GTPase activity in vitro with an IC50 within 3-fold of its published mechanism, and kills MRSA at an MIC within 2-fold of 1 µg/mL. Falsifier: MIC > 4 µg/mL against MRSA.
2. A candidate benzamide that out-scores PC190723 on 4DXD keeps a spontaneous resistance frequency no higher than PC190723's, alone and with imipenem. Falsifier: resistance frequency >10-fold higher than PC190723's.
3. The 4DXD pose predicts the resistance profile: a candidate whose docked pose loses contact with the cleft residues where resistance mutations map loses activity against the corresponding PC190723-resistant mutants first. Falsifier: a candidate without those contacts keeps wild-type potency against the mutants.

### 4.6 Proposed validation (university-lab feasible, 8–12 weeks)

Stage 1 (weeks 1–3): fix the pipeline query (verify ChEMBL target name and organism; hand-verify PDB title and bound ligands with a centre audit) and re-run the ligand retrieval for S. aureus FtsZ to build the comparison set this paper could not — five ChEMBL FtsZ ligands with measured potency, docked on 4DXD at the audited centre, plus the 2021 fluorescence-polarisation assay as the binding readout. Stage 2 (weeks 4–8): GTPase plus polymerisation assay for PC190723 against its published mechanism, plus the best-scoring candidate from stage 1, on wild-type SaFtsZ. Stage 3 (weeks 9–12): if any candidate passes stages 1–2, MIC assay against MSSA and MRSA plus a spontaneous-resistance-frequency assay with and without imipenem; if none passes, publish the negative result with the docking data as the reason the hypothesis failed. No animal work is proposed at this stage.

## 5. Limitations

1. Docking only; no experimental data in this study. Vina noise ±1–2 kcal/mol swallows any margin under ~2 kcal/mol.
2. There is no comparison set: ChEMBL resolved to human maltase-glucoamylase and returned zero bioactivities, so the benchmark question is unanswered.
3. The pipeline's first structure (3VOA) was the GDP-form; the −8.83 kcal/mol score on it measured the nucleotide site, not the cleft, and is discarded — the centre audit is what separates the two.
4. One rigid structure was used (4DXD, 2.0 Å); FtsZ reorganises markedly between curved and straight forms, so one structure under-samples the cleft.
5. Docking was on the wild-type structure only; the resistance-mutation question — the one that stopped the class clinically — was not docked, because no mutant FtsZ structure with a candidate ligand was in the comparison set.
6. No data on the clinical confounder: docking cannot distinguish the 1 µg/mL MIC from the pharmaceutical-properties and resistance-frequency problems that kept the class out of the clinic, or the Gram-positive selectivity question (E. coli FtsZ is not susceptible).
7. The classical-canon sweep found no FtsZ-relevant text: the Canon of Medicine treats wounds and abscesses, not bacteria, so the Islamic-principle discussion rests on hifz al-nafs as a principle, not on a classical source about this target.

## 6. Conclusion

PC190723, the 2,6-difluorobenzamide that stabilises FtsZ polymers and kills staphylococci at 1 µg/mL, re-docks at −9.43 kcal/mol on its own 2.0 Å structure 4DXD with tight pose consistency and no PAINS alert — a validated control, not a discovery. No analogue can be claimed to beat it or lose to it: ChEMBL resolved the target to a human digestive enzyme and returned zero bioactivities, so there is no comparison set, and the pipeline's first structure was the GDP-form of FtsZ, whose −8.83 kcal/mol score measured the nucleotide site and is discarded as a measurement of the wrong site. The paper's useful result is therefore the control plus the two named failures, and the centre audit that proves the difference: the same file holds a 28-atom GDP and a 23-atom inhibitor, and the centre used here is the inhibitor's, not the nucleotide's. What the docking cannot do is resolve the resistance and properties questions that define this class: the same cleft that binds PC190723 at −9.43 kcal/mol is the cleft whose mutations defeat it, and only a GTPase-plus-MIC assay with a resistance-frequency readout can tell whether a successor keeps the combination logic that made PC190723 interesting. The next step is the cheap, decisive test — fix the query, build the comparison set, and run a GTPase plus MIC assay with a resistance-frequency readout — not another docking run on an unverified structure.

## 7. Policy implications

**Decision-maker:** Pakistan's Drug Regulatory Authority (DRAP) and the National Institute of Health's antimicrobial-resistance programme, with the SMBBMU ORIC office as the local route. **Decision:** whether to fund a small, targeted validation of FtsZ inhibition as an academic drug-discovery exercise, and whether to prioritise β-lactam combination strategies for MRSA in procurement. **Exact change:** commission the 8–12-week pipeline-fix plus GTPase screen proposed in §4.6 for the five best ChEMBL FtsZ ligands against PC190723, instead of funding another purely computational screen of the same target on unverified structures; and, in parallel, ask the AMR programme to note explicitly that the binding question is settled for the wild-type cleft — PC190723 re-docks at −9.43 kcal/mol — and that the remaining gap is the resistance frequency and the properties, not the drug's affinity: every rupee spent re-docking PC190723 into the GDP pocket is a rupee not spent testing candidates against the resistance mutants. **If evidence Z appears, reverse this:** if a candidate beats PC190723's re-dock by >2 kcal/mol on 4DXD and keeps a resistance frequency no higher than PC190723's with imipenem, drop the access-only framing and fund the candidate's development; if the fixed query returns no candidate within noise of PC190723, drop this ligand set and redirect the same screen to the next FtsZ chemotypes — do not proceed to any animal or clinical work on docking scores alone. The Islamic principle is hifz al-nafs (preservation of life, a maqsad of the Sharia): where a cheap test can distinguish a usable FtsZ inhibitor from a useless one for a pathogen associated with more than a million deaths a year, running the test is the obligation; prescribing on an untested docking score would violate it. The evidence here is thin — docking only, and a single-compound control at that — so the recommendation is "run the trial", not "do the policy".

## Acknowledgments

This manuscript was prepared with AI assistance (Lapis) for drafting, literature search and docking computations. The author reviewed the manuscript and takes responsibility for its content. No funding was received. The author declares no conflicts of interest.

## References

1. Antimicrobial Resistance Collaborators. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399:629-655.
2. Haydon DJ, et al. An inhibitor of FtsZ with potent and selective anti-staphylococcal activity. Science. 2008;321:1673-1675. doi:10.1126/science.1159961.
3. The antibacterial cell division inhibitor PC190723 is an FtsZ polymer-stabilizing agent that induces filament assembly and condensation. J Biol Chem. 2010.
4. Tan CM, et al. Restoring methicillin-resistant Staphylococcus aureus susceptibility to beta-lactam antibiotics. Sci Transl Med. 2012;4:126ra35. doi:10.1126/scitranslmed.3003592. PMID: 22440737.
5. Matsui T, et al. Structural reorganization of the bacterial cell-division protein FtsZ from Staphylococcus aureus. Acta Crystallogr D Biol Crystallogr. 2012;68:1175-1188. PMID: 22948918.
6. Targeting the FtsZ allosteric binding site with a novel fluorescence polarization screen, cytological and structural approaches for antibacterial discovery. J Med Chem. 2021. doi:10.1021/acs.jmedchem.0c02207.
7. 2,6-Difluorobenzamide inhibitors of the bacterial cell division protein FtsZ: design, synthesis and structure-activity relationship study. ChemMedChem. 2017;12:1303-1318.
8. RCSB PDB entry 4DXD: Staphylococcus aureus FtsZ in complex with PC190723, 2.0 Å. RCSB Protein Data Bank. Accessed 2026-11-23.
9. RCSB PDB entry 3VOA: Staphylococcus aureus FtsZ 12-316 GDP-form, 1.73 Å. RCSB Protein Data Bank. Accessed 2026-11-23.
10. ChEMBL target CHEMBL2074: Maltase-glucoamylase, Homo sapiens. ChEMBL database, European Bioinformatics Institute. Accessed 2026-11-23. (Wrong target for S. aureus FtsZ; zero bioactivities returned.)
11. UniProtKB P0A029: Cell division protein FtsZ, Staphylococcus aureus (strain Mu50 / ATCC 700699). UniProt. Accessed 2026-11-23.
12. PubChem CID 25016417: PC190723. National Library of Medicine. Accessed 2026-11-23.
13. Ibn Sina. Al-Qanun fi al-Tibb (Canon of Medicine). c. 1025. (Classical source; treats wounds and abscesses, not bacteria — cited for the hifz al-nafs principle only.)

## Data availability

All docking scores reported here are in `hidden_files/dock-HP-090-4dxd-2026-11-23.json` (PC190723 on 4DXD) and `hidden_files/dock-HP-090-2026-11-23.json` (P0A029 pipeline run, including the discarded 3VOA docking step). Reference inhibitor PC190723 (PubChem CID 25016417). Structure: PDB 4DXD (2.0 Å); discarded structure PDB 3VOA (GDP-form). Target: UniProtKB P0A029; ChEMBL target CHEMBL2074 (human maltase-glucoamylase — wrong target; zero bioactivities). No additional data were generated.
