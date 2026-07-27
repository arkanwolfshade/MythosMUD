# Whisper Reply Command Tests

> 38 nodes · cohesion 0.08

## Key Concepts

- **handle_whisper_command()** (20 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_whisper_reply.py** (16 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_whisper_command.py** (12 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_handle_whisper_command_chat_service_failure()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_target_not_found()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_whisper_to_self()** (4 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_reply_command_no_message()** (3 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_no_message()** (3 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_no_services()** (3 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_handle_whisper_command_no_target()** (3 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_whisper_command_missing_message()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_missing_target()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_no_player_service()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_sender_not_found()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_success()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_target_not_found()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_whisper_command_whisper_to_self()** (3 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Test handle_whisper_command with no target.** (2 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **mock_request()** (2 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **mock_sender()** (2 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **mock_target()** (2 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Test whisper command with missing target.** (2 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Unit tests for who commands.** (2 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Unit tests for whisper and reply communication command handlers.** (1 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- *... and 13 more nodes in this community*

## Relationships

- [[Communication Command Handlers]] (12 shared connections)
- [[Communication Command Flows]] (2 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)
- [[Admin Status Commands]] (1 shared connections)
- [[Who Command Tests]] (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- `server/tests/unit/commands/test_whisper_command.py`
- `server/tests/unit/commands/test_who_commands.py`

## Audit Trail

- EXTRACTED: 123 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
