# task registry app

> 249 nodes

## Key Concepts

- **ContainerComponent** (106 connections) — `server/models/container.py`
- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerLockState** (15 connections) — `server/models/container.py`
- **conftest.py** (14 connections) — `server/tests/unit/api/conftest.py`
- **CorpseServiceError** (13 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (10 connections) — `server/services/corpse_lifecycle_service.py`
- **Any** (8 connections)
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse()** (7 connections) — `server/models/container.py`
- **CorpseNotFoundError** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_environment()** (6 connections) — `server/models/container.py`
- **.create_equipment()** (6 connections) — `server/models/container.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (5 connections)
- **ContainerComponent** (5 connections)
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.validate_source_type()** (4 connections) — `server/models/container.py`
- **.validate_lock_state()** (4 connections) — `server/models/container.py`
- **.validate_entity_id()** (4 connections) — `server/models/container.py`
- **.would_exceed_capacity()** (4 connections) — `server/models/container.py`
- **UUID** (4 connections)
- *... and 224 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (43 shared connections)
- [models npc rationale](models_npc_rationale.md) (13 shared connections)
- [auth rationale access](auth_rationale_access.md) (10 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [player requests schemas](player_requests_schemas.md) (3 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [alias storage commands](alias_storage_commands.md) (1 shared connections)
- [services npc startup](services_npc_startup.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 721 (93%)
- INFERRED: 51 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*