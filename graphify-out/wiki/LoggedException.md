# LoggedException

> 18 nodes

## Key Concepts

- **LoggedException** (20 connections) — `server/exceptions.py`
- **test_logged_http_exception_initialization()** (5 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_logged_exception_already_logged()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_logged_exception_mark_logged()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_logged_exception_already_logged()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_mark_logged()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **.already_logged()** (2 connections) — `server/exceptions.py`
- **Marker base class indicating an exception has already produced a log entry.** (1 connections) — `server/exceptions.py`
- **Return True if this exception instance has already been logged.** (1 connections) — `server/exceptions.py`
- **Test LoggedException can be instantiated.** (1 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **Test LoggedException.mark_logged() marks as logged.** (1 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **Test LoggedException can be created with already_logged=True.** (1 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **Test LoggedHTTPException initialization.** (1 connections) — `server/tests/unit/test_exceptions.py`
- **Test LoggedException initialization.** (1 connections) — `server/tests/unit/test_exceptions.py`
- **Test LoggedException with already_logged flag.** (1 connections) — `server/tests/unit/test_exceptions.py`
- **Test LoggedException.mark_logged() method.** (1 connections) — `server/tests/unit/test_exceptions.py`

## Relationships

- [test_exceptions.py](test_exceptions.py.md) (6 shared connections)
- [test_exceptions_comprehensive.py](test_exceptions_comprehensive.py.md) (5 shared connections)
- [ErrorContext](ErrorContext.md) (3 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)

## Source Files

- `server/exceptions.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 35 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*