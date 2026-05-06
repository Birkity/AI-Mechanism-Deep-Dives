# Sources

## Canonical Sources

1. OpenAI. "Introducing Structured Outputs in the API"  
   https://openai.com/index/introducing-structured-outputs-in-the-api/

2. Saibo Geng, Martin Josifoski, Maxime Peyrard, and Robert West. "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning"  
   https://aclanthology.org/2023.emnlp-main.674/

3. Brandon T. Willard and Remi Louf. "Efficient Guided Generation for Large Language Models"  
   https://arxiv.org/abs/2307.09702

4. OpenAI Cookbook. "Introduction to Structured Outputs"  
   https://cookbook.openai.com/examples/structured_outputs_intro

## Tool or Pattern Used

- Toy constrained-decoding demonstration: compare raw next-token probabilities with a schema-valid token mask, then renormalize the remaining valid probabilities. This makes the mechanism visible without requiring an API key.

## Sources intentionally dropped from the main Day 2 list

- Brown et al. 2020, "Language Models are Few-Shot Learners" - valid paper, but only background for prompting and not directly about schema-constrained decoding.
- Lewis et al. 2020, "Autoregressive Entity Retrieval" - valid paper, but not central to this explainer unless the post discusses constrained entity-name generation.
- Broad OpenAI Cookbook and Azure OpenAI documentation homepages - useful documentation entry points, but less precise than the specific Structured Outputs sources above.
