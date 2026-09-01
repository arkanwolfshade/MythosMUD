# ComprehensiveLoggingMiddleware

> 32 nodes

## Key Concepts

- **ComprehensiveLoggingMiddleware** (16 connections) — `server/middleware/comprehensive_logging.py`
- **test_comprehensive_logging.py** (11 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **.__call__()** (8 connections) — `server/middleware/comprehensive_logging.py`
- **.dispatch()** (7 connections) — `server/middleware/comprehensive_logging.py`
- **comprehensive_logging.py** (7 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_error()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_start()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_success_with_status()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **asyncio** (5 connections)
- **test_comprehensive_logging_passes_non_http()** (4 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_reraises_exception()** (4 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_successful_request()** (4 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **Request** (4 connections)
- **.__init__()** (3 connections) — `server/middleware/comprehensive_logging.py`
- **test_comprehensive_logging_dispatch_error()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_dispatch_success()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_log_request_start_long_auth_header()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **.default()** (2 connections) — `server/realtime/envelope.py`
- **Any** (1 connections)
- **ASGIApp** (1 connections)
- **Exception** (1 connections)
- **Receive** (1 connections)
- **Scope** (1 connections)
- **Send** (1 connections)
- **Comprehensive logging middleware for MythosMUD server. This module provides a…** (1 connections) — `server/middleware/comprehensive_logging.py`
- *... and 7 more nodes in this community*

## Relationships

- [middleware](middleware.md) (3 shared connections)
- [factory.py](factory.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/middleware/comprehensive_logging.py`
- `server/realtime/envelope.py`
- `server/tests/unit/middleware/test_comprehensive_logging.py`

## Audit Trail

- EXTRACTED: 53 (85%)
- INFERRED: 9 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*