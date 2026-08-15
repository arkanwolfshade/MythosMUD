# position_commands.py

> 41 nodes

## Key Concepts

- **position_commands.py** (26 connections) — `server/commands/position_commands.py`
- **_handle_position_change()** (12 connections) — `server/commands/position_commands.py`
- **test_position_commands.py** (12 connections) — `server/tests/unit/commands/test_position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **SupportsConnectionManager** (9 connections) — `server/services/player_position_service.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **SupportsPlayerPersistence** (8 connections) — `server/services/player_position_service.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- **_get_position_command_services()** (6 connections) — `server/commands/position_commands.py`
- **Request** (5 connections)
- **asyncio** (5 connections)
- **_RoomBroadcaster** (4 connections) — `server/commands/position_commands.py`
- **_broadcast_posture_change()** (4 connections) — `server/commands/position_commands.py`
- **_build_posture_change_event()** (4 connections) — `server/commands/position_commands.py`
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- **test_handle_ground_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_lie_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_sit_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_already_standing_still_sends_player_update()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_EventSequence** (3 connections) — `server/commands/position_commands.py`
- **.broadcast_to_room()** (3 connections) — `server/commands/position_commands.py`
- **.get_online_player_by_display_name()** (2 connections) — `server/services/player_position_service.py`
- **Protocol** (2 connections)
- **Protocol** (2 connections)
- *... and 16 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (10 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (3 shared connections)
- [_format_room_posture_message](_format_room_posture_message.md) (3 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [.change_position](change_position.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)

## Source Files

- `server/commands/position_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_position_commands.py`

## Audit Trail

- EXTRACTED: 103 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*