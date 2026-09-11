# command_request_app_state

> 11 nodes

## Key Concepts

- **command_request_app_state()** (16 connections) — `server/command_handler/command_execution_request.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (3 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **CommandExecutionRequest** (1 connections)
- **Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).…** (1 connections) — `server/command_handler/command_execution_request.py`
- **Unit tests for unified command request app-state extraction.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for HTTP/FastAPI-style request objects.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for WebSocketRequestContext.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Gracefully returns None when app or state is absent.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`

## Relationships

- [command_guards.py](command_guards.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (2 shared connections)
- [_is_predefined_emote](_is_predefined_emote.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`

## Audit Trail

- EXTRACTED: 26 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*