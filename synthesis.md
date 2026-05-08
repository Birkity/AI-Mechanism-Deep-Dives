# Week 12 Synthesis

## Overview

Week 12 turned my Week 10/11 systems from things I could build into systems I can explain, defend, and test. The recurring pattern is that LLM reliability is rarely solved by a single better prompt or a single headline metric. It depends on knowing which boundary is being controlled: instruction influence, output structure, reasoning faithfulness, preference-pair semantics, coverage, or agreement.

Across four days, I closed eight concrete gaps: four I asked and four I explained for peers. The biggest shift in my thinking is that reliability claims need their denominators and mechanisms exposed. A structured output can guarantee parseable form, not truth. A reasoning chain can sound causal while being post-hoc. A preference pair can teach a shortcut if the rejected sample is too easy. An accuracy score can be biased if abstentions hide hard cases. A raw agreement score can be inflated by skewed base rates.

## Gaps Closed

1. **Day 1 - My gap: instruction/rubric drift in long judge loops.**  
   I learned why early system-prompt or rubric tokens can lose practical influence in long evaluator loops even when they remain in the context window. Recency effects, positional distance, attention allocation, and attention sinks can reduce the effective pull of early anchors. The engineering implication is that long judge sessions need re-anchoring, segmented state, structured rubric representation, and constrained outputs rather than faith that the first prompt stays equally influential forever.

2. **Day 1 - Peer gap I explained: cautious vs overconfident language at inference time.**  
   I explained how uncertainty signals and decoding settings shape whether a model emits cautious downgrade language or overconfident commitment language. The mechanism is the next-token distribution: weak evidence can flatten the distribution across semantic clusters, while temperature and top-p decide how much the decoder explores those alternatives.

3. **Day 2 - My gap: whether reasoning steps cause judge verdicts or rationalize them.**  
   I learned that autoregressive dependence is not the same as faithful reasoning. A verdict can be conditioned on generated reasoning without that reasoning reflecting the true decision process. The right test is intervention: corrupt, remove, reorder, or swap intermediate steps and check whether the verdict changes in the expected direction.

4. **Day 2 - Peer gap I explained: prompt constraints vs schema-constrained decoding.**  
   I explained that prompts softly shift probabilities while schema-constrained decoding masks invalid continuations to zero probability. This turns structured output from a writing preference into an interface contract. The limitation is equally important: schemas guarantee form, not semantic correctness.

5. **Day 3 - My gap: verdict signal vs explanation-pattern mimicry in preference-tuned judges.**  
   I learned that sequence-level preference optimization can reward a whole completion, so a judge may learn explanation style instead of the verdict boundary. The fix is to design training pairs and held-out tests that separate verdict correctness from rationale surface form through verdict-only metrics, rationale perturbations, contrast sets, and held-out formats.

6. **Day 3 - Peer gap I explained: near-miss rejections for grounded SDR personalization.**  
   I explained why total-failure rejected samples can teach ORPO a shallow anti-template rule instead of grounded personalization. Near-miss rejections are stronger because they sound plausible but fail one clear constraint, such as unsupported trigger, wrong entity, shallow personalization, misaligned offer, or overclaiming.

7. **Day 4 - My gap: conditional accuracy under abstention and unparseable outputs.**  
   I learned that answered-case accuracy is a conditional estimate: "how often the model is right, given that it tried." That number is trustworthy only when abstentions or parser failures are random with respect to task type and difficulty. If abstentions cluster on hard slices, the main report must include coverage, full-set accuracy, abstention-as-failure accuracy, and abstention rates by slice.

8. **Day 4 - Peer gap I explained: raw agreement, kappa, and skewed base rates.**  
   I explained why Amir's 91.7% raw agreement and 0.46 Cohen's kappa are not contradictions. Raw agreement is useful but inflated by a high "correct" base rate. Kappa exposes chance agreement but can be depressed under extreme prevalence. The defensible report is a bundle: observed agreement, base rates, contingency tables, Cohen's kappa, Gwet's AC1 or PABAK, and a clear statement that the protocol measured intra-rater reliability rather than true inter-rater agreement.

## Most Surprising Insight

The most surprising insight is that many evaluation failures are denominator failures. If a model abstains, the denominator changes. If a rubric has skewed labels, expected agreement changes. If a preference pair uses easy negatives, the semantic contrast changes. If a judge emits a clean schema, parseability improves but correctness still needs its own denominator and test set.

The practical lesson is to report the whole reliability surface, not one flattering slice. For model evaluation, that means coverage plus accuracy. For judges, that means structure plus semantic audits. For preference tuning, that means total failures plus near-misses. For agreement studies, that means raw agreement plus chance correction plus prevalence context.

## Canonical Reading List

- Wei et al. (2022), "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"  
  https://arxiv.org/abs/2201.11903

- Turpin et al. (2023), "Language Models Don't Always Say What They Think"  
  https://arxiv.org/abs/2305.04388

- OpenAI, "Introducing Structured Outputs in the API"  
  https://openai.com/index/introducing-structured-outputs-in-the-api/

- Hong et al. (2024), "ORPO: Monolithic Preference Optimization without Reference Model"  
  https://arxiv.org/abs/2403.07691

- Rafailov et al. (2023), "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"  
  https://arxiv.org/abs/2305.18290

- Meng, Xia, and Chen (2024), "SimPO: Simple Preference Optimization with a Reference-Free Reward"  
  https://papers.nips.cc/paper_files/paper/2024/hash/e099c1c9699814af0be873a175361713-Abstract-Conference.html

- Gardner et al. (2020), "Evaluating Models' Local Decision Boundaries via Contrast Sets"  
  https://aclanthology.org/2020.findings-emnlp.117/

- Cohen (1960), "A Coefficient of Agreement for Nominal Scales"  
  https://doi.org/10.1177/001316446002000104

- Gwet (2008), "Computing inter-rater reliability and its variance in the presence of high agreement"  
  https://doi.org/10.1348/000711006X126600

- Chow (1970), "On Optimum Recognition Error and Reject Tradeoff"  
  https://research.ibm.com/publications/on-optimum-recognition-error-and-reject-tradeoff

## Tool and Pattern List

- Reasoning intervention tests: corrupt, remove, reorder, or swap intermediate reasoning and check whether verdicts move.
- Structured judge outputs: enforce valid fields and enums so output form is reliable.
- Schema-constrained decoding: mask invalid continuations and renormalize over valid tokens.
- Near-miss rejection design: make rejected outputs almost correct but wrong on one target constraint.
- Contrast-set held-out evaluation: change one meaningful fact while holding style mostly constant.
- Verdict/rationale disentanglement eval: perturb explanation style while preserving the correct label.
- Risk-coverage reporting: report coverage, answered-case accuracy, full-set accuracy, and abstention-by-slice rates.
- Reliability reporting bundle: report raw agreement, base rates, kappa, AC1/PABAK, contingency tables, and disagreement review.
