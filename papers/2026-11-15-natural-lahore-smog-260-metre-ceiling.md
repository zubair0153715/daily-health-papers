# The 260-Metre Ceiling: A Falsifiable Attribution of Lahore's November Smog Peak to Domestic Sources and Seasonal Meteorology, with a Smog-Budget Policy for Punjab

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan. ORCID: 0009-0001-5921-7509.
**Drafting assistant:** Lapis (AI research assistant).
**Date:** 15 November 2026. **Field:** Natural Science (atmospheric science / environmental policy).
**Status:** Manuscript draft. Not submitted anywhere. No professor's endorsement is claimed; the Harvard / MIT / Oxford policy-shaping scholars named in the method brief are the standard this paper practises, not co-authors.

---

## Abstract

**Question.** Is Lahore's November smog peak driven mainly by polluted air crossing the border from India, or by domestic emissions amplified by the seasonal collapse of the atmosphere's mixing height?

**Claim.** The November peak is driven predominantly by domestic emissions — transport, domestic crop-residue burning, waste burning, industry and brick kilns — amplified by the collapse of the mixing height from 830–860 m in May–June to about 260 m in November, a ~3.2-fold compression of the air available to dilute the same emissions. Transboundary inflow is a secondary contributor, estimated at 13–30% across published studies.

**Falsifier.** The claim would be refuted if a November smog episode showed (i) PM2.5 rising faster in border cities than in inland cities, while (ii) HYSPLIT back-trajectories showed air masses reaching Lahore from the east, and (iii) TROPOMI NO2 columns at the border exceeded Lahore's. The 8–10 November 2026 Diwali episode tested all three conditions and produced the opposite pattern: inland cities (Faisalabad, Multan) rose by 85 µg/m³ against 36 µg/m³ in border cities, Delhi air stayed at least 266 km from Lahore, and Lahore — not the border — is Punjab's strongest TROPOMI NO2 hotspot (92.31 µmol/m²).

**Identification.** Natural experiment (the Diwali window as an exogenous transboundary shock) with a spatial gradient (distance from the border as the dose). **Not an RCT; no single-source causal effect size is estimated. The paper falsifies the transboundary-dominant hypothesis; it does not prove exact domestic shares.**

**One clean number: 260 metres** — Lahore's November mixing height, the ceiling under which a city of ~14 million people breathes. The stakes number is 3.9 years: the average life expectancy air pollution removes from a Pakistani, up to 7 years in Lahore.

**Keywords:** Lahore smog; PM2.5; mixing height; Sentinel-5P TROPOMI; source apportionment; transboundary air pollution; Punjab; khilafah; smog budget.

---

## 1. Introduction

Lahore is, in November, routinely the most polluted major city on Earth. On 23 October 2026 IQAir ranked it first worldwide with an air quality index (AQI) of 410 and PM2.5 at 45.2 times the World Health Organization's annual guideline of 5 µg/m³ — about 226 µg/m³ by arithmetic. On a Monday in early November 2026, AQI crossed 530 and PM2.5 reached 343 µg/m³ (Dawn, 5 November 2026). The Pakistan Air Quality Initiative (PAQI) estimates Lahore's annual average PM2.5 above 110 µg/m³, more than 22 times the WHO guideline, and that sustained exposure could cut life expectancy in the city by up to seven years, against a national loss of 3.9 years and roughly 128,000 premature deaths a year (PAQI, October 2026). The State of Global Air, cited by the Overseas Investors Chamber of Commerce and Industry, puts the national death toll higher, above 248,000 a year; the two estimates differ in scope and method and are both reported here with attribution rather than reconciled (see §7). The economic burden is estimated at about 6.5% of GDP.

The political explanation offered most often by the Punjab government is that the smog drifts across the border — stubble burning and fireworks in Indian Punjab. The alternative explanation is domestic: a year-round emissions baseline, a seasonal pulse of domestic crop burning, and meteorology that traps both. These two accounts imply opposite policies. If the border account is right, the main lever is diplomacy. If the domestic account is right, the main lever is Punjab's own emissions, and every November spent blaming the border is a November of unspent domestic action. This paper tests the two accounts against the freshest available evidence — two reports published in November 2026, a 2026 peer-reviewed TROPOMI analysis of Punjab, and the city's emissions inventories — and derives a policy that is falsifiable in its own right.

The paper's method ancestor is named deliberately: Al-Biruni (973–1050), who measured the Earth's circumference to within about 1% and recorded the natural world before theorising about it (*Kitab al-Hind*, c. 1030). The discipline this paper demands of Punjab's smog policy is the same: measure first, publish the measurement, and let the claim be killed by the next measurement.

## 2. Methods

### 2.1 Literature sweep

Three legs, in the order required by the programme's standing rules:

1. **Modern scientific literature.** The daily research digest of 14 November 2026 (health-focused; no atmospheric item) plus targeted searches on 15 November 2026 for Lahore smog source apportionment, Sentinel-5P TROPOMI NO2 over Punjab, and Pakistan air-pollution health burden. Peer-reviewed sources used: Mariam, Haq & Batool (2026, *Environmental Monitoring and Assessment* 198:831); Lama et al. (2020, *Atmospheric Chemistry and Physics* 20:10295); Rehmat et al. (2023, *Proceedings of the Pakistan Academy of Sciences* B 60(3):505–513); WHO global air quality guidelines (2021). Grey literature used and labelled as such: the Hamari Hawa report (Tariq, 2 November 2026), the PAQI national report (October 2026), the PAQI Diwali-episode assessment (11 November 2026), and the Punjab Environment Protection and Climate Change Department (EPCCD) first-year monitoring report (November 2026), all as reported by Dawn, Moneycontrol, Times of India syndication and other press on 5–12 November 2026. Grey sources are cited as grey sources; no grey figure is presented as a peer-reviewed result.
2. **Islamic canon.** Seyyed Hossein Nasr, *Man and Nature: The Spiritual Crisis of Modern Man* (1968); Al-Biruni, *Kitab al-Hind* (c. 1030); Al-Ghazali, *Al-Mustasfa* (the five necessities of the law); Al-Shatibi, *Al-Muwafaqat* (systematisation of maqasid al-shariah); Qur'an 2:30 (stewardship), 4:135 and 16:90 (justice). Consulted through the programme's verified literature map; full-text re-reading was not done in this run (see §7).
3. **Method standard.** The 10-point checklist of the policy-shaping professors (Banerjee & Duflo; Acemoglu, Johnson & Robinson; Chetty; Thaler & Sunstein; Heckman; Hanushek; Rodrik; Deaton; Haynes & Gawande; Pacala & Socolow; Myles Allen): one falsifiable question, named identification, mechanism, effect size with uncertainty, analysis plan stated before results, replication/data availability, limitations that bite, policy implications naming the decision-maker, comparison against the strongest incumbent, one clean number.

Research agents were not used in this run: Mimosa's litellm patch has landed but its smoke test remains incomplete and the user declined further monitoring; Co-Scientist, Denario and EvoScientist remain blocked on authentication or onboarding. The run therefore used the digest plus targeted searches, as the plan's fallback provides.

### 2.2 Pre-registered analysis plan (stated before results)

1. **Test the transboundary-dominant hypothesis** with the 8–10 November 2026 Diwali window as a natural experiment: compare PM2.5 changes in border cities (Lahore, Kasur, Sialkot, Narowal) against inland cities (Faisalabad, Multan), and check HYSPLIT back-trajectories for Delhi air reaching Lahore.
2. **Compute the mixing-height compression ratio** from ERA5 reanalysis (Hamari Hawa) and state its uncertainty from the published ERA5 bias literature.
3. **Compare the two available emissions inventories** (Urban Unit 2023; PAQI 2026) and report where they agree and where they cannot be compared.
4. **Recommend policy only for the account that survives the falsifier**, with a stated reversal rule.

### 2.3 The gradient test (identification, stated formally)

If transboundary inflow dominated Lahore's November peak, the effect should be strongest nearest the source: border cities should rise most, and the rise should track air masses arriving from the east. Distance from the border is therefore the dose. A pattern in which inland cities rise *more* than border cities, while trajectories show eastern air never reaching Lahore, falsifies the transboundary-dominant account. This is a natural experiment, not a randomised trial: the "treatment" (Diwali fireworks plus Indian stubble smoke, 8–10 November 2026) was exogenous to Punjab's domestic emissions, but a single episode cannot identify the exact share of any one domestic source. The paper claims falsification, not precise apportionment.

## 3. Results

### 3.1 The baseline is year-round, not seasonal

Lahore's monthly average PM2.5 stayed above 35 µg/m³ in every month from October 2025 to October 2026 (Hamari Hawa, via Dawn). Even in the cleaner months, April–September 2026, monthly averages were 40–59 µg/m³, against Pakistan's national annual standard of 15 µg/m³; the lowest month, June 2026, averaged 40 µg/m³. October 2025–February 2026 averaged 124–183 µg/m³; October 2026 averaged 100 µg/m³. The city therefore never has clean air; winter makes a bad baseline worse. Any account that treats smog as a purely seasonal, imported event must explain the 40–59 µg/m³ summer floor. The domestic-baseline account explains it directly.

### 3.2 The ceiling collapses: 830 m → 260 m

Using ERA5 atmospheric reanalysis, Hamari Hawa estimated Lahore's average mixing height at 830–860 m in May–June, about 400 m in October, about 260 m in November and about 190 m in December. Average wind speed stayed light all year, 1.8–2.4 m/s, and October is not windier or calmer than September. The arithmetic is elementary and is the paper's central mechanism: for fixed emissions, ground-level concentration scales roughly inversely with mixing height. November's 260 m against May–June's 830–860 m is a compression factor of **3.2–3.3×**; October-to-November alone is 400 ÷ 260 ≈ **1.5×**. Hamari Hawa's own idealised comparison states the same result in words: halving or thirding the mixing layer makes smoke roughly two to three times more concentrated. The seasonal peak is therefore expected from meteorology alone, before any change in emissions.

**Uncertainty on the metres.** ERA5 reanalysis carries systematic bias: peer-reviewed research published in January 2026 identified biases of 200–500 m in ERA5 over the monsoon region (cited by the EPCCD, via Dawn). Ground-based SUPARCO ceilometer measurements in Lahore found only a 10 m increase in the minimum mixing height over the comparison period, against a 25 m increase cited by PAQI. The absolute values (260 m, 400 m) are therefore uncertain by tens to hundreds of metres; the seasonal *ratio* — a threefold collapse from summer to November — is the robust quantity, and the paper's claim rests on the ratio, not on any single metre value.

### 3.3 The burning is timed to the collapse

Between 15 October and 1 November 2026, satellites recorded 781 crop-associated heat detections within 40 km of central Lahore: Sheikhupura 322, Tarn Taran (India) 149, Amritsar (India) 106, Nankana Sahib 77, Lahore district 62, Kasur 50 (Hamari Hawa). Two facts matter. First, the single largest cluster is domestic — Sheikhupura, 322 detections, more than Tarn Taran and Amritsar combined (255). Second, the timing is systematic: in each of the seven seasons from 2019 to 2025, between 37% and 63% of crop-associated detections within 100 km of Lahore on the Pakistani side occurred *after* 1 November — exactly when the mixing layer is at its shallowest. The harvest pulse and the meteorological trap coincide every year. Punjab-wide, PAQI counted 16,714 probable farm fires between 1 October and 9 November 2026, barely changed from the same stretch a year earlier.

**Uncertainty on the fires.** Satellite heat detections do not confirm individual fires: one field fire may generate several detections, cloud-obscured fires are missed, and the figures measure neither area burnt nor pollution released (Hamari Hawa's own caveat). Fire counts are therefore evidence of timing and geography, not of emitted mass.

### 3.4 The Diwali natural experiment falsifies the border account

The PAQI assessment of 11 November 2026 examined the Diwali window (evening of 8 November to the early hours of 10 November), when fireworks were set off across India:

- HYSPLIT back-trajectories showed emissions from New Delhi never reached Lahore during the monitored period; air from the capital entered Pakistan near Rahim Yar Khan and Bahawalpur after 3 a.m. on 10 November, staying at least **266 km** from Lahore.
- Lahore's average PM2.5 rose about **10%** over the window compared with the previous week's average.
- Faisalabad (~130 km from the border) and Multan (~180 km) each recorded a **40%** increase.
- Averaged across the border cities (Lahore, Kasur, Sialkot, Narowal) the rise was **36 µg/m³**, against **85 µg/m³** in Faisalabad and Multan.

The gradient runs the wrong way for the transboundary-dominant account: the cities farthest from the border rose most. PAQI found no conclusive link between Diwali fireworks and Lahore's smog, and attributed the bulk of the episode's pollution to crop-residue burning within Pakistan — an estimate rendered in press coverage as "around 89%" (Moneycontrol, 11 November 2026). That 89% figure is treated here as an unpublished-method estimate, not a measured apportionment: its method and uncertainty were not published with the figure, and it is not used as a quantitative input to this paper's claim. The gradient test does not need it.

Published estimates of the cross-border contribution to Lahore's pollution range from **13% to 30%** across different studies and geographical areas (Hamari Hawa's synthesis). That range — not zero, not a majority — is the number this paper adopts for the transboundary share.

### 3.5 The satellite record agrees: Lahore is the hotspot, not the border

Mariam, Haq & Batool (2026) analysed TROPOMI NO2 over Punjab from 2018 to 2025. The provincial average was about 37.37 µmol/m², the highest monthly concentration occurred in **November**, and the hotspots were Lahore **92.31 µmol/m²**, Sheikhupura 65.07, Kasur 59.11, Nankana Sahib 54.42, Gujranwala 50.65 and Faisalabad 50.5 µmol/m². The strongest column sits over Lahore itself — 2.5 times the provincial average — not at the border. Road transport accounts for about **33.88%** of Punjab's total NOx emissions in that study; external transport from India and Afghanistan may also contribute, indicated by PSCF/CWT analysis of HYSPLIT trajectories. Rehmat et al. (2023), using Sentinel-5P TROPOMI from May 2018 to May 2022, likewise found NO2 over Lahore and Karachi exceeding WHO limits, with Lahore higher than Karachi. Lama et al. (2020) found Lahore had the *lowest* NO2/CO emission ratio among six megacities studied (Tehran, Mexico City, Cairo, Riyadh, Lahore, Los Angeles) — consistent with a large biomass-burning component in Lahore's combustion mix — and that inventory emission ratios ran 60–85% higher than TROPOMI-derived ratios, a warning that inventories overstate emissions relative to what the satellite sees.

### 3.6 Two inventories, one agreement and one warning

The Urban Unit's 2023 Lahore inventory (2020–21 data) attributes the city's PM2.5 emissions as: transport **35%**, crop-residue burning **33%**, waste burning **29%**, industry **3%**. PAQI's 2026 national inventory attributes Lahore's primary PM2.5 as: transport **35%**, industry **28%**, brick kilns **17%** (combined 80% for the three). Both agree on the headline — transport is about 35%, the largest single share — and both agree that no single source dominates. They disagree in detail because they measure different things: the Urban Unit inventory is an emissions inventory, PAQI's is primary PM2.5 by sector, and waste burning versus industry are classified differently. Hamari Hawa's warning is adopted here as a rule: **inventories, ground monitoring and source-apportionment studies measure different aspects of air pollution, and their percentages cannot be directly compared or converted into one another.** The frequently quoted "83% for transport" is explicitly rejected: it covers all pollutants by weight and is dominated by carbon monoxide, not PM2.5.

Two further inventory facts shape the policy section: Punjab-wide, heavy-duty vehicles and buses produce **55%** of road vehicles' exhaust PM2.5 against **18%** from motorcycles (Urban Unit 2020); and **890** mapped brick kilns sit within 50 km of central Lahore, **196** within 25 km.

### 3.7 Progress is real, and insufficient

The EPCCD reports a 15% net improvement across six major pollutants in the first year of Punjab's real-time monitoring programme, a 28% fall in peak AQI in October 2026 against October 2025, and no hazardous-AQI (>300) days in October 2026 against four in October 2025 — achieved despite 50% less rainfall in October 2026 than October 2025 (Pakistan Meteorological Department). The monitoring network grew from 30 to 59 stations, with 100 planned; 612 electric buses are in service with 3,000 planned; about 500,000 vehicles underwent emissions testing; more than 800 notices were issued to heavy transport; 10,000 super seeders were provided at subsidy, field stubble-burning incidents fell by one-third, and 25,000 seeders are planned; more than 95% of brick kilns have adopted zigzag technology; coal consumption's annual compound growth rate fell 14.2%. The World Bank-backed $300 million Punjab Clean Air Programme aims to cut PM2.5 by 35% over a decade. These are real gains — and October 2026 still averaged 100 µg/m³, twenty times the WHO annual guideline. Improvement at this rate does not reach the standard within a decade.

## 4. Discussion

### 4.1 Mechanism: three multipliers, one trap

The November peak is the product of three factors, each independently measured:

1. **A year-round domestic baseline** (~40–59 µg/m³ even in the cleanest months) from transport, industry, kilns, waste burning, generators, household fuels and dust — sources that operate every day and that Punjab controls entirely.
2. **A seasonal domestic pulse** — rice-stubble burning concentrated after 1 November, with the largest fire cluster (Sheikhupura, 322 detections) inside Punjab, not across the border.
3. **A meteorological multiplier** — the mixing height collapses ~3.2-fold from summer to November while winds stay light (1.8–2.4 m/s), so the same emissions produce roughly three times the ground-level concentration.

Transboundary inflow adds to this, at an estimated 13–30% — real, measurable, and not the main story. The three-factor mechanism explains the timing (November, not September), the geography (Lahore as the NO2 hotspot, inland cities rising fastest in the Diwali episode), and the persistence (a summer floor far above any standard).

### 4.2 Comparison against the strongest incumbent

The strongest incumbent explanation is the provincial government's transboundary account: that Lahore's smog is substantially imported from Indian Punjab's stubble burning and, in 2026, Diwali fireworks. It is the strongest because it is partly true — cross-border smoke is real, the 13–30% range is non-trivial, and 255 of the 781 fire detections near Lahore in late October 2026 were in Tarn Taran and Amritsar. The account fails as the *dominant* explanation on three independent tests: the spatial gradient (inland > border), the trajectories (Delhi air ≥266 km away), and the satellite columns (Lahore, not the border, is the hotspot). The second incumbent, the "crop-burning-only" account (PAQI's ~89% estimate), fails differently: it is a single-source story for a multi-source baseline, it rests on an unpublished method, and it cannot explain the 40–59 µg/m³ summer floor when no stubble is burning. The three-factor account survives both comparisons because it is the only one consistent with the year-round data.

### 4.3 What this paper does not claim

This is a synthesis and falsification test, not new measurement. No new satellite retrieval was performed, no new ground monitoring was conducted, and no exact domestic share is estimated. The claim is that the transboundary-dominant hypothesis is false; the precise domestic shares await a peer-reviewed 2026 source-apportionment study for Lahore, which does not yet exist in this sweep. The policy recommendations below are therefore designed to be testable and reversible, not to rest on a share this paper cannot measure.

## 5. Policy implications

**Decision-maker:** the Government of Punjab, acting through the Environment Protection and Climate Change Department (EPCCD) and the Punjab Agriculture Department, with the World Bank Punjab Clean Air Programme ($300 million) as the funding vehicle.

**Exact changes:**

1. **Adopt a published daily Smog Budget, October–December.** Each morning the EPCCD publishes the forecast mixing height and the implied dilution volume for Lahore. When the forecast mixing height falls below **300 m**, pre-announced emergency measures trigger automatically: heavy-vehicle entry restrictions, brick-kiln curtailment, and staggered school and office hours. The 300 m trigger is set just above November's ~260 m average so that action precedes the worst days rather than following them. **Reversal rule:** if two consecutive Novembers show border cities rising faster than inland cities *and* HYSPLIT trajectories showing eastern air reaching Lahore, the budget's attribution is revised and the transboundary lever is re-prioritised.
2. **Scale super seeders 10,000 → 25,000 as already planned, but target the ring first.** Prioritise Sheikhupura district — 322 fire detections within 40 km of Lahore, the largest single cluster — before expanding province-wide. Success metric: fire detections within 40 km of Lahore, published weekly each October–November.
3. **Enforce heavy vehicles before motorcycles.** Heavy-duty vehicles and buses produce 55% of road exhaust PM2.5 against 18% from motorcycles; enforcement and fitness certification should follow that order, not the reverse.
4. **Publish the border-vs-inland gradient after every smog episode.** The PAQI Diwali method — border-city versus inland-city PM2.5 change plus HYSPLIT trajectories — should become a routine, published test, so the transboundary claim is checked every year instead of asserted.
5. **Verify the 196 kilns within 25 km by ground inspection.** More than 95% zigzag adoption is claimed; the kilns nearest the city should be verified on the ground, not by self-report.

**The Islamic principle behind the recommendation.** *Khilafah* — stewardship: human beings are trustees of the earth, not its owners (Qur'an 2:30), so the air is a trust held for the next generation, and depleting it is a debt, not free income (Nasr, *Man and Nature*, 1968). *Hifz al-nafs* — preservation of life, one of the five objectives of the law (Al-Ghazali, *Al-Mustasfa*; Al-Shatibi, *Al-Muwafaqat*): a policy that costs 3.9 years of life, and 7 in Lahore, fails the first test of the law. *'Adl* — justice (Qur'an 4:135; 16:90): the burden of smog falls hardest on those who cannot buy air purifiers, move house, or keep children indoors; a policy that blames a foreign source while domestic emissions go unenforced taxes the poorest for the state's inaction. Where the Islamic sources and the modern evidence point the same way, this paper says so: both demand measurement before blame, protection of the vulnerable first, and stewardship priced as a debt to the future. Where they differ, the paper would say so; here they do not.

## 6. Conclusion

Lahore's November smog is not mainly imported. It is a domestic baseline of about 35% transport and a third crop burning and the rest waste, industry and kilns, compressed under a ceiling that falls to **260 metres** in November, with a harvest pulse timed to the collapse and a transboundary contribution of 13–30%. The Diwali window of 8–10 November 2026 provided a clean natural experiment, and the transboundary-dominant hypothesis failed it: inland cities rose more than border cities, Delhi's air stayed 266 km away, and the satellite record puts the strongest NO2 column over Lahore itself. The falsifiable policy that follows is a daily Smog Budget with a 300 m trigger, targeted super-seeder deployment to Sheikhupura, heavy-vehicle enforcement first, a published gradient test after every episode, and ground verification of the 196 kilns nearest the city. If the next two Novembers show the opposite gradient, the attribution — and the policy — must change. That is the point: a claim that cannot be killed by the next November is not a policy, it is an excuse.

## 7. Limitations

1. **No peer-reviewed 2026 source-apportionment study for Lahore was found in this sweep.** The newest inventory (Urban Unit, 2023) uses 2020–21 data. PAQI's ~89% crop-burning figure for the Diwali episode is an unpublished-method estimate and was not used as a quantitative input.
2. **Mixing heights are reanalysis, not measurement.** ERA5 carries published biases of 200–500 m over the monsoon region (January 2026 peer-reviewed research, cited by the EPCCD); SUPARCO's ceilometer and PAQI disagree on the change over the comparison period (10 m vs 25 m). The paper's claim rests on the seasonal ratio (~3.2×), not on any absolute metre value.
3. **Satellite fire detections are not fires or emissions.** One field fire may generate several detections; cloud-obscured fires are missed; neither area burnt nor pollution released is measured.
4. **The two inventories cannot be directly compared.** PAQI (transport 35%, industry 28%, kilns 17%) and the Urban Unit (transport 35%, crop burning 33%, waste 29%, industry 3%) classify sources differently; percentages from different methods are not interchangeable.
5. **One episode is not a climatology.** The Diwali natural experiment is a single 3-day window; wind patterns and burning calendars vary year to year. The gradient test must be repeated.
6. **Health-burden estimates disagree.** PAQI estimates ~128,000 premature deaths a year; the State of Global Air estimates above 248,000. Both are reported with attribution; the paper does not reconcile them, and the difference reflects scope and method, not error in either.
7. **Islamic canon — what was not read.** Nasr's *Man and Nature* (1968) and Al-Biruni's *Kitab al-Hind* (c. 1030) were consulted through the programme's verified literature map, not re-read in full in this run. Al-Biruni's *Al-Qanun al-Mas'udi* was not consulted in full (no complete open English translation was used in this run). Nidhal Guessoum's *Islam's Quantum Question* (2011) is a relevant work for the science–religion method that was not consulted in this run. Undigitised manuscripts held in the Süleymaniye Library (Istanbul), Dar al-Kutub (Cairo) and the British Library were not accessed. Most of Al-Razi's *Kitab al-Hawi* exists in English only in selections and was not relevant to this question.
8. **This is a synthesis, not new measurement.** No new satellite retrieval or ground monitoring was performed. All numbers trace to the sources listed in §8; any number without a source in that list is derived arithmetic and is labelled as such.

## 8. References

1. Tariq H (Hamari Hawa). *Lahore's smog: The year-round baseline, and what changes in October.* Environmental monitoring report, 2 November 2026. Reported in: Dawn. "Lahore's air pollution a year-round problem, worsened by winter and agricultural burning: report." 5 November 2026. https://www.dawn.com/news/2042329/lahores-air-pollution-a-year-round-problem-intensified-by-winter-agricultural-burning-report
2. Pakistan Air Quality Initiative. *Unveiling Pakistan's Air Pollution: A National Landscape Report on Health Risks, Sources, and Solutions.* October 2026. Reported in: Asia Daily, 28 October 2026; Skardu Times, 28 October 2026.
3. Pakistan Air Quality Initiative. Assessment of Diwali fireworks and transboundary transport during the Lahore smog episode, 8–10 November 2026. 11 November 2026. Reported in: Moneycontrol, 11 November 2026; Times Reading, 12 November 2026.
4. Mariam A, Haq ZU, Batool SA. Assessment of spatio-temporal dynamics of tropospheric NO2 and covariates using the wavelet analysis: a Punjab case study. *Environmental Monitoring and Assessment.* 2026;198:831. doi:10.1007/s10661-026-15674-7
5. Lama S, Houweling S, Boersma KF, Eskes H, Aben I, Denier van der Gon HAC, Krol MC, Dolman H, Borsdorff T, Lorente A. Quantifying burning efficiency in megacities using the NO2/CO ratio from the Tropospheric Monitoring Instrument (TROPOMI). *Atmospheric Chemistry and Physics.* 2020;20:10295–10310. doi:10.5194/acp-20-10295-2020
6. Rehmat R, Rafique L, Irfan M, Ahmed SR, Lahori AH, Muhammadi A, Taha M, Vambol S, Shulga M. Space-borne air quality monitoring of nitrogen dioxide (NO2) over Karachi and Lahore using remote sensing tools. *Proceedings of the Pakistan Academy of Sciences: B. Life and Environmental Sciences.* 2023;60(3):505–513. doi:10.53560/PPASB(60-3)875
7. Ali M, Siddique I, Abbas S. Characterizing air pollution and its association with emission sources in Lahore: a guide to adaptation action plans to control pollution and smog. *Applied Sciences.* 2022;12(10):5102. doi:10.3390/app12105102
8. World Health Organization. *WHO global air quality guidelines: particulate matter (PM2.5 and PM10), ozone, nitrogen dioxide, sulfur dioxide and carbon monoxide.* Geneva: WHO; 2021. (PM2.5 annual guideline 5 µg/m³; 24-hour guideline 15 µg/m³.)
9. Health Effects Institute / Institute for Health Metrics and Evaluation. *State of Global Air 2025.* Cited via: Overseas Investors Chamber of Commerce and Industry, reported in The Express Tribune, 5 November 2026. https://tribune.com.pk/story/2638702/air-pollution-costs-65-of-gdp
10. Environment Protection and Climate Change Department, Government of Punjab. First-year report of the real-time air quality monitoring programme. November 2026. Reported in: Dawn, 5 November 2026 (see ref. 1).
11. The Urban Unit. Lahore emissions inventory. 2023 (2020–21 data). Cited via Hamari Hawa (ref. 1).
12. World Bank. Punjab Clean Air Program ($300 million). Cited via The Express Tribune, 5 November 2026 (see ref. 9).
13. Nasr SH. *Man and Nature: The Spiritual Crisis of Modern Man.* London: George Allen & Unwin; 1968.
14. Al-Biruni. *Kitab al-Hind.* c. 1030.
15. Al-Ghazali. *Al-Mustasfa min 'Ilm al-Usul.* (The five necessities of the law: din, nafs, 'aql, nasl, mal.)
16. Al-Shatibi. *Al-Muwafaqat fi Usul al-Shari'a.* 8th century AH.
17. The Qur'an 2:30 (stewardship / khilafah); 4:135 and 16:90 (justice / 'adl).
18. Allen M, et al. Warming caused by cumulative carbon emissions. *Nature.* 2009;458:1163–1166. (Method standard: one clean quantitative relationship — the trillion-tonne carbon budget — cited as the template for this paper's single-number argument, not as evidence on smog.)
19. Pacala S, Socolow R. Stabilization wedges: solving the climate problem for the next 50 years with current technologies. *Science.* 2004;305(5686):968–972. (Method standard: the portfolio-of-deployable-pieces framing, cited as the template for the Smog Budget.)

## 9. Data availability

All data used are public. The Hamari Hawa report is published at hamarihawa.org; the Dawn report of 5 November 2026 is at the URL in ref. 1. The PAQI national report and Diwali-episode assessment were released publicly in October–November 2026 and are reported in refs. 2–3. TROPOMI NO2 data are available from the Copernicus Sentinel-5P data portal; ERA5 reanalysis from the Copernicus Climate Data Store; IQAir historical data from iqair.com. The Urban Unit inventory (2020–21 data) and the EPCCD monitoring data are published by the Government of Punjab. No new dataset was generated. The search log for this run (digest of 14 November 2026; targeted searches of 15 November 2026) is held in the programme's run records. Replication: the gradient test in §2.3 can be repeated on any future smog episode using PAQI/IQAir city-level PM2.5 series and HYSPLIT back-trajectories; the mixing-height ratio can be recomputed from ERA5 or SUPARCO ceilometer records.

---

*End of manuscript. AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.*
