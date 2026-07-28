# Server Services (15)

> 95 nodes

## Key Concepts

- **HolidayService** (38 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (37 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **TestHolidayService** (20 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **datetime** (7 connections)
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **_holiday_entry_from_row()** (6 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (6 connections) — `server/services/holiday_service.py`
- **test_holiday_service.py** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_HolidayLoadResult** (5 connections) — `server/services/holiday_service.py`
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_ensure_utc()** (4 connections) — `server/services/holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- **test_holiday_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_id_map()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_ensure_unique_ids()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **.test_init_with_collection()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_activates_matching_holiday()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_no_matches()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_expires_old_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- *... and 70 more nodes in this community*

## Relationships

- [Server Schemas (2)](Server_Schemas_%282%29.md) (21 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (7 shared connections)
- [Server Utils (14)](Server_Utils_%2814%29.md) (6 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (5 shared connections)
- [Server Admin](Server_Admin.md) (3 shared connections)
- [Server Api (7)](Server_Api_%287%29.md) (3 shared connections)
- [Server Services (42)](Server_Services_%2842%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Api](Server_Api.md) (2 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (1 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 360 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*