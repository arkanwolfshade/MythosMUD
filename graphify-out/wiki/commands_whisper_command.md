# commands whisper command

> 53 nodes

## Key Concepts

- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **handle_whisper_command()** (20 connections) — `server/commands/communication_commands.py`
- **test_communication_commands_whisper_reply.py** (17 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **test_whisper_command.py** (13 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **handle_reply_command()** (10 connections) — `server/commands/communication_commands.py`
- **communication_commands_mocks.py** (5 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
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
- *... and 28 more nodes in this community*

## Relationships

- [message nats handler](message_nats_handler.md) (12 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (9 shared connections)
- [commands communication flows](commands_communication_flows.md) (6 shared connections)
- [commands party examples](commands_party_examples.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- `server/tests/unit/commands/test_whisper_command.py`

## Audit Trail

- EXTRACTED: 185 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*