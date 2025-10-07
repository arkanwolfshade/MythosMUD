# Error Handlers Namespace Resolution

## Problem

During the Pydantic audit, we created a new `server/error_handlers/` package with modular error handlers. However, this created a namespace conflict with the existing `server/error_handlers.py` module. When tests tried to `from server.error_handlers import ...`, Python would prioritize the package over the module, causing import errors.

## Solution

Renamed `server/error_handlers.py` to `server/legacy_error_handlers.py` to eliminate the namespace conflict.

## Changes Made

### Files Renamed

- `server/error_handlers.py` → `server/legacy_error_handlers.py`

### Files Updated

1. **server/tests/test_error_handlers.py**
   - Updated import: `from server.legacy_error_handlers import ...`
   - Fixed test expectations for Pydantic ValidationError status codes (422 instead of 400)
   - Updated to import `register_error_handlers` from `server.middleware.error_handling_middleware`

2. **server/error_handlers/**init**.py**
   - Updated documentation to clarify the relationship between the new package and legacy module
   - Documented proper import patterns for both new and legacy code

3. **server/error_handlers/standardized_responses.py**
   - Fixed import: Changed `from ..error_handlers.pydantic_error_handler import` to `from .pydantic_error_handler import`

## Import Patterns

### For New Code (Recommended)

```python
from server.error_handlers import PydanticErrorHandler, StandardizedErrorResponse
from server.middleware.error_handling_middleware import setup_error_handling
```

### For Legacy Code

```python
from server.legacy_error_handlers import (
    create_error_response,
    sanitize_html_content,
    sanitize_text_content,
    _is_safe_detail_key,
    _sanitize_context,
    _sanitize_detail_value,
)
```

## Test Results

All 20 tests in `server/tests/test_error_handlers.py` now pass:

- 19 sanitization and error response tests
- 1 error handler integration test

## Future Work

The legacy `server/legacy_error_handlers.py` module should be gradually refactored to use the new modular error handling infrastructure in `server/error_handlers/`.
