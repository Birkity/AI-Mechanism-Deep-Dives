Sources

Canonical Sources

1) Vaswani et al. (2017), "Attention Is All You Need" — https://arxiv.org/abs/1706.03762
2) Liu et al. (2023), "Lost in the Middle: How Language Models Use Long Contexts" — https://arxiv.org/abs/2307.03172

Tool or Pattern Used

- Attention-weight inspection pattern using `output_attentions=True` (Transformers-style APIs) to measure how much attention mass later tokens allocate to early “anchor” token spans over time.