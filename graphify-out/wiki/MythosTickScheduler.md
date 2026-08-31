# MythosTickScheduler

> 92 nodes

## Key Concepts

- **MythosTickScheduler** (32 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **test_tick_scheduler.py** (19 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **tick_scheduler.py** (17 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **asyncio** (9 connections)
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._truncate_to_hour()** (5 connections) — `server/time/tick_scheduler.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- *... and 67 more nodes in this community*

## Relationships

- [test_time_bundle.py](test_time_bundle.py.md) (9 shared connections)
- [get_username_from_user](get_username_from_user.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (4 shared connections)
- [time_event_consumer.py](time_event_consumer.py.md) (4 shared connections)
- [TaskRegistry](TaskRegistry.md) (4 shared connections)
- [HolidayService](HolidayService.md) (4 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [schedule_service.py](schedule_service.py.md) (2 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (2 shared connections)

## Source Files

- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 217 (92%)
- INFERRED: 20 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*