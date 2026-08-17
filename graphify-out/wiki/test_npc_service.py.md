# test_npc_service.py

> 278 nodes

## Key Concepts

- **test_npc_service.py** (50 connections) — `server/tests/unit/services/test_npc_service.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **asyncio** (35 connections)
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **_mock_result_mappings_all()** (29 connections) — `server/tests/unit/services/test_npc_service.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **_def_row()** (18 connections) — `server/tests/unit/services/test_npc_service.py`
- **definition_crud.py** (16 connections) — `server/services/npc_service/definition_crud.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **spawn_rule_crud.py** (12 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **AsyncSession** (8 connections)
- **NPCQueryMixin** (7 connections) — `server/services/npc_service/queries.py`
- *... and 253 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (61 shared connections)
- [DatabaseError](DatabaseError.md) (15 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (7 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (6 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (5 shared connections)
- [get_session_maker](get_session_maker.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (2 shared connections)
- [_NPCCombatIntegrationValidationDeps](_NPCCombatIntegrationValidationDeps.md) (1 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 559 (99%)
- INFERRED: 8 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*