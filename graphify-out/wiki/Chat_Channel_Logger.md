# Chat Channel Logger

> 45 nodes

## Key Concepts

- **ChatLogger** (42 connections) — `server/services/chat_logger.py`
- **._write_log_entry()** (14 connections) — `server/services/chat_logger.py`
- **Any** (12 connections)
- **._queue_log_entry()** (8 connections) — `server/services/chat_logger.py`
- **.log_local_channel_message()** (6 connections) — `server/services/chat_logger.py`
- **.log_global_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **.log_system_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **.log_whisper_channel_message()** (5 connections) — `server/services/chat_logger.py`
- **._get_local_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **.log_chat_message()** (4 connections) — `server/services/chat_logger.py`
- **.log_moderation_event()** (4 connections) — `server/services/chat_logger.py`
- **.log_system_event()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_stats()** (4 connections) — `server/services/chat_logger.py`
- **.log_message_flagged()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_muted()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_unmuted()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_joined_room()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_left_room()** (3 connections) — `server/services/chat_logger.py`
- **.log_rate_limit_violation()** (3 connections) — `server/services/chat_logger.py`
- **._ensure_log_directories()** (2 connections) — `server/services/chat_logger.py`
- **.shutdown()** (2 connections) — `server/services/chat_logger.py`
- **.wait_for_queue_processing()** (2 connections) — `server/services/chat_logger.py`
- **.cleanup_old_local_channel_logs()** (2 connections) — `server/services/chat_logger.py`
- **Structured logging service for chat system events.      This logger creates JSON** (1 connections) — `server/services/chat_logger.py`
- **Ensure log directory exists.** (1 connections) — `server/services/chat_logger.py`
- *... and 20 more nodes in this community*

## Relationships

- [AnyIO vs Asyncio Guide](AnyIO_vs_Asyncio_Guide.md) (18 shared connections)
- [Procedures Readme Semgrep](Procedures_Readme_Semgrep.md) (3 shared connections)
- [Plan Archive Character](Plan_Archive_Character.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Admin Teleport FRD](Admin_Teleport_FRD.md) (2 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (1 shared connections)
- [chat_logger](chat_logger.md) (1 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 164 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*