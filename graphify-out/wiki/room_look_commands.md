# room look commands

> 214 nodes

## Key Concepts

- **NPCDefinition** (121 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **__init__.py** (15 connections) — `server/services/npc_service/__init__.py`
- **definition_crud.py** (15 connections) — `server/services/npc_service/definition_crud.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
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
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **._spawn_npc()** (7 connections) — `server/npc/population_control.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- *... and 189 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (49 shared connections)
- [container events rationale](container_events_rationale.md) (42 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (14 shared connections)
- [lucidity event services](lucidity_event_services.md) (12 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (5 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (4 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [countdown rest task](countdown_rest_task.md) (3 shared connections)
- [npc lifecycle config](npc_lifecycle_config.md) (3 shared connections)
- [auth rationale access](auth_rationale_access.md) (3 shared connections)

## Source Files

- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawning_models.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 753 (96%)
- INFERRED: 33 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*