# Week 12 Synthesis

## Overview

Week 12 is turning my Week 10/11 systems from "things I shipped" into systems I can explain and defend. The pattern so far is clear: many reliability problems in LLM systems are not solved by better wording alone. They require knowing where the model is making a probabilistic generation choice, where the application needs a hard interface contract, and where an explanation may be persuasive without being causally faithful.

So far, Day 1 through Day 3 closed six concrete gaps: three I named and three I researched for peers. The biggest shift in my thinking is that evaluator and alignment reliability have separate layers: the generated form must be controlled, the judgment behavior must be tested, and the training contrast must actually expose the boundary I want the model to learn. A structured output can make a judge easier to parse, but it cannot prove the judge is correct. A reasoning chain can make a verdict easier to read, but it cannot prove the reasoning caused the verdict. A preference pair can make a model prefer one output over another, but it cannot guarantee the model learned the intended semantic distinction if the rejected sample is too easy.

## Gaps Closed

1. **Day 1 - My gap: instruction/rubric drift in long judge loops.**  
   I started with a concern that an LLM-as-a-judge might stop following early rubric instructions across long sessions even when those instructions remain in the context. The gap was about mechanism: how attention over long prefixes, recency effects, and attention sinks can reduce the practical influence of early anchor tokens. The explainer I received helped me understand why simply making the context window longer does not guarantee instruction fidelity. The portfolio implication is that long evaluator loops need re-anchoring, segmented state, structured rubric representation, or constrained outputs rather than assuming the original system prompt remains equally influential forever.

2. **Day 1 - Peer gap I explained: cautious vs overconfident language at inference time.**  
   I explained how prompt uncertainty and decoding settings affect whether a model emits cautious downgrade language or confident commitment language. The key mechanism is the next-token probability distribution: weak evidence produces a flatter distribution where multiple semantic clusters compete, and temperature/top-p decide how much the model exploits the top cluster versus samples from alternatives. This connected directly to the Week 11 Sales Agent Evaluation Bench and the `bench_overcommitment`/signal-direction rubric. The main takeaway was that confidence style can be an inference-time effect, not only a training-time property.

3. **Day 2 - My gap: whether reasoning steps cause judge verdicts or rationalize them.**  
   Melkam's explainer closed my gap about reasoning-chain faithfulness in judge formats. I now understand that autoregressive dependence is not the same as faithful reasoning: a verdict can be conditioned on earlier generated text without those steps reflecting the true decision process. The right way to test causality is intervention: corrupt, remove, reorder, or replace intermediate steps and measure whether the final verdict changes in the expected direction. If the verdict stays stable while the reasoning changes, the chain is likely acting as post-hoc rationalization. This means reordering or expanding a judge's reasoning format will only improve ambiguous-case accuracy if the steps are actually load-bearing and reused by the decision process, not merely more fluent.

4. **Day 2 - Peer gap I explained: prompt constraints vs schema-constrained decoding.**  
   I explained Melkam Beyene's question about why schema-defined outputs reduce invalid or unreliable outputs compared with prompt-only instructions. The core mechanism is token-level: prompts softly shift next-token probabilities, while schema-constrained decoding masks invalid continuations to zero probability and samples only from schema-valid tokens. This changes the output boundary from a writing preference into an interface contract. The important limitation is that schemas guarantee structure, not truth: they can force valid fields, enums, and JSON shape, but they do not prove the verdict or reasoning is correct.

5. **Day 3 - My gap: verdict signal vs explanation-pattern mimicry in SimPO-style judge training.**  
   My Day 3 question focused on a preference-tuned classifier or judge that outputs a short verdict followed by a reason. The gap was that sequence-level preference optimization can score the whole completion, so the model may learn the explanation format around the verdict instead of the classification boundary itself. The mechanism lesson is that training pairs and held-out evals need to separate verdict correctness from rationale surface form. That means using verdict-only metrics, explanation-style perturbations, counterfactual label-boundary cases, swapped or shortened rationales, and held-out formats where the correct verdict must survive changes in the reason text.

6. **Day 3 - Peer gap I explained: near-miss rejections for grounded SDR personalization in ORPO.**  
   I explained Ramlla Akmel's ORPO dataset question: if chosen SDR emails are highly personalized but rejected emails are only terrible generic templates, the model may learn anti-template behavior instead of grounded personalization. The key mechanism is that ORPO learns from the chosen/rejected contrast it is given. Total-failure rejects teach the floor, while near-miss rejects teach the boundary. A polished rejected email that invents a trigger event is more diagnostic than "Dear Sir/Madam" because it forces the model to learn that specificity only counts when it is supported by the prompt evidence. The portfolio implication is to curate near-miss rejected samples and held-out contrast sets for wrong entity, unsupported trigger, shallow personalization, misaligned offer, overclaiming, and weak-evidence calibration.

7. **Day 4 - Pending.**  
   To be completed after the Day 4 pair work.

8. **Day 4 - Pending.**  
   To be completed after the Day 4 pair work.

9. **Day 5 - Pending.**  
   To be completed after the Day 5 pair work.

10. **Day 5 - Pending.**  
    To be completed after the Day 5 pair work.

## Most Surprising Insight

The most surprising insight so far is that "looks more reasoned," "looks more structured," and "looks more personalized" are all weaker claims than reliability. A model can produce a longer chain of thought, a cleaner JSON record, or a more specific SDR email without becoming more accurate or more grounded. Reliability requires matching the intervention to the failure mode: constrained decoding for structure, evaluation for correctness, causal intervention tests for reasoning faithfulness, and near-miss preference pairs for semantic boundaries.

For my judge work, this changes how I think about training format. I should not assume that adding more intermediate reasoning steps will improve accuracy. First I need to test whether those steps are causal. If they are not, the better engineering move is to make intermediate decisions explicit, validate them separately, and force the final verdict to consume those checked fields.

For my preference-data work, this changes how I think about rejected examples. I should not assume that any bad response is a useful negative. The rejected response has to fail along the dimension I want the model to learn. If I care about grounded personalization, I need rejected examples that sound plausible but are ungrounded, plus held-out evaluations that test the same boundary.

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

- Hong et al. (2024), "ORPO: Monolithic Preference Optimization without Reference Model" - central source for understanding chosen/rejected preference optimization without a separate reference model.  
  https://arxiv.org/abs/2403.07691

- Rafailov et al. (2023), "Direct Preference Optimization: Your Language Model is Secretly a Reward Model" - background source for direct preference optimization and why pair construction matters.  
  https://arxiv.org/abs/2305.18290

- Meng, Xia, and Chen (2024), "SimPO: Simple Preference Optimization with a Reference-Free Reward" - relevant to sequence-level judge training because its average log-probability reward raises verdict-token versus explanation-token concerns.  
  https://papers.nips.cc/paper_files/paper/2024/hash/e099c1c9699814af0be873a175361713-Abstract-Conference.html

- Gardner et al. (2020), "Evaluating Models' Local Decision Boundaries via Contrast Sets" - useful for designing held-out tests where one meaningful fact changes while surface form stays similar.  
  https://aclanthology.org/2020.findings-emnlp.117/

## Tool and Pattern List

- **Reasoning intervention tests:** corrupt or swap intermediate reasoning steps, ablate the chain, reorder subtasks, and check whether verdicts move in the expected direction.
- **Structured judge outputs:** require verdicts, rubric dimensions, confidence labels, evidence, and failure reasons as typed fields rather than free-form prose.
- **Schema-constrained decoding demo:** compare raw next-token probabilities with a schema-valid token mask, then renormalize the remaining valid probabilities.
- **Decoding sweeps:** vary temperature/top-p on the same prompts to detect whether style or verdict changes are inference-time effects.
- **Near-miss rejection design:** make rejected preference samples almost correct but wrong on one grounding constraint, so the model learns the intended boundary instead of an easy artifact.
- **Contrast-set held-out eval:** hold style constant while changing one fact, trigger, or label boundary to test whether the model follows the semantic signal.
- **Verdict/rationale disentanglement eval:** perturb explanation format while holding labels fixed to test whether a preference-tuned judge learned the verdict signal rather than rationale surface style.
