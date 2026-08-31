# ErrorType

> 275 nodes

## Key Concepts

- **ErrorType** (52 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **error_types.py** (35 connections) — `server/error_types.py`
- **standardized_responses.py** (34 connections) — `server/error_handlers/standardized_responses.py`
- **test_websocket_handler_helpers_extended.py** (34 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **ErrorMessages** (32 connections) — `server/error_types.py`
- **create_websocket_error_response()** (30 connections) — `server/error_types.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **create_standard_error_response()** (22 connections) — `server/error_types.py`
- **websocket_handler_validation.py** (22 connections) — `server/realtime/websocket_handler_validation.py`
- **asyncio** (20 connections)
- **test_error_types.py** (18 connections) — `server/tests/unit/test_error_types.py`
- **JSONResponse** (15 connections) — `docs/examples/logging/fastapi_integration.py`
- **ResourceNotFoundError** (13 connections) — `server/exceptions.py`
- **test_standardized_responses_security.py** (13 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_validation_error()** (12 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorSeverity** (10 connections) — `server/error_types.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **test_websocket_handler_error_handling.py** (10 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- *... and 250 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (37 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (30 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (19 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (8 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (7 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (7 shared connections)
- [players/__init__.py](players-__init__.py.md) (5 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (4 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (3 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (3 shared connections)
- [BaseCommand](BaseCommand.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_handler_validation.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- `server/tests/unit/test_error_types.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 622 (92%)
- INFERRED: 56 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*