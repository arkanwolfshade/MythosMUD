# NPCDefinition

> 337 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **migrate_combat_data.py** (28 connections) — `server/scripts/migrate_combat_data.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_combat_schema.py** (20 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **CombatSchemaValidationError** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_base_stats_combat_data()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_combat_messages()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **combat/__init__.py** (10 connections) — `server/schemas/combat/__init__.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **add_default_combat_data_to_stats()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **validate_behavior_config_combat_data()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **_migrate_one_npc()** (9 connections) — `server/scripts/migrate_combat_data.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- *... and 312 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (67 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (14 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (11 shared connections)
- [NPCBase](NPCBase.md) (7 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (5 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [npc_database.py](npc_database.py.md) (4 shared connections)
- [server/models/__init__.py](server-models-__init__.py.md) (3 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/npc/threading.py`
- `server/schemas/combat/__init__.py`
- `server/schemas/combat/combat_schema.py`
- `server/scripts/migrate_combat_data.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 687 (99%)
- INFERRED: 10 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*