# Thread

Use each numbered section as one post in the reply chain.

## Post 1/6

Bad rejected examples can make preference tuning look better than it really is.

If every rejected SDR email is obvious generic junk, ORPO may only learn:

"do not write generic templates"

That is not the same as learning high-quality personalization.

## Post 2/6

ORPO learns from contrast.

For each prompt, it sees a chosen response and a rejected response.

The training signal pushes the model to assign higher odds to the chosen response than the rejected one.

So the difference between those two responses matters a lot.

## Post 3/6

If the rejected email says:

"Dear Sir/Madam, we help businesses grow..."

the model has an easy job.

It can avoid bad templates without learning whether the chosen email was grounded in the prospect's role, company, trigger, and pain point.

## Post 4/6

A near-miss rejection is more useful.

Example:

The email has the right tone, right prospect, and right offer, but invents a trigger event that was not in the prompt.

Now the model must learn:

personalization must be grounded, not just plausible.

## Post 5/6

For SDR outreach, near-miss rejects should target specific failures:

- wrong company or role
- unsupported trigger
- shallow personalization
- wrong pain point
- overconfident claim
- weak evidence calibration

Each pair should teach one boundary.

## Post 6/6

The eval should match the training goal.

Do not only test chosen vs terrible.

Hold out near-miss cases where style is good but grounding is flawed.

That is how you check whether ORPO learned real personalization, not just anti-template behavior.
