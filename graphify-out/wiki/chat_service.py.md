# chat_service.py

> 43 nodes

## Key Concepts

- **chat_service.py** (33 connections) — `server/game/chat_service.py`
- **ChatMessage** (27 connections) — `server/game/chat_message.py`
- **chat_pose_helpers.py** (14 connections) — `server/game/chat_pose_helpers.py`
- **chat_message.py** (13 connections) — `server/game/chat_message.py`
- **set_player_pose()** (8 connections) — `server/game/chat_pose_helpers.py`
- **clear_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **get_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **Any** (5 connections)
- **get_room_poses()** (4 connections) — `server/game/chat_pose_helpers.py`
- **normalize_player_id()** (4 connections) — `server/game/chat_pose_helpers.py`
- **test_get_room_messages()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **UUID** (4 connections)
- **.to_dict()** (3 connections) — `server/game/chat_message.py`
- **test_chat_message_init()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_init_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_log_message()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_echo_sent()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **.__init__()** (2 connections) — `server/game/chat_message.py`
- **.log_message()** (2 connections) — `server/game/chat_message.py`
- **UUID** (2 connections)
- **vulture_allowlist.py** (2 connections) — `vulture_allowlist.py`
- **Any** (1 connections)
- **Chat message model for MythosMUD. This module provides the ChatMessage class…** (1 connections) — `server/game/chat_message.py`
- *... and 18 more nodes in this community*

## Relationships

- [chat_message_senders.py](chat_message_senders.py.md) (16 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_chat_service.py](test_chat_service.py.md) (10 shared connections)
- [chat_nats_publisher.py](chat_nats_publisher.py.md) (7 shared connections)
- [ChatService](ChatService.md) (4 shared connections)
- [ChatModeration](ChatModeration.md) (2 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (2 shared connections)
- [UserManagerProtocol](UserManagerProtocol.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_service.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 174 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*