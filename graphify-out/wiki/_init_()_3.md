# . init ()

> 49 nodes

## Key Concepts

- **WebSocketRequestContext** (26 connections) — `server/realtime/request_context.py`
- **test_request_context.py** (16 connections) — `server/tests/unit/realtime/test_request_context.py`
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Any** (7 connections)
- **.set_app_state_services()** (4 connections) — `server/realtime/request_context.py`
- **.get_event_bus()** (4 connections) — `server/realtime/request_context.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
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
- *... and 24 more nodes in this community*

## Relationships

- [.is required()](is_required%28%29.md) (10 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (6 shared connections)
- [test alias storage](test_alias_storage.md) (2 shared connections)
- [chat send with room bundle()](chat_send_with_room_bundle%28%29.md) (2 shared connections)
- [test alias graph](test_alias_graph.md) (1 shared connections)
- [CommandExecutionRequest](CommandExecutionRequest.md) (1 shared connections)
- [.validate topic()](validate_topic%28%29.md) (1 shared connections)
- [ContainerData](ContainerData.md) (1 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/realtime/request_context.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/realtime/test_request_context.py`

## Audit Trail

- EXTRACTED: 149 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*