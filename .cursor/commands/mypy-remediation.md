---
description: Rules for fixing mypy type checking errors
alwaysApply: false
---
# Mypy Type Checking Remediation Prompt - AI-Optimized Version

> "In the arcane libraries of code quality, we discover that proper type checking requires systematic error categorization, methodical remediation patterns, and thorough validation protocols. The path to type-safe code lies not in hasty fixes, but in structured mypy remediation and comprehensive verification."

## 🎯 MANDATORY AI EXECUTION PROTOCOL

**CRITICAL**: You MUST follow this exact sequence. Do not skip steps or deviate from the order.

### Phase 1: Initial Assessment (REQUIRED FIRST)

```bash
# Step 1: Run mypy to get current type checking state
make mypy
```

**AI ACTION**: Capture the complete mypy output. If mypy passes, STOP - no remediation needed.

**AI RULE**: If mypy fails, continue to Phase 2. If mypy passes, document success and exit.

### Phase 2: Categorize and Prioritize Mypy Issues

**AI DECISION TREE**: For each mypy issue, categorize into ONE of these priority levels:

#### 🔴 CRITICAL (Fix First - Blocking Issues)

- **Import errors** - Module not found, cannot import name
- **Name errors** - Name not defined, attribute does not exist
- **Type errors in function signatures** - Incompatible return types, parameter types
- **Missing type annotations** in critical functions (public APIs)

#### 🟡 HIGH PRIORITY (Fix Second - Core Functionality)

- **Type incompatibility errors** - Assigning wrong types to variables
- **Missing type annotations** in internal functions
- **Optional/None handling errors** - Item "None" has no attribute
- **Type narrowing issues** - Need to add type guards or assertions

#### 🟢 MEDIUM PRIORITY (Fix Third - Enhancement)

- **Unused type: ignore comments** - No longer needed
- **Redundant casts** - Type is already correct
- **Missing return statements** - Function with return type doesn't return
- **Incomplete type stubs** - Third-party libraries without stubs

#### 🔵 LOW PRIORITY (Fix Last - Polish)

- **Implicit Any types** - Could be more specific
- **Overly broad types** - Could use Union or Literal
- **Missing type annotations** in test files
- **Documentation type hints** - Docstring types don't match annotations

### Phase 3: Systematic Fixing Process

**AI RULE**: Fix ONE category at a time. Do not move to the next category until current one is resolved.

#### For Each Issue Category

1. **IDENTIFY**: Use specific tools to locate the exact issues
2. **ANALYZE**: Understand root cause before attempting fix
3. **FIX**: Apply targeted solution using search_replace tool
4. **VERIFY**: Run mypy again to confirm fix works
5. **VALIDATE**: Ensure no regressions introduced

### Phase 4: Tool Selection Guide

**AI TOOL MAPPING**: Use these specific tools for each issue type:

#### Mypy Type Checking

```bash
# REQUIRED: Check all mypy issues
uv run mypy .

# OPTIONAL: Check specific file or directory
uv run mypy path/to/file.py
uv run mypy path/to/directory/

# OPTIONAL: Check with verbose output
uv run mypy . --show-error-codes --pretty

# OPTIONAL: Show traceback for errors
uv run mypy . --show-traceback
```

**AI ACTION**: Use `grep` to find specific error codes, `read_file` to examine files, `search_replace` to fix issues.

#### Understanding Mypy Error Codes

```bash
# Get explanation of specific error code
uv run mypy --help-error-code <error-code>

# Example: Understand assignment error
uv run mypy --help-error-code assignment

# Example: Understand union-attr error
uv run mypy --help-error-code union-attr
```

**AI ACTION**: Use mypy's built-in documentation to understand error codes before attempting fixes.

### Phase 5: Fix Implementation Patterns

#### 🔴 CRITICAL FIXES - Import and Name Errors

```python
# Pattern 1: Fix missing imports
# BEFORE: error: Name "Optional" is not defined
# AFTER: Add missing import
from typing import Optional

# Pattern 2: Fix import errors
# BEFORE: error: Cannot find implementation or library stub for module named "mymodule"
# AFTER: Ensure module exists or add to mypy exclusions
# mypy: ignore-errors

# Pattern 3: Fix attribute errors
# BEFORE: error: Module has no attribute "missing_func"
# AFTER: Verify module interface or add type: ignore comment
from mymodule import existing_func
```

#### 🟡 HIGH PRIORITY FIXES - Type Errors

```python
# Pattern 1: Fix function return type mismatch
# BEFORE: error: Incompatible return value type (got "int", expected "str")
def get_name() -> str:
    return 123

# AFTER: Fix return type or implementation
def get_name() -> str:
    return "123"

# Pattern 2: Fix parameter type mismatch
# BEFORE: error: Argument 1 has incompatible type "str"; expected "int"
def process(value: int) -> None:
    print(value)
process("hello")

# AFTER: Fix argument or parameter type
def process(value: int) -> None:
    print(value)
process(123)

# Pattern 3: Fix Optional/None handling
# BEFORE: error: Item "None" has no attribute "strip"
def process(value: str | None) -> str:
    return value.strip()

# AFTER: Add type guard or assertion
def process(value: str | None) -> str:
    if value is None:
        return ""
    return value.strip()

# Pattern 4: Add missing type annotations
# BEFORE: error: Function is missing a return type annotation
def calculate(x, y):
    return x + y

# AFTER: Add complete type annotations
def calculate(x: int, y: int) -> int:
    return x + y

# Pattern 5: Fix type narrowing
# BEFORE: error: Argument 1 has incompatible type "str | int"; expected "str"
def process_string(s: str) -> None:
    print(s.upper())

value: str | int = get_value()
process_string(value)

# AFTER: Add type guard
value: str | int = get_value()
if isinstance(value, str):
    process_string(value)
```

#### 🟢 MEDIUM PRIORITY FIXES - Type Refinement

```python
# Pattern 1: Remove unused type: ignore
# BEFORE:
result = calculate(1, 2)  # type: ignore  # unused "type: ignore" comment
# AFTER:
result = calculate(1, 2)

# Pattern 2: Fix redundant cast
# BEFORE: error: Redundant cast to "str"
from typing import cast
name: str = "hello"
result = cast(str, name)  # Already str

# AFTER: Remove unnecessary cast
name: str = "hello"
result = name

# Pattern 3: Fix missing return
# BEFORE: error: Missing return statement
def get_value() -> int:
    if condition:
        return 42

# AFTER: Add return or make return type Optional
def get_value() -> int:
    if condition:
        return 42
    return 0  # or raise exception

# Pattern 4: Add type stubs for third-party
# BEFORE: error: Library stubs not installed for "requests"
import requests

# AFTER: Install type stubs
# Run: uv pip install types-requests
import requests
```

#### 🔵 LOW PRIORITY FIXES - Type Precision

```python
# Pattern 1: Replace implicit Any with specific types
# BEFORE: note: Implicit return value of "Any"
def process(data):
    return data.get("key")

# AFTER: Add explicit types
from typing import Any
def process(data: dict[str, Any]) -> Any:
    return data.get("key")

# Better: Use specific types
def process(data: dict[str, str]) -> str | None:
    return data.get("key")

# Pattern 2: Use Union/Literal for precision
# BEFORE:
def set_mode(mode: str) -> None:
    pass

# AFTER: Use Literal for limited options
from typing import Literal
def set_mode(mode: Literal["debug", "release", "test"]) -> None:
    pass

# Pattern 3: Add type annotations in tests
# BEFORE:
def test_feature():
    result = calculate(1, 2)
    assert result == 3

# AFTER:
def test_feature() -> None:
    result: int = calculate(1, 2)
    assert result == 3
```

### Phase 6: Verification Protocol

**AI MANDATORY CHECKS**: After each fix, run these commands in order:

```bash
# 1. Verify type checking passes
uv run mypy .

# 2. Check specific file if only one was changed
uv run mypy path/to/changed_file.py

# 3. Verify with error codes shown
uv run mypy . --show-error-codes

# 4. Check for new errors introduced
uv run mypy . --pretty
```

**AI RULE**: If ANY check fails, STOP and fix the issue before proceeding.

### Phase 7: Success Validation

**AI SUCCESS CRITERIA**: All of these must pass:

- [ ] `uv run mypy .` exits with code 0
- [ ] No type errors remaining
- [ ] No new type errors introduced
- [ ] All critical and high-priority issues resolved
- [ ] Code still passes tests (`make test`)

## 🚨 AI ERROR HANDLING

### If Mypy Still Fails After Fixes

1. **STOP** - Do not continue with more fixes
2. **ANALYZE** - Use `grep` to find specific remaining errors
3. **INVESTIGATE** - Check if the fix introduced new issues
4. **REVERT** - If fix caused problems, revert and try different approach
5. **REPORT** - Document what was attempted and why it failed

### If Multiple Categories Have Issues

1. **PRIORITIZE** - Always fix CRITICAL first, then HIGH, then MEDIUM, then LOW
2. **ISOLATE** - Fix one category completely before moving to next
3. **VALIDATE** - Run verification protocol after each category
4. **DOCUMENT** - Keep track of what was fixed in each category

## 📋 AI EXECUTION CHECKLIST

**Before Starting:**

- [ ] Confirm you are in the project root directory
- [ ] Verify you have access to `uv run mypy` command
- [ ] Understand the priority system (CRITICAL → HIGH → MEDIUM → LOW)

**During Execution:**

- [ ] Follow the exact sequence: Assessment → Categorize → Fix → Verify
- [ ] Fix ONE category at a time
- [ ] Run verification protocol after each category
- [ ] Document what was fixed and why

**After Completion:**

- [ ] All success criteria met
- [ ] No regressions introduced
- [ ] All critical and high-priority issues resolved
- [ ] Mypy passes with `uv run mypy .`

## 🔧 COMMON FIX TEMPLATES

### Template 1: Add Missing Type Imports

```python
# BEFORE: error: Name "Optional" is not defined
def get_value(key: str) -> Optional[str]:
    return data.get(key)

# AFTER: Add import
from typing import Optional

def get_value(key: str) -> Optional[str]:
    return data.get(key)
```

### Template 2: Fix Function Signature

```python
# BEFORE: error: Incompatible return value type
def calculate(x: int, y: int) -> str:
    return x + y  # Returns int, not str

# AFTER: Fix return type
def calculate(x: int, y: int) -> int:
    return x + y
```

### Template 3: Handle Optional Values

```python
# BEFORE: error: Item "None" has no attribute "upper"
def format_name(name: str | None) -> str:
    return name.upper()

# AFTER: Add type guard
def format_name(name: str | None) -> str:
    if name is None:
        return ""
    return name.upper()

# Alternative: Use assertion if None is impossible
def format_name(name: str | None) -> str:
    assert name is not None, "name cannot be None"
    return name.upper()
```

### Template 4: Fix Type Narrowing

```python
# BEFORE: error: Argument has incompatible type "str | int"
def process_string(value: str) -> None:
    print(value.upper())

data: str | int = get_data()
process_string(data)

# AFTER: Add isinstance check
data: str | int = get_data()
if isinstance(data, str):
    process_string(data)
else:
    process_string(str(data))
```

### Template 5: Add Generic Type Parameters

```python
# BEFORE: error: Missing type parameters
def get_items() -> list:
    return [1, 2, 3]

# AFTER: Add type parameter
def get_items() -> list[int]:
    return [1, 2, 3]
```

## 🎯 AI SUCCESS METRICS

**Primary Success**: `uv run mypy .` passes with exit code 0
**Secondary Success**: All type errors resolved systematically
**Tertiary Success**: Code quality improved with better type safety

**AI RULE**: Primary success is mandatory. Secondary and tertiary are preferred but not blocking.

## 📊 MYPY ERROR CODE CATEGORIZATION GUIDE

### Common Mypy Error Codes

| Code           | Category   | Priority | Description                | Fix Pattern                       |
| -------------- | ---------- | -------- | -------------------------- | --------------------------------- |
| import         | Import     | CRITICAL | Cannot find module/import  | Add import or install stubs       |
| name-defined   | Name       | CRITICAL | Name not defined           | Import or define name             |
| attr-defined   | Attribute  | CRITICAL | Attribute does not exist   | Fix attribute or add type: ignore |
| return-value   | Return     | HIGH     | Incompatible return type   | Fix return value or type          |
| arg-type       | Argument   | HIGH     | Incompatible argument type | Fix argument or parameter         |
| union-attr     | Optional   | HIGH     | None has no attribute      | Add type guard                    |
| var-annotated  | Annotation | HIGH     | Missing type annotation    | Add type annotation               |
| assignment     | Assignment | HIGH     | Incompatible assignment    | Fix types on both sides           |
| no-untyped-def | Definition | MEDIUM   | Function lacks annotation  | Add full type signature           |
| redundant-cast | Cast       | MEDIUM   | Unnecessary cast           | Remove cast                       |
| unused-ignore  | Ignore     | MEDIUM   | Unused type: ignore        | Remove comment                    |
| no-any-return  | Any        | LOW      | Returns Any                | Make return type specific         |

## 🔍 DEBUGGING GUIDE

### If Mypy Command Fails

```bash
# Check if mypy is installed
uv run mypy --version

# Check mypy configuration
cat pyproject.toml | grep -A 20 "\[tool.mypy\]"

# Run with verbose output
uv run mypy . --verbose

# Show error codes
uv run mypy . --show-error-codes

# Show traceback for debugging
uv run mypy . --show-traceback
```

### If Specific Issues Persist

```bash
# Get help on specific error code
uv run mypy --help-error-code <error-code>

# Check specific file only
uv run mypy path/to/problematic_file.py

# Ignore specific error temporarily
# Add to pyproject.toml:
# [[tool.mypy.overrides]]
# module = "problematic_module.*"
# ignore_errors = true
```

### Understanding Type Checker Behavior

```bash
# Show inferred types
uv run mypy --show-column-numbers path/to/file.py

# Check what mypy sees
uv run mypy --show-traceback path/to/file.py

# Understand why something fails
uv run mypy --no-error-summary path/to/file.py
```

## 🚀 OPTIMIZATION TIPS

### For Large Codebases

1. **Focus on Critical Issues First** - Fix import and name errors before type refinement
2. **Use Incremental Fixes** - Fix one file at a time
3. **Leverage Type Stubs** - Install type stubs for third-party libraries
4. **Use mypy Cache** - Mypy caches results for faster subsequent runs

### For Performance

1. **Use Specific Paths** - Run mypy on specific directories when possible
2. **Enable Incremental Mode** - Use `--incremental` for faster checks
3. **Parallel Checking** - Mypy uses multiple processes by default

### Type Annotation Strategies

1. **Start with Public APIs** - Annotate public functions first
2. **Use Type Inference** - Let mypy infer simple variable types
3. **Add Gradual Types** - Use `Any` temporarily, refine later
4. **Document Complex Types** - Add comments explaining complex type annotations

## 📝 DOCUMENTATION REQUIREMENTS

### Required Documentation for Each Fix

1. **Issue Description** - What was the mypy error?
2. **Root Cause** - Why did it occur?
3. **Fix Applied** - What change was made?
4. **Verification** - How was it confirmed fixed?
5. **Impact** - Any side effects or considerations?

### Example Documentation Format

```text
FIX: union-attr - Optional attribute access in server/auth/utils.py:42
CAUSE: Function parameter was Optional[User] but accessed .name without check
CHANGE: Added type guard: if user is None: return ""
VERIFY: Ran 'uv run mypy server/auth/utils.py' - no errors
IMPACT: More explicit None handling, prevents runtime AttributeError
```

## 🎯 AI EXECUTION SUCCESS CRITERIA

**MANDATORY SUCCESS CONDITIONS:**

1. **Mypy Passes**: `uv run mypy .` exits with code 0
2. **No Regressions**: All existing functionality preserved
3. **Type Safety**: All critical and high-priority issues resolved
4. **Documentation**: All fixes properly documented

**OPTIONAL SUCCESS CONDITIONS:**

1. **Type Precision**: All medium-priority issues resolved
2. **Performance**: No performance degradation
3. **Maintainability**: Code is more type-safe and maintainable

**AI RULE**: Focus on mandatory success conditions first. Optional conditions are nice-to-have but not blocking.

## 🔄 COMMON SCENARIOS AND SOLUTIONS

### Scenario 1: Third-Party Library Without Stubs

```bash
# Error: Library stubs not installed for "requests"
# Solution: Install type stubs
uv pip install types-requests

# If stubs don't exist, ignore the module
# Add to pyproject.toml:
# [[tool.mypy.overrides]]
# module = "untyped_library.*"
# ignore_missing_imports = true
```

### Scenario 2: Complex Union Types

```python
# Problem: Too many Union combinations
def process(data: str | int | float | bool | None) -> str:
    return str(data)

# Solution: Use broader base type or Any
from typing import Any
def process(data: Any) -> str:
    return str(data)

# Better: Use Protocol if possible
from typing import Protocol
class Stringable(Protocol):
    def __str__(self) -> str: ...

def process(data: Stringable) -> str:
    return str(data)
```

### Scenario 3: Recursive Types

```python
# Problem: Recursive type definition
from typing import Union, Dict, List
JSON = Union[Dict[str, "JSON"], List["JSON"], str, int, float, bool, None]

# Solution: Use proper recursive type
from typing import Any
JSON = dict[str, Any] | list[Any] | str | int | float | bool | None
```

---

**Remember**: This prompt focuses on investigating and fixing mypy type errors systematically. Always run mypy after making changes and ensure no regressions are introduced.

**AI INSTRUCTION**: Follow the exact sequence outlined above. Do not skip steps or deviate from the priority order. Your success will be measured by the successful execution of `uv run mypy .` with exit code 0.
