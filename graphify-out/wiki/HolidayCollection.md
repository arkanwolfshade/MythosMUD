# HolidayCollection

> 98 nodes

## Key Concepts

- **HolidayService** (41 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (37 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **TestHolidayService** (20 connections) — `server/tests/unit/services/test_holiday_service.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
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
- **test_holiday_collection_ensure_unique_ids()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **.test_init_with_collection()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_activates_matching_holiday()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_no_matches()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_expires_old_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_refresh_active_caps_duration()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- *... and 73 more nodes in this community*

## Relationships

- [hash password()](hash_password%28%29.md) (23 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (11 shared connections)
- [Formatter](Formatter.md) (7 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (5 shared connections)
- [get health status()](get_health_status%28%29.md) (5 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (3 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (3 shared connections)
- [test player event handlers state](test_player_event_handlers_state.md) (2 shared connections)
- [rate overrides](rate_overrides.md) (2 shared connections)
- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (2 shared connections)
- [metrics](metrics.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 372 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*