# ComprehensiveLoggingMiddleware

> 20 nodes

## Key Concepts

- **ComprehensiveLoggingMiddleware** (9 connections) — `server/middleware/comprehensive_logging.py`
- **.__call__()** (8 connections) — `server/middleware/comprehensive_logging.py`
- **.dispatch()** (7 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_error()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_start()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_success_with_status()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **Request** (4 connections)
- **.__init__()** (3 connections) — `server/middleware/comprehensive_logging.py`
- **Any** (1 connections)
- **ASGIApp** (1 connections)
- **Exception** (1 connections)
- **Receive** (1 connections)
- **Scope** (1 connections)
- **Send** (1 connections)
- **Log request start information.** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Log successful request completion.** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Pure ASGI middleware that combines access, error, and request logging. This…** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Initialize comprehensive logging middleware. Args: app: ASGI application…** (1 connections) — `server/middleware/comprehensive_logging.py`
- **ASGI application interface. Args: scope: ASGI connection scope receive: ASGI…** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Backward-compatible dispatch method for BaseHTTPMiddleware interface. This…** (1 connections) — `server/middleware/comprehensive_logging.py`

## Relationships

- [factory.py](factory.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/middleware/comprehensive_logging.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*