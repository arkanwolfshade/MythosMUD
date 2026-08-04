# container events rationale

> 300 nodes

## Key Concepts

- **NPCDefinition** (121 connections) — `server/models/npc.py`
- **NPCSpawnRule** (55 connections) — `server/models/npc.py`
- **test_npc_service.py** (49 connections) — `server/tests/unit/services/test_npc_service.py`
- **npc.py** (38 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **_mock_result_mappings_all()** (29 connections) — `server/tests/unit/services/test_npc_service.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **_def_row()** (18 connections) — `server/tests/unit/services/test_npc_service.py`
- **__init__.py** (15 connections) — `server/services/npc_service/__init__.py`
- **definition_crud.py** (15 connections) — `server/services/npc_service/definition_crud.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **NPCDefinitionType** (11 connections) — `server/models/npc.py`
- **queries.py** (11 connections) — `server/services/npc_service/queries.py`
- **spawn_rule_crud.py** (11 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **_JSONDict** (10 connections)
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- *... and 275 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (33 shared connections)
- [Error Conversion](Error_Conversion.md) (24 shared connections)
- [spell game magic](spell_game_magic.md) (18 shared connections)
- [models npc rationale](models_npc_rationale.md) (13 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (13 shared connections)
- [NPC Combat](NPC_Combat.md) (10 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (9 shared connections)
- [commands npc admin](commands_npc_admin.md) (6 shared connections)
- [world models rationale](world_models_rationale.md) (6 shared connections)
- [tools generate invite](tools_generate_invite.md) (5 shared connections)
- [combat services rationale](combat_services_rationale.md) (5 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (5 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/services/test_npc_instance_service.py`
- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 1125 (97%)
- INFERRED: 39 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*