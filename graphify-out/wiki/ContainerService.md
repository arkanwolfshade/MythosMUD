# ContainerService

> 185 nodes · cohesion 0.02

## Key Concepts

- **ContainerService** (78 connections) — `server/services/container_service.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **TestHelperFunctions** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestTransferItems** (20 connections) — `server/tests/unit/api/test_containers.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **.transfer_from_container()** (18 connections) — `server/services/container_service.py`
- **UUID** (17 connections)
- **TestCloseContainer** (17 connections) — `server/tests/unit/api/test_containers.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **TestRequestModels** (16 connections) — `server/tests/unit/api/test_containers.py`
- **.open_container()** (15 connections) — `server/services/container_service.py`
- **CloseContainerRequest** (14 connections) — `server/api/container_models.py`
- **.transfer_to_container()** (13 connections) — `server/services/container_service.py`
- **Any** (13 connections)
- **TestHandleContainerServiceError** (13 connections) — `server/tests/unit/api/test_container_helpers.py`
- **execute_transfer()** (12 connections) — `server/api/container_helpers.py`
- **.lock_container()** (12 connections) — `server/services/container_service.py`
- **.unlock_container()** (12 connections) — `server/services/container_service.py`
- **TestCreateErrorContext** (12 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.loot_all()** (11 connections) — `server/services/container_service.py`
- **._validate_container_access()** (11 connections) — `server/services/container_service.py`
- **TestApplyRateLimitingForCloseContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- *... and 160 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (160 shared connections)
- [MythosMUDError](MythosMUDError.md) (35 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (25 shared connections)
- [ContainerComponent](ContainerComponent.md) (25 shared connections)
- [User](User.md) (25 shared connections)
- [DatabaseError](DatabaseError.md) (13 shared connections)
- [transfer_all_items_from_container](transfer_all_items_from_container.md) (12 shared connections)
- [__init__.py](__init__.py.md) (6 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [UserManager](UserManager.md) (4 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (3 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (3 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 748 (75%)
- INFERRED: 251 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*