# chat_service.py

> 91 nodes

## Key Concepts

- **chat_service.py** (61 connections) — `server/game/chat_service.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **test_chat_message_senders.py** (28 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **send_local_message()** (18 connections) — `server/game/chat_message_senders.py`
- **send_predefined_emote()** (17 connections) — `server/game/chat_message_senders.py`
- **chat_logger.py** (17 connections) — `server/services/chat_logger.py`
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
- **services/rate_limiter.py** (10 connections) — `server/services/rate_limiter.py`
- **ChatEmoteService** (9 connections) — `server/game/chat_channel_message_senders.py`
- **normalize_player_id()** (8 connections) — `server/game/chat_message_senders.py`
- **validate_say_message()** (7 connections) — `server/game/chat_validation_helpers.py`
- **test_send_global_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_rate_limit_and_nats_fail()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_validation_and_auth()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- *... and 66 more nodes in this community*

## Relationships

- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (37 shared connections)
- [ChatMessage](ChatMessage.md) (27 shared connections)
- [ChatService](ChatService.md) (15 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (7 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (5 shared connections)
- [ChatModeration](ChatModeration.md) (3 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (3 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (3 shared connections)
- [user_manager.py](user_manager.py.md) (2 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [UserManager](UserManager.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/services/chat_logger.py`
- `server/services/rate_limiter.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 299 (92%)
- INFERRED: 26 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*