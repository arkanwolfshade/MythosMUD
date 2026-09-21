# command_guards.py

> 68 nodes

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
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **.testcheck_grace_period_block_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_no_connection_manager()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_no_player_service()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 43 more nodes in this community*

## Relationships

- [catatonia_check.py](catatonia_check.py.md) (15 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (5 shared connections)
- [command_input.py](command_input.py.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_guards.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 141 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*