# WebSocketRequestContext

> 39 nodes

## Key Concepts

- **WebSocketRequestContext** (26 connections) — `server/realtime/request_context.py`
- **test_request_context.py** (16 connections) — `server/tests/unit/realtime/test_request_context.py`
- **Any** (7 connections)
- **.get_event_bus()** (4 connections) — `server/realtime/request_context.py`
- **test_create_websocket_request_context()** (4 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_create_websocket_request_context_no_user()** (4 connections) — `server/tests/unit/realtime/test_request_context.py`
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
- *... and 14 more nodes in this community*

## Relationships

- [look_command.py](look_command.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [command_request_app_state](command_request_app_state.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/tests/unit/realtime/test_request_context.py`

## Audit Trail

- EXTRACTED: 65 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*