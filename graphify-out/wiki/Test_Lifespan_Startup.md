# Test Lifespan Startup

> 143 nodes

## Key Concepts

- **lifespan_startup.py** (66 connections) — `server/app/lifespan_startup.py`
- **lifespan.py** (46 connections) — `server/app/lifespan.py`
- **test_lifespan_startup.py** (43 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **FastAPI** (16 connections)
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (15 connections)
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **test_jwt_strategy.py** (10 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (9 connections) — `server/app/lifespan_startup.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **_attach_combat_service()** (8 connections) — `server/app/lifespan_startup.py`
- **set_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **_get_item_prototype_entries()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- *... and 118 more nodes in this community*

## Relationships

- [Application Container Bundles](Application_Container_Bundles.md) (22 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (13 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (10 shared connections)
- [Performance Monitor](Performance_Monitor.md) (6 shared connections)
- [Test Users](Test_Users.md) (6 shared connections)
- [Lifespan Protocols](Lifespan_Protocols.md) (5 shared connections)
- [Lucidity Helpers & Catatonia](Lucidity_Helpers_&_Catatonia.md) (5 shared connections)
- [Test Player Death Service](Test_Player_Death_Service.md) (4 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (4 shared connections)
- [Test Game Tick Death](Test_Game_Tick_Death.md) (4 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (4 shared connections)
- [Test Lifespan Event Subscriptions](Test_Lifespan_Event_Subscriptions.md) (4 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_protocols.py`
- `server/app/lifespan_startup.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/auth/test_jwt_strategy.py`

## Audit Trail

- EXTRACTED: 408 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*