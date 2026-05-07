# Thread

Published thread: https://x.com/BYishak24169/status/2052377188109029511

Use each numbered section as one post in the reply chain.

## Post 1/6

Preference tuning can look successful for the wrong reason.

If every rejected SDR email is obvious generic junk, ORPO may learn:

"avoid bad templates"

That is useful, but it is not the same as learning grounded personalization.

## Post 2/6

ORPO learns from contrast.

It sees a prompt, a chosen response, and a rejected response.

If the chosen and rejected outputs are far apart, the model can rely on easy cues: company name vs no company, specific pain vs filler, real trigger vs no trigger.

## Post 3/6

A total-failure reject teaches the floor.

Example:

"Dear Sir/Madam, we help businesses grow..."

The model can reject that without understanding whether the chosen email was actually grounded in the prospect evidence.

## Post 4/6

A near-miss reject teaches the boundary.

It might have the right person, company, tone, and offer, but invent the trigger event.

Now the model has to learn:

specificity only counts when it is supported by the input.

## Post 5/6

Good near-misses fail one constraint at a time:

- wrong entity
- unsupported trigger
- shallow personalization
- misaligned offer
- overconfident claim
- weak evidence calibration

That makes the preference signal sharper.

## Post 6/6

The eval has to include near-misses too.

Do not only test chosen vs terrible.

Hold out polished-but-flawed emails and check whether the model rejects them.

That is how you tell whether ORPO learned personalization, not just anti-template behavior.
