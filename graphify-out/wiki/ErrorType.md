# ErrorType

> 223 nodes

## Key Concepts

- **ErrorType** (65 connections) — `server/error_types.py`
- **legacy_error_handlers.py** (44 connections) — `server/legacy_error_handlers.py`
- **test_legacy_error_handlers.py** (43 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **ErrorMessages** (35 connections) — `server/error_types.py`
- **standardized_responses.py** (35 connections) — `server/error_handlers/standardized_responses.py`
- **test_websocket_handler_helpers_extended.py** (34 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **TestErrorMapping** (32 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **create_websocket_error_response()** (31 connections) — `server/error_types.py`
- **create_standard_error_response()** (26 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (26 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_map_error_type()** (23 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (22 connections) — `server/exceptions.py`
- **ResourceNotFoundError** (21 connections) — `server/exceptions.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **asyncio** (20 connections)
- **ErrorSeverity** (19 connections) — `server/error_types.py`
- **_get_status_code_for_error()** (19 connections) — `server/legacy_error_handlers.py`
- **_get_severity_for_error()** (18 connections) — `server/legacy_error_handlers.py`
- **ConfigurationError** (17 connections) — `server/exceptions.py`
- **logged_http_exception_handler()** (17 connections) — `server/legacy_error_handlers.py`
- **GameLogicError** (16 connections) — `server/exceptions.py`
- **ErrorResponse** (16 connections) — `server/legacy_error_handlers.py`
- **create_sse_error_response()** (16 connections) — `server/error_types.py`
- **create_error_response()** (15 connections) — `server/legacy_error_handlers.py`
- *... and 198 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (47 shared connections)
- [MythosMUDError](MythosMUDError.md) (47 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (41 shared connections)
- [TestErrorHandlers](TestErrorHandlers.md) (22 shared connections)
- [PydanticErrorHandler](PydanticErrorHandler.md) (17 shared connections)
- [ValidationError](ValidationError.md) (17 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (12 shared connections)
- [legacy_error_sanitization.py](legacy_error_sanitization.py.md) (12 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (11 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (9 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (7 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (6 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- `server/tests/unit/test_error_types.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 615 (84%)
- INFERRED: 113 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*