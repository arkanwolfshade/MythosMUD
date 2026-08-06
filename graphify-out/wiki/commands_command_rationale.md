# commands command rationale

> 88 nodes

## Key Concepts

- **test_go_command.py** (31 connections) — `server/tests/unit/commands/test_go_command.py`
- **go_command.py** (29 connections) — `server/commands/go_command.py`
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

- [rest grace period](rest_grace_period.md) (5 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (5 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (2 shared connections)
- [realtime real time](realtime_real_time.md) (2 shared connections)
- [connection realtime statistics](connection_realtime_statistics.md) (2 shared connections)
- [add used user](add_used_user.md) (2 shared connections)
- [dialogue service game](dialogue_service_game.md) (2 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/exploration_commands.py`
- `server/commands/go_command.py`
- `server/tests/unit/commands/test_exploration_commands.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 310 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*