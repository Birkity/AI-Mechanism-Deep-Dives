# Tenacious-Bench intra-rater reliability — computes kappa, PABAK, and Gwet's AC1
# Input: Amir's two-pass labeling data (83 dimension-task pairs, binary label)

po           = 0.917   # observed agreement (76/83)
p1_correct   = 0.927   # pass 1 "correct" rate
p2_correct   = 0.902   # pass 2 "correct" rate
p1_incorrect = 1 - p1_correct
p2_incorrect = 1 - p2_correct

# Cohen's kappa — chance from product of actual marginals
pe_kappa = (p1_correct * p2_correct) + (p1_incorrect * p2_incorrect)
kappa    = (po - pe_kappa) / (1 - pe_kappa)

# PABAK — chance fixed at 0.5 (balanced prevalence assumption)
# Equivalent to kappa under Pe = 0.5, simplifies to 2*Po - 1
pabak    = 2 * po - 1

# Gwet's AC1 — chance from average proportions across both passes
pi_c   = (p1_correct   + p2_correct)   / 2
pi_i   = (p1_incorrect + p2_incorrect) / 2
pe_ac1 = (pi_c * (1 - pi_c)) + (pi_i * (1 - pi_i))
ac1    = (po - pe_ac1) / (1 - pe_ac1)

print(f"Observed agreement : {po:.3f}")
print(f"Pe (kappa)         : {pe_kappa:.3f}  ← inflated by skewed marginals")
print(f"Cohen's kappa      : {kappa:.3f}  ← depressed by kappa paradox")
print(f"PABAK              : {pabak:.3f}  ← kappa under 50/50 prevalence assumption")
print(f"Pe (AC1)           : {pe_ac1:.3f}  ← stable under high prevalence")
print(f"Gwet's AC1         : {ac1:.3f}  ← prevalence-robust reading")
