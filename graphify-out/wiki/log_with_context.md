# log_with_context

> 33 nodes

## Key Concepts

- **log_with_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **wrap_third_party_exception_enhanced()** (10 connections) — `server/utils/enhanced_error_logging.py`
- **log_structured_error()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (9 connections)
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **create_logged_http_exception_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **log_and_raise_http_enhanced()** (6 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception()** (6 connections) — `server/utils/error_logging.py`
- **log_performance_metric()** (5 connections) — `server/utils/enhanced_error_logging.py`
- **log_security_event_enhanced()** (5 connections) — `server/utils/enhanced_error_logging.py`
- **create_logged_http_exception()** (5 connections) — `server/utils/error_logging.py`
- **log_error_with_context()** (5 connections) — `server/utils/error_logging.py`
- **Any** (5 connections)
- **log_and_raise_http()** (4 connections) — `server/utils/error_logging.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **Exception** (2 connections)
- **HTTPException** (2 connections)
- **Exception** (2 connections)
- **BoundLogger** (1 connections)
- **HTTPException** (1 connections)
- **Resolve an alert. Args: alert_id: ID of the alert to resolve Returns: True if…** (1 connections) — `server/monitoring/monitoring_dashboard.py`
- **Log a message with the current context automatically included. Args:…** (1 connections) — `server/structured_logging/logging_context.py`
- **Log HTTP error and optionally raise or return HTTPException. Shared by raise vs…** (1 connections) — `server/utils/enhanced_error_logging.py`
- **Enhanced HTTP error logging with structured logging. This function provides a…** (1 connections) — `server/utils/enhanced_error_logging.py`
- **Create an HTTPException with proper logging and return it (caller raises when…** (1 connections) — `server/utils/enhanced_error_logging.py`
- *... and 8 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (11 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)
- [bind_request_context](bind_request_context.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [MythosMUDError](MythosMUDError.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)

## Source Files

- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 70 (85%)
- INFERRED: 12 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*