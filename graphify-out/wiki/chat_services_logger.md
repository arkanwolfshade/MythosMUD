# chat services logger

> 74 nodes

## Key Concepts

- **ChatLogger** (42 connections) — `server/services/chat_logger.py`
- **._write_log_entry()** (14 connections) — `server/services/chat_logger.py`
- **Any** (12 connections)
- **Path** (12 connections)
- **._queue_log_entry()** (8 connections) — `server/services/chat_logger.py`
- **._get_current_log_file()** (6 connections) — `server/services/chat_logger.py`
- **.log_local_channel_message()** (6 connections) — `server/services/chat_logger.py`
- **.__init__()** (5 connections) — `server/services/chat_logger.py`
- **._process_log_entry()** (5 connections) — `server/services/chat_logger.py`
- **.log_global_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **.log_system_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **.log_whisper_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **.get_global_channel_log_stats()** (5 connections) — `server/services/chat_logger.py`
- **.get_local_channel_log_stats()** (5 connections) — `server/services/chat_logger.py`
- **._get_local_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **.log_chat_message()** (4 connections) — `server/services/chat_logger.py`
- **.log_moderation_event()** (4 connections) — `server/services/chat_logger.py`
- **.log_system_event()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_file_paths()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_stats()** (4 connections) — `server/services/chat_logger.py`
- **._get_global_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **._get_whisper_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **._get_system_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **.get_global_channel_log_files()** (4 connections) — `server/services/chat_logger.py`
- **.cleanup_old_global_channel_logs()** (4 connections) — `server/services/chat_logger.py`
- *... and 49 more nodes in this community*

## Relationships

- [chat logger services](chat_logger_services.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [follow game service](follow_game_service.md) (1 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)
- [game chat whisper](game_chat_whisper.md) (1 shared connections)
- [tools generate invite](tools_generate_invite.md) (1 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 249 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*