# Evening Call Summary

- Status: Completed
- Participants: Birkity Yishak and Ramlla Akmel

## What landed

The evening call closed the Day 3 gap because Ramlla's ORPO question now has a clear mechanism and a practical dataset answer. The key idea is that ORPO learns from the contrast between chosen and rejected responses. If the rejected SDR emails are only obvious generic templates, the model can reduce the loss by learning a shallow anti-template rule. That helps basic quality, but it does not prove the model learned grounded personalization.

The near-miss framing landed well. A near-miss rejection keeps the email mostly strong but violates one important constraint, such as inventing a trigger event, using the wrong company, making an unsupported claim, or sounding too certain when the evidence is weak. That makes the contrast more diagnostic because the model must learn the specific personalization boundary rather than broad style differences.

## What needed tightening

The first draft needed a sharper distinction between "bad because generic" and "bad because subtly ungrounded." We also needed to make the held-out evaluation stronger. It is not enough to show that the tuned model beats terrible rejected emails. The real test is whether it can reject polished near-misses where the style is good but the grounding is wrong.

## Revisions made

I revised the explainer and blog draft to make the ORPO mechanism more direct, added a clearer SDR example with chosen, total-failure rejected, and near-miss rejected emails, and strengthened the evaluation design. The final version now recommends a dataset mix that includes some total failures for basic hygiene, many near-misses for the real personalization boundary, and held-out contrast sets organized by failure type.

The Day 3 signoff is now closed because the question is no longer just "are rejected samples too bad?" The resolved answer is: yes, rejected-sample difficulty changes what the model can learn, and near-miss rejections are the better tool for teaching grounded personalization and calibration.
