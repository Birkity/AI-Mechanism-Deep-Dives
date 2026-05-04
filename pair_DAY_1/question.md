Question

My question (Birkity Yishak)

- Final question:
	In long, multi-turn evaluator loops (LLM-as-a-judge) and agent sessions, the model can gradually stop following the initial system rules/rubric even when those instruction tokens are still present in the context window.

	Mechanism: during late decode steps, what happens to the attention logits and softmax distribution over a long prefix that makes early “anchor” tokens (system prompt / rubric) contribute less to the next-token prediction than more recent tokens? Concretely, how do recency effects, RoPE/positional effects at long distances, and “attention sinks” (high-attention tokens that attract probability mass) show up at the token level, and what does that imply for instruction influence over time?

	Inference optimizations: what do KV caching and prefix/prompt caching change (compute/latency) versus not change (the model’s attention probabilities and behavior), and in what situations can caching-related design choices (e.g., truncation, summarization, partial context replay) indirectly worsen or improve instruction fidelity?

	Engineering: beyond simply increasing context length, what practical mechanisms can an engineer use to preserve instruction fidelity and judge consistency across extended sessions (e.g., re-anchoring strategies, rubric/state representation, session segmentation, constrained outputs), and what tradeoffs do they introduce?

- Connection to Week 10/11 artifact:
	The evaluator/judge prompt + rubric we used in Week 11 for scoring model outputs (and any long multi-turn agent evaluation loop where we assumed the judge would keep following the original rules).

- Why this gap matters:
	If early rubric tokens lose practical influence, the judge becomes inconsistent over long conversations, undermining evaluation reliability and making our “grade” or “ranking” results hard to defend.

Partner question I will work on (Beamlak Adane)

- Final question:
	In my Week 11 Sales Agent Evaluation Bench, I penalize bench_overcommitment (hard delivery commitments when signals are weak) and reward outputs that downgrade to phased discovery / handoff. What I do not understand (and cannot defend) is the inference-time mechanism behind this behavior: how prompt conditioning, the model’s token probability distribution under uncertainty, and decoding choices (temperature / top-p) interact to produce cautious downgrade tokens (phased/scope/discovery/handoff) versus overconfident commitment tokens (immediately/this week/we can deploy).

	Concretely: at decode time, what changes in the next-token distribution when the prompt introduces uncertainty signals, and how do temperature and nucleus sampling affect whether “safe” versus “confident” tokens win early in the completion?

- Connection to Week 10/11 artifact:
	Week 11 Sales Agent Evaluation Bench rubric, specifically the bench_overcommitment penalty and the preference for phased discovery/handoff.

- Why this gap matters:
	If we can’t explain how decoding and uncertainty conditioning drive cautious vs overconfident tokens, we can’t defend our evaluation design choices or tune generation settings to reduce overcommitment in production.