"""Derived quantities for 2026-11-07 Space paper (FLIP archive forecast).
Inputs: published values in Table 1 of the manuscript. Re-run: python3 flip-archive-forecast-2026-11-07.py
"""
import math
# HWO residual stability gap: requirement 100-1000x / FLIP gain 2-15x
print("HWO gap best: 100/15 =", round(100/15, 1), " worst: 1000/2 =", round(1000/2, 1))
print("log10 gap:", round(math.log10(100/15), 2), "to", round(math.log10(1000/2), 2))
# Clopper-Pearson one-sided 95% lower bound, k=1 success in n=1 trial:
# P(X>=1|p) = 1-(1-p) = p = 0.05  ->  p_low = 0.05
p_low = 0.05
for n in (20, 59):
    print(f"P(>=1 recovery in {n} datasets at p=0.05) =", round(1-(1-p_low)**n, 4))
print("rule of three, 0 in 59: 3/59 =", round(3/59, 4))
# 3/3 lower bound (dropout screen prior)
print("p_low for 3/3 =", round(0.05**(1/3), 3))
# Capotauro: mu = 132 mas / 3.5 yr; v_t = 4.74 * mu(" /yr) * d(pc)
mu = 132/3.5/1000
vt = 4.74*mu*730
print("mu =", round(mu*1000, 1), "mas/yr; v_t =", round(vt, 1), "km/s; +-15% =", round(vt*0.15, 1))
print("parallax at 730 pc =", round(1000/730, 2), "mas; distance ly =", round(730*3.26156), "+/-", round(110*3.26156))
# JADES surface density
print("JADES all/Y per arcmin2:", round(41/309.5, 3), round(10/309.5, 4))
# FLIP compute budget for 20 datasets
print("20 x 35 min =", round(20*35/60, 1), "GPU-hours on 1x A30")
