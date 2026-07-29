# ComprehensiveLoggingMiddleware

> 20 nodes

## Key Concepts

- **ComprehensiveLoggingMiddleware** (10 connections) — `server/middleware/comprehensive_logging.py`
- **.__call__()** (8 connections) — `server/middleware/comprehensive_logging.py`
- **.dispatch()** (7 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_start()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_success_with_status()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_error()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **Request** (4 connections)
- **.__init__()** (3 connections) — `server/middleware/comprehensive_logging.py`
- **ASGIApp** (1 connections)
- **Scope** (1 connections)
- **Receive** (1 connections)
- **Send** (1 connections)
- **Any** (1 connections)
- **Exception** (1 connections)
- **Pure ASGI middleware that combines access, error, and request logging.      This** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Initialize comprehensive logging middleware.          Args:             app: ASG** (1 connections) — `server/middleware/comprehensive_logging.py`
- **ASGI application interface.          Args:             scope: ASGI connection sc** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Backward-compatible dispatch method for BaseHTTPMiddleware interface.          T** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Log request start information.** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Log successful request completion.** (1 connections) — `server/middleware/comprehensive_logging.py`

## Relationships

- [BaseUserManager](BaseUserManager.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)

## Source Files

- `server/middleware/comprehensive_logging.py`

## Audit Trail

- EXTRACTED: 58 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*