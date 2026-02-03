---
name: mythosmud-pre-commit-checklist
description: Run MythosMUD pre-commit checks before considering work done: format, mypy, lint (and optionally codacy-tools), then test or test-coverage. Use when finishing a change, before commit, or when the user asks if everything is done.
---

# MythosMUD Pre-Commit Checklist

## Definition of Done

Work is not done until these pass:

1. **Format** — `make format`
2. **Type check** — `make mypy`
3. **Lint** — `make lint` (and `make lint-sqlalchemy` if touching SQLAlchemy)
4. **Tests** — `make test` (fast) or `make test-coverage` (with coverage)
5. **Codacy** — After any file edit, run Codacy analysis per project rules (see [.cursor/rules/codacy.mdc](../../rules/codacy.mdc))

All commands are run from the **project root**.

## Full Pipeline (Optional)

For a full quality run including Codacy tools and OpenAPI spec:

```powershell
make all
```

This runs: format, mypy, lint, lint-sqlalchemy, codacy-tools, build, openapi-spec, test-coverage.

## Order

Run in this order: format first (so lint/mypy see formatted code), then mypy, then lint, then tests. Run Codacy analysis for each edited file as specified in the Codacy rule.

## Reference

- Definition of Done: [CLAUDE.md](../../CLAUDE.md) "Definition of Done"
- Codacy after edit: [.cursor/rules/codacy.mdc](../../rules/codacy.mdc)
- Makefile targets: [Makefile](../../Makefile) (help, format, mypy, lint, test, test-coverage, all)
