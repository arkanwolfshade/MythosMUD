# Admin Teleport FRD

> 28 nodes

## Key Concepts

- **test_chat_logger.py** (17 connections) — `server/tests/unit/services/test_chat_logger.py`
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
- **Unit tests for chat logger service.  Tests the ChatLogger class for structured c** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Create a temporary directory for chat logs.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test ChatLogger initialization with explicit directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_chat_message writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_moderation_event writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_system_event writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test shutdown stops writer thread.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_player_muted writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_player_unmuted writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_player_joined_room writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Test log_rate_limit_violation writes entry.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- *... and 3 more nodes in this community*

## Relationships

- [Performance Optimization Summary](Performance_Optimization_Summary.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)
- [Commands Time](Commands_Time.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*