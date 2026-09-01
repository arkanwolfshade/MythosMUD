# container_endpoints_basic.py

> 210 nodes

## Key Concepts

- **container_endpoints_basic.py** (64 connections) — `server/api/container_endpoints_basic.py`
- **RateLimitError** (44 connections) — `server/exceptions.py`
- **test_container_helpers.py** (44 connections) — `server/tests/unit/api/test_container_helpers.py`
- **api/container_helpers.py** (43 connections) — `server/api/container_helpers.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (32 connections) — `server/api/container_endpoints_loot.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **test_container_endpoints_loot.py** (13 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **get_current_user()** (11 connections) — `docs/examples/logging/fastapi_integration.py`
- **execute_transfer()** (11 connections) — `server/api/container_helpers.py`
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
- *... and 185 more nodes in this community*

## Relationships

- [test_containers.py](test_containers.py.md) (49 shared connections)
- [LootAllRequest](LootAllRequest.md) (39 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (29 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (26 shared connections)
- [User](User.md) (24 shared connections)
- [ContainerService](ContainerService.md) (12 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (11 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (9 shared connections)
- [MythosMUDError](MythosMUDError.md) (8 shared connections)
- [ContainerComponent](ContainerComponent.md) (8 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (5 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/exceptions.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 599 (93%)
- INFERRED: 45 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*