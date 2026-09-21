# test_logging_handlers.py

> 81 nodes

## Key Concepts

- **test_logging_handlers.py** (28 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **create_aggregator_handler()** (20 connections) — `server/structured_logging/logging_handlers.py`
- **logging_handlers.py** (20 connections) — `server/structured_logging/logging_handlers.py`
- **SafeRotatingFileHandler** (15 connections) — `server/structured_logging/logging_handlers.py`
- **WarningOnlyFilter** (12 connections) — `server/structured_logging/logging_handlers.py`
- **load_player_guid_formatter_class()** (10 connections) — `server/structured_logging/logging_utilities.py`
- **AsyncioConnLostWriteFilter** (9 connections) — `server/structured_logging/logging_handlers.py`
- **_build_aggregator_formatter()** (6 connections) — `server/structured_logging/logging_handlers.py`
- **_instantiate_aggregator_handler()** (6 connections) — `server/structured_logging/logging_handlers.py`
- **_resolve_aggregator_handler_class()** (6 connections) — `server/structured_logging/logging_handlers.py`
- **RotatingFileHandler** (6 connections)
- **_aggregator_handler_class_for_windows()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_make_exec_for_aggregator()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **._open()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **.shouldRollover()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **test_create_aggregator_handler_warning_level()** (5 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_error_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **Path** (4 connections)
- **.filter()** (3 connections) — `server/structured_logging/logging_handlers.py`
- **temp_log_dir()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **temp_log_file()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_non_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_retries_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_with_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- *... and 56 more nodes in this community*

## Relationships

- [logging_file_setup.py](logging_file_setup.py.md) (9 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (3 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (2 shared connections)
- [LoggingConfig](LoggingConfig.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_handlers.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 145 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*