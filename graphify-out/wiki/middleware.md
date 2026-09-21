# middleware

> 18 nodes

## Key Concepts

- **middleware()** (17 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **CorrelationMiddleware** (13 connections) — `server/middleware/correlation_middleware.py`
- **test_correlation_middleware.py** (12 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **correlation_middleware.py** (8 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **asyncio** (5 connections)
- **test_correlation_middleware_adds_response_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_reraises_exception()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_uses_existing_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_create_correlation_middleware_factory()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Any** (1 connections)
- **Correlation middleware for request tracing and logging context. This middleware…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Create a correlation middleware factory. Args: correlation_header: HTTP header…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Pure ASGI middleware for adding correlation IDs and request context to all…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Unit tests for correlation ID middleware.** (1 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Create SecurityHeadersMiddleware instance.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [test_security_headers.py](test_security_headers.py.md) (5 shared connections)
- [.__call__](__call__.md) (4 shared connections)
- [ComprehensiveLoggingMiddleware](ComprehensiveLoggingMiddleware.md) (3 shared connections)
- [factory.py](factory.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (1 shared connections)
- [SecurityHeadersMiddleware](SecurityHeadersMiddleware.md) (1 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 40 (73%)
- INFERRED: 15 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*