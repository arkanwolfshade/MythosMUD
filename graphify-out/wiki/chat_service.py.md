# chat_service.py

> 64 nodes

## Key Concepts

- **chat_service.py** (59 connections) — `server/game/chat_service.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **send_local_message()** (18 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (17 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (14 connections) — `server/game/chat_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatRateLimiter** (12 connections) — `server/game/chat_channel_message_senders.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **ChatPlayerService** (11 connections) — `server/game/chat_channel_message_senders.py`
- **check_channel_permissions()** (10 connections) — `server/game/chat_validation_helpers.py`
- **normalize_player_id()** (8 connections) — `server/game/chat_message_senders.py`
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **check_say_permissions()** (6 connections) — `server/game/chat_validation_helpers.py`
- **Protocol** (6 connections)
- **Any** (6 connections)
- **validate_emote_action()** (5 connections) — `server/game/chat_validation_helpers.py`
- **validate_global_message()** (5 connections) — `server/game/chat_validation_helpers.py`
- **UUID** (5 connections)
- **.get_player_by_id()** (3 connections) — `server/game/chat_channel_message_senders.py`
- **ChatMessage** (3 connections)
- **.log_chat_message()** (2 connections) — `server/game/chat_channel_message_senders.py`
- **.log_global_channel_message()** (2 connections) — `server/game/chat_channel_message_senders.py`
- **.log_system_channel_message()** (2 connections) — `server/game/chat_channel_message_senders.py`
- **.log_whisper_channel_message()** (2 connections) — `server/game/chat_channel_message_senders.py`
- *... and 39 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (41 shared connections)
- [ChatService](ChatService.md) (14 shared connections)
- [chat_message.py](chat_message.py.md) (11 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (7 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (5 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (4 shared connections)
- [ChatModeration](ChatModeration.md) (3 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (3 shared connections)
- [EmoteService](EmoteService.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 195 (92%)
- INFERRED: 18 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*