# OccupantFormatter

> 84 nodes · cohesion 0.04

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (40 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **.__init__()** (9 connections) — `server/services/holiday_service.py`
- **test_holiday_service.py** (9 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **_ensure_utc()** (6 connections) — `server/services/holiday_service.py`
- **datetime** (6 connections)
- **.test_init_loads_from_database()** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **.sample_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_collection_property()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_day_ordinal()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holiday_names()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_active_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_serialized_active_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_serialized_upcoming_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_get_upcoming_holidays_wraps_around()** (4 connections) — `server/tests/unit/services/test_holiday_service.py`
- *... and 59 more nodes in this community*

## Relationships

- [NPCCombatDataProvider](NPCCombatDataProvider.md) (17 shared connections)
- [start_grace_period](start_grace_period.md) (14 shared connections)
- [populate_npc_sample_data.py](populate_npc_sample_data.py.md) (7 shared connections)
- [Communities (11 total, 0 thin omitted)](Communities_11_total,_0_thin_omitted.md) (5 shared connections)
- [EventHandler](EventHandler.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [test_party_service.py](test_party_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 190 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*