"""
Chapter 2 — Extending Concepts (Hard Problems)
Ron Larson, Elementary Statistics 5th Ed.

Problems: 51 (Coefficient of Variation), 53 (Scaling Data), 57 (Pearson's Skewness)
"""

import numpy as np
from scipy import stats

print("=" * 70)
print("PROBLEM 51: Coefficient of Variation")
print("=" * 70)
print()
print("CV = (Standard deviation / Mean) × 100%")
print("Compare heights (inches) vs weights (pounds) of basketball players.")
print()

heights = np.array([72, 74, 68, 76, 74, 69, 72, 79, 70, 69, 77, 73])
weights = np.array([180, 168, 225, 201, 189, 192, 197, 162, 174, 171, 185, 210])

h_mean = np.mean(heights)
h_std = np.std(heights, ddof=1)  # sample std
h_cv = (h_std / h_mean) * 100

w_mean = np.mean(weights)
w_std = np.std(weights, ddof=1)
w_cv = (w_std / w_mean) * 100

print(f"Heights:  mean = {h_mean:.2f} in,  s = {h_std:.2f} in,  CV = {h_cv:.2f}%")
print(f"Weights:  mean = {w_mean:.2f} lb,  s = {w_std:.2f} lb,  CV = {w_cv:.2f}%")
print()
print(f"Conclusion: Heights (CV={h_cv:.1f}%) are LESS variable than")
print(f"weights (CV={w_cv:.1f}%) relative to their means.")
print(f"Even though weight has a larger std dev in absolute terms,")
print(f"the CV lets us compare across different units.")

print()
print("=" * 70)
print("PROBLEM 53: Scaling Data")
print("=" * 70)
print()
print("Annual salaries (thousands of dollars):")

salaries = np.array([42, 36, 48, 51, 39, 39, 42, 36, 48, 33, 39, 42, 45])

# (a) Original
mean_a = np.mean(salaries)
std_a = np.std(salaries, ddof=1)
print(f"\n(a) Original data:")
print(f"    x̄ = {mean_a:.1f} ($thousands),  s = {std_a:.2f} ($thousands)")

# (b) 5% raise: multiply each by 1.05
raised = salaries * 1.05
mean_b = np.mean(raised)
std_b = np.std(raised, ddof=1)
print(f"\n(b) After 5% raise (multiply by 1.05):")
print(f"    x̄ = {mean_b:.2f} ($thousands),  s = {std_b:.3f} ($thousands)")
print(f"    Note: x̄_new = x̄_old × 1.05 = {mean_a:.1f} × 1.05 = {mean_a*1.05:.2f} ✓")
print(f"    Note: s_new = s_old × 1.05 = {std_a:.2f} × 1.05 = {std_a*1.05:.3f} ✓")

# (c) Monthly salary: divide each by 12
monthly = salaries / 12
mean_c = np.mean(monthly)
std_c = np.std(monthly, ddof=1)
print(f"\n(c) Monthly salary (divide by 12):")
print(f"    x̄ = {mean_c:.3f} ($thousands),  s = {std_c:.4f} ($thousands)")
print(f"    Note: x̄_new = x̄_old / 12 = {mean_a:.1f} / 12 = {mean_a/12:.3f} ✓")
print(f"    Note: s_new = s_old / 12 = {std_a:.2f} / 12 = {std_a/12:.4f} ✓")

# (d) Conclusion
print(f"\n(d) CONCLUSION:")
print(f"    When you MULTIPLY (or divide) each data value by a constant c:")
print(f"      • The mean is multiplied (or divided) by c")
print(f"      • The standard deviation is multiplied (or divided) by |c|")
print(f"    In general: x̄_new = c · x̄_old,  s_new = |c| · s_old")

print()
print("=" * 70)
print("PROBLEM 57: Pearson's Index of Skewness")
print("=" * 70)
print()
print("P = 3(x̄ − median) / s")
print("P > 0 → skewed right,  P < 0 → skewed left,  P = 0 → symmetric")
print()

cases = [
    ("a", 17, 19, 2.3),
    ("b", 32, 25, 5.1),
    ("c", 9.2, 9.2, 1.8),
    ("d", 42, 40, 6.0),
]

for label, xbar, median, s in cases:
    P = 3 * (xbar - median) / s
    if P > 0:
        shape = "skewed RIGHT"
    elif P < 0:
        shape = "skewed LEFT"
    else:
        shape = "SYMMETRIC"

    print(f"({label}) x̄={xbar}, median={median}, s={s}")
    print(f"    P = 3({xbar} − {median}) / {s} = 3({xbar - median}) / {s} = {P:.4f}")
    print(f"    Shape: {shape}")
    print()

print("=" * 70)
print("BONUS: Problem 56 — Chebychev's Theorem")
print("=" * 70)
print()
print("At least 99% of data lies within how many standard deviations?")
print()
print("Solve: 1 - 1/k² ≥ 0.99")
print("       1/k² ≤ 0.01")
print("       k² ≥ 100")
print("       k ≥ 10")

k = np.sqrt(1 / (1 - 0.99))
print(f"\nk = √(1/(1-0.99)) = √(100) = {k:.1f}")
print(f"\nAnswer: At least 99% of data lies within {k:.0f} standard deviations of the mean.")
