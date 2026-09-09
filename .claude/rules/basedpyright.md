---
description: Ban basedpyright reportAny and reportExplicitAny; no typing.Any shortcut
paths:
  - "**/*.py"
---

# basedpyright: no `Any`

Canonical rule: `.cursor/rules/basedpyright-no-any.mdc` (also in `AGENTS.md`).

Do not write Python that triggers **`reportAny`** or **`reportExplicitAny`**. Do not use
`typing.Any`, `from typing import Any`, `dict[str, Any]`, `list[Any]`, `*args: Any`,
`manager: Any`, or `# type: ignore` / `# pyright: ignore` to hide those rules.

**Enforced since #784.** After editing Python, run `uv run basedpyright` (full run, no file
arguments) from the repo root. It exits non-zero on any finding not already in
`.basedpyright/baseline.json`. The same check runs in pre-commit, in CI, and via `make typecheck`.

Also forbidden: deleting an annotation to dodge the rule. An unannotated parameter fires
`reportMissingParameterType` / `reportUnknownParameterType` instead, and those are gated too —
`Unknown` is just the implicit form of `Any`.

**Never run `basedpyright --writebaseline` to silence a new finding.** The baseline may only
shrink. `make any-report` shows what remains.

If a suppression is genuinely correct, it must name its rule and carry
`# Reason: <CATEGORY> - <cause>` plus `# Appropriate because: <why Any is right, ≥40 chars>`.
`scripts/lint_pyright_suppressions.py` enforces this. Full rules, categories, and the
replacement table: see **No `Any` in `server/` (enforced)** in `AGENTS.md`.

Ponytail: `Any` is not a one-liner. Protocol + TypedDict (dict value types matching the
real class) is the shortest correct diff. Mutable dicts are invariant:
`dict[str, WebSocket | None]` is not assignable to `dict[str, WebSocket]`.
