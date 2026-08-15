# MythosMUDError

> 326 nodes

## Key Concepts

- **MythosMUDError** (66 connections) — `server/exceptions.py`
- **ErrorType** (65 connections) — `server/error_types.py`
- **RateLimitError** (49 connections) — `server/exceptions.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **AuthenticationError** (46 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (44 connections) — `server/legacy_error_handlers.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **ErrorMessages** (35 connections) — `server/error_types.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **standardized_responses.py** (33 connections) — `server/error_handlers/standardized_responses.py`
- **test_websocket_handler_helpers_extended.py** (33 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **TestErrorMapping** (32 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **create_websocket_error_response()** (31 connections) — `server/error_types.py`
- **test_standardized_responses.py** (29 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **create_standard_error_response()** (26 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_map_error_type()** (23 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (22 connections) — `server/exceptions.py`
- **ResourceNotFoundError** (21 connections) — `server/exceptions.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **JSONResponse** (20 connections) — `docs/examples/logging/fastapi_integration.py`
- **asyncio** (20 connections)
- **ErrorSeverity** (19 connections) — `server/error_types.py`
- **_get_status_code_for_error()** (19 connections) — `server/legacy_error_handlers.py`
- *... and 301 more nodes in this community*

## Relationships

- [ErrorContext](ErrorContext.md) (39 shared connections)
- [DatabaseError](DatabaseError.md) (35 shared connections)
- [PydanticErrorHandler](PydanticErrorHandler.md) (31 shared connections)
- [ValidationError](ValidationError.md) (26 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (20 shared connections)
- [TestErrorHandlers](TestErrorHandlers.md) (17 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (17 shared connections)
- [legacy_error_sanitization.py](legacy_error_sanitization.py.md) (12 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (11 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (11 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (10 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (9 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/auth/argon2_utils.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- `server/tests/unit/test_error_types.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 850 (81%)
- INFERRED: 204 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*