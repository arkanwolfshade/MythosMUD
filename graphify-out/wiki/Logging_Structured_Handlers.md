# Logging Structured Handlers

> 73 nodes

## Key Concepts

- **test_logging_handlers.py** (26 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **SafeRotatingFileHandler** (20 connections) — `server/structured_logging/logging_handlers.py`
- **logging_handlers.py** (19 connections) — `server/structured_logging/logging_handlers.py`
- **create_aggregator_handler()** (19 connections) — `server/structured_logging/logging_handlers.py`
- **WarningOnlyFilter** (13 connections) — `server/structured_logging/logging_handlers.py`
- **RotatingFileHandler** (6 connections)
- **_resolve_aggregator_handler_class()** (6 connections) — `server/structured_logging/logging_handlers.py`
- **_open_aggregator_handler()** (6 connections) — `server/structured_logging/logging_handlers.py`
- **._open()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **.shouldRollover()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_make_exec_for_aggregator()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_aggregator_handler_class_for_windows()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_aggregator_formatter()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **Path** (4 connections)
- **test_create_aggregator_handler_warning_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_error_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **.filter()** (3 connections) — `server/structured_logging/logging_handlers.py`
- **test_safe_rotating_file_handler_init()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_success()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_no_base_filename()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_returns_stringio_on_final_failure()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_false()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_no_base_filename()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_retries_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_warning_only_filter_warning_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- *... and 48 more nodes in this community*

## Relationships

- [Logging File Setup](Logging_File_Setup.md) (10 shared connections)
- [Logging Path Utilities](Logging_Path_Utilities.md) (6 shared connections)
- [Windows Log Rotation](Windows_Log_Rotation.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)

## Source Files

- `server/structured_logging/logging_handlers.py`
- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 235 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*