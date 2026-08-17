# chat_service.py

> 85 nodes

## Key Concepts

- **chat_service.py** (59 connections) — `server/game/chat_service.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **chat_message.py** (19 connections) — `server/game/chat_message.py`
- **send_local_message()** (18 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (17 connections) — `server/game/chat_message_senders.py`
- **create_and_log_chat_message()** (14 connections) — `server/game/chat_message_helpers.py`
- **send_party_message()** (14 connections) — `server/game/chat_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **ChatRateLimiter** (12 connections) — `server/game/chat_channel_message_senders.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **ChatPlayerService** (11 connections) — `server/game/chat_channel_message_senders.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **.send_say_message()** (11 connections) — `server/game/chat_service.py`
- **check_channel_permissions()** (10 connections) — `server/game/chat_validation_helpers.py`
- **normalize_player_id()** (8 connections) — `server/game/chat_message_senders.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **store_global_message_in_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **_publish_room_chat()** (6 connections) — `server/game/chat_service.py`
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- **Protocol** (6 connections)
- **Any** (6 connections)
- *... and 60 more nodes in this community*

## Relationships

- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (31 shared connections)
- [ChatMessage](ChatMessage.md) (26 shared connections)
- [ChatService](ChatService.md) (17 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (10 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (10 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (6 shared connections)
- [ChatModeration](ChatModeration.md) (4 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (4 shared connections)
- [EmoteService](EmoteService.md) (2 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (2 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 260 (92%)
- INFERRED: 23 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*