# Canonical List (Annotated)

## Papers

- Wei et al. (2022), "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"  
  https://arxiv.org/abs/2201.11903  
  Canonical background for why intermediate reasoning can improve task performance, while still leaving faithfulness as a separate question.

- Turpin et al. (2023), "Language Models Don't Always Say What They Think"  
  https://arxiv.org/abs/2305.04388  
  Important source for the gap between generated explanations and the model's true decision process.

- Hong et al. (2024), "ORPO: Monolithic Preference Optimization without Reference Model"  
  https://arxiv.org/abs/2403.07691  
  Core source for Day 3's ORPO chosen/rejected preference-learning mechanism.

- Rafailov et al. (2023), "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"  
  https://arxiv.org/abs/2305.18290  
  Canonical direct preference optimization source for understanding how preference pairs encode behavior.

- Meng, Xia, and Chen (2024), "SimPO: Simple Preference Optimization with a Reference-Free Reward"  
  https://papers.nips.cc/paper_files/paper/2024/hash/e099c1c9699814af0be873a175361713-Abstract-Conference.html  
  Relevant to judge training where sequence-level rewards can blur verdict correctness and explanation-format mimicry.

- Gardner et al. (2020), "Evaluating Models' Local Decision Boundaries via Contrast Sets"  
  https://aclanthology.org/2020.findings-emnlp.117/  
  Canonical pattern for testing whether models learned the intended boundary by changing one meaningful detail.

## Tools

- Schema-constrained decoding / Structured Outputs  
  https://openai.com/index/introducing-structured-outputs-in-the-api/  
  Enforces valid structured output forms at decode time, useful for judge verdict schemas and tool arguments.

## Patterns

- Reasoning intervention tests - apply to judge chains where intermediate steps may be post-hoc rather than causal.
- Near-miss rejection design - apply to ORPO/DPO preference datasets where easy negatives create shortcut learning.
- Contrast-set held-out evaluation - apply when the desired proof is that the model learned the semantic boundary, not surface artifacts.
- Grounded personalization checks - apply to SDR outreach models where every personalized claim should be supported by prompt evidence.
