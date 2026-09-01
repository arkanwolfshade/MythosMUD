# ErrorType

> 123 nodes

## Key Concepts

- **ErrorType** (52 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **error_types.py** (35 connections) — `server/error_types.py`
- **create_websocket_error_response()** (30 connections) — `server/error_types.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **create_standard_error_response()** (22 connections) — `server/error_types.py`
- **test_error_types.py** (18 connections) — `server/tests/unit/test_error_types.py`
- **JSONResponse** (15 connections) — `docs/examples/logging/fastapi_integration.py`
- **ErrorSeverity** (10 connections) — `server/error_types.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **create_standardized_error_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._create_fallback_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **_normalize_error_response_details()** (6 connections) — `server/error_types.py`
- **TypedDict** (6 connections)
- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **._create_error_details()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._determine_error_type_from_exception()** (5 connections) — `server/error_handlers/standardized_responses.py`
- *... and 98 more nodes in this community*

## Relationships

- [pydantic_error_handler.py](pydantic_error_handler.py.md) (28 shared connections)
- [MythosMUDError](MythosMUDError.md) (21 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (14 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (11 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (7 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (5 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (5 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (3 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 324 (89%)
- INFERRED: 39 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*