# _prepare_command_for_processing

> 77 nodes

## Key Concepts

- **_prepare_command_for_processing()** (20 connections) — `server/command_handler_unified.py`
- **command_input.py** (18 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (17 connections) — `server/command_handler/command_input.py`
- **command_handler/__init__.py** (14 connections) — `server/command_handler/__init__.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **_is_predefined_emote()** (11 connections) — `server/command_handler/command_input.py`
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
- **test_a_combat_verb_is_never_mistaken_for_an_emote()** (3 connections) — `server/tests/unit/commands/test_assist_wiring.py`
- **.test_clean_command_input_basic()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_leading_trailing_whitespace()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_multiple_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_tabs()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_empty()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_no_slash()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- *... and 52 more nodes in this community*

## Relationships

- [MessageCategory](MessageCategory.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [command_parser.py](command_parser.py.md) (6 shared connections)
- [AliasGraph](AliasGraph.md) (4 shared connections)
- [command_guards.py](command_guards.py.md) (3 shared connections)
- [get_help_content](get_help_content.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (2 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)
- [processing.py](processing.py.md) (2 shared connections)
- [_check_rate_limit](_check_rate_limit.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/command_input.py`
- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_assist_wiring.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/commands/test_protect_wiring.py`

## Audit Trail

- EXTRACTED: 155 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*