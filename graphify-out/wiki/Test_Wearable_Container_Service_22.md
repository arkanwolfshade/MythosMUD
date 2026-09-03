# Test Wearable Container Service

> 20 nodes

## Key Concepts

- **asyncio** (48 connections)
- **test_get_wearable_containers_for_player_filters_non_equipment()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_dict_items()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_wearable_containers_for_player()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_wearable_containers_for_player_empty()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_wearable_containers_for_player_multiple_containers()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_empty_overflow()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_inventory_full()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_existing_container_different_item_instance()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_existing_container_no_metadata()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_no_inner_container()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test get_wearable_containers_for_player returns containers.** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_equip_wearable_container when existing container has no metadata.** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test add_items_to_wearable_container adds items.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_container_overflow drops to ground when inventory full.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_equip_wearable_container returns None when no inner_container.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_container_overflow handles empty overflow list.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test get_wearable_containers_for_player filters out non-equipment containers.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test add_items_to_wearable_container handles dict items correctly.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`

## Relationships

- [Test Wearable Container Service](Test_Wearable_Container_Service.md) (48 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 70 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*