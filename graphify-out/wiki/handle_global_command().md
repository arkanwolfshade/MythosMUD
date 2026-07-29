# handle global command()

> 67 nodes

## Key Concepts

- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_communication_commands_channels.py** (20 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **handle_say_command()** (17 connections) — `server/commands/communication_commands.py`
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **handle_global_command()** (12 connections) — `server/commands/communication_commands.py`
- **handle_local_command()** (11 connections) — `server/commands/communication_commands.py`
- **communication_commands_mocks.py** (5 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_handle_local_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_level_too_low()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_not_admin()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_local_command_no_room()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_say_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_delegates_broadcast_to_chat_service_with_ids()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_clear_pose()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_set_pose()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_room()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_player_id()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_chat_service_failure()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_exception()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- *... and 42 more nodes in this community*

## Relationships

- [Any](Any.md) (22 shared connections)
- [handle reply command()](handle_reply_command%28%29.md) (8 shared connections)
- [communication commands](communication_commands.md) (6 shared connections)
- [chat send with room bundle()](chat_send_with_room_bundle%28%29.md) (3 shared connections)
- [communication commands support](communication_commands_support.md) (2 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`

## Audit Trail

- EXTRACTED: 261 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*