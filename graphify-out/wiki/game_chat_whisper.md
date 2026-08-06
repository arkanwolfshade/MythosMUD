# game chat whisper

> 34 nodes

## Key Concepts

- **ChatPoseManager** (11 connections) — `server/game/chat_pose_manager.py`
- **ChatWhisperTracker** (10 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (7 connections) — `server/game/chat_service.py`
- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
- **chat_pose_manager.py** (5 connections) — `server/game/chat_pose_manager.py`
- **.normalize_player_id()** (5 connections) — `server/game/chat_pose_manager.py`
- **chat_whisper_tracker.py** (5 connections) — `server/game/chat_whisper_tracker.py`
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
- **Chat pose management utilities.  This module provides pose management functional** (1 connections) — `server/game/chat_pose_manager.py`
- **Manages in-memory storage of player poses.** (1 connections) — `server/game/chat_pose_manager.py`
- **Initialize the pose manager.** (1 connections) — `server/game/chat_pose_manager.py`
- **Normalize player identifiers to string form.** (1 connections) — `server/game/chat_pose_manager.py`
- **Set a player's pose in memory.          Args:             player_id: ID of the p** (1 connections) — `server/game/chat_pose_manager.py`
- **Get a player's current pose.          Args:             player_id: ID of the pla** (1 connections) — `server/game/chat_pose_manager.py`
- **Clear a player's pose.          Args:             player_id: ID of the player** (1 connections) — `server/game/chat_pose_manager.py`
- **Get all poses (for testing/debugging).          Returns:             Dictionary** (1 connections) — `server/game/chat_pose_manager.py`
- *... and 9 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [chat service game](chat_service_game.md) (3 shared connections)
- [chat moderation game](chat_moderation_game.md) (1 shared connections)
- [profession models rationale](profession_models_rationale.md) (1 shared connections)
- [chat services logger](chat_services_logger.md) (1 shared connections)
- [event events serialization](event_events_serialization.md) (1 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)
- [chat logger services](chat_logger_services.md) (1 shared connections)

## Source Files

- `server/game/chat_pose_manager.py`
- `server/game/chat_service.py`
- `server/game/chat_whisper_tracker.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 83 (92%)
- INFERRED: 7 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*