# NPCDefinition

> 201 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **lifecycle_periodic.py** (19 connections) — `server/npc/lifecycle_periodic.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **definition_crud.py** (16 connections) — `server/services/npc_service/definition_crud.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **spawning_models.py** (13 connections) — `server/npc/spawning_models.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **queries.py** (12 connections) — `server/services/npc_service/queries.py`
- **spawn_rule_crud.py** (12 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCDefinitionType** (11 connections) — `server/models/npc.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **NPCMaintenanceConfig** (10 connections) — `server/config/npc_config.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- *... and 176 more nodes in this community*

## Relationships

- [NPCLifecycleManager](NPCLifecycleManager.md) (19 shared connections)
- [DatabaseError](DatabaseError.md) (19 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (15 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (14 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (13 shared connections)
- [test_spawn_validator.py](test_spawn_validator.py.md) (13 shared connections)
- [ConnectionManager](ConnectionManager.md) (12 shared connections)
- [test_npc_definitions_api.py](test_npc_definitions_api.py.md) (11 shared connections)
- [EventBus](EventBus.md) (10 shared connections)
- [_JSONDict](_JSONDict.md) (10 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (8 shared connections)

## Source Files

- `server/config/npc_config.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/npc/threading.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`

## Audit Trail

- EXTRACTED: 549 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*