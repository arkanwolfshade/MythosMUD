# clean command input()

> 45 nodes

## Key Concepts

- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (10 connections) — `server/command_handler/command_input.py`
- **_is_predefined_emote()** (8 connections) — `server/command_handler/command_input.py`
- **test_command_input.py** (8 connections) — `server/tests/unit/commands/test_command_input.py`
- **TestEmoteDetection** (8 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_basic()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_multiple_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_leading_trailing_whitespace()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_tabs()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_no_slash()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_with_slash()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_empty()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_whitespace_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_with_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_true()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_false()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_system_command()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_unknown_word()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_predefined_emote()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test normalize_command() with whitespace only.** (2 connections) — `server/tests/unit/commands/test_command_input.py`
- **Clean and normalize command input by collapsing multiple spaces and stripping wh** (1 connections) — `server/command_handler/command_input.py`
- *... and 20 more nodes in this community*

## Relationships

- [Validate an expanded command for](Validate_an_expanded_command_for.md) (5 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (4 shared connections)
- [CommandExecutionRequest](CommandExecutionRequest.md) (3 shared connections)
- [Test prepare command for processing](Test_prepare_command_for_processing.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/command_handler/command_input.py`
- `server/tests/unit/commands/test_command_input.py`

## Audit Trail

- EXTRACTED: 139 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*