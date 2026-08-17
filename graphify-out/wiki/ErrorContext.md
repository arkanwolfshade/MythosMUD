# ErrorContext

> 120 nodes

## Key Concepts

- **ErrorContext** (43 connections) — `server/exceptions.py`
- **test_error_logging.py** (25 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (24 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **.__init__()** (15 connections) — `server/exceptions.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (13 connections)
- **log_structured_error()** (11 connections) — `server/utils/enhanced_error_logging.py`
- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **create_context_from_request()** (10 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception_enhanced()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (9 connections)
- **log_and_raise_http_enhanced()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **.__init__()** (7 connections) — `server/exceptions.py`
- **log_performance_metric()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **log_security_event_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_websocket()** (7 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception()** (7 connections) — `server/utils/error_logging.py`
- **log_error_with_context()** (7 connections) — `server/utils/error_logging.py`
- **track_exception_with_context()** (6 connections) — `server/monitoring/exception_tracker.py`
- **log_and_raise_http()** (6 connections) — `server/utils/error_logging.py`
- **.mark_logged()** (5 connections) — `server/exceptions.py`
- **increment_exception()** (5 connections) — `server/monitoring/exception_metrics.py`
- **Any** (5 connections)
- *... and 95 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (95 shared connections)
- [ValidationError](ValidationError.md) (11 shared connections)
- [bind_request_context](bind_request_context.md) (5 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (4 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (2 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [User](User.md) (1 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/monitoring/exception_metrics.py`
- `server/monitoring/exception_tracker.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 268 (90%)
- INFERRED: 30 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*