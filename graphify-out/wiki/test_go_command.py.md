# test_go_command.py

> 84 nodes

## Key Concepts

- **test_go_command.py** (33 connections) — `server/tests/unit/commands/test_go_command.py`
- **go_command.py** (30 connections) — `server/commands/go_command.py`
- **handle_go_command()** (21 connections) — `server/commands/go_command.py`
- **asyncio** (16 connections)
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **_execute_movement()** (10 connections) — `server/commands/go_command.py`
- **_validate_exit()** (10 connections) — `server/commands/go_command.py`
- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **_cancel_rest_if_moving()** (7 connections) — `server/commands/go_command.py`
- **_movement_combat_and_event_bus_from_go_app()** (6 connections) — `server/commands/go_command.py`
- **_movement_service_for_go_command()** (6 connections) — `server/commands/go_command.py`
- **_canonical_room_id_for_go()** (4 connections) — `server/commands/go_command.py`
- **_connection_manager_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolve_async_persistence_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolved_direction_for_go_command()** (4 connections) — `server/commands/go_command.py`
- **test_execute_movement_error_handling()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_failure()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_fallback_service()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_success()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_invalid_posture()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_no_direction()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_no_exit()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_rest_interrupt_still_moves()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- *... and 59 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (3 shared connections)
- [talk_command.py](talk_command.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [command_service.py](command_service.py.md) (3 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (3 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [look_command.py](look_command.py.md) (2 shared connections)
- [handle_explore_command](handle_explore_command.md) (2 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)

## Source Files

- `server/commands/exploration_commands.py`
- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 180 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*