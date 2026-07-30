# . init ()

> 401 nodes

## Key Concepts

- **MythosMUDError** (79 connections) — `server/exceptions.py`
- **RateLimitError** (76 connections) — `server/exceptions.py`
- **ErrorContext** (54 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorType** (47 connections) — `server/error_types.py`
- **ErrorMessages** (47 connections) — `server/error_types.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **CircuitBreaker** (38 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (37 connections) — `server/legacy_error_handlers.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ResourceNotFoundError** (34 connections) — `server/exceptions.py`
- **create_error_context()** (33 connections) — `server/exceptions.py`
- **standardized_responses.py** (32 connections) — `server/error_handlers/standardized_responses.py`
- **ConfigurationError** (32 connections) — `server/exceptions.py`
- **GameLogicError** (31 connections) — `server/exceptions.py`
- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **JSONResponse** (30 connections) — `docs/examples/logging/fastapi_integration.py`
- **ErrorSeverity** (30 connections) — `server/error_types.py`
- **TestErrorHandlers** (27 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **LoggedException** (23 connections) — `server/exceptions.py`
- **TestCircuitBreaker** (22 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Request** (21 connections)
- *... and 376 more nodes in this community*

## Relationships

- [convert pydantic error()](convert_pydantic_error%28%29.md) (76 shared connections)
- [real time](real_time.md) (60 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (49 shared connections)
- [.initialize()](initialize%28%29.md) (40 shared connections)
- [create access token()](create_access_token%28%29.md) (31 shared connections)
- [BaseCommand](BaseCommand.md) (26 shared connections)
- [world](world.md) (14 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (10 shared connections)
- [. init ()](_init_%28%29.md) (7 shared connections)
- [Core character statistics with Lovecraftian](Core_character_statistics_with_Lovecraftian.md) (7 shared connections)
- [Response](Response.md) (6 shared connections)
- [.reset instance()](reset_instance%28%29.md) (6 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/player_helpers.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/middleware/error_handling_middleware.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 1639 (74%)
- INFERRED: 587 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*