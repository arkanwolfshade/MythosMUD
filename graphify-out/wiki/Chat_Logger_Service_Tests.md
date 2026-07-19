# Chat Logger Service Tests

> 28 nodes · cohesion 0.07

## Key Concepts

- **test_chat_logger.py** (16 connections) — `server/tests/unit/services/test_chat_logger.py`
- **chat_logger()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_chat_logger_initialization_with_directory()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_get_stats()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **Test log_player_muted writes entry.** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test get_log_stats returns statistics.** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
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
- **Unit tests for chat logger service.  Tests the ChatLogger class for structured c** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_player_joined_room writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_rate_limit_violation writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test get_log_file_paths returns correct paths.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_whisper_channel_message writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test ChatLogger initialization with explicit directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_chat_message writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- *... and 3 more nodes in this community*

## Relationships

- [[Chat Channel Logger]] (3 shared connections)
- [[Room Subscription Helpers]] (1 shared connections)
- [[Alias Storage Services]] (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
