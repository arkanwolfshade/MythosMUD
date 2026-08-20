# TestErrorHandlers

> 38 nodes

## Key Concepts

- **TestErrorHandlers** (16 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **asyncio** (13 connections)
- **general_exception_handler()** (12 connections) — `server/legacy_error_handlers.py`
- **mythos_exception_handler()** (12 connections) — `server/legacy_error_handlers.py`
- **TestLegacyHandlerSecurity** (6 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_mythos_exception_handler_sets_request_id()** (6 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_include_error_details_from_request()** (5 connections) — `server/legacy_error_handlers.py`
- **.test_logged_http_exception_handler_401()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_logged_http_exception_handler_404()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_logged_http_exception_handler_422()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_logged_http_exception_handler_429()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_mythos_exception_handler()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_mythos_exception_handler_with_debug()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_logged_http_exception_does_not_expose_raw_detail()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Request** (5 connections)
- **.test_general_exception_handler()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_http_exception_handler_401()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_http_exception_handler_starlette()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_register_error_handlers()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **._response_message()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_http_exception_does_not_expose_raw_detail()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Exception** (1 connections)
- **Handle MythosMUD-specific exceptions. Args: request: FastAPI request object…** (1 connections) — `server/legacy_error_handlers.py`
- **Handle all other exceptions. Args: request: FastAPI request object exc: Generic…** (1 connections) — `server/legacy_error_handlers.py`
- **Safely read the debug flag from app.state.config; defaults to False.** (1 connections) — `server/legacy_error_handlers.py`
- *... and 13 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (22 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [MythosMUDError](MythosMUDError.md) (5 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (3 shared connections)

## Source Files

- `server/legacy_error_handlers.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 89 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*