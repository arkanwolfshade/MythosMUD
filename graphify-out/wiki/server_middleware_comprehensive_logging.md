# server middleware comprehensive logging

> 31 nodes

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
- **Any** (1 connections)
- **ASGIApp** (1 connections)
- **Exception** (1 connections)
- **Receive** (1 connections)
- **Scope** (1 connections)
- **Send** (1 connections)
- **Comprehensive logging middleware for MythosMUD server. This module provides a…** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Log request start information.** (1 connections) — `server/middleware/comprehensive_logging.py`
- *... and 6 more nodes in this community*

## Relationships

- [server middleware correlation middleware](server_middleware_correlation_middleware.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [scripts generate openapi spec](scripts_generate_openapi_spec.md) (2 shared connections)
- [server realtime envelope rationale 33](server_realtime_envelope_rationale_33.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `server/middleware/comprehensive_logging.py`
- `server/tests/unit/middleware/test_comprehensive_logging.py`

## Audit Trail

- EXTRACTED: 51 (84%)
- INFERRED: 10 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*