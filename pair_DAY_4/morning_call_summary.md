# Morning Call Summary

- Date: Day 4, Week 12
- Participants: Birkity Yishak and Amir Ahmedin
- Topic: Evaluation statistics — abstention reporting and intra-rater reliability

**My question (Birkity):** Sharpened from a general concern about abstentions into a denominator problem. The core question became: when a model skips or fails to parse some fraction of evaluation tasks, answered-case accuracy is conditional on the model choosing to answer. That makes it a reliable estimate only when abstentions are random. If abstentions cluster on harder task types — e.g., the model abstains more on complex multi-step tasks — conditional accuracy overestimates true reliability by hiding the hardest cases in the abstention bucket. The diagnostic: does the abstention rate vary by task slice? If yes, full-set accuracy (treating abstentions as failures) and coverage must be reported alongside answered-case accuracy.

**Amir's question:** Sharpened from "is 91.7% agreement good?" into a measurement question. The numbers already in hand — 92.7% "correct" in pass 1, 90.2% in pass 2, kappa 0.461 — tell a specific story: the 91.7% headline is only 7.3 points above the chance agreement the marginal rates alone would produce (84.4%). Whether that gap is defensible depends on which notion of "chance" is correct: Cohen's formula (Pe = 0.844, kappa = 0.46), PABAK's balanced-prevalence assumption (Pe = 0.5, PABAK = 0.834), or Gwet's average-proportion formula (Pe = 0.156, AC1 = 0.902).

We agreed the protocol should be named intra-rater test-retest reliability, not inter-rater agreement, because the same rater labeled the same tasks twice after a 24-hour gap. That distinction narrows the claim: consistent for its author does not mean clear to another evaluator.

**What was agreed:**
- My evaluation needs coverage and abstention-by-slice reporting before answered-case accuracy can be trusted as the main reliability claim.
- Amir's report needs the protocol name corrected, the full metric bundle (raw agreement + base rates + kappa + PABAK + AC1 + contingency tables), and a revised methodology threshold — the current >80% raw agreement requirement is below the 84.4% chance floor and does not distinguish a working rubric from a degenerate one.
- The `workflow_correctness` dimension at 84.6% raw agreement requires qualitative disagreeement review and a kappa-based decision rule before use as a training signal.
