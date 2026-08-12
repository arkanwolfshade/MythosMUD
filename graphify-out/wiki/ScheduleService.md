# ScheduleService

> 104 nodes

## Key Concepts

- **ScheduleService** (27 connections) — `server/services/schedule_service.py`
- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **time_service.py** (25 connections) — `server/time/time_service.py`
- **time_event_consumer.py** (24 connections) — `server/time/time_event_consumer.py`
- **MythosTimeEventConsumer** (22 connections) — `server/time/time_event_consumer.py`
- **datetime** (15 connections)
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **test_schedule_service.py** (8 connections) — `server/tests/unit/services/test_schedule_service.py`
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 79 more nodes in this community*

## Relationships

- [HolidayService](HolidayService.md) (18 shared connections)
- [bundles/game.py](bundles-game.py.md) (12 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [EventBus](EventBus.md) (7 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (5 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (5 shared connections)
- [GameBundle](GameBundle.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [.__post_init__](__post_init__.md) (4 shared connections)
- [RoomService](RoomService.md) (4 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [send_game_event](send_game_event.md) (3 shared connections)

## Source Files

- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 424 (94%)
- INFERRED: 27 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*