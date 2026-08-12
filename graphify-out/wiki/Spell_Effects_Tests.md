# Spell Effects Tests

> 44 nodes

## Key Concepts

- **HolidayCollection** (37 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (20 connections) — `server/tests/unit/services/test_holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **.test_init_with_collection()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_activates_matching_holiday()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_no_matches()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_expires_old_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_caps_duration()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holiday_names()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays_wraps_around()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_summary()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_day_ordinal()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_collection_property()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_last_refresh_property()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.id_map()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.collection()** (3 connections) — `server/services/holiday_service.py`
- **.sample_holidays()** (3 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.ensure_unique_ids()** (2 connections) — `server/schemas/calendar/calendar.py`
- **.mock_chronicle()** (2 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Wrapper for the complete holiday JSON payload.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Create a mapping of holiday IDs to holiday entries.          Returns:** (1 connections) — `server/schemas/calendar/calendar.py`
- **Ensure all holiday IDs are unique.          Raises:             ValueError: If d** (1 connections) — `server/schemas/calendar/calendar.py`
- *... and 19 more nodes in this community*

## Relationships

- [Combat Messaging Base](Combat_Messaging_Base.md) (25 shared connections)
- [Error Handling Guide](Error_Handling_Guide.md) (7 shared connections)
- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (6 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (2 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 150 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*