# handler realtime nats

> 142 nodes

## Key Concepts

- **ErrorType** (48 connections) — `server/error_types.py`
- **ErrorMessages** (47 connections) — `server/error_types.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **standardized_responses.py** (33 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **ErrorSeverity** (30 connections) — `server/error_types.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **PydanticErrorHandler** (23 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **_AppWithLegacyConfigState** (20 connections) — `server/legacy_error_handlers.py`
- **_AppStateWithLegacyConfig** (19 connections) — `server/legacy_error_handlers.py`
- **ErrorResponseDetailsInput** (18 connections)
- **create_sse_error_response()** (17 connections) — `server/error_types.py`
- **Exception** (17 connections)
- **HTTPException** (17 connections)
- **_CircuitBreakerResult** (17 connections)
- **HttpStandardErrorResponse** (16 connections) — `server/error_types.py`
- **.handle_validation_error()** (14 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorResponseDetailsInput** (14 connections)
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **handle_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- *... and 117 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (99 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (45 shared connections)
- [Exception Containers](Exception_Containers.md) (24 shared connections)
- [command commands aliases](command_commands_aliases.md) (18 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (14 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (10 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (9 shared connections)
- [add used user](add_used_user.md) (8 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (7 shared connections)
- [realtime message validator](realtime_message_validator.md) (6 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 662 (79%)
- INFERRED: 181 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*