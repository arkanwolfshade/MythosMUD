# ContainerComponent

> 218 nodes

## Key Concepts

- **ContainerComponent** (100 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **ContainerService** (79 connections) — `server/services/container_service.py`
- **test_container_service.py** (61 connections) — `server/tests/unit/services/test_container_service.py`
- **ContainerLockState** (42 connections) — `server/models/container.py`
- **test_container.py** (40 connections) — `server/tests/unit/models/test_container.py`
- **models/container.py** (34 connections) — `server/models/container.py`
- **container_service_session.py** (28 connections) — `server/services/container_service_session.py`
- **container_service_lock.py** (26 connections) — `server/services/container_service_lock.py`
- **ContainerAccessMixin** (19 connections) — `server/services/container_service_access.py`
- **asyncio** (18 connections)
- **container_service_access.py** (17 connections) — `server/services/container_service_access.py`
- **_container()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (15 connections) — `server/services/inventory_mutation_guard.py`
- **_stack()** (12 connections) — `server/tests/unit/services/test_container_service.py`
- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **.create_corpse()** (5 connections) — `server/models/container.py`
- **.validate_entity_id()** (5 connections) — `server/models/container.py`
- **.validate_lock_state()** (5 connections) — `server/models/container.py`
- **.validate_source_type()** (5 connections) — `server/models/container.py`
- **test_container_component_default_lock_state()** (5 connections) — `server/tests/unit/models/test_container.py`
- *... and 193 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (56 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (31 shared connections)
- [container_service_transfer_to.py](container_service_transfer_to.py.md) (24 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (20 shared connections)
- [container_events.py](container_events.py.md) (19 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [._validate_container_access](_validate_container_access.md) (8 shared connections)
- [pytest.md](pytest.md.md) (8 shared connections)
- [EnvironmentalContainerLoader](EnvironmentalContainerLoader.md) (7 shared connections)
- [log_and_raise](log_and_raise.md) (7 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (6 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (6 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/container_service.py`
- `server/services/container_service_access.py`
- `server/services/container_service_lock.py`
- `server/services/container_service_session.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`

## Audit Trail

- EXTRACTED: 468 (67%)
- INFERRED: 228 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*