# Game Tick Processing

> 34 nodes

## Key Concepts

- **ChatChannelLoggerMixin** (19 connections) — `server/services/chat_channel_logger.py`
- **Path** (8 connections)
- **._queue_log_entry()** (7 connections) — `server/services/chat_channel_logger.py`
- **.log_local_channel_message()** (6 connections) — `server/services/chat_channel_logger.py`
- **Any** (6 connections)
- **.log_global_channel_message()** (5 connections) — `server/services/chat_channel_logger.py`
- **.log_system_channel_message()** (5 connections) — `server/services/chat_channel_logger.py`
- **.log_whisper_channel_message()** (5 connections) — `server/services/chat_channel_logger.py`
- **.get_global_channel_log_stats()** (5 connections) — `server/services/chat_channel_logger.py`
- **.get_local_channel_log_stats()** (5 connections) — `server/services/chat_channel_logger.py`
- **._get_local_channel_log_file()** (4 connections) — `server/services/chat_channel_logger.py`
- **._get_global_channel_log_file()** (4 connections) — `server/services/chat_channel_logger.py`
- **._get_whisper_channel_log_file()** (4 connections) — `server/services/chat_channel_logger.py`
- **._get_system_channel_log_file()** (4 connections) — `server/services/chat_channel_logger.py`
- **.get_global_channel_log_files()** (4 connections) — `server/services/chat_channel_logger.py`
- **.cleanup_old_global_channel_logs()** (4 connections) — `server/services/chat_channel_logger.py`
- **.get_local_channel_log_files()** (3 connections) — `server/services/chat_channel_logger.py`
- **.cleanup_old_local_channel_logs()** (2 connections) — `server/services/chat_channel_logger.py`
- **Channel log paths, writers, stats, and cleanup. Requires ChatLogger attrs.** (1 connections) — `server/services/chat_channel_logger.py`
- **Queue a log entry; implemented by ChatLogger.** (1 connections) — `server/services/chat_channel_logger.py`
- **Get the local channel log file path for a specific sub-zone.          Args:** (1 connections) — `server/services/chat_channel_logger.py`
- **Log a local channel message to sub-zone specific file.          Args:** (1 connections) — `server/services/chat_channel_logger.py`
- **Log a global channel message to global.log file.          Args:             m** (1 connections) — `server/services/chat_channel_logger.py`
- **Get the global channel log file path.          Returns:             Path to t** (1 connections) — `server/services/chat_channel_logger.py`
- **Log a system channel message to system.log file.          Args:             m** (1 connections) — `server/services/chat_channel_logger.py`
- *... and 9 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Performance Optimization Summary](Performance_Optimization_Summary.md) (1 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/services/chat_channel_logger.py`

## Audit Trail

- EXTRACTED: 115 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*