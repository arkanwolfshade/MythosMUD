# WearableContainerService

> 63 nodes

## Key Concepts

- **WearableContainerService** (28 connections) — `server/services/wearable_container_service.py`
- **get_shared_services()** (21 connections) — `server/commands/inventory_service_helpers.py`
- **wearable_container_service.py** (20 connections) — `server/services/wearable_container_service.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **Any** (15 connections)
- **UUID** (14 connections)
- **._load_player_wearable_container()** (9 connections) — `server/services/wearable_container_service.py`
- **_ensure_shared_services_initialized()** (8 connections) — `server/commands/inventory_service_helpers.py`
- **_filter_container_data()** (8 connections) — `server/services/wearable_container_service.py`
- **_get_enum_value()** (8 connections) — `server/services/wearable_container_service.py`
- **.handle_container_overflow()** (8 connections) — `server/services/wearable_container_service.py`
- **.handle_equip_wearable_container()** (8 connections) — `server/services/wearable_container_service.py`
- **.add_items_to_wearable_container()** (7 connections) — `server/services/wearable_container_service.py`
- **._update_container_items_or_raise()** (7 connections) — `server/services/wearable_container_service.py`
- **.update_wearable_container_items()** (7 connections) — `server/services/wearable_container_service.py`
- **.handle_unequip_wearable_container()** (6 connections) — `server/services/wearable_container_service.py`
- **._validate_inner_container_capacity()** (6 connections) — `server/services/wearable_container_service.py`
- **test_inventory_service_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **._create_equipment_container_record()** (5 connections) — `server/services/wearable_container_service.py`
- **._drop_overflow_to_ground()** (5 connections) — `server/services/wearable_container_service.py`
- **._find_existing_equipment_container()** (5 connections) — `server/services/wearable_container_service.py`
- **.get_wearable_containers_for_player()** (5 connections) — `server/services/wearable_container_service.py`
- **._save_overflow_inventory()** (5 connections) — `server/services/wearable_container_service.py`
- **._split_overflow_items()** (4 connections) — `server/services/wearable_container_service.py`
- **test_get_enum_value_with_enum()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- *... and 38 more nodes in this community*

## Relationships

- [inventory_equip_command.py](inventory_equip_command.py.md) (10 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (10 shared connections)
- [DatabaseError](DatabaseError.md) (9 shared connections)
- [container_helpers_inventory_find.py](container_helpers_inventory_find.py.md) (5 shared connections)
- [ContainerComponent](ContainerComponent.md) (5 shared connections)
- [InventoryService](InventoryService.md) (4 shared connections)
- [inventory_unequip_command.py](inventory_unequip_command.py.md) (4 shared connections)
- [test_look_player.py](test_look_player.py.md) (3 shared connections)
- [container_helpers_inventory_display.py](container_helpers_inventory_display.py.md) (3 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)

## Source Files

- `server/commands/inventory_service_helpers.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/commands/test_inventory_service_helpers.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 173 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*