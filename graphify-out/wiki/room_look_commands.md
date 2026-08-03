# room look commands

> 119 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **websocket_handler_message_loop.py** (26 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_chat_message()** (18 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_system_message.py** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (4 connections)
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_websocket_handler_json_error.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **UUID** (3 connections)
- *... and 94 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (18 shared connections)
- [models npc rationale](models_npc_rationale.md) (10 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (10 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (9 shared connections)
- [room websocket updates](room_websocket_updates.md) (9 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (9 shared connections)
- [realtime player connection](realtime_player_connection.md) (7 shared connections)
- [combat services messaging](combat_services_messaging.md) (6 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (5 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (4 shared connections)
- [realtime message validator](realtime_message_validator.md) (4 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`

## Audit Trail

- EXTRACTED: 434 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*