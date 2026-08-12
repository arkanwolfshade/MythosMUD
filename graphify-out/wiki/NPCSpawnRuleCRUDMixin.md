# NPCSpawnRuleCRUDMixin

> 19 nodes

## Key Concepts

- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.get_spawn_rule()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.get_spawn_rules()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **AsyncSession** (6 connections)
- **.delete_spawn_rule()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._validate_spawn_rule_inputs()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Any** (2 connections)
- **Any** (2 connections)
- **Map procedure result row to NPCSpawnRule model.** (1 connections) — `server/services/npc_service_models.py`
- **Validate NPC definition existence and population counts for spawn rule creation.** (1 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Execute create_spawn_rule stored procedure and return the created spawn rule.** (1 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Delete an NPC spawn rule.** (1 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Mixin providing NPC spawn rule CRUD operations.** (1 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Get all NPC spawn rules.** (1 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Get a specific NPC spawn rule by ID.** (1 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Create a new NPC spawn rule.** (1 connections) — `server/services/npc_service/spawn_rule_crud.py`

## Relationships

- [EventBus](EventBus.md) (6 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (1 shared connections)

## Source Files

- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 70 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*