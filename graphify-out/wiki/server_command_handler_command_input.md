# server command handler command input

> 49 nodes

## Key Concepts

- **command_input.py** (15 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (10 connections) — `server/command_handler/command_input.py`
- **TestEmoteDetection** (8 connections) — `server/tests/unit/commands/test_command_input.py`
- **_is_predefined_emote()** (8 connections) — `server/command_handler/command_input.py`
- **test_command_input.py** (8 connections) — `server/tests/unit/commands/test_command_input.py`
- **patch** (5 connections)
- **.test_is_predefined_emote_false()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_true()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_predefined_emote()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_unknown_word()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_basic()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_leading_trailing_whitespace()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_multiple_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_tabs()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_empty()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_no_slash()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_with_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_whitespace_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_with_slash()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_system_command()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- *... and 24 more nodes in this community*

## Relationships

- [server command handler command execution](server_command_handler_command_execution.md) (6 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server game emote service emotedefinition](server_game_emote_service_emotedefinition.md) (2 shared connections)
- [server tests unit validators test](server_tests_unit_validators_test.md) (2 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)

## Source Files

- `server/command_handler/command_input.py`
- `server/tests/unit/commands/test_command_input.py`

## Audit Trail

- EXTRACTED: 92 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*