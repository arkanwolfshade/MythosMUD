# HolidayService

> 115 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **._init_temporal_services()** (10 connections) — `server/container/bundles/time.py`
- **test_holiday_service.py** (9 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **.initialize()** (6 connections) — `server/container/bundles/time.py`
- **_ensure_utc()** (6 connections) — `server/services/holiday_service.py`
- **.test_init_loads_from_database()** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **datetime** (6 connections)
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **_string_list_from_row()** (5 connections) — `server/services/holiday_service.py`
- **.test_async_load_from_database()** (5 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- *... and 90 more nodes in this community*

## Relationships

- [HolidayCollection](HolidayCollection.md) (35 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (14 shared connections)
- [bundles/game.py](bundles-game.py.md) (12 shared connections)
- [MythosHourTickEvent](MythosHourTickEvent.md) (11 shared connections)
- [MythosChronicle](MythosChronicle.md) (8 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (5 shared connections)
- [api/game.py](api-game.py.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [RoomService](RoomService.md) (4 shared connections)
- [field_validator](field_validator.md) (3 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (3 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 301 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*