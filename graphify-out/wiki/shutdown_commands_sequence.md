# shutdown commands sequence

> 49 nodes

## Key Concepts

- **test_shutdown_sequence.py** (26 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **shutdown_sequence.py** (17 connections) — `server/commands/shutdown_sequence.py`
- **execute_shutdown_sequence()** (15 connections) — `server/commands/shutdown_sequence.py`
- **_ShutdownAppState** (14 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **_ShutdownApp** (14 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **_persist_all_players()** (8 connections) — `server/commands/shutdown_sequence.py`
- **Any** (8 connections)
- **_despawn_all_npcs()** (7 connections) — `server/commands/shutdown_sequence.py`
- **_cancel_background_tasks()** (7 connections) — `server/commands/shutdown_sequence.py`
- **_disconnect_all_players()** (6 connections) — `server/commands/shutdown_sequence.py`
- **_stop_nats_message_handler()** (6 connections) — `server/commands/shutdown_sequence.py`
- **_disconnect_nats_service()** (6 connections) — `server/commands/shutdown_sequence.py`
- **_cleanup_connection_manager()** (6 connections) — `server/commands/shutdown_sequence.py`
- **test_persist_all_players_database_error_on_player()** (6 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_execute_shutdown_sequence_happy_path()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_persist_all_players_no_connection_manager()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_persist_all_players_player_not_found()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_despawn_all_npcs_via_app_state_fallback()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_despawn_all_npcs_no_services()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_disconnect_all_players_string_uuid()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_stop_nats_message_handler_missing()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_disconnect_nats_service_os_error()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_cleanup_connection_manager_missing()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_cancel_background_tasks_timeout()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **test_cancel_background_tasks_unregisters_shutdown_task()** (5 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- *... and 24 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (5 shared connections)
- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (3 shared connections)
- [health monitor realtime](health_monitor_realtime.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)

## Source Files

- `server/commands/shutdown_process_termination.py`
- `server/commands/shutdown_sequence.py`
- `server/tests/unit/commands/test_shutdown_sequence.py`

## Audit Trail

- EXTRACTED: 226 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*