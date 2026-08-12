# ErrorContext

> 90 nodes

## Key Concepts

- **ErrorContext** (41 connections) — `server/exceptions.py`
- **LoggedException** (19 connections) — `server/exceptions.py`
- **.__init__()** (15 connections) — `server/exceptions.py`
- **Any** (13 connections)
- **create_enhanced_error_context()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **player_helpers.py** (9 connections) — `server/api/player_helpers.py`
- **test_enhanced_logging_config.py** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_StubBoundLogger** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.__init__()** (7 connections) — `server/exceptions.py`
- **create_context_from_request()** (7 connections) — `server/utils/error_logging.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.mark_logged()** (5 connections) — `server/exceptions.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **create_context_from_websocket()** (5 connections) — `server/utils/error_logging.py`
- **test_player_helpers.py** (5 connections) — `server/tests/unit/api/test_player_helpers.py`
- **.__init__()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- *... and 65 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (47 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [ErrorType](ErrorType.md) (4 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [User](User.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [MythosChronicle](MythosChronicle.md) (2 shared connections)
- [test_command_factories_utility.py](test_command_factories_utility.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)
- [error_handling_middleware.py](error_handling_middleware.py.md) (1 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 319 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*