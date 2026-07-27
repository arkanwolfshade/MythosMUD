# Chat Channel Logger

> 71 nodes · cohesion 0.05

## Key Concepts

- **ChatLogger** (45 connections) — `server/services/chat_logger.py`
- **._write_log_entry()** (14 connections) — `server/services/chat_logger.py`
- **Any** (12 connections) — `server/services/chat_logger.py`
- **Path** (12 connections) — `server/services/chat_logger.py`
- **._queue_log_entry()** (8 connections) — `server/services/chat_logger.py`
- **._get_current_log_file()** (6 connections) — `server/services/chat_logger.py`
- **.log_local_channel_message()** (6 connections) — `server/services/chat_logger.py`
- **.get_global_channel_log_stats()** (5 connections) — `server/services/chat_logger.py`
- **.get_local_channel_log_stats()** (5 connections) — `server/services/chat_logger.py`
- **.__init__()** (5 connections) — `server/services/chat_logger.py`
- **.log_global_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **.log_system_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **.log_whisper_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **._process_log_entry()** (5 connections) — `server/services/chat_logger.py`
- **.cleanup_old_global_channel_logs()** (4 connections) — `server/services/chat_logger.py`
- **._get_global_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **.get_global_channel_log_files()** (4 connections) — `server/services/chat_logger.py`
- **._get_local_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_file_paths()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_stats()** (4 connections) — `server/services/chat_logger.py`
- **._get_system_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **._get_whisper_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **.log_chat_message()** (4 connections) — `server/services/chat_logger.py`
- **.log_moderation_event()** (4 connections) — `server/services/chat_logger.py`
- **.log_system_event()** (4 connections) — `server/services/chat_logger.py`
- *... and 46 more nodes in this community*

## Relationships

- [[NPC Admin API]] (3 shared connections)
- [[Chat Logger Service Tests]] (3 shared connections)
- [[Services User Manager]] (2 shared connections)
- [[Player Mute Persistence]] (2 shared connections)
- [[Chat NATS Publisher]] (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 249 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
