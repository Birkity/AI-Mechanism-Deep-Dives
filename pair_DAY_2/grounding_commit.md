# Grounding Commit

- Artifact pointer: Week 11 judge/evaluator training format and the Week 12 synthesis entry in `synthesis.md`.
  - Day 2 blog: [Prompting Is Not Enforcement](https://sprout-krill-3c0.notion.site/Prompting-Is-Not-Enforcement-How-Schema-Constrained-Decoding-Makes-LLM-Outputs-Reliable-358fb8a6541b8029bf93e4438c21c5b5?source=copy_link)
  - Day 2 thread: [x.com](https://x.com/i/status/2052077945141743904)
- What changed and why:

Day 2 did not require a large code change because the main value was conceptual: it changed how I should interpret and defend reasoning chains in my judge format. The concrete grounding update is that `synthesis.md` now records the Day 2 lesson: intermediate reasoning steps should not be treated as reliable evidence of the model's decision process unless they pass intervention tests. This improves the portfolio narrative around the Week 11 judge by clarifying that reordering or expanding reasoning steps is not automatically an accuracy improvement. The next implementation edit, if applied to the Week 11 judge, should add an evaluation slice that corrupts, removes, or swaps intermediate rubric steps and checks whether verdicts change appropriately on ambiguous cases.
