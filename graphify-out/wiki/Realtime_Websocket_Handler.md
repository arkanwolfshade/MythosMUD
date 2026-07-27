# Realtime Websocket Handler

> 17 nodes · cohesion 0.15

## Key Concepts

- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_system_message.py** (7 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_system_message_disconnected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_warning()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **mock_websocket()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Test send_system_message() with warning type.** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Test send_system_message sends system message.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Unit tests for websocket handler system message functions.  Tests the system mes** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Create a mock WebSocket.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Test send_system_message() successfully sends message.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Test send_system_message() handles WebSocket disconnection.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Test send_system_message handles error.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **Send a system message to a player.      Args:         websocket: The WebSocket c** (1 connections) — `server/realtime/websocket_handler.py`

## Relationships

- [[Help and WebSocket Core]] (2 shared connections)
- [[WebSocket Handler Helpers]] (2 shared connections)
- [[Combat Player Broadcasts]] (1 shared connections)
- [[WebSocket Message Validation]] (1 shared connections)
- [[WebSocket Message Validator]] (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
