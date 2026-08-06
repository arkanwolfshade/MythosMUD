# Error Handling Core

> 233 nodes

## Key Concepts

- **MythosMUDError** (88 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **CircuitBreaker** (38 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (37 connections) — `server/legacy_error_handlers.py`
- **ResourceNotFoundError** (36 connections) — `server/exceptions.py`
- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ConfigurationError** (32 connections) — `server/exceptions.py`
- **JSONResponse** (31 connections) — `docs/examples/logging/fastapi_integration.py`
- **GameLogicError** (31 connections) — `server/exceptions.py`
- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestErrorHandlers** (27 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestCircuitBreaker** (22 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Request** (21 connections)
- **TestErrorResponse** (20 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **sanitize_detail_value()** (19 connections) — `server/legacy_error_sanitization.py`
- **TestCreateErrorResponse** (19 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestLegacyHandlerSecurity** (19 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **FastAPI** (18 connections)
- **legacy_error_sanitization.py** (18 connections) — `server/legacy_error_sanitization.py`
- **TestGracefulDegradation** (18 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **create_error_response()** (17 connections) — `server/legacy_error_handlers.py`
- **_map_error_type()** (15 connections) — `server/legacy_error_handlers.py`
- **mythos_exception_handler()** (14 connections) — `server/legacy_error_handlers.py`
- *... and 208 more nodes in this community*

## Relationships

- [handler realtime nats](handler_realtime_nats.md) (99 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (54 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (33 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (32 shared connections)
- [add used user](add_used_user.md) (24 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (22 shared connections)
- [Exception Containers](Exception_Containers.md) (18 shared connections)
- [middleware error handling](middleware_error_handling.md) (10 shared connections)
- [commands communication support](commands_communication_support.md) (5 shared connections)
- [player game schema](player_game_schema.md) (4 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (3 shared connections)
- [task registry app](task_registry_app.md) (3 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/standardized_responses.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 955 (74%)
- INFERRED: 342 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*