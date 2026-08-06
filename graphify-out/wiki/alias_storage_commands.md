# alias storage commands

> 115 nodes

## Key Concepts

- **ContainerService** (104 connections) — `server/services/container_service.py`
- **test_container_service.py** (71 connections) — `server/tests/unit/services/test_container_service.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (18 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **EnvironmentalContainerLoader** (16 connections) — `server/services/environmental_container_loader.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **_container()** (15 connections) — `server/tests/unit/services/test_container_service.py`
- **conftest.py** (14 connections) — `server/tests/unit/api/conftest.py`
- **_stack()** (11 connections) — `server/tests/unit/services/test_container_service.py`
- **.test_transfer_all_items_from_container_capacity_error()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_success()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_transfer_error()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_multiple_items()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_item_without_quantity()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_partial_success()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_empty_items()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_updates_from_result()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_container()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_inventory()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **test_validate_corpse_grace_period_blocks_non_owner()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_capacity_exceeded()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **UUID** (4 connections)
- **test_validate_proximity_different_room_raises()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- *... and 90 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (60 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (21 shared connections)
- [task registry app](task_registry_app.md) (20 shared connections)
- [add used user](add_used_user.md) (9 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [player requests schemas](player_requests_schemas.md) (3 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/services/container_service.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 492 (87%)
- INFERRED: 71 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*