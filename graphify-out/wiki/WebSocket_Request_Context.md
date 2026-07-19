# WebSocket Request Context

> 41 nodes · cohesion 0.07

## Key Concepts

- **WebSocketRequestContext** (24 connections) — `server/realtime/request_context.py`
- **test_request_context.py** (15 connections) — `server/tests/unit/realtime/test_request_context.py`
- **create_websocket_request_context()** (9 connections) — `server/realtime/request_context.py`
- **Any** (7 connections) — `server/realtime/request_context.py`
- **.get_alias_storage()** (3 connections) — `server/realtime/request_context.py`
- **.get_event_bus()** (3 connections) — `server/realtime/request_context.py`
- **.get_persistence()** (3 connections) — `server/realtime/request_context.py`
- **.__init__()** (3 connections) — `server/realtime/request_context.py`
- **.set_alias_storage()** (3 connections) — `server/realtime/request_context.py`
- **.set_app_state_services()** (3 connections) — `server/realtime/request_context.py`
- **Test WebSocketRequestContext.set_alias_storage().** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
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
- **Get the event bus from the request context.** (1 connections) — `server/realtime/request_context.py`
- **Get the alias storage from the request context.** (1 connections) — `server/realtime/request_context.py`
- *... and 16 more nodes in this community*

## Relationships

- [[NPC Admin API]] (3 shared connections)
- [[WebSocket Command Handler]] (2 shared connections)
- [[Command Request App State]] (2 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/tests/unit/realtime/test_request_context.py`

## Audit Trail

- EXTRACTED: 130 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
