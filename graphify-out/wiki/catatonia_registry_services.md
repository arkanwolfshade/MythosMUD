# catatonia registry services

> 91 nodes

## Key Concepts

- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **CatatoniaRegistry** (43 connections) — `server/services/catatonia_registry.py`
- **TestCatatoniaRegistry** (26 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **FastAPI** (13 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **catatonia_registry.py** (12 connections) — `server/services/catatonia_registry.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **UUID** (6 connections)
- **_start_npc_thread_manager_and_pending()** (4 connections) — `server/app/lifespan_startup.py`
- **datetime** (4 connections)
- **.is_catatonic()** (4 connections) — `server/services/catatonia_registry.py`
- **test_catatonia_registry.py** (4 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.on_catatonia_entered()** (3 connections) — `server/services/catatonia_registry.py`
- **.on_catatonia_cleared()** (3 connections) — `server/services/catatonia_registry.py`
- **.should_trigger_sanitarium_failover()** (3 connections) — `server/services/catatonia_registry.py`
- **.get_snapshot()** (3 connections) — `server/services/catatonia_registry.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_init_with_failover_callback()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- *... and 66 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (25 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (17 shared connections)
- [aggro threat services](aggro_threat_services.md) (10 shared connections)
- [nats services service](nats_services_service.md) (8 shared connections)
- [player room realtime](player_room_realtime.md) (7 shared connections)
- [room look commands](room_look_commands.md) (4 shared connections)
- [realtime player connection](realtime_player_connection.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [player service game](player_service_game.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [auth rationale access](auth_rationale_access.md) (3 shared connections)
- [player room event](player_room_event.md) (2 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/services/catatonia_registry.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 376 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*