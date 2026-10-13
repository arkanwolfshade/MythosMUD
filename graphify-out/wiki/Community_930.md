# Community 930

> 16 nodes

## Key Concepts

- **._handle_exception()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **.log_exception()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **request_id_from_scope()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **.__call__()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **.dispatch()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **Scope** (3 connections)
- **test_request_id_from_scope_non_str_coerced()** (2 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Receive** (2 connections)
- **Send** (2 connections)
- **Exception** (2 connections)
- **Response** (1 connections)
- **ASGI application interface. Args: scope: ASGI connection scope receive: ASGI…** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Handle an exception and send a standardized error response. Args: scope: ASGI…** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Backward-compatible dispatch method for BaseHTTPMiddleware interface. This…** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Log the exception with full context information. Public entry point so unit…** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Read request_id from ASGI scope.state (Scope values are Any; avoid untyped .get…** (1 connections) — `server/middleware/error_handling_middleware.py`

## Relationships

- [Community 445](Community_445.md) (8 shared connections)
- [Community 205](Community_205.md) (2 shared connections)
- [API Response Models](API_Response_Models.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)

## Source Files

- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*