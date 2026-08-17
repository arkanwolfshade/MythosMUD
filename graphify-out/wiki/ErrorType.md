# ErrorType

> 203 nodes

## Key Concepts

- **ErrorType** (65 connections) — `server/error_types.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **ErrorMessages** (35 connections) — `server/error_types.py`
- **test_websocket_handler_helpers_extended.py** (34 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **create_websocket_error_response()** (31 connections) — `server/error_types.py`
- **create_standard_error_response()** (26 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (26 connections) — `server/error_handlers/pydantic_error_handler.py`
- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **websocket_handler_validation.py** (22 connections) — `server/realtime/websocket_handler_validation.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **asyncio** (20 connections)
- **create_sse_error_response()** (16 connections) — `server/error_types.py`
- **.handle_validation_error()** (13 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_standardized_responses_security.py** (13 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **test_websocket_handler_error_handling.py** (10 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **HttpStandardErrorResponse** (7 connections) — `server/error_types.py`
- **.convert_to_mythos_error()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- *... and 178 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (39 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (37 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (16 shared connections)
- [JSONResponse](JSONResponse.md) (14 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (7 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (7 shared connections)
- [User](User.md) (6 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (6 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (5 shared connections)
- [players/__init__.py](players-__init__.py.md) (5 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/legacy_error_handlers.py`
- `server/realtime/websocket_handler_validation.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 480 (88%)
- INFERRED: 63 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*