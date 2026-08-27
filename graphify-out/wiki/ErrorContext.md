# ErrorContext

> 24 nodes

## Key Concepts

- **ErrorContext** (40 connections) — `server/exceptions.py`
- **.__init__()** (15 connections) — `server/exceptions.py`
- **Any** (13 connections)
- **.__init__()** (7 connections) — `server/exceptions.py`
- **.mark_logged()** (5 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.to_dict()** (3 connections) — `server/exceptions.py`
- **._log_error()** (3 connections) — `server/exceptions.py`
- **Initialize the Pydantic error handler. Args: context: Optional error context…** (1 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Initialize MythosMUD error. Args: message: Technical error message context:…** (1 connections) — `server/exceptions.py`
- **Log validation errors at warning so expected user-input errors do not flood…** (1 connections) — `server/exceptions.py`
- **Contextual information for error handling. Provides structured context for…** (1 connections) — `server/exceptions.py`
- **Initialize LoggedHTTPException. Args: status_code: HTTP status code detail:…** (1 connections) — `server/exceptions.py`
- **Convert context to dictionary for logging.** (1 connections) — `server/exceptions.py`
- **Mark this exception instance as already logged.** (1 connections) — `server/exceptions.py`

## Relationships

- [ValidationError](ValidationError.md) (9 shared connections)
- [test_exceptions_comprehensive.py](test_exceptions_comprehensive.py.md) (7 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (7 shared connections)
- [MythosMUDError](MythosMUDError.md) (6 shared connections)
- [ErrorType](ErrorType.md) (4 shared connections)
- [LoggedException](LoggedException.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)
- [ConfigurationError](ConfigurationError.md) (1 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`

## Audit Trail

- EXTRACTED: 87 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*