# Catalog Expansion Review — 2026-09-04

## Objective

Reduce publisher concentration and strengthen thin outcome categories without lowering the admission standard. The review began with more than 20 current external candidates and admitted ten.

## Method

Each admitted entry was checked against the eight criteria in the [editorial policy](../EDITORIAL-POLICY.md): consequential decision, evidence discipline, bounded workflow, decision-grade output, pressure testing, safety and limits, reproducibility, and maintenance and licensing.

“Reviewed” means the full skill instructions and bundled executable or required reference files were inspected. It does not mean the skill has received a published Petrichor Strategy Skill Index score. Scores require a pinned fixture, preserved output, and auditable evaluation record.

## Candidate pool

The discovery pass screened the following source sets before source-level review. Listing a candidate here is not an endorsement.

| Source | Candidates screened |
|---|---|
| [Headcount](https://github.com/cbrock84/headcount) | Market Entry; Mergers and Acquisitions; Portfolio Strategy; Scenario Planning; Strategic Alliances; Capital Allocation; Enterprise Risk; Operating Cadence; Organization Design; Portfolio Governance |
| [Google Meridian](https://github.com/google/meridian) | Meridian Budget Optimization; Meridian Scenario Planner |
| [Daloopa Investing](https://github.com/daloopa/investing) | Bull/Bear; Capital Allocation; Industry Analysis; Unit Economics |
| [Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills) | Ansoff Matrix; Business Health Diagnostic; Feature Investment Advisor; Product Strategy Session; TAM/SAM/SOM Calculator; Porter’s Five Forces |
| [PM Claude Skills](https://github.com/mohitagw15856/pm-claude-skills) | Capital Allocation |
| [Agent Skills](https://github.com/tech-leads-club/agent-skills) | Partner & Affiliate |
| [Wondel AI Skills](https://github.com/wondelai/skills) | Cold Start Problem; Lean Analytics |
| [ECC](https://github.com/affaan-m/ECC) | Competitive Platform Analysis; Strategic Compact; Recursive Decision Ledger |
| [Brand Building Skills](https://github.com/arnabbagxd/Brand-building-skills) | Brand Partnerships |
| [One Page Strategy](https://github.com/olgasafonova/one-page-strategy) and [Eterdis Strategy Skills](https://github.com/eterdis/strategy-skills) | One Page Strategy; Wardley Map |

The admitted sources were pinned during review: [Headcount `9cbf340`](https://github.com/cbrock84/headcount/commit/9cbf34005e3e8a980a6af9b55eb226bd926a62b3), [Google Meridian `322e400`](https://github.com/google/meridian/commit/322e400e156b996376c32074d8e47b7f37cd046a), [Daloopa Investing `f46f350`](https://github.com/daloopa/investing/commit/f46f350b526f6460d2172e33f7e9ed4b3f45045e), [ECC `e04ea0b`](https://github.com/affaan-m/ECC/commit/e04ea0b9cc8248686edf5ac751cadff550e162b8), [One Page Strategy `35146ae`](https://github.com/olgasafonova/one-page-strategy/commit/35146ae1f8f6ed9136413f40e49aebce1cb22384), and [Eterdis Strategy Skills `8bd22e9`](https://github.com/eterdis/strategy-skills/commit/8bd22e987163cc11a5ca631c132273a91a2e6390).

## Admitted skills

| Skill | Publisher | Category | Source commit | Why it passed | Material limitation |
|---|---|---|---|---|---|
| [Bull/Bear Scenario Analysis](https://github.com/daloopa/investing/tree/main/.claude/skills/bull-bear) | Daloopa | Executive decisions | `f46f350` | Requires cited fundamentals and filings, explicit scenarios, current price context, and traceable assumptions. | Requires a Daloopa account and data connection; it supports analysis, not trading authority. |
| [Market Entry](https://github.com/cbrock84/headcount/tree/main/plugins/corporate-strategy/skills/market-entry) | Chris Brock | GTM and growth | `9cbf340` | Tests market size, advantage transfer, entry modes, economics, a narrow initial test, and stopping criteria. | Quality depends on the operator supplying credible market and cost evidence. |
| [Meridian Budget Optimization](https://github.com/google/meridian/tree/main/skills/meridian_budget_optimization) | Google | Measurement and experimentation | `322e400` | Constrains optimization with fitted-model inputs, spend bounds, scenario comparison, generated code, and repeated human checkpoints. | Requires a fitted Meridian model; model misspecification remains a human responsibility. |
| [Mergers and Acquisitions](https://github.com/cbrock84/headcount/tree/main/plugins/corporate-strategy/skills/mergers-and-acquisitions) | Chris Brock | Executive decisions | `9cbf340` | Defines the thesis before target selection, sets walkaway conditions, treats diligence as falsification, and plans integration early. | It structures judgment but does not replace legal, tax, accounting, or specialist diligence. |
| [One Page Strategy](https://github.com/olgasafonova/one-page-strategy/tree/main/one-page-strategy) | Olga Safonova | Executive decisions | `35146ae` | Gates facts, root problem, guiding idea, and actions; checks falsifiability, trade-offs, conflicting objectives, and unsupported facts. | Its compact format is a decision narrative, not a substitute for supporting research or an execution plan. |
| [Operating Cadence](https://github.com/cbrock84/headcount/tree/main/plugins/operations/skills/operating-cadence) | Chris Brock | Execution systems | `9cbf340` | Gives each recurring forum a decision purpose, metric owner, escalation threshold, review interval, and deletion test. | Cadence design still needs adaptation to organization size and decision latency. |
| [Portfolio Strategy](https://github.com/cbrock84/headcount/tree/main/plugins/corporate-strategy/skills/portfolio-strategy) | Chris Brock | Product and portfolio | `9cbf340` | Uses the same attractiveness and right-to-win tests across units, forces ranking, and makes harvest and exit choices explicit. | The method depends on comparable evidence across unlike businesses and does not calculate valuation. |
| [Recursive Decision Ledger](https://github.com/affaan-m/ECC/tree/main/skills/recursive-decision-ledger) | Affaan Mustafa / ECC | Execution systems | `e04ea0b` | Preserves an append-only evidence trail across repeated trials and blocks live promotion without freshness, replay, risk, and approval gates. | It is a protocol for governing repeated analysis, not a domain-specific strategy model. |
| [Scenario Planning](https://github.com/cbrock84/headcount/tree/main/plugins/corporate-strategy/skills/scenario-planning) | Chris Brock | Executive decisions | `9cbf340` | Separates predetermined facts from load-bearing uncertainty and ends with no-regret moves, options, signals, owners, and triggers. | Scenario quality is sensitive to which uncertainties the team selects. |
| [Wardley Map](https://github.com/eterdis/strategy-skills/tree/main/wardley-map) | Eterdis AS | Product and portfolio | `8bd22e9` | Connects user needs, dependencies, evolution hypotheses, inertia, actions, confidence labels, and observable reassessment triggers. | Component placement is a judgment call and should be treated as a testable map, not objective market truth. |

## Not admitted in this round

| Candidate | Source | Decision |
|---|---|---|
| TAM/SAM/SOM Calculator | Product Manager Skills | Rejected: a worked example presents placeholder URLs and unsupported market figures in the shape of citations. |
| Feature Investment Advisor | Product Manager Skills | Rejected: worked examples calculate margin, profit, and ROI inconsistently. |
| Capital Allocation | PM Claude Skills | Rejected: its greedy score-per-cost helper can return a suboptimal portfolio for indivisible initiatives. |
| Partner & Affiliate | Agent Skills | Rejected: upstream licensing was not clear enough for reviewed status, and current platform claims were not adequately sourced. |
| Cold Start Problem and Lean Analytics | Wondel AI Skills | Deferred: derivative-source and attribution questions need more review before admission. |
| Competitive Platform Analysis | ECC | Deferred: useful workflow, but its instructions are narrowly tied to creative-service agencies despite a generic title. |
| Brand Partnerships | Brand Building Skills | Rejected: the workflow did not meet the catalog’s evidence and pressure-testing bar. |
| Other Headcount candidates | Headcount | Deferred: several passed an initial read, but this round capped additions from one suite to limit source concentration. |

## Coverage change

| Category | Before | After |
|---|---:|---:|
| Product and portfolio | 2 | 4 |
| Go-to-market and growth | 5 | 6 |
| Executive decisions | 10 | 14 |
| Measurement and experimentation | 4 | 5 |
| Execution systems | 1 | 3 |
| Total catalog | 52 | 62 |

The catalog now includes 13 publishers, up from seven. No candidate received an empirical index score in this round; the next step is a shared-fixture evaluation for comparable skills.
