# test_error_logging.py

> 68 nodes

## Key Concepts

- **test_error_logging.py** (23 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (22 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception_enhanced()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **log_structured_error()** (11 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_request()** (10 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception_enhanced()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (9 connections)
- **log_and_raise_http_enhanced()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception()** (8 connections) — `server/utils/error_logging.py`
- **log_performance_metric()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **log_security_event_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_websocket()** (7 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception()** (7 connections) — `server/utils/error_logging.py`
- **log_error_with_context()** (7 connections) — `server/utils/error_logging.py`
- **log_and_raise_http()** (6 connections) — `server/utils/error_logging.py`
- **Any** (5 connections)
- **test_wrap_third_party_exception_enhanced()** (3 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_create_error_context()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_error_context_with_metadata()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_error_context_to_dict()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_log_and_raise_delegates_to_enhanced()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_wrap_third_party_exception_delegates()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- *... and 43 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (18 shared connections)
- [DatabaseError](DatabaseError.md) (18 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (5 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (5 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (5 shared connections)
- [MythosMUDError](MythosMUDError.md) (4 shared connections)
- [ErrorContext](ErrorContext.md) (3 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (2 shared connections)
- [create_error_context](create_error_context.md) (2 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_context.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 158 (91%)
- INFERRED: 15 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*