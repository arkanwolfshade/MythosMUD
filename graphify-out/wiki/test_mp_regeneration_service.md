# test mp regeneration service

> 34 nodes

## Key Concepts

- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition_by_name()** (5 connections) — `server/services/npc_service/definition_crud.py`
- **._log_npc_definition_created()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._add_simple_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **Any** (4 connections)
- **._add_json_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **.delete_npc_definition()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._validate_create_npc_definition_params()** (3 connections) — `server/services/npc_service/definition_crud.py`
- **._validate_npc_update_params()** (3 connections) — `server/services/npc_service/definition_crud.py`
- **Mixin providing NPC definition CRUD operations.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Get all NPC definitions.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Get a specific NPC definition by ID.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Get an NPC definition by name (case-insensitive).** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Create a new NPC definition.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Execute create_npc_definition stored procedure and return the created definition** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Validate create_npc_definition parameters. Raises ValueError if invalid.** (1 connections) — `server/services/npc_service/definition_crud.py`
- *... and 9 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (16 shared connections)
- [real time](real_time.md) (3 shared connections)
- [message handlers](message_handlers.md) (2 shared connections)
- [Profession](Profession.md) (2 shared connections)
- [def row()](def_row%28%29.md) (1 shared connections)
- [projectorHandlersMessages](projectorHandlersMessages.md) (1 shared connections)

## Source Files

- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 138 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*