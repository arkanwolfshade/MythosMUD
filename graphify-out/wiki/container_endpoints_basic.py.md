# container_endpoints_basic.py

> 65 nodes · cohesion 0.06

## Key Concepts

- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **TestOpenContainer** (20 connections) — `server/tests/unit/api/test_containers.py`
- **OpenContainerRequest** (17 connections) — `server/api/container_models.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **_convert_inventory_list_to_inventory_stacks()** (11 connections) — `server/api/container_endpoints_basic.py`
- **register_basic_endpoints()** (10 connections) — `server/api/container_endpoints_basic.py`
- **ContainerCloseResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerOpenResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerData** (10 connections) — `server/schemas/containers/container_data.py`
- **InventoryStack** (10 connections) — `server/schemas/containers/container_data.py`
- **containers.py** (9 connections) — `server/api/containers.py`
- **container.py** (9 connections) — `server/schemas/containers/container.py`
- **register_loot_endpoints()** (8 connections) — `server/api/container_endpoints_loot.py`
- **_build_container_data_from_dict()** (7 connections) — `server/api/container_endpoints_basic.py`
- **container_data.py** (7 connections) — `server/schemas/containers/container_data.py`
- **__init__.py** (7 connections) — `server/schemas/containers/__init__.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **.test_open_container_access_denied()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_locked()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_not_found()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_open_container_rate_limit()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **Any** (5 connections)
- *... and 40 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (30 shared connections)
- [ContainerService](ContainerService.md) (25 shared connections)
- [ContainerComponent](ContainerComponent.md) (18 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [User](User.md) (5 shared connections)
- [__init__.py](__init__.py.md) (5 shared connections)
- [game.py](game.py.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [exceptions.py](exceptions.py.md) (2 shared connections)
- [MythosMUDError](MythosMUDError.md) (2 shared connections)
- [dependencies.py](dependencies.py.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 295 (85%)
- INFERRED: 53 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*