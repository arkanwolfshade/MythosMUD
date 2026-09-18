# Community 349

> 48 nodes

## Key Concepts

- **test_shutdown_sequence.py** (26 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **shutdown_sequence.py** (17 connections) — `server/commands/shutdown_sequence.py`
- **execute_shutdown_sequence()** (15 connections) — `server/commands/shutdown_sequence.py`
- **_ShutdownApp** (13 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **_ShutdownAppState** (13 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- **asyncio** (12 connections)
- **_persist_all_players()** (8 connections) — `server/commands/shutdown_sequence.py`
- **Any** (8 connections)
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
- **test_persist_all_players_player_not_found()** (6 connections) — `server/tests/unit/commands/test_shutdown_sequence.py`
- *... and 23 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (8 shared connections)
- [Community 440](Community_440.md) (3 shared connections)
- [Community 628](Community_628.md) (2 shared connections)
- [Community 107](Community_107.md) (2 shared connections)

## Source Files

- `server/commands/shutdown_sequence.py`
- `server/tests/unit/commands/test_shutdown_sequence.py`

## Audit Trail

- EXTRACTED: 128 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*