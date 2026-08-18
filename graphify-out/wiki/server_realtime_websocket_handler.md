# server realtime websocket handler

> 167 nodes

## Key Concepts

- **websocket_handler.py** (65 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_helpers.py** (42 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **websocket_helpers.py** (39 connections) — `server/realtime/websocket_helpers.py`
- **websocket_handler_message_loop.py** (27 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_helpers_player.py** (24 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **get_player_and_room()** (14 connections) — `server/realtime/websocket_helpers.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_shutdown_and_reject()** (13 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **prepare_player_data()** (12 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_player_service_from_connection_manager()** (9 connections) — `server/realtime/websocket_helpers.py`
- **get_player_stats_data()** (9 connections) — `server/realtime/websocket_helpers.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (9 connections)
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **build_basic_player_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- **WebSocket** (7 connections)
- **asyncio** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- *... and 142 more nodes in this community*

## Relationships

- [server commands look helpers lookrequest](server_commands_look_helpers_lookrequest.md) (23 shared connections)
- [server realtime websocket handler commands](server_realtime_websocket_handler_commands.md) (11 shared connections)
- [server realtime websocket handler app](server_realtime_websocket_handler_app.md) (11 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (8 shared connections)
- [attributeerror](attributeerror.md) (8 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server realtime message validator](server_realtime_message_validator.md) (7 shared connections)
- [server container main get container](server_container_main_get_container.md) (6 shared connections)
- [server async persistence](server_async_persistence.md) (4 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (4 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (4 shared connections)
- [server realtime websocket handler handle](server_realtime_websocket_handler_handle.md) (4 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 380 (94%)
- INFERRED: 26 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*