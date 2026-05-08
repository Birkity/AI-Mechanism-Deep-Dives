# Grounding Commit

- Artifact pointer:
  - Repo-visible update: [portfolio_update.md](../portfolio_update.md)
  - Day 4 explainer: [explainer.md](explainer.md)
  - Day 4 source list: [sources.md](sources.md)
  - Day 4 reliability computation: [reliability_metrics.py](reliability_metrics.py)
  - Day 4 blog: [When 91.7% Agreement Isn't the Whole Story](https://sprout-krill-3c0.notion.site/When-91-7-Agreement-Isn-t-the-Whole-Story-35afb8a6541b8047bdacf807e4522f6d?source=copy_link)
  - Day 4 thread: [x.com](https://x.com/BYishak24169/status/2052730818569658810)

- What changed and why:

Day 4 grounds the evaluation-statistics discussion back into the Week 10/11 judge and benchmark work. The portfolio update now adds coverage-aware reporting for abstentions and prevalence-aware reliability reporting for agreement studies. For my evaluator work, abstentions and unparseable outputs should not disappear from the metric; I should report coverage, answered-case accuracy, full-set accuracy, and abstention rates by task slice. For Amir's Tenacious-Bench reliability work, the report should describe the same-rater protocol as intra-rater test-retest reliability and include observed agreement, base rates, Cohen's kappa, Gwet's AC1 or PABAK, contingency tables, and qualitative review of `workflow_correctness` disagreement cases.
