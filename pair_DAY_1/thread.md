Thread (4-6 Posts)

1) In my Sales Agent Eval Bench, I penalize “overcommitment” (hard delivery promises on weak signals). But why does the same model sometimes say “we can deploy this week” and other times downgrade to “discovery / phased plan”?

2) Mechanism: at each step, the model samples the next token from a probability distribution (softmax over logits). Under uncertainty, the top options are *close* → the distribution is flatter → small decoding changes can flip the outcome.

3) Temperature reshapes the distribution. Low temperature / greedy decoding strongly exploits the top token → if “commitment” wording is slightly ahead, it tends to win consistently. Higher temperature explores more alternatives → “downgrade” tokens become more likely to appear.

4) Top-p (nucleus) sampling chooses from the smallest set of tokens whose cumulative probability exceeds $p$. When the model is uncertain, that set gets larger — meaning more phrasing options survive, including cautious alternatives.

5) Practical engineering: make judges deterministic (greedy or very low temperature), separate evidence extraction from the commitment decision (two-stage judge), and/or constrain outputs (explicit `commitment_type` field).

6) How to verify: hold the prompt fixed and sweep `temperature` and `top_p`. If your API supports logprobs, compare logprob mass on commitment cues (“deploy”, “this week”) vs downgrade cues (“discovery”, “phase”, “handoff”).