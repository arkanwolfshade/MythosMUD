# container_endpoints_basic.py

> 436 nodes

## Key Concepts

- **container_endpoints_basic.py** (64 connections) — `server/api/container_endpoints_basic.py`
- **LootAllRequest** (58 connections) — `server/api/container_models.py`
- **ContainerServiceError** (49 connections) — `server/services/container_service_helpers.py`
- **test_container_helpers.py** (44 connections) — `server/tests/unit/api/test_container_helpers.py`
- **api/container_helpers.py** (43 connections) — `server/api/container_helpers.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_service.py** (33 connections) — `server/services/container_service.py`
- **container_endpoints_loot.py** (32 connections) — `server/api/container_endpoints_loot.py`
- **handle_transfer_items_exceptions()** (28 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (28 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **handle_open_container_exceptions()** (23 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (22 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **ContainerNotFoundError** (20 connections) — `server/services/container_service_helpers.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **ContainerCapacityError** (15 connections) — `server/services/container_service_helpers.py`
- **ContainerAccessDeniedError** (14 connections) — `server/services/container_service_helpers.py`
- *... and 411 more nodes in this community*

## Relationships

- [TransferContainerRequest](TransferContainerRequest.md) (56 shared connections)
- [ContainerComponent](ContainerComponent.md) (56 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (52 shared connections)
- [User](User.md) (42 shared connections)
- [container_service_transfer_to.py](container_service_transfer_to.py.md) (27 shared connections)
- [DatabaseError](DatabaseError.md) (23 shared connections)
- [container_events.py](container_events.py.md) (13 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) (8 shared connections)
- [pytest.md](pytest.md.md) (7 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (5 shared connections)
- [ErrorType](ErrorType.md) (5 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/services/container_service.py`
- `server/services/container_service_helpers.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 1036 (89%)
- INFERRED: 134 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*