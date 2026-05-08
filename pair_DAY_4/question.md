# Question

## My question (Birkity Yishak)

- Final question:

When a model abstains or returns unparseable output on some fraction of evaluation tasks, and you compute accuracy only over the tasks it answered, you are reporting a conditional estimate — "how often is it right, given that it tried." That number diverges from true reliability whenever abstentions cluster on specific task types rather than occurring at random. How do you detect whether abstentions are random or systematic, and how does that distinction change which accuracy number you should report and trust?:

- Connection to Week 10/11 artifact:

This connects to my Week 10/11 judge/evaluator work where structured verdicts, parser failures, refusals, and abstentions can change the denominator of reported accuracy. If I only score answered cases, I may overstate reliability by hiding the hardest cases in the abstention bucket.

- Why this gap matters:

If abstentions are random, conditional accuracy over answered tasks may be a useful estimate with a separate coverage number. If abstentions are systematic, conditional accuracy is biased toward easier slices and should not be trusted as the main reliability claim. I need a reporting pattern that separates coverage, answered-case accuracy, full-set accuracy, and abstention-by-slice diagnostics.

## Peer question I will explain: Amir Ahmedin

- Final question:

In my Week 11 Tenacious-Bench inter-rater agreement protocol (`inter_rater_agreement.md`), I report 91.7% raw agreement (76/83 dimension-task pairs) across two labeling passes on 30 tasks. The challenge spec requires >80% agreement per dimension, and all four dimensions pass: signal_accuracy 100%, tone_adherence 95.2%, resource_honesty 88.2%, workflow_correctness 84.6%. I present this as evidence that my rubric is well-specified.

**But raw agreement doesn't account for chance agreement. With a high base rate (92.7% of labels are "correct" in pass 1, 90.2% in pass 2), chance agreement is already 84.4%. My Cohen's kappa is 0.461 — "moderate" agreement, not the "almost perfect" my 91.7% headline implies. The 91.7% is only 7.3 percentage points above what I'd get by labeling everything "correct" without reading the tasks. How should I interpret and report inter-rater agreement when the base rate is this skewed — and does a kappa of 0.46 on my rubric actually undermine the benchmark's credibility, or is raw agreement the correct metric for this specific protocol (intra-rater consistency on a binary label with known high base rate)?**

A satisfying answer would tell me: (1) when kappa is the right metric vs when raw agreement is defensible (and which applies to my specific protocol — same rater, 24h gap, binary label), (2) whether 0.46 kappa on workflow_correctness specifically (the dimension with lowest agreement and the one that requires LLM judge) means my rubric is genuinely ambiguous or just that the task is inherently harder, and (3) what I should actually report in the inter-rater agreement section — raw agreement alone, kappa alone, both with interpretation, or a different metric entirely (e.g., prevalence-adjusted bias-adjusted kappa, PABAK).

- Connection to Week 10/11 artifact:

This connects to Amir's Week 11 Tenacious-Bench reliability reporting, especially `inter_rater_agreement.md`, `methodology.md`, `model_card.md`, `evaluation/scoring_evaluator.py`, and `tenacious-sales-bench/datasheet.md`.

- Why this gap matters:

If a benchmark reports only raw agreement under a heavily skewed label distribution, reviewers may mistake a high-looking percentage for strong reliability. But if it reports only Cohen's kappa, the prevalence paradox may make a stable rubric look weaker than it is. The benchmark needs a reporting pattern that is honest about base rates, chance correction, protocol type, and the hardest dimension.
