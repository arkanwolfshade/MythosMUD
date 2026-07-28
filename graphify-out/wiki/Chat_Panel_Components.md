# Chat Panel Components

> 135 nodes · cohesion 0.02

## Key Concepts

- **test_wearable_container_service.py** (62 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **WearableContainerServiceError** (22 connections) — `server/services/wearable_container_service.py`
- **_filter_container_data()** (9 connections) — `server/services/wearable_container_service.py`
- **_get_enum_value()** (9 connections) — `server/services/wearable_container_service.py`
- **Any** (8 connections)
- **.add_items_to_wearable_container()** (8 connections) — `server/services/wearable_container_service.py`
- **.update_wearable_container_items()** (8 connections) — `server/services/wearable_container_service.py`
- **UUID** (7 connections)
- **.handle_container_overflow()** (6 connections) — `server/services/wearable_container_service.py`
- **.handle_equip_wearable_container()** (6 connections) — `server/services/wearable_container_service.py`
- **.handle_unequip_wearable_container()** (6 connections) — `server/services/wearable_container_service.py`
- **.get_wearable_containers_for_player()** (5 connections) — `server/services/wearable_container_service.py`
- **.__init__()** (3 connections) — `server/services/wearable_container_service.py`
- **test_add_items_to_wearable_container_capacity_exceeded()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_not_found()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_update_fails()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_wrong_player()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_wrong_source_type()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_filter_container_data()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_enum_value_with_enum()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_enum_value_with_string()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_player_not_found()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_capacity_exceeded()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_creation_error()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_capacity_exceeded()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- *... and 110 more nodes in this community*

## Relationships

- [Commands Inventory Item](Commands_Inventory_Item.md) (16 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (4 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 320 (90%)
- INFERRED: 34 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*