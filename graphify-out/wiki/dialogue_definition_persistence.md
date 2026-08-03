# dialogue definition persistence

> 27 nodes

## Key Concepts

- **DialogueDefinitionRepository** (22 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **dialogue_definition_repository.py** (19 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **DialogueDefinition** (13 connections) — `server/models/dialogue.py`
- **_row_to_dialogue()** (9 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.list_all()** (8 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.get_by_id()** (8 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.get_by_npc_definition_id()** (8 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.upsert()** (8 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_DialogueRow** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_as_dialogue_row()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.delete()** (5 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_definition_dict()** (3 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Base** (1 connections)
- **NPC dialogue tree template: id (PK), definition JSONB, optional npc link.** (1 connections) — `server/models/dialogue.py`
- **Protocol** (1 connections)
- **DialogueDefinition repository (#583).  CRUD via PostgreSQL procedures in db/pr** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Shape of dialogue procedure result rows (attribute access via mappings).** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Coerce JSONB definition cell to a plain string-keyed dict.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Narrow SQLAlchemy RowMapping to the dialogue procedure row shape.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Map procedure result row to DialogueDefinition model.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Repository for dialogue_definitions via stored procedures.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Return all dialogue definitions ordered by id.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Load a dialogue definition by id. Returns None if not found.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Load dialogue linked to an NPC definition id. Returns None if none.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- *... and 2 more nodes in this community*

## Relationships

- [npc populate databases](npc_populate_databases.md) (8 shared connections)
- [admin auth service](admin_auth_service.md) (7 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [dialogue service game](dialogue_service_game.md) (6 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (6 shared connections)
- [world models rationale](world_models_rationale.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [dialogue definitions admin](dialogue_definitions_admin.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)

## Source Files

- `server/models/dialogue.py`
- `server/persistence/repositories/dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 118 (89%)
- INFERRED: 15 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*