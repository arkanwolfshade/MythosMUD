# middleware comprehensive logging

> 29 nodes

## Key Concepts

- **ComprehensiveLoggingMiddleware** (17 connections) — `server/middleware/comprehensive_logging.py`
- **test_comprehensive_logging.py** (9 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **.__call__()** (8 connections) — `server/middleware/comprehensive_logging.py`
- **.dispatch()** (7 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_start()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_success_with_status()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_error()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **Request** (4 connections)
- **.__init__()** (3 connections) — `server/middleware/comprehensive_logging.py`
- **test_comprehensive_logging_passes_non_http()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_successful_request()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_reraises_exception()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_log_request_start_long_auth_header()** (3 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **.default()** (2 connections) — `server/realtime/envelope.py`
- **test_comprehensive_logging_dispatch_success()** (2 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **test_comprehensive_logging_dispatch_error()** (2 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **ASGIApp** (1 connections)
- **Scope** (1 connections)
- **Receive** (1 connections)
- **Send** (1 connections)
- **Any** (1 connections)
- **Exception** (1 connections)
- **Pure ASGI middleware that combines access, error, and request logging.      This** (1 connections) — `server/middleware/comprehensive_logging.py`
- **Initialize comprehensive logging middleware.          Args:             app: ASG** (1 connections) — `server/middleware/comprehensive_logging.py`
- **ASGI application interface.          Args:             scope: ASGI connection sc** (1 connections) — `server/middleware/comprehensive_logging.py`
- *... and 4 more nodes in this community*

## Relationships

- [app factory rationale](app_factory_rationale.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [feature services flag](feature_services_flag.md) (1 shared connections)
- [playerHandlers eventHandlers healthEvent](playerHandlers_eventHandlers_healthEvent.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)

## Source Files

- `server/middleware/comprehensive_logging.py`
- `server/realtime/envelope.py`
- `server/tests/unit/middleware/test_comprehensive_logging.py`

## Audit Trail

- EXTRACTED: 88 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*