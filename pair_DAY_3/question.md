# Question

## My question (Birkity Yishak)

- Final question:

When you use a sequence-level preference optimization method like SimPO to train a judge that outputs a short structured verdict followed by a reason, the loss is computed equally across every token,  so the model cannot distinguish between "learn the correct classification boundary" and "learn to mimic the explanation format that follows the verdict." How do you design training pairs and held-out evaluation for a preference-tuned classifier to confirm it learned the verdict signal rather than the surface explanation pattern?:

- Connection to Week 10/11 artifact:

This connects to my Week 10/11 judge and evaluator work, where a model produces a compact structured verdict followed by a short reason. The concern is that preference tuning may optimize the whole output sequence without knowing which tokens are the real decision target and which tokens are just explanation surface form.

- Why this gap matters:

If the judge learns the explanation pattern instead of the verdict boundary, it may look aligned during training but fail on held-out cases where the same verdict must be produced with a different explanation style, reordered fields, missing rationale, or adversarially similar reasoning language. I need pair design and evaluation that separate verdict accuracy from explanation mimicry.

## My peer (Ramlla Akmel) question for me and my role as an explainer

- Final question:

While curating my  dataset for ORPO training, I noticed that many of the “Rejected” responses were extremely poor generic templates, while the “Chosen” responses were highly personalized SDR emails. This raised an important question: If the rejected examples are too low quality, does the model only learn to avoid obviously bad outputs rather than learn the subtle difference between “generic” and “high-quality personalization”? I want to understand whether “Near-Miss Rejections”  outputs that are almost correct but fail a specific personalization or grounding constraint  produce better post-training behavior than “Total-Failure Rejections” that are obviously poor.
[11:34 AM]So here is my question

How does the semantic difference between Chosen and Rejected responses influence learning during ORPO post-training, and do “Near-Miss” rejected samples improve personalization and calibration more effectively than highly generic rejected outputs in SDR outreach models?:

- Connection to Week 10/11 artifact:

This connects to Ramlla's Week 10/11 SDR outreach model and preference dataset, where chosen responses are intended to reward grounded personalization and rejected responses are intended to teach what bad outreach looks like.

- Why this gap matters:

If the rejected samples are only total failures, ORPO may teach the model to avoid generic templates without learning the finer boundary between grounded personalization and plausible but flawed personalization. Near-miss rejections make the preference signal more diagnostic because they isolate the exact constraint the chosen response satisfies.
