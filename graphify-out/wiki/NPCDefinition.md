# NPCDefinition

> 524 nodes

## Key Concepts

- **NPCDefinition** (108 connections) — `server/models/npc.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **test_npc_service.py** (49 connections) — `server/tests/unit/services/test_npc_service.py`
- **NPCSpawningService** (48 connections) — `server/npc/spawning_service.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **models/npc.py** (37 connections) — `server/models/npc.py`
- **asyncio** (35 connections)
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **_mock_result_mappings_all()** (29 connections) — `server/tests/unit/services/test_npc_service.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **asyncio** (23 connections)
- **spawning_request_execution.py** (19 connections) — `server/npc/spawning_request_execution.py`
- **npc_startup_service.py** (19 connections) — `server/services/npc_startup_service.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **_def_row()** (18 connections) — `server/tests/unit/services/test_npc_service.py`
- **SimpleNPCDefinition** (15 connections) — `server/npc/spawning_models.py`
- **definition_crud.py** (15 connections) — `server/services/npc_service/definition_crud.py`
- **npc_service/__init__.py** (15 connections) — `server/services/npc_service/__init__.py`
- **NPCBundle** (14 connections) — `server/container/bundles/npc.py`
- **NPCSpawnResult** (14 connections) — `server/npc/spawning_models.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- *... and 499 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (146 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (12 shared connections)
- [Any](Any.md) (12 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (11 shared connections)
- [DatabaseError](DatabaseError.md) (10 shared connections)
- [database.py](database.py.md) (7 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (6 shared connections)
- [router.py](router.py.md) (6 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (5 shared connections)
- [NPCStartupService](NPCStartupService.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)
- [npc_database.py](npc_database.py.md) (4 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/npc/threading.py`
- `server/services/npc_instance_service.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/models/test_npc_models.py`

## Audit Trail

- EXTRACTED: 1976 (98%)
- INFERRED: 39 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*