# HolidayService

> 57 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (40 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **.test_init_loads_from_database()** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **.test_collection_property()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_day_ordinal()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holiday_names()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_serialized_active_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_serialized_upcoming_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays_wraps_around()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_summary()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_init_with_collection()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_last_refresh_property()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_activates_matching_holiday()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_caps_duration()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_expires_old_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_no_matches()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_removes_unknown_holiday_id()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.collection()** (3 connections) — `server/services/holiday_service.py`
- *... and 32 more nodes in this community*

## Relationships

- [.get_upcoming_holidays](get_upcoming_holidays.md) (10 shared connections)
- [test_holiday_service.py](test_holiday_service.py.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [HolidayEntry](HolidayEntry.md) (6 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (5 shared connections)
- [ScheduleCollection](ScheduleCollection.md) (4 shared connections)
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) (4 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [.sample_holidays](sample_holidays.md) (2 shared connections)
- [MythosChronicle](MythosChronicle.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 151 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*