# position_commands.py

> 32 nodes

## Key Concepts

- **position_commands.py** (21 connections) — `server/commands/position_commands.py`
- **test_position_commands.py** (13 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **SupportsPlayerPersistence** (8 connections) — `server/services/player_position_service.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- **SupportsConnectionManager** (7 connections) — `server/services/player_position_service.py`
- **_get_position_command_services()** (6 connections) — `server/commands/position_commands.py`
- **Request** (5 connections)
- **asyncio** (5 connections)
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- **test_handle_ground_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_lie_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_sit_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_already_standing_still_sends_player_update()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **.save_player()** (3 connections) — `server/services/player_position_service.py`
- **Protocol** (3 connections)
- **.get_online_player_by_display_name()** (1 connections) — `server/services/player_position_service.py`
- **Command handlers for posture adjustments within MythosMUD. According to…** (1 connections) — `server/commands/position_commands.py`
- **Handle /stand command.** (1 connections) — `server/commands/position_commands.py`
- **Handle /lie command (accepts optional 'down').** (1 connections) — `server/commands/position_commands.py`
- **Shared entry point for posture-changing commands.** (1 connections) — `server/commands/position_commands.py`
- **Persistence surface required for posture updates.** (1 connections) — `server/services/player_position_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [FollowService](FollowService.md) (9 shared connections)
- [command_service.py](command_service.py.md) (8 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [.state](state.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [User](User.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/position_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_position_commands.py`

## Audit Trail

- EXTRACTED: 89 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*