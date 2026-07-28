# Server Structured Logging (6)

> 51 nodes

## Key Concepts

- **test_logging_handlers.py** (26 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **create_aggregator_handler()** (21 connections) — `server/structured_logging/logging_handlers.py`
- **logging_handlers.py** (14 connections) — `server/structured_logging/logging_handlers.py`
- **WarningOnlyFilter** (13 connections) — `server/structured_logging/logging_handlers.py`
- **_make_exec_for_aggregator()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_aggregator_handler_class_for_windows()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **RotatingFileHandler** (4 connections)
- **test_create_aggregator_handler_warning_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_error_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_init()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_success()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_no_base_filename()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_returns_stringio_on_final_failure()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_false()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_no_base_filename()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_should_rollover_retries_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_warning_only_filter_warning_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_warning_only_filter_error_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_warning_only_filter_critical_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_warning_only_filter_info_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_warning_only_filter_debug_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_with_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_without_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_non_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- *... and 26 more nodes in this community*

## Relationships

- [Server Structured Logging (5)](Server_Structured_Logging_%285%29.md) (16 shared connections)
- [Server Structured Logging](Server_Structured_Logging.md) (4 shared connections)
- [Server Structured Logging (4)](Server_Structured_Logging_%284%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Structured Logging (15)](Server_Structured_Logging_%2815%29.md) (2 shared connections)
- [Server Structured Logging (3)](Server_Structured_Logging_%283%29.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_handlers.py`
- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 171 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*