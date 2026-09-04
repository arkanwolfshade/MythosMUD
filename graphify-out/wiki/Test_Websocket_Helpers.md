# Test Websocket Helpers

> 132 nodes

## Key Concepts

- **websocket_handler.py** (54 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_helpers.py** (42 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **websocket_helpers.py** (36 connections) — `server/realtime/websocket_helpers.py`
- **websocket_handler_message_loop.py** (24 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_shutdown_and_reject()** (11 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **logging_context.py** (11 connections) — `server/structured_logging/logging_context.py`
- **test_websocket_correlation_context.py** (11 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_npc_name_from_instance()** (10 connections) — `server/realtime/websocket_helpers.py`
- **handle_websocket_message_loop()** (9 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **load_player_mute_data()** (9 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (9 connections)
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **send_websocket_error_response()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- *... and 107 more nodes in this community*

## Relationships

- [Test Websocket Initial State](Test_Websocket_Initial_State.md) (14 shared connections)
- [Test Websocket Helpers Player](Test_Websocket_Helpers_Player.md) (12 shared connections)
- [Test Websocket Handler App State](Test_Websocket_Handler_App_State.md) (8 shared connections)
- [Test Websocket Handler Validation Errors](Test_Websocket_Handler_Validation_Errors.md) (8 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (8 shared connections)
- [Test Websocket Handler Coverage Gaps](Test_Websocket_Handler_Coverage_Gaps.md) (7 shared connections)
- [Test Message Validator](Test_Message_Validator.md) (7 shared connections)
- [Test Websocket Room Updates](Test_Websocket_Room_Updates.md) (7 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (5 shared connections)
- [Websocket Integration](Websocket_Integration.md) (5 shared connections)
- [Websocket Handler Commands](Websocket_Handler_Commands.md) (4 shared connections)
- [Player Event Handlers Respawn Room](Player_Event_Handlers_Respawn_Room.md) (3 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/realtime/test_websocket_correlation_context.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 329 (94%)
- INFERRED: 20 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*