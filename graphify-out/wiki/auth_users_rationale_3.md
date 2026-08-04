# auth users rationale

> 82 nodes

## Key Concepts

- **HolidayService** (45 connections) — `server/services/holiday_service.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **test_holiday_service.py** (9 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **datetime** (7 connections)
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **_ensure_utc()** (6 connections) — `server/services/holiday_service.py`
- **.test_async_load_from_database()** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_string_list_from_row()** (5 connections) — `server/services/holiday_service.py`
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
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
- *... and 57 more nodes in this community*

## Relationships

- [holiday service services](holiday_service_services.md) (30 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (11 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (6 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (1 shared connections)
- [rate lucidity services](rate_lucidity_services.md) (1 shared connections)

## Source Files

- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 275 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*