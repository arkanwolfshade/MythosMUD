# LootAllRequest

> 199 nodes

## Key Concepts

- **LootAllRequest** (58 connections) — `server/api/container_models.py`
- **test_container_helpers.py** (44 connections) — `server/tests/unit/api/test_container_helpers.py`
- **api/container_helpers.py** (43 connections) — `server/api/container_helpers.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (32 connections) — `server/api/container_endpoints_loot.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **test_container_endpoints_loot.py** (13 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **test_container_endpoints_loot_register.py** (12 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **execute_transfer()** (11 connections) — `server/api/container_helpers.py`
- **Request** (11 connections)
- **TestGetContainerAndPlayerForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **apply_rate_limiting_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- *... and 174 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (63 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (41 shared connections)
- [ContainerService](ContainerService.md) (35 shared connections)
- [ContainerComponent](ContainerComponent.md) (20 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (20 shared connections)
- [ConnectionManager](ConnectionManager.md) (17 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (17 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (9 shared connections)
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) (8 shared connections)
- [TestExecuteTransfer](TestExecuteTransfer.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 549 (91%)
- INFERRED: 54 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*