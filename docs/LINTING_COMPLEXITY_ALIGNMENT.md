# Complexity Checking Alignment: Ruff C901 vs Pylint

**Date**: 2025-01-28
**Status**: Analysis Complete

## Executive Summary

Ruff and Pylint use **fundamentally different approaches** to complexity checking:

- **Ruff (C901)**: Uses **McCabe cyclomatic complexity** - measures decision points in code
- **Pylint (R0911-R0915)**: Uses **multiple code metrics** - counts various code elements

These are **complementary, not equivalent** metrics. We should use ruff for cyclomatic complexity and suppress pylint's complexity metrics.

---

## Ruff C901: McCabe Cyclomatic Complexity

### What It Measures

Cyclomatic complexity counts the number of **independent paths** through a function by counting:

- Decision points (`if`, `elif`, `else`)
- Loops (`for`, `while`)
- Exception handlers (`try`, `except`)
- Boolean operators (`and`, `or`)
- Conditional expressions (`if` expressions)

### Configuration

```toml
[tool.ruff.lint.mccabe]
max-complexity = 11
```

**Current Status**: ✅ **ENABLED**
**Threshold**: 11 (matches Codacy threshold)
**Current Findings**: 3 functions exceed threshold

### Example

```python
def complex_function(x, y):
    if x > 0:          # +1
        if y > 0:      # +1
            return 1
        else:          # +1
            return 2
    else:              # +1
        return 3
    # Total complexity: 4
```

### Why It's Useful

- **Predicts testability**: Higher complexity = more test cases needed
- **Indicates refactoring needs**: Functions with complexity > 10-15 are harder to maintain
- **Industry standard**: Widely used metric (McCabe, 1976)

---

## Pylint Complexity Metrics (R0911-R0915)

### What They Measure

#### R0911: Too Many Return Statements

Counts the number of `return` statements in a function.

**Default Threshold**: 6
**Rationale**: Functions with many returns may be hard to follow

#### R0912: Too Many Branches

Counts the number of branches (`if`, `elif`, `except`, `for`, `while`).

**Default Threshold**: 12
**Rationale**: Similar to cyclomatic complexity but counts differently

#### R0913: Too Many Arguments

Counts function parameters.

**Default Threshold**: 5
**Rationale**: Functions with many arguments are harder to use and test

#### R0914: Too Many Local Variables

Counts local variable assignments.

**Default Threshold**: 15
**Rationale**: Functions with many variables may be doing too much

#### R0915: Too Many Statements

Counts executable statements (excluding comments, docstrings, blank lines).

**Default Threshold**: 50
**Rationale**: Long functions are harder to understand and maintain

### Configuration

Pylint does **not** have a configurable threshold for these rules in `.pylintrc`. The thresholds are hardcoded in pylint.

**Current Status**: ⚠️ **ENABLED** (by default)
**Current Findings**: ~935 findings across all R0911-R0915 rules

---

## Key Differences

| Aspect                   | Ruff C901                      | Pylint R0911-R0915                          |
| ------------------------ | ------------------------------ | ------------------------------------------- |
| **Metric Type**          | Single metric (cyclomatic)     | Multiple metrics (5 different rules)        |
| **What It Counts**       | Decision points                | Returns, branches, args, locals, statements |
| **Configurable**         | Yes (max-complexity)           | No (hardcoded thresholds)                   |
| **Philosophy**           | "How many paths through code?" | "How many of X in this function?"           |
| **Industry Standard**    | Yes (McCabe)                   | No (pylint-specific)                        |
| **Refactoring Guidance** | "Simplify control flow"        | "Reduce function size/complexity"           |

### Example Comparison

```python
def example_function(x, y, z, a, b, c, d):  # 7 args
    result = 0                              # local 1
    temp1 = x + y                           # local 2
    temp2 = z * a                           # local 3
    temp3 = b - c                           # local 4
    temp4 = d / 2                           # local 5
    if x > 0:                               # branch 1, complexity +1
        if y > 0:                           # branch 2, complexity +1
            result = temp1                  # statement 1
            return result                   # return 1
        else:                               # branch 3, complexity +1
            result = temp2                  # statement 2
            return result                   # return 2
    else:                                   # branch 4, complexity +1
        result = temp3                      # statement 3
        return result                       # return 3
    # Total: 4 branches, 3 returns, 7 args, 5 locals, 3 statements
    # Complexity: 4
```

**Ruff C901**: ✅ Passes (complexity 4 < 11)
**Pylint R0913**: ❌ Fails (7 args > 5)
**Pylint R0914**: ✅ Passes (5 locals < 15)
**Pylint R0915**: ✅ Passes (3 statements < 50)

---

## Current State Analysis

### Ruff C901 Findings

**Count**: 3 functions
**Files**: `scripts/compare_linting_results.py` (3 functions)

1. `compare_findings`: complexity 16 > 11
2. `categorize_findings`: complexity 16 > 11
3. `generate_report`: complexity 15 > 11

**Action**: These should be refactored to reduce complexity.

### Pylint R0911-R0915 Findings

**Count**: ~935 findings
**Breakdown**:

- R0913 (too-many-arguments): ~100+ findings
- R0914 (too-many-locals): ~50+ findings
- R0915 (too-many-statements): ~20+ findings
- R0911 (too-many-returns): ~10+ findings
- R0912 (too-many-branches): ~5+ findings
- R0902 (too-many-instance-attributes): ~50+ findings
- R0904 (too-many-public-methods): ~20+ findings

**Action**: These should be suppressed in `.pylintrc` (as recommended in `LINTING_PYLINT_UNIQUE_FINDINGS.md`).

---

## Recommended Strategy

### 1. Use Ruff for Cyclomatic Complexity ✅

**Rationale**:

- Industry-standard metric (McCabe)
- Configurable threshold
- Single, clear metric
- Already configured and working

**Action**: Keep ruff C901 enabled, refactor functions that exceed threshold.

### 2. Suppress Pylint Complexity Metrics ✅

**Rationale**:

- Different philosophy (multiple metrics vs. single metric)
- Not configurable (hardcoded thresholds)
- Creates noise (~935 findings)
- Ruff already handles complexity checking

**Action**: Add to `.pylintrc`:

```ini
[MESSAGES CONTROL]
disable=too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-statements,too-many-return-statements,too-many-branches,too-many-instance-attributes,too-many-public-methods
```

### 3. Align Inline Suppressions

**Rationale**: If a function is suppressed for complexity in one tool, it should be suppressed in the other.

**Current State**:

- Ruff: `# noqa: C901` for complexity suppressions
- Pylint: No equivalent inline suppression (would need to suppress multiple R0911-R0915 rules)

**Action**: When suppressing complexity:

- Use `# noqa: C901` for ruff
- Use `# pylint: disable=too-many-arguments,too-many-locals,too-many-statements,too-many-return-statements,too-many-branches` for pylint (if needed)

**Note**: Since we're suppressing these globally in `.pylintrc`, inline suppressions are not needed.

---

## Implementation Plan

### Step 1: Update `.pylintrc` ✅

Add complexity metrics to the disable list:

```ini
[MESSAGES CONTROL]
disable=line-too-long,import-outside-toplevel,too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-statements,too-many-return-statements,too-many-branches,too-many-instance-attributes,too-many-public-methods
```

### Step 2: Refactor Ruff C901 Violations

Refactor the 3 functions in `scripts/compare_linting_results.py`:

- `compare_findings` (complexity 16)
- `categorize_findings` (complexity 16)
- `generate_report` (complexity 15)

**Approach**: Extract helper functions to reduce complexity.

### Step 3: Document the Strategy

Update `docs/LINTING_RUFF_PYLINT_MAPPING.md` to clarify:

- Ruff C901 is the primary complexity checker
- Pylint R0911-R0915 are suppressed
- Inline suppressions should use `# noqa: C901` for ruff

### Step 4: Verify Alignment

Run comparison again to verify:

- Ruff C901 findings are addressed
- Pylint complexity findings are suppressed
- No conflicting suppressions

---

## Conclusion

**Ruff C901** and **Pylint R0911-R0915** measure different aspects of code complexity:

- **Ruff C901**: Cyclomatic complexity (decision points) - **KEEP ENABLED**
- **Pylint R0911-R0915**: Code metrics (counts) - **SUPPRESS**

This approach:

- ✅ Uses industry-standard cyclomatic complexity (ruff)
- ✅ Reduces noise from pylint (~935 findings)
- ✅ Maintains clear complexity checking via ruff
- ✅ Aligns with project's preference for ruff as primary linter

**Status**: Strategy defined, ready for implementation.
