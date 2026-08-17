# server game chat service chatservice

> 9 nodes

## Key Concepts

- **chat_logger()** (8 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (7 connections) — `server/game/chat_service.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **temp_log_dir()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **fixture** (2 connections)
- **Initialize chat service. Args: persistence: Database persistence layer…** (1 connections) — `server/game/chat_service.py`
- **Initialize the rate limiter with configuration-based limits.** (1 connections) — `server/services/rate_limiter.py`
- **Create a temporary directory for chat logs.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (2 shared connections)
- [server game chat pose manager](server_game_chat_pose_manager.md) (1 shared connections)
- [server game chat whisper tracker](server_game_chat_whisper_tracker.md) (1 shared connections)
- [server game chat moderation chatmoderation](server_game_chat_moderation_chatmoderation.md) (1 shared connections)
- [server api players](server_api_players.md) (1 shared connections)
- [server game chat service chatservice](server_game_chat_service_chatservice.md) (1 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)
- [server services rate limiter py](server_services_rate_limiter_py.md) (1 shared connections)
- [server services chat logger chatlogger](server_services_chat_logger_chatlogger.md) (1 shared connections)
- [server realtime event handler py](server_realtime_event_handler_py.md) (1 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 15 (75%)
- INFERRED: 5 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*