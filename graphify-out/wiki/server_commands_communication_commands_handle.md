# server commands communication commands handle

> 76 nodes

## Key Concepts

- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (23 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_communication_commands_channels.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **handle_say_command()** (16 connections) — `server/commands/communication_commands.py`
- **asyncio** (15 connections)
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **asyncio** (13 connections)
- **handle_global_command()** (11 connections) — `server/commands/communication_commands.py`
- **handle_local_command()** (10 connections) — `server/commands/communication_commands.py`
- **handle_system_command()** (10 connections) — `server/commands/communication_commands.py`
- **handle_me_command()** (7 connections) — `server/commands/communication_commands.py`
- **test_handle_global_command_level_too_low()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_success()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_local_command_no_room()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_local_command_success()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_not_admin()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_success()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_pose_command_clear_pose()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_set_pose()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_chat_service_failure()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_delegates_broadcast_to_chat_service_with_ids()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_exception()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_player_id()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- *... and 51 more nodes in this community*

## Relationships

- [server commands communication commands](server_commands_communication_commands.md) (15 shared connections)
- [server commands communication commands handle](server_commands_communication_commands_handle.md) (8 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (7 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (6 shared connections)
- [server commands alias commands](server_commands_alias_commands.md) (3 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`

## Audit Trail

- EXTRACTED: 182 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*