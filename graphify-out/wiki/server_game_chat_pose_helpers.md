# server game chat pose helpers

> 27 nodes

## Key Concepts

- **test_chat_pose_helpers.py** (18 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **set_player_pose()** (15 connections) — `server/game/chat_pose_helpers.py`
- **chat_pose_helpers.py** (15 connections) — `server/game/chat_pose_helpers.py`
- **clear_player_pose()** (7 connections) — `server/game/chat_pose_helpers.py`
- **get_player_pose()** (7 connections) — `server/game/chat_pose_helpers.py`
- **asyncio** (7 connections)
- **get_room_poses()** (6 connections) — `server/game/chat_pose_helpers.py`
- **normalize_player_id()** (6 connections) — `server/game/chat_pose_helpers.py`
- **Any** (5 connections)
- **test_get_room_poses()** (4 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **UUID** (4 connections)
- **test_get_and_clear_player_pose()** (3 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_empty()** (3 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_nats_failure()** (3 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_no_room()** (3 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_player_not_found()** (3 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_success()** (3 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_too_long()** (3 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **_player()** (2 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_normalize_player_id()** (2 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **Pose management helpers for chat service.** (1 connections) — `server/game/chat_pose_helpers.py`
- **Clear a player's pose. Args: player_id: ID of the player pose_manager: Pose…** (1 connections) — `server/game/chat_pose_helpers.py`
- **Get all poses for players in a room. Args: room_id: ID of the room…** (1 connections) — `server/game/chat_pose_helpers.py`
- **Normalize player identifiers to string form.** (1 connections) — `server/game/chat_pose_helpers.py`
- **Set a player's pose (temporary, in-memory only). Args: player_id: ID of the…** (1 connections) — `server/game/chat_pose_helpers.py`
- *... and 2 more nodes in this community*

## Relationships

- [chatresult](chatresult.md) (5 shared connections)
- [server game chat nats publisher](server_game_chat_nats_publisher.md) (3 shared connections)
- [server game chat message chatmessage](server_game_chat_message_chatmessage.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server game chat message](server_game_chat_message.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/game/chat_pose_helpers.py`
- `server/tests/unit/game/test_chat_pose_helpers.py`

## Audit Trail

- EXTRACTED: 69 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*