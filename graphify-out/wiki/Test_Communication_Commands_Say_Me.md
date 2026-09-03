# Test Communication Commands Say Me

> 92 nodes

## Key Concepts

- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (23 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **handle_whisper_command()** (19 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_whisper_reply.py** (18 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **handle_say_command()** (15 connections) — `server/commands/communication_commands.py`
- **asyncio** (15 connections)
- **test_whisper_command.py** (14 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **handle_pose_command()** (13 connections) — `server/commands/communication_commands.py`
- **asyncio** (11 connections)
- **handle_reply_command()** (9 connections) — `server/commands/communication_commands.py`
- **asyncio** (7 connections)
- **handle_me_command()** (6 connections) — `server/commands/communication_commands.py`
- **test_handle_pose_command_clear_pose()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_set_pose()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_chat_service_failure()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_delegates_broadcast_to_chat_service_with_ids()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_exception()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_player_id()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_room()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_success()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_reply_command_no_last_whisper_sender()** (5 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_reply_command_success()** (5 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_chat_service_failure()** (5 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- *... and 67 more nodes in this community*

## Relationships

- [Test Communication Commands Flows](Test_Communication_Commands_Flows.md) (23 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (5 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (3 shared connections)
- [Test Rescue Commands](Test_Rescue_Commands.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- `server/tests/unit/commands/test_whisper_command.py`

## Audit Trail

- EXTRACTED: 209 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*