# Archive Database Migration

> 8 nodes

## Key Concepts

- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Unit tests for unified command request app-state extraction.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for HTTP/FastAPI-style request objects.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for WebSocketRequestContext.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Gracefully returns None when app or state is absent.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`

## Relationships

- [Room Exploration API](Room_Exploration_API.md) (4 shared connections)
- [Config Model Tests](Config_Model_Tests.md) (2 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (2 shared connections)
- [Persistence Container Extended](Persistence_Container_Extended.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/tests/unit/command_handler/test_command_execution_request.py`

## Audit Trail

- EXTRACTED: 22 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*