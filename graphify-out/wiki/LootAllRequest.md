# LootAllRequest

> 120 nodes

## Key Concepts

- **LootAllRequest** (58 connections) — `server/api/container_models.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (31 connections) — `server/api/container_endpoints_loot.py`
- **test_container_helpers_loot.py** (22 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **asyncio** (14 connections)
- **test_container_endpoints_loot.py** (12 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestGetContainerAndPlayerForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **apply_rate_limiting_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **test_container_endpoints_loot_register.py** (10 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **asyncio** (9 connections)
- **.test_loot_all_items_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_container_not_found()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_locked_error()** (7 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_transfer_all_items_from_container_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **asyncio** (7 connections)
- **TestApplyRateLimitingForLootAll** (6 connections) — `server/tests/unit/api/test_container_helpers.py`
- **_build_loot_all_response()** (6 connections) — `server/api/container_endpoints_loot.py`
- **register_loot_endpoints()** (6 connections) — `server/api/container_endpoints_loot.py`
- **.test_loot_all_items_emit_event_failure()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- *... and 95 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (36 shared connections)
- [ContainerComponent](ContainerComponent.md) (32 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (19 shared connections)
- [ConnectionManager](ConnectionManager.md) (14 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (7 shared connections)
- [User](User.md) (6 shared connections)
- [MythosMUDError](MythosMUDError.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [models/user.py](models-user.py.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 333 (91%)
- INFERRED: 32 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*