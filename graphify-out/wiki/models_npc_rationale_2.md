# models npc rationale

> 343 nodes

## Key Concepts

- **NPCDefinition** (121 connections) — `server/models/npc.py`
- **NPCSpawnRule** (55 connections) — `server/models/npc.py`
- **test_npc_service.py** (49 connections) — `server/tests/unit/services/test_npc_service.py`
- **npc.py** (38 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **_mock_result_mappings_all()** (29 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (22 connections) — `server/npc/spawn_validator.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **_def_row()** (18 connections) — `server/tests/unit/services/test_npc_service.py`
- **npc_startup_service.py** (16 connections) — `server/services/npc_startup_service.py`
- **__init__.py** (15 connections) — `server/services/npc_service/__init__.py`
- **definition_crud.py** (15 connections) — `server/services/npc_service/definition_crud.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **spawn_validator.py** (11 connections) — `server/npc/spawn_validator.py`
- **queries.py** (11 connections) — `server/services/npc_service/queries.py`
- **spawn_rule_crud.py** (11 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **_JSONDict** (10 connections)
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **._evaluate_spawn_requirements()** (9 connections) — `server/npc/spawning_service.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- *... and 318 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (47 shared connections)
- [models npc rationale](models_npc_rationale.md) (18 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (16 shared connections)
- [Database Config](Database_Config.md) (13 shared connections)
- [player realtime event](player_realtime_event.md) (10 shared connections)
- [spell game magic](spell_game_magic.md) (8 shared connections)
- [admin auth service](admin_auth_service.md) (7 shared connections)
- [commands npc admin](commands_npc_admin.md) (6 shared connections)
- [combat services rationale](combat_services_rationale.md) (6 shared connections)
- [world models rationale](world_models_rationale.md) (5 shared connections)
- [tools generate invite](tools_generate_invite.md) (5 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (5 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 1285 (96%)
- INFERRED: 49 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*