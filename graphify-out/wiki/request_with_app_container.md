# request_with_app_container

> 42 nodes

## Key Concepts

- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (23 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **handle_say_command()** (16 connections) — `server/commands/communication_commands.py`
- **asyncio** (15 connections)
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **handle_me_command()** (7 connections) — `server/commands/communication_commands.py`
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
- **communication_commands_mocks.py** (5 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_handle_me_command_no_action()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_me_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_message()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_no_services()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Room-wide say; returns user-facing result dict.** (1 connections) — `server/commands/communication_commands.py`
- **Set or clear persistent pose text.** (1 connections) — `server/commands/communication_commands.py`
- **Shared mock wiring for communication command unit tests.** (1 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- *... and 17 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (10 shared connections)
- [test_communication_commands_channels.py](test_communication_commands_channels.py.md) (9 shared connections)
- [handle_whisper_command](handle_whisper_command.md) (8 shared connections)
- [communication_commands_flows.py](communication_commands_flows.py.md) (7 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`

## Audit Trail

- EXTRACTED: 112 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*