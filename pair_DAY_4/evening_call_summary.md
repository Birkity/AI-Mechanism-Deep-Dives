# Evening Call Summary

- Date: Day 4, Week 12
- Participants: Birkity Yishak and Amir Ahmedin

The main feedback was that the reliability answer should not choose between raw agreement and kappa as if one number could settle the question. What landed: the combined reporting pattern (observed agreement + base rates + kappa + AC1 or PABAK), the protocol-name correction (intra-rater test-retest, not inter-rater agreement), and the explicit chance arithmetic showing 84.4% expected agreement from the marginal rates.

What required follow-up and is now addressed in the updated explainer:

- **PABAK mechanism:** the formula 2Po − 1 is Cohen's kappa evaluated under a fixed Pe = 0.5 (balanced prevalence). It removes the skew distortion but assumes the imbalance is a measurement artifact rather than a real property of the task distribution.
- **Gwet's AC1 computed:** AC1 uses average proportions across both passes as its chance estimate (Pe ≈ 0.156), producing AC1 ≈ 0.902 on Amir's data — a much more favorable reading than kappa's 0.46, because AC1's Pe does not inflate from the skewed marginals the way kappa's does.
- **workflow_correctness threshold:** at estimated κ ≈ 0.3, the dimension falls in the "fair" band and should not be used as the sole training signal. The updated explainer includes a kappa-band decision table (slight / fair / moderate / substantial) with concrete actions.
- **Code demonstration:** `reliability_metrics.py` computes all three metrics from Amir's actual numbers, satisfying the challenge spec requirement for a concrete engineering demonstration.
- **Methodology threshold problem:** the current >80% raw agreement threshold is below the 84.4% chance agreement floor, meaning any rubric passes regardless of quality. The updated explainer recommends converting the threshold to κ ≥ 0.4 per dimension or setting a raw floor above chance.
