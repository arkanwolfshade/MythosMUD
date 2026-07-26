# test_logging_handlers.py

> 68 nodes · cohesion 0.05

## Key Concepts

- **test_logging_handlers.py** (26 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **ensure_log_directory()** (23 connections) — `server/structured_logging/logging_utilities.py`
- **create_aggregator_handler()** (21 connections) — `server/structured_logging/logging_handlers.py`
- **SafeRotatingFileHandler** (20 connections) — `server/structured_logging/logging_handlers.py`
- **logging_handlers.py** (16 connections) — `server/structured_logging/logging_handlers.py`
- **WarningOnlyFilter** (13 connections) — `server/structured_logging/logging_handlers.py`
- **_aggregator_handler_class_for_windows()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_make_exec_for_aggregator()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **._open()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **.shouldRollover()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **RotatingFileHandler** (4 connections)
- **test_create_aggregator_handler_error_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_warning_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **Path** (3 connections)
- **.filter()** (3 connections) — `server/structured_logging/logging_handlers.py`
- **test_create_aggregator_handler_non_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_retries_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_with_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_without_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_init()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_no_base_filename()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_returns_stringio_on_final_failure()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_success()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_false()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- *... and 43 more nodes in this community*

## Relationships

- [logging_file_setup.py](logging_file_setup.py.md) (17 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (10 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_handlers.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 233 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*