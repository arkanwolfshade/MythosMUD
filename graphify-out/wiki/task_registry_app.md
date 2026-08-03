# task registry app

> 214 nodes

## Key Concepts

- **ContainerComponent** (106 connections) — `server/models/container.py`
- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **ContainerLockState** (15 connections) — `server/models/container.py`
- **conftest.py** (14 connections) — `server/tests/unit/api/conftest.py`
- **CorpseServiceError** (13 connections) — `server/services/corpse_lifecycle_service.py`
- **Any** (8 connections)
- **.create_corpse()** (7 connections) — `server/models/container.py`
- **CorpseNotFoundError** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_environment()** (6 connections) — `server/models/container.py`
- **.create_equipment()** (6 connections) — `server/models/container.py`
- **UUID** (5 connections)
- **.validate_source_type()** (4 connections) — `server/models/container.py`
- **.validate_lock_state()** (4 connections) — `server/models/container.py`
- **.validate_entity_id()** (4 connections) — `server/models/container.py`
- **.would_exceed_capacity()** (4 connections) — `server/models/container.py`
- **test_container_component_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_capacity_slots_validation_min()** (4 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_capacity_slots_validation_max()** (4 connections) — `server/tests/unit/models/test_container.py`
- **test_corpse_not_found_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **.validate_metadata_no_personal_data()** (3 connections) — `server/models/container.py`
- **.validate_room_id()** (3 connections) — `server/models/container.py`
- **.has_room_for()** (3 connections) — `server/models/container.py`
- **.is_decayed()** (3 connections) — `server/models/container.py`
- **datetime** (3 connections)
- *... and 189 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (37 shared connections)
- [rate limiter services](rate_limiter_services.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (8 shared connections)
- [container events rationale](container_events_rationale.md) (8 shared connections)
- [alias storage commands](alias_storage_commands.md) (4 shared connections)
- [command inventory models](command_inventory_models.md) (3 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (2 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (2 shared connections)
- [services npc startup](services_npc_startup.md) (1 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [admin auth service](admin_auth_service.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 604 (93%)
- INFERRED: 48 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*