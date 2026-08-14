# NPCDefinitionCRUDMixin

> 28 nodes

## Key Concepts

- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition_by_name()** (5 connections) — `server/services/npc_service/definition_crud.py`
- **._add_json_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._add_simple_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **.delete_npc_definition()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._log_npc_definition_created()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **Any** (4 connections)
- **._validate_create_npc_definition_params()** (3 connections) — `server/services/npc_service/definition_crud.py`
- **._validate_npc_update_params()** (3 connections) — `server/services/npc_service/definition_crud.py`
- **Validate create_npc_definition parameters. Raises ValueError if invalid.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Log successful NPC definition creation.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Validate NPC update parameters.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Add a simple field to update_data if value is not None.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Add a JSON-encoded field to update_data if value is not None.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Build update data dictionary from provided parameters.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Execute the database update via procedure and return updated definition.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Mixin providing NPC definition CRUD operations.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Update an existing NPC definition.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Delete an NPC definition.** (1 connections) — `server/services/npc_service/definition_crud.py`
- *... and 3 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [EventBus](EventBus.md) (6 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)

## Source Files

- `server/services/npc_service/definition_crud.py`

## Audit Trail

- EXTRACTED: 64 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*