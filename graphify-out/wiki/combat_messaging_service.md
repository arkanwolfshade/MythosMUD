# combat messaging service

> 26 nodes

## Key Concepts

- **test_chat_pose_helpers.py** (17 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **chat_pose_helpers.py** (15 connections) — `server/game/chat_pose_helpers.py`
- **set_player_pose()** (15 connections) — `server/game/chat_pose_helpers.py`
- **get_player_pose()** (7 connections) — `server/game/chat_pose_helpers.py`
- **clear_player_pose()** (7 connections) — `server/game/chat_pose_helpers.py`
- **normalize_player_id()** (6 connections) — `server/game/chat_pose_helpers.py`
- **get_room_poses()** (6 connections) — `server/game/chat_pose_helpers.py`
- **Any** (5 connections)
- **UUID** (4 connections)
- **test_get_and_clear_player_pose()** (3 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_get_room_poses()** (3 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_normalize_player_id()** (2 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_empty()** (2 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_too_long()** (2 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_player_not_found()** (2 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_no_room()** (2 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_success()** (2 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **test_set_player_pose_nats_failure()** (2 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **_player()** (2 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **Pose management helpers for chat service.** (1 connections) — `server/game/chat_pose_helpers.py`
- **Normalize player identifiers to string form.** (1 connections) — `server/game/chat_pose_helpers.py`
- **Set a player's pose (temporary, in-memory only).      Args:         player_id: I** (1 connections) — `server/game/chat_pose_helpers.py`
- **Get a player's current pose.      Args:         player_id: ID of the player** (1 connections) — `server/game/chat_pose_helpers.py`
- **Clear a player's pose.      Args:         player_id: ID of the player         po** (1 connections) — `server/game/chat_pose_helpers.py`
- **Get all poses for players in a room.      Args:         room_id: ID of the room** (1 connections) — `server/game/chat_pose_helpers.py`
- *... and 1 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (5 shared connections)
- [quest chat game](quest_chat_game.md) (3 shared connections)
- [alias command models](alias_command_models.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)

## Source Files

- `server/game/chat_pose_helpers.py`
- `server/tests/unit/game/test_chat_pose_helpers.py`

## Audit Trail

- EXTRACTED: 111 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*