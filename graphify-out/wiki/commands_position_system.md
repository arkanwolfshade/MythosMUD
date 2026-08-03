# commands position system

> 136 nodes

## Key Concepts

- **command_service.py** (95 connections) — `server/commands/command_service.py`
- **alias_storage.py** (67 connections) — `server/alias_storage.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **position_commands.py** (19 connections) — `server/commands/position_commands.py`
- **handle_follow_command()** (18 connections) — `server/commands/follow_commands.py`
- **follow_commands.py** (15 connections) — `server/commands/follow_commands.py`
- **get_help_content()** (15 connections) — `server/help/help_content.py`
- **handle_pose_command()** (13 connections) — `server/commands/communication_commands.py`
- **handle_inventory_command()** (13 connections) — `server/commands/inventory_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **test_position_commands.py** (11 connections) — `server/tests/unit/commands/test_position_commands.py`
- **handle_unfollow_command()** (10 connections) — `server/commands/follow_commands.py`
- **handle_following_command()** (10 connections) — `server/commands/follow_commands.py`
- **_format_room_posture_message()** (10 connections) — `server/commands/position_commands.py`
- **handle_system_command()** (10 connections) — `server/commands/system_commands.py`
- **handle_stand_command()** (9 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- *... and 111 more nodes in this community*

## Relationships

- [commands npc admin](commands_npc_admin.md) (25 shared connections)
- [models npc rationale](models_npc_rationale.md) (22 shared connections)
- [commands whisper command](commands_whisper_command.md) (18 shared connections)
- [commands admin mute](commands_admin_mute.md) (13 shared connections)
- [NPC Combat](NPC_Combat.md) (13 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (9 shared connections)
- [inventory commands command](inventory_commands_command.md) (8 shared connections)
- [command helpers functions](command_helpers_functions.md) (8 shared connections)
- [realtime real time](realtime_real_time.md) (7 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (7 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (6 shared connections)
- [commands inventory put](commands_inventory_put.md) (5 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/__init__.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/follow_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/commands/test_follow_commands.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/commands/test_system_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 693 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*