# logging_file_setup.py

> 82 nodes

## Key Concepts

- **logging_file_setup.py** (36 connections) — `server/structured_logging/logging_file_setup.py`
- **setup_enhanced_file_logging()** (21 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_file_setup.py** (21 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_Handler** (13 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **add_handler_to_loggers()** (10 connections) — `server/structured_logging/logging_file_categories.py`
- **_setup_aggregator_handlers()** (10 connections) — `server/structured_logging/logging_file_setup.py`
- **LoggerNameFilter** (9 connections) — `server/structured_logging/logging_file_categories.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **test_queue_listener_has_aggregator_handlers()** (9 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_warning_and_error_reach_aggregator_files()** (9 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **Queue** (9 connections)
- **DropOldestQueueHandler** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_restore_root_handlers()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_root_handlers_snapshot()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_async_log_queue_is_bounded()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **get_queue_listener()** (7 connections) — `server/structured_logging/logging_file_setup.py`
- **stop_queue_listener()** (7 connections) — `server/structured_logging/logging_file_setup.py`
- **test_aggregator_handlers_on_root_when_async()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_log_directory_under_env()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_get_handler_class()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_classes()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_or_create_log_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_async_logging_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- *... and 57 more nodes in this community*

## Relationships

- [LoggingConfig](LoggingConfig.md) (13 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (9 shared connections)
- [logging_file_categories.py](logging_file_categories.py.md) (8 shared connections)
- [test_logging_file_categories.py](test_logging_file_categories.py.md) (6 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (6 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (2 shared connections)
- [safe_run_static](safe_run_static.md) (1 shared connections)
- [LogAggregator](LogAggregator.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_categories.py`
- `server/structured_logging/logging_file_setup.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`

## Audit Trail

- EXTRACTED: 198 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*