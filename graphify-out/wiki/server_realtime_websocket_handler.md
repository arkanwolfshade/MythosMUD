# server realtime websocket handler

> 120 nodes

## Key Concepts

- **websocket_handler.py** (65 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_helpers.py** (42 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **websocket_handler_message_loop.py** (27 connections) — `server/realtime/websocket_handler_message_loop.py`
- **websocket_handler_connection.py** (18 connections) — `server/realtime/websocket_handler_connection.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **validate_occupant_name()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (9 connections)
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_occupant_names()** (8 connections) — `server/realtime/websocket_helpers.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **WebSocket** (7 connections)
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **cleanup_websocket_connection()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- *... and 95 more nodes in this community*

## Relationships

- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (18 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (16 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server realtime occupant display](server_realtime_occupant_display.md) (10 shared connections)
- [server realtime message validator](server_realtime_message_validator.md) (8 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (8 shared connections)
- [server realtime websocket handler app](server_realtime_websocket_handler_app.md) (7 shared connections)
- [server error types errormessages](server_error_types_errormessages.md) (4 shared connections)
- [room](room.md) (4 shared connections)
- [playercombatservice](playercombatservice.md) (3 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (3 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (3 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 280 (94%)
- INFERRED: 19 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*