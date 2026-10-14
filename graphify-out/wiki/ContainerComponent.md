# ContainerComponent

> 562 nodes

## Key Concepts

- **ContainerComponent** (169 connections) — `server/models/container.py`
- **ContainerSourceType** (95 connections) — `server/models/container.py`
- **test_corpse_lifecycle_service.py** (61 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **ContainerServiceError** (49 connections) — `server/services/container_service_helpers.py`
- **ContainerLockState** (42 connections) — `server/models/container.py`
- **test_container.py** (41 connections) — `server/tests/unit/models/test_container.py`
- **InventoryStack** (38 connections) — `server/services/inventory_service.py`
- **container_service.py** (38 connections) — `server/services/container_service.py`
- **container_service_transfer_to.py** (34 connections) — `server/services/container_service_transfer_to.py`
- **models/container.py** (33 connections) — `server/models/container.py`
- **container_service_session.py** (30 connections) — `server/services/container_service_session.py`
- **handle_transfer_items_exceptions()** (29 connections) — `server/api/container_exception_handlers.py`
- **container_service_transfer_from.py** (28 connections) — `server/services/container_service_transfer_from.py`
- **test_container_exception_handlers.py** (27 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **container_service_lock.py** (26 connections) — `server/services/container_service_lock.py`
- **handle_open_container_exceptions()** (24 connections) — `server/api/container_exception_handlers.py`
- **container_service_helpers.py** (24 connections) — `server/services/container_service_helpers.py`
- **ContainerTransferFromMixin** (22 connections) — `server/services/container_service_transfer_from.py`
- **container_exception_handlers.py** (22 connections) — `server/api/container_exception_handlers.py`
- **ContainerSessionMixin** (21 connections) — `server/services/container_service_session.py`
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **ContainerAccessMixin** (20 connections) — `server/services/container_service_access.py`
- **ContainerNotFoundError** (20 connections) — `server/services/container_service_helpers.py`
- **ContainerTransferToMixin** (20 connections) — `server/services/container_service_transfer_to.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- *... and 537 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (86 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (53 shared connections)
- [LootAllRequest](LootAllRequest.md) (46 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (42 shared connections)
- [ContainerService](ContainerService.md) (29 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (27 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (24 shared connections)
- [alias_storage.py](alias_storage.py.md) (15 shared connections)
- [test_corpse_lifecycle_decay.py](test_corpse_lifecycle_decay.py.md) (12 shared connections)
- [InventoryService](InventoryService.md) (10 shared connections)
- [ValueError](ValueError.md) (10 shared connections)
- [ValidationError](ValidationError.md) (7 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/models/container.py`
- `server/services/container_service.py`
- `server/services/container_service_access.py`
- `server/services/container_service_helpers.py`
- `server/services/container_service_lock.py`
- `server/services/container_service_session.py`
- `server/services/container_service_transfer_from.py`
- `server/services/container_service_transfer_to.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/inventory_service.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_endpoints_basic_weapon.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 1303 (82%)
- INFERRED: 279 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*