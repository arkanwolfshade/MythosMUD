# LootAllRequest

> 119 nodes

## Key Concepts

- **LootAllRequest** (58 connections) — `server/api/container_models.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (32 connections) — `server/api/container_endpoints_loot.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **test_container_endpoints_loot.py** (13 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **test_container_endpoints_loot_register.py** (12 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **TestGetContainerAndPlayerForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **_build_container_data_from_dict()** (10 connections) — `server/api/container_endpoints_basic.py`
- **containers/container.py** (10 connections) — `server/schemas/containers/container.py`
- **ContainerOpenResponse** (9 connections) — `server/schemas/containers/container.py`
- **ContainerData** (9 connections) — `server/schemas/containers/container_data.py`
- **_convert_inventory_list_to_inventory_stacks()** (9 connections) — `server/api/container_endpoints_basic.py`
- **containers/__init__.py** (9 connections) — `server/schemas/containers/__init__.py`
- **asyncio** (9 connections)
- **_build_transfer_response()** (8 connections) — `server/api/container_endpoints_basic.py`
- **containers/container_data.py** (8 connections) — `server/schemas/containers/container_data.py`
- **ContainerCloseResponse** (7 connections) — `server/schemas/containers/container.py`
- **InventoryStack** (7 connections) — `server/schemas/containers/container_data.py`
- **.test_loot_all_items_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_container_not_found()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_locked_error()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- *... and 94 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (58 shared connections)
- [transfer_all_items_from_container](transfer_all_items_from_container.md) (18 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (13 shared connections)
- [ContainerComponent](ContainerComponent.md) (11 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (9 shared connections)
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) (8 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (6 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (5 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (4 shared connections)
- [server/models/game.py](server-models-game.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_models.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 322 (92%)
- INFERRED: 29 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*