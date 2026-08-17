# EventBus

> 402 nodes

## Key Concepts

- **EventBus** (153 connections) — `server/events/event_bus.py`
- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **NPCLifecycleManager** (69 connections) — `server/npc/lifecycle_manager.py`
- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **passive_mob_npc.py** (20 connections) — `server/npc/passive_mob_npc.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **SimpleNPCDefinition** (16 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **shopkeeper_npc.py** (13 connections) — `server/npc/shopkeeper_npc.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **Any** (10 connections)
- *... and 377 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (131 shared connections)
- [get_logger](get_logger.md) (31 shared connections)
- [NPCDied](NPCDied.md) (19 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (10 shared connections)
- [BaseEvent](BaseEvent.md) (9 shared connections)
- [npc_config_parsing.py](npc_config_parsing.py.md) (9 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (8 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (8 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (7 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (6 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (6 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (6 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/events/event_bus.py`
- `server/models/room.py`
- `server/npc/behaviors.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/npc_base.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/realtime/connection_manager.py`
- `server/services/combat_hp_sync.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/npc/test_spawning_modules.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 876 (86%)
- INFERRED: 142 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*