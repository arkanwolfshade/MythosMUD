# Error Handling Middleware

> 52 nodes · cohesion 0.06

## Key Concepts

- **error_handling_middleware.py** (18 connections) — `server/middleware/error_handling_middleware.py`
- **ErrorHandlingMiddleware** (15 connections) — `server/middleware/error_handling_middleware.py`
- **test_error_handling_middleware.py** (12 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **._handle_exception()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **setup_error_handling()** (8 connections) — `server/middleware/error_handling_middleware.py`
- **.log_exception()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **request_id_from_scope()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **.__call__()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.dispatch()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **register_error_handlers()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **__init__.py** (6 connections) — `server/middleware/__init__.py`
- **add_error_handling_middleware()** (5 connections) — `server/middleware/error_handling_middleware.py`
- **extract_user_id_from_non_mapping()** (5 connections) — `server/middleware/error_handling_middleware.py`
- **_error_log_kwargs()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_adds_user_id_for_mapping_user()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **_UserWithGet** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **FastAPI** (4 connections) — `server/middleware/error_handling_middleware.py`
- **.__init__()** (3 connections) — `server/middleware/error_handling_middleware.py`
- **_UserObjectWithId** (3 connections) — `server/middleware/error_handling_middleware.py`
- **test_log_exception_mapping_user_missing_id_sets_none()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_request_id_from_scope()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **_UserWithId** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Scope** (3 connections) — `server/middleware/error_handling_middleware.py`
- **test_extract_user_id_from_non_mapping()** (2 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_request_id_from_scope_non_str_coerced()** (2 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- *... and 27 more nodes in this community*

## Relationships

- [[Pydantic Error Handlers]] (4 shared connections)
- [[FastAPI App Factory]] (3 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Standardized Error Responses]] (2 shared connections)
- [[Container Exception Handlers]] (1 shared connections)
- [[Player Combat XP]] (1 shared connections)

## Source Files

- `server/middleware/__init__.py`
- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 176 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
