# chat_service.py

> 91 nodes

## Key Concepts

- **chat_service.py** (61 connections) — `server/game/chat_service.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **test_chat_message_senders.py** (27 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **send_local_message()** (18 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (17 connections) — `server/game/chat_message_senders.py`
- **send_party_message()** (14 connections) — `server/game/chat_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **_attr()** (13 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **asyncio** (13 connections)
- **ChatRateLimiter** (12 connections) — `server/game/chat_channel_message_senders.py`
- **_ctx()** (12 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **ChatPlayerService** (11 connections) — `server/game/chat_channel_message_senders.py`
- **_player()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **check_channel_permissions()** (10 connections) — `server/game/chat_validation_helpers.py`
- **ChatEmoteService** (9 connections) — `server/game/chat_channel_message_senders.py`
- **normalize_player_id()** (8 connections) — `server/game/chat_message_senders.py`
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **test_send_global_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_rate_limit_and_nats_fail()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_validation_and_auth()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_whisper_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **Protocol** (7 connections)
- *... and 66 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (63 shared connections)
- [ChatService](ChatService.md) (15 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (7 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (5 shared connections)
- [ChatModeration](ChatModeration.md) (4 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (3 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (2 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 280 (92%)
- INFERRED: 26 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*