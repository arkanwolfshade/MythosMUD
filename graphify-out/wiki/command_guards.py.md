# command_guards.py

> 76 nodes

## Key Concepts

- **command_guards.py** (22 connections) — `server/command_handler/command_guards.py`
- **check_grace_period_block()** (18 connections) — `server/command_handler/command_guards.py`
- **command_request_app_state()** (16 connections) — `server/command_handler/command_execution_request.py`
- **check_casting_state()** (12 connections) — `server/command_handler/command_guards.py`
- **test_grace_period_blocking.py** (11 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler/command_guards.py`
- **_get_grace_check_context()** (7 connections) — `server/command_handler/command_guards.py`
- **_as_command_request()** (7 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **TestCheckCastingState** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_request_state()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_allows_commands_when_not_in_grace_period()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_blocks_commands()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_missing_services()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_player_not_found()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **_CastingStateManagerView** (5 connections) — `server/command_handler/command_guards.py`
- **_coerce_player_uuid()** (5 connections) — `server/command_handler/command_guards.py`
- **_raw_player_id()** (5 connections) — `server/command_handler/command_guards.py`
- **Protocol** (5 connections)
- **_CastingStateView** (4 connections) — `server/command_handler/command_guards.py`
- **_MagicServiceView** (4 connections) — `server/command_handler/command_guards.py`
- **_PlayerLookup** (4 connections) — `server/command_handler/command_guards.py`
- **.testcheck_casting_state_allowed_command()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_casting_state_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_casting_state_no_magic_service()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 51 more nodes in this community*

## Relationships

- [catatonia_check.py](catatonia_check.py.md) (18 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (6 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (3 shared connections)
- [_prepare_command_for_processing](_prepare_command_for_processing.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_guards.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 153 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*