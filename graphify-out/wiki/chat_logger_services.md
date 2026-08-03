# chat logger services

> 37 nodes

## Key Concepts

- **test_chat_logger.py** (20 connections) — `server/tests/unit/services/test_chat_logger.py`
- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **test_chat_logger_initialization_with_directory()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **temp_log_dir()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_chat_message()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_moderation_event()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_system_event()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_shutdown()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_player_muted()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_player_unmuted()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_player_joined_room()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_rate_limit_violation()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_get_log_file_paths()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_get_log_stats()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_whisper_channel_message()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_log_local_global_system_channel_messages()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **test_channel_log_stats_and_cleanup()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Initialize the user manager.          Args:             data_dir: Directory f** (1 connections) — `server/services/user_manager.py`
- **test_log_message_flagged_and_player_left()** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Unit tests for chat logger service.  Tests the ChatLogger class for structured c** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Create a temporary directory for chat logs.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test ChatLogger initialization with explicit directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_chat_message writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- *... and 12 more nodes in this community*

## Relationships

- [chat services logger](chat_services_logger.md) (3 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [game chat whisper](game_chat_whisper.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [rate limiter services](rate_limiter_services.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 76 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*