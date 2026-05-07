# Portfolio Update (Week 10-11 Improvements)

## Summary

These grounding commits turn the Week 10/11 artifacts from working demos into systems with clearer mechanisms, failure modes, and evaluation plans. The common improvement is that each artifact now names the boundary it must control: instruction fidelity, inference-time confidence, structured output reliability, reasoning faithfulness, and grounded personalization.

## Commit 1

- Artifact: `pair_DAY_1/grounding_commit.md`
- What changed and why it is better:
  - Added a mechanism-level explanation for instruction/rubric drift in long judge loops.
  - The Week 11 judge work is stronger because it no longer assumes early system-prompt tokens remain equally influential forever.

## Commit 2

- Artifact: `pair_DAY_2/grounding_commit.md`
- What changed and why it is better:
  - Added the prompt-vs-schema distinction for structured judge outputs.
  - The portfolio now separates structural reliability from semantic correctness.

## Commit 3

- Artifact: `pair_DAY_3/grounding_commit.md`
- What changed and why it is better:
  - Added grounded personalization as a measurable constraint for SDR outreach preference data.
  - The Week 10/11 SDR model work is better because rejected samples should now include near-misses, not only generic total failures.

## Commit 4

- Artifact: link or file path.
- What changed and why it is better.

## Commit 5

- Artifact: link or file path.
- What changed and why it is better.
