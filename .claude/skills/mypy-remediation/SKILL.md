---
name: mypy-remediation
description: Systematically fix mypy type-checking errors, most-critical first. Use when `make mypy` fails or the user asks to fix type errors.
disable-model-invocation: true
---

# Mypy Remediation

Fixes mypy type-checking errors. This is a manual-trigger workflow (`disable-model-invocation:
true`) since remediation touches multiple files — invoke it explicitly rather than letting it
auto-fire mid-conversation.

## Entry point

Run `make mypy` from the project root — not `mypy .` directly, since `make mypy` applies this
repo's actual configuration. If it passes, stop; nothing to do.

## Priority

Fix in this order. Each tier encodes real judgment about blast radius — don't skip ahead.

| Tier | Category | Example codes |
|---|---|---|
| 🔴 Critical | Import/name errors, missing annotations on public APIs | `import`, `name-defined`, `attr-defined` |
| 🟡 High | Type incompatibilities, `Optional`/`None` handling, missing internal annotations | `return-value`, `arg-type`, `union-attr`, `var-annotated`, `assignment` |
| 🟢 Medium | Unused `type: ignore`, redundant casts, missing returns, missing stubs | `no-untyped-def`, `redundant-cast`, `unused-ignore` |
| 🔵 Low | Implicit `Any`, overly broad types, test-file annotations | `no-any-return` |

## Fix-verify loop

For each issue: locate it (`search_symbols`/`search_text` via jCodemunch, or grep), understand
the root cause, fix with the Edit tool, then re-run `make mypy` (or `uv run mypy path/to/file.py`
for a faster targeted check) before moving to the next tier.

## Never

- Blanket `# type: ignore` without a specific error code and a reason
- Suppressing an error by widening a type to `Any` when a real type is knowable
- Declaring victory before `make mypy` actually exits 0

See [reference.md](reference.md) for fix patterns per error code, the full error-code table, and
debugging commands for when a fix doesn't take.
