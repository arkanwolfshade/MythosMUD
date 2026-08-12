# LootAllRequest

> 119 nodes

## Key Concepts

- **LootAllRequest** (63 connections) — `server/api/container_models.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (30 connections) — `server/api/container_endpoints_loot.py`
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **models/container.py** (26 connections) — `server/models/container.py`
- **TestLootAllItems** (19 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **test_container_endpoints_loot.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestGetContainerAndPlayerForLootAll** (14 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **environmental_container_loader.py** (13 connections) — `server/services/environmental_container_loader.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **ContainerLockState** (10 connections) — `server/models/container.py`
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerData** (10 connections) — `server/schemas/containers/container_data.py`
- **InventoryStack** (10 connections) — `server/schemas/containers/container_data.py`
- **_convert_inventory_list_to_inventory_stacks()** (10 connections) — `server/api/container_endpoints_basic.py`
- **test_container_endpoints_loot_register.py** (10 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **ContainerCloseResponse** (9 connections) — `server/schemas/containers/container.py`
- **ContainerOpenResponse** (9 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (9 connections) — `server/schemas/containers/container.py`
- **containers/container.py** (9 connections) — `server/schemas/containers/container.py`
- **asyncio** (9 connections)
- **TestEmitContainerOpenedEventsEdgeCases** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEventDirections** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **_build_container_data_from_dict()** (7 connections) — `server/api/container_endpoints_basic.py`
- *... and 94 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (59 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (39 shared connections)
- [asyncio](asyncio.md) (32 shared connections)
- [ContainerComponent](ContainerComponent.md) (18 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (8 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (6 shared connections)
- [server/models/game.py](server-models-game.py.md) (5 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [WearableContainerService](WearableContainerService.md) (2 shared connections)
- [User](User.md) (2 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/models/game.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 576 (89%)
- INFERRED: 68 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*