# HolidayService

> 76 nodes

## Key Concepts

- **HolidayService** (41 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (37 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **TestHolidayService** (20 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **.test_init_loads_from_database()** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **datetime** (6 connections)
- **test_holiday_service.py** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **_ensure_utc()** (4 connections) — `server/services/holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **.sample_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_collection_property()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_day_ordinal()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holiday_names()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays_wraps_around()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_summary()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_init_with_collection()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_last_refresh_property()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- *... and 51 more nodes in this community*

## Relationships

- [test_calendar_schemas.py](test_calendar_schemas.py.md) (19 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (11 shared connections)
- [ChronicleLike](ChronicleLike.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [field_validator](field_validator.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (2 shared connections)
- [test_game.py](test_game.py.md) (2 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [get_mythos_time](get_mythos_time.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 192 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*