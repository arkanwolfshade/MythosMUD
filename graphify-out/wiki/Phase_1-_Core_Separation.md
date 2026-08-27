# Phase 1: Core Separation

> 23 nodes

## Key Concepts

- **asyncio** (48 connections)
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

- [asyncio](asyncio.md) (21 shared connections)
- [](unnamed.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [Visual Test Value Distribution](Visual_Test_Value_Distribution.md) (2 shared connections)
- [Deprecated get_async_persistence Global](Deprecated_get_async_persistence_Global.md) (2 shared connections)
- [Success Criteria](Success_Criteria.md) (2 shared connections)
- [authoritative_schema.sql](authoritative_schema.sql.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [4pt Spacing System](4pt_Spacing_System.md) (1 shared connections)
- [JSON Schema Validation](JSON_Schema_Validation.md) (1 shared connections)
- [Color and Contrast Reference](Color_and_Contrast_Reference.md) (1 shared connections)
- [ADR Structure (Status/Context/Decision)](ADR_Structure_Status-Context-Decision.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 79 (86%)
- INFERRED: 13 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*