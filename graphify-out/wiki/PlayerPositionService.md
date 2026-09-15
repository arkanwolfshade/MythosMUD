# PlayerPositionService

> 104 nodes

## Key Concepts

- **PlayerPositionService** (50 connections) — `server/services/player_position_service.py`
- **rest_command.py** (31 connections) — `server/commands/rest_command.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **is_player_resting()** (19 connections) — `server/commands/rest_command.py`
- **player_position_service.py** (18 connections) — `server/services/player_position_service.py`
- **PositionPlayer** (13 connections) — `server/services/player_position_service.py`
- **_start_rest_countdown()** (13 connections) — `server/commands/rest_command.py`
- **Any** (13 connections)
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **asyncio** (12 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **UUID** (11 connections)
- **_begin_seated_rest_countdown()** (10 connections) — `server/commands/rest_command.py`
- **_stand_after_cancelled_rest()** (8 connections) — `server/commands/rest_command.py`
- **_disconnect_player_intentionally()** (7 connections) — `server/commands/rest_command.py`
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_delayed_disconnect_player_intentionally()** (5 connections) — `server/commands/rest_command.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (5 connections) — `server/services/player_position_service.py`
- **._load_player_stats()** (5 connections) — `server/services/player_position_service.py`
- **test_change_position_database_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_save_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **._get_player_for_position_change()** (4 connections) — `server/services/player_position_service.py`
- *... and 79 more nodes in this community*

## Relationships

- [test_rest_command.py](test_rest_command.py.md) (26 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [command_service.py](command_service.py.md) (10 shared connections)
- [FollowService](FollowService.md) (7 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (6 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [test_go_command.py](test_go_command.py.md) (3 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (3 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [InstanceManager](InstanceManager.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)

## Source Files

- `server/commands/rest_command.py`
- `server/services/player_position_service.py`
- `server/services/position_messages.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 250 (93%)
- INFERRED: 19 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*