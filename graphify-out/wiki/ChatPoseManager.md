# ChatPoseManager

> 30 nodes

## Key Concepts

- **ChatPoseManager** (11 connections) — `server/game/chat_pose_manager.py`
- **ChatWhisperTracker** (10 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (8 connections) — `server/game/chat_service.py`
- **.normalize_player_id()** (5 connections) — `server/game/chat_pose_manager.py`
- **chat_pose_manager.py** (5 connections) — `server/game/chat_pose_manager.py`
- **.clear_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.get_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.set_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.get_all_poses()** (2 connections) — `server/game/chat_pose_manager.py`
- **.__init__()** (2 connections) — `server/game/chat_pose_manager.py`
- **.clear_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_all_trackings()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.store_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **Chat pose management utilities. This module provides pose management…** (1 connections) — `server/game/chat_pose_manager.py`
- **Manages in-memory storage of player poses.** (1 connections) — `server/game/chat_pose_manager.py`
- **Initialize the pose manager.** (1 connections) — `server/game/chat_pose_manager.py`
- **Normalize player identifiers to string form.** (1 connections) — `server/game/chat_pose_manager.py`
- **Set a player's pose in memory. Args: player_id: ID of the player pose: Pose…** (1 connections) — `server/game/chat_pose_manager.py`
- **Get a player's current pose. Args: player_id: ID of the player Returns: Current…** (1 connections) — `server/game/chat_pose_manager.py`
- **Clear a player's pose. Args: player_id: ID of the player Returns: True if pose…** (1 connections) — `server/game/chat_pose_manager.py`
- **Get all poses (for testing/debugging). Returns: Dictionary mapping player IDs…** (1 connections) — `server/game/chat_pose_manager.py`
- **Initialize chat service. Args: persistence: Database persistence layer…** (1 connections) — `server/game/chat_service.py`
- **Tracks last whisper senders for reply functionality.** (1 connections) — `server/game/chat_whisper_tracker.py`
- *... and 5 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (3 shared connections)
- [ChatService](ChatService.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [ChatModeration](ChatModeration.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)

## Source Files

- `server/game/chat_pose_manager.py`
- `server/game/chat_service.py`
- `server/game/chat_whisper_tracker.py`

## Audit Trail

- EXTRACTED: 42 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*