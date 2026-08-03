# Error Handling Core

> 586 nodes

## Key Concepts

- **MythosMUDError** (79 connections) — `server/exceptions.py`
- **RateLimitError** (76 connections) — `server/exceptions.py`
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
- *... and 561 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (90 shared connections)
- [command inventory factories](command_inventory_factories.md) (80 shared connections)
- [npc populate databases](npc_populate_databases.md) (32 shared connections)
- [auth rationale access](auth_rationale_access.md) (20 shared connections)
- [Loot Generation](Loot_Generation.md) (19 shared connections)
- [auth users rationale](auth_users_rationale.md) (16 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (15 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (12 shared connections)
- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [System Metrics](System_Metrics.md) (8 shared connections)
- [app factory rationale](app_factory_rationale.md) (7 shared connections)
- [character creation validate](character_creation_validate.md) (6 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`
- `server/tests/unit/test_error_types.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`
- `server/tests/unit/utils/test_rate_limiter_utils.py`
- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 2398 (78%)
- INFERRED: 657 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*