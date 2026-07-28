# Server Structured Logging (9)

> 23 nodes

## Key Concepts

- **LoggedException** (23 connections) — `server/exceptions.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **test_enhanced_logging_config.py** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_StubBoundLogger** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_logged_http_exception_inheritance()** (4 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_already_logged()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **.already_logged()** (2 connections) — `server/exceptions.py`
- **BoundLogger** (2 connections)
- **Marker base class indicating an exception has already produced a log entry.** (1 connections) — `server/exceptions.py`
- **Return True if this exception instance has already been logged.** (1 connections) — `server/exceptions.py`
- **Exception** (1 connections)
- **Log an exception once, respecting exceptions that have already been logged.** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Unit tests for enhanced_logging_config helpers.  Covers log_exception_once ded** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Minimal stand-in for BoundLogger: only what log_exception_once touches for these** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Adapt test double to the function param type (structural use only).** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Plain exceptions get _already_logged via __setattr__ fallback; second log is sup** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **LoggedException uses mark_logged(); repeat call does not log again.** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Test that LoggedHTTPException inherits from both classes.** (1 connections) — `server/tests/unit/test_exceptions.py`
- **Test LoggedException can be created with already_logged=True.** (1 connections) — `server/tests/unit/test_exceptions_comprehensive.py`

## Relationships

- [Server Utils (3)](Server_Utils_%283%29.md) (13 shared connections)
- [Server Services (62)](Server_Services_%2862%29.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Admin](Server_Admin.md) (2 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (2 shared connections)
- [Server Api](Server_Api.md) (2 shared connections)
- [Server Monitoring](Server_Monitoring.md) (2 shared connections)
- [Server Error Handlers (2)](Server_Error_Handlers_%282%29.md) (1 shared connections)
- [Server Services](Server_Services.md) (1 shared connections)
- [Server Time](Server_Time.md) (1 shared connections)

## Source Files

- `server/exceptions.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 87 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*