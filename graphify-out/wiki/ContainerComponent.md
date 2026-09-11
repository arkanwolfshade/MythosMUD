# ContainerComponent

> 564 nodes

## Key Concepts

- **ContainerComponent** (147 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **ContainerServiceError** (49 connections) — `server/services/container_service_helpers.py`
- **ContainerLockState** (44 connections) — `server/models/container.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **InventoryStack** (37 connections) — `server/services/inventory_service.py`
- **models/container.py** (33 connections) — `server/models/container.py`
- **container_service.py** (33 connections) — `server/services/container_service.py`
- **container_service_transfer_to.py** (33 connections) — `server/services/container_service_transfer_to.py`
- **handle_transfer_items_exceptions()** (28 connections) — `server/api/container_exception_handlers.py`
- **container_service_session.py** (28 connections) — `server/services/container_service_session.py`
- **container_service_lock.py** (26 connections) — `server/services/container_service_lock.py`
- **container_service_transfer_from.py** (26 connections) — `server/services/container_service_transfer_from.py`
- **test_container_exception_handlers.py** (26 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **CorpseLifecycleService** (24 connections) — `server/services/corpse_lifecycle_service.py`
- **handle_open_container_exceptions()** (23 connections) — `server/api/container_exception_handlers.py`
- **container_service_helpers.py** (23 connections) — `server/services/container_service_helpers.py`
- **asyncio** (23 connections)
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (21 connections) — `server/api/container_exception_handlers.py`
- **ContainerNotFoundError** (20 connections) — `server/services/container_service_helpers.py`
- **ContainerTransferToMixin** (20 connections) — `server/services/container_service_transfer_to.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **ContainerAccessMixin** (19 connections) — `server/services/container_service_access.py`
- *... and 539 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (93 shared connections)
- [get_logger](get_logger.md) (91 shared connections)
- [ContainerService](ContainerService.md) (31 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (30 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (15 shared connections)
- [Player](Player.md) (12 shared connections)
- [User](User.md) (12 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (7 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [RoomService](RoomService.md) (4 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (3 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (3 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/models/container.py`
- `server/services/container_service.py`
- `server/services/container_service_access.py`
- `server/services/container_service_helpers.py`
- `server/services/container_service_lock.py`
- `server/services/container_service_session.py`
- `server/services/container_service_transfer_from.py`
- `server/services/container_service_transfer_to.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/environmental_container_loader.py`
- `server/services/inventory_service.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`
- `server/tests/unit/services/test_environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 1245 (84%)
- INFERRED: 238 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*