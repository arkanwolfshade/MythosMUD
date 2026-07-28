# Server App

> 167 nodes

## Key Concepts

- **ApplicationContainer** (131 connections) — `server/container/main.py`
- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **FastAPI** (13 connections)
- **get_container()** (13 connections) — `server/container/main.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **lifespan_event_subscriptions.py** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **.event_bus()** (11 connections) — `server/realtime/connection_manager.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **subscribe_quest_events()** (9 connections) — `server/app/lifespan_event_subscriptions.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **reset_container()** (8 connections) — `server/container/main.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **__init__.py** (8 connections) — `server/tests/fixtures/unit/__init__.py`
- **subscribe_room_occupants_refresh()** (7 connections) — `server/app/lifespan_event_subscriptions.py`
- **__init__.py** (7 connections) — `server/container/__init__.py`
- *... and 142 more nodes in this community*

## Relationships

- [Server App (2)](Server_App_%282%29.md) (25 shared connections)
- [Server Monitoring](Server_Monitoring.md) (17 shared connections)
- [Server Npc](Server_Npc.md) (17 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (17 shared connections)
- [Server Commands](Server_Commands.md) (12 shared connections)
- [Server Events](Server_Events.md) (9 shared connections)
- [Server Services](Server_Services.md) (8 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (7 shared connections)
- [Server Realtime (16)](Server_Realtime_%2816%29.md) (6 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (5 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (5 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (5 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/container/__init__.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/fixtures/unit/mock_helpers.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 761 (95%)
- INFERRED: 38 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*