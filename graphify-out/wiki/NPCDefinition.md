# NPCDefinition

> 339 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **NPCSpawningService** (69 connections) — `server/npc/spawning_service.py`
- **ZoneConfiguration** (54 connections) — `server/npc/zone_configuration.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **test_spawning_modules.py** (47 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_service.py** (41 connections) — `server/npc/spawning_service.py`
- **models/npc.py** (38 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **Random** (22 connections)
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **SimpleNPCDefinition** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **spawn_validator.py** (15 connections) — `server/npc/spawn_validator.py`
- **spawning_models.py** (14 connections) — `server/npc/spawning_models.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_JSONDict** (10 connections)
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- *... and 314 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (65 shared connections)
- [NPCBase](NPCBase.md) (46 shared connections)
- [EventBus](EventBus.md) (21 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (20 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [test_population_control.py](test_population_control.py.md) (16 shared connections)
- [test_npc_definitions_api.py](test_npc_definitions_api.py.md) (8 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (8 shared connections)
- [zone_config_loader.py](zone_config_loader.py.md) (8 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (7 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (7 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (6 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/npc/threading.py`
- `server/npc/zone_configuration.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_spawning_modules.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 817 (95%)
- INFERRED: 44 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*