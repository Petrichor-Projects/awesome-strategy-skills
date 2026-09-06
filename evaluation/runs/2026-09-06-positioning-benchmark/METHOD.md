# Positioning Strategy Benchmark — Method

## Purpose

This benchmark asks how nine published strategy skills handle the same positioning-decay decision. It tests task fit, evidence behavior, decision quality, and usable output. It is not a universal ranking of authors or repositories.

## Fixture

- **Fixture:** [`positioning-decay-v1`](../../fixtures/positioning-decay-v1/README.md)
- **Task:** Decide whether HelioDesk should preserve, refresh, or replace its current positioning and make the next 90 days explicit.
- **Input:** [`input.md`](../../fixtures/positioning-decay-v1/input.md)
- **Held out during generation:** [`evaluator-reference.md`](../../fixtures/positioning-decay-v1/evaluator-reference.md)

## Compared skills and pinned sources

| Skill | Publisher | Commit | Native job | Output |
|---|---|---|---|---|
| Relevancy Audit | Petrichor Projects | `0ab4479e6e688b2df588dc488f8a25d0d029111c` | Diagnose positioning decay | [Output](../2026-08-22-positioning-pilot/outputs/relevancy-audit.md) |
| Positioning Craft | Udi Menkes | `53530efba26431c05ac3fd1dcc5452bdb2fc120e` | Build a positioning canvas | [Output](../2026-08-22-positioning-pilot/outputs/positioning-craft.md) |
| Product Marketing Context | Corey Haines | `3df87f97621e18fbed7f6aa684edba54f49779a7` | Build shared marketing context | [Output](../2026-08-22-positioning-pilot/outputs/product-marketing-context.md) |
| One Page Strategy | Olga Safonova | `35146ae1f8f6ed9136413f40e49aebce1cb22384` | Create a Facts–Problem–Idea–Solution strategy | [Output](outputs/one-page-strategy.md) |
| Competitor Profiling | Corey Haines | `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` | Produce source-traceable competitor profiles | [Output](outputs/competitor-profiling.md) |
| Scenario Planning | Chris Brock | `9cbf34005e3e8a980a6af9b55eb226bd926a62b3` | Build moves that survive uncertain futures | [Output](outputs/scenario-planning.md) |
| Customer Research | Corey Haines | `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` | Synthesize customer evidence | [Output](outputs/customer-research.md) |
| Competitive Intelligence | Alireza Rezvani | `19392f7a08264ed00486a251f5b2098321771f94` | Turn competitor evidence into cross-functional action | [Output](outputs/competitive-intelligence.md) |
| Strategy Frameworks | Udi Menkes | `53530efba26431c05ac3fd1dcc5452bdb2fc120e` | Define where to play and how to win | [Output](outputs/strategy-frameworks.md) |

## Execution protocol

1. The evaluator read the complete pinned instruction file for each skill and any directly required template used for the output.
2. Every skill received the same fixture and task. No outside company, customer, or market facts were allowed.
3. Follow-up questions were disabled. The evidence pack was treated as the complete answer set so interactive skills could be compared in a fixed run.
4. Each skill produced its native artifact. Research skills produced research artifacts. Diagnostic and planning skills produced decisions or plans.
5. Missing inputs stayed missing. No live scraping, interviews, pricing research, or certification claims were simulated.
6. The held-out evaluator reference was opened only after outputs were complete.
7. The original three outputs from the August pilot remain byte-preserved and are incorporated by reference. Six additional outputs were generated on 2026-09-06.

## Scoring protocol

- **Rubric:** Eight dimensions from the [Petrichor Strategy Skill Index](../../RUBRIC.md), each scored 0–3.
- **Unit of analysis:** Source workflow plus observable output behavior on this fixture.
- **Critical failures:** Fabricated evidence, hidden external action, unqualified safety or compliance claims, or no usable artifact.
- **Task-fit rule:** A high-quality research skill can score below a diagnostic when it does not make the requested decision. That is a scope finding, not a quality verdict.
- **Evidence:** [`SCORES.md`](SCORES.md) records dimension-level reasons and links to every output.

## Bias and limits

- One Codex evaluator acting for Petrichor generated and scored the corpus.
- Petrichor authored Relevancy Audit and maintains this catalog. That conflict is material.
- The skill order was not blinded or randomized.
- Three outputs were generated in the August pilot and six in the September expansion. The fixture and evaluation rubric were unchanged.
- The skills promise different artifact types. A research synthesis, context file, positioning canvas, and decision audit should not be treated as interchangeable.
- No alternate model, repeat sampling, or inter-rater reliability estimate is included.

All scores are **provisional**. The benchmark becomes independently reviewed only after an eligible outside reviewer submits blind dimension evidence under the [review protocol](../../../docs/INDEPENDENT-REVIEW.md).
