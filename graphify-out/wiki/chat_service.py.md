# chat_service.py

> 62 nodes · cohesion 0.08

## Key Concepts

- **chat_service.py** (46 connections) — `server/game/chat_service.py`
- **ChatMessage** (26 connections) — `server/game/chat_message.py`
- **chat_message_senders.py** (26 connections) — `server/game/chat_message_senders.py`
- **publish_chat_message_to_nats()** (18 connections) — `server/game/chat_nats_publisher.py`
- **send_global_message()** (13 connections) — `server/game/chat_message_senders.py`
- **chat_message.py** (12 connections) — `server/game/chat_message.py`
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
- **store_message_in_room_history()** (7 connections) — `server/game/chat_message_helpers.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **ChatMessage** (6 connections)
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- **Any** (6 connections)
- *... and 37 more nodes in this community*

## Relationships

- [ChatService](ChatService.md) (14 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [chat_nats_publisher.py](chat_nats_publisher.py.md) (11 shared connections)
- [chat_pose_helpers.py](chat_pose_helpers.py.md) (10 shared connections)
- [UUID](UUID.md) (7 shared connections)
- [EmoteService](EmoteService.md) (2 shared connections)
- [ChatModeration](ChatModeration.md) (2 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (2 shared connections)
- [ChatWhisperTracker](ChatWhisperTracker.md) (2 shared connections)
- [.to_dict](to_dict.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [dependencies.py](dependencies.py.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 363 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*