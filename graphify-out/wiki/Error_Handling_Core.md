# Error Handling Core

> 309 nodes

## Key Concepts

- **exceptions.py** (243 connections) — `server/exceptions.py`
- **MythosMUDError** (88 connections) — `server/exceptions.py`
- **RateLimitError** (76 connections) — `server/exceptions.py`
- **AuthenticationError** (63 connections) — `server/exceptions.py`
- **ErrorContext** (54 connections) — `server/exceptions.py`
- **ErrorType** (48 connections) — `server/error_types.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorMessages** (47 connections) — `server/error_types.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **CircuitBreaker** (38 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (37 connections) — `server/legacy_error_handlers.py`
- **ResourceNotFoundError** (36 connections) — `server/exceptions.py`
- **create_error_context()** (36 connections) — `server/exceptions.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **standardized_responses.py** (33 connections) — `server/error_handlers/standardized_responses.py`
- **ConfigurationError** (32 connections) — `server/exceptions.py`
- **JSONResponse** (31 connections) — `docs/examples/logging/fastapi_integration.py`
- **GameLogicError** (31 connections) — `server/exceptions.py`
- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ErrorSeverity** (30 connections) — `server/error_types.py`
- **TestErrorHandlers** (27 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestCircuitBreaker** (22 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 284 more nodes in this community*

## Relationships

- [handler realtime nats](handler_realtime_nats.md) (79 shared connections)
- [command inventory models](command_inventory_models.md) (45 shared connections)
- [Exception Containers](Exception_Containers.md) (44 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (43 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (41 shared connections)
- [models npc rationale](models_npc_rationale.md) (36 shared connections)
- [package argon2 engines](package_argon2_engines.md) (23 shared connections)
- [spell game magic](spell_game_magic.md) (20 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (17 shared connections)
- [add used user](add_used_user.md) (16 shared connections)
- [middleware error handling](middleware_error_handling.md) (13 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (13 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 1632 (72%)
- INFERRED: 620 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*