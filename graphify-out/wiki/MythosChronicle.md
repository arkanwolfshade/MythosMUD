# MythosChronicle

> 86 nodes

## Key Concepts

- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **test_time_bundle.py** (21 connections) — `server/tests/unit/container/test_time_bundle.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.error()** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **isolated_chronicle()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_get_mythos_chronicle_singleton()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_time_bundle_initialize_missing_dependencies()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **_season_for_month()** (5 connections) — `server/time/time_service.py`
- **MythosCalendarComponents** (4 connections) — `server/time/time_service.py`
- *... and 61 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [HolidayService](HolidayService.md) (3 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (2 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (2 shared connections)
- [Lock](Lock.md) (1 shared connections)
- [test_enhanced_logging_config.py](test_enhanced_logging_config.py.md) (1 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [._run_idle_sampler](_run_idle_sampler.md) (1 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/config/models/app.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 162 (93%)
- INFERRED: 13 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*