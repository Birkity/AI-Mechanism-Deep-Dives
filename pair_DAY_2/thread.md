# Thread

1/6

Prompting is soft control.

Schema-constrained decoding is hard control.

That difference is why "please output valid JSON" is not the same thing as giving the model a real output schema.

2/6

LLMs generate one token at a time.

At each step, the model assigns probabilities to possible next tokens.

A prompt can make JSON-like tokens more likely, but invalid tokens can still remain in the distribution.

3/6

That is why prompt-only JSON fails:

- extra commentary
- missing fields
- wrong enum values
- trailing commas
- broken tool arguments

The model was nudged toward structure, not forced into it.

4/6

Schema decoding changes the token set itself.

After each partial output, the decoder asks:

"Which next tokens still keep this valid under the schema?"

Everything else gets masked to probability zero.

5/6

So the model still chooses probabilistically, but only among valid continuations.

For judge/tool outputs, that means fewer parser failures and cleaner fields like:

- verdict
- rubric dimension
- confidence
- evidence
- failure reason

6/6

But structure is not correctness.

A schema can force `"verdict": "pass"` or `"fail"`.

It cannot prove the verdict is right.

Use schemas for reliable form.
Use evals for reliable judgment.
