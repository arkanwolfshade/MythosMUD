# server commands position commands

> 56 nodes

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
- *... and 31 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (6 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (5 shared connections)
- [server commands alias commands](server_commands_alias_commands.md) (4 shared connections)
- [server commands rest command](server_commands_rest_command.md) (3 shared connections)
- [scripts add flavor text column](scripts_add_flavor_text_column.md) (3 shared connections)
- [server services player position service](server_services_player_position_service.md) (2 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (2 shared connections)
- [aliasrecord](aliasrecord.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

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