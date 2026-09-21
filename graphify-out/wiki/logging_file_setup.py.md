# logging_file_setup.py

> 77 nodes

## Key Concepts

- **logging_file_setup.py** (36 connections) — `server/structured_logging/logging_file_setup.py`
- **LoggingConfig** (29 connections) — `server/config/models/security_logging.py`
- **setup_enhanced_file_logging()** (21 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_file_setup.py** (21 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_Handler** (13 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_setup_aggregator_handlers()** (10 connections) — `server/structured_logging/logging_file_setup.py`
- **security_logging.py** (10 connections) — `server/config/models/security_logging.py`
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
- *... and 52 more nodes in this community*

## Relationships

- [logging_file_categories.py](logging_file_categories.py.md) (11 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [test_config_models.py](test_config_models.py.md) (7 shared connections)
- [test_enhanced_logging_config.py](test_enhanced_logging_config.py.md) (6 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (6 shared connections)
- [SecurityConfig](SecurityConfig.md) (5 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (3 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (2 shared connections)
- [safe_run_static](safe_run_static.md) (1 shared connections)
- [LogAggregator](LogAggregator.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/config/models/security_logging.py`
- `server/structured_logging/logging_file_setup.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`

## Audit Trail

- EXTRACTED: 204 (94%)
- INFERRED: 14 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*