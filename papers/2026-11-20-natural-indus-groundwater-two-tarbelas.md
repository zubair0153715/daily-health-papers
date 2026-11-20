# Two Tarbelas a Year: The Post-2015 Acceleration of Indus Basin Groundwater Loss and a Stepped-Wedge Groundwater Budget for Punjab

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan. ORCID: 0009-0001-5921-7509.
**Drafting assistant:** Lapis (AI research assistant).
**Date:** 20 November 2026. **Field:** Natural Science (hydrology / water policy).
**Status:** Manuscript draft. Not submitted anywhere. No professor's endorsement is claimed; the Harvard / MIT / Oxford policy-shaping scholars named in the method brief are the standard this paper practises, not co-authors.

---

## Abstract

**Question.** Has Indus Basin groundwater loss genuinely accelerated since 2015, is the acceleration driven by pumping rather than climate, and what policy, tested how, would stop it in Pakistan's Punjab?

**Claim.** Yes, the loss more than tripled: basin-wide terrestrial water storage fell at −0.65 cm/yr in 2002–2015 and at −2.16 cm/yr after 2015 (Dharpure et al., *Water Resources Research*, 2025). Converted to volume over the basin's 1.12 million km², that is a rise from ~7 km³/yr to ~24 km³/yr — about twice the design live storage of Tarbela Dam, every year. The acceleration is pumping-driven and concentrated in managed landscapes: non-glaciated regions lose water about twice as fast as glaciated ones (−1.44 vs −0.78 cm/yr), downscaled GRACE attributes 47–83% of the decline in most sub-regions to anthropogenic stressors, and aquifer depletion drives 67% of the Indus's total water-storage decline. Pakistan alone extracts ~65 km³/yr of groundwater against ~55 km³/yr of recharge — a ~10 km³/yr deficit, roughly one Tarbela a year.

**Falsifier.** The claim fails if (i) GRACE-FO data for 2024–2028 show the non-glaciated/glaciated loss ratio collapsing toward 1 (which would mean the acceleration is climate-driven, not pumping-driven), or (ii) a stepped-wedge trial of district groundwater budgets shows no divergence between pilot and control districts after five years (see §6). Either result would require withdrawing the pumping-driven attribution or the policy, respectively.

**Identification.** Natural-experiment contrast (glaciated vs non-glaciated regions under shared climate forcing; managed vs natural landscapes in downscaled GRACE) plus a general additive model decomposition for attribution; **the attribution is association only — not causal proof**. The policy claim will be tested by a stepped-wedge cluster-randomised rollout of district groundwater budgets, which is the causal design.

**One clean number: 24 km³/yr** — the water the Indus Basin now loses every year, about two Tarbelas. The stakes number is 300 million: the people the basin supports.

**Keywords:** Indus Basin; groundwater depletion; GRACE; GRACE-FO; Punjab; tube wells; solar pumping; stepped-wedge trial; khilafah; water commons.

---

## 1. Introduction

The Indus Basin — 1.12 million km² across Afghanistan, China, India and Pakistan, home to nearly 300 million people — is the most intensively irrigated river basin on Earth, and its groundwater is its hidden reservoir. Pakistan is the world's fourth-largest user of groundwater, and its aquifer system is the second-most overstressed on the planet (Pakistan Institute of Development Economics, 2026). Per-capita water availability in Pakistan has fallen from over 5,000 m³ in 1947 to under 1,000 m³ today — the standard threshold of absolute water scarcity.

Until recently the depletion was understood as a slow, chronic decline. A study published in February 2025 changed the picture: using GRACE and GRACE-FO satellite gravity data from April 2002 to May 2023, Dharpure, Howat and Kaushik showed that the basin's water loss more than tripled after 2015 — from −0.65 cm/yr to −2.16 cm/yr — and that 83.7% of the basin is now in significant decline. The question this paper answers is the one the study leaves open: how big is that loss in volumes a minister can picture, is it pumping or climate, which districts cross the danger line first, and what exactly should Punjab — which pumps over 90% of Pakistan's groundwater — do, tested in a way that can prove itself wrong?

The paper's method ancestor is named deliberately: Al-Biruni (973–1050), who measured the Earth's circumference to within about 1% and recorded the rivers and lands of India before theorising about them (*Kitab al-Hind*, c. 1030). The discipline this paper demands of Punjab's water policy is the same: measure first, publish the measurement, and let the claim be killed by the next measurement.

## 2. Methods

### 2.1 Literature sweep

Three legs, in the order required by the programme's standing rules:

1. **Modern scientific literature.** The daily research digest of 14 November 2026 (health-focused; no water item) plus targeted searches on 20 November 2026 for Indus groundwater depletion, GRACE/GRACE-FO rates, Pakistan abstraction and tube-well counts, and Lahore water-table decline. Peer-reviewed sources used: Dharpure, Howat & Kaushik (2025, *Water Resources Research* 61(2), e2024WR038279, DOI 10.1029/2024WR038279); Arshad et al. (2024, *Water Resources Research* 60, DOI 10.1029/2023WR035882); the Frontiers in Earth Science decomposition of Indus–Ganges–Brahmaputra storage (2025, DOI 10.3389/feart.2025.1551218); and the Lahore aquifer literature (MDPI *Water*, 2022; *Groundwater Environment in Lahore*, Elsevier, 2017). Grey literature used and labelled as such: the Pakistan Institute of Development Economics report *Pakistan's Groundwater Crisis: Policy Lessons and a Framework for Sustainable Resource Use* (2026, as reported by *The News* and *ProPakistani*, October–November 2026); Punjab Irrigation Department piezometer data as reported by *Dawn* (12 May 2025) and the Sustainable Development Policy Institute; Pakistan Council of Research in Water Resources (PCRWR) figures as reported by *Business Recorder* (2026). Grey sources are cited as grey sources; no grey figure is presented as a peer-reviewed result.
2. **Islamic canon.** The hadith of the three commons — "Muslims are partners in three things: pasture, water and fire" (Sunan Abi Dawud 3477, graded sahih by al-Albani); Qur'an 21:30 ("We made from water every living thing"); Qur'an 2:30 (humanity as khalifah, steward, on earth); Al-Biruni, *Kitab al-Hind* (c. 1030); Seyyed Hossein Nasr, *Man and Nature: The Spiritual Crisis of Modern Man* (1968); Al-Ghazali, *Al-Mustasfa* (the five necessities of the law); Al-Shatibi, *Al-Muwafaqat* (systematisation of maqasid al-shariah). Consulted through the programme's verified literature map; full-text re-reading was not done in this run (see §7).
3. **Method standard.** The 10-point checklist of the policy-shaping professors (Banerjee & Duflo; Acemoglu, Johnson & Robinson; Chetty; Thaler & Sunstein; Heckman; Hanushek; Rodrik; Deaton; Haynes & Gawande; Pacala & Socolow; Myles Allen): one falsifiable question, named identification, mechanism, effect size with uncertainty, analysis plan stated before results, replication/data availability, limitations that bite, policy implications naming the decision-maker, comparison against the strongest incumbent, one clean number.

Research agents were not used in this run: Mimosa's litellm patch has landed but its smoke test remains incomplete; Co-Scientist, Denario and EvoScientist remain blocked on authentication or onboarding. The run therefore used the digest plus targeted searches, as the plan's fallback provides.

### 2.2 Pre-registered analysis plan (stated before results)

1. **Convert the published satellite rates to volumes** using the published basin area (1.12 million km², range 1.08–1.165 million km²), with the arithmetic shown and the range carried through as the uncertainty band. No new satellite processing is claimed.
2. **Test the pumping-driven attribution** against three independent published lines: the glaciated/non-glaciated contrast (Dharpure et al. 2025), the downscaled-GRACE anthropogenic share (Arshad et al. 2024), and the storage-decomposition share (Frontiers 2025). The claim requires at least two of the three to point the same way.
3. **Rank Punjab districts** by published water-table decline rates and abstraction volumes, and propose a regulatory trigger threshold grounded in the observed Lahore rate.
4. **Design the policy test** as a stepped-wedge cluster-randomised trial with a pre-stated success criterion, so the policy can fail in public.

### 2.3 Volume conversion (the paper's own arithmetic)

Water-equivalent depth (cm/yr) × basin area (km²) = volume (km³/yr). 1 cm over 1 km² = 0.01 km³. All conversions in §3 are this multiplication, labelled "derived here", and use the central basin area of 1.12 million km² with the published area range (1.08–1.165 million km²) as the band. Tarbela Dam's design live storage is 9.68 million acre-feet (MAF) = 11.94 km³ (1 MAF = 1.2335 km³); siltation has cut its present live storage to roughly 5.7–6.8 MAF (7.0–8.4 km³). Both figures are used, and the paper says which one each comparison uses.

## 3. Results

### 3.1 The acceleration, in volumes

Dharpure et al. (2025) report basin-wide terrestrial water storage anomaly (TWSA) falling at −0.65 cm/yr before 2015/16 and −2.16 cm/yr after — a 3.3-fold acceleration — with 83.7% of the basin in significant decline (>−0.15 cm/yr, p < 0.05). Converted (derived here):

| Period | Rate (cm/yr) | Volume loss (km³/yr) | In Tarbelas (design live storage, 11.94 km³) |
|---|---|---|---|
| 2002–2015 | −0.65 | 7.3 (range 7.0–7.6) | ~0.6 |
| 2015–2022 | −2.16 | 24.2 (range 23.3–25.2) | ~2.0 |

The basin now loses about **24 km³ of water a year — two Tarbelas a year, every year** — against about 7 km³/yr before 2015. Against Tarbela's *present*, silted live storage (7.0–8.4 km³), the annual loss is roughly three Tarbelas. The Indus River system distributes about 153 billion m³ (153 km³) of freshwater a year through its canals; the groundwater loss is now equivalent to about one-sixth of that entire annual surface flow, disappearing underground.

### 3.2 The acceleration is pumping-driven, not climate-driven

Three independent published lines point the same way:

- **The glaciated/non-glaciated contrast (Dharpure et al. 2025).** Glaciated regions lose −0.78 cm/yr; non-glaciated regions lose −1.44 cm/yr — about twice as fast. Both regions share the same climate forcing; what differs is that the non-glaciated plains are where the pumping happens. Among sub-basins, the Upper Indus (glaciated, little pumping) loses least (−0.42 cm/yr) while the Panjnad (the Punjab confluence of the five rivers, intensively pumped) loses most (−1.70 cm/yr).
- **The downscaled-GRACE attribution (Arshad et al. 2024).** At 1 km² resolution, validated against 2,200 monitoring wells (Kling–Gupta efficiency 0.50–0.85, correlation 0.60–0.95), a general additive model attributes 47–83% of the total water-storage decline in most sub-regions to anthropogenic stressors — expanding cropped area, water consumption and settlements. The worst hotspots are in managed landscapes: Dehli Doab groundwater storage falling at −585 mm/yr, BIST Doab at −556 mm/yr. In upstream sub-regions, by contrast, climatic factors explain 72–91% of the change — the method can tell the two apart, and it says the plains are us.
- **The storage decomposition (Frontiers in Earth Science, 2025).** Aquifer depletion drives 67% of the Indus's total water-storage decline (76% in the Ganges). The falling signal is mostly groundwater, not snow or soil moisture.

Dharpure et al. also report the climate contribution honestly: declining precipitation and surface runoff, rising evapotranspiration, and vegetation cover growing 0.23% a year (more crops, more water demand). Climate loads the gun; pumping pulls the trigger. **Attribution is association only** — no randomised manipulation exists — but the three lines agree, and the glaciated/non-glaciated contrast is the closest thing to a control group the basin offers.

### 3.3 Pakistan's side of the ledger

The satellite picture and the ground picture agree in magnitude:

- **Extraction vs recharge (PIDE, 2026).** Pakistan extracts ~65 km³/yr of groundwater against ~55 km³/yr of natural recharge — a deficit of ~10 km³/yr, roughly one Tarbela (design live storage) every year. Punjab accounts for over 90% of national abstraction.
- **The tube-well explosion (Punjab Irrigation Department, via *Dawn*, May 2025).** Agricultural tube wells in Punjab rose from 333,881 in 1994 to over 1.2 million in 2024; nationally the count exceeds 1.4 million. Punjab's wells now withdraw over 51 MAF/yr — about 63 km³/yr, slightly less than Punjab's entire allocated share of river water under the 1991 Water Apportionment Accord. District Rahim Yar Khan alone has 97,571 tube wells extracting around 4 MAF/yr, driven largely by sugarcane. Punjab's extraction rate is 142% above its recharge rate (*Dawn*, February 2025).
- **The solar accelerant (Reuters, via *Business Recorder*, 2026).** Roughly 650,000 of Pakistan's 1.4 million-plus tube wells — nearly half — are now solar-powered. Solar pumping has zero marginal energy cost: once the panels are installed, every extra hour of pumping is free. That is the mechanism by which a water-saving technology became a water-mining technology.
- **The water table on the ground (Punjab Irrigation Department piezometers, 2004–2024).** Water tables fell in 30 Punjab districts, sharply in 27. Lahore's fell from 31 ft to 79 ft — a decline of 2.61 ft/yr (≈0.8 m/yr), the fastest in the province — with the central city now below 40 m and falling about 0.9–1.0 m/yr (WASA; PCRWR 2023). Pakpattan fell 44 ft and Multan 32 ft over the same twenty years. Outside the canal command the rates are worse: Rawalpindi ~2.5 m/yr, Quetta Valley ~6 m/yr with wells now deeper than 350 m (PCRWR 2023). Lahore alone extracts about 4.32 million m³ of groundwater a day through nearly 1,800 tube wells.

### 3.4 Which districts cross the line first — a proposed trigger

No official "critical district" threshold exists for Punjab's groundwater. This paper proposes one, grounded in the observed data rather than invented: **a district is declared critical when its five-year mean water-table decline exceeds 2 ft/yr (≈0.61 m/yr)** — a rate Lahore (2.61 ft/yr) and Pakpattan (2.2 ft/yr) already exceed, and Multan (1.6 ft/yr) approaches. The threshold is a *proposal*, not a measurement; its purpose is to convert a satellite trend into an administrative fact with a named consequence (metering, then a cap). On published rates, the first critical districts are Lahore, Pakpattan, Rahim Yar Khan (by abstraction volume), Multan, and the Lahore-adjacent urbanising districts — the order is a ranking by published evidence, and the trial in §6 will test whether the ranking predicts stabilisation.

## 4. Discussion

### 4.1 Mechanism

The causal chain has five links, each with a published test:

1. **Free energy.** Solar panels collapsed the marginal cost of pumping to zero for ~650,000 wells. Standard economics predicts more pumping; the well count (334,000 → 1.2 million in Punjab) and the post-2015 acceleration are consistent with it.
2. **Thirsty crops.** Sugarcane in Rahim Yar Khan and rice across the doabs expanded on pumped water; vegetation cover grew 0.23%/yr basin-wide (Dharpure et al. 2025).
3. **Open access.** Groundwater was a de facto open-access resource until the Punjab Irrigation, Drainage and Rivers Act (2023) vested all groundwater rights in the government; the Punjab Water Act (2019) already provides licensing tools for large users. The law now exists; enforcement does not.
4. **Falling recharge.** Declining precipitation and runoff plus urban paving reduce the water going back in, while abstraction rises — the 142%-above-recharge figure.
5. **Deepening.** As shallow water fails, wells go deeper (Lahore's potable water now at 800 ft in places; Quetta beyond 350 m), raising costs for the poorest farmers first and mining fossil water that accumulated over thousands of years.

### 4.2 Why the incumbent answer — build more dams — cannot fix this

The strongest incumbent policy is surface storage: build another Tarbela. The comparison is arithmetic. A new large dam adds, at best, one Tarbela's worth of live storage (~7–12 km³) after a decade or more of construction and tens of billions of rupees — and storage does not create water, it only retimes it. The groundwater deficit recurs every year: ~10 km³/yr for Pakistan alone, ~24 km³/yr basin-wide. Dams also lose live storage to siltation (Tarbela has lost roughly a third). Capping abstraction at recharge, by contrast, saves the same volume every year at the cost of meters and licences. Storage and demand management are complements, not substitutes — but a policy that only builds storage while abstraction grows 3.3-fold is arithmetic denial. The PIDE report reaches the same conclusion: the crisis is "fundamentally a failure of policy and governance rather than a physical lack of water."

### 4.3 The Islamic frame: water as a commons, not a commodity

The policy conclusion the modern evidence points to is the one the Islamic canon stated fourteen centuries ago. The Prophet ﷺ said: *"Muslims are partners in three things: pasture, water and fire"* (Sunan Abi Dawud 3477, graded sahih by al-Albani) — water that is not under anyone's private control is a shared property, and monopolising it is prohibited. The Qur'an grounds the same point in creation itself: *"We made from water every living thing"* (Qur'an 21:30), and in stewardship: humanity is placed on earth as khalifah, trustee (Qur'an 2:30). Al-Biruni's *Kitab al-Hind* (c. 1030) measured the rivers and lands of this very basin before theorising about them — the measurement-first discipline this paper follows. Seyyed Hossein Nasr (*Man and Nature*, 1968) argues the ecological crisis is at root a spiritual one: nature treated as a resource to exhaust rather than a trust (amanah) to keep. Against the maqasid al-shariah (Al-Ghazali, *Al-Mustasfa*; Al-Shatibi, *Al-Muwafaqat*), the current regime fails on the preservation of life (nafs) — 70–80% of Pakistan's groundwater is unsafe to drink, with arsenic threatening up to 60 million people (PIDE 2026) — and on wealth (mal), as the aquifer, the country's largest water store, is mined. Where the Islamic source and the modern evidence point the same way, this paper says so: both say water is a commons, pumping must be capped at recharge, and the burden must not fall on the poorest farmers. Where they differ, the paper says so too: the canon gives the principle, not the number — the 2 ft/yr trigger and the stepped-wedge design are modern instruments, not derived from scripture.

## 5. Policy implications

**Decision-maker:** the Secretary, Punjab Irrigation Department, acting with the Punjab Water Commission under the Punjab Irrigation, Drainage and Rivers Act (2023) and the Punjab Water Act (2019). **The exact change, in order:**

1. **Declare critical districts by the 2 ft/yr trigger** (§3.4), starting with Lahore, Pakpattan, Rahim Yar Khan and Multan, and publish the district ranking with the underlying piezometer data — Chetty's lesson: publish the data as a public tool, not just the finding.
2. **Meter solar tube wells first, within 24 months.** The ~650,000 solar wells are the marginal-cost-free pumpers; metering them is the cheapest measurement in the system and the precondition for any cap. Fund it from the electricity-subsidy savings as diesel/electric wells convert.
3. **Cap district abstraction at recharge, rolled out as a stepped-wedge cluster-randomised trial.** Districts are randomised into licensing waves; each wave's cap is set at the district's GRACE-derived recharge rate, enforced through the 2019 Act's licensing tools. Pre-register the analysis: the primary outcome is the district GWSA trend from GRACE-FO plus piezometers; success is a pilot-district trend of −0.5 cm/yr or better against control districts continuing at −1.5 cm/yr or worse, after five years. **If pilot districts show no divergence from controls, the cap-and-meter approach is withdrawn and the recommendation reverses to supply-side measures only.**
4. **Protect small farmers by design ('adl).** The cap must be paired with a lifeline allocation for smallholders and a shift of price support away from sugarcane and rice toward less thirsty crops — otherwise the burden falls on the poorest, and the policy fails the justice test (Qur'an 4:135, 16:90).

**Islamic principle behind the recommendation:** the hadith of the three commons (water as shared property — Sunan Abi Dawud 3477) and khilafah stewardship (Qur'an 2:30), operationalised through maslaha (public interest) and 'adl (justice). The trial design itself is an act of shura in method: the policy is tested in the open, and its subjects — the districts — are its witnesses.

## 6. The falsifiable claim, stated once more

**Claim:** the post-2015 acceleration of Indus groundwater loss is pumping-driven and concentrated in Punjab's managed landscapes, and a district groundwater budget (cap at recharge, metered solar wells) will stabilise pilot districts within five years. **Falsifier 1 (attribution):** GRACE-FO 2024–2028 shows the non-glaciated/glaciated loss ratio falling to ~1. **Falsifier 2 (policy):** pilot districts' GWSA trends do not diverge from controls by at least 1 cm/yr after five years. **Falsifier 3 (mechanism):** metering shows solar wells are not the marginal pumpers — i.e., metered solar abstraction is flat while total abstraction still rises, which would point to a different driver. Any one of the three kills the corresponding part of the claim.

## 7. Limitations

1. **GRACE cannot see a district.** GRACE/GRACE-FO resolve ~300 km; the 1 km² downscaled products are model outputs, validated against wells with correlation 0.60–0.95 and RMSE of 17.5 cm against in-situ groundwater storage in the Indus (ISPRS Archives, 2026). District rankings in §3.4 rest on piezometers and abstraction proxies, not on direct district-level satellite measurement.
2. **The 65/55 km³ figures are estimates.** PIDE's national extraction and recharge numbers carry wide, unstated uncertainty; different sources put national abstraction at 50 MAF (~62 km³) to 65 km³ and Punjab's well count at 1.2–1.5 million. The deficit is robust in sign, not precise in size.
3. **Attribution is association only.** The glaciated/non-glaciated contrast and the GAM decomposition are quasi-experimental; no randomised manipulation of pumping exists. The stepped-wedge trial is proposed precisely because the current evidence cannot prove causality.
4. **The 2 ft/yr trigger is proposed, not measured.** It is calibrated to the observed Lahore rate, but the threshold at which a district's aquifer becomes economically unviable for small farmers is not established in the literature and will vary with depth to water and energy cost.
5. **Grey sources.** PIDE, PCRWR and Punjab Irrigation Department figures reach this paper through reputable press reporting, not through the underlying reports, which were not obtained in this run. They are labelled as such in §2.1.
6. **Islamic canon gaps.** Al-Biruni's *Kitab al-Hind* and Nasr's *Man and Nature* were consulted through the programme's verified literature map, not re-read in full in this run. The classical fiqh chapters on water rights beyond the cited hadith, and Ibn Khaldun's discussion of urban water supply in the *Muqaddimah*, were not consulted; many classical Arabic manuscripts on water law remain undigitised in libraries (Süleymaniye, Istanbul; Dar al-Kutub, Cairo) with no online copy. The hadith and Qur'an citations were verified against published references in this run; no quotation is offered from memory.
7. **Transboundary scope.** The basin spans four countries; this paper's policy lever sits in Punjab, Pakistan. The fastest-declining hotspots (Dehli and BIST doabs) lie across the border, and no basin-wide treaty mechanism for groundwater exists.

## 8. Conclusion

The Indus Basin's groundwater loss more than tripled after 2015, from ~7 km³/yr to ~24 km³/yr — two Tarbelas a year. The loss is concentrated where the pumping is, the attribution is consistent across three independent published lines, and Pakistan's own deficit is about one Tarbela a year. The law to fix it already exists; the measurement to enforce it already exists; what does not exist is a tested policy. The proposal is therefore small and testable: declare critical districts by a published trigger, meter the solar wells first, and cap abstraction at recharge in a stepped-wedge trial that can fail in public. Water is a shared trust — the satellite, the piezometer and the hadith agree on that much. What remains is to act as if it were true.

---

## References

1. Dharpure JK, Howat IM, Kaushik S. Declining Groundwater Storage in the Indus Basin Revealed Using GRACE and GRACE-FO Data. *Water Resources Research*. 2025;61(2):e2024WR038279. DOI: 10.1029/2024WR038279.
2. Arshad A, Tran TND, Mirchi A, He C, Rahman MM, et al. Downscaled-GRACE Data Reveal Anthropogenic and Climate-Induced Water Storage Decline Across the Indus Basin. *Water Resources Research*. 2024;60. DOI: 10.1029/2023WR035882.
3. Decomposing land surface total water storage in the Indus, Ganges, and Brahmaputra basins. *Frontiers in Earth Science*. 2025. DOI: 10.3389/feart.2025.1551218.
4. Pakistan Institute of Development Economics. *Pakistan's Groundwater Crisis: Policy Lessons and a Framework for Sustainable Resource Use*. Islamabad: PIDE; 2026. As reported by *The News*, October 2026, and *ProPakistani*, November 2026.
5. Punjab Irrigation Department. Groundwater monitoring data (piezometers, tube-well census), as reported by *Dawn*, 12 May 2025 and 6 February 2025.
6. Pakistan Council of Research in Water Resources. Groundwater extraction and water-table figures, as reported by *Business Recorder*, 2026.
7. Water and Sanitation Agency (WASA) Lahore; MDPI *Water*. Water Demand Estimation in Service Areas with Limited Numbers of Customer Meters — Case Study in WASA Lahore, Pakistan. *Water*. 2022;14:2197.
8. Groundwater Environment in Lahore, Pakistan. In: *Groundwater Environment in South Asia* (Elsevier, 2017) — Lahore water-table decline 0.45–1.50 m/yr; abstraction 1,161 MCM/yr vs recharge 1,013 MCM/yr.
9. Al-Biruni. *Kitab al-Hind* (c. 1030).
10. Nasr SH. *Man and Nature: The Spiritual Crisis of Modern Man*. London: Allen & Unwin; 1968.
11. Al-Ghazali. *Al-Mustasfa min 'Ilm al-Usul* (c. 1109).
12. Al-Shatibi. *Al-Muwafaqat fi Usul al-Shari'a* (14th c.).
13. Sunan Abi Dawud 3477 (Book of Hire / Kitab al-Ijarah): "Muslims are partners in three things: pasture, water and fire." Graded sahih by al-Albani.
14. Qur'an 21:30; Qur'an 2:30; Qur'an 4:135; Qur'an 16:90.
15. Ohio State University, Byrd Polar and Climate Research Center. "Study Highlights Decline in Water Storage in the Indus Basin." 2025. https://byrd.osu.edu/news/study-highlights-decline-water-storage-indus-basin
16. GRACE and GRACE Follow-On: On Accurate Estimation of Groundwater Storage Change from Satellite Gravimetry and Beyond. *International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences*. 2026;XLIX-B3-2026:783. DOI (proceedings): isprs-archives-XLIX-B3-2026-783-2026.

## Data availability

All satellite rates are from the published sources in the References (Dharpure et al. 2025; Arshad et al. 2024), publicly available through AGU/Wiley. GRACE and GRACE-FO data are public from NASA's Physical Oceanography Distributed Active Archive Center (PO.DAAC) and the German Research Centre for Geosciences (GFZ). Punjab piezometer and tube-well data are held by the Punjab Irrigation Department; the figures used here are those reported in the press citations above, because the underlying departmental reports were not obtained in this run. All volume conversions are shown in §2.3 and can be recomputed from the cited rates and the published basin area (1.12 million km², range 1.08–1.165 million km²). No new dataset was generated. The drafting assistant's working notes and source log are retained in the programme's hidden files.
