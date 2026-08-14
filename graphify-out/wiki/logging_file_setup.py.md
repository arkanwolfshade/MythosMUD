# logging_file_setup.py

> 80 nodes

## Key Concepts

- **logging_file_setup.py** (35 connections) — `server/structured_logging/logging_file_setup.py`
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **SafeRotatingFileHandler** (18 connections) — `server/structured_logging/logging_handlers.py`
- **test_logging_file_setup.py** (14 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_Handler** (11 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **load_player_guid_formatter_class()** (10 connections) — `server/structured_logging/logging_utilities.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_aggregator_handlers()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **LoggerNameFilter** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_handler_for_category()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **test_queue_listener_has_aggregator_handlers()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_warning_and_error_reach_aggregator_files()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_CategoryHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_ConsoleHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_formatter()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **get_queue_listener()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **stop_queue_listener()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_restore_root_handlers()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_root_handlers_snapshot()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_aggregator_handlers_on_root_when_async()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **Queue** (6 connections)
- **test_nats_message_handler_base.py** (6 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_add_handler_to_loggers()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- *... and 55 more nodes in this community*

## Relationships

- [test_logging_handlers.py](test_logging_handlers.py.md) (15 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (11 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (5 shared connections)
- [._open](_open.md) (2 shared connections)
- [NATSMessageHandlerMixinBase](NATSMessageHandlerMixinBase.md) (2 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (2 shared connections)
- [default_log_config](default_log_config.md) (2 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [safe_run_static](safe_run_static.md) (1 shared connections)
- [LogAggregator](LogAggregator.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_handlers.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`

## Audit Trail

- EXTRACTED: 180 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*