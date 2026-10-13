# Community 311

> 54 nodes

## Key Concepts

- **equipment_helpers.py** (30 connections) — `server/commands/equipment_helpers.py`
- **test_equipment_helpers.py** (25 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **get_shared_services()** (13 connections) — `server/commands/inventory_service_helpers.py`
- **resolve_unequip_slot()** (12 connections) — `server/commands/equipment_helpers.py`
- **resolve_equip_item_index()** (11 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_equip()** (8 connections) — `server/commands/equipment_helpers.py`
- **_player()** (8 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **find_equipped_item_after_equip()** (7 connections) — `server/commands/equipment_helpers.py`
- **normalize_equipped_items()** (6 connections) — `server/commands/equipment_helpers.py`
- **test_inventory_service_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **handle_wearable_container_on_unequip()** (5 connections) — `server/commands/equipment_helpers.py`
- **normalize_inventory_slots()** (5 connections) — `server/commands/equipment_helpers.py`
- **_equip_stack_from_inventory_index()** (4 connections) — `server/commands/equipment_helpers.py`
- **test_handle_wearable_container_on_equip_creates()** (4 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_handle_wearable_container_on_equip_no_inner()** (4 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **InventoryStack** (4 connections)
- **_find_equipped_by_item_id()** (3 connections) — `server/commands/equipment_helpers.py`
- **reset_shared_inventory_services_for_tests()** (3 connections) — `server/commands/inventory_service_helpers.py`
- **test_resolve_equip_by_index()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_by_search_term()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_index_out_of_range()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_search_no_match()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **test_resolve_equip_usage()** (3 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **_request_with_persistence()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **reset_shared_inventory_services_autouse()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- *... and 29 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (12 shared connections)
- [Community 105](Community_105.md) (11 shared connections)
- [Community 131](Community_131.md) (2 shared connections)
- [Community 274](Community_274.md) (2 shared connections)
- [Community 235](Community_235.md) (2 shared connections)
- [Community 611](Community_611.md) (1 shared connections)
- [Community 258](Community_258.md) (1 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_service_helpers.py`
- `server/tests/unit/commands/test_equipment_helpers.py`
- `server/tests/unit/commands/test_inventory_service_helpers.py`

## Audit Trail

- EXTRACTED: 129 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*