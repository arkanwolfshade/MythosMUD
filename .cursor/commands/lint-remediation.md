---
description: Rules for fixing linting errors found
alwaysApply: false
---
# Lint Remediation

Fixes Python (Ruff) and React (ESLint) lint errors, most-critical first.

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

For each issue: locate it, fix it, then re-run `make lint` before moving to the next tier.

## Never

- Silence a lint error by disabling the rule just to make the run pass
- Leave line-length violations broken across multiple statements in a way that changes behavior

## Fix patterns by tier

### 🔴 Critical — compilation errors

```python
# Missing import
from .component import Component
```
```typescript
// Missing import
import { Component } from './Component';
```

### 🟡 High — code quality

```python
# F401 unused import — remove it
# I001 import sorting — stdlib, then third-party, then local, each group blank-line separated
import os
import sys

from third_party import lib

from my_module import ClassA
```
```typescript
// @typescript-eslint/no-unused-vars — remove, or prefix with underscore if intentionally unused
const _unusedVariable = 'value';

// react-hooks/exhaustive-deps — include every dependency actually used inside the effect
useEffect(() => {
  fetchData(userId);
}, [userId]);
```

### 🟢 Medium — style

```python
# B007 unused loop variable — prefix with underscore
for _player_id, websocket in items():
    ...
```

## Error code table

| Code | Category | Tier | Fix |
|---|---|---|---|
| `F401` | Import | 🟡 | Remove unused import |
| `I001` | Import | 🟡 | Reorder imports |
| `E501` | Style | 🟡 | Break into multiple lines |
| `B007` | Style | 🟢 | Prefix unused loop var with `_` |
| `UP` | Upgrade | 🟢 | Apply the suggested modern syntax |
| `react-hooks/exhaustive-deps` | Hook | 🟡 | Add every used value to the deps array |
| `@typescript-eslint/no-unused-vars` | Variable | 🟡 | Remove or prefix with `_` |
| `max-len` | Style | 🟡 | Break into multiple lines |
| `prefer-const` | Style | 🟢 | Change `let` to `const` |

## Debugging when a fix doesn't take

```bash
ls scripts/lint.py                                  # confirm the script exists
uv run ruff --version                                # confirm Ruff is installed
cat pyproject.toml | grep -A 20 "\[tool.ruff\]"       # confirm expected config
uv run ruff check --line-length=120 . --verbose
cd client && npx eslint . --debug
```
