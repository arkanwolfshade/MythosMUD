# StandardizedErrorResponse

> 100 nodes

## Key Concepts

- **StandardizedErrorResponse** (35 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (31 connections) — `server/error_types.py`
- **create_standard_error_response()** (26 connections) — `server/error_types.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **JSONResponse** (20 connections) — `docs/examples/logging/fastapi_integration.py`
- **create_sse_error_response()** (16 connections) — `server/error_types.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **_SampleModel** (7 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **handle_api_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **_normalize_error_response_details()** (7 connections) — `server/error_types.py`
- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **create_standardized_error_response()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._get_logged_http_user_friendly_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._map_status_code_to_error_type()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_exception_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- *... and 75 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (56 shared connections)
- [PydanticErrorHandler](PydanticErrorHandler.md) (15 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (6 shared connections)
- [error_handling_middleware.py](error_handling_middleware.py.md) (4 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (4 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (3 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (2 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (2 shared connections)
- [message_handler_factory.py](message_handler_factory.py.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 256 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*