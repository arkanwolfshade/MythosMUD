# Test Logging Handlers

> 73 nodes

## Key Concepts

- **test_logging_handlers.py** (29 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **create_aggregator_handler()** (22 connections) — `server/structured_logging/logging_handlers.py`
- **logging_handlers.py** (17 connections) — `server/structured_logging/logging_handlers.py`
- **SafeRotatingFileHandler** (15 connections) — `server/structured_logging/logging_handlers.py`
- **WarningOnlyFilter** (12 connections) — `server/structured_logging/logging_handlers.py`
- **AsyncioConnLostWriteFilter** (9 connections) — `server/structured_logging/logging_handlers.py`
- **load_player_guid_formatter_class()** (8 connections) — `server/structured_logging/logging_utilities.py`
- **_aggregator_handler_class_for_windows()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_make_exec_for_aggregator()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **._open()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **.shouldRollover()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **test_create_aggregator_handler_warning_level()** (5 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_error_level()** (4 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **RotatingFileHandler** (4 connections)
- **.filter()** (3 connections) — `server/structured_logging/logging_handlers.py`
- **temp_log_dir()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **temp_log_file()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_non_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_retries_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_with_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_create_aggregator_handler_without_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_init()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_no_base_filename()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **test_safe_rotating_file_handler_open_returns_stringio_on_final_failure()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- *... and 48 more nodes in this community*

## Relationships

- [Test Logging Utilities](Test_Logging_Utilities.md) (7 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [Logging File Setup](Logging_File_Setup.md) (6 shared connections)
- [Test Windows Safe Rotation](Test_Windows_Safe_Rotation.md) (3 shared connections)
- [Test Player Guid Formatter](Test_Player_Guid_Formatter.md) (2 shared connections)
- [Logging File Categories](Logging_File_Categories.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_handlers.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 131 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*