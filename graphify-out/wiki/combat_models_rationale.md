# combat models rationale

> 295 nodes

## Key Concepts

- **HolidayService** (45 connections) — `server/services/holiday_service.py`
- **game.py** (43 connections) — `server/container/bundles/game.py`
- **HolidayCollection** (41 connections) — `server/schemas/calendar/calendar.py`
- **.initialize()** (35 connections) — `server/container/bundles/game.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleService** (30 connections) — `server/services/schedule_service.py`
- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **time_service.py** (26 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **test_schedule_service.py** (12 connections) — `server/tests/unit/services/test_schedule_service.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **time_commands.py** (10 connections) — `server/commands/time_commands.py`
- **__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- *... and 270 more nodes in this community*

## Relationships

- [rate limiter services](rate_limiter_services.md) (28 shared connections)
- [nats services service](nats_services_service.md) (21 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (17 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (16 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (7 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (7 shared connections)
- [NPC Combat](NPC_Combat.md) (7 shared connections)
- [aggro threat services](aggro_threat_services.md) (7 shared connections)
- [manager subject services](manager_subject_services.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (5 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/commands/time_commands.py`
- `server/container/bundles/game.py`
- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 1241 (97%)
- INFERRED: 45 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*