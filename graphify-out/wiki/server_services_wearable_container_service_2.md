# server services wearable container service

> 22 nodes

## Key Concepts

- **WearableContainerServiceError** (18 connections) — `server/services/wearable_container_service.py`
- **Test update_wearable_container_items raises error when container not found.** (5 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_capacity_exceeded()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_not_found()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_update_fails()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_wrong_player()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_wrong_source_type()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_player_not_found()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_capacity_exceeded()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_creation_error()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_capacity_exceeded()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_not_found()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_update_fails()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_wrong_player()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_wrong_source_type()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test add_items_to_wearable_container raises error when capacity exceeded.** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Base exception for wearable container service operations.** (1 connections) — `server/services/wearable_container_service.py`
- **Test add_items_to_wearable_container raises error when container not found.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_container_overflow raises error when player not found.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_equip_wearable_container handles container creation error.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test add_items_to_wearable_container raises error when update fails.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_equip_wearable_container raises error when capacity exceeded.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (27 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (2 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 44 (77%)
- INFERRED: 13 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*