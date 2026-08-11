# Spell Effects Tests

> 42 nodes

## Key Concepts

- **HolidayCollection** (37 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (20 connections) — `server/tests/unit/services/test_holiday_service.py`
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
- **Get the holiday collection.          Returns:             HolidayCollection: The** (1 connections) — `server/services/holiday_service.py`
- *... and 17 more nodes in this community*

## Relationships

- [Player Respawn Service](Player_Respawn_Service.md) (24 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (5 shared connections)
- [Async Room Loading Tests](Async_Room_Loading_Tests.md) (4 shared connections)
- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (4 shared connections)
- [Cursor Skills Critique](Cursor_Skills_Critique.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 145 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*