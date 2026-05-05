Sources

Canonical Sources

1) Holtzman et al. (2019), "The Curious Case of Neural Text Degeneration" (nucleus/top-p sampling background) — https://arxiv.org/abs/1904.09751
2) Hugging Face Transformers documentation (generation parameters: temperature, top_p, greedy vs sampling) — https://huggingface.co/docs/transformers/main/en/generation_strategies

Tool or Pattern Used

- Decoding sweep + logprob inspection pattern: run the same prompt across a grid of `temperature` and `top_p`, label overcommitment vs downgrade outputs, and (when your API supports token logprobs) track logprob mass for commitment cues vs downgrade cues.