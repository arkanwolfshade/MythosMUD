# Community 152

> 84 nodes

## Key Concepts

- **ChatLogger** (29 connections) — `server/services/chat_logger.py`
- **test_chat_logger.py** (20 connections) — `server/tests/unit/services/test_chat_logger.py`
- **._write_log_entry()** (14 connections) — `server/services/chat_logger.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **._get_current_log_file()** (6 connections) — `server/services/chat_logger.py`
- **chat_logger()** (6 connections) — `server/tests/unit/services/test_chat_logger.py`
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
- **temp_log_dir()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- *... and 59 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (4 shared connections)
- [Game Event Types](Game_Event_Types.md) (3 shared connections)
- [Community 244](Community_244.md) (2 shared connections)
- [Community 513](Community_513.md) (1 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (1 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (1 shared connections)
- [Community 173](Community_173.md) (1 shared connections)
- [Community 594](Community_594.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/services/chat_logger.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 121 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*