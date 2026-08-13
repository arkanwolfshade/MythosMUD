# test_chat_logger.py

> 33 nodes

## Key Concepts

- **test_chat_logger.py** (17 connections) — `server/tests/unit/services/test_chat_logger.py`
- **chat_logger()** (8 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **temp_log_dir()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_chat_logger_initialization_with_directory()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_get_log_file_paths()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_get_log_stats()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_chat_message()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_moderation_event()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_player_joined_room()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_player_muted()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_player_unmuted()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_rate_limit_violation()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_system_event()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_whisper_channel_message()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_shutdown()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **fixture** (2 connections)
- **Initialize the rate limiter with configuration-based limits.** (1 connections) — `server/services/rate_limiter.py`
- **Unit tests for chat logger service. Tests the ChatLogger class for structured…** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_player_muted writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_player_unmuted writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_player_joined_room writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_rate_limit_violation writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Create a temporary directory for chat logs.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test get_log_file_paths returns correct paths.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- *... and 8 more nodes in this community*

## Relationships

- [ChatLogger](ChatLogger.md) (3 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (1 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)
- [user_manager.py](user_manager.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 38 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*