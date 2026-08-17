# JSONResponse

> 51 nodes

## Key Concepts

- **JSONResponse** (20 connections) — `docs/examples/logging/fastapi_integration.py`
- **logged_http_exception_handler()** (17 connections) — `server/legacy_error_handlers.py`
- **TestErrorHandlers** (16 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **http_exception_handler()** (15 connections) — `server/legacy_error_handlers.py`
- **asyncio** (13 connections)
- **mythos_exception_handler()** (12 connections) — `server/legacy_error_handlers.py`
- **register_error_handlers()** (11 connections) — `server/legacy_error_handlers.py`
- **TestLegacyHandlerSecurity** (6 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_mythos_exception_handler_sets_request_id()** (6 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **_include_error_details_from_request()** (5 connections) — `server/legacy_error_handlers.py`
- **.test_logged_http_exception_handler_401()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_logged_http_exception_handler_404()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_logged_http_exception_handler_422()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_logged_http_exception_handler_429()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_mythos_exception_handler()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_mythos_exception_handler_with_debug()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_logged_http_exception_does_not_expose_raw_detail()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Request** (5 connections)
- **.to_response()** (4 connections) — `server/legacy_error_handlers.py`
- **.test_general_exception_handler()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_http_exception_handler_401()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_http_exception_handler_starlette()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_register_error_handlers()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **._response_message()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 26 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (25 shared connections)
- [ErrorType](ErrorType.md) (14 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [general_exception_handler](general_exception_handler.md) (2 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (1 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (1 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 119 (85%)
- INFERRED: 21 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*