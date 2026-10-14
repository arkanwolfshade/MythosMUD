# container_endpoints_basic.py

> 340 nodes

## Key Concepts

- **container_endpoints_basic.py** (64 connections) — `server/api/container_endpoints_basic.py`
- **TransferContainerRequest** (40 connections) — `server/api/container_models.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **get_container_service()** (26 connections) — `server/api/container_helpers.py`
- **container_events.py** (26 connections) — `server/api/container_events.py`
- **test_containers.py** (26 connections) — `server/tests/unit/api/test_containers.py`
- **test_player_schema_converter_weapon.py** (25 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_container_events.py** (24 connections) — `server/tests/unit/api/test_container_events.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **asyncio** (20 connections)
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **ConnectionManager** (18 connections)
- **asyncio** (17 connections)
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (16 connections) — `server/api/container_events.py`
- **container_models.py** (16 connections) — `server/api/container_models.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **test_container_endpoints_basic_weapon.py** (15 connections) — `server/tests/unit/api/test_container_endpoints_basic_weapon.py`
- **OpenContainerRequest** (14 connections) — `server/api/container_models.py`
- **_weapon_from_prototype_registry()** (14 connections) — `server/game/player_schema_converter.py`
- **get_current_user()** (13 connections) — `docs/examples/logging/fastapi_integration.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- *... and 315 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (80 shared connections)
- [ContainerComponent](ContainerComponent.md) (42 shared connections)
- [LootAllRequest](LootAllRequest.md) (25 shared connections)
- [get_logger](get_logger.md) (23 shared connections)
- [ConnectionManager](ConnectionManager.md) (9 shared connections)
- [ContainerService](ContainerService.md) (9 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (9 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (8 shared connections)
- [Stats](Stats.md) (7 shared connections)
- [container_helpers_inventory_ops.py](container_helpers_inventory_ops.py.md) (3 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (3 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/dependencies.py`
- `server/game/player_schema_converter.py`
- `server/main.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/services/container_service.py`
- `server/tests/fixtures/shared/weapon_metadata.py`
- `server/tests/unit/api/test_container_endpoints_basic_weapon.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_models.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 827 (94%)
- INFERRED: 55 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*