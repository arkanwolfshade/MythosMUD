# chat_service.py

> 29 nodes

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
- **UUID** (4 connections)
- **.to_dict()** (3 connections) — `server/game/chat_message.py`
- **.__init__()** (2 connections) — `server/game/chat_message.py`
- **.log_message()** (2 connections) — `server/game/chat_message.py`
- **UUID** (2 connections)
- **vulture_allowlist.py** (2 connections) — `vulture_allowlist.py`
- **Any** (1 connections)
- **Chat message model for MythosMUD. This module provides the ChatMessage class…** (1 connections) — `server/game/chat_message.py`
- **Represents a chat message with metadata.** (1 connections) — `server/game/chat_message.py`
- **Convert message to dictionary for serialization.** (1 connections) — `server/game/chat_message.py`
- **Log this chat message to the communications log.** (1 connections) — `server/game/chat_message.py`
- **Pose management helpers for chat service.** (1 connections) — `server/game/chat_pose_helpers.py`
- **Clear a player's pose. Args: player_id: ID of the player pose_manager: Pose…** (1 connections) — `server/game/chat_pose_helpers.py`
- **Get all poses for players in a room. Args: room_id: ID of the room…** (1 connections) — `server/game/chat_pose_helpers.py`
- **Normalize player identifiers to string form.** (1 connections) — `server/game/chat_pose_helpers.py`
- *... and 4 more nodes in this community*

## Relationships

- [chat_message_senders.py](chat_message_senders.py.md) (16 shared connections)
- [ChatService](ChatService.md) (12 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [chat_nats_publisher.py](chat_nats_publisher.py.md) (7 shared connections)
- [ChatModeration](ChatModeration.md) (2 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [UserManagerProtocol](UserManagerProtocol.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [user_manager.py](user_manager.py.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_service.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 100 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*