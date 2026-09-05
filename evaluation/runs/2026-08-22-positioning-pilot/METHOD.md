# Positioning Strategy Pilot — Method

## Purpose

This pilot tests whether three different strategy-skill designs can turn the same evidence pack into a defensible positioning decision.

It is a methods demonstration, not a definitive leaderboard.

## Fixture

- **Fixture:** [`positioning-decay-v1`](../../fixtures/positioning-decay-v1/README.md)
- **Task:** Decide whether HelioDesk should preserve, refresh, or replace its current positioning and identify the next 90 days of work.
- **Input available to each skill:** [`input.md`](../../fixtures/positioning-decay-v1/input.md)
- **Held out during generation:** [`evaluator-reference.md`](../../fixtures/positioning-decay-v1/evaluator-reference.md)

## Skills and pinned sources

| Label | Skill | Publisher | Commit | Source |
|---|---|---|---|---|
| A | Relevancy Audit | Petrichor Projects | `0ab4479e6e688b2df588dc488f8a25d0d029111c` | [Source](https://github.com/Petrichor-Projects/resilience-stack/tree/0ab4479e6e688b2df588dc488f8a25d0d029111c/skills/positioning/relevancy-audit) |
| B | Positioning Craft | Udi Menkes | `53530efba26431c05ac3fd1dcc5452bdb2fc120e` | [Source](https://github.com/menkesu/awesome-pm-skills/tree/53530efba26431c05ac3fd1dcc5452bdb2fc120e/positioning-craft) |
| C | Product Marketing Context | Corey Haines | `3df87f97621e18fbed7f6aa684edba54f49779a7` | [Source](https://github.com/coreyhaines31/marketingskills/tree/3df87f97621e18fbed7f6aa684edba54f49779a7/skills/product-marketing) |

## Generation protocol

1. The evaluator read the complete pinned instruction files and directly referenced templates, rubrics, and evaluations.
2. Each skill received the same fixture and task.
3. The evidence pack was treated as complete for the pilot; follow-up questions were not permitted.
4. Each output followed the native artifact shape of its skill rather than a forced common template.
5. No facts outside the fixture were permitted.
6. The evaluator reference remained out of the generation prompt and was used only during scoring.

## Evaluation protocol

- **Method:** Direct scoring against the eight-dimension [Petrichor Strategy Skill Index](../../RUBRIC.md).
- **Scale:** 0–3 per dimension, maximum 24.
- **Critical-failure check:** Fabricated evidence, unqualified safety or compliance claims, no actual decision, or no human ownership.
- **Evidence:** Scores cite both source behavior and generated output behavior.
- **Task fit:** The score applies to this positioning-decay task, not every use of the skill.

## Bias and limitations

- A single evaluator generated and scored all three outputs in one Codex session.
- The evaluator is acting for Petrichor Projects, which created Skill A and maintains this catalog.
- There was no blinded order, independent human panel, alternate model, or inter-rater calibration.
- Output length differs because the skills promise different artifact types.
- Skill C is primarily a context-building skill, not a diagnostic; the pilot intentionally measures that scope mismatch.
- Skill A was evaluated on a task closely aligned with its native purpose, which is a legitimate task-fit advantage but also a home-field advantage.

For those reasons, all scores are labeled **provisional**. The report emphasizes fit, failure modes, and evidence—not a universal winner.

