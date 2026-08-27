# Second NPC Combat And Linkdead Findings

> 9 nodes

## Key Concepts

- **TestCheckAllCommandBlocks** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_casting()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_catatonia()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_grace_period()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_no_blocks()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns block result for catatonia.** (2 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns block result for casting.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns None when no blocks.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`

## Relationships

- [test_message_handlers.py](test_message_handlers.py.md) (5 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (4 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*