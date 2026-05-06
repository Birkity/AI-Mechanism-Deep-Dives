# Signoff

- Status: closed
- What I understand now that I did not before:

Melkam and I both agreed that the Day 2 gaps were closed. I now understand that a reasoning chain before a judge verdict is not automatically evidence that the reasoning caused the verdict. Autoregressive generation means the final verdict is conditioned on earlier tokens, but that does not prove the intermediate reasoning steps are faithful to the model's actual decision process. To test whether the steps are causal, I need intervention tests: corrupt, remove, reorder, or replace intermediate claims such as signal direction, ICP fit, and pitch frame, then measure whether the final verdict changes in the expected direction. If the verdict remains stable while the reasoning changes, the chain is likely post-hoc; if it moves with the edited intermediate step, that step is more likely to be load-bearing.

From my explanation to Melkam, we also agreed that prompt-only structure and schema-constrained decoding are different mechanisms. Prompting nudges token probabilities, while schema constraints mask invalid continuations during decoding. That closes the structured-output gap: schemas improve structural reliability, but they do not by themselves prove semantic correctness.
