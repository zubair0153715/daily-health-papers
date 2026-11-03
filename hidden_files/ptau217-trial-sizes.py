"""Prevention-trial sample sizes under plasma p-tau217 enrichment.
Source: Buckley et al., JAMA 2026;336(11):950-959, PMID 42449500, PMCID PMC13370474.
Model-based 5-year absolute risks (Table 2, Cox model, g-formula standardisation):
  low (<-0.5 SD, ~<10 Centiloid)          12% (95% CI 9-15%)
  intermediate (-0.5 to <1.1 SD, ~10-24)  15% (12-17%)
  high (1.1 to <2.5 SD, ~25-60)           24% (20-28%)
  very high (>=2.5 SD, ~>60)              38% (33-43%)
Observed overall: 478/2684 = 17.8% progressed over median follow-up 5.4 y
  (used as the unselected-trial reference; approximate 5-year rate).
HRs: per 1-SD p-tau217 1.38 (1.30-1.46); high vs low 2.34 (1.60-3.44);
  very high vs low 4.66 (3.17-6.85). 5-year AUC 0.80 (0.77-0.83).
PACC slopes (units/year): low +0.03, intermediate +0.01, high -0.03, very high -0.07;
  very-high minus low = -0.10 (95% CI -0.13 to -0.07).
Two-proportion sample size per arm, two-sided alpha 0.05, power 80%:
  n = (Z_a/2*sqrt(2*pbar*qbar) + Z_b*sqrt(p1*q1 + p2*q2))^2 / (p1 - p2)^2
"""
import math

Z_A = 1.959964
Z_B = 0.841621

def n_per_arm(p1, p2):
    pbar = (p1 + p2) / 2.0
    num = (Z_A * math.sqrt(2 * pbar * (1 - pbar))
           + Z_B * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p1 - p2) ** 2)

def scenario(label, p1, rrr):
    p2 = p1 * (1 - rrr)
    n = n_per_arm(p1, p2)
    print(f"{label:32s} p1={p1:.3f} p2={p2:.4f} RRR={rrr:.0%}  n/arm={n:5d}  total={2*n:5d}  NNT5y={1.0/(p1-p2):.1f}")
    return n

print("Observed overall progression: 478/2684 =", round(478/2684, 4))
print("Very-high vs low 5-year risk ratio:", round(0.38/0.12, 2))
print("Very-high vs overall enrichment factor:", round(0.38/(478/2684), 2))
print("PACC slope gap (very high vs low):", round(-0.07-0.03, 2), "units/year;",
      "over 5 y =", round((-0.07-0.03)*5, 2), "units")
print()
print("--- 30% relative risk reduction, 5-year horizon, 80% power, alpha 0.05 ---")
scenario("Unselected (observed 17.8%)", 478/2684, 0.30)
scenario("Low p-tau217 (12%)", 0.12, 0.30)
scenario("Intermediate p-tau217 (15%)", 0.15, 0.30)
scenario("High p-tau217 (24%)", 0.24, 0.30)
scenario("Very high p-tau217 (38%)", 0.38, 0.30)
print()
print("--- Sensitivity: 25% RRR ---")
scenario("Unselected (observed 17.8%)", 478/2684, 0.25)
scenario("High p-tau217 (24%)", 0.24, 0.25)
scenario("Very high p-tau217 (38%)", 0.38, 0.25)
print()
print("--- Sensitivity: 95% CI bounds for very-high stratum, 30% RRR ---")
scenario("Very high, lower bound (33%)", 0.33, 0.30)
scenario("Very high, upper bound (43%)", 0.43, 0.30)
print()
print("--- Events expected per 1000 enrolled over 5 years ---")
for label, p in [("Unselected", 478/2684), ("Low", 0.12), ("Intermediate", 0.15),
                 ("High", 0.24), ("Very high", 0.38)]:
    print(f"{label:32s} {p*1000:.0f} events / 1000 enrolled")
print()
print("--- Saving relative to unselected (30% RRR) ---")
n_un = n_per_arm(478/2684, (478/2684)*0.70)
n_vh = n_per_arm(0.38, 0.38*0.70)
print(f"Very-high total {2*n_vh} vs unselected total {2*n_un}: "
      f"{100*(1 - 2*n_vh/(2*n_un)):.0f}% fewer participants")
