# Signoff

- Status: closed
- What I understand now that I did not before:

Ramlla and I closed the Day 3 gap. I now understand that ORPO does not magically learn "good personalization" from any chosen/rejected pair. It learns from the contrast it is given. If the rejected responses are mostly total failures, the model can learn an easy shortcut: avoid generic templates, filler greetings, and empty claims. That is useful, but it is not the same as learning the subtle boundary between grounded personalization and plausible but unsupported personalization.

Near-miss rejections make the training signal sharper because they keep most of the response good while breaking one important constraint. A rejected SDR email that has the right tone and structure but invents the trigger event teaches a different lesson than a rejected email that says "Dear Sir/Madam." The near-miss teaches that personalization must be grounded in the provided evidence, not just sound specific.

The held-out evaluation also needs to match the claim. To prove the model learned the personalization boundary, I should not only test chosen emails against terrible generic rejects. I should test against polished near-misses, counterfactual grounding changes, failure-type slices, and calibration cases where the model should stay cautious when the evidence is weak.
