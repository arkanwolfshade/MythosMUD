# Ruff to Pylint Rule Mapping

This document maps ruff linting rules to their pylint equivalents, focusing on rules that are suppressed in our configuration and need alignment between the two tools.

## Purpose

To ensure parity between `ruff` and `pylint` linting results, we need to:
1. Suppress the same issues in both tools
2. Understand which rules are equivalent
3. Document rules that have no direct equivalent

## Global Ignores (pyproject.toml)

### E501 - Line too long

- **Ruff**: `E501` (line too long, handled by line-length)
- **Pylint**: `C0301` (line-too-long)
- **Status**: ✅ **ALIGNED** - Both disabled in `.pylintrc` (`line-too-long` disabled)

### B008 - Function calls in argument defaults

- **Ruff**: `B008` (do not perform function calls in argument defaults)
- **Pylint**: No direct equivalent
- **Status**: ⚠️ **NO PYLINT EQUIVALENT** - This is a flake8-bugbear specific rule. Pylint does not check for function calls in default arguments by default. This is acceptable as it's a stylistic preference, not a critical issue.

## Per-File Ignores (pyproject.toml)

### `__init__.py` files: F401 (unused import)

- **Ruff**: `F401` (module imported but unused)
- **Pylint**: `W0611` (unused-import)
- **Status**: ⚠️ **NEEDS ALIGNMENT** - Should add per-file ignore for `__init__.py` files in `.pylintrc` using `pylint-per-file-ignores` plugin or inline suppressions

### `tests/**/*` files: B011 (assert on exception)

- **Ruff**: `B011` (do not assert False (python -O will remove check), use raise AssertionError)
- **Pylint**: No direct equivalent (pylint doesn't flag `assert False` in tests)
- **Status**: ✅ **ALIGNED** - Pylint doesn't check this, so no suppression needed

### `docs/**/*` files: Multiple rules

#### F821 - Undefined name

- **Ruff**: `F821` (undefined name)
- **Pylint**: `E0602` (undefined-variable) or `E0601` (undefined-name)
- **Status**: ⚠️ **NEEDS ALIGNMENT** - Docs may have intentional undefined names for examples

#### F841 - Unused variable

- **Ruff**: `F841` (local variable assigned but never used)
- **Pylint**: `W0612` (unused-variable)
- **Status**: ⚠️ **NEEDS ALIGNMENT** - Docs may have unused variables for examples

#### F811 - Redefined name

- **Ruff**: `F811` (redefined while unused)
- **Pylint**: `W0621` (redefined-outer-name) or `W0622` (redefined-builtin)
- **Status**: ⚠️ **NEEDS ALIGNMENT** - Docs may intentionally redefine for examples

#### B904 - Broad except

- **Ruff**: `B904` (within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None`)
- **Pylint**: `W0707` (raise-missing-from) - similar but not identical
- **Status**: ⚠️ **PARTIAL ALIGNMENT** - Pylint's rule is similar but not identical

#### E402 - Module level import not at top

- **Ruff**: `E402` (module level import not at top of file)
- **Pylint**: `C0413` (wrong-import-position) - similar concept
- **Status**: ⚠️ **PARTIAL ALIGNMENT** - Similar but not identical

### `server/stubs/**/*.pyi` files: UP046 (old Generic syntax)

- **Ruff**: `UP046` (use `X | Y` for type annotations instead of `typing.Union[X, Y]`)
- **Pylint**: No direct equivalent (pylint doesn't check for old typing syntax)
- **Status**: ✅ **ALIGNED** - Pylint doesn't check this, so no suppression needed

## Complexity Checking

### C901 - Too complex (PRIMARY COMPLEXITY CHECKER)

- **Ruff**: `C901` (function is too complex, max-complexity = 11)
  - Uses **McCabe cyclomatic complexity** (industry standard)
  - Measures decision points in code (if, elif, else, for, while, except, etc.)
  - Configurable threshold: `max-complexity = 11` (in `pyproject.toml`)
  - **Status**: ✅ **ENABLED** - This is our primary complexity metric
- **Pylint**: `R0911` (too-many-return-statements), `R0912` (too-many-branches), `R0913` (too-many-arguments), `R0914` (too-many-locals), `R0915` (too-many-statements), `R0902` (too-many-instance-attributes), `R0904` (too-many-public-methods)
  - Uses multiple separate metrics (counts of returns, branches, args, locals, statements, etc.)
  - Not configurable (hardcoded thresholds)
  - **Status**: ✅ **SUPPRESSED** - All R09xx complexity rules are disabled in `.pylintrc`
- **Strategy**: We use **Ruff C901** as the primary complexity checker because:
  1. It's an industry-standard metric (McCabe cyclomatic complexity)
  2. It's configurable (we can adjust the threshold)
  3. It provides a single, unified complexity score
  4. Pylint's multiple metrics create noise and aren't configurable
- **Inline Suppressions**:
  - **Ruff**: Use `# noqa: C901` to suppress complexity warnings
  - **Pylint**: If needed, use `# pylint: disable=too-many-arguments,too-many-locals,too-many-statements,too-many-return-statements,too-many-branches` (but typically not needed since R09xx rules are globally disabled)
- **Reference**: See `docs/LINTING_COMPLEXITY_ALIGNMENT.md` for detailed explanation of the differences and strategy

## Category Mappings

| Ruff Category | Pylint Category | Notes |
|--------------|------------------|-------|
| E (pycodestyle errors) | C (Convention), E (Error) | Overlapping but not identical |
| W (pycodestyle warnings) | W (Warning) | Overlapping but not identical |
| F (pyflakes) | F (Fatal) | Overlapping but not identical |
| B (flake8-bugbear) | R (Refactor) | Overlapping but not identical |
| C (McCabe complexity) | R (Refactor) | **Ruff C901 is primary, Pylint R09xx suppressed** |
| I (isort) | C (Convention) | Import organization |
| UP (pyupgrade) | W (Warning) | Code modernization |

## Rules with No Direct Pylint Equivalent

1. **B008** - Function calls in argument defaults (flake8-bugbear specific)
2. **B011** - Assert on exception (flake8-bugbear specific, but not relevant for pylint)
3. **UP046** - Old Generic syntax (pyupgrade specific, pylint doesn't check this)

## Rules with Partial Pylint Equivalents

1. **B904** - Broad except → Pylint `W0707` (raise-missing-from) - similar but not identical
2. **E402** - Module level import not at top → Pylint `C0413` (wrong-import-position) - similar concept
3. **C901** - Complexity → Pylint has multiple complexity-related rules (R0911-R0915, R0902, R0904) but uses different metrics. **We use Ruff C901 as the primary complexity checker and suppress all Pylint R09xx rules.** See `docs/LINTING_COMPLEXITY_ALIGNMENT.md` for details.

## Next Steps

1. ✅ Document mappings (this file)
2. ⏳ Add per-file suppressions to `.pylintrc` for `__init__.py` (F401 → W0611)
3. ⏳ Add per-file suppressions to `.pylintrc` for `docs/**/*` (multiple rules)
4. ⏳ Verify inline suppressions are aligned between tools
5. ⏳ Create verification script to check parity
