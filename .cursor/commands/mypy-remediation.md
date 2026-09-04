---
description: Rules for fixing mypy type checking errors
alwaysApply: false
---
# Mypy Remediation

Fixes mypy type-checking errors, most-critical first.

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

For each issue: locate it (grep/semantic search), understand the root cause, fix it, then
re-run `make mypy` (or `uv run mypy path/to/file.py` for a faster targeted check) before moving
to the next tier.

## Never

- Blanket `# type: ignore` without a specific error code and a reason
- Suppressing an error by widening a type to `Any` when a real type is knowable
- Declaring victory before `make mypy` actually exits 0

## Fix patterns by tier

### 🔴 Critical — import and name errors

```python
# error: Name "Optional" is not defined
from typing import Optional  # add the missing import

# error: Module has no attribute "missing_func"
from mymodule import existing_func  # verify the actual interface
```

### 🟡 High — type errors

```python
# Optional/None handling — add a type guard
def process(value: str | None) -> str:
    if value is None:
        return ""
    return value.strip()

# Type narrowing — isinstance check before use
value: str | int = get_value()
if isinstance(value, str):
    process_string(value)
```

### 🟢 Medium — type refinement

```python
# Remove unused "type: ignore"
result = calculate(1, 2)  # not: calculate(1, 2)  # type: ignore

# Add missing return / make return type Optional
def get_value() -> int:
    if condition:
        return 42
    return 0  # or raise
```

### 🔵 Low — type precision

```python
# Replace implicit Any with a specific type
def process(data: dict[str, str]) -> str | None:
    return data.get("key")
```

## Error code table

| Code | Category | Tier | Fix |
|---|---|---|---|
| `import` | Import | 🔴 | Add import or install stubs |
| `name-defined` | Name | 🔴 | Import or define the name |
| `attr-defined` | Attribute | 🔴 | Fix attribute or add `type: ignore[attr-defined]` |
| `return-value` | Return | 🟡 | Fix return value or type |
| `arg-type` | Argument | 🟡 | Fix argument or parameter type |
| `union-attr` | Optional | 🟡 | Add a type guard |
| `var-annotated` | Annotation | 🟡 | Add a type annotation |
| `assignment` | Assignment | 🟡 | Fix types on both sides |
| `no-untyped-def` | Definition | 🟢 | Add a full type signature |
| `redundant-cast` | Cast | 🟢 | Remove the cast |
| `unused-ignore` | Ignore | 🟢 | Remove the comment |
| `no-any-return` | Any | 🔵 | Make the return type specific |

## Debugging when a fix doesn't take

```bash
uv run mypy --version                              # confirm mypy is actually installed
cat pyproject.toml | grep -A 20 "\[tool.mypy\]"     # confirm expected config is present
uv run mypy . --show-error-codes --pretty           # verbose, with codes
uv run mypy --help-error-code <error-code>          # explain a specific code
uv run mypy path/to/file.py --show-traceback        # isolate to one file
```
