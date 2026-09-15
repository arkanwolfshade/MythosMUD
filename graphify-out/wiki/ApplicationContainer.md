# ApplicationContainer

> 145 nodes

## Key Concepts

- **ApplicationContainer** (162 connections) — `server/container/main.py`
- **lifespan_startup.py** (65 connections) — `server/app/lifespan_startup.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **.get_instance()** (23 connections) — `server/container/main.py`
- **get_container()** (21 connections) — `server/container/main.py`
- **container/__init__.py** (18 connections) — `server/container/__init__.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **FastAPI** (15 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (9 connections) — `server/app/lifespan_startup.py`
- **_attach_combat_service()** (8 connections) — `server/app/lifespan_startup.py`
- **fixtures/unit/__init__.py** (8 connections) — `server/tests/fixtures/unit/__init__.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **nats_is_connected()** (5 connections) — `server/app/lifespan_protocols.py`
- **_ensure_room_cache_before_npc_startup()** (5 connections) — `server/app/lifespan_startup.py`
- *... and 120 more nodes in this community*

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (42 shared connections)
- [test_lifespan_startup.py](test_lifespan_startup.py.md) (26 shared connections)
- [PlayerService](PlayerService.md) (14 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (13 shared connections)
- [NPCDefinition](NPCDefinition.md) (12 shared connections)
- [lifespan.py](lifespan.py.md) (11 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (5 shared connections)
- [HolidayService](HolidayService.md) (5 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_startup.py`
- `server/container/__init__.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/services/combat_cleanup_handler.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 462 (95%)
- INFERRED: 26 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*