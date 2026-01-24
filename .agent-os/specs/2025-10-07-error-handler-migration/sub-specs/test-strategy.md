# Test Strategy

This document outlines the testing strategy for the error handler migration to ensure functionality is preserved and no regressions are introduced.

## Testing Philosophy

**Preserve, Don't Change:**

- The migration should NOT change behavior, only code organization
- All existing tests should pass with minimal modifications
- Only update imports and function names, not test logic or assertions

## Test Files to Update

### Primary Test File: `server/tests/test_error_handlers.py`

**Current State:**

- Tests import from `server.legacy_error_handlers`
- Tests verify sanitization functions work correctly
- Tests verify error response creation
- Tests cover security-critical sanitization logic

**Required Changes:**

1. Update imports:

   ```python
   # OLD:

   from server.legacy_error_handlers import (
       _is_safe_detail_key,
       _sanitize_context,
       _sanitize_detail_value,
       create_error_response,
       sanitize_html_content,
       sanitize_text_content,
   )

   # NEW:

   from server.error_handlers.sanitization import (
       is_safe_detail_key,  # Note: no leading underscore
       sanitize_context,     # Note: no leading underscore
       sanitize_detail_value, # Note: no leading underscore
       sanitize_html_content,
       sanitize_text_content,
   )
   from server.error_handlers.standardized_responses import (
       create_standardized_error_response,
       handle_api_error,
   )
   ```

2. Update function calls for renamed functions:

   - `_is_safe_detail_key()` → `is_safe_detail_key()`
   - `_sanitize_detail_value()` → `sanitize_detail_value()`
   - `_sanitize_context()` → `sanitize_context()`

3. Update tests for `create_error_response()`:

   - Replace with equivalent calls to `create_standardized_error_response()` or `handle_api_error()`
   - Verify response format matches expected structure
   - May need to adjust assertions if response format differs slightly

### Secondary Test Files

**Search for Additional Test Files:**

```bash
grep -r "legacy_error_handlers" server/tests/
grep -r "ErrorResponse" server/tests/ --include="*.py"
grep -r "create_error_response" server/tests/ --include="*.py"
```

Update any found test files following the same pattern.

## Test Coverage Requirements

### Must Maintain Coverage For

**Sanitization Functions:**

✅ `is_safe_detail_key()` - Verify safe keys allowed, unsafe patterns blocked

✅ `sanitize_detail_value()` - Test string, dict, list, and other types
- ✅ `sanitize_context()` - Test context extraction and sanitization
- ✅ `sanitize_html_content()` - Test XSS prevention, tag filtering
- ✅ `sanitize_text_content()` - Test length limits, HTML removal

**Security Test Cases:**

- XSS attack prevention in HTML sanitization
- SQL injection patterns in detail values
- Path traversal attempts in file paths
- Stack trace exposure prevention
- Sensitive key filtering (passwords, tokens, etc.)

**Edge Cases:**

- Empty strings and None values
- Very long strings (length limits)
- Nested data structures
- Unicode and special characters
- Invalid input types

## Regression Testing

### Pre-Migration Baseline

1. Run full test suite: `make test`
2. Record current pass/fail count
3. Record current coverage percentage
4. Save output for comparison

### Post-Migration Verification

1. Run full test suite: `make test`
2. Verify same or more tests pass
3. Verify coverage ≥ 80% (same or better)
4. Compare output with baseline

### Specific Regression Checks

**Error Response Format:**

- Verify error responses have required fields: `error`, `type`, `message`, `user_friendly`
- Verify HTTP status codes match error types
- Verify sanitization prevents information disclosure

**Sanitization Behavior:**

- Verify same strings are sanitized the same way
- Verify same keys are blocked/allowed
- Verify same HTML tags are stripped/allowed

## Integration Testing

### Manual Testing Checklist

1. **Start Development Server:**

   ```bash
   ./scripts/start_local.ps1
   ```

   - Verify server starts without import errors
   - Check logs for any error handler warnings

2. **Trigger Error Conditions:**

   - Invalid login credentials (authentication error)
   - Malformed JSON (validation error)
   - Non-existent endpoint (404 error)
   - Send request with HTML in fields (sanitization test)
   - Send request with very long strings (length limit test)

3. **Verify Error Responses:**

   - Check response format is correct
   - Verify user-friendly messages are present
   - Confirm no sensitive information in response
   - Verify appropriate HTTP status codes

4. **Check Logs:**

   - Verify errors are logged correctly
   - Confirm no stack traces in user responses
   - Verify sanitization is applied in logs

## Test Execution Plan

### Phase 1: Pre-Migration Tests

```bash
# Run tests before any changes

make test > pre-migration-results.txt

# Check coverage
# Results should show ≥80% coverage

```

### Phase 2: Update Imports

```bash
# After updating imports in test files

make test

# Should pass with same results as Phase 1
# If failures, investigate import paths

```

### Phase 3: Update Function Names

```bash
# After changing function names (underscore removal)

make test

# May have failures due to function renames
# Update test code to use new names

```

### Phase 4: Final Verification

```bash
# After all migration complete

make test > post-migration-results.txt

# Compare with pre-migration results

diff pre-migration-results.txt post-migration-results.txt

# Run linting

make lint
```

### Phase 5: Integration Tests

```bash
# Start server

./scripts/start_local.ps1

# Run manual tests from checklist above
# Use Postman, curl, or web browser

```

## Success Criteria

Tests are successful when:
✅ All unit tests pass

✅ Test coverage ≥ 80% (same or better than before)

✅ No import errors
- ✅ No linting errors
- ✅ Manual integration tests pass
- ✅ Error responses format correctly
- ✅ Sanitization prevents XSS and information disclosure
- ✅ Server starts without errors

## Rollback Criteria

Roll back migration if:
❌ Test coverage drops below 80%

❌ Critical security tests fail

❌ Server fails to start
- ❌ Error responses expose sensitive information
- ❌ Sanitization fails to prevent XSS

## Documentation of Test Results

After migration completion, document:

1. Test execution timestamps
2. Pass/fail counts (before and after)
3. Coverage percentages (before and after)
4. Any test modifications required
5. Any issues discovered and resolved
6. Performance impact (if any)

Store results in: `.agent-os/specs/2025-10-07-error-handler-migration/test-results.md`
