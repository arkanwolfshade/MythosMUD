# chat_service.py

> 128 nodes

## Key Concepts

- **chat_service.py** (61 connections) — `server/game/chat_service.py`
- **ChatMessage** (60 connections) — `server/game/chat_message.py`
- **chat_channel_message_senders.py** (40 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **ChatSendServices** (20 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message.py** (19 connections) — `server/game/chat_message.py`
- **send_local_message()** (18 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (17 connections) — `server/game/chat_channel_message_senders.py`
- **send_predefined_emote()** (17 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (16 connections) — `server/game/chat_channel_message_senders.py`
- **send_global_message()** (14 connections) — `server/game/chat_channel_message_senders.py`
- **create_and_log_chat_message()** (14 connections) — `server/game/chat_message_helpers.py`
- **send_party_message()** (14 connections) — `server/game/chat_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **ChatRateLimiter** (12 connections) — `server/game/chat_channel_message_senders.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **ChatPlayerService** (11 connections) — `server/game/chat_channel_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_channel_message_senders.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **check_channel_permissions()** (10 connections) — `server/game/chat_validation_helpers.py`
- **ChatResult** (10 connections)
- **ChatEmoteService** (9 connections) — `server/game/chat_channel_message_senders.py`
- *... and 103 more nodes in this community*

## Relationships

- [ChatService](ChatService.md) (33 shared connections)
- [test_chat_message_senders.py](test_chat_message_senders.py.md) (32 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (18 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (16 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (8 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (5 shared connections)
- [ChatModeration](ChatModeration.md) (4 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (3 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (2 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (2 shared connections)
- [.to_dict](to_dict.md) (1 shared connections)

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

- EXTRACTED: 403 (91%)
- INFERRED: 39 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*