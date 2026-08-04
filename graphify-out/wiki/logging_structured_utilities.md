# logging structured utilities

> 165 nodes

## Key Concepts

- **test_logging_utilities.py** (40 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **logging_file_setup.py** (35 connections) — `server/structured_logging/logging_file_setup.py`
- **ensure_log_directory()** (23 connections) — `server/structured_logging/logging_utilities.py`
- **Path** (23 connections)
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **logging_utilities.py** (18 connections) — `server/structured_logging/logging_utilities.py`
- **rotate_log_files()** (18 connections) — `server/structured_logging/logging_utilities.py`
- **test_logging_file_setup.py** (14 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **resolve_log_base()** (13 connections) — `server/structured_logging/logging_utilities.py`
- **load_player_guid_formatter_class()** (11 connections) — `server/structured_logging/logging_utilities.py`
- **_Handler** (11 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_setup_aggregator_handlers()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **LoggerNameFilter** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_handler_for_category()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **Queue** (7 connections)
- **test_queue_listener_has_aggregator_handlers()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_warning_and_error_reach_aggregator_files()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **get_queue_listener()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **stop_queue_listener()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_CategoryHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_ConsoleHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_async_logging_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- *... and 140 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (25 shared connections)
- [logging handlers structured](logging_handlers_structured.md) (16 shared connections)
- [player guid formatter](player_guid_formatter.md) (5 shared connections)
- [windows safe rotation](windows_safe_rotation.md) (4 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (2 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (2 shared connections)
- [validator room toolkit](validator_room_toolkit.md) (2 shared connections)
- [scripts run guard](scripts_run_guard.md) (1 shared connections)
- [log structured logging](log_structured_logging.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`
- `server/tests/unit/structured_logging/test_logging_utilities.py`

## Audit Trail

- EXTRACTED: 616 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*