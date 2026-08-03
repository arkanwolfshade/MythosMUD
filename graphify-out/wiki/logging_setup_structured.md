# logging setup structured

> 69 nodes

## Key Concepts

- **logging_file_setup.py** (35 connections) — `server/structured_logging/logging_file_setup.py`
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_file_setup.py** (14 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_Handler** (11 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_setup_aggregator_handlers()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **LoggerNameFilter** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_handler_for_category()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **Queue** (7 connections)
- **test_queue_listener_has_aggregator_handlers()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_warning_and_error_reach_aggregator_files()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **get_queue_listener()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **stop_queue_listener()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_CategoryHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_async_logging_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **test_nats_message_handler_base.py** (6 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_root_handlers_snapshot()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_restore_root_handlers()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_aggregator_handlers_on_root_when_async()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_get_or_create_log_queue()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_class()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_add_handler_to_loggers()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_classes()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **test_log_directory_under_env()** (5 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **LogRecord** (3 connections)
- *... and 44 more nodes in this community*

## Relationships

- [logging structured utilities](logging_structured_utilities.md) (10 shared connections)
- [manager subject services](manager_subject_services.md) (9 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [logging handlers structured](logging_handlers_structured.md) (7 shared connections)
- [windows safe rotation](windows_safe_rotation.md) (3 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (3 shared connections)
- [log structured logging](log_structured_logging.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`

## Audit Trail

- EXTRACTED: 266 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*