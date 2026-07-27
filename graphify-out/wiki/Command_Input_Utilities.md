# Command Input Utilities

> 62 nodes · cohesion 0.04

## Key Concepts

- **CommandValidator** (14 connections) — `server/validators/command_validator.py`
- **command_input.py** (13 connections) — `server/command_handler/command_input.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (10 connections) — `server/command_handler/command_input.py`
- **_is_predefined_emote()** (8 connections) — `server/command_handler/command_input.py`
- **TestEmoteDetection** (8 connections) — `server/tests/unit/commands/test_command_input.py`
- **test_command_input.py** (7 connections) — `server/tests/unit/commands/test_command_input.py`
- **.validate_command_content()** (4 connections) — `server/validators/command_validator.py`
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
- **.test_is_predefined_emote_false()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_true()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_predefined_emote()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_system_command()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- *... and 37 more nodes in this community*

## Relationships

- [[Alias Expansion Logic]] (12 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Unified Command Handler]] (3 shared connections)
- [[Chat Message Helpers]] (2 shared connections)
- [[Emote Schema Validator]] (1 shared connections)
- [[Command Parser Tests]] (1 shared connections)
- [[Command Input Validator]] (1 shared connections)

## Source Files

- `server/command_handler/command_input.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 191 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
