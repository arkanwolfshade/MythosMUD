# chat_service.py

> 87 nodes

## Key Concepts

- **chat_service.py** (59 connections) — `server/game/chat_service.py`
- **chat_channel_message_senders.py** (39 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **ChatSendServices** (20 connections) — `server/game/chat_channel_message_senders.py`
- **send_whisper_message()** (17 connections) — `server/game/chat_channel_message_senders.py`
- **send_system_message()** (16 connections) — `server/game/chat_channel_message_senders.py`
- **send_global_message()** (14 connections) — `server/game/chat_channel_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatRateLimiter** (12 connections) — `server/game/chat_channel_message_senders.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **ChatPlayerService** (11 connections) — `server/game/chat_channel_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_channel_message_senders.py`
- **check_channel_permissions()** (10 connections) — `server/game/chat_validation_helpers.py`
- **ChatResult** (10 connections)
- **ChatPlayerView** (9 connections) — `server/game/chat_channel_message_senders.py`
- **_publish_chat_or_unavailable()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **WhisperTracker** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_whisper_message()** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_authorize_global_sender()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_system_message()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **normalize_player_id()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **ChatMessage** (7 connections)
- **_append_channel_history()** (6 connections) — `server/game/chat_channel_message_senders.py`
- *... and 62 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (43 shared connections)
- [ChatService](ChatService.md) (17 shared connections)
- [chat_message.py](chat_message.py.md) (15 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (8 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (5 shared connections)
- [ChatModeration](ChatModeration.md) (4 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (3 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (3 shared connections)
- [EmoteService](EmoteService.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 275 (92%)
- INFERRED: 25 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*