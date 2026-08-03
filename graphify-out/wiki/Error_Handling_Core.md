# Error Handling Core

> 564 nodes

## Key Concepts

- **MythosMUDError** (79 connections) — `server/exceptions.py`
- **AuthenticationError** (63 connections) — `server/exceptions.py`
- **ErrorContext** (54 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorType** (47 connections) — `server/error_types.py`
- **ErrorMessages** (47 connections) — `server/error_types.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **CircuitBreaker** (38 connections) — `server/legacy_error_handlers.py`
- **error_types.py** (37 connections) — `server/error_types.py`
- **NetworkError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (37 connections) — `server/legacy_error_handlers.py`
- **StandardizedErrorResponse** (35 connections) — `server/error_handlers/standardized_responses.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ResourceNotFoundError** (34 connections) — `server/exceptions.py`
- **create_error_context()** (33 connections) — `server/exceptions.py`
- **standardized_responses.py** (32 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **ConfigurationError** (32 connections) — `server/exceptions.py`
- **GameLogicError** (31 connections) — `server/exceptions.py`
- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **JSONResponse** (30 connections) — `docs/examples/logging/fastapi_integration.py`
- **ErrorSeverity** (30 connections) — `server/error_types.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- *... and 539 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (60 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (46 shared connections)
- [command inventory models](command_inventory_models.md) (43 shared connections)
- [Exception Containers](Exception_Containers.md) (41 shared connections)
- [command inventory factories](command_inventory_factories.md) (29 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (19 shared connections)
- [auth rationale access](auth_rationale_access.md) (19 shared connections)
- [combat services messaging](combat_services_messaging.md) (11 shared connections)
- [middleware error handling](middleware_error_handling.md) (9 shared connections)
- [auth users rationale](auth_users_rationale.md) (8 shared connections)
- [room look commands](room_look_commands.md) (5 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (5 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/realtime/message_handler_factory.py`
- `server/realtime/websocket_handler_validation.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/test_error_types.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 2353 (80%)
- INFERRED: 600 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*