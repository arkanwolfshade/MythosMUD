# chat services logger

> 47 nodes

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
- **test_chat_logger_initialization_with_directory()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **._ensure_log_directories()** (2 connections) — `server/services/chat_logger.py`
- **.shutdown()** (2 connections) — `server/services/chat_logger.py`
- **.wait_for_queue_processing()** (2 connections) — `server/services/chat_logger.py`
- **.cleanup_old_local_channel_logs()** (2 connections) — `server/services/chat_logger.py`
- **Structured logging service for chat system events.      This logger creates JSON** (1 connections) — `server/services/chat_logger.py`
- *... and 22 more nodes in this community*

## Relationships

- [persistence services combat](persistence_services_combat.md) (22 shared connections)
- [player realtime event](player_realtime_event.md) (2 shared connections)
- [chat logger services](chat_logger_services.md) (2 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (1 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 161 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*