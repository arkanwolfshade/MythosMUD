# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-10-07-error-handler-migration/spec.md

## Technical Requirements

### Module Structure

**New File: `server/error_handlers/sanitization.py`**

- Extract all sanitization functions from `server/legacy_error_handlers.py`:
  - `_is_safe_detail_key(key: str) -> bool`
  - `_sanitize_detail_value(value: Any) -> Any`
  - `_sanitize_context(context) -> dict[str, Any] | None`
  - `sanitize_html_content(content: str, allow_tags: list[str] | None = None) -> str`
  - `sanitize_text_content(content: str, max_length: int = 1000) -> str`
- Add comprehensive docstrings explaining security implications
- Add type hints for all parameters and return values
- Include usage examples in docstrings
- Export all public functions in `__all__`

**Update: `server/error_handlers/__init__.py`**

- Add imports from new `sanitization` module
- Update `__all__` to include sanitization functions
- Remove note about legacy error handlers (migration will be complete)
- Add migration completion date to module docstring

### Code Removal

**Functions to Remove from `server/legacy_error_handlers.py`:**

- `mythos_exception_handler()` - Superseded by `ErrorHandlingMiddleware`
- `general_exception_handler()` - Superseded by `ErrorHandlingMiddleware`
- `logged_http_exception_handler()` - Superseded by `ErrorHandlingMiddleware`
- `http_exception_handler()` - Superseded by `ErrorHandlingMiddleware`
- `register_error_handlers()` - Superseded by `server.middleware.error_handling_middleware.register_error_handlers()`
- `graceful_degradation()` - Already removed in previous cleanup
- `CircuitBreaker` class - Already removed in previous cleanup

**Classes to Remove:**

- `ErrorResponse` class - Superseded by `StandardizedErrorResponse`

**Helper Functions Associated with ErrorResponse:**

- `create_error_response()` - Superseded by `create_standardized_error_response()` and `handle_api_error()`
- `_map_error_type()` - Functionality now in `StandardizedErrorResponse._determine_error_type_from_exception()`
- `_get_severity_for_error()` - Functionality now in error type system
- `_get_status_code_for_error()` - Functionality now in `StandardizedErrorResponse.STATUS_CODE_MAPPINGS`

**File Deletion:**

- Delete `server/legacy_error_handlers.py` entirely once all functions are migrated or removed

### Import Updates

**Test Files to Update:**

- `server/tests/test_error_handlers.py`:
  - Change `from server.legacy_error_handlers import` to `from server.error_handlers.sanitization import`
  - Update any tests that use `ErrorResponse` to use `StandardizedErrorResponse`
  - Verify all assertions still pass with new imports

**Search Patterns for Finding Remaining Imports:**

```python
# Search patterns to execute

grep -r "from server.legacy_error_handlers import" server/
grep -r "from .legacy_error_handlers import" server/
grep -r "import server.legacy_error_handlers" server/
grep -r "ErrorResponse(" server/  # Find usage of old class
```

### Backwards Compatibility

**No Shim Required:**

- Find and fix all imports directly
- Use `grep` to ensure no lingering references
- Tests will catch any missed imports

**Migration Verification:**

- Run full test suite after each major change
- Verify no imports from `legacy_error_handlers.py` remain
- Confirm all error handling uses new modular architecture

### Code Quality Standards

**Type Hints:**

- All sanitization functions must have complete type hints
- Use `Any` from `typing` where appropriate for generic value handling
- Document any `None` return possibilities

**Documentation:**

- Each sanitization function needs comprehensive docstring
- Include security considerations in docstrings
- Provide usage examples for complex functions
- Document the bleach library dependency for HTML sanitization

**Testing:**

- Maintain all existing test coverage
- Update test imports but not test logic
- Verify behavior remains identical after migration
- Add docstrings to test functions explaining what they verify

### Security Considerations

**Sanitization Functions:**

- These functions are security-critical as they prevent XSS and information disclosure
- Any changes must preserve exact security behavior
- Document which patterns are blocked and why
- Maintain the bleach library integration for HTML sanitization

**Safe Detail Keys:**

- Document the whitelist of safe keys that don't expose sensitive information
- Document the blocklist patterns for unsafe keys
- Explain the rationale for each blocked pattern

## External Dependencies

No new external dependencies required. This is a pure refactoring/migration task using existing dependencies:

- `bleach` - Already used for HTML sanitization
- `typing` - Standard library for type hints
