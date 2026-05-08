# Raw Agreement, Kappa, and Skewed Base Rates

Amir's question was:

> How should I interpret and report inter-rater agreement when the base rate is skewed, and does a kappa of 0.46 undermine the benchmark's credibility?

The short answer: do not report raw agreement alone, but do not let Cohen's kappa alone carry the whole story either. For this protocol, the defensible report is observed agreement, base rates, contingency tables, Cohen's kappa, and a prevalence-aware companion statistic such as Gwet's AC1 or PABAK. Also fix the terminology: because the same rater labeled the tasks twice, this is intra-rater reliability, not true inter-rater agreement.

## First Fix The Protocol Name

If one person labels the same tasks twice after a 24-hour gap, the protocol measures intra-rater test-retest reliability: how consistently one evaluator applies the rubric over time.

It does not measure inter-rater agreement, which would require two or more independent raters scoring the same examples. That matters because a rubric can be consistent for its author but still unclear to another evaluator. So the reliability section should say:

> We measured intra-rater test-retest reliability over two labeling passes, not inter-rater agreement across independent raters.

That does not make the result useless. It makes the claim narrower.

## What Raw Agreement Tells You

Raw agreement answers:

> On what fraction of items did the two passes give the same label?

For Amir's data, that number is 91.7%: 76 agreements out of 83 dimension-task pairs. That is useful because it means only 7 pairs changed labels.

But raw agreement ignores how easy agreement is when almost every label is "correct." If pass 1 marks 92.7% as correct and pass 2 marks 90.2% as correct, then chance agreement from the marginal rates is already high:

```text
chance agreement = (0.927 * 0.902) + (0.073 * 0.098)
                 ~= 0.844
```

That means the 91.7% headline is only about 7.3 percentage points above the expected base-rate agreement. Raw agreement is not wrong; it is incomplete.

## What Cohen's Kappa Adds

Cohen's kappa asks:

> How much agreement remains after subtracting expected chance agreement?

```text
kappa = (observed agreement - expected chance agreement)
        / (1 - expected chance agreement)
```

With Amir's numbers:

```text
kappa ~= (0.917 - 0.844) / (1 - 0.844)
      ~= 0.46
```

Kappa is doing something valuable: it reveals that much of the raw agreement is explained by the skewed label distribution. That is exactly why reviewers expect chance-corrected metrics.

But kappa also has a known weakness. Under extreme prevalence, it can look surprisingly low even when observed disagreement is small. This is the kappa paradox: high agreement, low or moderate kappa. So kappa is not "wrong," but it needs prevalence context.

## Concrete Demonstration

The central mechanism is inspectable from the arithmetic:

| Quantity | Value | Meaning |
| --- | ---: | --- |
| Observed agreement | 91.7% | Actual match rate across passes |
| Expected chance agreement | 84.4% | Match rate implied by skewed marginals |
| Above-chance gap | 7.3 points | Extra agreement beyond prevalence |
| Cohen's kappa | 0.46 | Normalized above-chance agreement |
| PABAK | 0.834 | `2 * observed agreement - 1` |

This table shows why one number is not enough. Raw agreement says the rater was mostly stable. Kappa says the label distribution makes that stability less impressive than 91.7% sounds. PABAK shows how a prevalence-adjusted companion can look much closer to the practical match rate.

## What To Report

For this protocol, report a bundle:

| Metric | What it answers |
| --- | --- |
| Observed agreement | How often did the two passes match? |
| Base rates by pass | How skewed were the labels? |
| Cohen's kappa | How much agreement remains after marginal-rate chance correction? |
| Gwet's AC1 or PABAK | Does agreement still look strong under prevalence-aware adjustment? |
| Contingency table | Where did disagreements actually occur? |
| Specific agreement | Is agreement stable for both "correct" and "incorrect" labels? |

The revised writeup should not say, "91.7% proves the rubric is well-specified." A stronger version is:

```markdown
We measured intra-rater test-retest reliability, not inter-rater agreement.
Observed agreement was 91.7% (76/83). Because labels were highly skewed
toward "correct" (92.7% in pass 1, 90.2% in pass 2), expected chance
agreement was 84.4%. Cohen's kappa was 0.461. We therefore report kappa
with prevalence context and add Gwet's AC1 or PABAK plus per-dimension
contingency tables.
```

## What About Workflow Correctness?

`workflow_correctness` has the lowest raw agreement at 84.6%, so treat it as a diagnostic flag. But the statistic alone cannot decide whether the rubric is ambiguous or the task is inherently difficult.

Review the disagreement cases. If flips cluster around multi-step edge cases, implicit workflow steps, or recovery behavior, the dimension may need examples rather than a new metric. If the rater cannot reconstruct the rule behind the flips, the rubric is underspecified.

## Final Takeaway

Kappa 0.46 does not automatically destroy Tenacious-Bench's credibility. It does undermine a simple "91.7% agreement proves the rubric works" headline. The credible claim is narrower and stronger: one rater was mostly consistent, the label distribution was highly skewed, kappa shows the chance-agreement problem, and prevalence-aware metrics plus disagreement review are needed before making a broad rubric-quality claim.
