# inventory_unequip_command.py

> 89 nodes

## Key Concepts

- **inventory_unequip_command.py** (33 connections) — `server/commands/inventory_unequip_command.py`
- **test_equipment_service.py** (23 connections) — `server/tests/unit/services/test_equipment_service.py`
- **SlotValidationError** (21 connections) — `server/services/equipment_service.py`
- **get_shared_services()** (21 connections) — `server/commands/inventory_service_helpers.py`
- **EquipmentService** (18 connections) — `server/services/equipment_service.py`
- **handle_unequip_command()** (18 connections) — `server/commands/inventory_unequip_command.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **test_inventory_unequip_command.py** (13 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **EquipmentCapacityError** (11 connections) — `server/services/equipment_service.py`
- **.equip_from_inventory()** (10 connections) — `server/services/equipment_service.py`
- **_unequip_run_mutation()** (9 connections) — `server/commands/inventory_unequip_command.py`
- **_ensure_shared_services_initialized()** (8 connections) — `server/commands/inventory_service_helpers.py`
- **.unequip_to_inventory()** (8 connections) — `server/services/equipment_service.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- **test_handle_unequip_command_slot_validation_error()** (7 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_inventory_service_helpers.py** (7 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **EquipmentServiceError** (6 connections) — `server/services/equipment_service.py`
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **_clone_equipped()** (6 connections) — `server/services/equipment_service.py`
- **_clone_inventory()** (6 connections) — `server/services/equipment_service.py`
- **test_handle_unequip_command_mutation_suppressed()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_persist_rollback()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_success()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- **_mutation_cm()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- *... and 64 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (26 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (21 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (13 shared connections)
- [InventoryService](InventoryService.md) (8 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (5 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [WearableContainerService](WearableContainerService.md) (4 shared connections)
- [test_container_helpers_inventory_display.py](test_container_helpers_inventory_display.py.md) (3 shared connections)
- [.state](state.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [command_result_text](command_result_text.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/tests/unit/commands/test_inventory_service_helpers.py`
- `server/tests/unit/commands/test_inventory_unequip_command.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 229 (91%)
- INFERRED: 23 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*