# commands command rationale

> 79 nodes

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
- **_cancel_rest_if_moving()** (7 connections) — `server/commands/go_command.py`
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
- *... and 54 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [rest grace period](rest_grace_period.md) (5 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [commands party examples](commands_party_examples.md) (3 shared connections)
- [event connection helpers](event_connection_helpers.md) (2 shared connections)
- [connection realtime statistics](connection_realtime_statistics.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [player cache rationale](player_cache_rationale.md) (2 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/exploration_commands.py`
- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 287 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*