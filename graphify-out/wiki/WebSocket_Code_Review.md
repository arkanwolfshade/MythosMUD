# WebSocket Code Review

> 75 nodes

## Key Concepts

- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **time_event_consumer.py** (24 connections) — `server/time/time_event_consumer.py`
- **MythosTimeEventConsumer** (23 connections) — `server/time/time_event_consumer.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **MythosHourTickEvent** (12 connections) — `server/events/event_types.py`
- **_schedule_entry_from_row()** (8 connections) — `server/services/schedule_service.py`
- **test_schedule_service.py** (8 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.__init__()** (8 connections) — `server/time/time_event_consumer.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **._handle_tick()** (6 connections) — `server/time/time_event_consumer.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **_DatabaseLoadResult** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Any** (5 connections)
- **_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **.test_init_loads_from_database()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 50 more nodes in this community*

## Relationships

- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (16 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (12 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (11 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (9 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (7 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (6 shared connections)
- [Real-Time Architecture Docs](Real-Time_Architecture_Docs.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (3 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (3 shared connections)
- [Test Migration Report](Test_Migration_Report.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 285 (90%)
- INFERRED: 32 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*