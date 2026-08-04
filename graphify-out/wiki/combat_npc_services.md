# combat npc services

> 28 nodes

## Key Concepts

- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
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
- **Validate create_npc_definition parameters. Raises ValueError if invalid.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Log successful NPC definition creation.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Validate NPC update parameters.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Add a simple field to update_data if value is not None.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Add a JSON-encoded field to update_data if value is not None.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Build update data dictionary from provided parameters.** (1 connections) — `server/services/npc_service/definition_crud.py`
- *... and 3 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (13 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [player death service](player_death_service.md) (1 shared connections)

## Source Files

- `server/services/npc_service/definition_crud.py`

## Audit Trail

- EXTRACTED: 107 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*