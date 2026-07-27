# Chat Message Helpers

> 64 nodes · cohesion 0.08

## Key Concepts

- **chat_service.py** (44 connections) — `server/game/chat_service.py`
- **ChatMessage** (34 connections) — `server/game/chat_message.py`
- **chat_message_senders.py** (26 connections) — `server/game/chat_message_senders.py`
- **EmoteService** (21 connections) — `server/game/emote_service.py`
- **publish_chat_message_to_nats()** (18 connections) — `server/game/chat_nats_publisher.py`
- **send_global_message()** (13 connections) — `server/game/chat_message_senders.py`
- **send_local_message()** (12 connections) — `server/game/chat_message_senders.py`
- **chat_validation_helpers.py** (11 connections) — `server/game/chat_validation_helpers.py`
- **chat_message_helpers.py** (10 connections) — `server/game/chat_message_helpers.py`
- **send_predefined_emote()** (10 connections) — `server/game/chat_message_senders.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **.send_say_message()** (10 connections) — `server/game/chat_service.py`
- **create_and_log_chat_message()** (9 connections) — `server/game/chat_message_helpers.py`
- **normalize_player_id()** (9 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (9 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (9 connections) — `server/game/chat_message_senders.py`
- **check_channel_permissions()** (9 connections) — `server/game/chat_validation_helpers.py`
- **Any** (9 connections) — `server/game/chat_message_senders.py`
- **UUID** (9 connections) — `server/game/chat_message_senders.py`
- **ChatMessage** (8 connections) — `server/game/chat_message_senders.py`
- **store_message_in_room_history()** (7 connections) — `server/game/chat_message_helpers.py`
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- **Any** (6 connections) — `server/game/chat_validation_helpers.py`
- *... and 39 more nodes in this community*

## Relationships

- [[Chat NATS Publisher]] (20 shared connections)
- [[NPC Admin API]] (19 shared connections)
- [[Chat Service Whispers]] (12 shared connections)
- [[Chat Mute Admin API]] (12 shared connections)
- [[Game Emote Service]] (5 shared connections)
- [[Emote Schema Validator]] (3 shared connections)
- [[Chat Moderation Service]] (2 shared connections)
- [[Command Input Utilities]] (2 shared connections)
- [[Alias Game Chat]] (1 shared connections)
- [[Lifespan Startup Hooks]] (1 shared connections)
- [[Game Chat Moderation]] (1 shared connections)
- [[Game Chat Pose]] (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/game/emote_service.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 373 (95%)
- INFERRED: 19 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
