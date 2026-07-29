# ChatLogger

> 71 nodes

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
- *... and 46 more nodes in this community*

## Relationships

- [message filtering](message_filtering.md) (2 shared connections)
- [test chat logger](test_chat_logger.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (1 shared connections)
- [. get destination subzone()](_get_destination_subzone%28%29.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 249 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*