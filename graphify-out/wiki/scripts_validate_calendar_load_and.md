# scripts validate calendar load and

> 193 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (40 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **test_calendar_schemas.py** (23 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_service.py** (13 connections) — `server/tests/unit/services/test_schedule_service.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **calendar/__init__.py** (11 connections) — `server/schemas/calendar/__init__.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **calendar/calendar.py** (10 connections) — `server/schemas/calendar/calendar.py`
- **test_holiday_service.py** (10 connections) — `server/tests/unit/services/test_holiday_service.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **_ensure_utc()** (6 connections) — `server/services/holiday_service.py`
- *... and 168 more nodes in this community*

## Relationships

- [scripts validate calendar](scripts_validate_calendar.md) (34 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (20 shared connections)
- [server api players get player](server_api_players_get_player.md) (5 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (4 shared connections)
- [holidayresolver](holidayresolver.md) (4 shared connections)
- [server api game broadcast message](server_api_game_broadcast_message.md) (3 shared connections)
- [server events event types mythoshourtickevent](server_events_event_types_mythoshourtickevent.md) (3 shared connections)
- [server services schedule service databaseloadresult](server_services_schedule_service_databaseloadresult.md) (3 shared connections)
- [characterinfo](characterinfo.md) (3 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (2 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (2 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 400 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*