# test_chat_logger.py

> 41 nodes

## Key Concepts

- **test_chat_logger.py** (21 connections) — `server/tests/unit/services/test_chat_logger.py`
- **chat_logger()** (8 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (5 connections) — `server/services/user_manager.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **temp_log_dir()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_chat_logger_initialization_with_directory()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
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
- **Path** (2 connections)
- **fixture** (2 connections)
- **test_log_message_flagged_and_player_left()** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Initialize the rate limiter with configuration-based limits.** (1 connections) — `server/services/rate_limiter.py`
- **Initialize the user manager. Args: data_dir: Directory for player-specific mute…** (1 connections) — `server/services/user_manager.py`
- **Unit tests for chat logger service. Tests the ChatLogger class for structured…** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- *... and 16 more nodes in this community*

## Relationships

- [ChatLogger](ChatLogger.md) (3 shared connections)
- [UserManager](UserManager.md) (2 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (1 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/services/user_manager.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 48 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*