# StandardizedErrorResponse

> 72 nodes

## Key Concepts

- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **JSONResponse** (20 connections) — `docs/examples/logging/fastapi_integration.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **create_standardized_error_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **._create_error_details()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_user_id_from_state()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_exception_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_http_detail()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **test_handle_mythos_error_response()** (5 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **Request** (5 connections)
- **_SampleModel** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **_contains_file_path_in_exception()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **_contains_sensitive_exception_pattern()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_request_metadata()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **.__init__()** (4 connections) — `server/error_handlers/standardized_responses.py`
- *... and 47 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (34 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [PydanticErrorHandler](PydanticErrorHandler.md) (7 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (4 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (3 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [TestLegacyHandlerSecurity](TestLegacyHandlerSecurity.md) (1 shared connections)
- [HealthStatus](HealthStatus.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`

## Audit Trail

- EXTRACTED: 173 (86%)
- INFERRED: 27 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*