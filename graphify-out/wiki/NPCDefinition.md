# NPCDefinition

> 419 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **ZoneConfiguration** (54 connections) — `server/npc/zone_configuration.py`
- **test_npc_service.py** (50 connections) — `server/tests/unit/services/test_npc_service.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **asyncio** (35 connections)
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **_mock_result_mappings_all()** (29 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_spawn_validator.py** (25 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **_def_row()** (18 connections) — `server/tests/unit/services/test_npc_service.py`
- **definition_crud.py** (16 connections) — `server/services/npc_service/definition_crud.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **queries.py** (12 connections) — `server/services/npc_service/queries.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- *... and 394 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (56 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (28 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (14 shared connections)
- [NPCBase](NPCBase.md) (12 shared connections)
- [DatabaseError](DatabaseError.md) (12 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (6 shared connections)
- [Player](Player.md) (5 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (5 shared connections)
- [test_npc_admin_commands.py](test_npc_admin_commands.py.md) (5 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (3 shared connections)
- [PopulationStats](PopulationStats.md) (3 shared connections)

## Source Files

- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_service.py`
- `server/npc/zone_configuration.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_configuration.py`
- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 837 (95%)
- INFERRED: 47 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*