# ContainerComponent

> 319 nodes

## Key Concepts

- **ContainerComponent** (90 connections) — `server/models/container.py`
- **LootAllRequest** (63 connections) — `server/api/container_models.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (30 connections) — `server/api/container_endpoints_loot.py`
- **asyncio** (28 connections)
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **models/container.py** (26 connections) — `server/models/container.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **TestTransferAllItemsFromContainer** (20 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestLootAllItems** (19 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **test_container_endpoints_loot.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestGetContainerAndPlayerForLootAll** (14 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **asyncio** (14 connections)
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 294 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (78 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (18 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (14 shared connections)
- [ContainerService](ContainerService.md) (14 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (10 shared connections)
- [_convert_container_dict_to_container_data](_convert_container_dict_to_container_data.md) (9 shared connections)
- [User](User.md) (5 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [api/conftest.py](api-conftest.py.md) (2 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/schemas/containers/container.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/models/test_container.py`

## Audit Trail

- EXTRACTED: 746 (93%)
- INFERRED: 57 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*