# commands recovery lucidity

> 28 nodes

## Key Concepts

- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **test_command_input.py** (8 connections) — `server/tests/unit/commands/test_command_input.py`
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
- **Clean and normalize command input by collapsing multiple spaces and stripping wh** (1 connections) — `server/command_handler/command_input.py`
- **Normalize command input by removing optional slash prefix.      Supports both tr** (1 connections) — `server/command_handler/command_input.py`
- **Unit tests for command input processing.  Tests command normalization, cleaning,** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test command normalization functions.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test clean_command_input() with normal command.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test clean_command_input() collapses multiple spaces.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test clean_command_input() strips leading/trailing whitespace.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test clean_command_input() handles tabs.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test normalize_command() with no slash prefix.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test normalize_command() removes slash prefix.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test normalize_command() with empty string.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- *... and 3 more nodes in this community*

## Relationships

- [player model models](player_model_models.md) (5 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (4 shared connections)
- [command validation commands](command_validation_commands.md) (2 shared connections)
- [npc idle movement](npc_idle_movement.md) (1 shared connections)

## Source Files

- `server/command_handler/command_input.py`
- `server/tests/unit/commands/test_command_input.py`

## Audit Trail

- EXTRACTED: 86 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*