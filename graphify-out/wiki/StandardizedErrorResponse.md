# StandardizedErrorResponse

> 82 nodes

## Key Concepts

- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **JSONResponse** (15 connections) — `docs/examples/logging/fastapi_integration.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **create_standardized_error_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._create_fallback_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **._create_error_details()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._determine_error_type_from_exception()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_user_id_from_state()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._generate_user_friendly_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._get_logged_http_user_friendly_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._map_status_code_to_error_type()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_exception_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_http_detail()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **test_handle_mythos_error_response()** (5 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **Request** (5 connections)
- *... and 57 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (24 shared connections)
- [ErrorType](ErrorType.md) (21 shared connections)
- [PydanticErrorHandler](PydanticErrorHandler.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (3 shared connections)
- [._handle_exception](_handle_exception.md) (2 shared connections)
- [error_handling_middleware.py](error_handling_middleware.py.md) (2 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [HealthStatus](HealthStatus.md) (1 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `server/error_handlers/standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`

## Audit Trail

- EXTRACTED: 197 (93%)
- INFERRED: 14 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*