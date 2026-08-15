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

After editing Python, run `uv run basedpyright <edited files>` from the repo root. Fix
findings before considering the change done.

Ponytail: `Any` is not a one-liner. Protocol + TypedDict (dict value types matching the
real class) is the shortest correct diff. Mutable dicts are invariant:
`dict[str, WebSocket | None]` is not assignable to `dict[str, WebSocket]`.
