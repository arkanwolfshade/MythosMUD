# Deprecated Logging Patterns

> 47 nodes

## Key Concepts

- **handle_whisper_command()** (21 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_whisper_reply.py** (17 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_whisper_command.py** (13 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_handle_whisper_command_target_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_whisper_to_self()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_reply_command_no_last_whisper_sender()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_reply_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_chat_service_failure()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_no_target()** (3 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_no_message()** (3 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_no_services()** (3 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_reply_command_no_message()** (3 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_reply_command_no_services()** (3 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_whisper_command_missing_target()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_missing_message()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_no_player_service()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_sender_not_found()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_target_not_found()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_whisper_to_self()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_success()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **mock_request()** (2 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **mock_sender()** (2 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **mock_target()** (2 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Unit tests for whisper and reply communication command handlers.** (1 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- *... and 22 more nodes in this community*

## Relationships

- [Chat NATS Publisher](Chat_NATS_Publisher.md) (10 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (9 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- `server/tests/unit/commands/test_whisper_command.py`

## Audit Trail

- EXTRACTED: 139 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*