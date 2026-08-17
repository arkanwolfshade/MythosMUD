# StandardizedErrorResponse

> 61 nodes

## Key Concepts

- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **ErrorContextInitKwargs** (8 connections) — `server/exceptions.py`
- **convert_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **handle_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **.create_handler()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **create_standardized_error_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._create_error_details()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_user_id_from_state()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_exception_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **test_handle_mythos_error_response()** (5 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **Request** (5 connections)
- **_SampleModel** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **_contains_file_path_in_exception()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **_contains_sensitive_exception_pattern()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_request_metadata()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **.__init__()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **_response_message()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.test_pydantic_validation_error_does_not_expose_str_error_in_message()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **test_determine_error_type_from_exception_uses_attr()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **test_handle_logged_http_exception()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- *... and 36 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (37 shared connections)
- [DatabaseError](DatabaseError.md) (20 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [test_command_service.py](test_command_service.py.md) (1 shared connections)
- [JSONResponse](JSONResponse.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/exceptions.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`

## Audit Trail

- EXTRACTED: 148 (87%)
- INFERRED: 22 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*