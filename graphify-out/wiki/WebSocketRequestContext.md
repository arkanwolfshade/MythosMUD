# WebSocketRequestContext

> 37 nodes

## Key Concepts

- **WebSocketRequestContext** (24 connections) — `server/realtime/request_context.py`
- **test_request_context.py** (16 connections) — `server/tests/unit/realtime/test_request_context.py`
- **Any** (7 connections)
- **.get_event_bus()** (4 connections) — `server/realtime/request_context.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **.get_persistence()** (3 connections) — `server/realtime/request_context.py`
- **.__init__()** (3 connections) — `server/realtime/request_context.py`
- **.set_alias_storage()** (3 connections) — `server/realtime/request_context.py`
- **.set_app_state_services()** (3 connections) — `server/realtime/request_context.py`
- **test_websocket_request_context_get_alias_storage()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_alias_storage_not_set()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_event_bus()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_event_bus_none()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_persistence()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_init()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_init_no_user()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_alias_storage()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_app_state_services()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_app_state_services_none()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **Get the event bus from the request context.** (1 connections) — `server/realtime/request_context.py`
- **Creates FastAPI Request-like objects for WebSocket commands. This allows…** (1 connections) — `server/realtime/request_context.py`
- **Initialize the WebSocket request context. Args: app_state: Real application…** (1 connections) — `server/realtime/request_context.py`
- **Set the alias storage in the app state. Args: alias_storage: Alias storage…** (1 connections) — `server/realtime/request_context.py`
- **Set the app state services in the request context. Note: This method is kept…** (1 connections) — `server/realtime/request_context.py`
- **Get the persistence layer from the request context.** (1 connections) — `server/realtime/request_context.py`
- *... and 12 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (5 shared connections)
- [alias_storage](alias_storage.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/realtime/test_request_context.py`

## Audit Trail

- EXTRACTED: 114 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*