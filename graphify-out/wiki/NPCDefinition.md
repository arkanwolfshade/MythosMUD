# NPCDefinition

> 97 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **definition_crud.py** (16 connections) — `server/services/npc_service/definition_crud.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **queries.py** (12 connections) — `server/services/npc_service/queries.py`
- **spawn_rule_crud.py** (12 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCDefinitionType** (11 connections) — `server/models/npc.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **NPCQueryMixin** (7 connections) — `server/services/npc_service/queries.py`
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **CreateNPCDefinitionInput** (6 connections) — `server/services/npc_service_models.py`
- **NPCDefinitionCreateParams** (6 connections) — `server/services/npc_service_models.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._queue_npc_thread_start()** (5 connections) — `server/npc/lifecycle_manager.py`
- *... and 72 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (23 shared connections)
- [test_npc_models.py](test_npc_models.py.md) (18 shared connections)
- [NPCBase](NPCBase.md) (17 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (16 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (11 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (11 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (9 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (8 shared connections)
- [NPCLifecycleRecord](NPCLifecycleRecord.md) (8 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 346 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*