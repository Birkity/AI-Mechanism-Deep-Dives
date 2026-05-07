# Sources

## Canonical Sources

1. Jiwoo Hong, Noah Lee, and James Thorne. "ORPO: Monolithic Preference Optimization without Reference Model"  
   https://arxiv.org/abs/2403.07691  
   Core source for the ORPO mechanism: chosen-response SFT plus an odds-ratio term that contrasts favored and disfavored generations.

2. Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn. "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"  
   https://arxiv.org/abs/2305.18290  
   Background source for direct preference optimization and why chosen/rejected pair construction affects what the model learns.

3. Yu Meng, Mengzhou Xia, and Danqi Chen. "SimPO: Simple Preference Optimization with a Reference-Free Reward"  
   https://papers.nips.cc/paper_files/paper/2024/hash/e099c1c9699814af0be873a175361713-Abstract-Conference.html  
   Relevant to Birkity's Day 3 question because SimPO uses average sequence log probability as its implicit reward, raising the issue of verdict tokens versus explanation tokens.

4. Matt Gardner et al. "Evaluating Models' Local Decision Boundaries via Contrast Sets"  
   https://aclanthology.org/2020.findings-emnlp.117/  
   Supports the held-out evaluation pattern: perturb examples in small meaningful ways to test whether the model learned the intended boundary.

5. Suchin Gururangan, Swabha Swayamdipta, Omer Levy, Roy Schwartz, Samuel Bowman, and Noah A. Smith. "Annotation Artifacts in Natural Language Inference Data"  
   https://aclanthology.org/N18-2017/  
   Supports the shortcut-learning risk: models can exploit surface artifacts when dataset construction makes labels predictable from shallow cues.

6. Haocheng Lu, Minjun Zhu, and Henry Yu. "Hard Negative Sample-Augmented DPO Post-Training for Small Language Models"  
   https://arxiv.org/abs/2512.19728  
   Recent preprint connecting hard negatives and preference optimization; useful as supporting evidence for near-miss rejected samples.

## Tool or Pattern Used

- Near-miss rejection design: create rejected SDR emails that are almost correct but fail one target constraint, such as unsupported trigger, wrong entity, shallow personalization, misaligned offer, or overconfident claim.
- Contrast-set held-out evaluation: keep the email style mostly constant while changing one grounding fact, then test whether the model preference follows the fact rather than the surface pattern.
- Grounded personalization checklist: verify entity grounding, evidence grounding, relevance grounding, and calibration before treating a personalized SDR response as high quality.
