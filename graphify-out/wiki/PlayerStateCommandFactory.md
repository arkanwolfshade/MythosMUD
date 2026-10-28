# PlayerStateCommandFactory

> 129 nodes · cohesion 0.03

## Key Concepts

- **request_with_app_container()** (29 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (24 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **handle_whisper_command()** (20 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_channels.py** (20 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_communication_commands_whisper_reply.py** (18 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **handle_say_command()** (16 connections) — `server/commands/communication_commands.py`
- **asyncio** (15 connections)
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **asyncio** (13 connections)
- **test_whisper_command.py** (13 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **asyncio** (12 connections)
- **handle_global_command()** (11 connections) — `server/commands/communication_commands.py`
- **handle_reply_command()** (11 connections) — `server/commands/communication_commands.py`
- **handle_local_command()** (10 connections) — `server/commands/communication_commands.py`
- **handle_system_command()** (10 connections) — `server/commands/communication_commands.py`
- **handle_me_command()** (8 connections) — `server/commands/communication_commands.py`
- **asyncio** (7 connections)
- **communication_commands_mocks.py** (5 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_handle_global_command_level_too_low()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_success()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_local_command_no_room()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_local_command_success()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_not_admin()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_success()** (5 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- *... and 104 more nodes in this community*

## Relationships

- [BaseCommand](BaseCommand.md) (21 shared connections)
- [command_parser.py](command_parser.py.md) (20 shared connections)
- [look_container.py](look_container.py.md) (3 shared connections)
- [.load_room_data](load_room_data.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- `server/tests/unit/commands/test_whisper_command.py`

## Audit Trail

- EXTRACTED: 283 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*