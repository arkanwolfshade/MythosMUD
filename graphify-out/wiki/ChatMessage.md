# ChatMessage

> 74 nodes

## Key Concepts

- **ChatMessage** (60 connections) — `server/game/chat_message.py`
- **chat_channel_message_senders.py** (40 connections) — `server/game/chat_channel_message_senders.py`
- **ChatSendServices** (20 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message.py** (19 connections) — `server/game/chat_message.py`
- **send_whisper_message()** (17 connections) — `server/game/chat_channel_message_senders.py`
- **send_system_message()** (16 connections) — `server/game/chat_channel_message_senders.py`
- **send_global_message()** (14 connections) — `server/game/chat_channel_message_senders.py`
- **create_and_log_chat_message()** (14 connections) — `server/game/chat_message_helpers.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **send_party_message()** (11 connections) — `server/game/chat_channel_message_senders.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **ChatResult** (10 connections)
- **ChatPlayerView** (9 connections) — `server/game/chat_channel_message_senders.py`
- **_publish_chat_or_unavailable()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **WhisperTracker** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_whisper_message()** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_authorize_global_sender()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_system_message()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **normalize_player_id()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- **ChatMessage** (7 connections)
- **_append_channel_history()** (6 connections) — `server/game/chat_channel_message_senders.py`
- **store_global_message_in_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **UUID** (6 connections)
- *... and 49 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (63 shared connections)
- [ChatService](ChatService.md) (18 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (15 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (9 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (3 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 252 (92%)
- INFERRED: 23 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*