# Mypy Remediation — Reference

## Fix patterns by tier

### 🔴 Critical — import and name errors

```python
# error: Name "Optional" is not defined
from typing import Optional  # add the missing import

# error: Cannot find implementation or library stub for module named "mymodule"
# mypy: ignore-errors   # only if the module genuinely has no stubs and none can be installed

# error: Module has no attribute "missing_func"
from mymodule import existing_func  # verify the actual interface
```

### 🟡 High — type errors

```python
# Incompatible return value type
def get_name() -> str:
    return "123"  # not 123

# Incompatible argument type
def process(value: int) -> None: ...
process(123)  # not process("hello")

# Optional/None handling — add a type guard
def process(value: str | None) -> str:
    if value is None:
        return ""
    return value.strip()

# Missing type annotations
def calculate(x: int, y: int) -> int:
    return x + y

# Type narrowing — isinstance check before use
value: str | int = get_value()
if isinstance(value, str):
    process_string(value)
```

### 🟢 Medium — type refinement

```python
# Remove unused "type: ignore"
result = calculate(1, 2)  # not: calculate(1, 2)  # type: ignore

# Remove redundant cast
name: str = "hello"
result = name  # not: cast(str, name)

# Add missing return / make return type Optional
def get_value() -> int:
    if condition:
        return 42
    return 0  # or raise

# Install stubs for third-party libraries
# uv pip install types-requests
```

### 🔵 Low — type precision

```python
# Replace implicit Any with a specific type
def process(data: dict[str, str]) -> str | None:
    return data.get("key")

# Use Literal for a limited option set
from typing import Literal
def set_mode(mode: Literal["debug", "release", "test"]) -> None: ...

# Annotate tests too
def test_feature() -> None:
    result: int = calculate(1, 2)
    assert result == 3
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

For third-party libraries without stubs, prefer installing community stubs
(`uv pip install types-<lib>`) over `ignore_missing_imports` for the whole module — the latter
silences real errors too.
