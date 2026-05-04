Twitter Thread (6 tweets)

1/6 Why do LLMs sometimes sound overconfident, and other times cautious — on the *same task*?

It’s often not “mood” or “personality.” A lot of it is decided at inference time.

2/6 LLMs generate one token at a time.
At each step, the model has a probability distribution over possible next tokens.

Under weak evidence, “commitment” tokens (deploy, this week, guaranteed) can be close in probability to “downgrade” tokens (discovery, phase, scope, handoff).

3/6 Three things shape which cluster wins:
(1) Prompt conditioning (your instructions + evidence)
(2) Uncertainty (flat vs sharp next-token distribution)
(3) Decoding settings (temperature, top‑p)

4/6 Temperature: lower temperature (or greedy decoding) exploits the top token more aggressively.

So if confident wording is even slightly ahead, low temperature can make “hard commitment” phrasing happen consistently.

Higher temperature explores more alternatives — which can let cautious language surface.

5/6 Top‑p (nucleus sampling) keeps the smallest set of tokens whose cumulative probability exceeds p.

When the model is uncertain, that set grows, meaning more alternatives survive — including cautious phrases that might otherwise get cut off.

6/6 Why this matters: in my Week 11 Sales Agent Evaluation Bench, I penalize `bench_overcommitment` and reward phased discovery/handoff.

If decoding changes the language, it changes your benchmark outcomes.

Takeaway: for evaluators/judges, prefer deterministic decoding (or structure the decision) before trusting the scores.