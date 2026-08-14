# middleware

> 29 nodes

## Key Concepts

- **middleware()** (19 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_correlation_middleware.py** (17 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **CorrelationMiddleware** (12 connections) — `server/middleware/correlation_middleware.py`
- **correlation_middleware.py** (10 connections) — `server/middleware/correlation_middleware.py`
- **WebSocketCorrelationMiddleware** (8 connections) — `server/middleware/correlation_middleware.py`
- **asyncio** (7 connections)
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **test_correlation_middleware_adds_response_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_reraises_exception()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_uses_existing_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_websocket_correlation_middleware()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_websocket_correlation_middleware_generates_id()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- **test_create_correlation_middleware_factory()** (2 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_create_websocket_correlation_middleware()** (2 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Any** (2 connections)
- **Correlation middleware for request tracing and logging context. This middleware…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Middleware for adding correlation IDs to WebSocket connections. This middleware…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Initialize the WebSocket correlation middleware. Args: correlation_header: HTTP…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Process the WebSocket connection with correlation ID. Args: websocket:…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Create a correlation middleware factory. Args: correlation_header: HTTP header…** (1 connections) — `server/middleware/correlation_middleware.py`
- *... and 4 more nodes in this community*

## Relationships

- [test_security_headers.py](test_security_headers.py.md) (5 shared connections)
- [.__call__](__call__.md) (4 shared connections)
- [log_with_context](log_with_context.md) (3 shared connections)
- [ComprehensiveLoggingMiddleware](ComprehensiveLoggingMiddleware.md) (3 shared connections)
- [factory.py](factory.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [SecurityHeadersMiddleware](SecurityHeadersMiddleware.md) (1 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (1 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 66 (85%)
- INFERRED: 12 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*