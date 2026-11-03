# Health Papers Agent — Topic Pool

Seed pool for the daily 5/day Health Papers Agent. Source of truth is `topics-pool.json` — this file is generated from it; do not edit by hand (regenerate after pool changes).

Total topics: **60** · Areas: diabetes-metabolic, antimicrobial-resistance, tuberculosis, malaria-parasitic, oncology, antiviral, cardiovascular-renal, inflammation-pain, pakistan-burden · Updated 2026-11-03

Excluded by design (already covered by Papers #1–#4): thymoquinone/aldose-reductase, dual AR+SGLT2, GLP-1/Parkinson's BBB, p-tau217.


## diabetes-metabolic (10)

- **HP-001** — DPP-4 inhibition for type 2 diabetes — new scaffolds beyond gliptins · Target: Dipeptidyl peptidase-4 (DPP-4) · Ref: sitagliptin · Angle: Screen natural-product / repurposed leads against DPP-4; compare vs sitagliptin under the standardised protocol · *unused*
- **HP-002** — PPAR-gamma agonism without weight gain / oedema · Target: Peroxisome proliferator-activated receptor gamma (PPAR-gamma) · Ref: pioglitazone · Angle: Test partial-agonist scaffolds (including thymoquinone analogues on this NEW target) vs pioglitazone; PAINS screen mandatory · *unused*
- **HP-003** — PTP1B inhibition for insulin resistance — no approved drug yet · Target: Protein tyrosine phosphatase 1B (PTP1B) · Ref: ertiprotafib (failed, reference only) · Angle: Dock candidate leads vs PTP1B; honest note that no approved PTP1B drug exists, so the comparator is a literature inhibitor · *unused*
- **HP-004** — Alpha-glucosidase inhibition for postprandial glucose control · Target: Alpha-glucosidase (maltase-glucoamylase) · Ref: acarbose · Angle: Screen plant-derived leads (e.g. berberine analogues) vs acarbose · *unused*
- **HP-005** — Pancreatic alpha-amylase inhibition — dietary adjuncts for diabetes · Target: Human pancreatic alpha-amylase · Ref: acarbose · Angle: Test polyphenol / flavonoid leads vs acarbose; state bioavailability limits honestly · *unused*
- **HP-006** — SGLT2 inhibition with a novel scaffold (SGLT2-only, not the dual AR+SGLT2 angle of Paper #3) · Target: Sodium-glucose cotransporter 2 (SGLT2) · Ref: dapagliflozin · Angle: Dock a novel ChEMBL scaffold vs dapagliflozin on SGLT2 only; must state the Paper #3 polyol-escape caveat · *unused*
- **HP-007** — Glucokinase activation for type 2 diabetes · Target: Glucokinase (GCK) · Ref: dorzagliatin · Angle: Test glucokinase activator leads vs dorzagliatin; note hypoglycaemia risk class-wide · *unused*
- **HP-008** — 11beta-HSD1 inhibition for metabolic syndrome · Target: 11beta-hydroxysteroid dehydrogenase type 1 · Ref: INCB13739 (investigational, reference only) · Angle: Dock leads vs 11beta-HSD1; honest note: no approved drug in class · *unused*
- **HP-009** — Xanthine oxidase inhibition for gout — safer than allopurinol in CKD · Target: Xanthine oxidase · Ref: febuxostat · Angle: Screen leads vs febuxostat; note cardiovascular warning on febuxostat · *unused*
- **HP-010** — HMG-CoA reductase — statin alternatives for statin-intolerant patients · Target: HMG-CoA reductase · Ref: atorvastatin · Angle: Dock non-statin scaffolds vs atorvastatin; state that LDL-lowering needs clinical data, docking is only triage · *unused*

## antimicrobial-resistance (7)

- **HP-011** — NDM-1 metallo-beta-lactamase — carbapenem resistance · Target: New Delhi metallo-beta-lactamase 1 (NDM-1) · Ref: meropenem (failing drug — shows the gap) · Angle: Screen metal-chelating / non-chelating leads vs NDM-1; compare with meropenem binding as the negative control · *unused*
- **HP-012** — KPC carbapenemase in Klebsiella pneumoniae · Target: Klebsiella pneumoniae carbapenemase (KPC-2) · Ref: ceftazidime-avibactam · Angle: Dock leads vs KPC-2; compare vs avibactam acylation site · *unused*
- **HP-013** — MRSA PBP2a — beta-lactam resistance · Target: Penicillin-binding protein 2a (PBP2a) · Ref: ceftaroline · Angle: Dock leads vs PBP2a allosteric site; compare vs ceftaroline · *unused*
- **HP-014** — E. coli DHFR — trimethoprim resistance · Target: Escherichia coli dihydrofolate reductase (DHFR) · Ref: trimethoprim · Angle: Dock leads vs wild-type and trimethoprim-resistant DHFR mutants; state resistance-mutation limits · *unused*
- **HP-015** — DNA gyrase — fluoroquinolone resistance in Gram-negatives · Target: DNA gyrase (GyrB subunit) · Ref: ciprofloxacin · Angle: Dock leads vs GyrB ATP site; compare vs ciprofloxacin (different site — state this honestly) · *unused*
- **HP-016** — AmpC beta-lactamase — cephalosporin resistance · Target: AmpC beta-lactamase (Enterobacter) · Ref: ceftazidime · Angle: Screen leads vs AmpC; compare vs ceftazidime hydrolysis · *unused*
- **HP-017** — H. pylori urease — antibiotic-free eradication angle · Target: Helicobacter pylori urease · Ref: clarithromycin (regimen drug, not a urease inhibitor — state this) · Angle: Dock urease inhibitors vs the nickel active site; honest note that eradication needs clinical regimens · *unused*

## tuberculosis (4)

- **HP-018** — InhA — isoniazid resistance in Mycobacterium tuberculosis · Target: M. tuberculosis enoyl-ACP reductase (InhA) · Ref: isoniazid · Angle: Dock direct InhA inhibitors (no KatG activation needed) vs isoniazid; note KatG-mutant resistance bypass · *unused*
- **HP-019** — DprE1 — next-generation TB drugs · Target: M. tuberculosis DprE1 · Ref: macozinone (BTZ043, investigational) · Angle: Dock leads vs DprE1; compare vs macozinone; honest note: investigational comparator · *unused*
- **HP-020** — Mtb ATP synthase — bedaquiline resistance · Target: M. tuberculosis ATP synthase (AtpE) · Ref: bedaquiline · Angle: Dock leads vs AtpE; compare vs bedaquiline; note QT-prolongation class warning · *unused*
- **HP-021** — Mtb CYP51 — sterol biosynthesis as a TB target · Target: M. tuberculosis CYP51 (sterol 14alpha-demethylase) · Ref: posaconazole (repurposed comparator) · Angle: Dock azole / non-azole leads vs CYP51; state repurposing limits · *unused*

## malaria-parasitic (5)

- **HP-022** — PfATP4 — next-generation antimalarials beyond artemisinin · Target: Plasmodium falciparum PfATP4 · Ref: cipargamin (KAE609, investigational) · Angle: Dock leads vs PfATP4; note: no experimental PfATP4 structure existed at last check — honest 'no structure' handling if still true · *unused*
- **HP-023** — PfDHFR — pyrimethamine resistance · Target: Plasmodium falciparum dihydrofolate reductase (DHFR) · Ref: pyrimethamine · Angle: Dock leads vs wild-type and quadruple-mutant PfDHFR; state mutation panel used · *unused*
- **HP-024** — Trypanothione reductase — leishmaniasis drug target · Target: Leishmania trypanothione reductase · Ref: miltefosine · Angle: Dock leads vs trypanothione reductase; compare vs miltefosine (different mechanism — state this) · *unused*
- **HP-025** — T. cruzi CYP51 — Chagas disease · Target: Trypanosoma cruzi CYP51 · Ref: posaconazole · Angle: Dock leads vs T. cruzi CYP51; note clinical failure of posaconazole in Chagas — the target itself is questioned · *unused*
- **HP-026** — Schistosoma TGR — praziquantel alternatives · Target: Schistosoma mansoni thioredoxin glutathione reductase (TGR) · Ref: praziquantel · Angle: Dock leads vs TGR; compare vs praziquantel (different target — state this honestly) · *unused*

## oncology (13)

- **HP-027** — EGFR T790M/C797S — osimertinib resistance in NSCLC · Target: Epidermal growth factor receptor (EGFR, mutant) · Ref: osimertinib · Angle: Dock leads vs EGFR C797S mutant; compare vs osimertinib; state covalent-vs-reversible difference · *unused*
- **HP-028** — HER2-positive breast cancer — lapatinib alternatives · Target: Human epidermal growth factor receptor 2 (HER2) · Ref: lapatinib · Angle: Dock leads vs HER2 kinase domain; compare vs lapatinib · *unused*
- **HP-029** — BRAF V600E melanoma — vemurafenib resistance · Target: BRAF V600E · Ref: vemurafenib · Angle: Dock leads vs BRAF V600E; compare vs vemurafenib; note paradoxical activation risk · *unused*
- **HP-030** — FLT3-ITD acute myeloid leukaemia · Target: FMS-like tyrosine kinase 3 (FLT3) · Ref: gilteritinib · Angle: Dock leads vs FLT3-ITD; compare vs gilteritinib · *unused*
- **HP-031** — VEGFR2 — anti-angiogenic scaffolds · Target: Vascular endothelial growth factor receptor 2 (VEGFR2) · Ref: sorafenib · Angle: Dock leads vs VEGFR2; compare vs sorafenib · *unused*
- **HP-032** — BCR-ABL T315I — imatinib resistance in CML · Target: BCR-ABL1 T315I · Ref: ponatinib · Angle: Dock leads vs T315I gatekeeper mutant; compare vs ponatinib; note cardiovascular warning on ponatinib · *unused*
- **HP-033** — ALK-positive NSCLC — next-generation inhibitors · Target: Anaplastic lymphoma kinase (ALK) · Ref: alectinib · Angle: Dock leads vs ALK; compare vs alectinib · *unused*
- **HP-034** — CDK4/6 — breast cancer cell-cycle inhibition · Target: Cyclin-dependent kinases 4/6 (CDK4/6) · Ref: palbociclib · Angle: Dock leads vs CDK6; compare vs palbociclib; note neutropenia class effect · *unused*
- **HP-035** — PARP1 — synthetic lethality in BRCA-mutant cancers · Target: Poly(ADP-ribose) polymerase 1 (PARP1) · Ref: olaparib · Angle: Dock leads vs PARP1; compare vs olaparib; note PARP-trapping vs catalytic inhibition · *unused*
- **HP-036** — Androgen receptor — enzalutamide resistance in prostate cancer · Target: Androgen receptor (ligand-binding domain) · Ref: enzalutamide · Angle: Dock leads vs AR-LBD including F876L mutant; compare vs enzalutamide · *unused*
- **HP-056** — Aromatase inhibition — breast cancer endocrine therapy · Target: Aromatase (CYP19A1) · Ref: letrozole · Angle: Dock leads vs aromatase haem site; compare vs letrozole · *unused*
- **HP-057** — MEK1/2 — BRAF-mutant combination therapy · Target: MEK1/2 (MAP2K1/2) · Ref: trametinib · Angle: Dock leads vs MEK1 allosteric pocket; compare vs trametinib · *unused*
- **HP-058** — mTOR — rapalog alternatives · Target: Mechanistic target of rapamycin (mTOR, kinase domain) · Ref: everolimus · Angle: Dock ATP-competitive leads vs mTOR kinase domain; compare vs everolimus (allosteric — different site, state this) · *unused*

## antiviral (6)

- **HP-037** — SARS-CoV-2 main protease — nirmatrelvir alternatives · Target: SARS-CoV-2 main protease (Mpro / 3CLpro) · Ref: nirmatrelvir · Angle: Dock leads vs Mpro; compare vs nirmatrelvir; note ritonavir-boosting is a PK fix, not a target fix · *unused*
- **HP-038** — Influenza neuraminidase — oseltamivir resistance · Target: Influenza A neuraminidase (N1) · Ref: oseltamivir · Angle: Dock leads vs N1 including H274Y mutant; compare vs oseltamivir · *unused*
- **HP-039** — HIV-1 integrase — dolutegravir resistance · Target: HIV-1 integrase · Ref: dolutegravir · Angle: Dock leads vs integrase strand-transfer site; compare vs dolutegravir · *unused*
- **HP-040** — HCV NS5B polymerase — sofosbuvir alternatives · Target: Hepatitis C virus NS5B polymerase · Ref: sofosbuvir · Angle: Dock leads vs NS5B palm site; compare vs sofosbuvir (nucleotide — different site, state this) · *unused*
- **HP-041** — Dengue NS2B-NS3 protease — no approved dengue drug · Target: Dengue virus NS2B-NS3 protease · Ref: none approved (honest — compare vs literature inhibitors) · Angle: Dock leads vs NS2B-NS3; state plainly there is no approved reference drug · *unused*
- **HP-059** — HBV capsid assembly — functional cure angle · Target: Hepatitis B virus core protein (capsid) · Ref: none approved (compare vs literature capsid modulators) · Angle: Dock leads vs HBV capsid dimer interface; state plainly no approved reference drug exists · *unused*

## cardiovascular-renal (6)

- **HP-042** — ACE inhibition — cough-free alternatives · Target: Angiotensin-converting enzyme (ACE) · Ref: lisinopril · Angle: Dock leads vs ACE zinc site; compare vs lisinopril; note cough is bradykinin-mediated, class-wide · *unused*
- **HP-043** — Neprilysin inhibition for heart failure · Target: Neprilysin (NEP) · Ref: sacubitril · Angle: Dock leads vs neprilysin; compare vs sacubitril (prodrug — dock the active sacubitrilat, state this) · *unused*
- **HP-044** — Factor Xa — oral anticoagulation without routine monitoring · Target: Coagulation factor Xa · Ref: rivaroxaban · Angle: Dock leads vs factor Xa; compare vs rivaroxaban; note bleeding is the class risk · *unused*
- **HP-045** — HIF prolyl-hydroxylase — anaemia of chronic kidney disease · Target: Hypoxia-inducible factor prolyl hydroxylase (HIF-PH) · Ref: roxadustat · Angle: Dock leads vs HIF-PH; compare vs roxadustat; note cardiovascular safety debate · *unused*
- **HP-046** — PCSK9 — small-molecule LDL lowering (beyond antibodies) · Target: Proprotein convertase subtilisin/kexin type 9 (PCSK9) · Ref: evolocumab (antibody — state docking a small molecule vs an antibody target honestly) · Angle: Dock small molecules vs the PCSK9-LDLR interface; compare vs known small-molecule binders, not vs the antibody · *unused*
- **HP-060** — Thrombin — direct oral anticoagulation · Target: Thrombin (factor IIa) · Ref: dabigatran · Angle: Dock leads vs thrombin active site; compare vs dabigatran; note bleeding risk class-wide · *unused*

## inflammation-pain (4)

- **HP-047** — COX-2 selective inhibition without cardiovascular risk · Target: Cyclooxygenase-2 (COX-2) · Ref: celecoxib · Angle: Dock leads vs COX-2 selectivity pocket; compare vs celecoxib and vs COX-1 (selectivity ratio is the point) · *unused*
- **HP-048** — TNF-alpha — oral small-molecule alternatives to biologics · Target: Tumour necrosis factor alpha (TNF-alpha) · Ref: etanercept (biologic — state this; compare vs small-molecule TNF inhibitors in literature) · Angle: Dock small molecules vs the TNF trimer interface; honest note on biologic comparator · *unused*
- **HP-049** — JAK2 — myelofibrosis and inflammatory disease · Target: Janus kinase 2 (JAK2) · Ref: ruxolitinib · Angle: Dock leads vs JAK2; compare vs ruxolitinib; note JAK selectivity (JAK1 vs JAK2) matters · *unused*
- **HP-050** — PDE5 — pulmonary hypertension · Target: Phosphodiesterase 5 (PDE5) · Ref: sildenafil · Angle: Dock leads vs PDE5; compare vs sildenafil; note PDE selectivity (PDE6 vision effects) · *unused*

## pakistan-burden (5)

- **HP-051** — XDR typhoid — ceftriaxone-resistant Salmonella Typhi · Target: Salmonella Typhi DNA gyrase / topoisomerase IV · Ref: azithromycin (current fallback — state resistance is rising) · Angle: Dock leads vs S. Typhi gyrase; Pakistan-burden framing; compare vs azithromycin target (different — state this) · *unused*
- **HP-052** — Cutaneous leishmaniasis — oral alternatives to antimonials · Target: Leishmania major trypanothione reductase · Ref: sodium stibogluconate · Angle: Dock leads vs trypanothione reductase; compare vs antimonial (different mechanism — state this) · *unused*
- **HP-053** — Hepatitis C — affordable NS5A inhibition · Target: Hepatitis C virus NS5A · Ref: daclatasvir · Angle: Dock leads vs NS5A domain I; compare vs daclatasvir; Pakistan HCV-burden framing · *unused*
- **HP-054** — Diabetic kidney disease — aldose-reductase-independent polyol control (NOT the Paper #1/#3 AR angle) · Target: Sorbitol dehydrogenase (SORD) · Ref: none approved (honest — compare vs literature SORD inhibitors) · Angle: Dock leads vs sorbitol dehydrogenase, the second polyol-pathway step; explicitly distinct from Papers #1/#3 (AR, not SORD) · *unused*
- **HP-055** — Beta-thalassaemia — fetal haemoglobin induction · Target: BCL11A / gamma-globin repression pathway (target: BCL11A zinc finger) · Ref: hydroxyurea · Angle: Dock leads vs BCL11A; honest note: HbF induction is transcriptional, docking is only a first triage · *unused*
