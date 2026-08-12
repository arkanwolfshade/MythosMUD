# log_with_context

> 18 nodes

## Key Concepts

- **log_with_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **log_structured_error()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (9 connections)
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **create_logged_http_exception_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **log_and_raise_http_enhanced()** (6 connections) — `server/utils/enhanced_error_logging.py`
- **log_performance_metric()** (5 connections) — `server/utils/enhanced_error_logging.py`
- **log_security_event_enhanced()** (5 connections) — `server/utils/enhanced_error_logging.py`
- **Exception** (2 connections)
- **HTTPException** (2 connections)
- **BoundLogger** (1 connections)
- **Log a message with the current context automatically included. Args:…** (1 connections) — `server/structured_logging/logging_context.py`
- **Log HTTP error and optionally raise or return HTTPException. Shared by raise vs…** (1 connections) — `server/utils/enhanced_error_logging.py`
- **Enhanced HTTP error logging with structured logging. This function provides a…** (1 connections) — `server/utils/enhanced_error_logging.py`
- **Create an HTTPException with proper logging and return it (caller raises when…** (1 connections) — `server/utils/enhanced_error_logging.py`
- **Log an error with structured context information. This function provides a…** (1 connections) — `server/utils/enhanced_error_logging.py`
- **Log performance metrics with structured data. This function logs performance…** (1 connections) — `server/utils/enhanced_error_logging.py`
- **Log security events with structured data. This function logs security events…** (1 connections) — `server/utils/enhanced_error_logging.py`

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (12 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (3 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (2 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [ErrorContext](ErrorContext.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_context.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 63 (80%)
- INFERRED: 16 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*