# server command handler command execution

> 53 nodes

## Key Concepts

- **WebSocketRequestContext** (26 connections) — `server/realtime/request_context.py`
- **test_request_context.py** (16 connections) — `server/tests/unit/realtime/test_request_context.py`
- **command_execution_request.py** (10 connections) — `server/command_handler/command_execution_request.py`
- **request_context.py** (10 connections) — `server/realtime/request_context.py`
- **create_websocket_request_context()** (9 connections) — `server/realtime/request_context.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Any** (7 connections)
- **.get_alias_storage()** (4 connections) — `server/realtime/request_context.py`
- **.get_event_bus()** (4 connections) — `server/realtime/request_context.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_create_websocket_request_context()** (4 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_create_websocket_request_context_no_user()** (4 connections) — `server/tests/unit/realtime/test_request_context.py`
- **.get_persistence()** (3 connections) — `server/realtime/request_context.py`
- **.__init__()** (3 connections) — `server/realtime/request_context.py`
- **.set_alias_storage()** (3 connections) — `server/realtime/request_context.py`
- **.set_app_state_services()** (3 connections) — `server/realtime/request_context.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (3 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_websocket_request_context_get_alias_storage()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_alias_storage_not_set()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_event_bus()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_event_bus_none()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_persistence()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_init()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_init_no_user()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- *... and 28 more nodes in this community*

## Relationships

- [server command handler command execution](server_command_handler_command_execution.md) (6 shared connections)
- [server realtime websocket handler app](server_realtime_websocket_handler_app.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (1 shared connections)
- [server tests unit test alias](server_tests_unit_test_alias.md) (1 shared connections)
- [eventbus](eventbus.md) (1 shared connections)
- [object](object.md) (1 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (1 shared connections)
- [server command handler catatonia check](server_command_handler_catatonia_check.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)
- [server command handler processing](server_command_handler_processing.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/realtime/request_context.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/realtime/test_request_context.py`

## Audit Trail

- EXTRACTED: 85 (84%)
- INFERRED: 16 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*