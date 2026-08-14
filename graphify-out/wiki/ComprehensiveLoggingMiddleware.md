# ComprehensiveLoggingMiddleware

> 14 nodes

## Key Concepts

- **ComprehensiveLoggingMiddleware** (16 connections) — `server/middleware/comprehensive_logging.py`
- **test_comprehensive_logging.py** (9 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **asyncio** (5 connections)
- **test_comprehensive_logging_passes_non_http()** (4 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_reraises_exception()** (4 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_successful_request()** (4 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **.__init__()** (3 connections) — `server/middleware/comprehensive_logging.py`
- **test_comprehensive_logging_dispatch_error()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_dispatch_success()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_log_request_start_long_auth_header()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **ASGIApp** (1 connections)
- **Pure ASGI middleware that combines access, error, and request logging. This…** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Initialize comprehensive logging middleware. Args: app: ASGI application…** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Unit tests for comprehensive logging middleware.** (1 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`

## Relationships

- [.__call__](__call__.md) (5 shared connections)
- [middleware](middleware.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [factory.py](factory.py.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/middleware/comprehensive_logging.py`
- `server/tests/unit/middleware/test_comprehensive_logging.py`

## Audit Trail

- EXTRACTED: 31 (89%)
- INFERRED: 4 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*