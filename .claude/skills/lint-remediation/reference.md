# Lint Remediation — Reference

## Fix patterns by tier

### 🔴 Critical — compilation errors

```python
# Missing import
from .component import Component
```
```typescript
// Missing import
import { Component } from './Component';

// Missing interface for a prop that doesn't exist
interface Props {
  title: string;
}
```

### 🟡 High — code quality

```python
# F401 unused import — remove it
# I001 import sorting — stdlib, then third-party, then local, each group blank-line separated
import os
import sys

from third_party import lib

from my_module import ClassA

# E501 line too long — break into a parenthesized multi-line string
very_long_variable_name = (
    "this is a very long string that exceeds the 120 character limit "
    "and needs to be broken down"
)
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

# UP upgrade suggestion
list(dict.keys())  # not dict.keys() where a list is actually needed
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
cat client/eslint.config.js
```
