# container_endpoints_basic.py

> 141 nodes

## Key Concepts

- **container_endpoints_basic.py** (64 connections) — `server/api/container_endpoints_basic.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **Request** (11 connections)
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **TestHelperFunctions** (10 connections) — `server/tests/unit/api/test_containers.py`
- **_build_container_data_from_dict()** (10 connections) — `server/api/container_endpoints_basic.py`
- **apply_rate_limiting_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- **containers/container.py** (10 connections) — `server/schemas/containers/container.py`
- **ContainerOpenResponse** (9 connections) — `server/schemas/containers/container.py`
- **ContainerData** (9 connections) — `server/schemas/containers/container_data.py`
- **get_current_user()** (9 connections) — `docs/examples/logging/fastapi_integration.py`
- **_convert_inventory_list_to_inventory_stacks()** (9 connections) — `server/api/container_endpoints_basic.py`
- **containers/__init__.py** (9 connections) — `server/schemas/containers/__init__.py`
- *... and 116 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (71 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (21 shared connections)
- [User](User.md) (15 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (13 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (11 shared connections)
- [PlayerService](PlayerService.md) (8 shared connections)
- [loot_all_items](loot_all_items.md) (6 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [LootAllRequest](LootAllRequest.md) (3 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (2 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/models/game.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 381 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*