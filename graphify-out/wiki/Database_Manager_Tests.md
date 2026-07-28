# Database Manager Tests

> 118 nodes · cohesion 0.02

## Key Concepts

- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_websocket_handler_coverage_gaps.py** (24 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **handle_chat_message()** (18 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_system_message.py** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **WebSocket** (4 connections)
- **UUID** (3 connections)
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_with_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_chat_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_empty_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception_should_break()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_chat()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_type_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_system_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_chat_message_exception_handling()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- *... and 93 more nodes in this community*

## Relationships

- [WebSocket Command Handler](WebSocket_Command_Handler.md) (22 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (9 shared connections)
- [WebSocket Message Validator](WebSocket_Message_Validator.md) (7 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (5 shared connections)
- [WebSocket Helper Utilities](WebSocket_Helper_Utilities.md) (4 shared connections)
- [Look Item Command Tests](Look_Item_Command_Tests.md) (4 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (3 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Services Service Room](Services_Service_Room.md) (1 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`

## Audit Trail

- EXTRACTED: 327 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*