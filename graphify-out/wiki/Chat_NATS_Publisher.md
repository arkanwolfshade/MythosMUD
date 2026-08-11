# Chat NATS Publisher

> 117 nodes

## Key Concepts

- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **handle_whisper_command()** (21 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_channels.py** (20 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **handle_say_command()** (17 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_whisper_reply.py** (17 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **test_whisper_command.py** (13 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **handle_global_command()** (12 connections) — `server/commands/communication_commands.py`
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
- *... and 92 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (41 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (3 shared connections)
- [Schedule Service Loader](Schedule_Service_Loader.md) (2 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- `server/tests/unit/commands/test_whisper_command.py`

## Audit Trail

- EXTRACTED: 389 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*