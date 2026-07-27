# Command Commands Validation

> 17 nodes · cohesion 0.15

## Key Concepts

- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **TestCheckAllCommandBlocks** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_casting()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_catatonia()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_casting()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_catatonia()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_no_blocks()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns block result for catatonia.** (2 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns result when catatonia blocks.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _check_all_command_blocks returns result when grace period blocks.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _check_all_command_blocks returns result when casting blocks.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _check_all_command_blocks function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns block result for casting.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_all_command_blocks returns None when no blocks.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Check all command blocking conditions. Returns result if blocked, None otherwise** (1 connections) — `server/command_handler_unified.py`

## Relationships

- [[Command Alias Handling]] (4 shared connections)
- [[Catatonia Check Logic]] (3 shared connections)
- [[Unified Command Handler]] (3 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)
- [[Command Request App State]] (1 shared connections)
- [[Grace Period Blocking Tests]] (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
