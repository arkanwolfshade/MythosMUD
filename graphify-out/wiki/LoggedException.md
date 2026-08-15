# LoggedException

> 21 nodes

## Key Concepts

- **LoggedException** (20 connections) — `server/exceptions.py`
- **test_enhanced_logging_config.py** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_StubBoundLogger** (7 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_logged_http_exception_initialization()** (5 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_http_exception_inheritance()** (4 connections) — `server/tests/unit/test_exceptions.py`
- **.already_logged()** (2 connections) — `server/exceptions.py`
- **Exception** (2 connections)
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **BoundLogger** (1 connections)
- **Marker base class indicating an exception has already produced a log entry.** (1 connections) — `server/exceptions.py`
- **Return True if this exception instance has already been logged.** (1 connections) — `server/exceptions.py`
- **Unit tests for enhanced_logging_config helpers. Covers log_exception_once…** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Minimal stand-in for BoundLogger: only what log_exception_once touches for…** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Adapt test double to the function param type (structural use only).** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Plain exceptions get _already_logged via __setattr__ fallback; second log is…** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **LoggedException uses mark_logged(); repeat call does not log again.** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Test LoggedHTTPException initialization.** (1 connections) — `server/tests/unit/test_exceptions.py`
- **Test that LoggedHTTPException inherits from both classes.** (1 connections) — `server/tests/unit/test_exceptions.py`

## Relationships

- [ErrorContext](ErrorContext.md) (9 shared connections)
- [MythosMUDError](MythosMUDError.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/exceptions.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_exceptions.py`

## Audit Trail

- EXTRACTED: 39 (76%)
- INFERRED: 12 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*