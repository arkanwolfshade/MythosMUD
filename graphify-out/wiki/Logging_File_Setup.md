# Logging File Setup

> 74 nodes

## Key Concepts

- **logging_file_setup.py** (35 connections) — `server/structured_logging/logging_file_setup.py`
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_file_setup.py** (14 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **load_player_guid_formatter_class()** (11 connections) — `server/structured_logging/logging_utilities.py`
- **_setup_aggregator_handlers()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **LoggerNameFilter** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_handler_for_category()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **Queue** (7 connections)
- **test_queue_listener_has_aggregator_handlers()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_warning_and_error_reach_aggregator_files()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **get_queue_listener()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **stop_queue_listener()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_CategoryHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **Handler** (6 connections)
- **_ConsoleHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_async_logging_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_formatter()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_root_handlers_snapshot()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_restore_root_handlers()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_aggregator_handlers_on_root_when_async()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_get_or_create_log_queue()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_class()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_add_handler_to_loggers()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- *... and 49 more nodes in this community*

## Relationships

- [Logging Path Utilities](Logging_Path_Utilities.md) (13 shared connections)
- [Logging Structured Handlers](Logging_Structured_Handlers.md) (10 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (5 shared connections)
- [Windows Log Rotation](Windows_Log_Rotation.md) (4 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (3 shared connections)
- [Logging Structured Player](Logging_Structured_Player.md) (3 shared connections)
- [Monitoring Bundle Services](Monitoring_Bundle_Services.md) (1 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`

## Audit Trail

- EXTRACTED: 284 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*