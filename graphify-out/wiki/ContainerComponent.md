# ContainerComponent

> 209 nodes

## Key Concepts

- **ContainerComponent** (100 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **ContainerService** (79 connections) — `server/services/container_service.py`
- **test_container_service.py** (61 connections) — `server/tests/unit/services/test_container_service.py`
- **ContainerLockState** (42 connections) — `server/models/container.py`
- **test_container.py** (40 connections) — `server/tests/unit/models/test_container.py`
- **EnvironmentalContainerLoader** (18 connections) — `server/services/environmental_container_loader.py`
- **asyncio** (18 connections)
- **test_environmental_container_loader.py** (17 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **_container()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (15 connections) — `server/services/inventory_mutation_guard.py`
- **environmental_container_loader.py** (14 connections) — `server/services/environmental_container_loader.py`
- **_stack()** (12 connections) — `server/tests/unit/services/test_container_service.py`
- **test_container_endpoints_loot_register.py** (12 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **.validate_entity_id()** (5 connections) — `server/models/container.py`
- **.validate_lock_state()** (5 connections) — `server/models/container.py`
- **.validate_source_type()** (5 connections) — `server/models/container.py`
- **test_container_component_default_lock_state()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots_full()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_used_slots()** (5 connections) — `server/tests/unit/models/test_container.py`
- *... and 184 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (29 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (29 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (26 shared connections)
- [models/container.py](models-container.py.md) (24 shared connections)
- [transfer_all_items_from_container](transfer_all_items_from_container.md) (16 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (8 shared connections)
- [ValidationError](ValidationError.md) (8 shared connections)
- [.load_container_from_room_json](load_container_from_room_json.md) (7 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (5 shared connections)
- [ContainerFactoryOptions](ContainerFactoryOptions.md) (5 shared connections)
- [api/conftest.py](api-conftest.py.md) (4 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/container_service.py`
- `server/services/environmental_container_loader.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`
- `server/tests/unit/services/test_environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 449 (71%)
- INFERRED: 183 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*