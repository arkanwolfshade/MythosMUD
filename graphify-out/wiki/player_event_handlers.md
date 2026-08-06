# player event handlers

> 333 nodes

## Key Concepts

- **AsyncPersistenceLayer** (188 connections) — `server/async_persistence.py`
- **HolidayService** (45 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (41 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Any** (19 connections)
- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **CreateItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **test_holiday_service.py** (9 connections) — `server/tests/unit/services/test_holiday_service.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- *... and 308 more nodes in this community*

## Relationships

- [room realtime occupant](room_realtime_occupant.md) (32 shared connections)
- [Error Conversion](Error_Conversion.md) (24 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (23 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (22 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (10 shared connections)
- [Exception Containers](Exception_Containers.md) (6 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (6 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (6 shared connections)
- [EdgeCreationModal map STANDARD](EdgeCreationModal_map_STANDARD.md) (6 shared connections)
- [services user manager](services_user_manager.md) (5 shared connections)
- [tick game processing](tick_game_processing.md) (5 shared connections)
- [lucidity event services](lucidity_event_services.md) (4 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/npc/combat_integration_base.py`
- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 1213 (94%)
- INFERRED: 81 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*