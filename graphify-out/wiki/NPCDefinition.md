# NPCDefinition

> 118 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition_by_name()** (5 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions_by_sub_zone()** (5 connections) — `server/services/npc_service/queries.py`
- **.get_npc_definitions_by_type()** (5 connections) — `server/services/npc_service/queries.py`
- **_set_default_if_missing()** (4 connections) — `server/models/npc.py`
- **.can_spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._add_json_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._add_simple_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **.delete_npc_definition()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._log_npc_definition_created()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/models/npc.py`
- **.create_npc_instance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.__init__()** (3 connections) — `server/npc/lifecycle_types.py`
- *... and 93 more nodes in this community*

## Relationships

- [ZoneConfiguration](ZoneConfiguration.md) (26 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (23 shared connections)
- [get_logger](get_logger.md) (18 shared connections)
- [event_types.py](event_types.py.md) (8 shared connections)
- [NPCBase](NPCBase.md) (7 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (7 shared connections)
- [_JSONDict](_JSONDict.md) (6 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (5 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (3 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [npc_database.py](npc_database.py.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`

## Audit Trail

- EXTRACTED: 278 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*