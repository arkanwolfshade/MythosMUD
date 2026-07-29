# ChatMessage

> 64 nodes

## Key Concepts

- **chat_service.py** (49 connections) — `server/game/chat_service.py`
- **ChatMessage** (31 connections) — `server/game/chat_message.py`
- **chat_message_senders.py** (26 connections) — `server/game/chat_message_senders.py`
- **chat_message.py** (14 connections) — `server/game/chat_message.py`
- **send_global_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_local_message()** (12 connections) — `server/game/chat_message_senders.py`
- **chat_message_helpers.py** (11 connections) — `server/game/chat_message_helpers.py`
- **create_and_log_chat_message()** (11 connections) — `server/game/chat_message_helpers.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **send_predefined_emote()** (10 connections) — `server/game/chat_message_senders.py`
- **.send_say_message()** (10 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **store_message_in_room_history()** (9 connections) — `server/game/chat_message_helpers.py`
- **normalize_player_id()** (9 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (9 connections) — `server/game/chat_message_senders.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **ChatMessage** (6 connections)
- **Any** (6 connections)
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- **create_and_log_say_message()** (5 connections) — `server/game/chat_message_helpers.py`
- *... and 39 more nodes in this community*

## Relationships

- [ChatService](ChatService.md) (21 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (16 shared connections)
- [.initialize()](initialize%28%29.md) (16 shared connections)
- [main()](main%28%29.md) (13 shared connections)
- [chat pose helpers](chat_pose_helpers.md) (8 shared connections)
- [Any](Any.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [chat moderation](chat_moderation.md) (2 shared connections)
- [Protocol](Protocol.md) (1 shared connections)
- [message filtering](message_filtering.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 369 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*