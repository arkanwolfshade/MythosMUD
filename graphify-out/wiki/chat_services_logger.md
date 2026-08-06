# chat services logger

> 111 nodes

## Key Concepts

- **ChatLogger** (42 connections) — `server/services/chat_logger.py`
- **test_chat_logger.py** (20 connections) — `server/tests/unit/services/test_chat_logger.py`
- **._write_log_entry()** (14 connections) — `server/services/chat_logger.py`
- **Any** (12 connections)
- **Path** (12 connections)
- **._queue_log_entry()** (8 connections) — `server/services/chat_logger.py`
- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
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
- *... and 86 more nodes in this community*

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (2 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (1 shared connections)
- [rate limiter services](rate_limiter_services.md) (1 shared connections)
- [chat service game](chat_service_game.md) (1 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (1 shared connections)
- [services rescue service](services_rescue_service.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`
- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 325 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*