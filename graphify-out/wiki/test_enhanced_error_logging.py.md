# test_enhanced_error_logging.py

> 41 nodes

## Key Concepts

- **test_enhanced_error_logging.py** (22 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception_enhanced()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **log_structured_error()** (11 connections) — `server/utils/enhanced_error_logging.py`
- **create_logged_http_exception_enhanced()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (9 connections)
- **log_and_raise_http_enhanced()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **log_performance_metric()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **log_security_event_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **test_log_and_raise_enhanced()** (4 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_log_and_raise_enhanced_with_metadata()** (4 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_wrap_third_party_exception_enhanced()** (3 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_create_enhanced_error_context()** (2 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_create_error_context()** (2 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_create_logged_http_exception_enhanced()** (2 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_log_and_raise_http_enhanced()** (2 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_log_performance_metric()** (2 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_log_security_event_enhanced()** (2 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_log_structured_error()** (2 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **Exception** (2 connections)
- **HTTPException** (2 connections)
- **BoundLogger** (1 connections)
- *... and 16 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (21 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (6 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (5 shared connections)
- [MythosMUDError](MythosMUDError.md) (4 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (2 shared connections)

## Source Files

- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 100 (87%)
- INFERRED: 15 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*