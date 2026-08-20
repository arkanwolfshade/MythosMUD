# NPCDefinition

> 169 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **definition_crud.py** (16 connections) — `server/services/npc_service/definition_crud.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **queries.py** (12 connections) — `server/services/npc_service/queries.py`
- **NPCDefinitionType** (11 connections) — `server/models/npc.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **_JSONDict** (10 connections)
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **NPCQueryMixin** (7 connections) — `server/services/npc_service/queries.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **Base** (6 connections) — `server/models/npc.py`
- **CreateNPCDefinitionInput** (6 connections) — `server/services/npc_service_models.py`
- **NPCDefinitionCreateParams** (6 connections) — `server/services/npc_service_models.py`
- *... and 144 more nodes in this community*

## Relationships

- [NPCSpawningService](NPCSpawningService.md) (24 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (24 shared connections)
- [get_logger](get_logger.md) (22 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (17 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (8 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (8 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (7 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (7 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (6 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [population_control.py](population_control.py.md) (3 shared connections)
- [NPCStartupService](NPCStartupService.md) (2 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/population_control.py`
- `server/npc/threading.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`

## Audit Trail

- EXTRACTED: 398 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*