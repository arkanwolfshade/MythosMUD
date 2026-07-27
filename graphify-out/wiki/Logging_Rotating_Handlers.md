# Logging Rotating Handlers

> 50 nodes · cohesion 0.06

## Key Concepts

- **test_logging_handlers.py** (25 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **create_aggregator_handler()** (19 connections) — `server/structured_logging/logging_handlers.py`
- **WarningOnlyFilter** (11 connections) — `server/structured_logging/logging_handlers.py`
- **logging_handlers.py** (9 connections) — `server/structured_logging/logging_handlers.py`
- **_aggregator_handler_class_for_windows()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_make_exec_for_aggregator()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **Test WarningOnlyFilter blocks ERROR level logs.** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
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
- **test_warning_only_filter_critical_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_warning_only_filter_debug_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_warning_only_filter_error_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_warning_only_filter_info_level()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- *... and 25 more nodes in this community*

## Relationships

- [[Logging File Setup]] (16 shared connections)
- [[Logging Path Utilities]] (3 shared connections)
- [[Logging Structured Player]] (2 shared connections)
- [[Logging Structured Handlers]] (2 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/structured_logging/logging_handlers.py`
- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 161 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
