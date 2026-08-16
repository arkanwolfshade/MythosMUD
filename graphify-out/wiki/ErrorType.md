# ErrorType

> 92 nodes

## Key Concepts

- **ErrorType** (65 connections) — `server/error_types.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **create_websocket_error_response()** (31 connections) — `server/error_types.py`
- **create_standard_error_response()** (26 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (26 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **JSONResponse** (20 connections) — `docs/examples/logging/fastapi_integration.py`
- **create_sse_error_response()** (16 connections) — `server/error_types.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **HttpStandardErrorResponse** (7 connections) — `server/error_types.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **_normalize_error_response_details()** (7 connections) — `server/error_types.py`
- **ErrorResponseDetails** (6 connections) — `server/error_types.py`
- **TypedDict** (6 connections)
- **RealtimeErrorResponse** (5 connections) — `server/error_types.py`
- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **._determine_error_type_from_exception()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._generate_user_friendly_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._get_logged_http_user_friendly_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._map_status_code_to_error_type()** (5 connections) — `server/error_handlers/standardized_responses.py`
- *... and 67 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (37 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (34 shared connections)
- [PydanticErrorHandler](PydanticErrorHandler.md) (15 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (11 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (11 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (7 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (6 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (5 shared connections)
- [message_handler_factory.py](message_handler_factory.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (3 shared connections)
- [test_websocket_handler_error_handling.py](test_websocket_handler_error_handling.py.md) (3 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 278 (86%)
- INFERRED: 45 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*