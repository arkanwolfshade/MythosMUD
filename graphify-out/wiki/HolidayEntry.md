# HolidayEntry

> 20 nodes

## Key Concepts

- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **test_calendar_schemas.py** (23 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_ensure_unique_ids()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_id_map()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **.id_map()** (3 connections) — `server/schemas/calendar/calendar.py`
- **test_holiday_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_bonus_tags()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_season()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_tradition()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Create a mapping of holiday IDs to holiday entries. Returns: dict[str,…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Single holiday definition loaded from data/<env>/calendar/holidays.json.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Unit tests for calendar schemas. Tests the Pydantic models in calendar.py…** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection.id_map property.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection.ensure_unique_ids() detects duplicates.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry validates tradition.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry validates season.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry validates bonus_tags format.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`

## Relationships

- [ScheduleCollection](ScheduleCollection.md) (10 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (7 shared connections)
- [HolidayService](HolidayService.md) (6 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [.get_upcoming_holidays](get_upcoming_holidays.md) (5 shared connections)
- [test_holiday_service.py](test_holiday_service.py.md) (2 shared connections)
- [.sample_holidays](sample_holidays.md) (1 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`

## Audit Trail

- EXTRACTED: 65 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*