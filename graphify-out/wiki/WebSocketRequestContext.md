# WebSocketRequestContext

> 43 nodes

## Key Concepts

- **WebSocketRequestContext** (24 connections) — `server/realtime/request_context.py`
- **test_request_context.py** (16 connections) — `server/tests/unit/realtime/test_request_context.py`
- **request_context.py** (9 connections) — `server/realtime/request_context.py`
- **Any** (7 connections)
- **.get_alias_storage()** (4 connections) — `server/realtime/request_context.py`
- **.get_event_bus()** (4 connections) — `server/realtime/request_context.py`
- **.get_persistence()** (3 connections) — `server/realtime/request_context.py`
- **.__init__()** (3 connections) — `server/realtime/request_context.py`
- **.set_alias_storage()** (3 connections) — `server/realtime/request_context.py`
- **.set_app_state_services()** (3 connections) — `server/realtime/request_context.py`
- **test_create_websocket_request_context()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_create_websocket_request_context_no_user()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
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
- **Request context factory for WebSocket command processing. This module provides…** (1 connections) — `server/realtime/request_context.py`
- **Get the event bus from the request context.** (1 connections) — `server/realtime/request_context.py`
- **Get the alias storage from the request context.** (1 connections) — `server/realtime/request_context.py`
- *... and 18 more nodes in this community*

## Relationships

- [websocket_handler_commands.py](websocket_handler_commands.py.md) (6 shared connections)
- [command_request_app_state](command_request_app_state.md) (5 shared connections)
- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_alias_storage.py](test_alias_storage.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/tests/unit/realtime/test_request_context.py`

## Audit Trail

- EXTRACTED: 73 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*