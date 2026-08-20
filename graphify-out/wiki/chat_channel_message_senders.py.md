# chat_channel_message_senders.py

> 39 nodes

## Key Concepts

- **chat_channel_message_senders.py** (40 connections) — `server/game/chat_channel_message_senders.py`
- **ChatSendServices** (20 connections) — `server/game/chat_channel_message_senders.py`
- **send_whisper_message()** (17 connections) — `server/game/chat_channel_message_senders.py`
- **send_system_message()** (16 connections) — `server/game/chat_channel_message_senders.py`
- **send_global_message()** (14 connections) — `server/game/chat_channel_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_channel_message_senders.py`
- **ChatResult** (10 connections)
- **ChatPlayerView** (9 connections) — `server/game/chat_channel_message_senders.py`
- **_publish_chat_or_unavailable()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **WhisperTracker** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_whisper_message()** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_authorize_global_sender()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_system_message()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **normalize_player_id()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **ChatMessage** (7 connections)
- **_append_channel_history()** (6 connections) — `server/game/chat_channel_message_senders.py`
- **UUID** (6 connections)
- **_authorize_system_sender()** (5 connections) — `server/game/chat_channel_message_senders.py`
- **_load_whisper_participants()** (5 connections) — `server/game/chat_channel_message_senders.py`
- **check_global_level_requirement()** (5 connections) — `server/game/chat_validation_helpers.py`
- **validate_global_message()** (5 connections) — `server/game/chat_validation_helpers.py`
- **.get_player_by_id()** (3 connections) — `server/game/chat_channel_message_senders.py`
- **_system_message_input_error()** (3 connections) — `server/game/chat_channel_message_senders.py`
- **_whisper_message_input_error()** (3 connections) — `server/game/chat_channel_message_senders.py`
- **.store_sender()** (2 connections) — `server/game/chat_channel_message_senders.py`
- *... and 14 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (31 shared connections)
- [ChatMessage](ChatMessage.md) (20 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (4 shared connections)
- [ChatService](ChatService.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_validation_helpers.py`

## Audit Trail

- EXTRACTED: 146 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*