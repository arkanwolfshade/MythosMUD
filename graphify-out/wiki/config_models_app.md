# config models app

> 20 nodes

## Key Concepts

- **TestValidateCommandBasics** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCheckAllCommandBlocks** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_validate_command_basics_empty()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_validate_command_basics_too_long()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_validate_command_basics_invalid_content()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_validate_command_basics_valid()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_catatonia()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_casting()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_no_blocks()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns result for empty command.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns result for command too long.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns result for invalid command content.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns None for valid command.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns block result for catatonia.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns block result for grace period.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns block result for casting.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns None when no blocks.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`

## Relationships

- [command commands handler](command_commands_handler.md) (8 shared connections)
- [command validation commands](command_validation_commands.md) (2 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*