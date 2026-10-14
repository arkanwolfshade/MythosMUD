# NPCDefinitionCRUDMixin

> 40 nodes

## Key Concepts

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
- **._add_json_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._add_simple_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **.delete_npc_definition()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._log_npc_definition_created()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._validate_create_npc_definition_params()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._validate_npc_update_params()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **Any** (4 connections)
- **AsyncSession** (3 connections)
- **Any** (2 connections)
- **Execute create_npc_definition stored procedure and return the created…** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Validate create_npc_definition parameters. Raises ValueError if invalid.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Log successful NPC definition creation.** (1 connections) — `server/services/npc_service/definition_crud.py`
- *... and 15 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [EventBus](EventBus.md) (11 shared connections)
- [ValueError](ValueError.md) (2 shared connections)
- [NPCService](NPCService.md) (1 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (1 shared connections)

## Source Files

- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 92 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*