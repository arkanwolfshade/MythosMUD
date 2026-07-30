# logging handlers

> 79 nodes

## Key Concepts

- **test_logging_handlers.py** (26 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **ensure_log_directory()** (23 connections) — `server/structured_logging/logging_utilities.py`
- **create_aggregator_handler()** (21 connections) — `server/structured_logging/logging_handlers.py`
- **SafeRotatingFileHandler** (20 connections) — `server/structured_logging/logging_handlers.py`
- **logging_utilities.py** (18 connections) — `server/structured_logging/logging_utilities.py`
- **logging_handlers.py** (16 connections) — `server/structured_logging/logging_handlers.py`
- **WarningOnlyFilter** (13 connections) — `server/structured_logging/logging_handlers.py`
- **load_player_guid_formatter_class()** (11 connections) — `server/structured_logging/logging_utilities.py`
- **._open()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **.shouldRollover()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_make_exec_for_aggregator()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_aggregator_handler_class_for_windows()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **RotatingFileHandler** (4 connections)
- **_rotation_bound_logger()** (4 connections) — `server/structured_logging/logging_utilities.py`
- **test_create_aggregator_handler_warning_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_error_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **.filter()** (3 connections) — `server/structured_logging/logging_handlers.py`
- **Path** (3 connections)
- **test_safe_rotating_file_handler_init()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_success()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_no_base_filename()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_returns_stringio_on_final_failure()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_false()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_no_base_filename()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_retries_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- *... and 54 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (19 shared connections)
- [Path](Path.md) (12 shared connections)
- [world](world.md) (7 shared connections)
- [windows safe rotation](windows_safe_rotation.md) (4 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (4 shared connections)
- [get current tick()](get_current_tick%28%29.md) (2 shared connections)

## Source Files

- `server/structured_logging/logging_handlers.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 273 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*