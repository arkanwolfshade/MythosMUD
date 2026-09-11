# ScheduleEntry

> 140 nodes

## Key Concepts

- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **MythosHourTickEvent** (15 connections) — `server/events/event_types.py`
- **test_schedule_service.py** (12 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **test_database_config_helpers_asyncpg_settings.py** (9 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_time_event_consumer.py** (8 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **.initialize()** (6 connections) — `server/container/bundles/time.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (6 connections) — `server/services/schedule_service.py`
- **_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **field_validator** (6 connections)
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **._load_from_database()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_load_from_database_success()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 115 more nodes in this community*

## Relationships

- [time.py](time.py.md) (30 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [event_types.py](event_types.py.md) (10 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [RoomService](RoomService.md) (4 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [passive_corruption_flux/service.py](passive_corruption_flux-service.py.md) (2 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/database_config_helpers.py`
- `server/events/event_types.py`
- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 293 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*