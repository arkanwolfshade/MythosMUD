# Command Request App State

> 35 nodes · cohesion 0.07

## Key Concepts

- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (13 connections) — `server/command_handler/command_execution_request.py`
- **test_command_execution_request.py** (6 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **TestCheckCastingState** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_get_casting_block_result()** (6 connections) — `server/command_handler_unified.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **.test_check_casting_state_allowed_commands()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_error_handling()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_is_casting()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_no_magic_service()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_not_casting()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_allowed_command()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_casting_state_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_casting_state_no_magic_service()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_casting_state_player_casting()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test check_connections_health handles errors gracefully.** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **Test _check_casting_state returns None when player is not casting.** (2 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **test_check_connection_state_error()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connections_health_error()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).** (1 connections) — `server/command_handler/command_execution_request.py`
- **Unit tests for unified command request app-state extraction.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for HTTP/FastAPI-style request objects.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for WebSocketRequestContext.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- *... and 10 more nodes in this community*

## Relationships

- [[Command Alias Handling]] (6 shared connections)
- [[Catatonia Check Logic]] (5 shared connections)
- [[Unified Command Handler]] (5 shared connections)
- [[Alias Expansion Logic]] (4 shared connections)
- [[WebSocket Request Context]] (2 shared connections)
- [[Communication Command Flows]] (2 shared connections)
- [[Command Commands Validation]] (1 shared connections)
- [[Services Combat Cleanup]] (1 shared connections)
- [[Health Service Tests]] (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 109 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
