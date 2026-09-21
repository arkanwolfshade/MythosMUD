# command_guards.py

> 36 nodes

## Key Concepts

- **command_guards.py** (22 connections) — `server/command_handler/command_guards.py`
- **command_request_app_state()** (16 connections) — `server/command_handler/command_execution_request.py`
- **command_execution_request.py** (12 connections) — `server/command_handler/command_execution_request.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler/command_guards.py`
- **_CastingStateManagerView** (5 connections) — `server/command_handler/command_guards.py`
- **_coerce_player_uuid()** (5 connections) — `server/command_handler/command_guards.py`
- **_raw_player_id()** (5 connections) — `server/command_handler/command_guards.py`
- **Protocol** (5 connections)
- **_CastingStateView** (4 connections) — `server/command_handler/command_guards.py`
- **_MagicServiceView** (4 connections) — `server/command_handler/command_guards.py`
- **_PlayerLookup** (4 connections) — `server/command_handler/command_guards.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **UUID** (4 connections)
- **_AppStateCommandGuards** (3 connections) — `server/command_handler/command_guards.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (3 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **.get_casting_state()** (2 connections) — `server/command_handler/command_guards.py`
- **.is_casting()** (1 connections) — `server/command_handler/command_guards.py`
- **.get_player_by_name()** (1 connections) — `server/command_handler/command_guards.py`
- **CommandExecutionRequest** (1 connections)
- **HTTP Request or WebSocketRequestContext for unified command processing.** (1 connections) — `server/command_handler/command_execution_request.py`
- **Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).…** (1 connections) — `server/command_handler/command_execution_request.py`
- **Command blocking guards for unified command processing. Grace-period and…** (1 connections) — `server/command_handler/command_guards.py`
- **Return block result if player is currently casting, else None.** (1 connections) — `server/command_handler/command_guards.py`
- *... and 11 more nodes in this community*

## Relationships

- [check_grace_period_block](check_grace_period_block.md) (8 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (7 shared connections)
- [command_input.py](command_input.py.md) (3 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (3 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (2 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [alias_expansion.py](alias_expansion.py.md) (1 shared connections)
- [processing.py](processing.py.md) (1 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_guards.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`

## Audit Trail

- EXTRACTED: 82 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*