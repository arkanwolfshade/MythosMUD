# Test Comprehensive Logging

> 14 nodes

## Key Concepts

- **ComprehensiveLoggingMiddleware** (16 connections) — `server/middleware/comprehensive_logging.py`
- **test_comprehensive_logging.py** (11 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **comprehensive_logging.py** (7 connections) — `server/middleware/comprehensive_logging.py`
- **asyncio** (5 connections)
- **test_comprehensive_logging_passes_non_http()** (4 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_reraises_exception()** (4 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_successful_request()** (4 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_dispatch_error()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_dispatch_success()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_log_request_start_long_auth_header()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **.default()** (2 connections) — `server/realtime/envelope.py`
- **Comprehensive logging middleware for MythosMUD server. This module provides a…** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Pure ASGI middleware that combines access, error, and request logging. This…** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Unit tests for comprehensive logging middleware.** (1 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`

## Relationships

- [Comprehensive Logging](Comprehensive_Logging.md) (6 shared connections)
- [Test Security Headers](Test_Security_Headers.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Test Envelope](Test_Envelope.md) (1 shared connections)

## Source Files

- `server/middleware/comprehensive_logging.py`
- `server/realtime/envelope.py`
- `server/tests/unit/middleware/test_comprehensive_logging.py`

## Audit Trail

- EXTRACTED: 32 (78%)
- INFERRED: 9 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*