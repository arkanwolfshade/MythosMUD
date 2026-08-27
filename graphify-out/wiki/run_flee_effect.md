# run_flee_effect

> 31 nodes

## Key Concepts

- **_check_grace_period_block()** (23 connections) — `server/command_handler_unified.py`
- **test_grace_period_blocking.py** (9 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_get_grace_check_context()** (7 connections) — `server/command_handler_unified.py`
- **test_check_grace_period_block_allows_commands_when_not_in_grace_period()** (4 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_blocks_commands()** (4 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_missing_services()** (4 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_player_not_found()** (4 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **.test_check_grace_period_block_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_no_connection_manager()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_no_player_service()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_player_in_grace_period()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_player_not_found()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **asyncio** (4 connections)
- **mock_request()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **UUID** (2 connections)
- **fixture** (1 connections)
- **Resolve player_id and connection_manager for grace period check. Returns None…** (1 connections) — `server/command_handler_unified.py`
- **Check if player is in grace period and block commands. Players in grace period…** (1 connections) — `server/command_handler_unified.py`
- **Unit tests for grace period command blocking in unified command handler. Tests…** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Create a mock request.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() blocks commands for grace period players.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() allows commands when player not in grace…** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() handles missing services gracefully.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() handles player not found gracefully.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_connection_statistics.py](test_connection_statistics.py.md) (10 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (7 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (5 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 64 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*