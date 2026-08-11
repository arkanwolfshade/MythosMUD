# Error Handling Middleware

> 42 nodes

## Key Concepts

- **ErrorHandlingMiddleware** (14 connections) — `server/middleware/error_handling_middleware.py`
- **test_error_handling_middleware.py** (13 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **._handle_exception()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **request_id_from_scope()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **.log_exception()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **extract_user_id_from_non_mapping()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.__call__()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.dispatch()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **_error_log_kwargs()** (5 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **_UserObjectWithId** (4 connections) — `server/middleware/error_handling_middleware.py`
- **_UserWithGet** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_adds_user_id_for_mapping_user()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Scope** (3 connections)
- **.__init__()** (3 connections) — `server/middleware/error_handling_middleware.py`
- **_UserWithId** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_request_id_from_scope()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_log_exception_mapping_user_missing_id_sets_none()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Receive** (2 connections)
- **Send** (2 connections)
- **Exception** (2 connections)
- **Request** (2 connections)
- **.__init__()** (2 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **.get()** (2 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_request_id_from_scope_non_str_coerced()** (2 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **test_extract_user_id_from_non_mapping()** (2 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- *... and 17 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (9 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)

## Source Files

- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 126 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*