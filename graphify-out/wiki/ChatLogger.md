# ChatLogger

> 46 nodes

## Key Concepts

- **ChatLogger** (30 connections) — `server/services/chat_logger.py`
- **._write_log_entry()** (14 connections) — `server/services/chat_logger.py`
- **._get_current_log_file()** (6 connections) — `server/services/chat_logger.py`
- **Any** (6 connections)
- **.__init__()** (5 connections) — `server/services/chat_logger.py`
- **._process_log_entry()** (5 connections) — `server/services/chat_logger.py`
- **Path** (5 connections)
- **.get_log_file_paths()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_stats()** (4 connections) — `server/services/chat_logger.py`
- **.log_chat_message()** (4 connections) — `server/services/chat_logger.py`
- **.log_moderation_event()** (4 connections) — `server/services/chat_logger.py`
- **.log_system_event()** (4 connections) — `server/services/chat_logger.py`
- **._queue_log_entry()** (4 connections) — `server/services/chat_logger.py`
- **.log_message_flagged()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_joined_room()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_left_room()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_muted()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_unmuted()** (3 connections) — `server/services/chat_logger.py`
- **.log_rate_limit_violation()** (3 connections) — `server/services/chat_logger.py`
- **._start_writer_thread()** (3 connections) — `server/services/chat_logger.py`
- **._writer_worker()** (3 connections) — `server/services/chat_logger.py`
- **._ensure_log_directories()** (2 connections) — `server/services/chat_logger.py`
- **.shutdown()** (2 connections) — `server/services/chat_logger.py`
- **.wait_for_queue_processing()** (2 connections) — `server/services/chat_logger.py`
- **Shutdown the logger and wait for writer thread to finish.** (1 connections) — `server/services/chat_logger.py`
- *... and 21 more nodes in this community*

## Relationships

- [test_chat_logger.py](test_chat_logger.py.md) (3 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (1 shared connections)
- [user_manager.py](user_manager.py.md) (1 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 76 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*