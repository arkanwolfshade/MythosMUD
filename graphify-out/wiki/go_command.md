# go command

> 31 nodes

## Key Concepts

- **handle_go_command()** (19 connections) — `server/commands/go_command.py`
- **go_command.py** (15 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **_setup_go_command()** (12 connections) — `server/commands/go_command.py`
- **_execute_movement()** (10 connections) — `server/commands/go_command.py`
- **_validate_exit()** (9 connections) — `server/commands/go_command.py`
- **_movement_combat_and_event_bus_from_go_app()** (5 connections) — `server/commands/go_command.py`
- **_movement_service_for_go_command()** (5 connections) — `server/commands/go_command.py`
- **_cancel_rest_if_moving()** (5 connections) — `server/commands/go_command.py`
- **_resolve_async_persistence_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_canonical_room_id_for_go()** (4 connections) — `server/commands/go_command.py`
- **_resolved_direction_for_go_command()** (4 connections) — `server/commands/go_command.py`
- **_connection_manager_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **test_validate_exit_direction_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_invalid_posture()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **Go command for MythosMUD.  This module handles the go command for player movemen** (1 connections) — `server/commands/go_command.py`
- **Prefer container.async_persistence; fall back to app.state.persistence (legacy).** (1 connections) — `server/commands/go_command.py`
- **Return the room id to use for movement; log if player record disagrees with room** (1 connections) — `server/commands/go_command.py`
- **Setup and validate go command prerequisites.** (1 connections) — `server/commands/go_command.py`
- **Validate that exit exists and target room is valid.** (1 connections) — `server/commands/go_command.py`
- **Resolve player_combat_service and event_bus from DI container or legacy app.stat** (1 connections) — `server/commands/go_command.py`
- **Use container.movement_service when wired; else build MovementService (tests / p** (1 connections) — `server/commands/go_command.py`
- **Execute player movement using movement service.** (1 connections) — `server/commands/go_command.py`
- **Return normalized direction string, or None if missing (after logging).** (1 connections) — `server/commands/go_command.py`
- *... and 6 more nodes in this community*

## Relationships

- [Validate that player is in](Validate_that_player_is_in.md) (27 shared connections)
- [Any](Any.md) (3 shared connections)
- [Player](Player.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 130 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*