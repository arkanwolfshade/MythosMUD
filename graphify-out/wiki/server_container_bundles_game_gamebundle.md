# server container bundles game gamebundle

> 204 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **get_mythos_chronicle()** (27 connections) — `server/time/time_service.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **holiday_service.py** (25 connections) — `server/services/holiday_service.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **test_time_bundle.py** (21 connections) — `server/tests/unit/container/test_time_bundle.py`
- **MythosHourTickEvent** (15 connections) — `server/events/event_types.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **test_holiday_service.py** (10 connections) — `server/tests/unit/services/test_holiday_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **._init_temporal_layer()** (9 connections) — `server/container/bundles/game.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **test_time_event_consumer.py** (9 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- *... and 179 more nodes in this community*

## Relationships

- [claude rules fastapi](claude_rules_fastapi.md) (37 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (26 shared connections)
- [server services schedule service databaseloadresult](server_services_schedule_service_databaseloadresult.md) (13 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (11 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (8 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (7 shared connections)
- [server tests unit time test](server_tests_unit_time_test.md) (5 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (5 shared connections)
- [moduletype](moduletype.md) (4 shared connections)
- [server config init](server_config_init.md) (4 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (3 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (3 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/events/event_types.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/__init__.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 481 (95%)
- INFERRED: 25 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*