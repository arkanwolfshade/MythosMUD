# Application DI Bundles

> 83 nodes

## Key Concepts

- **test_websocket_handler_validation_errors.py** (39 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_system_message.py** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **WebSocket** (4 connections)
- **test_send_system_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_chat()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_system_message_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_warning()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_disconnected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_validate_message_validation_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_restores_csrf_from_message_jwt_when_metadata_token_missing()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_broadcast()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_system_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_process_websocket_command_player_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **mock_websocket()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_is_websocket_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- *... and 58 more nodes in this community*

## Relationships

- [Player Combat XP](Player_Combat_XP.md) (12 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (7 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (4 shared connections)
- [Database Helper Tests](Database_Helper_Tests.md) (4 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (1 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 201 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*