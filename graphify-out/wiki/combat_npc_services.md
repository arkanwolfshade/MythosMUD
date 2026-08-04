# combat npc services

> 39 nodes

## Key Concepts

- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (8 connections) — `server/command_handler_unified.py`
- **test_grace_period_blocking.py** (8 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **UUID** (3 connections)
- **test_check_grace_period_block_blocks_commands()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_allows_commands_when_not_in_grace_period()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_missing_services()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_player_not_found()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **.test_check_grace_period_block_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_not_in_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_in_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_no_player()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_uuid_conversion()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_no_player_service()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_player_not_found()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_player_in_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_grace_period_block_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **mock_request()** (2 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Resolve player_id and connection_manager for grace period check. Returns None if** (1 connections) — `server/command_handler_unified.py`
- **Check if player is in grace period and block commands.      Players in grace per** (1 connections) — `server/command_handler_unified.py`
- **Unit tests for grace period command blocking in unified command handler.  Tests** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Create a mock request.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() blocks commands for grace period players.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- *... and 14 more nodes in this community*

## Relationships

- [command commands handler](command_commands_handler.md) (15 shared connections)
- [command validation commands](command_validation_commands.md) (3 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [combat services turn](combat_services_turn.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 111 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*