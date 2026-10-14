# PlayerPositionService

> 112 nodes

## Key Concepts

- **PlayerPositionService** (50 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **position_commands.py** (20 connections) — `server/commands/position_commands.py`
- **player_position_service.py** (18 connections) — `server/services/player_position_service.py`
- **asyncio** (17 connections)
- **PositionPlayer** (13 connections) — `server/services/player_position_service.py`
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **test_position_commands.py** (12 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **SupportsPlayerPersistence** (8 connections) — `server/services/player_position_service.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- **SupportsConnectionManager** (7 connections) — `server/services/player_position_service.py`
- **_get_position_command_services()** (7 connections) — `server/commands/position_commands.py`
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (5 connections) — `server/services/player_position_service.py`
- **._load_player_stats()** (5 connections) — `server/services/player_position_service.py`
- **test_change_position_database_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_save_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **asyncio** (5 connections)
- **._get_player_for_position_change()** (4 connections) — `server/services/player_position_service.py`
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- **._initial_response()** (4 connections) — `server/services/player_position_service.py`
- *... and 87 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [FollowService](FollowService.md) (7 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (4 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (2 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `server/commands/position_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 228 (90%)
- INFERRED: 26 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*