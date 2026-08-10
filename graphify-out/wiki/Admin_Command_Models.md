# Admin Command Models

> 34 nodes

## Key Concepts

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
- **.sample_holidays()** (3 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.mock_chronicle()** (2 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Test suite for HolidayService class.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Create a mock chronicle for testing.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Create sample holiday entries for testing.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Test HolidayService initialization with collection parameter.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Test HolidayService initialization without persistence raises ValueError.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Test refresh_active activates holidays matching current date.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Test refresh_active returns empty when no holidays match.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Test refresh_active expires holidays past their duration.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [Player Respawn Service](Player_Respawn_Service.md) (18 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (13 shared connections)

## Source Files

- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 96 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*