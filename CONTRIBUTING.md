# Contributing

Thank you for helping make AI-assisted strategy more rigorous.

## Before nominating a skill

Confirm that the candidate:

- Supports a consequential strategic decision or diagnosis.
- Has a clear, reusable workflow rather than a loose prompt collection.
- States its required inputs and does not fabricate missing evidence.
- Produces a concrete, reviewable output.
- Has a visible license and active source repository.
- Meets the scope and standards in [EDITORIAL-POLICY.md](EDITORIAL-POLICY.md).
- Is something you have read closely enough to explain why it belongs.

Stars, social reach, repository size, and author reputation are not admission criteria.

## Nomination route

Use the [skill nomination issue form](https://github.com/Petrichor-Projects/awesome-strategy-skills/issues/new?template=nominate-skill.yml). This is best when you want maintainers to review and add the entry.

Include:

1. A permanent source URL.
2. The exact skill or collection name.
3. The decision it improves.
4. Evidence of its workflow and outputs.
5. License and compatibility information.
6. Your relationship to the project.
7. Known limitations or risks.

## Pull request route

Use a pull request when you are prepared to update both the human and machine-readable catalog.

1. Add one entry to the correct alphabetical section in `README.md`.
2. Add the corresponding object to `data/catalog.json`.
3. Use a neutral, outcome-focused description ending in a period.
4. Set `last_reviewed` to the date you actually inspected the source.
5. Use `reviewed` only after reading the full skill and bundled executable files.
6. Run the checks:

   ```bash
   python3 scripts/validate_catalog.py
   npx --yes awesome-lint
   ```

7. Complete the pull request template, including the conflict-of-interest disclosure.

Keep unrelated entries out of the same pull request.

## Catalog fields

Required fields are enforced by `scripts/validate_catalog.py`:

- `id` — Stable lowercase slug.
- `name` — Display name.
- `url` — Canonical source URL.
- `publisher` — Author or organization.
- `kind` — `skill` or `collection`.
- `category` — One approved outcome category.
- `status` — `petrichor-original`, `reviewed`, or `collection`.
- `license` — SPDX-style identifier or `Unknown`.
- `last_reviewed` — ISO date.
- `description` — Neutral sentence describing decision utility.
- `why_included` — Editorial reasoning beyond the project description.
- `conflict` — `none` or a plain-language disclosure.

## Removal

Removal is maintenance, not punishment. An entry may be removed when it becomes stale, unsafe, unlicensed, unreachable, deceptive, strategically generic, or materially weaker than alternatives.

## Conduct

Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Critique workflows and evidence. Do not attack contributors or authors.

