# ContainerComponent

> 222 nodes

## Key Concepts

- **ContainerComponent** (100 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **ContainerService** (79 connections) — `server/services/container_service.py`
- **test_container_service.py** (60 connections) — `server/tests/unit/services/test_container_service.py`
- **ContainerLockState** (42 connections) — `server/models/container.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **models/container.py** (33 connections) — `server/models/container.py`
- **asyncio** (18 connections)
- **_container()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (15 connections) — `server/services/inventory_mutation_guard.py`
- **api/conftest.py** (14 connections) — `server/tests/unit/api/conftest.py`
- **_stack()** (12 connections) — `server/tests/unit/services/test_container_service.py`
- **fixture** (7 connections)
- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **.create_corpse()** (5 connections) — `server/models/container.py`
- **.validate_entity_id()** (5 connections) — `server/models/container.py`
- **.validate_lock_state()** (5 connections) — `server/models/container.py`
- **.validate_source_type()** (5 connections) — `server/models/container.py`
- **test_container_component_default_lock_state()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots_full()** (5 connections) — `server/tests/unit/models/test_container.py`
- *... and 197 more nodes in this community*

## Relationships

- [LootAllRequest](LootAllRequest.md) (32 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (31 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (27 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (20 shared connections)
- [ConnectionManager](ConnectionManager.md) (19 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (13 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (4 shared connections)
- [WearableContainerService](WearableContainerService.md) (3 shared connections)
- [EnvironmentalContainerLoader](EnvironmentalContainerLoader.md) (3 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (3 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 412 (64%)
- INFERRED: 227 (36%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*