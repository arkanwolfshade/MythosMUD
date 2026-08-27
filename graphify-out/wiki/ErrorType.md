# ErrorType

> 198 nodes

## Key Concepts

- **ErrorType** (52 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **error_types.py** (35 connections) — `server/error_types.py`
- **standardized_responses.py** (34 connections) — `server/error_handlers/standardized_responses.py`
- **ErrorMessages** (32 connections) — `server/error_types.py`
- **create_websocket_error_response()** (30 connections) — `server/error_types.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **create_standard_error_response()** (22 connections) — `server/error_types.py`
- **test_error_types.py** (18 connections) — `server/tests/unit/test_error_types.py`
- **JSONResponse** (15 connections) — `docs/examples/logging/fastapi_integration.py`
- **test_standardized_responses_security.py** (13 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_validation_error()** (12 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorSeverity** (10 connections) — `server/error_types.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **test_websocket_handler_error_handling.py** (10 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorContextInitKwargs** (8 connections) — `server/exceptions.py`
- *... and 173 more nodes in this community*

## Relationships

- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (17 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (11 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [ValidationError](ValidationError.md) (9 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (7 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [MythosMUDError](MythosMUDError.md) (7 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (6 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (6 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (6 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (5 shared connections)
- [test_player_requests.py](test_player_requests.py.md) (5 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 495 (91%)
- INFERRED: 50 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*