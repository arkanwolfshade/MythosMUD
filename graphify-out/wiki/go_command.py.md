# go_command.py

> 33 nodes

## Key Concepts

- **go_command.py** (28 connections) — `server/commands/go_command.py`
- **handle_go_command()** (18 connections) — `server/commands/go_command.py`
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **_execute_movement()** (10 connections) — `server/commands/go_command.py`
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
- **test_validate_exit_no_exits()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_target_room_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **Go command for MythosMUD. This module handles the go command for player…** (1 connections) — `server/commands/go_command.py`
- **Validate that exit exists and target room is valid.** (1 connections) — `server/commands/go_command.py`
- **Resolve player_combat_service and event_bus from DI container or legacy…** (1 connections) — `server/commands/go_command.py`
- **Use container.movement_service when wired; else build MovementService (tests /…** (1 connections) — `server/commands/go_command.py`
- **Execute player movement using movement service.** (1 connections) — `server/commands/go_command.py`
- **Return normalized direction string, or None if missing (after logging).** (1 connections) — `server/commands/go_command.py`
- **Resolve ConnectionManager from DI container or legacy app.state.** (1 connections) — `server/commands/go_command.py`
- **If the player is resting, cancel rest and return an early client payload; else…** (1 connections) — `server/commands/go_command.py`
- *... and 8 more nodes in this community*

## Relationships

- [test_go_command.py](test_go_command.py.md) (29 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [MovementService](MovementService.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 102 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*