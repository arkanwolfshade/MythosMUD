# Validate that player is in

> 88 nodes

## Key Concepts

- **test_go_command.py** (31 connections) — `server/tests/unit/commands/test_go_command.py`
- **go_command.py** (28 connections) — `server/commands/go_command.py`
- **handle_go_command()** (19 connections) — `server/commands/go_command.py`
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **_execute_movement()** (12 connections) — `server/commands/go_command.py`
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **_validate_exit()** (9 connections) — `server/commands/go_command.py`
- **handle_explore_command()** (8 connections) — `server/commands/exploration_commands.py`
- **_cancel_rest_if_moving()** (7 connections) — `server/commands/go_command.py`
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
- **test_setup_go_command_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- *... and 63 more nodes in this community*

## Relationships

- [Any](Any.md) (6 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (5 shared connections)
- [real time](real_time.md) (5 shared connections)
- [Player Position Service](Player_Position_Service.md) (3 shared connections)
- [look helpers](look_helpers.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [handle global command()](handle_global_command%28%29.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (1 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)
- [Test check all command blocks](Test_check_all_command_blocks.md) (1 shared connections)

## Source Files

- `server/commands/exploration_commands.py`
- `server/commands/go_command.py`
- `server/tests/unit/commands/test_exploration_commands.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 308 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*