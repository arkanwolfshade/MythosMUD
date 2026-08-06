# player event handlers

> 296 nodes

## Key Concepts

- **ContainerComponent** (111 connections) — `server/models/container.py`
- **LootAllRequest** (57 connections) — `server/api/container_models.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **container.py** (32 connections) — `server/models/container.py`
- **ContainerSourceType** (30 connections) — `server/models/container.py`
- **container_events.py** (26 connections) — `server/api/container_events.py`
- **test_container_events.py** (25 connections) — `server/tests/unit/api/test_container_events.py`
- **test_container_helpers_loot.py** (22 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerLockState** (18 connections) — `server/models/container.py`
- **TestTransferAllItemsFromContainer** (18 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **container_service_access.py** (17 connections) — `server/services/container_service_access.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **test_container_events_loot.py** (16 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **emit_close_container_event()** (15 connections) — `server/api/container_events.py`
- **environmental_container_loader.py** (14 connections) — `server/services/environmental_container_loader.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestEmitTransferEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitCloseContainerEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **test_container_endpoints_loot.py** (12 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- *... and 271 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (50 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (45 shared connections)
- [Room Broadcast](Room_Broadcast.md) (42 shared connections)
- [Game Terminal UI](Game_Terminal_UI.md) (28 shared connections)
- [alias storage commands](alias_storage_commands.md) (23 shared connections)
- [add used user](add_used_user.md) (17 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (16 shared connections)
- [player preferences services](player_preferences_services.md) (14 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (8 shared connections)
- [task registry app](task_registry_app.md) (7 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (7 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/services/container_service_access.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/models/test_container.py`

## Audit Trail

- EXTRACTED: 1196 (92%)
- INFERRED: 108 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*