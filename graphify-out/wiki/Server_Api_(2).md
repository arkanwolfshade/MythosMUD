# Server Api (2)

> 369 nodes

## Key Concepts

- **RateLimitError** (76 connections) — `server/exceptions.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **ErrorMessages** (45 connections) — `server/error_types.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **container.py** (25 connections) — `server/models/container.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (20 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestTransferItems** (20 connections) — `server/tests/unit/api/test_containers.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- *... and 344 more nodes in this community*

## Relationships

- [Server Api](Server_Api.md) (230 shared connections)
- [Server Admin](Server_Admin.md) (62 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (31 shared connections)
- [Server Models (9)](Server_Models_%289%29.md) (29 shared connections)
- [Server Services (43)](Server_Services_%2843%29.md) (15 shared connections)
- [Server Commands](Server_Commands.md) (14 shared connections)
- [Server Error Handlers (2)](Server_Error_Handlers_%282%29.md) (10 shared connections)
- [Server Api (4)](Server_Api_%284%29.md) (9 shared connections)
- [Server Models (22)](Server_Models_%2822%29.md) (7 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (6 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (6 shared connections)
- [Server Utils (3)](Server_Utils_%283%29.md) (6 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/models/container.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/services/container_websocket_events.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 1690 (84%)
- INFERRED: 329 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*