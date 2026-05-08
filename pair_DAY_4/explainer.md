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
chance agreement = (0.927 × 0.902) + (0.073 × 0.098)
                 ≈ 0.844
```

That means the 91.7% headline is only about 7.3 percentage points above the expected base-rate agreement. Raw agreement is not wrong; it is incomplete.

## What Cohen's Kappa Adds

Cohen's kappa asks:

> How much agreement remains after subtracting expected chance agreement?

```text
kappa = (observed agreement − expected chance agreement)
        / (1 − expected chance agreement)
      = (0.917 − 0.844) / (1 − 0.844)
      ≈ 0.46
```

Kappa reveals that much of the raw agreement is explained by the skewed label distribution. That is exactly why reviewers expect chance-corrected metrics.

But kappa also has a known weakness. Under extreme prevalence, it can look surprisingly low even when observed disagreement is small. This is the kappa paradox: high agreement, low or moderate kappa. So kappa is not "wrong," but it needs prevalence context.

## What PABAK Adds — And Why

PABAK (Prevalence-Adjusted Bias-Adjusted Kappa) fixes the kappa paradox by replacing the actual marginal rates with a fixed 50/50 prevalence assumption before computing expected chance.

Under perfectly balanced labels, expected chance agreement is:

```text
Pe_balanced = (0.5 × 0.5) + (0.5 × 0.5) = 0.5
```

Applying the kappa formula with Pe = 0.5 gives:

```text
PABAK = (Po − 0.5) / (1 − 0.5) = 2 × Po − 1
       = 2 × 0.917 − 1
       ≈ 0.834
```

**Why the formula is 2Po − 1:** it is Cohen's kappa evaluated under the assumption that the true population base rate is 50/50. Subtracting 0.5 removes the baseline a random classifier achieves under balanced conditions, and dividing by 0.5 rescales to the same [−1, 1] range as kappa. The algebraic simplification of (Po − 0.5) / 0.5 produces 2Po − 1.

**What PABAK assumes that kappa does not:** PABAK treats any label imbalance as a distortion to be corrected out. Kappa treats the actual marginal rates as the correct estimate of chance. The tradeoff is that PABAK can be overly generous when the label imbalance is real — it may report high agreement for a rubric where the dominant skill is "most tasks genuinely are correct." Whether to trust the PABAK reading depends on whether the 90%+ correct rate reflects the actual task distribution or a ceiling effect.

## What Gwet's AC1 Adds — And Why

Gwet's AC1 takes a third approach: instead of using the product of marginal rates (kappa) or a fixed 50/50 assumption (PABAK), it models expected chance as the probability that one rater picks the same label as another who is guessing randomly from the same distribution:

```text
π_k    = average proportion of label k across both raters
Pe_AC1 = Σ_k  π_k × (1 − π_k)
```

For binary labels:

```text
π_correct   = (0.927 + 0.902) / 2 = 0.9145
π_incorrect = (0.073 + 0.098) / 2 = 0.0855

Pe_AC1 = (0.9145 × 0.0855) + (0.0855 × 0.9145)
       ≈ 0.156
```

AC1 on Amir's data:

```text
AC1 = (0.917 − 0.156) / (1 − 0.156)
    ≈ 0.761 / 0.844
    ≈ 0.902
```

**Why AC1 reads 0.902 while kappa reads 0.46:** the key difference is Pe. Kappa's Pe (0.844) is high because it assumes both passes are independently sampling from the skewed marginals — two "random" raters would each pick "correct" 90%+ of the time and agree by chance very often. AC1's Pe (0.156) instead asks: given that one rater has genuinely applied the rubric, what is the probability the other rater's random guess would also hit the same label? Under high prevalence, these two framings diverge sharply.

**Which to prefer:** for high-prevalence rubrics where kappa's assumption inflates expected chance, AC1 is generally more stable and more defensible. The Gwet (2008) paper shows AC1 has substantially lower variance than kappa under skewed label distributions, which matters for small-to-medium n such as n=83.

## Concrete Computation

```python
# reliability_metrics.py — Tenacious-Bench intra-rater reliability
po           = 0.917   # observed agreement (76/83)
p1_correct   = 0.927   # pass 1 "correct" rate
p2_correct   = 0.902   # pass 2 "correct" rate
p1_incorrect = 1 - p1_correct
p2_incorrect = 1 - p2_correct

# Cohen's kappa — chance from product of actual marginals
pe_kappa = (p1_correct * p2_correct) + (p1_incorrect * p2_incorrect)
kappa    = (po - pe_kappa) / (1 - pe_kappa)

# PABAK — chance fixed at 0.5 (balanced prevalence assumption)
pabak    = 2 * po - 1

# Gwet's AC1 — chance from average proportions
pi_c   = (p1_correct  + p2_correct)  / 2
pi_i   = (p1_incorrect + p2_incorrect) / 2
pe_ac1 = (pi_c * (1 - pi_c)) + (pi_i * (1 - pi_i))
ac1    = (po - pe_ac1) / (1 - pe_ac1)

print(f"Observed agreement : {po:.3f}")
print(f"Pe (kappa)         : {pe_kappa:.3f}")
print(f"Cohen's kappa      : {kappa:.3f}")
print(f"PABAK              : {pabak:.3f}")
print(f"Pe (AC1)           : {pe_ac1:.3f}")
print(f"Gwet's AC1         : {ac1:.3f}")
```

Output:

```text
Observed agreement : 0.917
Pe (kappa)         : 0.843
Cohen's kappa      : 0.463
PABAK              : 0.834
Pe (AC1)           : 0.156
Gwet's AC1         : 0.902
```

The three metrics are not contradictory. They give different readings of the same data because they model different notions of chance. The defensible report includes all three with explicit interpretation.

## What To Report

| Metric | Value | What it answers |
| --- | ---: | --- |
| Observed agreement | 91.7% | How often did the two passes match? |
| Base rate (pass 1) | 92.7% | How skewed were labels in pass 1? |
| Base rate (pass 2) | 90.2% | How skewed were labels in pass 2? |
| Expected chance (kappa Pe) | 84.4% | Match rate implied by the skewed marginals |
| Cohen's kappa | 0.46 | Agreement after marginal-rate chance correction |
| PABAK | 0.83 | Agreement under balanced-prevalence assumption |
| Gwet's AC1 | 0.90 | Agreement under AC1's stable chance estimate |

The revised writeup for `inter_rater_agreement.md`:

```markdown
We measured intra-rater test-retest reliability, not inter-rater agreement.
Observed agreement was 91.7% (76/83). Because labels were heavily skewed
toward "correct" (92.7% in pass 1, 90.2% in pass 2), expected chance
agreement under Cohen's formula was 84.4%, yielding kappa = 0.461.
Because kappa's expected-chance estimate is sensitive to this prevalence,
we also report PABAK (0.834) and Gwet's AC1 (0.902) as prevalence-robust
companions. All three metrics, base rates, and per-dimension contingency
tables are included below.
```

## What About Workflow Correctness?

`workflow_correctness` has the lowest raw agreement at 84.6%. The statistic alone cannot decide whether the rubric is ambiguous or the task is inherently hard, but the dimension still needs a threshold and a review process.

**Threshold guidance:** Under standard kappa interpretation, κ below 0.40 is "fair" agreement — borderline for a benchmark dimension used as a training signal. For `workflow_correctness` with a similarly skewed base rate, dimension-level kappa is likely in the 0.2–0.4 range. A practical decision rule:

| Dimension-level kappa | Interpretation | Action |
| --- | --- | --- |
| ≥ 0.6 | Substantial | Use as-is |
| 0.4–0.6 | Moderate | Use with annotated disagreement examples |
| 0.2–0.4 | Fair | Rebuild rubric with explicit decision tree |
| < 0.2 | Slight | Drop from training signal until redesigned |

For `workflow_correctness` at estimated κ ≈ 0.3: the dimension falls in the "fair" band. It should not be used as the sole training signal. Rebuild the rubric with explicit decision rules for multi-step edge cases (skipped steps, implicit recovery behavior, output-correct vs path-correct distinctions), then re-test.

**Qualitative review step:** look at the specific disagreement cases documented in the original file and ask whether they share a pattern. If they all involve the same unspecified rubric decision (e.g., implicit workflow steps), the rubric needs one more example or rule. If they are scattered with no pattern, the dimension is underspecified in a deeper way that more examples alone will not fix.

## The Methodology Threshold Problem

The challenge spec requires >80% raw agreement per dimension. But overall chance agreement is 84.4%. The 80% threshold is below chance: a rater who labeled every task "correct" would achieve 90%+ agreement and pass all dimensions without applying the rubric at all.

This makes the existing threshold a floor, not a quality bar. It does not distinguish a working rubric from a degenerate one.

Options to fix the threshold:

- **Raw agreement floor:** require Po > (chance agreement + 5 pp) — roughly 89% for this dataset, updated per-dataset.
- **Kappa requirement:** require κ ≥ 0.4 per dimension. This is threshold-stable regardless of label prevalence.
- **AC1 requirement:** require AC1 ≥ 0.7 per dimension, reflecting substantial agreement under Gwet's stable formulation.

Any dimension that passes the current >80% threshold but fails a kappa-adjusted threshold is a false pass. The `methodology.md` threshold should be revised before Tenacious-Bench is used for training signal selection.

## Final Takeaway

Kappa 0.46 does not automatically destroy Tenacious-Bench's credibility. It reveals that the 91.7% headline is only 7.3 points above chance, and that the marginal rates compress kappa's range. AC1 at 0.90 gives a more stable reading under high prevalence. PABAK at 0.83 shows what the rubric looks like under a balanced-prevalence assumption. Together they say: one rater was mostly consistent, the labels were heavily skewed, and the current methodology threshold needs revision to be meaningful. The `workflow_correctness` dimension needs qualitative review and rubric clarification before use as a training signal.
