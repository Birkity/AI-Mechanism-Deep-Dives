# Evening Call Summary

- Status: Completed
- Participants: Birkity Yishak and Melkam Beyene

## What landed

Melkam's explainer landed well because it answered my core Day 2 question directly: a reasoning chain before a verdict does not automatically prove that the reasoning caused the verdict. The most useful part was the intervention framing: corrupt, remove, reorder, or replace intermediate reasoning steps and then measure whether the final verdict changes in the expected direction. That gave me a concrete way to test whether my judge's signal-direction, ICP, and pitch-frame steps are load-bearing or post-hoc.

My explainer for Melkam also went well because it made the mechanism behind structured outputs concrete. The distinction between prompt-only control as probability nudging and schema-constrained decoding as invalid-token masking helped clarify why schemas reduce malformed outputs more reliably than instructions like "return valid JSON."

## What needed tightening

The main point to tighten was the boundary between reliable structure and reliable judgment. For my question, we clarified that autoregressive dependence is not the same as faithful reasoning. For Melkam's question, we clarified that schema constraints can enforce valid output shape, but they do not prove the verdict, evidence, or reasoning is semantically correct.

## Revisions made

I updated the Day 2 explainer and blog draft to emphasize the token-level mechanism: prompts shift probabilities, while schemas mask invalid continuations and renormalize the remaining valid probabilities. I also added the limitation that structured outputs guarantee form, not truth, and tied the lesson back to Week 10/11 judge outputs such as verdict, rubric dimension, confidence, evidence, and failure reason. Melkam's explanation closed my reasoning-faithfulness gap, and my structured-output explanation closed her schema-constrained decoding gap.
