# ApplicationContainer

> 129 nodes

## Key Concepts

- **ApplicationContainer** (145 connections) — `server/container/main.py`
- **lifespan_startup.py** (60 connections) — `server/app/lifespan_startup.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections)
- **asyncio** (12 connections)
- **initialize_combat_services()** (11 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **subscribe_quest_events()** (8 connections) — `server/app/lifespan_event_subscriptions.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **subscribe_room_occupants_refresh()** (6 connections) — `server/app/lifespan_event_subscriptions.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **.reset_instance()** (6 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **_get_item_prototype_count()** (5 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **.initialize()** (5 connections) — `server/container/main.py`
- *... and 104 more nodes in this community*

## Relationships

- [bundles/game.py](bundles-game.py.md) (51 shared connections)
- [get_logger](get_logger.md) (32 shared connections)
- [magic_service.py](magic_service.py.md) (17 shared connections)
- [lifespan.py](lifespan.py.md) (14 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (14 shared connections)
- [NPCDefinition](NPCDefinition.md) (12 shared connections)
- [GameBundle](GameBundle.md) (8 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (5 shared connections)
- [lifespan_shutdown.py](lifespan_shutdown.py.md) (4 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)
- [LucidityService](LucidityService.md) (4 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/main.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 636 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*