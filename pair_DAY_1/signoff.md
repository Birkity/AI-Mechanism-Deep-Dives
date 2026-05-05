Signoff

- Status: closed
- What I understand now that I did not before:
	I can now explain (and defend) why “overconfident commitment” vs “cautious downgrade” language can flip even with the same model and prompt when evidence is weak.
	The key mechanism is inference-time: under uncertainty the next-token distribution is flatter (competing token clusters are close), and decoding choices like temperature and top-p determine whether the system exploits the slightly-most-likely commitment tokens or explores alternatives where downgrade tokens can surface.
	Once early tokens land in one mode (commitment vs discovery), the rest of the completion becomes path-dependent because future token probabilities are conditioned on the generated text.
	For evaluator/judge loops, this means consistency requires controlling decoding (or structuring the decision) before trusting scores based on the generated phrasing.