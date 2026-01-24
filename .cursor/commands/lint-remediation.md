---
description: Rules for fixing linting errors found
alwaysApply: false
---
# Lint Remediation Prompt - AI-Optimized Version

*"In the arcane libraries of code quality, we discover that proper linting requires systematic error categorization, methodical remediation patterns, and thorough validation protocols. The path to clean code lies not in hasty fixes, but in structured lint remediation and comprehensive verification."*

## 🎯 MANDATORY AI EXECUTION PROTOCOL

**CRITICAL**: You MUST follow this exact sequence. Do not skip steps or deviate from the order.

### Phase 1: Initial Assessment (REQUIRED FIRST)

```bash
# Step 1: Run linting to get current state

make lint
```

**AI ACTION**: Capture the complete lint output. If lint passes, STOP - no remediation needed.

**AI RULE**: If lint fails, continue to Phase 2. If lint passes, document success and exit.

### Phase 2: Categorize and Prioritize Lint Issues

**AI DECISION TREE**: For each lint issue, categorize into ONE of these priority levels:

#### 🔴 CRITICAL (Fix First - Blocking Issues)

**Python compilation errors** (prevents execution)

**TypeScript compilation errors** (prevents build)

**Import resolution failures** (breaks module loading)
- **Syntax errors** (invalid code structure)

#### 🟡 HIGH PRIORITY (Fix Second - Core Functionality)

**Unused imports/variables** (code quality issues)

**Import sorting violations** (I001, isort issues)

**Line length violations** (E501, max-len)
- **Missing dependencies in hooks** (react-hooks/exhaustive-deps)

#### 🟢 MEDIUM PRIORITY (Fix Third - Enhancement)

**Unused loop variables** (B007)

**Code style violations** (formatting issues)

**Deprecated patterns** (UP upgrade suggestions)
- **Performance warnings** (optimization opportunities)

#### 🔵 LOW PRIORITY (Fix Last - Polish)

**Minor style inconsistencies** (non-functional)

**Documentation warnings** (non-blocking)

**Optional best practices** (nice-to-have)

### Phase 3: Systematic Fixing Process

**AI RULE**: Fix ONE category at a time. Do not move to the next category until current one is resolved.

#### For Each Issue Category

1. **IDENTIFY**: Use specific tools to locate the exact issues
2. **ANALYZE**: Understand root cause before attempting fix
3. **FIX**: Apply targeted solution using search_replace tool
4. **VERIFY**: Run lint again to confirm fix works
5. **VALIDATE**: Ensure no regressions introduced

### Phase 4: Tool Selection Guide

**AI TOOL MAPPING**: Use these specific tools for each issue type:

#### Python/Ruff Issues

```bash
# REQUIRED: Check specific Ruff issues

uv run ruff check --line-length=120 .
```

**AI ACTION**: Use `grep` to find specific error codes, `read_file` to examine files, `search_replace` to fix issues.

#### React/ESLint Issues

```bash
# REQUIRED: Check specific ESLint issues

cd client && npx eslint --fix .
```

**AI ACTION**: Use `grep` to find specific error codes, `read_file` to examine files, `search_replace` to fix issues.

### Phase 5: Fix Implementation Patterns

#### 🔴 CRITICAL FIXES - Compilation Errors

```python
# Pattern 1: Fix missing imports
# BEFORE: NameError: name 'Component' is not defined
# AFTER: Add missing import

from .component import Component

# Pattern 2: Fix syntax errors
# BEFORE: def function(  # Missing closing parenthesis
# AFTER:  def function()

```

```typescript
// Pattern 1: Fix missing imports
// BEFORE: Component not defined
// AFTER: Add missing import
import { Component } from './Component';

// Pattern 2: Fix TypeScript errors
// BEFORE: Property 'title' does not exist
// AFTER: Define proper interface
interface Props {
  title: string;
}
```

#### 🟡 HIGH PRIORITY FIXES - Code Quality Issues

```python
# Pattern 1: Fix unused imports
# BEFORE: import os  # F401: imported but unused
# AFTER:  Remove unused import

# Pattern 2: Fix import sorting
# BEFORE: import b; import a  # I001: import sorting
# AFTER:  import a; import b

# Pattern 3: Fix line length
# BEFORE: very_long_line_that_exceeds_120_characters_limit
# AFTER:  Break into multiple lines

very_long_line_that_exceeds_120_characters_limit = (
    "broken into multiple lines"
)
```

```typescript
// Pattern 1: Fix unused variables
// BEFORE: const unusedVar = 'value';  // @typescript-eslint/no-unused-vars
// AFTER:  Remove unused variable or prefix with underscore

// Pattern 2: Fix hook dependencies
// BEFORE: useEffect(() => { fetchData(userId); }, []);  // Missing dependency
// AFTER:  useEffect(() => { fetchData(userId); }, [userId]);
```

#### 🟢 MEDIUM PRIORITY FIXES - Style Issues

```python
# Pattern 1: Fix unused loop variables
# BEFORE: for player_id, websocket in items():  # B007: unused variable
# AFTER:  for _player_id, websocket in items():  # Prefix with underscore

# Pattern 2: Fix deprecated patterns
# BEFORE: dict.keys()  # UP: use list(dict.keys())
# AFTER:  list(dict.keys())

```

### Phase 6: Verification Protocol

**AI MANDATORY CHECKS**: After each fix, run these commands in order:

```bash
# 1. Verify Python linting

make lint

# 2. Check specific Ruff issues

uv run ruff check --line-length=120 .

# 3. Check specific ESLint issues

cd client && npx eslint --fix .
```

**AI RULE**: If ANY check fails, STOP and fix the issue before proceeding.

### Phase 7: Success Validation

**AI SUCCESS CRITERIA**: All of these must pass:

- [ ] `make lint` exits with code 0
- [ ] No Python/Ruff errors remaining
- [ ] No React/ESLint errors remaining
- [ ] No new lint violations introduced
- [ ] All critical and high-priority issues resolved

## 🚨 AI ERROR HANDLING

### If Lint Still Fails After Fixes

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
- [ ] Verify you have access to `make lint` command
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
- [ ] Lint passes with `make lint`

## 🔧 COMMON FIX TEMPLATES

### Template 1: Python Import Fix

```python
# BEFORE: F401 - imported but unused

import os
import sys
def function():
    return "hello"

# AFTER: Remove unused imports

def function():
    return "hello"
```

### Template 2: Python Import Sorting Fix

```python
# BEFORE: I001 - import sorting

import sys
import os
from typing import List

# AFTER: Proper import order

import os
import sys

from typing import List
```

### Template 3: Python Line Length Fix

```python
# BEFORE: E501 - line too long

very_long_variable_name = "this is a very long string that exceeds the 120 character limit and needs to be broken down"

# AFTER: Break into multiple lines

very_long_variable_name = (
    "this is a very long string that exceeds the 120 character limit "
    "and needs to be broken down"
)
```

### Template 4: React Hook Dependency Fix

```typescript
// BEFORE: react-hooks/exhaustive-deps
useEffect(() => {
  fetchData(userId);
}, []); // Missing userId dependency

// AFTER: Include all dependencies
useEffect(() => {
  fetchData(userId);
}, [userId]); // Include userId dependency
```

### Template 5: TypeScript Unused Variable Fix

```typescript
// BEFORE: @typescript-eslint/no-unused-vars
const unusedVariable = 'value';
const usedVariable = 'value';

// AFTER: Remove unused or prefix with underscore
const _unusedVariable = 'value'; // Prefix with underscore
const usedVariable = 'value';
```

## 🎯 AI SUCCESS METRICS

**Primary Success**: `make lint` passes with exit code 0
**Secondary Success**: All Python/Ruff and React/ESLint checks pass
**Tertiary Success**: No new lint violations introduced

**AI RULE**: Primary success is mandatory. Secondary and tertiary are preferred but not blocking.

## 📊 LINT ISSUE CATEGORIZATION GUIDE

### Python/Ruff Error Codes

| Code | Category | Priority | Description               | Fix Pattern      |
| ---- | -------- | -------- | ------------------------- | ---------------- |
| F401 | Import   | HIGH     | Imported but unused       | Remove import    |
| I001 | Import   | HIGH     | Import sorting            | Reorder imports  |
| E501 | Style    | HIGH     | Line too long             | Break into lines |
| B007 | Style    | MEDIUM   | Unused loop variable      | Prefix with _    |
| UP   | Upgrade  | MEDIUM   | Python upgrade suggestion | Update syntax    |

### React/ESLint Error Codes

| Code                              | Category | Priority | Description              | Fix Pattern             |
| --------------------------------- | -------- | -------- | ------------------------ | ----------------------- |
| react-hooks/exhaustive-deps       | Hook     | HIGH     | Missing dependencies     | Add to deps array       |
| @typescript-eslint/no-unused-vars | Variable | HIGH     | Unused variables         | Remove or prefix with _ |
| max-len                           | Style    | HIGH     | Line too long            | Break into lines        |
| prefer-const                      | Style    | MEDIUM   | Use const instead of let | Change to const         |

## 🔍 DEBUGGING GUIDE

### If Lint Command Fails

```bash
# Check if make command exists

which make

# Check if lint script exists

ls scripts/lint.py

# Run lint script directly

python scripts/lint.py

# Check Ruff installation

uv run ruff --version

# Check ESLint installation

cd client && npx eslint --version
```

### If Specific Issues Persist

```bash
# Check Ruff configuration

cat pyproject.toml | grep -A 20 "\[tool.ruff\]"

# Check ESLint configuration

cat client/eslint.config.js

# Run Ruff with verbose output

uv run ruff check --line-length=120 . --verbose

# Run ESLint with verbose output

cd client && npx eslint . --debug
```

## 🚀 OPTIMIZATION TIPS

### For Large Codebases

1. **Focus on Critical Issues First** - Fix compilation errors before style issues
2. **Use Incremental Fixes** - Fix one file at a time
3. **Leverage Auto-fix** - Use `--fix` flag when possible
4. **Batch Similar Issues** - Group similar fixes together

### For Performance

1. **Use Specific Paths** - Run lint on specific directories when possible
2. **Enable Caching** - Use lint caching for faster subsequent runs
3. **Parallel Processing** - Run Python and React linting in parallel when possible

## 📝 DOCUMENTATION REQUIREMENTS

### Required Documentation for Each Fix

1. **Issue Description** - What was the lint error?
2. **Root Cause** - Why did it occur?
3. **Fix Applied** - What change was made?
4. **Verification** - How was it confirmed fixed?
5. **Impact** - Any side effects or considerations?

### Example Documentation Format

```text
FIX: F401 - Unused import in server/auth/utils.py
CAUSE: Import was added but never used in the code
CHANGE: Removed unused 'os' import
VERIFY: Ran 'uv run ruff check server/auth/utils.py' - no errors
IMPACT: No functional changes, cleaner code
```

## 🎯 AI EXECUTION SUCCESS CRITERIA

**MANDATORY SUCCESS CONDITIONS:**

1. **Lint Passes**: `make lint` exits with code 0
2. **No Regressions**: All existing functionality preserved
3. **Code Quality**: All critical and high-priority issues resolved
4. **Documentation**: All fixes properly documented

**OPTIONAL SUCCESS CONDITIONS:**

1. **Style Consistency**: All medium-priority issues resolved
2. **Performance**: No performance degradation
3. **Maintainability**: Code is easier to maintain

**AI RULE**: Focus on mandatory success conditions first. Optional conditions are nice-to-have but not blocking.

---

**Remember**: This prompt focuses on investigating and fixing lint issues systematically. Always run lint after making changes and ensure no regressions are introduced.

**AI INSTRUCTION**: Follow the exact sequence outlined above. Do not skip steps or deviate from the priority order. Your success will be measured by the successful execution of `make lint` with exit code 0.

# Lint Remediation Prompt - AI-Optimized Version

*"In the arcane libraries of code quality, we discover that proper linting requires systematic error categorization, methodical remediation patterns, and thorough validation protocols. The path to clean code lies not in hasty fixes, but in structured lint remediation and comprehensive verification."*

## 🎯 MANDATORY AI EXECUTION PROTOCOL

**CRITICAL**: You MUST follow this exact sequence. Do not skip steps or deviate from the order.

### Phase 1: Initial Assessment (REQUIRED FIRST)

```bash
# Step 1: Run linting to get current state

make lint
```

**AI ACTION**: Capture the complete lint output. If lint passes, STOP - no remediation needed.

**AI RULE**: If lint fails, continue to Phase 2. If lint passes, document success and exit.

### Phase 2: Categorize and Prioritize Lint Issues

**AI DECISION TREE**: For each lint issue, categorize into ONE of these priority levels:

#### 🔴 CRITICAL (Fix First - Blocking Issues)

**Python compilation errors** (prevents execution)

**TypeScript compilation errors** (prevents build)

**Import resolution failures** (breaks module loading)
- **Syntax errors** (invalid code structure)

#### 🟡 HIGH PRIORITY (Fix Second - Core Functionality)

**Unused imports/variables** (code quality issues)

**Import sorting violations** (I001, isort issues)

**Line length violations** (E501, max-len)
- **Missing dependencies in hooks** (react-hooks/exhaustive-deps)

#### 🟢 MEDIUM PRIORITY (Fix Third - Enhancement)

**Unused loop variables** (B007)

**Code style violations** (formatting issues)

**Deprecated patterns** (UP upgrade suggestions)
- **Performance warnings** (optimization opportunities)

#### 🔵 LOW PRIORITY (Fix Last - Polish)

**Minor style inconsistencies** (non-functional)

**Documentation warnings** (non-blocking)

**Optional best practices** (nice-to-have)

### Phase 3: Systematic Fixing Process

**AI RULE**: Fix ONE category at a time. Do not move to the next category until current one is resolved.

#### For Each Issue Category

1. **IDENTIFY**: Use specific tools to locate the exact issues
2. **ANALYZE**: Understand root cause before attempting fix
3. **FIX**: Apply targeted solution using search_replace tool
4. **VERIFY**: Run lint again to confirm fix works
5. **VALIDATE**: Ensure no regressions introduced

### Phase 4: Tool Selection Guide

**AI TOOL MAPPING**: Use these specific tools for each issue type:

#### Python/Ruff Issues

```bash
# REQUIRED: Check specific Ruff issues

uv run ruff check --line-length=120 .
```

**AI ACTION**: Use `grep` to find specific error codes, `read_file` to examine files, `search_replace` to fix issues.

#### React/ESLint Issues

```bash
# REQUIRED: Check specific ESLint issues

cd client && npx eslint --fix .
```

**AI ACTION**: Use `grep` to find specific error codes, `read_file` to examine files, `search_replace` to fix issues.

### Phase 5: Fix Implementation Patterns

#### 🔴 CRITICAL FIXES - Compilation Errors

```python
# Pattern 1: Fix missing imports
# BEFORE: NameError: name 'Component' is not defined
# AFTER: Add missing import

from .component import Component

# Pattern 2: Fix syntax errors
# BEFORE: def function(  # Missing closing parenthesis
# AFTER:  def function()

```

```typescript
// Pattern 1: Fix missing imports
// BEFORE: Component not defined
// AFTER: Add missing import
import { Component } from './Component';

// Pattern 2: Fix TypeScript errors
// BEFORE: Property 'title' does not exist
// AFTER: Define proper interface
interface Props {
  title: string;
}
```

#### 🟡 HIGH PRIORITY FIXES - Code Quality Issues

```python
# Pattern 1: Fix unused imports
# BEFORE: import os  # F401: imported but unused
# AFTER:  Remove unused import

# Pattern 2: Fix import sorting
# BEFORE: import b; import a  # I001: import sorting
# AFTER:  import a; import b

# Pattern 3: Fix line length
# BEFORE: very_long_line_that_exceeds_120_characters_limit
# AFTER:  Break into multiple lines

very_long_line_that_exceeds_120_characters_limit = (
    "broken into multiple lines"
)
```

```typescript
// Pattern 1: Fix unused variables
// BEFORE: const unusedVar = 'value';  // @typescript-eslint/no-unused-vars
// AFTER:  Remove unused variable or prefix with underscore

// Pattern 2: Fix hook dependencies
// BEFORE: useEffect(() => { fetchData(userId); }, []);  // Missing dependency
// AFTER:  useEffect(() => { fetchData(userId); }, [userId]);
```

#### 🟢 MEDIUM PRIORITY FIXES - Style Issues

```python
# Pattern 1: Fix unused loop variables
# BEFORE: for player_id, websocket in items():  # B007: unused variable
# AFTER:  for _player_id, websocket in items():  # Prefix with underscore

# Pattern 2: Fix deprecated patterns
# BEFORE: dict.keys()  # UP: use list(dict.keys())
# AFTER:  list(dict.keys())

```

### Phase 6: Verification Protocol

**AI MANDATORY CHECKS**: After each fix, run these commands in order:

```bash
# 1. Verify Python linting

make lint

# 2. Check specific Ruff issues

uv run ruff check --line-length=120 .

# 3. Check specific ESLint issues

cd client && npx eslint --fix .
```

**AI RULE**: If ANY check fails, STOP and fix the issue before proceeding.

### Phase 7: Success Validation

**AI SUCCESS CRITERIA**: All of these must pass:

- [ ] `make lint` exits with code 0
- [ ] No Python/Ruff errors remaining
- [ ] No React/ESLint errors remaining
- [ ] No new lint violations introduced
- [ ] All critical and high-priority issues resolved

## 🚨 AI ERROR HANDLING

### If Lint Still Fails After Fixes

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
- [ ] Verify you have access to `make lint` command
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
- [ ] Lint passes with `make lint`

## 🔧 COMMON FIX TEMPLATES

### Template 1: Python Import Fix

```python
# BEFORE: F401 - imported but unused

import os
import sys
def function():
    return "hello"

# AFTER: Remove unused imports

def function():
    return "hello"
```

### Template 2: Python Import Sorting Fix

```python
# BEFORE: I001 - import sorting

import sys
import os
from typing import List

# AFTER: Proper import order

import os
import sys

from typing import List
```

### Template 3: Python Line Length Fix

```python
# BEFORE: E501 - line too long

very_long_variable_name = "this is a very long string that exceeds the 120 character limit and needs to be broken down"

# AFTER: Break into multiple lines

very_long_variable_name = (
    "this is a very long string that exceeds the 120 character limit "
    "and needs to be broken down"
)
```

### Template 4: React Hook Dependency Fix

```typescript
// BEFORE: react-hooks/exhaustive-deps
useEffect(() => {
  fetchData(userId);
}, []); // Missing userId dependency

// AFTER: Include all dependencies
useEffect(() => {
  fetchData(userId);
}, [userId]); // Include userId dependency
```

### Template 5: TypeScript Unused Variable Fix

```typescript
// BEFORE: @typescript-eslint/no-unused-vars
const unusedVariable = 'value';
const usedVariable = 'value';

// AFTER: Remove unused or prefix with underscore
const _unusedVariable = 'value'; // Prefix with underscore
const usedVariable = 'value';
```

## 🎯 AI SUCCESS METRICS

**Primary Success**: `make lint` passes with exit code 0
**Secondary Success**: All Python/Ruff and React/ESLint checks pass
**Tertiary Success**: No new lint violations introduced

**AI RULE**: Primary success is mandatory. Secondary and tertiary are preferred but not blocking.

## 📊 LINT ISSUE CATEGORIZATION GUIDE

### Python/Ruff Error Codes

| Code | Category | Priority | Description               | Fix Pattern      |
| ---- | -------- | -------- | ------------------------- | ---------------- |
| F401 | Import   | HIGH     | Imported but unused       | Remove import    |
| I001 | Import   | HIGH     | Import sorting            | Reorder imports  |
| E501 | Style    | HIGH     | Line too long             | Break into lines |
| B007 | Style    | MEDIUM   | Unused loop variable      | Prefix with _    |
| UP   | Upgrade  | MEDIUM   | Python upgrade suggestion | Update syntax    |

### React/ESLint Error Codes

| Code                              | Category | Priority | Description              | Fix Pattern             |
| --------------------------------- | -------- | -------- | ------------------------ | ----------------------- |
| react-hooks/exhaustive-deps       | Hook     | HIGH     | Missing dependencies     | Add to deps array       |
| @typescript-eslint/no-unused-vars | Variable | HIGH     | Unused variables         | Remove or prefix with _ |
| max-len                           | Style    | HIGH     | Line too long            | Break into lines        |
| prefer-const                      | Style    | MEDIUM   | Use const instead of let | Change to const         |

## 🔍 DEBUGGING GUIDE

### If Lint Command Fails

```bash
# Check if make command exists

which make

# Check if lint script exists

ls scripts/lint.py

# Run lint script directly

python scripts/lint.py

# Check Ruff installation

uv run ruff --version

# Check ESLint installation

cd client && npx eslint --version
```

### If Specific Issues Persist

```bash
# Check Ruff configuration

cat pyproject.toml | grep -A 20 "\[tool.ruff\]"

# Check ESLint configuration

cat client/eslint.config.js

# Run Ruff with verbose output

uv run ruff check --line-length=120 . --verbose

# Run ESLint with verbose output

cd client && npx eslint . --debug
```

## 🚀 OPTIMIZATION TIPS

### For Large Codebases

1. **Focus on Critical Issues First** - Fix compilation errors before style issues
2. **Use Incremental Fixes** - Fix one file at a time
3. **Leverage Auto-fix** - Use `--fix` flag when possible
4. **Batch Similar Issues** - Group similar fixes together

### For Performance

1. **Use Specific Paths** - Run lint on specific directories when possible
2. **Enable Caching** - Use lint caching for faster subsequent runs
3. **Parallel Processing** - Run Python and React linting in parallel when possible

## 📝 DOCUMENTATION REQUIREMENTS

### Required Documentation for Each Fix

1. **Issue Description** - What was the lint error?
2. **Root Cause** - Why did it occur?
3. **Fix Applied** - What change was made?
4. **Verification** - How was it confirmed fixed?
5. **Impact** - Any side effects or considerations?

### Example Documentation Format

```text
FIX: F401 - Unused import in server/auth/utils.py
CAUSE: Import was added but never used in the code
CHANGE: Removed unused 'os' import
VERIFY: Ran 'uv run ruff check server/auth/utils.py' - no errors
IMPACT: No functional changes, cleaner code
```

## 🎯 AI EXECUTION SUCCESS CRITERIA

**MANDATORY SUCCESS CONDITIONS:**

1. **Lint Passes**: `make lint` exits with code 0
2. **No Regressions**: All existing functionality preserved
3. **Code Quality**: All critical and high-priority issues resolved
4. **Documentation**: All fixes properly documented

**OPTIONAL SUCCESS CONDITIONS:**

1. **Style Consistency**: All medium-priority issues resolved
2. **Performance**: No performance degradation
3. **Maintainability**: Code is easier to maintain

**AI RULE**: Focus on mandatory success conditions first. Optional conditions are nice-to-have but not blocking.

---

**Remember**: This prompt focuses on investigating and fixing lint issues systematically. Always run lint after making changes and ensure no regressions are introduced.

**AI INSTRUCTION**: Follow the exact sequence outlined above. Do not skip steps or deviate from the priority order. Your success will be measured by the successful execution of `make lint` with exit code 0.
