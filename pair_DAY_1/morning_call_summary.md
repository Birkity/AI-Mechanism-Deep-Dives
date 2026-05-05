Morning Call Summary

- Date: 2026-05-04
- Participants: Birkity Yishak, Beamlak Adane
- What was ambiguous and how it was sharpened:
	For my question, the first draft (“why does the model ignore early instructions?”) was too broad and risked collapsing into generic prompt-engineering tips.
	We reframed it as a decode-phase, token-level question: how the attention logits/softmax over a long prefix shift toward recency, how positional effects (e.g., RoPE at long distances) and attention sinks can pull probability mass away from early rubric tokens, and what that means for the effective influence of initial instructions.
	We also separated “model behavior” from “inference optimization”: KV cache and prefix/prompt caching mostly change compute/latency, not attention probabilities, but context-management choices around caching (truncation, summarization, partial replay) can indirectly change fidelity.

	For Beamlak’s question, we clarified that the real gap is not “prompting for caution” in general, but the inference-time mechanism: how uncertainty cues shift the next-token distribution and how decoding controls (temperature and top-p) change the odds that cautious downgrade tokens win versus overconfident commitment tokens.
	We tied both questions to concrete Week 11 artifacts (judge/rubric stability; Sales Agent Evaluation Bench overcommitment penalty) so the resulting explainers can lead to defensible portfolio edits.