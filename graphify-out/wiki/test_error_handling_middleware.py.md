# test_error_handling_middleware.py

> 46 nodes

## Key Concepts

- **test_error_handling_middleware.py** (28 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **error_handling_middleware.py** (19 connections) — `server/middleware/error_handling_middleware.py`
- **ErrorHandlingMiddleware** (17 connections) — `server/middleware/error_handling_middleware.py`
- **register_error_handlers()** (11 connections) — `server/middleware/error_handling_middleware.py`
- **setup_error_handling()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **_http_scope()** (8 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **add_error_handling_middleware()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **request_id_from_scope()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **test_registered_exception_handlers_return_json()** (6 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **server/middleware/__init__.py** (6 connections) — `server/middleware/__init__.py`
- **asyncio** (6 connections)
- **extract_user_id_from_non_mapping()** (5 connections) — `server/middleware/error_handling_middleware.py`
- **_error_log_kwargs()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_levels_and_session()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_add_register_setup_error_handling()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_call_handles_exception()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_call_sets_request_id_and_success()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_dispatch_success_and_exception()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_handle_exception_fallback_when_handler_fails()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_request_id_from_scope()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **FastAPI** (4 connections)
- **_UserObjectWithId** (3 connections) — `server/middleware/error_handling_middleware.py`
- **_UserWithId** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **.__init__()** (3 connections) — `server/middleware/error_handling_middleware.py`
- **test_call_passes_through_non_http()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- *... and 21 more nodes in this community*

## Relationships

- [MythosMUDError](MythosMUDError.md) (9 shared connections)
- [._handle_exception](_handle_exception.md) (7 shared connections)
- [factory.py](factory.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)
- [_UserWithGet](_UserWithGet.md) (1 shared connections)

## Source Files

- `server/middleware/__init__.py`
- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 105 (88%)
- INFERRED: 14 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*