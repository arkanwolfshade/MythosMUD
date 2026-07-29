# . init ()

> 563 nodes

## Key Concepts

- **ValidationError** (524 connections) — `server/exceptions.py`
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
- *... and 538 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (161 shared connections)
- [APIRouter](APIRouter.md) (113 shared connections)
- [Connection Manager](Connection_Manager.md) (36 shared connections)
- [test command factories inventory](test_command_factories_inventory.md) (30 shared connections)
- [convert pydantic error()](convert_pydantic_error%28%29.md) (29 shared connections)
- [character creation](character_creation.md) (27 shared connections)
- [.initialize()](initialize%28%29.md) (27 shared connections)
- [.validate search term()](validate_search_term%28%29.md) (24 shared connections)
- [close db()](close_db%28%29.md) (21 shared connections)
- [. init ()](_init_%28%29.md) (21 shared connections)
- [test command factories utility](test_command_factories_utility.md) (18 shared connections)
- [.validate message()](validate_message%28%29.md) (17 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/database.py`
- `server/database_helpers.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/game/emote_service.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/npc/combat_integration.py`
- `server/persistence/container_persistence.py`
- `server/persistence/container_persistence_async.py`
- `server/realtime/websocket_handler_validation.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 2418 (70%)
- INFERRED: 1021 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*