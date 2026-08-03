# spawn npc services

> 37 nodes

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
- **.get_npc_definitions_by_sub_zone()** (5 connections) — `server/services/npc_service/queries.py`
- **._log_npc_definition_created()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._add_simple_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **Any** (4 connections)
- **._add_json_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **.delete_npc_definition()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._validate_create_npc_definition_params()** (3 connections) — `server/services/npc_service/definition_crud.py`
- **._validate_npc_update_params()** (3 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (3 connections)
- **Mixin providing NPC definition CRUD operations.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Get all NPC definitions.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Get a specific NPC definition by ID.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Get an NPC definition by name (case-insensitive).** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Create a new NPC definition.** (1 connections) — `server/services/npc_service/definition_crud.py`
- *... and 12 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (13 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (10 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 147 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*