# test_security_headers.py

> 86 nodes

## Key Concepts

- **test_security_headers.py** (20 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **middleware()** (17 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **CorrelationMiddleware** (13 connections) — `server/middleware/correlation_middleware.py`
- **SecurityHeadersMiddleware** (12 connections) — `server/middleware/security_headers.py`
- **test_correlation_middleware.py** (12 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **correlation_middleware.py** (8 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (6 connections) — `server/middleware/correlation_middleware.py`
- **MutableHeaders** (6 connections)
- **security_headers.py** (6 connections) — `server/middleware/security_headers.py`
- **.__call__()** (5 connections) — `server/middleware/security_headers.py`
- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **asyncio** (5 connections)
- **asyncio** (5 connections)
- **._add_security_headers_to_response()** (4 connections) — `server/middleware/security_headers.py`
- **test_correlation_middleware_adds_response_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_reraises_exception()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_uses_existing_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_security_headers_middleware_adds_headers()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_error_handling()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_non_http_scope()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- *... and 61 more nodes in this community*

## Relationships

- [factory.py](factory.py.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [bind_request_context](bind_request_context.md) (3 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (1 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`
- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 119 (84%)
- INFERRED: 22 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*