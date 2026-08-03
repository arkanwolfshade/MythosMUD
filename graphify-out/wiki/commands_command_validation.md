# commands command validation

> 51 nodes

## Key Concepts

- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- **_get_grace_check_context()** (8 connections) — `server/command_handler_unified.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_grace_period_blocking.py** (8 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **UUID** (3 connections)
- **test_command_request_app_state_from_http_request_like_object()** (3 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (3 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
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
- *... and 26 more nodes in this community*

## Relationships

- [command commands handler](command_commands_handler.md) (19 shared connections)
- [command validation commands](command_validation_commands.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [request context realtime](request_context_realtime.md) (3 shared connections)
- [alias graph rationale](alias_graph_rationale.md) (2 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [look helpers commands](look_helpers_commands.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 157 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*