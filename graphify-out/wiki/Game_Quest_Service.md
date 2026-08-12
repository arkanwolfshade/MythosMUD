# Game Quest Service

> 12 nodes

## Key Concepts

- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_no_player_service()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_player_not_found()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_player_in_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_grace_period_block function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_grace_period_block returns None when no connection manager.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_grace_period_block returns None when no player service.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_grace_period_block returns None when player not found.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_grace_period_block returns block result when player in grace period.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _check_grace_period_block returns None on error.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`

## Relationships

- [Room Exploration API](Room_Exploration_API.md) (5 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*