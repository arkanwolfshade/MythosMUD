# test_wearable_container_service.py

> 39 nodes

## Key Concepts

- **test_wearable_container_service.py** (73 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **_persistence_row()** (6 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_equip_reuses_the_existing_row_found_through_metadata_json()** (6 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_items_awaits_update_container_and_raises_when_it_fails()** (6 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_equip_awaits_create_container_and_returns_its_id()** (5 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_wearable_containers_validates_real_rows()** (5 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_unequip_folds_the_real_rows_contents_into_inner_container()** (5 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_enum_value_with_enum()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **_backpack_stack()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_dict_items()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_filter_container_data()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_wearable_containers_for_player()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_wearable_containers_for_player_error()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_wearable_containers_for_player_multiple_containers()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_inventory_full()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_spilled_items_save_player()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_no_inner_container()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_unequip_wearable_container_preserves()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_wearable_container_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_wearable_container_service_init()** (2 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **UUID** (2 connections)
- **Unit tests for wearable container service. Tests the WearableContainerService…** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **create_container is async: unawaited, equipping a wearable container always…** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Re-equipping matches the row by metadata_json.item_instance_id instead of…** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Unequip finds the row by metadata_json and returns its items_json as…** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- *... and 14 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (39 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (15 shared connections)
- [WearableContainerService](WearableContainerService.md) (11 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [wearable_service](wearable_service.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_overflow_spills_into_a_real_players_json_backed_inventory](test_overflow_spills_into_a_real_players_json_backed_inventory.md) (1 shared connections)
- [test_handle_container_overflow](test_handle_container_overflow.md) (1 shared connections)
- [test_get_enum_value_with_string](test_get_enum_value_with_string.md) (1 shared connections)
- [test_handle_container_overflow_empty_overflow](test_handle_container_overflow_empty_overflow.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 113 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*