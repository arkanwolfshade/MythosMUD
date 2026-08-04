# Error Handling Core

> 313 nodes

## Key Concepts

- **MythosMUDError** (88 connections) — `server/exceptions.py`
- **ErrorType** (48 connections) — `server/error_types.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorMessages** (47 connections) — `server/error_types.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **CircuitBreaker** (38 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (37 connections) — `server/legacy_error_handlers.py`
- **ResourceNotFoundError** (36 connections) — `server/exceptions.py`
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
- **TestErrorHandlers** (27 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **TestCircuitBreaker** (22 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Request** (21 connections)
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- *... and 288 more nodes in this community*

## Relationships

- [Spell Validation](Spell_Validation.md) (59 shared connections)
- [Loot Generation](Loot_Generation.md) (50 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (43 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (43 shared connections)
- [Exception Containers](Exception_Containers.md) (36 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (30 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (30 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (28 shared connections)
- [game weapon player](game_weapon_player.md) (19 shared connections)
- [middleware error handling](middleware_error_handling.md) (11 shared connections)
- [room websocket updates](room_websocket_updates.md) (10 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 1362 (72%)
- INFERRED: 521 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*