# Communication Command Handlers

> 71 nodes · cohesion 0.05

## Key Concepts

- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_communication_commands_channels.py** (19 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **handle_say_command()** (16 connections) — `server/commands/communication_commands.py`
- **handle_pose_command()** (13 connections) — `server/commands/communication_commands.py`
- **handle_global_command()** (11 connections) — `server/commands/communication_commands.py`
- **handle_local_command()** (10 connections) — `server/commands/communication_commands.py`
- **handle_reply_command()** (10 connections) — `server/commands/communication_commands.py`
- **handle_system_command()** (10 connections) — `server/commands/communication_commands.py`
- **AliasStorage** (9 connections) — `server/commands/communication_commands.py`
- **handle_me_command()** (7 connections) — `server/commands/communication_commands.py`
- **communication_commands_mocks.py** (5 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **Test handle_mute_global_command() successful execution.** (5 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **Test handle_local_command when services are not available.** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_say_command_exception()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_global_command_level_too_low()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_local_command_no_room()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_local_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_not_admin()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_pose_command_clear_pose()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_set_pose()** (4 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- *... and 46 more nodes in this community*

## Relationships

- [[Communication Command Flows]] (15 shared connections)
- [[Whisper Reply Command Tests]] (12 shared connections)
- [[Alias Expansion Logic]] (11 shared connections)
- [[Admin Status Commands]] (2 shared connections)
- [[Spellbook Read Command]] (2 shared connections)
- [[Command Helper Utilities]] (1 shared connections)
- [[Commands Npc Admin]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)
- [[Lucidity Recovery Commands]] (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_admin_commands.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 310 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
