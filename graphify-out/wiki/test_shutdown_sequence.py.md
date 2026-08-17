# test_shutdown_sequence.py

> 50 nodes

## Key Concepts

- **test_shutdown_sequence.py** (27 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **shutdown_sequence.py** (17 connections) — `server/commands/shutdown_sequence.py`
- **execute_shutdown_sequence()** (15 connections) — `server/commands/shutdown_sequence.py`
- **_ShutdownApp** (13 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **_ShutdownAppState** (13 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **asyncio** (12 connections)
- **_persist_all_players()** (8 connections) — `server/commands/shutdown_sequence.py`
- **Any** (8 connections)
- **schedule_process_termination()** (7 connections) — `server/commands/shutdown_process_termination.py`
- **_cancel_background_tasks()** (7 connections) — `server/commands/shutdown_sequence.py`
- **_despawn_all_npcs()** (7 connections) — `server/commands/shutdown_sequence.py`
- **test_despawn_all_npcs_via_app_state_fallback()** (7 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_execute_shutdown_sequence_happy_path()** (7 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_persist_all_players_database_error_on_player()** (7 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **_cleanup_connection_manager()** (6 connections) — `server/commands/shutdown_sequence.py`
- **_disconnect_all_players()** (6 connections) — `server/commands/shutdown_sequence.py`
- **_disconnect_nats_service()** (6 connections) — `server/commands/shutdown_sequence.py`
- **_stop_nats_message_handler()** (6 connections) — `server/commands/shutdown_sequence.py`
- **test_cancel_background_tasks_timeout()** (6 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_cancel_background_tasks_unregisters_shutdown_task()** (6 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_cleanup_connection_manager_missing()** (6 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_despawn_all_npcs_no_services()** (6 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_disconnect_all_players_string_uuid()** (6 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_disconnect_nats_service_os_error()** (6 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_persist_all_players_no_connection_manager()** (6 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- *... and 25 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [test_shutdown_process_termination.py](test_shutdown_process_termination.py.md) (3 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/shutdown_process_termination.py`
- `server/commands/shutdown_sequence.py`
- `server/tests/unit/commands/test_shutdown_sequence.py`

## Audit Trail

- EXTRACTED: 134 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*