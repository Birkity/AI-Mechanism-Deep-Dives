# Morning Call Summary

- Date: Day 3
- Participants: Birkity Yishak and Ramlla Akmel
- What was ambiguous and how it was sharpened:

The morning call went well because both questions became more concrete. My question was sharpened from a broad concern about SimPO and judge training into a specific evaluation-design problem: how do I prove that a preference-tuned classifier learned the verdict boundary rather than the surface pattern of a verdict followed by a reason?

Ramlla's question was sharpened from a general concern about rejected response quality into a contrast-design problem for ORPO: if rejected SDR emails are too obviously bad, the model may only learn to avoid generic templates. The more useful question is whether near-miss rejections, which are almost good but fail one personalization or grounding constraint, give the model a stronger signal about what high-quality personalization actually requires.

We agreed that both gaps are really about preference data geometry. The chosen and rejected outputs should differ along the dimension we want the model to learn. If they differ along too many easy surface dimensions, the model can win the training objective by learning shortcuts.
