# EventBus

> 398 nodes

## Key Concepts

- **EventBus** (157 connections) — `server/events/event_bus.py`
- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **NPCBase** (82 connections) — `server/npc/npc_base.py`
- **NPCSpawningService** (65 connections) — `server/npc/spawning_service.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **models/npc.py** (38 connections) — `server/models/npc.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **spawning_request_execution.py** (20 connections) — `server/npc/spawning_request_execution.py`
- **passive_mob_npc.py** (19 connections) — `server/npc/passive_mob_npc.py`
- **npc_startup_service.py** (19 connections) — `server/services/npc_startup_service.py`
- **SimpleNPCDefinition** (17 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (17 connections) — `server/npc/spawning_request_execution.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **NPCSpawnStatistics** (16 connections) — `server/npc/spawning_service.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **spawning_models.py** (13 connections) — `server/npc/spawning_models.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **NPCSpawnRequest** (12 connections) — `server/npc/spawning_models.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- *... and 373 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (57 shared connections)
- [get_logger](get_logger.md) (50 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (46 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (28 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (20 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (16 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (13 shared connections)
- [population_control.py](population_control.py.md) (12 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (10 shared connections)
- [CombatService](CombatService.md) (10 shared connections)
- [test_population_control.py](test_population_control.py.md) (10 shared connections)
- [.__init__](__init__.md) (10 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/models/npc.py`
- `server/npc/behaviors.py`
- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/npc/threading.py`
- `server/realtime/connection_manager.py`
- `server/schemas/combat/combat_schema.py`
- `server/services/combat_hp_sync.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/models/test_npc_models.py`

## Audit Trail

- EXTRACTED: 1060 (93%)
- INFERRED: 78 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*