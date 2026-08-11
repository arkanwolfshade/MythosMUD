# Performance Optimization Summary

> 46 nodes

## Key Concepts

- **ChatLogger** (29 connections) — `server/services/chat_logger.py`
- **._write_log_entry()** (14 connections) — `server/services/chat_logger.py`
- **Any** (6 connections)
- **._get_current_log_file()** (6 connections) — `server/services/chat_logger.py`
- **.__init__()** (5 connections) — `server/services/chat_logger.py`
- **._process_log_entry()** (5 connections) — `server/services/chat_logger.py`
- **Path** (5 connections)
- **._queue_log_entry()** (4 connections) — `server/services/chat_logger.py`
- **.log_chat_message()** (4 connections) — `server/services/chat_logger.py`
- **.log_moderation_event()** (4 connections) — `server/services/chat_logger.py`
- **.log_system_event()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_file_paths()** (4 connections) — `server/services/chat_logger.py`
- **.get_log_stats()** (4 connections) — `server/services/chat_logger.py`
- **._start_writer_thread()** (3 connections) — `server/services/chat_logger.py`
- **._writer_worker()** (3 connections) — `server/services/chat_logger.py`
- **.log_message_flagged()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_muted()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_unmuted()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_joined_room()** (3 connections) — `server/services/chat_logger.py`
- **.log_player_left_room()** (3 connections) — `server/services/chat_logger.py`
- **.log_rate_limit_violation()** (3 connections) — `server/services/chat_logger.py`
- **._ensure_log_directories()** (2 connections) — `server/services/chat_logger.py`
- **.shutdown()** (2 connections) — `server/services/chat_logger.py`
- **.wait_for_queue_processing()** (2 connections) — `server/services/chat_logger.py`
- **Structured logging service for chat system events.      This logger creates JSON** (1 connections) — `server/services/chat_logger.py`
- *... and 21 more nodes in this community*

## Relationships

- [Commands Time](Commands_Time.md) (2 shared connections)
- [Admin Teleport FRD](Admin_Teleport_FRD.md) (2 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (1 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (1 shared connections)
- [Command Parser](Command_Parser.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 144 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*