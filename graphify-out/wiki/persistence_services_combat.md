# persistence services combat

> 25 nodes

## Key Concepts

- **Path** (12 connections)
- **._queue_log_entry()** (8 connections) — `server/services/chat_logger.py`
- **.log_local_channel_message()** (6 connections) — `server/services/chat_logger.py`
- **.log_global_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **.log_system_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **.log_whisper_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **.get_global_channel_log_stats()** (5 connections) — `server/services/chat_logger.py`
- **._get_local_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **._get_global_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **._get_whisper_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **._get_system_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **.get_global_channel_log_files()** (4 connections) — `server/services/chat_logger.py`
- **.cleanup_old_global_channel_logs()** (4 connections) — `server/services/chat_logger.py`
- **Queue a log entry for writing by the background thread.          Args:** (1 connections) — `server/services/chat_logger.py`
- **Get the local channel log file path for a specific sub-zone.          Args:** (1 connections) — `server/services/chat_logger.py`
- **Log a local channel message to sub-zone specific file.          Args:** (1 connections) — `server/services/chat_logger.py`
- **Log a global channel message to global.log file.          Args:             mess** (1 connections) — `server/services/chat_logger.py`
- **Get the global channel log file path.          Returns:             Path to the** (1 connections) — `server/services/chat_logger.py`
- **Log a system channel message to system.log file.          Args:             mess** (1 connections) — `server/services/chat_logger.py`
- **Log a whisper channel message to whisper.log file.          Args:             me** (1 connections) — `server/services/chat_logger.py`
- **Get the whisper channel log file path.          Returns:             Path to the** (1 connections) — `server/services/chat_logger.py`
- **Get the system channel log file path.          Returns:             Path to the** (1 connections) — `server/services/chat_logger.py`
- **Get all global channel log files.          Returns:             List of string p** (1 connections) — `server/services/chat_logger.py`
- **Get statistics for global channel log files.          Returns:             Dicti** (1 connections) — `server/services/chat_logger.py`
- **Clean up old global channel log files.          Args:             days_to_keep:** (1 connections) — `server/services/chat_logger.py`

## Relationships

- [chat services logger](chat_services_logger.md) (22 shared connections)
- [player realtime event](player_realtime_event.md) (1 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 82 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*