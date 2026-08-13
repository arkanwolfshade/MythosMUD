# command_request_app_state

> 13 nodes

## Key Concepts

- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **CommandExecutionRequest** (1 connections)
- **HTTP Request or WebSocketRequestContext for unified command processing.** (1 connections) — `server/command_handler/command_execution_request.py`
- **Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).…** (1 connections) — `server/command_handler/command_execution_request.py`
- **Unit tests for unified command request app-state extraction.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for HTTP/FastAPI-style request objects.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for WebSocketRequestContext.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Gracefully returns None when app or state is absent.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`

## Relationships

- [command_handler_unified.py](command_handler_unified.py.md) (5 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (5 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (3 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`

## Audit Trail

- EXTRACTED: 31 (91%)
- INFERRED: 3 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*