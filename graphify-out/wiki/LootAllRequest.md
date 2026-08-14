# LootAllRequest

> 237 nodes

## Key Concepts

- **LootAllRequest** (58 connections) — `server/api/container_models.py`
- **TransferContainerRequest** (56 connections) — `server/api/container_models.py`
- **api/container_helpers.py** (42 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (42 connections) — `server/tests/unit/api/test_container_helpers.py`
- **ErrorMessages** (41 connections) — `server/error_types.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **ContainerSourceType** (30 connections) — `server/models/container.py`
- **container_endpoints_loot.py** (30 connections) — `server/api/container_endpoints_loot.py`
- **test_container_helpers_loot.py** (22 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (18 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **test_container_events_loot.py** (16 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **asyncio** (14 connections)
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **TestHandleContainerServiceErrorEdgeCases** (13 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **container_models.py** (13 connections) — `server/api/container_models.py`
- **TestGetContainerAndPlayerForLootAll** (12 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestHandleContainerServiceError** (12 connections) — `server/tests/unit/api/test_container_helpers.py`
- **test_container_endpoints_loot.py** (12 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestCreateErrorContext** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- *... and 212 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (73 shared connections)
- [ContainerService](ContainerService.md) (62 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (36 shared connections)
- [container_events.py](container_events.py.md) (30 shared connections)
- [MythosMUDError](MythosMUDError.md) (24 shared connections)
- [User](User.md) (24 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [ContainerComponent](ContainerComponent.md) (14 shared connections)
- [ConnectionManager](ConnectionManager.md) (10 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (10 shared connections)
- [ErrorType](ErrorType.md) (7 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (2 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/error_types.py`
- `server/models/container.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 653 (82%)
- INFERRED: 143 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*