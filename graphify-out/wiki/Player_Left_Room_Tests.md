# Player Left Room Tests

> 88 nodes

## Key Concepts

- **test_go_command.py** (30 connections) — `server/tests/unit/commands/test_go_command.py`
- **go_command.py** (28 connections) — `server/commands/go_command.py`
- **handle_go_command()** (18 connections) — `server/commands/go_command.py`
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **_execute_movement()** (12 connections) — `server/commands/go_command.py`
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **_validate_exit()** (9 connections) — `server/commands/go_command.py`
- **handle_explore_command()** (8 connections) — `server/commands/exploration_commands.py`
- **handle_look_command()** (8 connections) — `server/commands/look_command.py`
- **_rest_interrupt_payload_if_moving()** (7 connections) — `server/commands/go_command.py`
- **_movement_combat_and_event_bus_from_go_app()** (6 connections) — `server/commands/go_command.py`
- **_movement_service_for_go_command()** (6 connections) — `server/commands/go_command.py`
- **test_exploration_commands.py** (5 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **_resolve_async_persistence_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_canonical_room_id_for_go()** (4 connections) — `server/commands/go_command.py`
- **_resolved_direction_for_go_command()** (4 connections) — `server/commands/go_command.py`
- **_connection_manager_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **test_validate_player_posture_get_stats_error()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_explore_command()** (3 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_handle_explore_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_setup_go_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_room_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- *... and 63 more nodes in this community*

## Relationships

- [Player Schema Converter](Player_Schema_Converter.md) (7 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (5 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (5 shared connections)
- [Container Open Events](Container_Open_Events.md) (4 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (1 shared connections)

## Source Files

- `server/commands/exploration_commands.py`
- `server/commands/go_command.py`
- `server/commands/look_command.py`
- `server/tests/unit/commands/test_exploration_commands.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 310 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*