# Realtime Connection Impl

> 15 nodes · cohesion 0.18

## Key Concepts

- **.__call__()** (8 connections) — `server/middleware/comprehensive_logging.py`
- **.dispatch()** (7 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_error()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_start()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_success_with_status()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **Request** (4 connections)
- **Any** (1 connections)
- **Exception** (1 connections)
- **Receive** (1 connections)
- **Scope** (1 connections)
- **Send** (1 connections)
- **Log request start information.** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Log successful request completion.** (1 connections) — `server/middleware/comprehensive_logging.py`
- **ASGI application interface.          Args:             scope: ASGI connection sc** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Backward-compatible dispatch method for BaseHTTPMiddleware interface.          T** (1 connections) — `server/middleware/comprehensive_logging.py`

## Relationships

- [Community 2199](Community_2199.md) (5 shared connections)

## Source Files

- `server/middleware/comprehensive_logging.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*