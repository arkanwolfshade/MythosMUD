# generate invites db

> 19 nodes

## Key Concepts

- **._handle_exception()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **request_id_from_scope()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **.log_exception()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **.__call__()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.dispatch()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **Scope** (3 connections)
- **test_request_id_from_scope()** (3 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Receive** (2 connections)
- **Send** (2 connections)
- **Exception** (2 connections)
- **Request** (2 connections)
- **test_request_id_from_scope_non_str_coerced()** (2 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Response** (1 connections)
- **Read request_id from ASGI scope.state (Scope values are Any; avoid untyped .get** (1 connections) — `server/middleware/error_handling_middleware.py`
- **ASGI application interface.          Args:             scope: ASGI connection sc** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Handle an exception and send a standardized error response.          Args:** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Backward-compatible dispatch method for BaseHTTPMiddleware interface.          T** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Log the exception with full context information.          Public entry point so** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Scope** (1 connections)

## Relationships

- [Response](Response.md) (9 shared connections)
- [convert pydantic error()](convert_pydantic_error%28%29.md) (2 shared connections)

## Source Files

- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*