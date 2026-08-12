# container_endpoints_basic.py

> 70 nodes

## Key Concepts

- **container_endpoints_basic.py** (49 connections) — `server/api/container_endpoints_basic.py`
- **container_endpoints_loot.py** (30 connections) — `server/api/container_endpoints_loot.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerData** (10 connections) — `server/schemas/containers/container_data.py`
- **InventoryStack** (10 connections) — `server/schemas/containers/container_data.py`
- **_convert_inventory_list_to_inventory_stacks()** (10 connections) — `server/api/container_endpoints_basic.py`
- **ContainerCloseResponse** (9 connections) — `server/schemas/containers/container.py`
- **ContainerOpenResponse** (9 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (9 connections) — `server/schemas/containers/container.py`
- **containers/container.py** (9 connections) — `server/schemas/containers/container.py`
- **_build_container_data_from_dict()** (7 connections) — `server/api/container_endpoints_basic.py`
- **containers/container_data.py** (7 connections) — `server/schemas/containers/container_data.py`
- **containers/__init__.py** (7 connections) — `server/schemas/containers/__init__.py`
- **register_basic_endpoints()** (6 connections) — `server/api/container_endpoints_basic.py`
- **_build_loot_all_response()** (6 connections) — `server/api/container_endpoints_loot.py`
- **Any** (6 connections)
- **register_loot_endpoints()** (5 connections) — `server/api/container_endpoints_loot.py`
- **Any** (5 connections)
- **_convert_datetime_to_iso()** (4 connections) — `server/api/container_endpoints_basic.py`
- *... and 45 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (40 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (32 shared connections)
- [ContainerComponent](ContainerComponent.md) (28 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (7 shared connections)
- [User](User.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [server/models/game.py](server-models-game.py.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [ContainerService](ContainerService.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 373 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*