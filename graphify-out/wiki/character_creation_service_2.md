# character creation service

> 41 nodes

## Key Concepts

- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **handle_say_command()** (16 connections) — `server/commands/communication_commands.py`
- **handle_pose_command()** (13 connections) — `server/commands/communication_commands.py`
- **handle_me_command()** (7 connections) — `server/commands/communication_commands.py`
- **communication_commands_mocks.py** (5 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
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
- **test_handle_say_command_no_message()** (3 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_services()** (3 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_me_command_no_action()** (3 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_me_command_success()** (3 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Room-wide say; returns user-facing result dict.** (1 connections) — `server/commands/communication_commands.py`
- **Set or clear persistent pose text.** (1 connections) — `server/commands/communication_commands.py`
- **Shared mock wiring for communication command unit tests.** (1 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **Return (request, container) with request.app.state.container wired.      Typed M** (1 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- *... and 16 more nodes in this community*

## Relationships

- [message broadcast realtime](message_broadcast_realtime.md) (9 shared connections)
- [commands whisper command](commands_whisper_command.md) (8 shared connections)
- [character creation service](character_creation_service.md) (6 shared connections)
- [commands communication flows](commands_communication_flows.md) (6 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [npc combat service](npc_combat_service.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`

## Audit Trail

- EXTRACTED: 165 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*