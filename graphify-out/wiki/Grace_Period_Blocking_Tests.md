# Grace Period Blocking Tests

> 35 nodes · cohesion 0.07

## Key Concepts

- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **test_grace_period_blocking.py** (8 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **test_check_grace_period_block_allows_commands_when_not_in_grace_period()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_blocks_commands()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_missing_services()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_player_not_found()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **.test_check_grace_period_block_in_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_no_player()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_not_in_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_uuid_conversion()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_no_player_service()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_player_in_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_player_not_found()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **mock_request()** (2 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block returns block result when player in grace period.** (2 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Unit tests for grace period command blocking in unified command handler.  Tests** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Create a mock request.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() blocks commands for grace period players.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() allows commands when player not in grace period** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() handles missing services gracefully.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() handles player not found gracefully.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- *... and 10 more nodes in this community*

## Relationships

- [[Command Alias Handling]] (6 shared connections)
- [[Unified Command Handler]] (3 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)
- [[Catatonia Check Logic]] (2 shared connections)
- [[Command Commands Validation]] (1 shared connections)
- [[Look Command Helpers]] (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 101 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
