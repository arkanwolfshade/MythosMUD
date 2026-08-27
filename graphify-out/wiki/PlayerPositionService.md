# PlayerPositionService

> 181 nodes

## Key Concepts

- **PlayerPositionService** (48 connections) — `server/services/player_position_service.py`
- **test_rest_command.py** (41 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (28 connections) — `server/commands/rest_command.py`
- **test_player_position_service.py** (28 connections) — `server/tests/unit/services/test_player_position_service.py`
- **cancel_rest_countdown()** (25 connections) — `server/commands/rest_command.py`
- **asyncio** (22 connections)
- **handle_rest_command()** (21 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (19 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **Any** (12 connections)
- **asyncio** (12 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **UUID** (10 connections)
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **Player** (8 connections)
- **MockPersistence** (7 connections) — `server/tests/unit/commands/test_rest_command.py`
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_stand_after_cancelled_rest()** (6 connections) — `server/commands/rest_command.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- *... and 156 more nodes in this community*

## Relationships

- [rescue_commands.py](rescue_commands.py.md) (9 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (9 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [test_go_command.py](test_go_command.py.md) (5 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (5 shared connections)
- [combat_service.py](combat_service.py.md) (5 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (4 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (4 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_rest_command.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 374 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*