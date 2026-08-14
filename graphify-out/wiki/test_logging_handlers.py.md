# test_logging_handlers.py

> 61 nodes

## Key Concepts

- **test_logging_handlers.py** (28 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **create_aggregator_handler()** (21 connections) — `server/structured_logging/logging_handlers.py`
- **logging_handlers.py** (15 connections) — `server/structured_logging/logging_handlers.py`
- **WarningOnlyFilter** (11 connections) — `server/structured_logging/logging_handlers.py`
- **AsyncioConnLostWriteFilter** (10 connections) — `server/structured_logging/logging_handlers.py`
- **_aggregator_handler_class_for_windows()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_make_exec_for_aggregator()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **RotatingFileHandler** (4 connections)
- **_LoggingState** (3 connections) — `server/structured_logging/enhanced_logging_config.py`
- **temp_log_dir()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **temp_log_file()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_error_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_non_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_retries_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_warning_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_with_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_without_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_init()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_no_base_filename()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_returns_stringio_on_final_failure()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_success()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_false()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_no_base_filename()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_retries_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- *... and 36 more nodes in this community*

## Relationships

- [logging_file_setup.py](logging_file_setup.py.md) (15 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (4 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (4 shared connections)
- [._open](_open.md) (3 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (1 shared connections)

## Source Files

- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/logging_handlers.py`
- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 110 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*