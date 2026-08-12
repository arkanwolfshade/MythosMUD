# Health Check Service

> 34 nodes

## Key Concepts

- **test_communication_commands_channels.py** (20 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **handle_global_command()** (12 connections) — `server/commands/communication_commands.py`
- **handle_local_command()** (11 connections) — `server/commands/communication_commands.py`
- **handle_system_command()** (11 connections) — `server/commands/communication_commands.py`
- **test_handle_local_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_level_too_low()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_not_admin()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_local_command_no_room()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_local_command_no_message()** (3 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_local_command_no_services()** (3 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_no_message()** (3 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_global_command_no_services()** (3 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_no_message()** (3 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **test_handle_system_command_no_services()** (3 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **Local channel message.** (1 connections) — `server/commands/communication_commands.py`
- **Global channel message (level-gated in flow).** (1 connections) — `server/commands/communication_commands.py`
- **Admin-only system broadcast.** (1 connections) — `server/commands/communication_commands.py`
- **Unit tests for local, global, and system chat command handlers.** (1 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **Test handle_local_command with no message.** (1 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **Test handle_local_command when services are not available.** (1 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **Test handle_local_command successful execution.** (1 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **Test handle_global_command with no message.** (1 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- *... and 9 more nodes in this community*

## Relationships

- [Chat NATS Publisher](Chat_NATS_Publisher.md) (13 shared connections)
- [Container Open Events](Container_Open_Events.md) (6 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (3 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`

## Audit Trail

- EXTRACTED: 114 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*