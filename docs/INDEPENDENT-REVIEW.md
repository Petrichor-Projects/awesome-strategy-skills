# Independent Review Protocol

The first positioning pilot is intentionally provisional. This protocol makes third-party review concrete without manufacturing endorsement.

## Reviewer brief

Reviewers receive:

1. the [fixture input](../evaluation/fixtures/positioning-decay-v1/input.md);
2. the three preserved [outputs](../evaluation/runs/2026-08-22-positioning-pilot/outputs/);
3. the [Strategy Skill Index](../evaluation/RUBRIC.md); and
4. a blank copy of the [evaluation template](../evaluation/template.md).

Reviewers must not see the existing `SCORES.md` or `REPORT.md` until they submit their initial scores.

## Eligibility and disclosure

- Strategy, product marketing, product, GTM, research, or agent-evaluation experience is useful.
- Authors, contributors, customers, competitors, and friends may review if the relationship is disclosed.
- At least one accepted reviewer should have no financial or authorship relationship with Petrichor or any compared project.
- Reviewers retain attribution rights and may publish a dissenting note.

## Submission

Open a pull request containing one record per skill under:

```text
evaluation/independent-reviews/<reviewer-handle>/2026-08-22-positioning-pilot/
```

Each record must cite output evidence for all eight dimensions, identify any critical failure, and include a conflict statement.

## Resolution

Maintainers compare evidence, not reviewer authority. Score disagreements are shown before and after discussion; they are never silently averaged. The report moves from **provisional** to **independently reviewed** only when at least one eligible reviewer completes all three records and all material disagreements are published.

## Invitation

**Subject:** Independent review request: open AI strategy-skill benchmark

Petrichor Projects published a three-skill positioning pilot with a public fixture, pinned sources, full outputs, and a disclosed author conflict. We are looking for an independent reviewer to score the preserved outputs before seeing our scores.

The review uses eight 0–3 dimensions and should take approximately 60–90 minutes. Your scores, reasoning, relationship disclosure, and any dissent would be published under your name or handle. There is no requirement to agree with Petrichor's result.

Protocol: https://github.com/Petrichor-Projects/awesome-strategy-skills/blob/3669e6fa6171357c5c6e729f3439c7e700bf9b82/docs/INDEPENDENT-REVIEW.md
