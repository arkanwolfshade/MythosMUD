# Error Handling Core

> 217 nodes

## Key Concepts

- **MythosMUDError** (88 connections) — `server/exceptions.py`
- **AuthenticationError** (63 connections) — `server/exceptions.py`
- **ErrorType** (48 connections) — `server/error_types.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorMessages** (47 connections) — `server/error_types.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **CircuitBreaker** (38 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (37 connections) — `server/legacy_error_handlers.py`
- **ResourceNotFoundError** (36 connections) — `server/exceptions.py`
- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **standardized_responses.py** (33 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **ConfigurationError** (32 connections) — `server/exceptions.py`
- **GameLogicError** (31 connections) — `server/exceptions.py`
- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ErrorSeverity** (30 connections) — `server/error_types.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- **TestErrorHandlers** (27 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **TestCircuitBreaker** (22 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Request** (21 connections)
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **_AppWithLegacyConfigState** (20 connections) — `server/legacy_error_handlers.py`
- *... and 192 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (68 shared connections)
- [Spell Validation](Spell_Validation.md) (66 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (63 shared connections)
- [Loot Generation](Loot_Generation.md) (32 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (30 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (28 shared connections)
- [Database Config](Database_Config.md) (27 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (19 shared connections)
- [game weapon player](game_weapon_player.md) (18 shared connections)
- [middleware error handling](middleware_error_handling.md) (10 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (10 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (6 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/test_error_types.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 1096 (67%)
- INFERRED: 538 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*