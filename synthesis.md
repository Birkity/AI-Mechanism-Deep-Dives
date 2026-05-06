# Week 12 Synthesis

## Overview

Week 12 is turning my Week 10/11 systems from "things I shipped" into systems I can explain and defend. The pattern so far is clear: many reliability problems in LLM systems are not solved by better wording alone. They require knowing where the model is making a probabilistic generation choice, where the application needs a hard interface contract, and where an explanation may be persuasive without being causally faithful.

So far, Day 1 and Day 2 closed four concrete gaps: two I named and two I researched for peers. The biggest shift in my thinking is that evaluator reliability has two separate layers: the generated form must be controlled, and the judgment behavior must be tested. A structured output can make a judge easier to parse, but it cannot prove the judge is correct. A reasoning chain can make a verdict easier to read, but it cannot prove the reasoning caused the verdict.

## Gaps Closed

1. **Day 1 - My gap: instruction/rubric drift in long judge loops.**  
   I started with a concern that an LLM-as-a-judge might stop following early rubric instructions across long sessions even when those instructions remain in the context. The gap was about mechanism: how attention over long prefixes, recency effects, and attention sinks can reduce the practical influence of early anchor tokens. The explainer I received helped me understand why simply making the context window longer does not guarantee instruction fidelity. The portfolio implication is that long evaluator loops need re-anchoring, segmented state, structured rubric representation, or constrained outputs rather than assuming the original system prompt remains equally influential forever.

2. **Day 1 - Peer gap I explained: cautious vs overconfident language at inference time.**  
   I explained how prompt uncertainty and decoding settings affect whether a model emits cautious downgrade language or confident commitment language. The key mechanism is the next-token probability distribution: weak evidence produces a flatter distribution where multiple semantic clusters compete, and temperature/top-p decide how much the model exploits the top cluster versus samples from alternatives. This connected directly to the Week 11 Sales Agent Evaluation Bench and the `bench_overcommitment`/signal-direction rubric. The main takeaway was that confidence style can be an inference-time effect, not only a training-time property.

3. **Day 2 - My gap: whether reasoning steps cause judge verdicts or rationalize them.**  
   Melkam's explainer closed my gap about reasoning-chain faithfulness in judge formats. I now understand that autoregressive dependence is not the same as faithful reasoning: a verdict can be conditioned on earlier generated text without those steps reflecting the true decision process. The right way to test causality is intervention: corrupt, remove, reorder, or replace intermediate steps and measure whether the final verdict changes in the expected direction. If the verdict stays stable while the reasoning changes, the chain is likely acting as post-hoc rationalization. This means reordering or expanding a judge's reasoning format will only improve ambiguous-case accuracy if the steps are actually load-bearing and reused by the decision process, not merely more fluent.

4. **Day 2 - Peer gap I explained: prompt constraints vs schema-constrained decoding.**  
   I explained Melkam Beyene's question about why schema-defined outputs reduce invalid or unreliable outputs compared with prompt-only instructions. The core mechanism is token-level: prompts softly shift next-token probabilities, while schema-constrained decoding masks invalid continuations to zero probability and samples only from schema-valid tokens. This changes the output boundary from a writing preference into an interface contract. The important limitation is that schemas guarantee structure, not truth: they can force valid fields, enums, and JSON shape, but they do not prove the verdict or reasoning is correct.

5. **Day 3 - Pending.**  
   To be completed after the Day 3 pair work.

6. **Day 3 - Pending.**  
   To be completed after the Day 3 pair work.

7. **Day 4 - Pending.**  
   To be completed after the Day 4 pair work.

8. **Day 4 - Pending.**  
   To be completed after the Day 4 pair work.

9. **Day 5 - Pending.**  
   To be completed after the Day 5 pair work.

10. **Day 5 - Pending.**  
    To be completed after the Day 5 pair work.

## Most Surprising Insight

The most surprising insight so far is that "looks more reasoned" and "is more reliable" are different claims. A model can produce a longer chain of thought, a cleaner JSON record, or a more confident explanation without becoming more accurate. Reliability requires matching the intervention to the failure mode: constrained decoding for structure, evaluation for correctness, and causal intervention tests for reasoning faithfulness.

For my judge work, this changes how I think about training format. I should not assume that adding more intermediate reasoning steps will improve accuracy. First I need to test whether those steps are causal. If they are not, the better engineering move is to make intermediate decisions explicit, validate them separately, and force the final verdict to consume those checked fields.

## Canonical Reading List

- Wei et al. (2022), "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" - establishes why intermediate reasoning can improve performance on multi-step tasks, but does not by itself prove faithfulness.  
  https://arxiv.org/abs/2201.11903

- Turpin et al. (2023), "Language Models Don't Always Say What They Think" - important for understanding why generated explanations can be unfaithful or biased by the prompt while still sounding plausible.  
  https://arxiv.org/abs/2305.04388

- Nye et al. (2021), "Show Your Work: Scratchpads for Intermediate Computation" - useful for thinking about when intermediate computation can be made more operational rather than purely rhetorical.  
  https://arxiv.org/abs/2112.00114

- Schick et al. (2023), "Toolformer: Language Models Can Teach Themselves to Use Tools" - relevant adjacent pattern for making intermediate steps functional by connecting them to external actions or tools.  
  https://arxiv.org/abs/2302.04761

- OpenAI, "Introducing Structured Outputs in the API" - primary practical source for schema-constrained decoding and strict structured output behavior.  
  https://openai.com/index/introducing-structured-outputs-in-the-api/

- Geng et al. (2023), "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning" - research source for grammar-constrained decoding as a way to enforce structured generation.  
  https://aclanthology.org/2023.emnlp-main.674/

- Willard and Louf (2023), "Efficient Guided Generation for Large Language Models" - useful for understanding guided generation and token-level constraints through grammars/FSM-style mechanisms.  
  https://arxiv.org/abs/2307.09702

## Tool and Pattern List

- **Reasoning intervention tests:** corrupt or swap intermediate reasoning steps, ablate the chain, reorder subtasks, and check whether verdicts move in the expected direction.
- **Structured judge outputs:** require verdicts, rubric dimensions, confidence labels, evidence, and failure reasons as typed fields rather than free-form prose.
- **Schema-constrained decoding demo:** compare raw next-token probabilities with a schema-valid token mask, then renormalize the remaining valid probabilities.
- **Decoding sweeps:** vary temperature/top-p on the same prompts to detect whether style or verdict changes are inference-time effects.
