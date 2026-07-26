# error_handling_middleware.py

> 53 nodes · cohesion 0.06

## Key Concepts

- **error_handling_middleware.py** (19 connections) — `server/middleware/error_handling_middleware.py`
- **ErrorHandlingMiddleware** (14 connections) — `server/middleware/error_handling_middleware.py`
- **test_error_handling_middleware.py** (13 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **register_error_handlers()** (11 connections) — `server/middleware/error_handling_middleware.py`
- **._handle_exception()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **setup_error_handling()** (8 connections) — `server/middleware/error_handling_middleware.py`
- **.log_exception()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **request_id_from_scope()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **add_error_handling_middleware()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.__call__()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.dispatch()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **extract_user_id_from_non_mapping()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **__init__.py** (6 connections) — `server/middleware/__init__.py`
- **_error_log_kwargs()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **FastAPI** (4 connections)
- **_UserObjectWithId** (4 connections) — `server/middleware/error_handling_middleware.py`
- **test_log_exception_adds_user_id_for_mapping_user()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **_UserWithGet** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **.__init__()** (3 connections) — `server/middleware/error_handling_middleware.py`
- **Scope** (3 connections)
- **test_log_exception_mapping_user_missing_id_sets_none()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_request_id_from_scope()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **_UserWithId** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Exception** (2 connections)
- **Receive** (2 connections)
- *... and 28 more nodes in this community*

## Relationships

- [error_types.py](error_types.py.md) (5 shared connections)
- [MythosMUDError](MythosMUDError.md) (4 shared connections)
- [factory.py](factory.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [exceptions.py](exceptions.py.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [test_command_factories_utility.py](test_command_factories_utility.py.md) (1 shared connections)

## Source Files

- `server/middleware/__init__.py`
- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 179 (93%)
- INFERRED: 14 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*