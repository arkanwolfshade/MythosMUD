# Server Game (22)

> 45 nodes

## Key Concepts

- **chat_message_senders.py** (25 connections) — `server/game/chat_message_senders.py`
- **publish_chat_message_to_nats()** (24 connections) — `server/game/chat_nats_publisher.py`
- **send_global_message()** (12 connections) — `server/game/chat_message_senders.py`
- **send_local_message()** (11 connections) — `server/game/chat_message_senders.py`
- **chat_message_helpers.py** (10 connections) — `server/game/chat_message_helpers.py`
- **chat_validation_helpers.py** (10 connections) — `server/game/chat_validation_helpers.py`
- **create_and_log_chat_message()** (9 connections) — `server/game/chat_message_helpers.py`
- **normalize_player_id()** (9 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (9 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (8 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (8 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (8 connections) — `server/game/chat_message_senders.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **check_channel_permissions()** (7 connections) — `server/game/chat_validation_helpers.py`
- **store_message_in_room_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **ChatMessage** (6 connections)
- **Any** (6 connections)
- **validate_say_message()** (5 connections) — `server/game/chat_validation_helpers.py`
- **validate_global_message()** (5 connections) — `server/game/chat_validation_helpers.py`
- **check_global_level_requirement()** (5 connections) — `server/game/chat_validation_helpers.py`
- **store_global_message_in_history()** (4 connections) — `server/game/chat_message_helpers.py`
- **check_say_permissions()** (4 connections) — `server/game/chat_validation_helpers.py`
- **create_and_log_say_message()** (3 connections) — `server/game/chat_message_helpers.py`
- **validate_emote_action()** (3 connections) — `server/game/chat_validation_helpers.py`
- *... and 20 more nodes in this community*

## Relationships

- [Server Game (11)](Server_Game_%2811%29.md) (21 shared connections)
- [Server Game (16)](Server_Game_%2816%29.md) (8 shared connections)
- [Server Commands](Server_Commands.md) (5 shared connections)
- [Server Commands (10)](Server_Commands_%2810%29.md) (2 shared connections)
- [Server Game (13)](Server_Game_%2813%29.md) (2 shared connections)

## Source Files

- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_validation_helpers.py`

## Audit Trail

- EXTRACTED: 232 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*