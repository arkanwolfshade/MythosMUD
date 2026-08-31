# test_error_handling_middleware.py

> 28 nodes

## Key Concepts

- **test_error_handling_middleware.py** (30 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **ErrorHandlingMiddleware** (17 connections) — `server/middleware/error_handling_middleware.py`
- **_http_scope()** (8 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_registered_exception_handlers_return_json()** (6 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **asyncio** (6 connections)
- **extract_user_id_from_non_mapping()** (5 connections) — `server/middleware/error_handling_middleware.py`
- **_error_log_kwargs()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_levels_and_session()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_call_handles_exception()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_call_sets_request_id_and_success()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_dispatch_success_and_exception()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_handle_exception_fallback_when_handler_fails()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_request_id_from_scope()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **_UserWithId** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **.__init__()** (3 connections) — `server/middleware/error_handling_middleware.py`
- **test_call_passes_through_non_http()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_extract_user_id_from_non_mapping()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_adds_user_id_for_mapping_user()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_mapping_user_missing_id_sets_none()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **parametrize** (2 connections)
- **Scope** (2 connections)
- **.__init__()** (1 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **ASGIApp** (1 connections)
- **Read user id from a non-Mapping request.state.user (object with get and/or id).…** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Pure ASGI middleware to handle all exceptions across FastAPI endpoints. This…** (1 connections) — `server/middleware/error_handling_middleware.py`
- *... and 3 more nodes in this community*

## Relationships

- [error_handling_middleware.py](error_handling_middleware.py.md) (9 shared connections)
- [._handle_exception](_handle_exception.md) (8 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)
- [_UserWithGet](_UserWithGet.md) (1 shared connections)

## Source Files

- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 71 (90%)
- INFERRED: 8 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*