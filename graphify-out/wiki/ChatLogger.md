# ChatLogger

> 31 nodes

## Key Concepts

- **ChatLogger** (29 connections) — `server/services/chat_logger.py`
- **._write_log_entry()** (14 connections) — `server/services/chat_logger.py`
- **Any** (6 connections)
- **.get_log_stats()** (4 connections) — `server/services/chat_logger.py`
- **.log_chat_message()** (4 connections) — `server/services/chat_logger.py`
- **.log_moderation_event()** (4 connections) — `server/services/chat_logger.py`
- **.log_system_event()** (4 connections) — `server/services/chat_logger.py`
- **.log_message_flagged()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_joined_room()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_left_room()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_muted()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_unmuted()** (3 connections) — `server/services/chat_logger.py`
- **.log_rate_limit_violation()** (3 connections) — `server/services/chat_logger.py`
- **._ensure_log_directories()** (2 connections) — `server/services/chat_logger.py`
- **.shutdown()** (2 connections) — `server/services/chat_logger.py`
- **.wait_for_queue_processing()** (2 connections) — `server/services/chat_logger.py`
- **Shutdown the logger and wait for writer thread to finish.** (1 connections) — `server/services/chat_logger.py`
- **Wait for all queued log entries to be processed. Args: timeout: Maximum time to…** (1 connections) — `server/services/chat_logger.py`
- **Write a log entry to the appropriate log file. Args: log_type: Type of log…** (1 connections) — `server/services/chat_logger.py`
- **Log a chat message for AI processing. Args: message_data: Chat message data…** (1 connections) — `server/services/chat_logger.py`
- **Log a moderation event for AI training and processing. Args: event_type: Type…** (1 connections) — `server/services/chat_logger.py`
- **Structured logging service for chat system events. This logger creates JSON-…** (1 connections) — `server/services/chat_logger.py`
- **Log a flagged message for AI moderation. Args: message_id: ID of the flagged…** (1 connections) — `server/services/chat_logger.py`
- **Log a player mute action. Args: muter_id: ID of player who applied mute…** (1 connections) — `server/services/chat_logger.py`
- **Log a player unmute action. Args: unmuter_id: ID of player who removed mute…** (1 connections) — `server/services/chat_logger.py`
- *... and 6 more nodes in this community*

## Relationships

- [._get_current_log_file](_get_current_log_file.md) (11 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (1 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (1 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 102 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*