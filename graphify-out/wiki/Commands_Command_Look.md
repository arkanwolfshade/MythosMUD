# Commands Command Look

> 75 nodes · cohesion 0.04

## Key Concepts

- **test_go_command.py** (30 connections) — `server/tests/unit/commands/test_go_command.py`
- **go_command.py** (28 connections) — `server/commands/go_command.py`
- **handle_go_command()** (18 connections) — `server/commands/go_command.py`
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **_execute_movement()** (12 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **_validate_exit()** (9 connections) — `server/commands/go_command.py`
- **_rest_interrupt_payload_if_moving()** (7 connections) — `server/commands/go_command.py`
- **_movement_combat_and_event_bus_from_go_app()** (6 connections) — `server/commands/go_command.py`
- **_movement_service_for_go_command()** (6 connections) — `server/commands/go_command.py`
- **_canonical_room_id_for_go()** (4 connections) — `server/commands/go_command.py`
- **_connection_manager_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolve_async_persistence_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolved_direction_for_go_command()** (4 connections) — `server/commands/go_command.py`
- **test_validate_player_posture_get_stats_error()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_error_handling()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_failure()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_fallback_service()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_invalid_posture()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_no_direction()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_no_exit()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_setup_failure()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- *... and 50 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (6 shared connections)
- [Commands Rest Countdown](Commands_Rest_Countdown.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (2 shared connections)
- [Player Movement Service](Player_Movement_Service.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 267 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*