# Sources

## Canonical Sources

1. Jacob Cohen, "A Coefficient of Agreement for Nominal Scales"  
   https://doi.org/10.1177/001316446002000104  
   Original Cohen's kappa paper; useful for explaining chance-corrected agreement.

2. Alvan R. Feinstein and Domenic V. Cicchetti, "High agreement but low kappa: I. The problems of two paradoxes"  
   https://doi.org/10.1016/0895-4356(90)90058-L  
   Canonical source for the kappa paradox under skewed prevalence and marginal imbalance.

3. Kilem L. Gwet, "Computing inter-rater reliability and its variance in the presence of high agreement"  
   https://doi.org/10.1348/000711006X126600  
   Source for Gwet's AC1 as an alternative reliability coefficient under high agreement and prevalence imbalance.

4. Terry Byrt, Janet Bishop, and John B. Carlin, "Bias, prevalence and kappa"  
   https://doi.org/10.1016/0895-4356(93)90018-V  
   Source for prevalence-adjusted bias-adjusted kappa (PABAK) and prevalence/bias interpretation.

5. Jochen Kottner et al., "Guidelines for Reporting Reliability and Agreement Studies (GRRAS)"  
   https://doi.org/10.1016/j.jclinepi.2010.03.002  
   Reporting guidance for reliability studies, including clear distinction between intra-rater and inter-rater designs.

6. C. K. Chow, "On Optimum Recognition Error and Reject Tradeoff"  
   https://research.ibm.com/publications/on-optimum-recognition-error-and-reject-tradeoff  
   Relevant to Birkity's abstention question: classification with a reject option creates an accuracy-coverage tradeoff.

7. Yonatan Geifman and Ran El-Yaniv, "SelectiveNet: A Deep Neural Network with an Integrated Reject Option"  
   https://proceedings.mlr.press/v97/geifman19a.html  
   Modern selective prediction source for thinking about risk-coverage reporting when models abstain.

## Tool or Pattern Used

- Reliability reporting bundle: report observed agreement, base rates, chance-corrected agreement, prevalence-robust agreement, contingency tables, and qualitative disagreement review.
- Protocol naming check: distinguish intra-rater test-retest reliability from inter-rater agreement across independent raters.
- Risk-coverage reporting: for abstaining models, report coverage, answered-case accuracy, full-set accuracy, and abstention rates by slice.
