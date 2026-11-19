# Learning to Fix a Wrong Answer

**Author:** Siddharth Rao  
**Assignment:** Individual research short story  
**Primary paper:** [Training Language Models to Self-Correct via Reinforcement Learning](https://arxiv.org/abs/2409.12917), Kumar et al., 2024, version 2.  
**Topic approval:** The student confirmed that the instructor approved this paper. It is a 2024 research paper, not a recent survey. Two related surveys provide the broader taxonomy.

SCoRe trains a language model to revise its answers through two-stage, multi-turn reinforcement learning. This review explains the approach and asks how to measure both repaired mistakes and damage to initially correct answers. It connects the paper to survey taxonomies, Self-Refine, Reflexion, Pair-SFT, and STaR-style repair.

## Deliverables

| Artifact | File or destination |
| --- | --- |
| Illustrated article, 7 pages | [Article PDF](article/score-article.pdf) |
| Article for the Medium editor | [HTML](article/medium-ready.html) and [plain text](article/medium-ready.txt) |
| Editable presentation, 18 slides | [PowerPoint](slides/score-presentation.pptx) |
| Presentation PDF | [Slides PDF](slides/score-presentation.pdf) |
| Narrated video, exactly 15:00 | [MP4 video](video/score-presentation-15min.mp4) |
| Narration and captions | [Transcript](video/narration.txt), [SRT captions](video/captions.srt), [slide timings](video/timings.json) |
| Original diagrams and charts | [Visual assets](assets/) |
| Published benchmark tables | [CSV data and sources](data/) |
| Arithmetic verification | [Python script](src/verify_results.py) and [execution output](data/verification-results.json) |

The video includes the presentation slides and a **synthetic male voice**. It is AI-generated narration, not a recording of the student's voice or face. It includes an explicit narration disclosure. The duration is 15 minutes to satisfy both the rubric's 10-15 minute range and its separate minimum of 15 minutes.

## Publication and submission status

| Requirement | Status |
| --- | --- |
| Public GitHub repository | [Published and anonymously accessible](https://github.com/qwertydgdhegncf/score-self-correction-short-story) |
| Published Medium article | [Learning to Fix a Wrong Answer](https://medium.com/@siddharthrao522/learning-to-fix-a-wrong-answer-5e54c218e4d1) |
| Published SlideShare presentation | Blocked: [SlideShare upload page](https://www.slideshare.net/upload) states “Uploads are temporarily unavailable” and disables uploads. PPTX and PDF are available above. |
| YouTube video | [Published video](https://youtu.be/wp7iQxl6VjI) |
| GitHub URL added to course spreadsheet | Awaiting spreadsheet link |
| GitHub URL submitted to course assignment | Awaiting submission-page link |

GitHub, Medium, and YouTube publication are verified. SlideShare is blocked by its disabled upload service as observed on November 18, 2026. The spreadsheet and course submission remain pending their destination links. The local MP4 is exactly 900 seconds; YouTube displays its processed copy as 15:01.

## What the article and presentation cover

- Taxonomy: correction timing, source of feedback, and what adapts between attempts.
- Important techniques: Self-Refine, Reflexion, Pair-SFT, STaR-style repair, and SCoRe.
- Architecture: two attempts by one policy, with a training-only verifier and a separate inference information boundary.
- Training: constrained initialization and progress reward shaping.
- Metrics: first- and second-attempt accuracy, net gain, recovery share, damage share, and conditional transition rates.
- Comparisons: MATH500 and HumanEval tables from the paper, with model, split, and decoding details.
- Ablations: removal of multi-turn training, Stage I, and reward shaping, plus a STaR replacement.
- Original analysis: matched-compute comparisons, uncertainty, task transfer, verification limits, and an LLMOps release evaluation plan.

## Evidence and scope

All benchmark values come from **SCoRe version 2, Tables 2-4**. They are reported results, not new experiments run for this assignment. The comparison is a within-paper benchmark table, not a claim of current global leaderboard leadership.

The math experiment uses Gemini 1.5 Flash and evaluates on MATH500 after incorporating 4,500 original MATH test problems into training. The code experiment uses Gemini 1.0 Pro, trains on MBPP, and evaluates on HumanEval. Main benchmark comparisons use greedy decoding. These details matter when comparing against another paper.

The worked examples and diagrams are original explanatory material. The LLMOps workflow is a proposal, not a claimed production deployment. No new model training, proprietary model replication, or cloud deployment is claimed.

The supplied assignment text also contains a separate **group final-project** rubric. This package addresses the approved **individual short-story** assignment. Group-member presentations, training pipelines, cloud inference demos, and a group project report are separate deliverables for that other assignment.

## Verify the calculations

Python 3, standard library only:

```bash
python3 src/verify_results.py
```

The script checks all 14 transcribed result rows, allowing 0.11 percentage points for subtraction of rounded published values. It also derives the SCoRe MATH500 counts: 29 repairs, 7 damaged answers, and 22 additional correct answers. Conditional repair is 14.5%; conditional damage is approximately 2.3%. Neither conditional rate uses all 500 problems as its denominator.

## References

1. [Kumar et al. (2024), SCoRe](https://arxiv.org/html/2409.12917v2).
2. [Kamoi et al. (2024), When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://aclanthology.org/2024.tacl-1.78/).
3. [Pan et al. (2023), Automatically Correcting Large Language Models: Surveying the landscape of diverse self-correction strategies](https://arxiv.org/abs/2308.03188v2).
4. [Madaan et al. (2023), Self-Refine](https://arxiv.org/abs/2303.17651v2).
5. [Shinn et al. (2023), Reflexion](https://arxiv.org/abs/2303.11366v4).

## Attribution and AI assistance

The article was newly drafted for this assignment, rather than copied from an existing Medium article. AI assisted drafting, visualization, and slide creation. Microsoft online text-to-speech generated the male narration. Research contributions and benchmark results belong to their cited authors. The student should review the content and follow the course's AI-assistance disclosure rules.
