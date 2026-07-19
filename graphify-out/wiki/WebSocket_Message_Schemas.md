# WebSocket Message Schemas

> 58 nodes · cohesion 0.06

## Key Concepts

- **test_websocket_messages.py** (31 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **ChatMessageData** (11 connections) — `server/schemas/realtime/websocket_messages.py`
- **CommandMessageData** (11 connections) — `server/schemas/realtime/websocket_messages.py`
- **BaseWebSocketMessage** (10 connections) — `server/schemas/realtime/websocket_messages.py`
- **websocket_messages.py** (8 connections) — `server/schemas/realtime/websocket_messages.py`
- **ChatMessage** (7 connections) — `server/schemas/realtime/websocket_messages.py`
- **CommandMessage** (7 connections) — `server/schemas/realtime/websocket_messages.py`
- **PingMessage** (7 connections) — `server/schemas/realtime/websocket_messages.py`
- **WrappedMessage** (7 connections) — `server/schemas/realtime/websocket_messages.py`
- **test_chat_message()** (4 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_chat_message_rejects_extra_fields()** (4 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_chat_message_with_channel()** (4 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_command_message()** (4 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_command_message_rejects_extra_fields()** (4 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_command_message_with_csrf_token()** (4 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **Test ChatMessage with channel.** (3 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_base_websocket_message()** (3 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_base_websocket_message_with_csrf_token()** (3 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_base_websocket_message_with_timestamp()** (3 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_chat_message_data()** (3 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_chat_message_data_no_channel()** (3 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_chat_message_data_validation_error()** (3 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_chat_message_data_with_channel()** (3 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_command_message_data()** (3 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- **test_command_message_data_empty_args()** (3 connections) — `server/tests/unit/schemas/test_websocket_messages.py`
- *... and 33 more nodes in this community*

## Relationships

- [[Admin NPC Schemas]] (4 shared connections)
- [[NATS Message Schemas]] (1 shared connections)

## Source Files

- `server/schemas/realtime/websocket_messages.py`
- `server/tests/unit/schemas/test_websocket_messages.py`

## Audit Trail

- EXTRACTED: 205 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
