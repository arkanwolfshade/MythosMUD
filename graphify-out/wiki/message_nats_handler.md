# message nats handler

> 37 nodes

## Key Concepts

- **test_communication_commands_say_me_pose.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **handle_say_command()** (16 connections) — `server/commands/communication_commands.py`
- **handle_pose_command()** (13 connections) — `server/commands/communication_commands.py`
- **handle_me_command()** (7 connections) — `server/commands/communication_commands.py`
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
- **Unit tests for say, me, and pose communication command handlers.** (1 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Test handle_say_command with no message.** (1 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Test handle_say_command when services are not available.** (1 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **Test handle_say_command when player is not found.** (1 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- *... and 12 more nodes in this community*

## Relationships

- [commands whisper command](commands_whisper_command.md) (12 shared connections)
- [commands communication flows](commands_communication_flows.md) (5 shared connections)
- [commands party examples](commands_party_examples.md) (3 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (3 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [rate limiter services](rate_limiter_services.md) (2 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`

## Audit Trail

- EXTRACTED: 130 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*