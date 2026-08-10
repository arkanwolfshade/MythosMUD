# Deprecated Logging Patterns

> 25 nodes

## Key Concepts

- **handle_whisper_command()** (21 connections) — `server/commands/communication_commands.py`
- **test_whisper_command.py** (13 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **test_handle_whisper_command_no_message()** (3 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
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
- **Test handle_whisper_command with no message.** (1 connections) — `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- **Unit tests for whisper command.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Create a mock request object.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Create a mock sender player.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Create a mock target player.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Test whisper command with missing target.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Test whisper command with missing message.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Test whisper command when player service is unavailable.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Test whisper command when sender not found.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Test whisper command when target not found.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Test whisper command when trying to whisper to self.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`
- **Test successful whisper command.** (1 connections) — `server/tests/unit/commands/test_whisper_command.py`

## Relationships

- [Caching Lru Cache](Caching_Lru_Cache.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [FastAPI App Factory](FastAPI_App_Factory.md) (1 shared connections)
- [E 2 E Execution Guards](E_2_E_Execution_Guards.md) (1 shared connections)
- [E 2 E Scenario Template](E_2_E_Scenario_Template.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/tests/unit/commands/test_communication_commands_whisper_reply.py`
- `server/tests/unit/commands/test_whisper_command.py`

## Audit Trail

- EXTRACTED: 75 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*