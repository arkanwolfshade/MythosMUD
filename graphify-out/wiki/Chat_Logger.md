# Chat Logger

> 112 nodes

## Key Concepts

- **ChatLogger** (29 connections) — `server/services/chat_logger.py`
- **test_chat_logger.py** (21 connections) — `server/tests/unit/services/test_chat_logger.py`
- **._write_log_entry()** (14 connections) — `server/services/chat_logger.py`
- **ChatPoseManager** (11 connections) — `server/game/chat_pose_manager.py`
- **ChatWhisperTracker** (10 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (8 connections) — `server/game/chat_service.py`
- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
- **._get_current_log_file()** (6 connections) — `server/services/chat_logger.py`
- **Any** (6 connections)
- **.normalize_player_id()** (5 connections) — `server/game/chat_pose_manager.py`
- **.__init__()** (5 connections) — `server/services/chat_logger.py`
- **._process_log_entry()** (5 connections) — `server/services/chat_logger.py`
- **Path** (5 connections)
- **.get_log_file_paths()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_stats()** (4 connections) — `server/services/chat_logger.py`
- **.log_chat_message()** (4 connections) — `server/services/chat_logger.py`
- **.log_moderation_event()** (4 connections) — `server/services/chat_logger.py`
- **.log_system_event()** (4 connections) — `server/services/chat_logger.py`
- **._queue_log_entry()** (4 connections) — `server/services/chat_logger.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **.clear_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.get_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.set_pose()** (3 connections) — `server/game/chat_pose_manager.py`
- **.log_message_flagged()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_joined_room()** (3 connections) — `server/services/chat_logger.py`
- *... and 87 more nodes in this community*

## Relationships

- [Chat Service & Channels](Chat_Service_&_Channels.md) (5 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (5 shared connections)
- [User Manager](User_Manager.md) (3 shared connections)
- [Test Config Init](Test_Config_Init.md) (2 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (1 shared connections)
- [Chat Moderation](Chat_Moderation.md) (1 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (1 shared connections)
- [Test Rate Limiter](Test_Rate_Limiter.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/game/chat_pose_manager.py`
- `server/game/chat_service.py`
- `server/game/chat_whisper_tracker.py`
- `server/services/chat_logger.py`
- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 154 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*