Thread (4-6 Posts)

1) Ever notice an LLM judge / agent stops following the *system rubric* in long chats, even though the rubric tokens are still in the context? It’s not “memory loss” — it’s attention competition during decode.

2) At each new token, attention weights are a softmax over *all* prior tokens: scores come from $q_t \cdot k_i$ (plus positional effects). As the chat grows, anchors must stay highly relevant to keep winning probability mass.

3) Recent turns often match the current query better than old rubric text, so attention shifts locally. Some heads become strongly recency-biased (especially with long distance / positional behavior), so early rule tokens get less effective influence.

4) “Attention sinks” complicate this: some early tokens (like BOS / first tokens) can stay heavily attended by many heads. That can preserve a stable routing hub — but it doesn’t guarantee *your specific rule tokens* remain the ones getting attention.

5) KV cache + prefix caching mostly change *speed/cost*, not the math. Drift is usually about which tokens win attention at decision time (and whether truncation/summarization silently removed or rewrote the rules).

6) Practical fix: make rules recent at the decision point. Re-inject a short rubric reminder (cheap with prefix caching), use a 2-pass judge (extract rubric items → score), and constrain outputs (JSON/checklist) to force consistent rubric use.