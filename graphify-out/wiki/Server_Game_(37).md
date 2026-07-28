# Server Game (37)

> 14 nodes

## Key Concepts

- **ChatPoseManager** (8 connections) — `server/game/chat_pose_manager.py`
- **.normalize_player_id()** (5 connections) — `server/game/chat_pose_manager.py`
- **.set_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.get_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.clear_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.__init__()** (2 connections) — `server/game/chat_pose_manager.py`
- **.get_all_poses()** (2 connections) — `server/game/chat_pose_manager.py`
- **Manages in-memory storage of player poses.** (1 connections) — `server/game/chat_pose_manager.py`
- **Initialize the pose manager.** (1 connections) — `server/game/chat_pose_manager.py`
- **Normalize player identifiers to string form.** (1 connections) — `server/game/chat_pose_manager.py`
- **Set a player's pose in memory.          Args:             player_id: ID of the p** (1 connections) — `server/game/chat_pose_manager.py`
- **Get a player's current pose.          Args:             player_id: ID of the pla** (1 connections) — `server/game/chat_pose_manager.py`
- **Clear a player's pose.          Args:             player_id: ID of the player** (1 connections) — `server/game/chat_pose_manager.py`
- **Get all poses (for testing/debugging).          Returns:             Dictionary** (1 connections) — `server/game/chat_pose_manager.py`

## Relationships

- [Server Commands](Server_Commands.md) (1 shared connections)

## Source Files

- `server/game/chat_pose_manager.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*