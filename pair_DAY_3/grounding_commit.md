# Grounding Commit

- Artifact pointer:
  - Day 3 explainer: [explainer.md](explainer.md)
  - Day 3 blog: https://sprout-krill-3c0.notion.site/Near-Miss-Rejections-The-Missing-Ingredient-in-ORPO-Training-for-Grounded-SDR-Outreach-359fb8a6541b8051ad07f6db2041784d?source=copy_link
  - Day 3 thread: https://x.com/BYishak24169/status/2052377188109029511

- What changed and why:

Day 3 grounds the ORPO dataset-curation question back into the Week 10/11 SDR outreach work. The update is conceptual rather than code-based: I now treat "grounded personalization" as a measurable constraint, not just a writing style.

The practical change is that rejected samples should not be only generic total failures. The SDR preference dataset should include near-miss rejected responses that sound polished but fail one specific grounding constraint, such as wrong trigger, unsupported company event, shallow role connection, misaligned offer, or overconfident claim. This makes the preference signal more diagnostic because the chosen/rejected pair differs along the boundary I actually want the model to learn.

The evaluation update is to hold out polished near-misses, counterfactual grounding edits, and failure-type slices. That lets me test whether the model learned grounded personalization rather than just anti-template behavior.
