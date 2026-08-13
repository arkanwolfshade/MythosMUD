# HolidayCollection

> 38 nodes

## Key Concepts

- **HolidayCollection** (37 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (20 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_collection_property()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_day_ordinal()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holiday_names()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays_wraps_around()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_summary()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_init_with_collection()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_last_refresh_property()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_activates_matching_holiday()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_caps_duration()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_expires_old_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_no_matches()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.id_map()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.collection()** (3 connections) — `server/services/holiday_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.ensure_unique_ids()** (2 connections) — `server/schemas/calendar/calendar.py`
- **Create a mapping of holiday IDs to holiday entries. Returns: dict[str,…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Ensure all holiday IDs are unique. Raises: ValueError: If duplicate holiday IDs…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Wrapper for the complete holiday JSON payload.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Get the holiday collection. Returns: HolidayCollection: The loaded holiday…** (1 connections) — `server/services/holiday_service.py`
- **Test refresh_active activates holidays matching current date.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Test refresh_active returns empty when no holidays match.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- *... and 13 more nodes in this community*

## Relationships

- [HolidayService](HolidayService.md) (21 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (5 shared connections)
- [test_calendar_schemas.py](test_calendar_schemas.py.md) (4 shared connections)
- [ScheduleCollection](ScheduleCollection.md) (3 shared connections)
- [.__init__](__init__.md) (2 shared connections)
- [.sample_holidays](sample_holidays.md) (2 shared connections)
- [_holiday_entry_from_row](_holiday_entry_from_row.md) (1 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [.load_file](load_file.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 89 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*