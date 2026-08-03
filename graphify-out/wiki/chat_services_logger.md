# chat services logger

> 45 nodes

## Key Concepts

- **ChatLogger** (42 connections) — `server/services/chat_logger.py`
- **._write_log_entry()** (14 connections) — `server/services/chat_logger.py`
- **Any** (12 connections)
- **._get_current_log_file()** (6 connections) — `server/services/chat_logger.py`
- **._process_log_entry()** (5 connections) — `server/services/chat_logger.py`
- **.get_local_channel_log_stats()** (5 connections) — `server/services/chat_logger.py`
- **.log_chat_message()** (4 connections) — `server/services/chat_logger.py`
- **.log_moderation_event()** (4 connections) — `server/services/chat_logger.py`
- **.log_system_event()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_file_paths()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_stats()** (4 connections) — `server/services/chat_logger.py`
- **._writer_worker()** (3 connections) — `server/services/chat_logger.py`
- **.log_message_flagged()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_muted()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_unmuted()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_joined_room()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_left_room()** (3 connections) — `server/services/chat_logger.py`
- **.log_rate_limit_violation()** (3 connections) — `server/services/chat_logger.py`
- **.get_local_channel_log_files()** (3 connections) — `server/services/chat_logger.py`
- **._ensure_log_directories()** (2 connections) — `server/services/chat_logger.py`
- **.shutdown()** (2 connections) — `server/services/chat_logger.py`
- **.wait_for_queue_processing()** (2 connections) — `server/services/chat_logger.py`
- **.cleanup_old_local_channel_logs()** (2 connections) — `server/services/chat_logger.py`
- **Structured logging service for chat system events.      This logger creates JSON** (1 connections) — `server/services/chat_logger.py`
- **Ensure log directory exists.** (1 connections) — `server/services/chat_logger.py`
- *... and 20 more nodes in this community*

## Relationships

- [services chat logger](services_chat_logger.md) (22 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [skill game service](skill_game_service.md) (2 shared connections)
- [chat logger services](chat_logger_services.md) (2 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)
- [services chat rate](services_chat_rate.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 157 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*