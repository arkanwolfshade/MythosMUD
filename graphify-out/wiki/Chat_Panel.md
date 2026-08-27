# Chat Panel

> 9 nodes

## Key Concepts

- **command_request_app_state()** (11 connections) — `server/command_handler/command_execution_request.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (3 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **CommandExecutionRequest** (1 connections)
- **Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).…** (1 connections) — `server/command_handler/command_execution_request.py`
- **Returns app.state for HTTP/FastAPI-style request objects.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Returns app.state for WebSocketRequestContext.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Gracefully returns None when app or state is absent.** (1 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (1 shared connections)
- [FastAPI Code Review - Anti-Patterns and Best Practices](FastAPI_Code_Review_-_Anti-Patterns_and_Best_Practices.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`

## Audit Trail

- EXTRACTED: 16 (84%)
- INFERRED: 3 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*