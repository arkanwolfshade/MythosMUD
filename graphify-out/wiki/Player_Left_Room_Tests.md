# Player Left Room Tests

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

- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Player State Factories](Player_State_Factories.md) (5 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (2 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (2 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (2 shared connections)
- [Room Map Viewer UI](Room_Map_Viewer_UI.md) (2 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (2 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (1 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (1 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 267 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*