# ChatChannelLoggerMixin

> 42 nodes

## Key Concepts

- **ChatChannelLoggerMixin** (19 connections) — `server/services/chat_channel_logger.py`
- **chat_logger.py** (17 connections) — `server/services/chat_logger.py`
- **services/rate_limiter.py** (10 connections) — `server/services/rate_limiter.py`
- **chat_channel_logger.py** (8 connections) — `server/services/chat_channel_logger.py`
- **Path** (8 connections)
- **._queue_log_entry()** (7 connections) — `server/services/chat_channel_logger.py`
- **.log_local_channel_message()** (6 connections) — `server/services/chat_channel_logger.py`
- **Any** (6 connections)
- **log_time_formats.py** (6 connections) — `server/structured_logging/log_time_formats.py`
- **.get_global_channel_log_stats()** (5 connections) — `server/services/chat_channel_logger.py`
- **.get_local_channel_log_stats()** (5 connections) — `server/services/chat_channel_logger.py`
- **.log_global_channel_message()** (5 connections) — `server/services/chat_channel_logger.py`
- **.log_system_channel_message()** (5 connections) — `server/services/chat_channel_logger.py`
- **.log_whisper_channel_message()** (5 connections) — `server/services/chat_channel_logger.py`
- **.cleanup_old_global_channel_logs()** (4 connections) — `server/services/chat_channel_logger.py`
- **._get_global_channel_log_file()** (4 connections) — `server/services/chat_channel_logger.py`
- **.get_global_channel_log_files()** (4 connections) — `server/services/chat_channel_logger.py`
- **._get_local_channel_log_file()** (4 connections) — `server/services/chat_channel_logger.py`
- **._get_system_channel_log_file()** (4 connections) — `server/services/chat_channel_logger.py`
- **._get_whisper_channel_log_file()** (4 connections) — `server/services/chat_channel_logger.py`
- **.get_local_channel_log_files()** (3 connections) — `server/services/chat_channel_logger.py`
- **.cleanup_old_local_channel_logs()** (2 connections) — `server/services/chat_channel_logger.py`
- **Channel-specific chat log methods for MythosMUD. Mixin used by ChatLogger:…** (1 connections) — `server/services/chat_channel_logger.py`
- **Log a global channel message to global.log file. Args: message_data: Global…** (1 connections) — `server/services/chat_channel_logger.py`
- **Get the global channel log file path. Returns: Path to the global channel log…** (1 connections) — `server/services/chat_channel_logger.py`
- *... and 17 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [chat_service.py](chat_service.py.md) (3 shared connections)
- [ChatLogger](ChatLogger.md) (2 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (2 shared connections)
- [event_handler.py](event_handler.py.md) (2 shared connections)
- [test_room_utils.py](test_room_utils.py.md) (1 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (1 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/services/chat_channel_logger.py`
- `server/services/chat_logger.py`
- `server/services/rate_limiter.py`
- `server/structured_logging/log_time_formats.py`

## Audit Trail

- EXTRACTED: 95 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*