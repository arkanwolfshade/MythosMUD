# ContainerService

> 201 nodes

## Key Concepts

- **ContainerService** (99 connections) — `server/services/container_service.py`
- **test_container_service.py** (60 connections) — `server/tests/unit/services/test_container_service.py`
- **ContainerServiceError** (51 connections) — `server/services/container_service_helpers.py`
- **models/container.py** (33 connections) — `server/models/container.py`
- **container_service.py** (33 connections) — `server/services/container_service.py`
- **container_service_transfer_to.py** (33 connections) — `server/services/container_service_transfer_to.py`
- **container_service_session.py** (28 connections) — `server/services/container_service_session.py`
- **container_service_lock.py** (26 connections) — `server/services/container_service_lock.py`
- **container_service_transfer_from.py** (26 connections) — `server/services/container_service_transfer_from.py`
- **container_service_helpers.py** (23 connections) — `server/services/container_service_helpers.py`
- **ContainerNotFoundError** (22 connections) — `server/services/container_service_helpers.py`
- **ContainerAccessMixin** (19 connections) — `server/services/container_service_access.py`
- **ContainerSessionMixin** (18 connections) — `server/services/container_service_session.py`
- **ContainerTransferFromMixin** (18 connections) — `server/services/container_service_transfer_from.py`
- **asyncio** (18 connections)
- **ContainerCapacityError** (17 connections) — `server/services/container_service_helpers.py`
- **container_service_access.py** (17 connections) — `server/services/container_service_access.py`
- **ContainerAccessDeniedError** (16 connections) — `server/services/container_service_helpers.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **_container()** (15 connections) — `server/tests/unit/services/test_container_service.py`
- **ContainerLockState** (14 connections) — `server/models/container.py`
- **ContainerLockedError** (14 connections) — `server/services/container_service_helpers.py`
- **ContainerLockMixin** (14 connections) — `server/services/container_service_lock.py`
- **filter_container_data()** (14 connections) — `server/services/container_service_helpers.py`
- **api/conftest.py** (14 connections) — `server/tests/unit/api/conftest.py`
- *... and 176 more nodes in this community*

## Relationships

- [LootAllRequest](LootAllRequest.md) (62 shared connections)
- [get_logger](get_logger.md) (58 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (38 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (17 shared connections)
- [ContainerComponent](ContainerComponent.md) (15 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (14 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (13 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (13 shared connections)
- [Player](Player.md) (10 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (4 shared connections)
- [container_events.py](container_events.py.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/container_service.py`
- `server/services/container_service_access.py`
- `server/services/container_service_helpers.py`
- `server/services/container_service_lock.py`
- `server/services/container_service_session.py`
- `server/services/container_service_transfer_from.py`
- `server/services/container_service_transfer_to.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 629 (84%)
- INFERRED: 118 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*