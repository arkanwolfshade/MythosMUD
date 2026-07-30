# parse json field()

> 36 nodes

## Key Concepts

- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler_unified.py`
- **TestCheckCastingState** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **.test_check_casting_state_allowed_commands()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_not_casting()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_is_casting()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_no_magic_service()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_error_handling()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_allowed_command()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_casting_state_no_magic_service()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_casting_state_player_casting()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_casting_state_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **HTTP Request or WebSocketRequestContext for unified command processing.** (1 connections) — `server/command_handler/command_execution_request.py`
- **Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).** (1 connections) — `server/command_handler/command_execution_request.py`
- **Return block result if player is currently casting, else None. Caller must pass** (1 connections) — `server/command_handler_unified.py`
- **Check if player is casting and should be blocked. Returns result if blocked.** (1 connections) — `server/command_handler_unified.py`
- **Unit tests for unified command request app-state extraction.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for HTTP/FastAPI-style request objects.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for WebSocketRequestContext.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- *... and 11 more nodes in this community*

## Relationships

- [check alias safety()](check_alias_safety%28%29.md) (16 shared connections)
- [CommandExecutionRequest](CommandExecutionRequest.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [chat send with room bundle()](chat_send_with_room_bundle%28%29.md) (2 shared connections)
- [test movement service](test_movement_service.md) (1 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 115 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*