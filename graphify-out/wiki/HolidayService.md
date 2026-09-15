# HolidayService

> 128 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **MythosHourTickEvent** (15 connections) — `server/events/event_types.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **._init_temporal_services()** (10 connections) — `server/container/bundles/time.py`
- **test_holiday_service.py** (9 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **test_time_event_consumer.py** (8 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **.initialize()** (6 connections) — `server/container/bundles/time.py`
- **_ensure_utc()** (6 connections) — `server/services/holiday_service.py`
- **datetime** (6 connections)
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **_string_list_from_row()** (5 connections) — `server/services/holiday_service.py`
- *... and 103 more nodes in this community*

## Relationships

- [HolidayCollection](HolidayCollection.md) (34 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (14 shared connections)
- [bundles/game.py](bundles-game.py.md) (13 shared connections)
- [TestScheduleService](TestScheduleService.md) (12 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (4 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (4 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/events/event_types.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 326 (94%)
- INFERRED: 20 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*