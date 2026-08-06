# request context realtime

> 39 nodes

## Key Concepts

- **WebSocketRequestContext** (26 connections) — `server/realtime/request_context.py`
- **test_request_context.py** (16 connections) — `server/tests/unit/realtime/test_request_context.py`
- **Any** (7 connections)
- **.set_app_state_services()** (4 connections) — `server/realtime/request_context.py`
- **.get_event_bus()** (4 connections) — `server/realtime/request_context.py`
- **test_create_websocket_request_context()** (4 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_create_websocket_request_context_no_user()** (4 connections) — `server/tests/unit/realtime/test_request_context.py`
- **.__init__()** (3 connections) — `server/realtime/request_context.py`
- **.set_alias_storage()** (3 connections) — `server/realtime/request_context.py`
- **.get_persistence()** (3 connections) — `server/realtime/request_context.py`
- **test_websocket_request_context_init()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_init_no_user()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_alias_storage()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_app_state_services()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_app_state_services_none()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_persistence()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_event_bus()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_event_bus_none()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_alias_storage()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_alias_storage_not_set()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **Creates FastAPI Request-like objects for WebSocket commands.      This allows We** (1 connections) — `server/realtime/request_context.py`
- **Initialize the WebSocket request context.          Args:             app_state:** (1 connections) — `server/realtime/request_context.py`
- **Set the alias storage in the app state.          Args:             alias_storage** (1 connections) — `server/realtime/request_context.py`
- **Set the app state services in the request context.         Note: This method is** (1 connections) — `server/realtime/request_context.py`
- **Get the persistence layer from the request context.** (1 connections) — `server/realtime/request_context.py`
- *... and 14 more nodes in this community*

## Relationships

- [command commands aliases](command_commands_aliases.md) (5 shared connections)
- [player model models](player_model_models.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (2 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [lucidity event services](lucidity_event_services.md) (1 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/tests/unit/realtime/test_request_context.py`

## Audit Trail

- EXTRACTED: 117 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*