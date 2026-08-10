# Player Effects API

> 14 nodes

## Key Concepts

- **chat_pose_helpers.py** (14 connections) — `server/game/chat_pose_helpers.py`
- **set_player_pose()** (8 connections) — `server/game/chat_pose_helpers.py`
- **Any** (5 connections)
- **get_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **clear_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **normalize_player_id()** (4 connections) — `server/game/chat_pose_helpers.py`
- **UUID** (4 connections)
- **get_room_poses()** (4 connections) — `server/game/chat_pose_helpers.py`
- **Pose management helpers for chat service.** (1 connections) — `server/game/chat_pose_helpers.py`
- **Normalize player identifiers to string form.** (1 connections) — `server/game/chat_pose_helpers.py`
- **Set a player's pose (temporary, in-memory only).      Args:         player_id: I** (1 connections) — `server/game/chat_pose_helpers.py`
- **Get a player's current pose.      Args:         player_id: ID of the player** (1 connections) — `server/game/chat_pose_helpers.py`
- **Clear a player's pose.      Args:         player_id: ID of the player         po** (1 connections) — `server/game/chat_pose_helpers.py`
- **Get all poses for players in a room.      Args:         room_id: ID of the room** (1 connections) — `server/game/chat_pose_helpers.py`

## Relationships

- [Chat Message Helpers](Chat_Message_Helpers.md) (10 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/game/chat_pose_helpers.py`

## Audit Trail

- EXTRACTED: 55 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*