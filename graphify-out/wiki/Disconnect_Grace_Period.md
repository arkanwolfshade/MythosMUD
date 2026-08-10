# Disconnect Grace Period

> 36 nodes

## Key Concepts

- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
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
- **test_handle_reply_command_no_last_whisper_sender()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_say_command_no_message()** (3 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_services()** (3 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_me_command_no_action()** (3 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_me_command_success()** (3 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Return (request, container) with request.app.state.container wired.      Typed M** (1 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **Unit tests for say, me, and pose communication command handlers.** (1 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Test handle_say_command with no message.** (1 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Test handle_say_command when services are not available.** (1 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Test handle_say_command when player is not found.** (1 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Test handle_say_command successful execution.** (1 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Room say must call chat_service.send_say_message(player_id, message) for broadca** (1 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- *... and 11 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (28 shared connections)
- [Caching Lru Cache](Caching_Lru_Cache.md) (7 shared connections)
- [E 2 E Execution Guards](E_2_E_Execution_Guards.md) (1 shared connections)
- [E 2 E Scenario Template](E_2_E_Scenario_Template.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`

## Audit Trail

- EXTRACTED: 127 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*