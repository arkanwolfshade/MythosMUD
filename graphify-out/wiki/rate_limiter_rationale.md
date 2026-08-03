# rate limiter rationale

> 28 nodes

## Key Concepts

- **WearableContainerServiceError** (22 connections) — `server/services/wearable_container_service.py`
- **test_handle_equip_wearable_container_capacity_exceeded()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_not_found()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_capacity_exceeded()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_player_not_found()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_creation_error()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_wrong_player()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_wrong_source_type()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_update_fails()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_not_found()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_capacity_exceeded()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_update_fails()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_wrong_player()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_wrong_source_type()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Base exception for wearable container service operations.** (1 connections) — `server/services/wearable_container_service.py`
- **Test handle_equip_wearable_container raises error when capacity exceeded.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test add_items_to_wearable_container raises error when container not found.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test add_items_to_wearable_container raises error when capacity exceeded.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_container_overflow raises error when player not found.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_equip_wearable_container handles container creation error.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test add_items_to_wearable_container raises error when container belongs to diff** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test add_items_to_wearable_container raises error when container is not equipmen** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test add_items_to_wearable_container raises error when update fails.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test update_wearable_container_items raises error when container not found.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test update_wearable_container_items raises error when capacity exceeded.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [wearable container service](wearable_container_service.md) (14 shared connections)
- [schedule services service](schedule_services_service.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 45 (60%)
- INFERRED: 30 (40%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*