# position_commands.py

> 57 nodes

## Key Concepts

- **position_commands.py** (27 connections) — `server/commands/position_commands.py`
- **test_position_commands.py** (13 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_handle_position_change()** (12 connections) — `server/commands/position_commands.py`
- **_format_room_posture_message()** (10 connections) — `server/commands/position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **SupportsConnectionManager** (9 connections) — `server/services/player_position_service.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
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
- **test_format_room_posture_message_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- *... and 32 more nodes in this community*

## Relationships

- [PlayerPositionService](PlayerPositionService.md) (8 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [.state](state.md) (4 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)

## Source Files

- `server/commands/position_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`

## Audit Trail

- EXTRACTED: 126 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*