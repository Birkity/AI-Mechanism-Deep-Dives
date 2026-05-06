# Prompt Constraints vs Schema-Constrained Decoding

Melkam's question was:

> How do prompt constraints and schema-defined output formats influence token-by-token generation in my Week 10/11 systems, and through what mechanism do they reduce invalid or unreliable outputs compared with prompt-only instructions?

The short answer is that prompts change what the model is likely to do, while schema constraints change what the decoder allows the model to do.

That distinction matters in Week 10/11 systems because many AI workflows depend on structured outputs: judge verdicts, rubric dimensions, tool arguments, extracted fields, confidence labels, and failure reasons. If the model emits malformed JSON, an invalid enum, or an extra paragraph before the object, the downstream system may break even if the natural-language answer "basically looks right." Prompting can reduce those failures, but it cannot eliminate them. Schema-constrained decoding can eliminate many format failures by intervening during generation itself.

## Prompt-Only Control Is Soft

An LLM generates text one token at a time. At each step, it assigns scores to possible next tokens, converts those scores into probabilities, then chooses a token according to the decoding strategy.

When we write a prompt like "Return only valid JSON with fields `verdict`, `reason`, and `confidence`," we are influencing those probabilities. The instruction makes JSON-like tokens more likely: `{`, field names, quotes, commas, enum values, and so on. But the model is still sampling from the full vocabulary unless another mechanism intervenes. Tokens that would break the format can still have nonzero probability.

That is why prompt-only structured output can fail in familiar ways:

- The model adds "Here is the JSON:" before the object.
- It omits a required field.
- It invents an extra field.
- It returns `"high confidence"` when the schema expects `"high"`.
- It produces JSON-looking text with a trailing comma or mismatched brace.

The prompt nudges behavior. It does not enforce the output language.

## Schema-Constrained Decoding Is Hard

Schema-constrained decoding adds a control layer at generation time. Instead of letting the model choose from every token in the vocabulary, the decoder checks which next tokens would keep the output valid under the schema or grammar.

OpenAI's Structured Outputs post describes this as dynamic constrained decoding: the valid token set changes after every generated token. At the beginning of a JSON object, `{` may be valid. After the model has generated `{"verdict"`, another `{` may no longer be valid. The decoder recomputes the allowed continuations from the current prefix and masks invalid tokens so their probability becomes zero.

So the mechanism is:

1. The model computes normal next-token probabilities.
2. The schema or grammar determines which tokens are legal after the current prefix.
3. Invalid tokens are masked out.
4. The remaining probabilities are renormalized.
5. The model samples only from valid continuations.

This is why schema constraints are stronger than prompt constraints. The prompt changes preferences; the schema changes the support of the probability distribution.

## A Tiny Token-Level Demo

Imagine a judge output must begin with this JSON:

```json
{"verdict":
```

The schema says the next value must be one of:

```json
"pass"
"fail"
"needs_review"
```

Now suppose the model's raw next-token probabilities look like this:

| Candidate next token | Raw probability | Schema-valid? |
| --- | ---: | --- |
| `"pass"` | 0.34 | yes |
| `"fail"` | 0.28 | yes |
| `"needs_review"` | 0.10 | yes |
| `"maybe"` | 0.12 | no |
| `null` | 0.08 | no |
| `I` | 0.08 | no |

In prompt-only generation, all six options remain possible. The prompt may make valid enum values more likely, but `"maybe"`, `null`, or `I` can still be sampled.

In schema-constrained decoding, invalid tokens are set to zero:

| Candidate next token | After schema mask |
| --- | ---: |
| `"pass"` | 0.34 |
| `"fail"` | 0.28 |
| `"needs_review"` | 0.10 |
| `"maybe"` | 0.00 |
| `null` | 0.00 |
| `I` | 0.00 |

Then the valid probabilities are renormalized across the remaining mass. The valid mass is `0.34 + 0.28 + 0.10 = 0.72`, so the effective probabilities become roughly:

| Candidate next token | Renormalized probability |
| --- | ---: |
| `"pass"` | 0.47 |
| `"fail"` | 0.39 |
| `"needs_review"` | 0.14 |

The model still makes a probabilistic choice among valid options, but it cannot choose an invalid one at that step. This is the core reason structured outputs reduce parser errors, invalid tool arguments, and broken judge records.

## What This Means for Week 10/11 Systems

For a Week 11 evaluator or LLM-as-a-judge, the output contract should be treated as an interface, not a writing preference. A judge schema might require:

```json
{
  "verdict": "pass | fail | needs_review",
  "rubric_dimension": "signal_direction | icp_fit | pitch_frame",
  "confidence": "low | medium | high",
  "evidence": "string",
  "failure_reason": "string"
}
```

With prompt-only control, the model might usually follow this shape. With constrained decoding, the system can force the shape so downstream code receives parseable fields every time the generation finishes normally and does not refuse.

That makes the system more reliable in a production sense. You can validate outputs, route failures, aggregate verdicts, and compare rubric dimensions without writing fragile cleanup logic around every completion. The model becomes easier to integrate because the output boundary is typed.

## The Important Limitation

Schema constraints guarantee form, not truth.

They can force the model to choose one of `"pass"`, `"fail"`, or `"needs_review"`, but they cannot guarantee the chosen verdict is correct. They can force an `evidence` field to exist, but they cannot prove the evidence actually supports the verdict. They can separate `reasoning_steps` from `final_answer`, but they cannot prove the reasoning caused the final answer rather than rationalized it after the fact.

This matters for your judge work. Structured outputs are the right tool for reliability at the interface boundary: valid fields, parseable outputs, stable enums, fewer retries. They are not a substitute for evaluation. You still need test cases, adversarial examples, calibration checks, and semantic audits to know whether the judge is accurate on ambiguous cases.

The clean design principle is:

> Use schemas to make the output structurally reliable. Use evals to make the judgment behavior reliable.

## Sources

- OpenAI, "Introducing Structured Outputs in the API"  
  https://openai.com/index/introducing-structured-outputs-in-the-api/
- Saibo Geng, Martin Josifoski, Maxime Peyrard, and Robert West, "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning"  
  https://aclanthology.org/2023.emnlp-main.674/
- Brandon T. Willard and Remi Louf, "Efficient Guided Generation for Large Language Models"  
  https://arxiv.org/abs/2307.09702
- OpenAI Cookbook, "Introduction to Structured Outputs"  
  https://cookbook.openai.com/examples/structured_outputs_intro
