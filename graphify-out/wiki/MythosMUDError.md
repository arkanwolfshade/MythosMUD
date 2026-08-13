# MythosMUDError

> 163 nodes

## Key Concepts

- **MythosMUDError** (68 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (44 connections) — `server/legacy_error_handlers.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **CircuitBreaker** (36 connections) — `server/legacy_error_handlers.py`
- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **AuthenticationError** (34 connections) — `server/exceptions.py`
- **ErrorResponse** (33 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (28 connections) — `server/exceptions.py`
- **ResourceNotFoundError** (27 connections) — `server/exceptions.py`
- **TestErrorHandlers** (27 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ConfigurationError** (25 connections) — `server/exceptions.py`
- **ErrorSeverity** (24 connections) — `server/error_types.py`
- **GameLogicError** (24 connections) — `server/exceptions.py`
- **TestCircuitBreaker** (22 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestErrorResponse** (20 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestCreateErrorResponse** (19 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestLegacyHandlerSecurity** (19 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestGracefulDegradation** (18 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_AppStateWithLegacyConfig** (17 connections) — `server/legacy_error_handlers.py`
- **_AppWithLegacyConfigState** (17 connections) — `server/legacy_error_handlers.py`
- **create_error_response()** (15 connections) — `server/legacy_error_handlers.py`
- **_map_error_type()** (15 connections) — `server/legacy_error_handlers.py`
- **logged_http_exception_handler()** (14 connections) — `server/legacy_error_handlers.py`
- **handle_exception()** (13 connections) — `server/exceptions.py`
- **asyncio** (13 connections)
- *... and 138 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (60 shared connections)
- [ErrorType](ErrorType.md) (48 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (42 shared connections)
- [TestSanitization](TestSanitization.md) (21 shared connections)
- [DatabaseError](DatabaseError.md) (18 shared connections)
- [ErrorContext](ErrorContext.md) (13 shared connections)
- [.call](call.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [graceful_degradation](graceful_degradation.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [error_handling_middleware.py](error_handling_middleware.py.md) (3 shared connections)
- [test_argon2_utils.py](test_argon2_utils.py.md) (2 shared connections)

## Source Files

- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 453 (73%)
- INFERRED: 170 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*