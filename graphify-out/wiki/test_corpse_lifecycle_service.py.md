# test_corpse_lifecycle_service.py

> 70 nodes

## Key Concepts

- **logging_file_setup.py** (29 connections) — `server/structured_logging/logging_file_setup.py`
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_file_setup.py** (20 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_setup_aggregator_handlers()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **Queue** (9 connections)
- **DropOldestQueueHandler** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_restore_root_handlers()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_root_handlers_snapshot()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_queue_listener_has_aggregator_handlers()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_warning_and_error_reach_aggregator_files()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **get_queue_listener()** (7 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (7 connections) — `server/structured_logging/logging_file_setup.py`
- **stop_queue_listener()** (7 connections) — `server/structured_logging/logging_file_setup.py`
- **test_async_log_queue_is_bounded()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_get_or_create_log_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_prepare_log_environment()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_async_logging_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **test_aggregator_handlers_on_root_when_async()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_log_directory_under_env()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_get_handler_class()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_new_log_queue()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **LogRecord** (5 connections)
- **Path** (5 connections)
- **_CategoryHandlerConfig** (4 connections) — `server/structured_logging/logging_file_setup.py`
- *... and 45 more nodes in this community*

## Relationships

- [performance.test.tsx](performance.test.tsx.md) (9 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (7 shared connections)
- [CombatConfiguration](CombatConfiguration.md) (2 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`

## Audit Trail

- EXTRACTED: 155 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*