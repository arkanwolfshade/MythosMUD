# MythosTickScheduler

> 130 nodes

## Key Concepts

- **MythosTickScheduler** (32 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **game_tick_corpses.py** (21 connections) — `server/app/game_tick_corpses.py`
- **test_time_bundle.py** (21 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_tick_scheduler.py** (18 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **tick_scheduler.py** (16 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.error()** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
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
- **isolated_chronicle()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- *... and 105 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [time.py](time.py.md) (10 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (6 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (5 shared connections)
- [TaskRegistry](TaskRegistry.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (4 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 295 (91%)
- INFERRED: 28 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*