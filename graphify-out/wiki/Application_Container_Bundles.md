# Application Container Bundles

> 181 nodes

## Key Concepts

- **ApplicationContainer** (157 connections) — `server/container/main.py`
- **bundles/game.py** (40 connections) — `server/container/bundles/game.py`
- **container/main.py** (38 connections) — `server/container/main.py`
- **test_application_container.py** (29 connections) — `server/tests/unit/test_application_container.py`
- **.get_instance()** (22 connections) — `server/container/main.py`
- **TimeBundle** (21 connections) — `server/container/bundles/time.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **container/__init__.py** (18 connections) — `server/container/__init__.py`
- **test_application_container_main.py** (18 connections) — `server/tests/unit/container/test_application_container_main.py`
- **MonitoringBundle** (17 connections) — `server/container/bundles/monitoring.py`
- **normalize_environment()** (17 connections) — `server/utils/project_paths.py`
- **get_container()** (16 connections) — `server/container/main.py`
- **bundles/npc.py** (16 connections) — `server/container/bundles/npc.py`
- **bundles/realtime.py** (15 connections) — `server/container/bundles/realtime.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **bundles/combat.py** (14 connections) — `server/container/bundles/combat.py`
- **bundles/monitoring.py** (14 connections) — `server/container/bundles/monitoring.py`
- **project_paths.py** (13 connections) — `server/utils/project_paths.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/monitoring.py`
- **chat.py** (11 connections) — `server/container/bundles/chat.py`
- **ChatBundle** (10 connections) — `server/container/bundles/chat.py`
- **._init_temporal_services()** (10 connections) — `server/container/bundles/time.py`
- *... and 156 more nodes in this community*

## Relationships

- [Test Container Bundles](Test_Container_Bundles.md) (73 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (36 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (22 shared connections)
- [Holiday Calendar Validation](Holiday_Calendar_Validation.md) (15 shared connections)
- [Lifespan Magic](Lifespan_Magic.md) (13 shared connections)
- [Lifespan Protocols](Lifespan_Protocols.md) (11 shared connections)
- [Test Chat Npc System](Test_Chat_Npc_System.md) (10 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (8 shared connections)
- [Test Lifespan Event Subscriptions](Test_Lifespan_Event_Subscriptions.md) (7 shared connections)
- [Test Schedule Service](Test_Schedule_Service.md) (6 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (6 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (6 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/game/chat_npc_system.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/schedule_service.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/test_application_container.py`
- `server/tests/unit/utils/test_project_paths.py`

## Audit Trail

- EXTRACTED: 634 (92%)
- INFERRED: 52 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*