# Error Handling Core

> 518 nodes

## Key Concepts

- **MythosMUDError** (88 connections) — `server/exceptions.py`
- **RateLimitError** (76 connections) — `server/exceptions.py`
- **AuthenticationError** (63 connections) — `server/exceptions.py`
- **ErrorContext** (54 connections) — `server/exceptions.py`
- **ErrorType** (48 connections) — `server/error_types.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorMessages** (47 connections) — `server/error_types.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **CircuitBreaker** (38 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (37 connections) — `server/legacy_error_handlers.py`
- **ResourceNotFoundError** (36 connections) — `server/exceptions.py`
- **create_error_context()** (36 connections) — `server/exceptions.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **standardized_responses.py** (33 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **ConfigurationError** (32 connections) — `server/exceptions.py`
- **JSONResponse** (31 connections) — `docs/examples/logging/fastapi_integration.py`
- **GameLogicError** (31 connections) — `server/exceptions.py`
- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ErrorSeverity** (30 connections) — `server/error_types.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- *... and 493 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (88 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (53 shared connections)
- [command inventory factories](command_inventory_factories.md) (49 shared connections)
- [command inventory models](command_inventory_models.md) (40 shared connections)
- [Database Config](Database_Config.md) (33 shared connections)
- [models npc rationale](models_npc_rationale.md) (21 shared connections)
- [room look commands](room_look_commands.md) (18 shared connections)
- [middleware error handling](middleware_error_handling.md) (11 shared connections)
- [game models stats](game_models_stats.md) (10 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (10 shared connections)
- [auth rationale access](auth_rationale_access.md) (9 shared connections)
- [auth users rationale](auth_users_rationale.md) (6 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/realtime/websocket_handler_validation.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/test_error_types.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 2193 (78%)
- INFERRED: 630 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*