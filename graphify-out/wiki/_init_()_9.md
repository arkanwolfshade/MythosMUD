# . init ()

> 28 nodes

## Key Concepts

- **ChatPoseManager** (11 connections) — `server/game/chat_pose_manager.py`
- **ChatWhisperTracker** (10 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (7 connections) — `server/game/chat_service.py`
- **.normalize_player_id()** (5 connections) — `server/game/chat_pose_manager.py`
- **.set_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.get_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.clear_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.__init__()** (2 connections) — `server/game/chat_pose_manager.py`
- **.get_all_poses()** (2 connections) — `server/game/chat_pose_manager.py`
- **.__init__()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.store_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.clear_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_all_trackings()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **Manages in-memory storage of player poses.** (1 connections) — `server/game/chat_pose_manager.py`
- **Initialize the pose manager.** (1 connections) — `server/game/chat_pose_manager.py`
- **Normalize player identifiers to string form.** (1 connections) — `server/game/chat_pose_manager.py`
- **Set a player's pose in memory.          Args:             player_id: ID of the p** (1 connections) — `server/game/chat_pose_manager.py`
- **Get a player's current pose.          Args:             player_id: ID of the pla** (1 connections) — `server/game/chat_pose_manager.py`
- **Clear a player's pose.          Args:             player_id: ID of the player** (1 connections) — `server/game/chat_pose_manager.py`
- **Get all poses (for testing/debugging).          Returns:             Dictionary** (1 connections) — `server/game/chat_pose_manager.py`
- **Initialize chat service.          Args:             persistence: Database persis** (1 connections) — `server/game/chat_service.py`
- **Tracks last whisper senders for reply functionality.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Initialize the whisper tracker.** (1 connections) — `server/game/chat_whisper_tracker.py`
- **Store the last whisper sender for a player.          Args:             receiver_** (1 connections) — `server/game/chat_whisper_tracker.py`
- *... and 3 more nodes in this community*

## Relationships

- [ChatService](ChatService.md) (4 shared connections)
- [world](world.md) (2 shared connections)
- [ChatMessage](ChatMessage.md) (2 shared connections)
- [player preferences service](player_preferences_service.md) (1 shared connections)
- [CorpseNotFoundError](CorpseNotFoundError.md) (1 shared connections)

## Source Files

- `server/game/chat_pose_manager.py`
- `server/game/chat_service.py`
- `server/game/chat_whisper_tracker.py`

## Audit Trail

- EXTRACTED: 67 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*