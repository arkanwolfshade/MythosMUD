# chat_service.py

> 104 nodes

## Key Concepts

- **chat_service.py** (61 connections) — `server/game/chat_service.py`
- **chat_channel_message_senders.py** (40 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **ChatSendServices** (20 connections) — `server/game/chat_channel_message_senders.py`
- **send_local_message()** (18 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (17 connections) — `server/game/chat_channel_message_senders.py`
- **send_predefined_emote()** (17 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (16 connections) — `server/game/chat_channel_message_senders.py`
- **send_global_message()** (14 connections) — `server/game/chat_channel_message_senders.py`
- **send_party_message()** (14 connections) — `server/game/chat_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatRateLimiter** (12 connections) — `server/game/chat_channel_message_senders.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **ChatPlayerService** (11 connections) — `server/game/chat_channel_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_channel_message_senders.py`
- **check_channel_permissions()** (10 connections) — `server/game/chat_validation_helpers.py`
- **ChatResult** (10 connections)
- **ChatEmoteService** (9 connections) — `server/game/chat_channel_message_senders.py`
- **ChatPlayerView** (9 connections) — `server/game/chat_channel_message_senders.py`
- **_publish_chat_or_unavailable()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **WhisperTracker** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_whisper_message()** (8 connections) — `server/game/chat_channel_message_senders.py`
- **normalize_player_id()** (8 connections) — `server/game/chat_message_senders.py`
- **_authorize_global_sender()** (7 connections) — `server/game/chat_channel_message_senders.py`
- *... and 79 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (31 shared connections)
- [test_chat_message_senders.py](test_chat_message_senders.py.md) (22 shared connections)
- [ChatService](ChatService.md) (18 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (11 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (5 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (3 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [ChatModeration](ChatModeration.md) (1 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (1 shared connections)
- [ChatWhisperTracker](ChatWhisperTracker.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 320 (93%)
- INFERRED: 25 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*