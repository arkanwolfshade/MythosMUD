# _is_predefined_emote

> 27 nodes

## Key Concepts

- **_is_predefined_emote()** (11 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (11 connections) — `server/command_handler/command_input.py`
- **TestEmoteDetection** (10 connections) — `server/tests/unit/commands/test_command_input.py`
- **test_command_input.py** (9 connections) — `server/tests/unit/commands/test_command_input.py`
- **_mock_request()** (6 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_false()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_no_emote_service()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_true()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_no_request()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_predefined_emote()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_system_command()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_unknown_word()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **CommandExecutionRequest** (2 connections)
- **Check if a command is a predefined emote alias. Args: command: The command to…** (1 connections) — `server/command_handler/command_input.py`
- **Check if a single word command should be treated as an emote. This function…** (1 connections) — `server/command_handler/command_input.py`
- **Unit tests for command input processing. Tests command normalization, cleaning,…** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test _is_predefined_emote() returns False when no request is available.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test _is_predefined_emote() returns False when app.state has no emote_service.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test _is_predefined_emote() handles errors from the emote service gracefully.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test should_treat_as_emote() returns False for system commands.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test should_treat_as_emote() returns False for unknown words.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test should_treat_as_emote() returns True for predefined emotes.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Build a mock request whose app.state.emote_service is the given value.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test emote detection functions.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- *... and 2 more nodes in this community*

## Relationships

- [command_handler_unified.py](command_handler_unified.py.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)

## Source Files

- `server/command_handler/command_input.py`
- `server/tests/unit/commands/test_command_input.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*