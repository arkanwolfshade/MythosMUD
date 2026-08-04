# request context realtime

> 55 nodes

## Key Concepts

- **WebSocketRequestContext** (26 connections) — `server/realtime/request_context.py`
- **test_request_context.py** (16 connections) — `server/tests/unit/realtime/test_request_context.py`
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- **request_context.py** (9 connections) — `server/realtime/request_context.py`
- **create_websocket_request_context()** (9 connections) — `server/realtime/request_context.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **Any** (7 connections)
- **.set_app_state_services()** (4 connections) — `server/realtime/request_context.py`
- **.get_event_bus()** (4 connections) — `server/realtime/request_context.py`
- **.get_alias_storage()** (4 connections) — `server/realtime/request_context.py`
- **test_command_request_app_state_from_websocket_request_context()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_create_websocket_request_context()** (4 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_create_websocket_request_context_no_user()** (4 connections) — `server/tests/unit/realtime/test_request_context.py`
- **.__init__()** (3 connections) — `server/realtime/request_context.py`
- **.set_alias_storage()** (3 connections) — `server/realtime/request_context.py`
- **.get_persistence()** (3 connections) — `server/realtime/request_context.py`
- **test_command_request_app_state_from_http_request_like_object()** (3 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (3 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_websocket_request_context_init()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_init_no_user()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_alias_storage()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_app_state_services()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_set_app_state_services_none()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_persistence()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- **test_websocket_request_context_get_event_bus()** (3 connections) — `server/tests/unit/realtime/test_request_context.py`
- *... and 30 more nodes in this community*

## Relationships

- [command validation commands](command_validation_commands.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [command commands aliases](command_commands_aliases.md) (2 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (2 shared connections)
- [fixtures mock helpers](fixtures_mock_helpers.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [command commands handler](command_commands_handler.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/realtime/request_context.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/realtime/test_request_context.py`

## Audit Trail

- EXTRACTED: 173 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*