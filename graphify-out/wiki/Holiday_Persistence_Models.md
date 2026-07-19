# Holiday Persistence Models

> 80 nodes · cohesion 0.04

## Key Concepts

- **HolidayService** (52 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (29 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (20 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.__init__()** (9 connections) — `server/services/holiday_service.py`
- **HolidayEntry** (8 connections) — `server/services/holiday_service.py`
- **datetime** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **_holiday_entry_from_row()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (6 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (6 connections) — `server/services/holiday_service.py`
- **_HolidayLoadResult** (5 connections) — `server/services/holiday_service.py`
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **test_holiday_service.py** (5 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_ensure_utc()** (4 connections) — `server/services/holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **.test_collection_property()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_day_ordinal()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holiday_names()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays_wraps_around()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- *... and 55 more nodes in this community*

## Relationships

- [[Time Event Consumer]] (18 shared connections)
- [[Calendar Holiday Schemas]] (12 shared connections)
- [[Async Persistence Layer]] (9 shared connections)
- [[Game Service Bundle]] (9 shared connections)
- [[NPC Admin API]] (8 shared connections)
- [[Admin NPC Schemas]] (2 shared connections)
- [[Validate Calendar]] (1 shared connections)
- [[Dependency Risk Analyzer]] (1 shared connections)
- [[Inventory Service Helpers]] (1 shared connections)
- [[Lucidity Rate Overrides]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 286 (89%)
- INFERRED: 35 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
