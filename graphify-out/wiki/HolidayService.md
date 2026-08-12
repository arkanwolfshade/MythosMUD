# HolidayService

> 33 nodes

## Key Concepts

- **HolidayService** (41 connections) — `server/services/holiday_service.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **.test_init_loads_from_database()** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **datetime** (6 connections)
- **test_holiday_service.py** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **_ensure_utc()** (4 connections) — `server/services/holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **._day_ordinal()** (3 connections) — `server/services/holiday_service.py`
- **.get_active_holiday_names()** (3 connections) — `server/services/holiday_service.py`
- **.get_upcoming_summary()** (3 connections) — `server/services/holiday_service.py`
- **.last_refresh()** (3 connections) — `server/services/holiday_service.py`
- **Path** (1 connections)
- **patch** (1 connections)
- **Single holiday definition loaded from data/<env>/calendar/holidays.json.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Load holidays from PostgreSQL database.** (1 connections) — `server/services/holiday_service.py`
- **Update the active holiday window for the provided Mythos timestamp.** (1 connections) — `server/services/holiday_service.py`
- **Return currently active holiday entries.** (1 connections) — `server/services/holiday_service.py`
- **Get active holidays and serialize them for API responses. This method…** (1 connections) — `server/services/holiday_service.py`
- **Get upcoming holidays and serialize them for API responses. This method…** (1 connections) — `server/services/holiday_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [HolidayCollection](HolidayCollection.md) (23 shared connections)
- [test_calendar_schemas.py](test_calendar_schemas.py.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [api/game.py](api-game.py.md) (4 shared connections)
- [MythosChronicle](MythosChronicle.md) (4 shared connections)
- [ScheduleCollection](ScheduleCollection.md) (3 shared connections)
- [field_validator](field_validator.md) (3 shared connections)
- [bundles/game.py](bundles-game.py.md) (3 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (2 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [.sample_holidays](sample_holidays.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 158 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*