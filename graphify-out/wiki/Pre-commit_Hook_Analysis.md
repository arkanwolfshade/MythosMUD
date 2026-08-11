# Pre-commit Hook Analysis

> 28 nodes

## Key Concepts

- **WearableContainerServiceError** (25 connections) — `server/services/wearable_container_service.py`
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

- [Exploration Command Factories](Exploration_Command_Factories.md) (14 shared connections)
- [Schedule Service Loader](Schedule_Service_Loader.md) (7 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (1 shared connections)
- [Structured Concurrency Patterns](Structured_Concurrency_Patterns.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 45 (58%)
- INFERRED: 33 (42%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*