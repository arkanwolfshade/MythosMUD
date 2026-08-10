# Error Logging Implementation

> 75 nodes

## Key Concepts

- **test_go_command.py** (30 connections) — `server/tests/unit/commands/test_go_command.py`
- **go_command.py** (28 connections) — `server/commands/go_command.py`
- **handle_go_command()** (18 connections) — `server/commands/go_command.py`
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **_execute_movement()** (12 connections) — `server/commands/go_command.py`
- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **_validate_exit()** (9 connections) — `server/commands/go_command.py`
- **_rest_interrupt_payload_if_moving()** (7 connections) — `server/commands/go_command.py`
- **_movement_combat_and_event_bus_from_go_app()** (6 connections) — `server/commands/go_command.py`
- **_movement_service_for_go_command()** (6 connections) — `server/commands/go_command.py`
- **_resolve_async_persistence_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_canonical_room_id_for_go()** (4 connections) — `server/commands/go_command.py`
- **_resolved_direction_for_go_command()** (4 connections) — `server/commands/go_command.py`
- **_connection_manager_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **test_validate_player_posture_get_stats_error()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_room_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_room_id_mismatch()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_standing()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_sitting()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_lying()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_no_get_stats()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- *... and 50 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (13 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)
- [Combat Client Crash Report](Combat_Client_Crash_Report.md) (2 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 267 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*