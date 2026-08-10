# Combat Command Helpers

> 69 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (25 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_error_handling.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **test_websocket_handler_rate_limit.py** (7 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **handle_websocket_runtime_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_websocket_disconnect_message()** (6 connections) — `server/realtime/websocket_helpers.py`
- **process_websocket_inbound_message()** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_websocket_handler_json_error.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **Exception** (3 connections)
- **test_handle_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_handle_websocket_disconnect_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **mock_websocket()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **test_send_error_response_success()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **test_send_error_response_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- *... and 44 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (12 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (12 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (10 shared connections)
- [Database Helper Tests](Database_Helper_Tests.md) (8 shared connections)
- [Logout and Quit Commands](Logout_and_Quit_Commands.md) (6 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (3 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (2 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (2 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (1 shared connections)
- [Combat Feature Flags](Combat_Feature_Flags.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`

## Audit Trail

- EXTRACTED: 260 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*