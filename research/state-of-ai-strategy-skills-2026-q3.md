# State of AI Strategy Skills

## Q3 2026

**Published:** 2026-09-06
**Dataset:** 62 catalog records, 54 individual skills, nine scored outputs
**Status:** Maintainer research. Evaluation scores are provisional pending independent review.

## Executive finding

AI strategy skills are better at producing structured artifacts than governing consequential decisions.

The catalog contains 54 individual skills from 13 publishers. Nine have now been run against the same positioning-decay fixture. The median score was 18 of 24. The strongest workflows did three things the rest left to the operator: they named a commitment, preserved the evidence boundary, and stated what would reverse the decision.

Research and context skills often handled truth better than decision skills. They labeled source limits, missing data, and confidence. They scored lower on decision specificity because they correctly stopped before the executive commitment.

That boundary matters. A research artifact can be excellent and still be the wrong final interface for a board, founder, or product leader.

## What is in the catalog

| Measure | Q3 2026 |
|---|---:|
| Structured records | 62 |
| Individual skills | 54 |
| Collections | 8 |
| Outcome categories | 9 |
| Publishers | 13 |
| Empirically evaluated skills | 9 |
| Independent completed reviews | 0 |

The catalog is an editorial sample, not a census of every public skill repository. Inclusion requires a consequential decision, a bounded workflow, usable output, visible source, and a usable license.

## Supply clusters around executive and positioning work

| Skill category | Count | Share of individual skills |
|---|---:|---:|
| Executive decisions and operating systems | 14 | 25.9% |
| Positioning and competitive strategy | 11 | 20.4% |
| Customer and market intelligence | 9 | 16.7% |
| Go-to-market and growth | 6 | 11.1% |
| Measurement and experimentation | 5 | 9.3% |
| Product and portfolio strategy | 4 | 7.4% |
| Pricing and monetization | 3 | 5.6% |
| Execution systems | 2 | 3.7% |

The top three categories contain 34 of 54 skills, or 63.0% of the individual catalog. Pricing and execution remain thin. That is an editorial observation about this catalog, not proof that the wider market has the same distribution.

## Publisher concentration is the first catalog risk

Four publishers account for 49 of 62 records: Petrichor Projects (20), Corey Haines (11), Alireza Rezvani (9), and Udi Menkes (9). The concentration reflects where maintained, licensed, strategy-specific skills were easiest to verify during the first catalog cycle.

It creates two risks:

1. A small number of design philosophies can look like a field-wide norm.
2. Petrichor’s 20 records can make the catalog appear self-serving even when every conflict is disclosed.

The Q4 editorial target is not more volume. It is broader authorship: at least five accepted skills from publishers not already represented, without weakening the admission standard.

## Licensing is visible, but not fully resolved

| License | Records |
|---|---:|
| MIT | 38 |
| CC BY 4.0 | 20 |
| Apache 2.0 | 2 |
| See source | 2 |

Sixty of 62 records carry a specific license label. Two discovery records require the reader to inspect the source. A link directory can tolerate that ambiguity. An installation workflow should not. Future compatibility or install tooling must refuse to present a one-click path until the exact license and version are resolved.

## Nine skills on one fixture

The first benchmark asked every skill to handle the same fictional company. HelioDesk’s 2023 “AI copilot” position no longer matched buyer language, commercial performance, competitive movement, or its own product controls.

| Skill | Native artifact | Score |
|---|---|---:|
| Relevancy Audit | Positioning-decay diagnosis | 23 |
| One Page Strategy | Compact company strategy | 22 |
| Competitor Profiling | Comparative evidence record | 19 |
| Scenario Planning | Futures, options, and triggers | 19 |
| Customer Research | Customer-evidence synthesis | 18 |
| Competitive Intelligence | Recurring positioning update | 17 |
| Product Marketing Context | Shared downstream context | 16 |
| Positioning Craft | Positioning canvas | 15 |
| Strategy Frameworks | Where-to-play/how-to-win plan | 13 |

The mean and median were both 18. The ten-point spread came less from prose quality than from workflow design.

### Decision gates produced the highest task fit

Relevancy Audit and One Page Strategy forced a commitment, an exclusion, and a reversal condition. One was a detailed diagnostic. The other was a compressed strategy narrative. Both made it hard to hide behind a collection of reasonable observations.

### Research skills produced the clearest evidence boundaries

Competitor Profiling required dated raw sources, comparable fields, explicit inference, and untrusted-input handling. Customer Research required verbatim language, sample-bias checks, confidence levels, and a refusal to build personas from too little evidence.

Neither native artifact is the executive decision. That is why a lower task-fit score should not be read as lower craft.

### Generic frameworks transferred more burden to the operator

Strategy Frameworks asked the right high-level questions: where to play, how to win, what capabilities matter, and what the company will not do. It did not require provenance, counterevidence, approval, or kill criteria. A skilled operator can add those controls. The skill does not guarantee them.

## The missing layer is operational safety

No critical failure appeared in the fixture. No skill invented market facts or took an external action.

Safety still scored unevenly. Human approval was common. Complete handling of untrusted inputs, sensitive data, permissions, claims review, and external actions was rare. Competitor Profiling was the only external workflow in the benchmark that explicitly treated fetched pages as untrusted instructions.

Strategy skills are moving toward better epistemics faster than they are moving toward complete operating controls.

## A more useful architecture

The benchmark supports a sequence of distinct jobs:

1. Collect and qualify customer evidence.
2. Build comparable competitor evidence.
3. Diagnose whether the current position survives.
4. Test the decision against unresolved futures.
5. Compress the commitment into a repeatable strategy.
6. Express the approved market frame.
7. Distribute the source of truth to downstream teams.
8. Monitor the market and reopen the decision when a trigger fires.

No single evaluated skill handled all eight jobs at full depth. Teams should design the handoffs instead of asking one prompt to impersonate a research system, decision process, and operating cadence at once.

## Adoption baseline

As of 2026-09-06, the repository had 0 stars, 1 fork, 0 watchers, 1 unique view in GitHub’s retained traffic window, and 29 unique cloners. One retained referral came from LinkedIn.

The clone count is contaminated by setup and automation. It is not independent adoption. There are no completed outside reviews, verified badge placements, accepted outside contributors, or qualified inquiries attributable to the catalog yet.

That is the correct baseline for a new public asset.

## Q4 tests

The next report should answer five questions:

1. Can two blind reviewers reproduce the dimension evidence within a predeclared tolerance?
2. Does a second fixture in pricing or portfolio strategy change the ordering?
3. Can the catalog add five new publishers without lowering the admission bar?
4. Do listed authors adopt the badge or link back after individual accuracy-first outreach?
5. Does the companion hub produce qualified movement into a diagnostic or inquiry, not only repository traffic?

## Method and conflicts

Catalog counts come from [`data/catalog.json`](../data/catalog.json). Benchmark scores come from the public [nine-skill evaluation](../evaluation/runs/2026-09-06-positioning-benchmark/REPORT.md). The machine-readable summary is [`research/data/2026-q3-summary.json`](data/2026-q3-summary.json).

Petrichor created 19 individual skills in the catalog, authored the highest-scoring benchmark skill, selected the fixture, wrote the rubric, generated the outputs, and scored them. Those conflicts make independent review a release criterion for any claim stronger than “maintainer evaluation.”

This report describes one curated catalog and one task fixture. It does not estimate the size of the full skill ecosystem, rank models, or prove business outcomes.
