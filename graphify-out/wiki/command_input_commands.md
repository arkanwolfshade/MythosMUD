# command input commands

> 46 nodes

## Key Concepts

- **command_input.py** (14 connections) — `server/command_handler/command_input.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
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
- **Command Input Utilities for MythosMUD.  This module provides utilities for clean** (1 connections) — `server/command_handler/command_input.py`
- **Normalize command input by removing optional slash prefix.      Supports both tr** (1 connections) — `server/command_handler/command_input.py`
- *... and 21 more nodes in this community*

## Relationships

- [command handler unified](command_handler_unified.md) (13 shared connections)
- [emote game service](emote_game_service.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [command validator validators](command_validator_validators.md) (1 shared connections)
- [alias storage commands](alias_storage_commands.md) (1 shared connections)

## Source Files

- `server/command_handler/command_input.py`
- `server/tests/unit/commands/test_command_input.py`

## Audit Trail

- EXTRACTED: 143 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*