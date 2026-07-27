# MythosMUDError

> 174 nodes · cohesion 0.03

## Key Concepts

- **MythosMUDError** (79 connections) — `server/exceptions.py`
- **RateLimitError** (76 connections) — `server/exceptions.py`
- **AuthenticationError** (63 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorMessages** (47 connections) — `server/error_types.py`
- **ErrorType** (47 connections) — `server/error_types.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **CircuitBreaker** (38 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (37 connections) — `server/legacy_error_handlers.py`
- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ResourceNotFoundError** (34 connections) — `server/exceptions.py`
- **ConfigurationError** (32 connections) — `server/exceptions.py`
- **GameLogicError** (31 connections) — `server/exceptions.py`
- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ErrorSeverity** (30 connections) — `server/error_types.py`
- **TestErrorHandlers** (27 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestCircuitBreaker** (22 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Request** (21 connections)
- **_AppWithLegacyConfigState** (20 connections) — `server/legacy_error_handlers.py`
- **TestErrorResponse** (20 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_AppStateWithLegacyConfig** (19 connections) — `server/legacy_error_handlers.py`
- **TestCreateErrorResponse** (19 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestLegacyHandlerSecurity** (19 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ErrorResponseDetailsInput** (18 connections)
- *... and 149 more nodes in this community*

## Relationships

- [error_types.py](error_types.py.md) (67 shared connections)
- [ErrorContext](ErrorContext.md) (66 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (35 shared connections)
- [ContainerService](ContainerService.md) (35 shared connections)
- [sanitize_detail_value](sanitize_detail_value.md) (30 shared connections)
- [ValidationError](ValidationError.md) (29 shared connections)
- [DatabaseError](DatabaseError.md) (27 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (19 shared connections)
- [exceptions.py](exceptions.py.md) (11 shared connections)
- [.test_try_user_object_name_with_user](test_try_user_object_name_with_user.md) (9 shared connections)
- [.call](call.md) (6 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (5 shared connections)

## Source Files

- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 835 (59%)
- INFERRED: 589 (41%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*