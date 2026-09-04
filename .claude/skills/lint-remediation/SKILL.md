---
name: lint-remediation
description: Systematically fix Python/Ruff and React/ESLint lint errors, most-critical first. Use when `make lint` fails or the user asks to fix lint errors.
disable-model-invocation: true
---

# Lint Remediation

Fixes Python (Ruff) and React (ESLint) lint errors. Manual-trigger workflow
(`disable-model-invocation: true`) since remediation touches multiple files.

## Entry point

Run `make lint` from the project root. If it passes, stop; nothing to do.

- Python detail: `uv run ruff check --line-length=120 .`
- React detail: `cd client && npx eslint --fix .`

## Priority

| Tier | Category | Example |
|---|---|---|
| 🔴 Critical | Compilation/syntax errors, import resolution failures | Python `SyntaxError`, TS build failures |
| 🟡 High | Unused imports/variables, import sorting, line length, missing hook deps | `F401`, `I001`, `E501`, `react-hooks/exhaustive-deps` |
| 🟢 Medium | Unused loop variables, deprecated patterns | `B007`, `UP` |
| 🔵 Low | Minor style, non-blocking documentation warnings | — |

## Fix-verify loop

For each issue: locate it, fix with the Edit tool, then re-run `make lint` before moving to the
next tier.

## Never

- Silence a lint error by disabling the rule just to make the run pass
- Leave line-length violations broken across multiple statements in a way that changes behavior

See [reference.md](reference.md) for fix patterns and the error-code table.
