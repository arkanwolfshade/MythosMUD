# User Manager Mute Tests

> 175 nodes

## Key Concepts

- **ApplicationContainer** (151 connections) — `server/container/main.py`
- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **FastAPI** (13 connections)
- **lifespan_event_subscriptions.py** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_combat_services()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **subscribe_quest_events()** (9 connections) — `server/app/lifespan_event_subscriptions.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **subscribe_room_occupants_refresh()** (7 connections) — `server/app/lifespan_event_subscriptions.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **.reset_instance()** (6 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- *... and 150 more nodes in this community*

## Relationships

- [WebSocket Code Review](WebSocket_Code_Review.md) (43 shared connections)
- [Client Event Store](Client_Event_Store.md) (16 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (13 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (13 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (11 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (11 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (8 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (8 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (6 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (5 shared connections)
- [Combat Schema Validation](Combat_Schema_Validation.md) (4 shared connections)
- [Catatonia Registry Service](Catatonia_Registry_Service.md) (4 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/services/test_npc_service.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 734 (96%)
- INFERRED: 29 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*