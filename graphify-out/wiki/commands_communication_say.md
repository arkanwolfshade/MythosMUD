# commands communication say

> 65 nodes

## Key Concepts

- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_communication_commands_support.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **handle_say_command()** (16 connections) — `server/commands/communication_commands.py`
- **communication_commands_support.py** (16 connections) — `server/commands/communication_commands_support.py`
- **handle_pose_command()** (13 connections) — `server/commands/communication_commands.py`
- **app_from_request()** (12 connections) — `server/commands/communication_commands_support.py`
- **get_pose_persistence()** (11 connections) — `server/commands/communication_commands_support.py`
- **AsyncPersistenceForPose** (6 connections) — `server/commands/communication_commands_support.py`
- **Protocol** (5 connections)
- **PlayerWithPose** (4 connections) — `server/commands/communication_commands_support.py`
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
- *... and 40 more nodes in this community*

## Relationships

- [commands communication flows](commands_communication_flows.md) (38 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (15 shared connections)
- [commands whisper command](commands_whisper_command.md) (13 shared connections)
- [commands communication channels](commands_communication_channels.md) (12 shared connections)
- [dialogue service game](dialogue_service_game.md) (5 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [inventory commands command](inventory_commands_command.md) (2 shared connections)
- [command helpers functions](command_helpers_functions.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 286 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*