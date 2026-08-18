# equipment_service.py

> 55 nodes

## Key Concepts

- **equipment_service.py** (23 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (23 connections) — `server/tests/unit/services/test_equipment_service.py`
- **SlotValidationError** (21 connections) — `server/services/equipment_service.py`
- **EquipmentService** (18 connections) — `server/services/equipment_service.py`
- **EquipmentCapacityError** (11 connections) — `server/services/equipment_service.py`
- **.equip_from_inventory()** (10 connections) — `server/services/equipment_service.py`
- **.unequip_to_inventory()** (8 connections) — `server/services/equipment_service.py`
- **EquipmentServiceError** (6 connections) — `server/services/equipment_service.py`
- **_clone_equipped()** (6 connections) — `server/services/equipment_service.py`
- **_clone_inventory()** (6 connections) — `server/services/equipment_service.py`
- **InventoryStack** (5 connections)
- **_resolve_effective_equip_slot()** (4 connections) — `server/services/equipment_service.py`
- **equipment_service()** (4 connections) — `server/tests/unit/services/test_equipment_service.py`
- **inventory_service()** (4 connections) — `server/tests/unit/services/test_equipment_service.py`
- **Any** (4 connections)
- **._maybe_log_wearable_container_failure()** (3 connections) — `server/services/equipment_service.py`
- **test_equip_from_inventory_capacity_error()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_invalid_slot_index()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_no_slot_type()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_slot_mismatch()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_slot_type_inventory_requires_target_slot()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_unequip_to_inventory_capacity_error()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_unequip_to_inventory_empty_slot()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_unequip_to_inventory_no_slot_type()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- **test_equip_from_inventory_quantity_split()** (2 connections) — `server/tests/unit/services/test_equipment_service.py`
- *... and 30 more nodes in this community*

## Relationships

- [InventoryService](InventoryService.md) (12 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (8 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (5 shared connections)
- [command_service.py](command_service.py.md) (5 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (4 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (3 shared connections)
- [handle_unequip_command](handle_unequip_command.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/equipment_service.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 112 (86%)
- INFERRED: 18 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*