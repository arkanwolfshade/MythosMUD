# LootAllRequest

> 160 nodes

## Key Concepts

- **LootAllRequest** (58 connections) — `server/api/container_models.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **models/container.py** (34 connections) — `server/models/container.py`
- **container_endpoints_loot.py** (32 connections) — `server/api/container_endpoints_loot.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **test_container_events_loot.py** (17 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **asyncio** (14 connections)
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **test_container_endpoints_loot.py** (13 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **test_container_endpoints_loot_register.py** (12 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **TestGetContainerAndPlayerForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **containers/container.py** (10 connections) — `server/schemas/containers/container.py`
- **ContainerOpenResponse** (9 connections) — `server/schemas/containers/container.py`
- **ContainerData** (9 connections) — `server/schemas/containers/container_data.py`
- **containers/__init__.py** (9 connections) — `server/schemas/containers/__init__.py`
- **asyncio** (9 connections)
- **.test_emit_loot_all_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events_loot.py`
- *... and 135 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (67 shared connections)
- [ContainerComponent](ContainerComponent.md) (33 shared connections)
- [ContainerService](ContainerService.md) (14 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (13 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (12 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (5 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (3 shared connections)
- [ContainerFactoryOptions](ContainerFactoryOptions.md) (3 shared connections)
- [BaseCommand](BaseCommand.md) (3 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 465 (92%)
- INFERRED: 40 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*