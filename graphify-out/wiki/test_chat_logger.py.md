# test_chat_logger.py

> 52 nodes

## Key Concepts

- **test_chat_logger.py** (20 connections) — `server/tests/unit/services/test_chat_logger.py`
- **ChatWhisperTracker** (10 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (8 connections) — `server/game/chat_service.py`
- **chat_logger()** (8 connections) — `server/tests/unit/services/test_chat_logger.py`
- **chat_whisper_tracker.py** (5 connections) — `server/game/chat_whisper_tracker.py`
- **temp_log_dir()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_chat_logger_initialization_with_directory()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.clear_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_all_trackings()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.get_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.__init__()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **.store_sender()** (2 connections) — `server/game/chat_whisper_tracker.py`
- **test_channel_log_stats_and_cleanup()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_get_log_file_paths()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_get_log_stats()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_chat_message()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_local_global_system_channel_messages()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_moderation_event()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_player_joined_room()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_player_muted()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_player_unmuted()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_rate_limit_violation()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_system_event()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_whisper_channel_message()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_shutdown()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- *... and 27 more nodes in this community*

## Relationships

- [ChatLogger](ChatLogger.md) (3 shared connections)
- [chat_service.py](chat_service.py.md) (2 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [ChatModeration](ChatModeration.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [event_handler.py](event_handler.py.md) (1 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)
- [._cleanup_player_mutes](_cleanup_player_mutes.md) (1 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/game/chat_whisper_tracker.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 63 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*