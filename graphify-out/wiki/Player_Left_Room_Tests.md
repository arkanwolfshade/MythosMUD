# Player Left Room Tests

> 77 nodes

## Key Concepts

- **test_go_command.py** (30 connections) — `server/tests/unit/commands/test_go_command.py`
- **go_command.py** (28 connections) — `server/commands/go_command.py`
- **handle_go_command()** (18 connections) — `server/commands/go_command.py`
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **_execute_movement()** (12 connections) — `server/commands/go_command.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
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
- *... and 52 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (7 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (5 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (3 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (2 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (1 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 271 (94%)
- INFERRED: 16 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*