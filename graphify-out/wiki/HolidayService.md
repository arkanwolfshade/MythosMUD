# HolidayService

> 145 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **MythosHourTickEvent** (15 connections) — `server/events/event_types.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **._init_temporal_layer()** (9 connections) — `server/container/bundles/game.py`
- **test_time_event_consumer.py** (9 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **_ensure_utc()** (6 connections) — `server/services/holiday_service.py`
- **.test_init_loads_from_database()** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **datetime** (6 connections)
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **._load_from_database()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database()** (5 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_load_from_database_success()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._handle_tick()** (5 connections) — `server/time/time_event_consumer.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- *... and 120 more nodes in this community*

## Relationships

- [bundles/game.py](bundles-game.py.md) (57 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (7 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [._async_load_from_database](_async_load_from_database.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [test_time_bundle.py](test_time_bundle.py.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/events/event_types.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 296 (93%)
- INFERRED: 22 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*