# test mp regeneration service

> 61 nodes

## Key Concepts

- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **__init__.py** (15 connections) — `server/services/npc_service/__init__.py`
- **definition_crud.py** (15 connections) — `server/services/npc_service/definition_crud.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **queries.py** (11 connections) — `server/services/npc_service/queries.py`
- **spawn_rule_crud.py** (11 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **NPCQueryMixin** (7 connections) — `server/services/npc_service/queries.py`
- **CreateNPCDefinitionInput** (6 connections) — `server/services/npc_service_models.py`
- **NPCDefinitionCreateParams** (6 connections) — `server/services/npc_service_models.py`
- **.get_npc_definition_by_name()** (5 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions_by_type()** (5 connections) — `server/services/npc_service/queries.py`
- **.get_npc_definitions_by_sub_zone()** (5 connections) — `server/services/npc_service/queries.py`
- **.get_system_statistics()** (5 connections) — `server/services/npc_service/queries.py`
- **._log_npc_definition_created()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._add_simple_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- *... and 36 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (18 shared connections)
- [real time](real_time.md) (10 shared connections)
- [world](world.md) (8 shared connections)
- [. repr ()](_repr_%28%29.md) (7 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [Any](Any.md) (3 shared connections)
- [close db()](close_db%28%29.md) (2 shared connections)
- [Lock](Lock.md) (1 shared connections)

## Source Files

- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 266 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*