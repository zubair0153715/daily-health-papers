# Who Gets the Youth Loan? Concentration, Subsidy and the Missing Enterprise Test in Pakistan's PMYBALS, 2023–2026

**AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.**

**Author:** Zubair Ali, Pharm-D student, SMBBMU Larkana, Pakistan. ORCID: 0009-0001-5921-7509.
**Drafting assistant:** Lapis (AI research assistant).
**Date:** 21 November 2026. **Field:** Social Science (public economics / development finance).
**Status:** Manuscript draft. Not submitted anywhere. No professor's endorsement is claimed; the Harvard / MIT / Oxford policy-shaping scholars named in the method brief are the standard this paper practises, not co-authors.

---

## Abstract

**Question.** Pakistan's Prime Minister's Youth Business & Agriculture Loan Scheme (PMYBALS) has disbursed roughly Rs 289 billion since January 2023 to over half a million borrowers, at a taxpayer subsidy the State Bank of Pakistan (SBP) prices at about 15 paisa per rupee lent. Its stated purpose is youth enterprise creation. Does the money actually reach young entrepreneurs and create new enterprises — or does subsidised credit concentrate in a small number of large borrowers while youth unemployment keeps rising?

**Claim.** On the published aggregates, the scheme fails its own enterprise test twice over. First, **concentration**: in the SBP's own tier tables to December 2025, Tier-III loans (Rs 1.5–7.5 million, 7% fixed interest) took **67.0% of all money disbursed while reaching only 11.0% of borrowers**, and the average Tier-III loan (Rs 2.92 million) was **22 times** the average interest-free Tier-I loan (Rs 132,339) that 85.6% of borrowers received. Second, **no enterprise signal**: while Rs 175 billion had been disbursed by June 2025, youth unemployment (ages 15–24) *rose* from 11.1% (2020-21) to 12.6% (2024-25) in the Pakistan Bureau of Statistics Labour Force Survey, and the 27.4% jump in SECP company registrations in FY2024-25 is attributed by SECP itself to digitisation (99.9% of incorporations online), not to the loan scheme. A third finding is a data-quality failure: the press-reported claim that Rs 102 billion went to 3,957 agriculture borrowers is arithmetically impossible under the scheme's Rs 7.5 million loan cap (maximum Rs 29.7 billion) — a 3.4× gap that the government has not explained.

**Falsifier.** The claim is refuted if either (i) district-level SBP disbursement data, once published, show that per-youth disbursement positively predicts per-youth SECP registrations or Labour Force Survey youth self-employment after controlling for the pre-2023 registration trend and the SECP digitisation rollout, or (ii) a follow-up survey of a random sample of Tier-I borrowers finds that at least 50% operate a business that was still trading 24 months after disbursement. The FY2026-27 outturn — a Rs 292 billion disbursement target that exceeds the entire three-year cumulative total — is the first scheduled test.

**Identification.** **Association only.** This is a descriptive audit of published national aggregates, with no control group and no randomised or quasi-experimental variation in who receives loans. Confounders — SECP digitisation, GDP growth, inflation, the January 2023 scheme launch coinciding with post-flood recovery lending — are named, not controlled. The paper falsifies the claim that "disbursement equals enterprise creation"; it does not estimate a causal effect of any loan. A difference-in-differences design on district-level data and a randomised musharakah-vs-interest-loan trial are proposed as the causal tests.

**One clean number: 67% of the money to 11% of the borrowers** — the share of PMYBALS disbursements absorbed by the largest loan tier, against 85.6% of borrowers sharing 23.7% of the money in the interest-free tier. The stakes number is **Rs 38 billion**: the SBP's estimated annual subsidy bill for the scheme, against Rs 21 billion budgeted — a Rs 17 billion (45%) funding gap.

**Keywords:** PMYBALS; youth enterprise; credit concentration; subsidy; Pakistan; SBP; SECP; riba; musharakah; 'adl; maqasid.

---

## 1. Introduction

Pakistan has 46.3 million people aged 15–24 — 18.5% of the population — and their unemployment rate rose from 11.1% in 2020-21 to 12.6% in 2024-25, even as the youth labour force grew from 18.3 million to 21.1 million (Pakistan Bureau of Statistics, Labour Force Survey 2024-25). The government's flagship answer is the Prime Minister's Youth Business & Agriculture Loan Scheme (PMYBALS), launched in January 2023: subsidised credit for young Pakistanis aged 21–45 (18 for IT and e-commerce), in tiers — Tier-I up to Rs 0.5 million interest-free, Tier-II Rs 0.5–1.5 million at 5%, Tier-III Rs 1.5–7.5 million at 7% — with a new Tier-IV of Rs 7.5–25 million at 8% approved by the Economic Coordination Committee on 4 November 2026 and ratified by the federal cabinet, plus an interest-free Tier-V for laptops and overseas workers (Dawn, 11 November 2026; The News, November 2026).

The scheme is large. By 31 December 2025 the State Bank of Pakistan recorded 461,795 loans disbursed worth Rs 220.9 billion, cumulative from January 2023 (SBP, PMYBALS Quarterly Data Tables, December 2025). Press reporting of official statistics to June 2026 puts the total at Rs 288 billion to 570,290 beneficiaries (The Express Tribune, November 2026). The FY2026-27 disbursement target is Rs 292 billion — more than the scheme disbursed in its entire first three years. And it is expensive: the SBP estimates the subsidy at Rs 38 billion on Rs 250 billion of disbursement in the current fiscal year, against Rs 21 billion budgeted (Tribune, November 2026).

Yet no published evaluation asks the scheme's central question: does subsidised youth credit create youth enterprises? The SBP publishes disbursement counts and amounts by tier, not outcomes — no business survival rate, no jobs created, no district breakdown, no follow-up of borrowers. This paper performs the audit that the published data permit: it computes the concentration of disbursements across tiers, the subsidy cost per rupee, the non-performing-loan profile by tier, and the only enterprise signal available — SECP company registrations and Labour Force Survey youth unemployment — and tests the scheme's stated purpose against them. It then applies the Islamic policy lens the programme's own principles require: the prohibition of riba (Qur'an 2:275–279), 'adl — justice in distribution (Qur'an 4:135) — and the maqasid test of whether public money serves the public interest (maslaha).

## 2. Methods

**Analysis plan (stated before results).** Before any computation, the plan was: (1) take the SBP's quarterly PMYBALS tables as the authoritative source and compute, for each tier, the share of borrowers, the share of money, the average loan, and the non-performing-loan (NPL) rate by amount and by count; (2) derive quarterly disbursement flows by differencing cumulative totals; (3) cross-check the press-reported June 2026 totals against the scheme's own loan caps for arithmetic consistency; (4) compare the enterprise outcome proxies (SECP registrations, LFS youth unemployment) against the disbursement series; (5) compute the subsidy rate and the budget gap from the SBP's published estimates. No post-hoc analysis was added after seeing the results; the inconsistency check in step (3) was pre-specified because press totals and SBP tables use different reporting dates.

**Data sources.** SBP PMYBALS Quarterly Data Tables as of 31 March 2025, 30 June 2025, 30 September 2025 and 31 December 2025 (SBP, sbp.org.pk and archive.sbp.org.pk); The Express Tribune, "Farming leads PM's youth loan drive" (November 2026, reporting official statistics to June 2026); Dawn, "Cabinet, ECC sanction new tier-4 category for PM loan scheme" (11 November 2026); The News, "Revised structure of PM's youth business loan more beneficial" (November 2026); SECP press statement via Business Recorder / Centreline (11 January 2026); Pakistan Bureau of Statistics, Labour Force Survey 2024-25, as reported by Dawn, The News and Geo (November 2025).

**Islamic canon consulted.** Qur'an 2:275–279 (riba), 4:135 ('adl), 42:38 (shura), 2:30 (khilafah/stewardship), 9:60 (zakat); Al-Shatibi, *Al-Muwafaqat* (maqasid al-shariah); Al-Ghazali, *Al-Mustasfa*; Ibn Khaldun, *Muqaddimah* (1377, Rosenthal translation, Princeton, 1958), ch. 3 (state expenditure and dynastic cycles); Chapra, *Islam and the Economic Challenge* (1992); Siddiqi, *Banking Without Interest* (1983); Usmani, *An Introduction to Islamic Finance* (2002). These works were consulted through the verified holdings named in the programme's Islamic-thought literature map; no Qur'anic verse or classical passage is quoted from memory — all citations are to the named surah:ayah or named book.

**Method standard.** Banerjee & Duflo's RCT programme (*Poor Economics*, 2011) is the template for the proposed causal test; Chetty et al.'s Opportunity Atlas (NBER Working Paper 25147, 2018) is the template for publishing the underlying data as a public tool; Acemoglu, Johnson & Robinson (*American Economic Review*, 2001) are the template for finding variation no one can manipulate; Thaler & Sunstein (*Nudge*, 2008) are the template for small, tested design changes over grand reform. None of these scholars is a co-author and none endorses this paper.

**Limitations of method (stated here, expanded in §6).** The SBP publishes no district-level disbursement data and no borrower outcomes. All enterprise tests in this paper are therefore ecological — national aggregates against national aggregates — and the identification is association only.

## 3. Results

### 3.1 Concentration: two-thirds of the money to one-tenth of the borrowers

As of 31 December 2025 (SBP, cumulative from January 2023), 461,795 loans had been disbursed for Rs 220,948 million — an average loan of Rs 478,455. The tier breakdown is stark:

| Tier | Borrowers | Share of borrowers | Amount (Rs m) | Share of money | Avg loan (Rs) | NPL by amount | NPL by count |
|---|---|---|---|---|---|---|---|
| Tier-I (≤ Rs 0.5m, 0%) | 395,504 | 85.6% | 52,340.6 | 23.7% | 132,339 | 0.24% | 0.32% |
| Tier-II (Rs 0.5–1.5m, 5%) | 15,545 | 3.4% | 20,620.9 | 9.3% | 1,326,529 | 3.78% | 5.60% |
| Tier-III (Rs 1.5–7.5m, 7%) | 50,746 | 11.0% | 147,986.5 | 67.0% | 2,916,220 | 0.44% | 2.65% |
| **Total** | **461,795** | **100%** | **220,948.0** | **100%** | **478,455** | **0.70%** | **0.75%** |

Three facts follow. First, **the interest-free tier is where the youth are, but the money is elsewhere**: 85.6% of borrowers share 23.7% of the money, while 11.0% of borrowers in Tier-III take 67.0%. Second, **76.3% of all money disbursed is lent at fixed interest** (Tiers II and III combined) — the scheme's financial core is interest-bearing credit, not the interest-free Tier-I that dominates its public presentation. Third, the average Tier-III loan is **22.0 times** the average Tier-I loan (Rs 2,916,220 vs Rs 132,339). Agriculture dominates the large end: of total disbursements, agriculture loans were Rs 115,541.5 million (52.3%) against Rs 105,406.5 million for SME/business loans.

### 3.2 The pace is accelerating — and the target exceeds the history

Quarterly disbursement flows, derived by differencing the SBP's cumulative totals, accelerated through 2025: Rs 13,832.7 million in Q4 FY2024-25 (April–June 2025), Rs 22,169.2 million in Q1 FY2025-26, and Rs 23,874.2 million in Q2 FY2025-26. Press-reported totals to June 2026 imply a further Rs 67.1 billion disbursed to 108,495 borrowers in the first half of 2026 (average Rs 618,019). The FY2026-27 target of Rs 292 billion is 1.01 times the entire cumulative disbursement of the scheme's first three years (Rs 288 billion) — the government plans to lend in one year what it lent in three.

### 3.3 The non-performing-loan profile: the middle tier defaults most

Overall NPLs are low: 3,469 loans (0.75% by count) and Rs 1,555.1 million (0.70% by amount) at December 2025. But the profile is uneven. Tier-II — small shops, workshops and farm upgrades at 5% — carries the worst repayment record by a wide margin: 5.60% of Tier-II loans by count and 3.78% by amount are non-performing, against 0.32%/0.24% in Tier-I and 2.65%/0.44% in Tier-III. The middle of the scheme, not the top or the bottom, is where credit discipline breaks down. (One caution: the SBP's own tables show NPL amounts moving non-monotonically — Rs 1,263.0 million at June 2025, Rs 1,722.3 million at September 2025, Rs 1,555.1 million at December 2025 — and the SBP disclaimer notes figures vary with revisions and reversals; the tier ranking, however, is stable across all four quarters.)

### 3.4 The enterprise test: no signal in the only outcomes published

Two outcome series exist. **Company registrations**: SECP recorded 35,087 new companies in FY2024-25, up 27.4% from 27,542 in FY2023-24, with 21,542 more in the first half of FY2025-26 and the registry passing 258,000 companies. But SECP attributes the growth to its own digitisation reforms — 99.9% of incorporations processed online — not to the loan scheme, and most PMYBALS borrowers are sole proprietors and farmers who never register a company. Registrations therefore cannot be credited to the scheme without district-level matching, which the SBP does not publish. **Youth unemployment**: the LFS 2024-25 records youth (15–24) unemployment at 12.6%, up 1.5 percentage points from 11.1% in 2020-21, while the scheme disbursed Rs 174.9 billion by June 2025. The number of unemployed persons rose from 4.5 million to 5.9 million over the same interval. A youth-enterprise scheme that coincides with *rising* youth unemployment has not demonstrated its mechanism; at minimum, the burden of proof has not been met. Both tests are ecological and association-only — but the scheme's defenders, not its critics, bear the burden of producing borrower-level outcome data.

### 3.5 Data-quality audit: the reported concentration figures do not add up

Press reporting of official statistics to June 2026 states that Rs 102 billion — over 35% of all loans — went to 3,957 agriculture borrowers taking loans "in the range of Rs 1.5 million to Rs 7.5 million" at 7%, and that Rs 193 billion (67%) went to 24,362 borrowers in the maximum-loan category (Tribune, November 2026). Both claims are arithmetically inconsistent with the scheme's own caps:

- 3,957 borrowers × Rs 7.5 million (the Tier-III ceiling) = **Rs 29.7 billion maximum** — against Rs 102 billion claimed, a **3.44× gap**. The implied average loan is Rs 25.8 million, more than triple the legal maximum.
- 24,362 borrowers × Rs 7.5 million = **Rs 182.7 billion maximum** — against Rs 193 billion claimed; the implied average of Rs 7.92 million also exceeds the cap.

Possible explanations — multiple loans per borrower, misreported borrower counts, or a reporting error — cannot be distinguished from the published figures, and the government has published no correction. The SBP's own tier tables (Table 3.1) are internally consistent and are therefore the evidentiary basis of this paper; the press-reported figures are cited here only as a data-quality finding. Either the concentration is even worse than the SBP tables show, or the official statistics released to the press are wrong. Both possibilities demand the same remedy: publish borrower-level, district-level data.

### 3.6 The subsidy: 15 paisa in every rupee

The SBP estimates the subsidy at Rs 38 billion on Rs 250 billion of disbursement for the current fiscal year — **15.2% of every rupee lent** — against Rs 21 billion budgeted, a **Rs 17 billion (45%) funding gap** (Tribune, November 2026). At the FY2026-27 target of Rs 292 billion, the same subsidy rate implies roughly Rs 44 billion of taxpayer money in a single year, with no published estimate of jobs or enterprises created per rupee of subsidy. For comparison, the entire subsidy bill now rivals the annual development budget of a small province — spent without a published cost-per-enterprise figure.

## 4. Discussion

### 4.1 Mechanism: why the money concentrates

The mechanism is structural, not accidental. Tier-III loans require bank-policy security and an 80:20 debt-equity ratio for new businesses (SBP, PMYBALS terms); collateral and equity screen out exactly the asset-poor young people the scheme names as its beneficiaries, while favouring established farmers and businesses that can post security. Agriculture's 52.3% share of disbursements, and the press-reported concentration among large agriculture borrowers, follow from the same design: land is collateral, and collateral is what banks can lend against. The scheme therefore functions less as youth-enterprise finance and more as subsidised agricultural and SME credit routed through a youth label — a classic case of what Banerjee & Duflo warn against: a programme whose targeting mechanism defeats its targeting intent, measurable only because the SBP publishes tier tables.

### 4.2 Comparison vs the strongest incumbent

The strongest incumbent is not "no scheme" but the scheme's own Tier-I: interest-free, collateral-light (personal guarantee), reaching 85.6% of borrowers with the lowest default rate in the programme (0.24% by amount). Tier-I is also the only tier that is unambiguously compatible with the Islamic prohibition of riba. The honest comparison is therefore Tier-I against Tiers II–IV: the interest-free tier reaches eight times as many borrowers per rupee of subsidy, defaults less, and needs no theological defence. The new Tier-IV (Rs 7.5–25 million at 8%) moves the scheme further in the opposite direction — larger loans, higher rates, more collateral — and should be judged against Tier-I's record, not against nothing.

### 4.3 The Islamic lens

Four principles bear on the scheme, and on each the evidence points the same way:

- **Riba (Qur'an 2:275–279).** "Allah has permitted trade and has forbidden interest." Tiers II, III and the new Tier-IV charge fixed interest of 5%, 7% and 8% — 76.3% of all money disbursed. The state's subsidy pays the difference between the borrower's rate and the bank's KIBOR-plus margin; the subsidy makes interest cheaper, it does not remove it. A scheme that is three-quarters interest-bearing cannot be presented as consistent with the prohibition; the interest-free Tier-I and Tier-V show the alternative already exists inside the same programme.
- **'Adl — justice (Qur'an 4:135).** "Stand out firmly for justice, as witnesses to Allah, even if it be against yourselves, your parents, and your relatives." A subsidy is a public transfer. When 67% of subsidised credit reaches 11% of borrowers — and the largest borrowers are established agriculturalists with land collateral — the transfer is regressive: public money subsidises those who already hold assets. The 'adl test asks who bears the burden and who takes the benefit; here the benefit concentrates at the top.
- **Maqasid and maslaha (Al-Ghazali, *Al-Mustasfa*; Al-Shatibi, *Al-Muwafaqat*).** Public policy must preserve life (nafs), intellect ('aql) and wealth (mal) and secure genuine public benefit. A Rs 38 billion annual subsidy with no published outcome measure — no enterprises counted, no jobs counted, no survival rate — fails the maslaha test of accountability: benefit that cannot be measured cannot be claimed. Hifz al-mal cuts both ways: it protects the borrower's wealth, but also the public purse.
- **Shura (Qur'an 42:38) and Ibn Khaldun's fiscal warning.** Decisions are to be taken by consultation; no published consultation with borrowers, youth organisations or Islamic-finance scholars accompanies the scheme's revisions, including the November 2026 Tier-IV expansion. Ibn Khaldun (*Muqaddimah*, ch. 3) warned that state expenditure grows as dynasties age and that rising exactions shrink the base that pays them — the scheme's subsidy bill growing from Rs 21 billion budgeted to Rs 38 billion estimated, while the FY2026-27 target exceeds three years of lending, is the pattern he described: expenditure that expands faster than the revenue and the results that justify it.

The Islamic alternative is not to abolish youth finance but to restructure it on risk-sharing: a **musharakah youth fund** in which the state shares profit and loss with the young entrepreneur instead of charging fixed interest (Chapra, *Islam and the Economic Challenge*, 1992; Siddiqi, *Banking Without Interest*, 1983; Usmani, *An Introduction to Islamic Finance*, 2002). Under musharakah the state's return depends on the enterprise succeeding — which aligns the state's incentive with the outcome the scheme claims to want, and which automatically concentrates state attention on the smallest borrowers, since a profit-share in a failed large loan loses public money. Zakat and waqf instruments (Qur'an 9:60) can fund the smallest, collateral-free tier outright as grants for the poorest applicants, where even an interest-free loan is a burden.

## 5. Policy Implications

**Decision-maker 1 — the Prime Minister's Youth Programme (PMYP) and the Ministry of Finance.** Before the Rs 292 billion FY2026-27 target is released: (a) publish district-level disbursement and borrower-outcome data (business survival at 12 and 24 months, jobs created) as open data, on the Chetty model of publishing the data as a public tool; (b) cap any single borrower's cumulative subsidised borrowing and publish the concentration ratio quarterly; (c) freeze Tier-IV disbursements until the arithmetic inconsistency in the reported June 2026 figures (§3.5) is corrected in public. If district data show no positive association between per-youth disbursement and enterprise formation, the target should be cut and the money redirected to Tier-I. **Islamic principle:** 'adl and maslaha — public money must be shown to benefit the public, with the burden of proof on the spender.

**Decision-maker 2 — the State Bank of Pakistan.** Add three fields to the quarterly PMYBALS tables: district, borrower age band, and 24-month business-survival status. The tables already exist and are published quarterly; the marginal cost is small and the accountability gain is large. **Islamic principle:** shura — the public cannot consult on what it cannot see.

**Decision-maker 3 — the Ministry of Finance and the SBP Shariah governance framework.** Pilot a musharakah youth window alongside Tiers II–IV: identical eligibility, but the state takes a profit-share instead of fixed interest, with the return capped and losses shared. Randomise eligible applicants between the musharakah window and the standard interest-bearing tiers (the Banerjee & Duflo template) and measure business survival and repayment at 24 months. If the musharakah arm survives at least as well, convert the scheme's growth funding to risk-sharing. **Islamic principle:** the riba prohibition (Qur'an 2:275–279) requires an alternative, not only a criticism — Chapra (1992) and Usmani (2002) supply the design.

**Decision-maker 4 — the Auditor General of Pakistan.** Audit the June 2026 concentration figures: reconcile the reported Rs 102 billion to 3,957 borrowers against the Rs 7.5 million loan cap, and publish the reconciliation. A 3.44× arithmetic gap in official statistics released to the press is itself a finding that requires an answer. **Islamic principle:** hifz al-mal — stewardship of public wealth (Qur'an 2:30, khilafah) begins with accurate accounts.

## 6. Limitations

1. **Association only.** No district-level or borrower-level data are published, so no causal claim is made. The concentration finding is arithmetic on official aggregates; the enterprise finding is ecological. A district panel could overturn the enterprise conclusion — which is why the paper's first recommendation is to publish one.
2. **Press-reported totals are inconsistent (§3.5).** The June 2026 totals come from press reporting of official statistics, not from a published SBP table. If the SBP's own June 2026 table, when published, differs, the figures in §3.2 and §3.5 must be revised — and the inconsistency itself would remain a finding about statistical reporting.
3. **Outcome proxies are indirect.** SECP registrations capture only incorporated companies; most youth enterprises are sole proprietorships. LFS youth unemployment reflects the whole economy, not the scheme's borrowers. The paper claims only that the scheme has not demonstrated its effect on the outcomes its own purpose implies — not that it has no effect.
4. **NPL figures are revised.** The SBP disclaimer notes figures vary with revisions and reversals; the September-to-December 2025 fall in NPL amounts illustrates this. Tier rankings are stable across quarters, but point estimates should be read with the revision caveat.
5. **Islamic canon gaps (named, per the programme's sweep rule).** This paper consulted the Qur'an, Al-Shatibi, Al-Ghazali, Ibn Khaldun, Chapra, Siddiqi and Usmani as named in the literature map. It did **not** consult: Al-Mawardi's *Al-Ahkam al-Sultaniyya* (constitutional theory of public finance) in full; the classical fiqh literature on qard hasan (benevolent loans) beyond the modern summaries; or the State Bank's own Shariah-board rulings on subsidised lending, which are not published in accessible form. A fuller treatment would read Al-Mawardi on the treasury (bayt al-mal) and the modern AAOIFI Shariah standards on musharakah; their absence is a gap, not a claim that they were read.

## 7. Conclusion

Pakistan's youth loan scheme is big, expensive and unevaluated. On the State Bank's own tables, 67% of its money reaches 11% of its borrowers, 76% of its money is lent at fixed interest, the middle tier defaults at fifteen times the rate of the interest-free tier, and the subsidy costs the taxpayer 15 paisa per rupee lent — while youth unemployment rose through the scheme's first three years and the official concentration figures released to the press are arithmetically impossible under the scheme's own loan caps. The interest-free Tier-I, which reaches 85.6% of borrowers with the lowest default rate, shows the scheme already contains its own best design. The honest next step is not a bigger target — the Rs 292 billion FY2026-27 target exceeds the scheme's entire three-year history — but published district-level outcomes, a corrected statistical record, and a randomised musharakah pilot that tests whether risk-sharing finance serves young Pakistanis better than subsidised interest. Until those exist, the claim that the scheme creates youth enterprises is unproven, and the subsidy is a transfer whose beneficiaries are, on the evidence, the borrowers who needed it least.

---

## References

1. State Bank of Pakistan. Prime Minister's Youth Business & Agriculture Loan Scheme (PMYB&ALS): Quarterly Data Tables as of 31 December 2025. SBP, 2026. https://archive.sbp.org.pk/publications/Quarterly/PMYB/PMYB&ALS%20Data%20tables%20-%20December%202025.pdf
2. State Bank of Pakistan. PMYB&ALS Quarterly Data Tables as of 30 September 2025. SBP, 2025. https://archive.sbp.org.pk/publications/Quarterly/PMYB/PMYB&ALS%20Data%20Tables%20-%20September%202025.pdf
3. State Bank of Pakistan. PMYB&ALS Quarterly Data Tables as of 30 June 2025. SBP, 2025. https://www.sbp.org.pk/assets/document/publications/Jun-2025_1.pdf
4. State Bank of Pakistan. PMYB&ALS Quarterly Data Tables as of 31 March 2025. SBP, 2025. https://www.sbp.org.pk/assets/document/publications/Mar-2025.pdf
5. The Express Tribune. "Farming leads PM's youth loan drive." November 2026. https://tribune.com.pk/story/2640881/farming-leads-pms-youth-loan-drive
6. Dawn. "Cabinet, ECC sanction new tier-4 category for PM loan scheme." 11 November 2026. https://epaper.dawn.com/DetailImage.php?StoryImage=11_11_2026_004_004
7. The News. "Revised structure of PM's youth business loan more beneficial." November 2026. https://www.thenews.pk/print/1448040-revised-structure-of-pm-s-youth-business-loan-more-beneficial
8. Business Recorder. "SECP records 35,000 company incorporations in FY2024-25." July 2025. https://www.brecorder.com/news/40371744
9. Pakistan Bureau of Statistics. Labour Force Survey 2024-25. Islamabad: PBS, 2025. As reported in Dawn, "1.4m more jobless in four years," November 2025; The News, "Unemployment rate up from 6.3% in 2020-21 to 7.1% in 2024-25," November 2025.
10. Banerjee AV, Duflo E. *Poor Economics: A Radical Rethinking of the Way to Fight Global Poverty.* New York: PublicAffairs, 2011.
11. Acemoglu D, Johnson S, Robinson JA. "The Colonial Origins of Comparative Development: An Empirical Investigation." *American Economic Review* 91(5), 2001, 1369–1401.
12. Chetty R, Friedman JN, Hendren N, Jones M, Porter SR. "The Opportunity Atlas: Mapping the Childhood Roots of Social Mobility." NBER Working Paper 25147, October 2018.
13. Thaler RH, Sunstein CR. *Nudge: Improving Decisions about Health, Wealth, and Happiness.* New Haven: Yale University Press, 2008.
14. Heckman JJ. "Schools, Skills, and Synapses." *Economic Inquiry* 46(3), 2008, 289–324.
15. The Holy Qur'an 2:275–279 (riba); 4:135 ('adl); 42:38 (shura); 2:30 (khilafah); 9:60 (zakat).
16. Al-Shatibi I. *Al-Muwafaqat fi Usul al-Shari'a.* 8th c. AH; English trans. Nyazee, Garnet, 2012.
17. Al-Ghazali. *Al-Mustasfa min 'Ilm al-Usul.* c. 1109.
18. Ibn Khaldun. *Muqaddimah* (1377). Trans. Rosenthal F. Princeton: Princeton University Press, 1958.
19. Chapra MU. *Islam and the Economic Challenge.* Leicester: Islamic Foundation, 1992.
20. Siddiqi MN. *Banking Without Interest.* Leicester: Islamic Foundation, 1983.
21. Usmani MT. *An Introduction to Islamic Finance.* The Hague: Kluwer Law International, 2002.

---

## Data availability

All numbers in this paper are computed from the sources listed in the References: the SBP's published PMYBALS quarterly tables (Refs 1–4), press reporting of official statistics (Refs 5–8), and the PBS Labour Force Survey 2024-25 as reported in the national press (Ref 9). Derived quantities — tier shares, average loans, quarterly flows, NPL rates, subsidy rates, and the cap-consistency checks — are arithmetic on those published figures and are reproducible from the tables in §3. No borrower-level or district-level data were available; the SBP does not publish them. All computations were performed in Python 3 on 21 November 2026; the computation log is retained with the author's working files. No data were invented.

*AI-assisted draft — NOT peer-reviewed, NOT published. All claims require independent verification.*
