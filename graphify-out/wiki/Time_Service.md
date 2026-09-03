# Time Service

> 123 nodes

## Key Concepts

- **MythosTickScheduler** (32 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **test_time_bundle.py** (22 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_tick_scheduler.py** (19 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **tick_scheduler.py** (17 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **asyncio** (9 connections)
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **isolated_chronicle()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_get_mythos_chronicle_singleton()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_time_bundle_initialize_missing_dependencies()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- *... and 98 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (9 shared connections)
- [Test Game Tick Death](Test_Game_Tick_Death.md) (7 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (5 shared connections)
- [Holiday Calendar Validation](Holiday_Calendar_Validation.md) (5 shared connections)
- [Lifespan Protocols](Lifespan_Protocols.md) (4 shared connections)
- [Test Schedule Service](Test_Schedule_Service.md) (4 shared connections)
- [Task Registry](Task_Registry.md) (4 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (3 shared connections)
- [Test Config Init](Test_Config_Init.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (3 shared connections)
- [Test Command Factories Utility](Test_Command_Factories_Utility.md) (2 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)

## Source Files

- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 255 (92%)
- INFERRED: 22 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*