# _prepare_command_for_processing

> 71 nodes

## Key Concepts

- **_prepare_command_for_processing()** (20 connections) — `server/command_handler_unified.py`
- **command_input.py** (15 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **_is_predefined_emote()** (11 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (11 connections) — `server/command_handler/command_input.py`
- **TestEmoteDetection** (10 connections) — `server/tests/unit/commands/test_command_input.py`
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **test_command_input.py** (9 connections) — `server/tests/unit/commands/test_command_input.py`
- **TestPrepareCommandForProcessing** (7 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **_mock_request()** (6 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_false()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_no_emote_service()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_true()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **test_command_preparation.py** (4 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_clean_command_input_basic()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_leading_trailing_whitespace()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_multiple_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_tabs()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_empty()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_no_slash()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_with_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_whitespace_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- *... and 46 more nodes in this community*

## Relationships

- [command_handler_unified.py](command_handler_unified.py.md) (11 shared connections)
- [TestHelperFunctions](TestHelperFunctions.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [command_guards.py](command_guards.py.md) (2 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [_validate_command_basics](_validate_command_basics.md) (1 shared connections)
- [_ensure_alias_storage](_ensure_alias_storage.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [CommandValidator](CommandValidator.md) (1 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (1 shared connections)

## Source Files

- `server/command_handler/command_input.py`
- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 132 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*