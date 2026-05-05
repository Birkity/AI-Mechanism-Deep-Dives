LinkedIn Post Draft

Why do LLMs sometimes sound overconfident, and other times sound cautious?

It’s not “personality drift.” A lot of the difference is decided at inference time.

When a model generates text, it picks the next token from a probability distribution (built from internal scores a.k.a. logits). Under weak evidence, “commitment” phrasing (deploy, this week, guaranteed) can be close in probability to “downgrade” phrasing (discovery, phase, scope, handoff).

Whether the output commits or downgrades often depends on:

1) Prompt conditioning: how your instructions and evidence shift token scores.
2) Uncertainty: how flat vs sharp the next-token distribution is.
3) Decoding: settings like temperature and top‑p.

Lower temperature (or greedy decoding) tends to exploit the top token more aggressively — so a small edge for confident wording can become a consistent “hard commitment.” Higher temperature or a wider top‑p keeps more alternatives alive, which can let cautious language surface.

Why it matters: in my Week 11 Sales Agent Evaluation Bench, I penalize `bench_overcommitment` and reward phased discovery/handoff. If decoding changes the language, it changes your benchmark outcomes.

Takeaway: for evaluators/judges, make decoding deterministic (or structure the decision) before you trust the scores.