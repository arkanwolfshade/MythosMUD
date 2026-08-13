# ContainerServiceError

> 352 nodes

## Key Concepts

- **ContainerServiceError** (81 connections) — `server/services/container_service.py`
- **RateLimitError** (67 connections) — `server/exceptions.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (49 connections) — `server/api/container_endpoints_basic.py`
- **api/container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **ErrorMessages** (41 connections) — `server/error_types.py`
- **ContainerCapacityError** (41 connections) — `server/services/container_service.py`
- **ContainerNotFoundError** (39 connections) — `server/services/container_service.py`
- **ContainerLockedError** (35 connections) — `server/services/container_service.py`
- **ContainerAccessDeniedError** (31 connections) — `server/services/container_service.py`
- **test_container_exception_handlers.py** (31 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (31 connections) — `server/tests/unit/api/test_containers.py`
- **handle_transfer_items_exceptions()** (28 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (26 connections) — `server/api/container_exception_handlers.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **handle_open_container_exceptions()** (23 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **TestHelperFunctions** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestOpenContainer** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestTransferItems** (20 connections) — `server/tests/unit/api/test_containers.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- *... and 327 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (78 shared connections)
- [get_logger](get_logger.md) (73 shared connections)
- [User](User.md) (54 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (47 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (37 shared connections)
- [ContainerService](ContainerService.md) (29 shared connections)
- [_convert_container_dict_to_container_data](_convert_container_dict_to_container_data.md) (20 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (7 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [fixture](fixture.md) (4 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/schemas/containers/container.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 908 (75%)
- INFERRED: 308 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*