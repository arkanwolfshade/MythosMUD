# Spec Tasks

## Tasks

- [ ] 1. **Create Sanitization Module**
  - [ ] 1.1 Create `server/error_handlers/sanitization.py` with module docstring and imports
  - [ ] 1.2 Extract and migrate `_is_safe_detail_key()` → `is_safe_detail_key()` with type hints and docstring
  - [ ] 1.3 Extract and migrate `_sanitize_detail_value()` → `sanitize_detail_value()` with type hints and docstring
  - [ ] 1.4 Extract and migrate `_sanitize_context()` → `sanitize_context()` with type hints and docstring
  - [ ] 1.5 Extract and migrate `sanitize_html_content()` with comprehensive docstring and security notes
  - [ ] 1.6 Extract and migrate `sanitize_text_content()` with comprehensive docstring
  - [ ] 1.7 Add `__all__` list to sanitization module
  - [ ] 1.8 Update `server/error_handlers/__init__.py` to import and export sanitization functions
  - [ ] 1.9 Run tests to verify new module imports correctly: `make test`

- [ ] 2. **Update Test Imports and Function Calls**
  - [ ] 2.1 Update imports in `server/tests/test_error_handlers.py` to use new sanitization module
  - [ ] 2.2 Update function calls to use new names (remove leading underscores)
  - [ ] 2.3 Search for additional imports: `grep -r "legacy_error_handlers" server/`
  - [ ] 2.4 Update any additional found imports to use new module structure
  - [ ] 2.5 Run full test suite to verify all tests pass: `make test`
  - [ ] 2.6 Verify test coverage remains ≥80%

- [ ] 3. **Remove Legacy Exception Handlers**
  - [ ] 3.1 Verify no usage of old exception handlers with grep searches
  - [ ] 3.2 Remove `mythos_exception_handler()` from legacy file
  - [ ] 3.3 Remove `general_exception_handler()` from legacy file
  - [ ] 3.4 Remove `logged_http_exception_handler()` from legacy file
  - [ ] 3.5 Remove `http_exception_handler()` from legacy file
  - [ ] 3.6 Remove `register_error_handlers()` function from legacy file
  - [ ] 3.7 Run tests to verify removal doesn't break anything: `make test`

- [ ] 4. **Remove ErrorResponse Class and Helpers**
  - [ ] 4.1 Search for `ErrorResponse(` usage in codebase to verify no external usage
  - [ ] 4.2 Remove `ErrorResponse` class from legacy file
  - [ ] 4.3 Remove `create_error_response()` function from legacy file
  - [ ] 4.4 Remove `_map_error_type()` function from legacy file
  - [ ] 4.5 Remove `_get_severity_for_error()` function from legacy file
  - [ ] 4.6 Remove `_get_status_code_for_error()` function from legacy file
  - [ ] 4.7 Run full test suite: `make test`
  - [ ] 4.8 Verify test coverage remains ≥80%

- [ ] 5. **Delete Legacy File and Final Verification**
  - [ ] 5.1 Verify no remaining imports from legacy file: `grep -r "legacy_error_handlers" server/`
  - [ ] 5.2 Delete `server/legacy_error_handlers.py` file
  - [ ] 5.3 Run full test suite: `make test`
  - [ ] 5.4 Run linting: `make lint`
  - [ ] 5.5 Start development server to verify no import errors
  - [ ] 5.6 Manually test error conditions to verify error handling works correctly
  - [ ] 5.7 Update `server/error_handlers/__init__.py` docstring to remove legacy migration note
  - [ ] 5.8 Document migration completion date in module docstring
