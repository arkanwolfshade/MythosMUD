# logging_file_setup.py

> 104 nodes

## Key Concepts

- **logging_file_setup.py** (36 connections) — `server/structured_logging/logging_file_setup.py`
- **LoggingConfig** (25 connections) — `server/config/models/security_logging.py`
- **setup_enhanced_file_logging()** (21 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_file_setup.py** (21 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_Handler** (13 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **logging_file_categories.py** (12 connections) — `server/structured_logging/logging_file_categories.py`
- **add_handler_to_loggers()** (10 connections) — `server/structured_logging/logging_file_categories.py`
- **_setup_aggregator_handlers()** (10 connections) — `server/structured_logging/logging_file_setup.py`
- **load_player_guid_formatter_class()** (10 connections) — `server/structured_logging/logging_utilities.py`
- **security_logging.py** (10 connections) — `server/config/models/security_logging.py`
- **LoggerNameFilter** (9 connections) — `server/structured_logging/logging_file_categories.py`
- **create_handler_for_category()** (9 connections) — `server/structured_logging/logging_file_categories.py`
- **test_queue_listener_has_aggregator_handlers()** (9 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_warning_and_error_reach_aggregator_files()** (9 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **Queue** (9 connections)
- **DropOldestQueueHandler** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **create_formatter()** (8 connections) — `server/structured_logging/logging_file_categories.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_restore_root_handlers()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_root_handlers_snapshot()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_async_log_queue_is_bounded()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **SecurityConfig** (7 connections) — `server/config/models/security_logging.py`
- **get_queue_listener()** (7 connections) — `server/structured_logging/logging_file_setup.py`
- **stop_queue_listener()** (7 connections) — `server/structured_logging/logging_file_setup.py`
- *... and 79 more nodes in this community*

## Relationships

- [test_logging_utilities.py](test_logging_utilities.py.md) (15 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (9 shared connections)
- [test_enhanced_logging_config.py](test_enhanced_logging_config.py.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_logging_file_categories.py](test_logging_file_categories.py.md) (7 shared connections)
- [CORSConfig](CORSConfig.md) (6 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (3 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (2 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (2 shared connections)
- [safe_run_static](safe_run_static.md) (1 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (1 shared connections)

## Source Files

- `server/config/models/security_logging.py`
- `server/structured_logging/logging_file_categories.py`
- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`

## Audit Trail

- EXTRACTED: 245 (94%)
- INFERRED: 16 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*