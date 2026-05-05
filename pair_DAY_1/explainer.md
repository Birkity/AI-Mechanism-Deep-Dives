Inference-Time Mechanisms: Cautious vs Overconfident Language in LLMs

Large language models generate text token by token, using an internal probability distribution over the vocabulary at each step. These probabilities are computed from the model's logits (raw scores) via the softmax function. Softmax converts arbitrary real-valued logits into a normalized probability distribution. In practice, a higher logit means much higher probability: for example, the softmax of logits (1, 2, 8) is about (0.001, 0.002, 0.997), assigning almost all the weight to the largest score. In other words, softmax amplifies differences: if one token has the highest logit, even by a little, it tends to dominate the probability mass.

When the model is uncertain, however, the logits for many tokens can be similar, producing a flattened distribution. If no next-word stands out, several tokens might each get a sizable probability. In top-p (nucleus) sampling, this situation is recognized: when the model is confident, the cumulative probability can be met with few tokens; when it's uncertain (a flat distribution), the nucleus pool of top tokens must be much larger. In intuitive terms, a flat (high-entropy) distribution means the model is hedging among many options.

![alt text](image-1.png)
Figure: A hypothetical LLM probability distribution for the next token given the prompt "What's your favorite color?" Here "green" has ~50% and "red" ~30%, while other tokens like "a" and "the" have very low probability. Softmax of the model's logits produces this distribution.

Because probabilities are spread across many tokens when uncertain, it often helps to think in semantic clusters. Tokens with similar meaning (for example, synonyms or related phrases) often share probability mass. Phrases like "at once," "immediately," "right away" form a confident cluster, while "initially," "phase," "scope" form a cautious cluster. The LLM's softmax may allocate some probability to each cluster. If one cluster's tokens collectively have more total probability, the model is effectively more "sure" of that style. When probabilities are split more evenly, neither cluster clearly wins, reflecting model uncertainty.

Prompt Conditioning as Logit Nudging
The prompt influences these logits indirectly. When the prompt and any instructions are processed, they set up the model's initial hidden state (via token embeddings and transformer layers), which in turn affects all future logits. In effect, a prompt nudges the model's expectations: tokens that align with the prompt tend to start with higher logits. For example, a prompt saying "You are a cautious advisor..." will bias the model's internal state so that caution-related tokens get a leg up in probability. However, this influence is soft and distributed; it doesn't hard-code any word choice, it merely shifts logits.

Over a long generation, this prompt influence can decay. Transformers often give disproportionate attention to the first token(s) (sometimes called an attention sink), which acts as an anchor carrying prompt information. But as more tokens are generated, the model's focus tends to drift toward the new content and away from the original prompt. In other words, without mechanisms to re-inject the instructions, a long generated sequence will naturally rely more on its own recent tokens than on the distant prompt. This is why early prompt words can have a large initial effect (an "anchor"), but the explicit instructions can feel less potent later in the text.

Decoding Strategy Effects
At each step, once we have the probability distribution over tokens, the decoding strategy decides which token to output. With greedy decoding, the model always picks the highest-probability token. With sampling (stochastic decoding), the model instead draws the next token at random from the distribution, optionally using algorithms like temperature or nucleus filtering to modify it. These choices dramatically affect style:

- Temperature rescales the logits before softmax. Mathematically, we replace each logit z by z/T before softmax. When T < 1, we are dividing by a small number, making the differences larger (a peaked distribution). When T > 1, dividing by a larger number flattens the distribution. In summary, low temperature sharpens the distribution, favoring the highest-probability (high-confidence) tokens; high temperature flattens it, giving smaller-logit tokens a bigger chance. As a rule of thumb, low T leads to safe, repetitive or deterministic outputs (always exploiting the top choice), whereas high T produces more diverse, surprising outputs (exploring less likely words).

- Top-p (nucleus) sampling truncates the vocabulary to the smallest set of tokens whose total probability exceeds a threshold p. If the model is very sure, p might cover only a few tokens; if uncertain (flat distribution), p will include many tokens. Thus top-p dynamically adapts to confidence: it effectively allows a larger candidate set in low-confidence scenarios, giving fringe tokens (like cautious words) a chance to be sampled. In contrast, greedy or a small fixed top-k would ignore them. (For example, if the model assigns 75% cumulative to "immediately" phrases, a top-p of 0.9 would include some cautious tokens in the remaining 15%.)

Putting these together: a low temperature or strict filtering (low p) makes the model "play it safe" by sticking to the single most likely tokens. A higher temperature or looser filter spreads probability out, so tokens in the cautious cluster can survive sampling. In practice, using a low T (for example, 0.3) means the model almost always picks the highest-logit word ("we can deploy"), whereas a higher T (for example, 0.8) may pick a lower-logit word ("maybe we should scope") some of the time.

Combined Dynamics: Interaction Effects
When these factors combine, the outcome depends on how strong the signals are. Consider a prompt with weak evidence about timing. The model's logits for different outcomes might be relatively close (for example, logit of +2.0 for "deploy immediately" vs +1.8 for "phase-in plan"). Softmax turns these into probabilities that are not extremely lopsided. Now the decoding method decides which semantic cluster wins.

- With greedy or low-T sampling, the highest-logit choice ("immediately") will almost always win. Even a slight edge in probability is enough to consistently output the confident token, making the phrasing appear overconfident.
- With higher-T or top-p sampling, the gap is effectively reduced. The cautious token's chance increases. Sampling may then randomly pick the cautious phrase in some runs, so the model plugs cautious terms like "phase" or "discovery" some of the time. In effect, a flatter distribution and a permissive sampler let the underdog (cautious cluster) win occasionally.

Put another way, if the difference in logits between clusters is small, a small temperature bump or allowing more candidates can tip the balance. Conversely, if the prompt strongly favored a cluster (for example, an instructive "answer boldly"), the logits might be sharply in one cluster's favor, and changing T/p won't easily flip that.

Taken together: weak prompt signal -> flat distribution -> decoding choice decides which style appears. This is purely an inference effect, not a learned "rule": under high uncertainty, either cluster of tokens could win depending on sampling. Adjusting temperature or top-p will change how often the cautious cluster is chosen versus the overconfident cluster.

Prefill vs Decode Phase
It helps to distinguish the two stages of generation. In the prefill phase, the model processes the entire prompt in one forward pass to build its internal memory (the key/value caches). No tokens are output yet; the model is simply reading and encoding the prompt (and instructions) into its hidden state. In the decode phase, the model actually generates text one token at a time, using the cached prompt info plus the tokens generated so far. Each new token is chosen by applying softmax to the current logits and then sampling.

During decode, the initial prompt tokens remain in memory but the sequence grows. Each new token is then influenced by both the prompt (via the KV cache) and the previously generated tokens. In practice, because each generation adds more context, the relative weight of the original prompt in the attention mechanism can shrink, leading to the decay of prompt instructions over a long output.

In other words, prompt instructions set the stage at prefill, but during decode the model continually refines its state with newly generated content. Without explicit cues to stay on track, the influence of the original instruction can wane (especially if it was never strongly encoded into persistent context). This is why prompt-following can falter after many tokens.

Practical Diagnostics
An engineer can observe these effects by experiment. Use the same prompt and generate multiple outputs while varying the decoding parameters. For instance:

- Temperature sweep: Generate with a low T (for example, 0.1) and with a higher T (for example, 0.7 or 1.0). You will likely see that low-T outputs consistently use the strongest, most certain language ("We can deploy by next week."), whereas higher-T outputs may sometimes include weaker commitments ("Perhaps we should first scope the project"). If low-T generation feels like "always picking the obvious answer," try raising T, which should introduce more variety (and cautious phrasing) into the output.

- Top-p variation: Try a tight nucleus (for example, p = 0.6) versus a very loose one (for example, p = 0.95). With a small p, the model is restricted to its very highest-probability words, often yielding the most confident phrasing. A larger p allows more tokens in play, so if caution-language tokens were just outside the cutoff, they can now appear.

By observing how the style shifts, one can directly see that the model's confidence language is not a fixed trait but depends on how the probability mass is allocated and sampled. These diagnostics make it clear: the same prompt can yield either overconfident or cautious language depending on inference settings, confirming that it's an inference-time effect.

Decoding Sweep (Week 12 grounding commit)

Model: google/gemini-2.5-flash
Prompt mode: strict vs relaxed
Input: C:/Users/Ab/OneDrive/Desktop/10 Academy/Week 11/trp1-tenacious-bench-week11/data/tenacious_bench_v0.1/dev/dev_tasks.jsonl
Sample size (negative velocity): 8

Settings tested
- Low: T = 0.2, p = 0.7
- High: T = 0.9, p = 0.95

Results
- Strict prompt: no D3 flips observed.
- Relaxed prompt: D3 failed 1/8 (12%) in both low and high settings; growth-term hits 1/8 (12%).
- No clear temperature/top-p separation at n = 8.

Interpretation
- Decoding can surface growth-frame language when prompt constraints are relaxed, consistent with the mechanism described above.
- The signal is weak at n = 8; a larger sample or a second model is needed to test for a stable decoding-parameter effect.

Why This Generalizes
This mechanism is ubiquitous in any LLM-driven system that uses token sampling. In a conversational agent or multi-turn dialogue, the same softmax + sampling rules apply at each turn, so the choice between safe and risky language follows identical dynamics. As conversations grow long, prompt-decay issues only compound (each turn's output becomes part of the next prompt). Similarly, automated evaluators or reward models that penalize "overcommitment" will see models adjust phrasing if the underlying distribution changes. In short, any system relying on LLM generation will experience the tension between the most probable tokens and the exploratory tail of the distribution.

Even models trained for safety or politeness face the same inference tradeoffs: temperature and top-p still govern whether they stick to safe scripts or stray into bolder language. The difference lies only in where the baseline logits are. Thus, the safe-vs-risky phrasing phenomenon is not a quirk of one dataset or prompt, but a direct consequence of how LLMs decode under uncertainty.

In summary, overcommitment versus cautious tone is explained by inference-time probabilities and sampling. A weak prompt yields a flat softmax where both clusters of tokens vie for selection. The model's output then hinges on decoding knobs: low temperature/top-p hones in on the slight winner (often confident words), while higher temperature or looser filtering lets the alternative cluster (cautious words) sometimes win. This interplay is fully mechanistic: it comes from softmaxed token probabilities, prompt-conditioned logits, and the randomness induced by sampling. The result is that the same LLM, on the same prompt, can appear cautious or bold simply due to these inference settings, not because of some change in its underlying knowledge or training.
