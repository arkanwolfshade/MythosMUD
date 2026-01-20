# Migration Plan

This document outlines the step-by-step migration plan for transitioning from legacy error handlers to the new modular architecture.

## Phase 1: Create New Sanitization Module

### Step 1.1: Create sanitization.py

- Create `server/error_handlers/sanitization.py`
- Copy sanitization functions from legacy file:
  - `_is_safe_detail_key()`
  - `_sanitize_detail_value()`
  - `_sanitize_context()`
  - `sanitize_html_content()`
  - `sanitize_text_content()`
- Make helper functions public by removing leading underscore:
  - `_is_safe_detail_key()` → `is_safe_detail_key()`
  - `_sanitize_detail_value()` → `sanitize_detail_value()`
  - `_sanitize_context()` → `sanitize_context()`
- Add comprehensive module docstring
- Add type hints to all functions
- Add detailed docstrings with security notes
- Define `__all__` list

### Step 1.2: Update error_handlers/__init__.py

- Import sanitization functions
- Add to `__all__` list
- Update module docstring to remove legacy note

## Phase 2: Update Test Imports

### Step 2.1: Update test_error_handlers.py

- Change imports from `server.legacy_error_handlers` to `server.error_handlers.sanitization`
- Update function names if they changed (underscore removal)
- Run tests to verify functionality preserved
- Fix any assertion failures due to function renames

### Step 2.2: Search for Other Imports

- Run: `grep -r "from server.legacy_error_handlers import" server/`
- Run: `grep -r "from .legacy_error_handlers import" server/`
- Update any found imports to use new modules

## Phase 3: Remove Legacy Code

### Step 3.1: Delete Deprecated Exception Handlers

From `server/legacy_error_handlers.py`, remove:

- `mythos_exception_handler()`
- `general_exception_handler()`
- `logged_http_exception_handler()`
- `http_exception_handler()`
- `register_error_handlers()` function

### Step 3.2: Delete ErrorResponse Class and Helpers

From `server/legacy_error_handlers.py`, remove:

- `ErrorResponse` class
- `create_error_response()` function
- `_map_error_type()` function
- `_get_severity_for_error()` function
- `_get_status_code_for_error()` function

### Step 3.3: Verify No Remaining Usage

- Search for `ErrorResponse(` usage in codebase
- Search for `create_error_response(` usage
- Ensure all found instances are in files being deleted or updated

### Step 3.4: Delete Legacy File

- Once all functions are migrated or confirmed unused, delete entire file
- Remove from any `__init__.py` imports
- Remove from git

## Phase 4: Verification

### Step 4.1: Run Test Suite

- Run full test suite: `make test`
- Verify all tests pass
- Check for any import errors
- Verify coverage remains above 80%

### Step 4.2: Code Quality Checks

- Run linting: `make lint`
- Fix any linting errors
- Verify formatting is correct

### Step 4.3: Import Verification

- Run: `grep -r "legacy_error_handlers" server/`
- Should only find references in:
  - This migration spec documentation
  - Git history
  - No actual code imports

### Step 4.4: Manual Verification

- Start development server
- Trigger various error conditions
- Verify error responses use new handlers
- Check logs for proper error formatting

## Phase 5: Documentation Update

### Step 5.1: Update Module Documentation

- Update `server/error_handlers/__init__.py` docstring
- Remove notes about legacy migration
- Add completion date of migration

### Step 5.2: Update Architecture Documentation

- Update any architecture docs mentioning error handling
- Remove references to legacy error handlers
- Ensure docs point to new modular structure

### Step 5.3: Git Commit

- Create comprehensive commit message
- Reference this spec in commit
- Link to any related issues
- Tag commit with migration completion

## Rollback Plan

If issues are discovered after migration:

1. __Immediate Rollback__: Git revert the migration commits
2. __Root Cause Analysis__: Identify what broke and why
3. __Fix Forward**: Address the issue and re-apply migration
4. __Additional Testing__: Add tests to prevent regression

## Success Criteria

Migration is complete when:

- ✅ All sanitization functions in `server/error_handlers/sanitization.py`
- ✅ All tests passing with updated imports
- ✅ No imports from `legacy_error_handlers.py` remain
- ✅ File `server/legacy_error_handlers.py` deleted
- ✅ Linting passes
- ✅ Test coverage remains ≥80%
- ✅ Development server starts without errors
- ✅ Error responses work correctly in manual testing
