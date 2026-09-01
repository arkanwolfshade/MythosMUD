# WebSocketRequestContext

> 107 nodes

## Key Concepts

- **WebSocketRequestContext** (26 connections) — `server/realtime/request_context.py`
- **command_guards.py** (22 connections) — `server/command_handler/command_guards.py`
- **check_grace_period_block()** (18 connections) — `server/command_handler/command_guards.py`
- **command_request_app_state()** (16 connections) — `server/command_handler/command_execution_request.py`
- **test_request_context.py** (16 connections) — `server/tests/unit/realtime/test_request_context.py`
- **command_execution_request.py** (13 connections) — `server/command_handler/command_execution_request.py`
- **check_casting_state()** (12 connections) — `server/command_handler/command_guards.py`
- **test_grace_period_blocking.py** (12 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **create_websocket_request_context()** (11 connections) — `server/realtime/request_context.py`
- **request_context.py** (10 connections) — `server/realtime/request_context.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler/command_guards.py`
- **_get_grace_check_context()** (7 connections) — `server/command_handler/command_guards.py`
- **_as_command_request()** (7 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **Any** (7 connections)
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
- *... and 82 more nodes in this community*

## Relationships

- [catatonia_check.py](catatonia_check.py.md) (15 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (4 shared connections)
- [command_input.py](command_input.py.md) (3 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (3 shared connections)
- [look_command.py](look_command.py.md) (3 shared connections)
- [.state](state.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [alias_expansion.py](alias_expansion.py.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_guards.py`
- `server/realtime/request_context.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/realtime/test_request_context.py`

## Audit Trail

- EXTRACTED: 215 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*