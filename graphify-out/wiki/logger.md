# logger

> 84 nodes

## Key Concepts

- **logging_file_setup.py** (35 connections) — `server/structured_logging/logging_file_setup.py`
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_file_setup.py** (20 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_Handler** (13 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_setup_aggregator_handlers()** (10 connections) — `server/structured_logging/logging_file_setup.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **Queue** (9 connections)
- **DropOldestQueueHandler** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_restore_root_handlers()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_root_handlers_snapshot()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_queue_listener_has_aggregator_handlers()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_warning_and_error_reach_aggregator_files()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **LoggerNameFilter** (7 connections) — `server/structured_logging/logging_file_categories.py`
- **get_queue_listener()** (7 connections) — `server/structured_logging/logging_file_setup.py`
- **stop_queue_listener()** (7 connections) — `server/structured_logging/logging_file_setup.py`
- **test_async_log_queue_is_bounded()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_nats_message_handler_base.py** (7 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **add_handler_to_loggers()** (6 connections) — `server/structured_logging/logging_file_categories.py`
- **_get_handler_class()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_classes()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_or_create_log_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_async_logging_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **test_aggregator_handlers_on_root_when_async()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- *... and 59 more nodes in this community*

## Relationships

- [server structured logging logging utilities](server_structured_logging_logging_utilities.md) (9 shared connections)
- [formatter](formatter.md) (8 shared connections)
- [server structured logging logging handlers](server_structured_logging_logging_handlers.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (3 shared connections)
- [server structured logging windows safe](server_structured_logging_windows_safe.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [eventdict](eventdict.md) (1 shared connections)
- [logentry](logentry.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_categories.py`
- `server/structured_logging/logging_file_setup.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`

## Audit Trail

- EXTRACTED: 192 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*