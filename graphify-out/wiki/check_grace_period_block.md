# check_grace_period_block

> 36 nodes

## Key Concepts

- **check_grace_period_block()** (18 connections) — `server/command_handler/command_guards.py`
- **test_grace_period_blocking.py** (11 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_get_grace_check_context()** (7 connections) — `server/command_handler/command_guards.py`
- **_as_command_request()** (7 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **_request_state()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_allows_commands_when_not_in_grace_period()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_blocks_commands()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_missing_services()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_player_not_found()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **.testcheck_grace_period_block_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_no_connection_manager()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_no_player_service()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_player_in_grace_period()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_player_not_found()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **CommandExecutionRequest** (4 connections)
- **asyncio** (4 connections)
- **mock_request()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **CommandExecutionRequest** (1 connections)
- **fixture** (1 connections)
- **Check if player is in grace period and block commands. Players in grace period…** (1 connections) — `server/command_handler/command_guards.py`
- **Resolve player_id and connection_manager for grace period check. Returns None…** (1 connections) — `server/command_handler/command_guards.py`
- **Unit tests for grace period command blocking in unified command handler. Tests…** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test check_grace_period_block() handles player not found gracefully.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Create a mock request with app.state for command guards.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- *... and 11 more nodes in this community*

## Relationships

- [catatonia_check.py](catatonia_check.py.md) (9 shared connections)
- [command_guards.py](command_guards.py.md) (8 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)

## Source Files

- `server/command_handler/command_guards.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 74 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*