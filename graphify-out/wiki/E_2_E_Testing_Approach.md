# E 2 E Testing Approach

> 12 nodes

## Key Concepts

- **test_grace_period_blocking.py** (8 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_blocks_commands()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_allows_commands_when_not_in_grace_period()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_missing_services()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_player_not_found()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **mock_request()** (2 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Unit tests for grace period command blocking in unified command handler.  Tests** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Create a mock request.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() blocks commands for grace period players.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() allows commands when player not in grace period** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() handles missing services gracefully.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Test _check_grace_period_block() handles player not found gracefully.** (1 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`

## Relationships

- [Room Exploration API](Room_Exploration_API.md) (6 shared connections)

## Source Files

- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*